import requests
import json
import re
from base64 import b64encode

user = "sabhya@urbansingapore.com"
password = "aHsH QIhY eO5j tKcS odCx eTOL"
token = b64encode(f"{user}:{password}".encode()).decode()
headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}

def strip(html):
    return re.sub(r'<[^>]+>', ' ', html).strip()

# ─── STEP 1: Get all pages ───────────────────────────────────────────────────
print("Fetching all pages...")
all_pages = []
page = 1
while True:
    r = requests.get(f"https://aarisehealthcare.com/wp-json/wp/v2/pages?per_page=100&page={page}", headers=headers)
    data = r.json()
    if r.status_code != 200 or not data:
        break
    all_pages.extend(data)
    page += 1
print(f"Total pages: {len(all_pages)}")

# Original product pages (no -2 suffix, research-compound in slug)
product_pages = [p for p in all_pages if
                 'research-compound' in p['slug'] and
                 not p['slug'].endswith('-2')]
print(f"Original product pages to fix: {len(product_pages)}")

# ─── STEP 2: Meta descriptions for product pages ─────────────────────────────
def make_product_meta(title, slug, content_html):
    title_clean = re.sub(r'&#\d+;|&[a-z]+;', '', title).strip()
    content = strip(content_html)

    # Extract CAS number if present
    cas_match = re.search(r'CAS[^\d]*(\d[\d\-]+)', content)
    cas = f" CAS {cas_match.group(1)}." if cas_match else ""

    # Extract category
    category = "research compound"
    if 'steroid' in slug or any(x in slug for x in ['testosterone','nandrolone','trenbolone','boldenone','oxandrolone','stanozolol','methandienone','oxymetholone','mesterolone']):
        category = "research steroid"
    elif 'peptide' in slug or any(x in slug for x in ['semaglutide','tirzepatide','bpc','igf','cjc','ipamorelin','ghrp','tb-500','epithalon','selank','dsip','aod']):
        category = "research peptide"
    elif 'hormone' in slug or any(x in slug for x in ['hcg','hgh','progesterone','estradiol','testosterone','insulin','igf']):
        category = "research hormone"
    elif 'sarm' in slug or any(x in slug for x in ['ostarine','ligandrol','rad-140','cardarine','andarine']):
        category = "SARM"

    name = title_clean.replace('Buy ', '').replace(' Research Compound', '').replace(' — 99% Purity | Aarise Healthcare', '').strip()
    return f"Buy {name} {category} — 99%+ purity, independent COA.{cas} Pharma-grade, ships from India. Research use only."[:155]

success = 0
fail = 0
for p in product_pages:
    meta = make_product_meta(p['title']['rendered'], p['slug'], p['content']['rendered'])
    payload = json.dumps({"meta": {"_yoast_wpseo_metadesc": meta}})
    r = requests.post(
        f"https://aarisehealthcare.com/wp-json/wp/v2/pages/{p['id']}",
        headers=headers,
        data=payload.encode("utf-8")
    )
    if r.status_code == 200:
        success += 1
    else:
        fail += 1
        print(f"  FAIL {p['id']}: {r.text[:100]}")
    if success % 50 == 0 and success > 0:
        print(f"  ...{success} product pages done")

print(f"Product page meta done: {success} success, {fail} failed")

# ─── STEP 3: FAQ schema on all supplier/buy posts ───────────────────────────
print("\nFetching all posts for FAQ schema...")
all_posts = []
page = 1
while True:
    r = requests.get(f"https://aarisehealthcare.com/wp-json/wp/v2/posts?per_page=100&page={page}", headers=headers)
    data = r.json()
    if r.status_code != 200 or not data:
        break
    all_posts.extend(data)
    page += 1

# Supplier and buy posts that don't have FAQ schema yet
supplier_posts = [p for p in all_posts if
                  any(x in p['slug'] for x in ['supplier','buy-research','catalog']) and
                  'application/ld+json' not in p['content']['rendered']]

print(f"Posts needing FAQ schema: {len(supplier_posts)}")

def get_country(slug):
    for c in ['paraguay','peru','mexico','us']:
        if c in slug:
            return c.upper() if c == 'us' else c.capitalize()
    return 'your region'

def get_compound_type(slug):
    if 'peptide' in slug: return 'peptides'
    if 'steroid' in slug: return 'steroid compounds'
    if 'hormone' in slug: return 'hormone compounds'
    if 'pharma' in slug: return 'pharma-grade compounds'
    return 'research compounds'

def make_faq_schema(country, compound_type):
    return f"""
<!-- wp:html -->
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{{"@type":"Question","name":"What {compound_type} are available for {country}?","acceptedAnswer":{{"@type":"Answer","text":"Aarise Healthcare supplies a full range of {compound_type} for {country} including peptides, steroids, hormones, and SARMs. All compounds are 99%+ purity verified by independent HPLC testing with full Certificate of Analysis (COA)."}} }},
{{"@type":"Question","name":"How long does shipping to {country} take?","acceptedAnswer":{{"@type":"Answer","text":"Research compound orders to {country} typically arrive within 7-12 business days via DHL or FedEx international express from India. All shipments include tracking and customs documentation."}} }},
{{"@type":"Question","name":"Do you provide a Certificate of Analysis (COA) for {country} orders?","acceptedAnswer":{{"@type":"Answer","text":"Yes. Every order shipped to {country} includes a full independent third-party Certificate of Analysis confirming compound identity, purity (99%+), and absence of heavy metals and residual solvents."}} }},
{{"@type":"Question","name":"What is the minimum order quantity for {country}?","acceptedAnswer":{{"@type":"Answer","text":"Aarise Healthcare supplies {compound_type} for {country} starting from single research quantities up to bulk wholesale. Contact us for pricing based on your requirements."}} }}
]}}
</script>
<!-- /wp:html -->"""

faq_success = 0
faq_fail = 0
for p in supplier_posts:
    country = get_country(p['slug'])
    compound_type = get_compound_type(p['slug'])
    faq = make_faq_schema(country, compound_type)
    new_content = p['content']['rendered'] + faq

    payload = json.dumps({"content": new_content})
    r = requests.post(
        f"https://aarisehealthcare.com/wp-json/wp/v2/posts/{p['id']}",
        headers=headers,
        data=payload.encode("utf-8")
    )
    if r.status_code == 200:
        faq_success += 1
    else:
        faq_fail += 1

print(f"FAQ schema done: {faq_success} success, {faq_fail} failed")

# ─── STEP 4: Noindex WooCommerce system pages ────────────────────────────────
print("\nNoindexing WooCommerce system pages...")
woo_slugs = ['cart','checkout','my-account','order-received','shop','wishlist','terms','privacy-policy','refund-policy']
woo_pages = [p for p in all_pages if p['slug'] in woo_slugs]
print(f"WooCommerce system pages found: {len(woo_pages)}")

woo_success = 0
for p in woo_pages:
    payload = json.dumps({"meta": {"_yoast_wpseo_meta-robots-noindex": "1"}})
    r = requests.post(
        f"https://aarisehealthcare.com/wp-json/wp/v2/pages/{p['id']}",
        headers=headers,
        data=payload.encode("utf-8")
    )
    if r.status_code == 200:
        woo_success += 1
        print(f"  Noindexed: {p['slug']}")

print(f"WooCommerce noindex done: {woo_success}/{len(woo_pages)}")

print("\n=== ALL DONE ===")
print(f"- Meta descriptions: {success} product pages")
print(f"- FAQ schema: {faq_success} supplier posts")
print(f"- Noindexed WooCommerce: {woo_success} system pages")
