import requests
import json
from base64 import b64encode

user = "sabhya@urbansingapore.com"
password = "aHsH QIhY eO5j tKcS odCx eTOL"
token = b64encode(f"{user}:{password}".encode()).decode()
headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}

def make_content(country, regulator, shipping_days, reg_detail):
    return f"""<!-- wp:paragraph -->
<p><strong>Aarise Healthcare</strong> is a pharma-grade research compound supplier for {country}, shipping directly from India with independent Certificate of Analysis (COA) documentation on every order. We supply research-grade peptides, steroids, hormones, SARMs, and GLP-1 compounds to laboratories, clinics, and research institutions across {country}.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>What Are Research Compounds?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Research compounds are high-purity chemical substances supplied exclusively for laboratory and scientific research purposes. They are not approved for human consumption. Each compound is independently verified for identity, purity (99%+), and absence of heavy metals and residual solvents before shipment.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Research Compound Categories Available for {country}</h2>
<!-- /wp:heading -->

<!-- wp:heading {{"level":3}} -->
<h3>Peptides</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul><li>BPC-157 — tissue repair and gut research</li><li>TB-500 — wound healing and recovery studies</li><li>Semaglutide — GLP-1 receptor agonist research</li><li>Tirzepatide — dual GIP/GLP-1 agonist research</li><li>CJC-1295 with DAC — growth hormone secretagogue</li><li>Ipamorelin — GHRP research</li><li>IGF-1 LR3 — growth factor research</li><li>Epithalon — telomerase and anti-aging research</li></ul>
<!-- /wp:list -->

<!-- wp:heading {{"level":3}} -->
<h3>Steroids</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul><li>Testosterone Enanthate — androgen research</li><li>Testosterone Cypionate — hormone replacement studies</li><li>Nandrolone Decanoate — anabolic pathway research</li><li>Boldenone Undecylenate — performance research</li><li>Trenbolone Acetate — receptor binding studies</li><li>Oxandrolone — lean tissue research</li></ul>
<!-- /wp:list -->

<!-- wp:heading {{"level":3}} -->
<h3>Hormones</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul><li>Human Growth Hormone (HGH) — somatotropin research</li><li>HCG (Human Chorionic Gonadotropin) — gonadotropin studies</li><li>Progesterone — reproductive hormone research</li><li>Estradiol — estrogen pathway studies</li></ul>
<!-- /wp:list -->

<!-- wp:heading {{"level":3}} -->
<h3>SARMs</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul><li>Ostarine (MK-2866) — muscle and bone research</li><li>Ligandrol (LGD-4033) — anabolic pathway studies</li><li>RAD-140 — neuroprotective SARM research</li><li>Cardarine (GW-501516) — metabolic and endurance research</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Certificate of Analysis (COA) — What It Means</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Every research compound shipped to {country} includes a full Certificate of Analysis (COA) from an independent third-party laboratory. The COA confirms compound identity verified by HPLC and mass spectrometry, purity of 99%+ confirmed, heavy metals below detection threshold, residual solvents absent, and a batch number traceable to the production record.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Shipping Research Compounds to {country}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We ship research compounds from India to {country} via DHL and FedEx international express. Typical delivery time is {shipping_days} business days. All shipments include tracking, discreet packaging, and full documentation for customs clearance. Bulk and wholesale pricing is available for laboratories and institutions ordering larger quantities.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Regulatory Information for {country}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{reg_detail}</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Frequently Asked Questions</h2>
<!-- /wp:heading -->

<!-- wp:heading {{"level":3}} -->
<h3>What are research compounds used for in {country}?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Research compounds in {country} are used by licensed laboratories, universities, and medical research institutions for in-vitro and pre-clinical studies. They are not for human or veterinary use and are supplied with full COA documentation.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3>What is a COA and why does it matter?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>A Certificate of Analysis (COA) is a document from an independent laboratory confirming a compound's identity, purity, and absence of contaminants. Aarise Healthcare provides third-party COA with every order shipped to {country}.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3>How long does shipping to {country} take?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Research compound orders to {country} typically arrive within {shipping_days} business days via DHL or FedEx international express from India. All shipments are tracked and include customs documentation.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3>What is the minimum order quantity?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Aarise Healthcare supplies research compounds starting from single vials up to bulk wholesale quantities for institutions. Contact us for pricing based on your specific research requirements.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3>Are the compounds pharma grade?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Yes. All compounds are manufactured to pharma-grade standards with 99%+ purity verified by independent HPLC testing, produced in GMP-compliant facilities with full documentation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Ready to order?</strong> Contact Aarise Healthcare -- your trusted research compound supplier for {country} from India, with full COA documentation and reliable international shipping.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"What are research compounds used for in {country}?","acceptedAnswer":{{"@type":"Answer","text":"Research compounds in {country} are used by licensed laboratories, universities, and medical research institutions for in-vitro and pre-clinical studies. They are not for human or veterinary use and are supplied with full COA documentation."}}}},{{"@type":"Question","name":"What is a COA and why does it matter for research compounds?","acceptedAnswer":{{"@type":"Answer","text":"A Certificate of Analysis (COA) is a document from an independent laboratory confirming a compound identity, purity, and absence of contaminants. Aarise Healthcare provides third-party COA with every research compound order shipped to {country}."}}}},{{"@type":"Question","name":"How long does shipping research compounds to {country} take?","acceptedAnswer":{{"@type":"Answer","text":"Research compound orders to {country} typically arrive within {shipping_days} business days via DHL or FedEx from India. All shipments are tracked and include customs documentation."}}}},{{"@type":"Question","name":"Are Aarise Healthcare research compounds pharma grade?","acceptedAnswer":{{"@type":"Answer","text":"Yes. All compounds are manufactured to pharma-grade standards with 99%+ purity verified by independent HPLC testing, produced in GMP-compliant facilities with full documentation."}}}}]}}
</script>
<!-- /wp:html -->"""

pages = [
    {
        "id": 1004959,
        "country": "Peru",
        "regulator": "DIGEMID",
        "shipping_days": "8-12",
        "reg_detail": "In Peru, research compounds classified as Research Use Only (RUO) are regulated by <strong>DIGEMID</strong> (Direccion General de Medicamentos, Insumos y Drogas). RUO compounds supplied for laboratory research purposes do not follow the same pharmaceutical registration pathway as drugs intended for human use. Aarise Healthcare provides full COA and supplier documentation with every shipment to support customs clearance.",
        "meta_desc": "Pharma-grade research compounds supplier for Peru. Peptides, steroids, hormones and SARMs shipped from India with independent COA. DIGEMID-compliant documentation. 8-12 day DHL/FedEx delivery."
    },
    {
        "id": 1004955,
        "country": "Mexico",
        "regulator": "COFEPRIS",
        "shipping_days": "7-10",
        "reg_detail": "In Mexico, research compounds are regulated by <strong>COFEPRIS</strong> (Comision Federal para la Proteccion contra Riesgos Sanitarios). Research Use Only (RUO) compounds supplied for laboratory research are distinct from pharmaceutical products for human use. Aarise Healthcare provides full COA documentation and supplier records with every shipment to Mexico to support customs and regulatory compliance.",
        "meta_desc": "Pharma-grade research compounds supplier for Mexico. Peptides, steroids, hormones and SARMs shipped from India with independent COA. COFEPRIS-compliant documentation. 7-10 day DHL/FedEx delivery."
    },
    {
        "id": 1004967,
        "country": "the US",
        "regulator": "FDA",
        "shipping_days": "5-8",
        "reg_detail": "In the United States, research compounds sold as Research Use Only (RUO) are regulated by the <strong>FDA</strong>. RUO compounds are legal to purchase for legitimate laboratory research and are not intended for human or veterinary use. Aarise Healthcare provides independent third-party COA documentation with every shipment confirming purity, identity, and absence of contaminants.",
        "meta_desc": "Pharma-grade research compounds supplier for the US. Peptides, steroids, hormones and SARMs shipped from India with independent COA. FDA RUO compliant documentation. 5-8 day DHL/FedEx delivery."
    }
]

for p in pages:
    content = make_content(p["country"], p["regulator"], p["shipping_days"], p["reg_detail"])
    payload = {
        "content": content,
        "meta": {
            "_yoast_wpseo_metadesc": p["meta_desc"],
        }
    }
    r = requests.post(
        f"https://aarisehealthcare.com/wp-json/wp/v2/posts/{p['id']}",
        headers=headers,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8")
    )
    status = r.json().get('link', r.text[:100])
    print(f"{p['country']}: {r.status_code} — {status}")
