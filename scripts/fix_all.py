import requests
import json
import re
import time
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

# ─── STEP 2: Noindex all -2 duplicate pages ──────────────────────────────────
dupes = [p for p in all_pages if p['slug'].endswith('-2') and 'research-compound' in p['slug']]
print(f"\nNoindexing {len(dupes)} duplicate pages...")

success = 0
fail = 0
for p in dupes:
    payload = json.dumps({
        "meta": {
            "_yoast_wpseo_meta-robots-noindex": "1",
            "_yoast_wpseo_meta-robots-nofollow": "1"
        }
    })
    r = requests.post(
        f"https://aarisehealthcare.com/wp-json/wp/v2/pages/{p['id']}",
        headers=headers,
        data=payload.encode("utf-8")
    )
    if r.status_code == 200:
        success += 1
    else:
        fail += 1
    if success % 50 == 0 and success > 0:
        print(f"  ...{success} done")

print(f"Noindex done: {success} success, {fail} failed")

# ─── STEP 3: Get all posts ───────────────────────────────────────────────────
print("\nFetching all posts...")
all_posts = []
page = 1
while True:
    r = requests.get(f"https://aarisehealthcare.com/wp-json/wp/v2/posts?per_page=100&page={page}", headers=headers)
    data = r.json()
    if r.status_code != 200 or not data:
        break
    all_posts.extend(data)
    page += 1
print(f"Total posts: {len(all_posts)}")

# ─── STEP 4: Generate + push meta descriptions for all posts ─────────────────
print(f"\nAdding meta descriptions to {len(all_posts)} posts...")

def make_meta(title, slug, content_text):
    title = re.sub(r'&#\d+;|&amp;|&[a-z]+;', ' ', title).strip()
    content_text = strip(content_text)[:300]

    # Country-specific supplier pages
    for country, reg in [("Paraguay","DINAVISA"), ("Peru","DIGEMID"), ("Mexico","COFEPRIS"), ("US","FDA"), ("the US","FDA")]:
        c = country.lower().replace("the ","")
        if c in slug:
            if "peptide" in slug:
                return f"Buy research peptides for {country} — BPC-157, Semaglutide, TB-500 and more. Pharma-grade, 99%+ purity, independent COA. Ships from India via DHL/FedEx."
            elif "steroid" in slug:
                return f"Buy research steroid compounds for {country} — Testosterone, Nandrolone, Trenbolone and more. 99%+ purity with independent COA. Ships from India."
            elif "hormone" in slug:
                return f"Buy research hormone compounds for {country} — HGH, HCG, Progesterone and more. Pharma-grade, 99%+ purity, independent COA. Ships from India via DHL."
            elif "pharma" in slug:
                return f"Buy pharma-grade research compounds for {country}. Full product catalog with COA, HPLC verified purity 99%+. Ships from India via DHL/FedEx."
            elif "supplier" in slug:
                return f"Pharma-grade research compound supplier for {country}. Peptides, steroids, hormones and SARMs with independent COA. Reliable shipping from India."
            elif "catalog" in slug:
                return f"Research compound catalog for {country} — full specifications, CAS numbers, purity data and applications. Sourced from India with independent COA."
            elif "guide" in slug:
                return f"Research compounds guide for {country} — compound categories, regulatory information, purity standards and how to order from India with COA."

    # Research guide pages
    if "epithalon" in slug:
        return "Epithalon peptide research guide — telomerase activation, anti-aging studies, dosing protocols and handling. 99%+ purity available with independent COA."
    if "ostarine" in slug or "mk-2866" in slug:
        return "Ostarine (MK-2866) research guide — mechanism of action, muscle and bone studies, purity standards and handling. Research-grade SARMs with COA."
    if "semaglutide" in slug:
        return "Semaglutide research guide — GLP-1 receptor agonist mechanism, studies, purity standards. Research-grade semaglutide with independent COA from India."
    if "tirzepatide" in slug:
        return "Tirzepatide research guide — dual GIP/GLP-1 agonist mechanism, studies, handling. 99%+ purity research-grade tirzepatide with independent COA."
    if "bpc-157" in slug or "bpc157" in slug:
        return "BPC-157 research guide — tissue repair mechanism, gut studies, handling and storage. 99%+ purity research-grade BPC-157 with independent COA from India."

    # Generic fallback using title
    clean_title = title[:80]
    return f"{clean_title} — pharma-grade, 99%+ purity with independent Certificate of Analysis (COA). Research use only. Ships from India."

post_success = 0
post_fail = 0
for p in all_posts:
    title = p['title']['rendered']
    slug = p['slug']
    content = p['content']['rendered']
    meta_desc = make_meta(title, slug, content)[:155]

    payload = json.dumps({
        "meta": {
            "_yoast_wpseo_metadesc": meta_desc
        }
    })
    r = requests.post(
        f"https://aarisehealthcare.com/wp-json/wp/v2/posts/{p['id']}",
        headers=headers,
        data=payload.encode("utf-8")
    )
    if r.status_code == 200:
        post_success += 1
    else:
        post_fail += 1
        print(f"  FAIL {p['id']}: {r.text[:100]}")

    if post_success % 20 == 0 and post_success > 0:
        print(f"  ...{post_success} posts done")

print(f"Meta descriptions done: {post_success} success, {post_fail} failed")

# ─── STEP 5: Noindex original product pages too (500 thin product pages) ────
print("\nFetching original product pages to noindex...")
orig_dupes = [p for p in all_pages if
              'research-compound' in p['slug'] and
              not p['slug'].endswith('-2') and
              len(p['content']['rendered']) < 3000]

print(f"Thin original product pages: {len(orig_dupes)}")
# Don't noindex originals - they are the canonical versions
# Just report
print("Keeping originals as-is (canonical versions)")

print("\n=== ALL DONE ===")
print(f"- Noindexed {success} duplicate -2 pages")
print(f"- Added meta descriptions to {post_success} posts")
