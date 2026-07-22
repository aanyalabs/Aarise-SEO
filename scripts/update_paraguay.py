import requests
import json
from base64 import b64encode

user = "sabhya@urbansingapore.com"
password = "aHsH QIhY eO5j tKcS odCx eTOL"
token = b64encode(f"{user}:{password}".encode()).decode()
headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}

content = """<!-- wp:paragraph -->
<p><strong>Aarise Healthcare</strong> is a pharma-grade research compound supplier for Paraguay, shipping directly from India with independent Certificate of Analysis (COA) documentation on every order. We supply research-grade peptides, steroids, hormones, SARMs, and GLP-1 compounds to laboratories, clinics, and research institutions across Paraguay.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>What Are Research Compounds?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Research compounds are high-purity chemical substances supplied exclusively for laboratory and scientific research purposes. They are not approved for human consumption. Each compound is independently verified for identity, purity (99%+), and absence of heavy metals and residual solvents before shipment.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Research Compound Categories Available for Paraguay</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3>Peptides</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul><li>BPC-157 — tissue repair and gut research</li><li>TB-500 — wound healing and recovery studies</li><li>Semaglutide — GLP-1 receptor agonist research</li><li>Tirzepatide — dual GIP/GLP-1 agonist research</li><li>CJC-1295 with DAC — growth hormone secretagogue</li><li>Ipamorelin — GHRP research</li><li>IGF-1 LR3 — growth factor research</li><li>Epithalon — telomerase and anti-aging research</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3>Steroids</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul><li>Testosterone Enanthate — androgen research</li><li>Testosterone Cypionate — hormone replacement studies</li><li>Nandrolone Decanoate — anabolic pathway research</li><li>Boldenone Undecylenate — performance research</li><li>Trenbolone Acetate — receptor binding studies</li><li>Oxandrolone — lean tissue research</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3>Hormones</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul><li>Human Growth Hormone (HGH) — somatotropin research</li><li>HCG (Human Chorionic Gonadotropin) — gonadotropin studies</li><li>Progesterone — reproductive hormone research</li><li>Estradiol — estrogen pathway studies</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3>SARMs</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul><li>Ostarine (MK-2866) — muscle and bone research</li><li>Ligandrol (LGD-4033) — anabolic pathway studies</li><li>RAD-140 — neuroprotective SARM research</li><li>Cardarine (GW-501516) — metabolic and endurance research</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Certificate of Analysis (COA) — What It Means</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Every research compound shipped to Paraguay includes a full Certificate of Analysis (COA) from an independent third-party laboratory. The COA confirms compound identity verified by HPLC and mass spectrometry, purity of 99%+ confirmed, heavy metals below detection threshold, residual solvents absent, and a batch number traceable to the production record.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Shipping Research Compounds to Paraguay</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We ship research compounds from India to Paraguay via DHL and FedEx international express. Typical delivery time is 8-12 business days. All shipments include tracking, discreet packaging, and full documentation for customs clearance. Bulk and wholesale pricing is available for laboratories and institutions ordering larger quantities.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Regulatory Information for Paraguay</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In Paraguay, research compounds classified as Research Use Only (RUO) are regulated by <strong>DINAVISA</strong> (Direccion Nacional de Vigilancia Sanitaria). RUO compounds supplied for laboratory research are distinct from pharmaceutical drugs and do not require the same registration pathway. All orders should be accompanied by documentation confirming research purpose. Aarise Healthcare provides full COA and supplier documentation with every shipment.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Frequently Asked Questions</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3>What are research compounds used for in Paraguay?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Research compounds in Paraguay are used by licensed laboratories, universities, and medical research institutions for in-vitro and pre-clinical studies. They are not for human or veterinary use and are supplied with full COA documentation.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>What is a COA and why does it matter?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>A Certificate of Analysis (COA) is a document from an independent laboratory confirming a compound's identity, purity, and absence of contaminants. For research compounds, a COA is essential proof that what you ordered is what you received at the stated purity level. Aarise Healthcare provides third-party COA with every order.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>How long does shipping to Paraguay take?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Research compound orders to Paraguay typically arrive within 8-12 business days via DHL or FedEx international express from India. All shipments are tracked and include customs documentation.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>What is the minimum order quantity?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Aarise Healthcare supplies research compounds in research quantities starting from single vials, as well as bulk and wholesale quantities for institutions. Contact us for pricing based on your research requirements.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Are the compounds pharma grade?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Yes. All compounds are manufactured to pharma-grade standards with 99%+ purity verified by independent HPLC testing. They are produced in GMP-compliant facilities and supplied with full documentation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Ready to order?</strong> Contact Aarise Healthcare -- your trusted research compound supplier for Paraguay from India, with full COA documentation and reliable international shipping.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What are research compounds used for in Paraguay?","acceptedAnswer":{"@type":"Answer","text":"Research compounds in Paraguay are used by licensed laboratories, universities, and medical research institutions for in-vitro and pre-clinical studies. They are not for human or veterinary use and are supplied with full COA documentation."}},{"@type":"Question","name":"What is a COA and why does it matter for research compounds?","acceptedAnswer":{"@type":"Answer","text":"A Certificate of Analysis (COA) is a document from an independent laboratory confirming a compound's identity, purity, and absence of contaminants. Aarise Healthcare provides third-party COA with every research compound order shipped to Paraguay."}},{"@type":"Question","name":"How long does shipping research compounds to Paraguay take?","acceptedAnswer":{"@type":"Answer","text":"Research compound orders to Paraguay typically arrive within 8-12 business days via DHL or FedEx international express from India. All shipments are tracked and include customs documentation."}},{"@type":"Question","name":"What is the minimum order for research compounds shipped to Paraguay?","acceptedAnswer":{"@type":"Answer","text":"Aarise Healthcare supplies research compounds starting from single vials up to bulk wholesale quantities for institutions. Contact us for pricing based on your specific research requirements."}},{"@type":"Question","name":"Are Aarise Healthcare research compounds pharma grade?","acceptedAnswer":{"@type":"Answer","text":"Yes. All compounds are manufactured to pharma-grade standards with 99%+ purity verified by independent HPLC testing, produced in GMP-compliant facilities with full documentation."}}]}
</script>
<!-- /wp:html -->"""

meta_desc = "Pharma-grade research compounds supplier for Paraguay. Peptides, steroids, hormones and SARMs shipped from India with independent COA. 8-12 day delivery via DHL/FedEx."

payload = {
    "content": content,
    "title": "Research Compounds Supplier for Paraguay — Pharma Grade with COA | Aarise Healthcare",
    "meta": {
        "_yoast_wpseo_metadesc": meta_desc,
        "_yoast_wpseo_title": "Research Compounds Supplier for Paraguay — Pharma Grade with COA | Aarise Healthcare"
    }
}

r = requests.post(
    "https://aarisehealthcare.com/wp-json/wp/v2/posts/1004963",
    headers=headers,
    data=json.dumps(payload, ensure_ascii=False).encode("utf-8")
)
print(f"Paraguay: {r.status_code} — {r.json().get('link', r.text[:200])}")
