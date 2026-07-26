---
name: seo-aarise-context
description: "Full SEO project context for Aarise Pharmaceuticals and Aarise Healthcare — what's been done, what's broken, what to do next. Read this at the start of any Aarise SEO session."
metadata: 
  node_type: memory
  type: project
  originSessionId: 02e29f80-db1d-4559-9450-840ab8a34f89
  modified: 2026-07-26T09:50:47.044Z
---

# Aarise SEO Project — Full Context

**Client:** LynqLeads / Rishikesh Sawant  
**Contact person:** Sabhya (handles WordPress admin, installs plugins etc.)  
**Our contact:** Priyansh Arora, Aanya Labs  
**Client email contact:** marketing@invinciblegg.com  
**Last updated:** July 26, 2026

---

## Two Sites

### 1. Aarise Pharma
- URL: aarisepharma.com
- WordPress site
- **What they sell:** Bulk pharmaceutical APIs, dispersible tablet contract manufacturing, third party pharma manufacturing
- **Target buyers:** B2B procurement managers at pharma companies in USA, Mexico, Brazil, Germany, South Korea, etc.
- **Current SEO status:** Ranking well for Indian informational keywords (dispersible tablets, dispersible tablet uses) — NOT yet ranking for international buyer-intent keywords

### 2. Aarise Healthcare
- URL: aarisehealthcare.com  
- WordPress + WooCommerce site
- **What they sell:** Research compounds — peptides, steroids, hormones (Tirzepatide, Semaglutide, BPC-157 etc.)
- **Target buyers:** Research labs, individual researchers
- **Current SEO status:** Early stage, average position 45.4 (improved from 62.7), "research compound" at position 7.8 (Page 1)

---

## WordPress API Credentials
See [[project_aarise_credentials]] for WP REST API credentials for both sites.

---

## GSC / GA4 Data — June 2026 Report Period (Jun 20 – Jul 22, 2026)

### Aarise Pharma GSC
- Clicks: 439 (+44 MoM)
- Impressions: 59,628 (+9,756, +20% MoM)
- CTR: 0.74%
- Avg Position: 6.1 (was 5.3 — position dropped slightly as more keywords entered index)
- Keywords tracked: 1,340
- Page 1 keywords: 800 (60%)
- Top keyword: "dispersible tablets" — 10,762 impressions, 43 clicks, pos 4.0
- Branded CTR: "aarise pharmaceuticals" at 50.6% CTR, pos 1.0
- GA4: 986 organic sessions, 4,094 direct, **16 AI Assistant sessions** (first time this channel appeared — ChatGPT/Gemini/Perplexity citing the site)

### Aarise Healthcare GSC
- Clicks: 0
- Impressions: 655 (+81, +14% MoM)
- Avg Position: 45.4 (was 62.7 — 17 position improvement, biggest MoM gain ever)
- Keywords tracked: 269
- Page 1: 6 keywords. Page 2: 9 keywords
- Top keyword: "research compounds" — 179 impressions, pos 15.3
- "research compound" at pos 7.8 (Page 1), "aarise" at pos 9.6 (Page 1)
- GA4: 232 active users, 138s avg engagement time (exceptional), 13 checkout views (5.6% checkout rate)

---

## Technical Work Completed (Healthcare)

| Fix | Pages | Impact |
|---|---|---|
| Duplicate pages noindexed ("-2" suffix) | 286 | Consolidates ranking signals |
| Meta descriptions added — posts | 91 | CTR improvement |
| Meta descriptions added — product pages | 293 | Keyword-targeted copy |
| FAQ schema — supplier posts | 42 | AI Overview eligibility |
| Country pages rewritten (Paraguay, Peru, Mexico, US) | 4 | 200→800+ words + FAQ schema |
| WooCommerce system pages noindexed | 5 | Crawl budget reclaimed |
| llms.txt published | 1 | Live at aarisehealthcare.com/llms.txt |

---

## llms.txt Status

- **Healthcare:** LIVE at aarisehealthcare.com/llms.txt — implemented via Code Snippets plugin (snippet ID 37), PHP intercept method
- **Pharma:** BLOCKED — Sabhya needs to install Code Snippets plugin on aarisepharma.com. File content is ready, just needs the plugin installed and snippet created.

---

## Monthly Reports Generated

Two separate DOCX files generated via Python (python-docx):

- `C:\Users\priya\Downloads\Aarise_Pharma_SEO_Monthly_Report_June_2026.docx`
- `C:\Users\priya\Downloads\Aarise_Healthcare_SEO_Monthly_Report_June_2026.docx`

Generation script: `C:\Users\priya\AppData\Local\Temp\claude\d--stak\02e29f80-db1d-4559-9450-840ab8a34f89\scratchpad\split_reports.py`

**Report format reference:** Two previous weekly DOCX reports were used as format reference:
- `C:\Users\priya\Downloads\Aarise_Healthcare_SEO_Report_Week3_May_2026 (1) (1).docx`
- `C:\Users\priya\Downloads\Aarise_Pharma_SEO_Report_Week3_May_2026 (1) (1).docx`

**Sections the weekly report has that monthly is MISSING (needs to be added next time):**
- Device breakdown (Mobile/Desktop/Tablet from GSC)
- Top Countries (GSC)
- Top Cities (GA4)
- Key Events (GA4 — form_start, form_submit)
- Blog Posts Published This Month (list with titles and target keywords)
- Cumulative Blog Summary (running total of posts published)
- Target Keyword Strategy / Clusters
- Next Month Blog Plan

---

## Competitors (Aarise Pharma)

31 competitors identified by client, including:
- **Big players:** Dr. Reddy's, Aurobindo Pharma, Sun Pharma, Divi's Laboratories, Laurus Labs, Neuland Laboratories, Hetero
- **Mid-tier:** Granules India, Concord Biotech, Sai Life Sciences, Shilpa Medicare, Syngene International, Aragen Life Sciences
- **Small/niche:** Avik Pharmaceutical, Natural Biogenex, Century Pharma, Cerata Pharmaceuticals, Brichem Sciences, Symbiotec Pharmalab, Global Calcium, etc.

**All these competitors are active in:** USA, Mexico, Peru, Brazil, Colombia, Chile, Argentina, Guatemala, Ecuador, Spain, Germany, Poland, Turkey, South Korea, Vietnam, Canada, Russia, Netherlands

---

## Core SEO Problem (Critical to Understand)

**The client is getting zero leads from international markets. Here's why:**

Current rankings are for Indian informational keywords — people searching "what is dispersible tablets" are students/doctors/patients in India, NOT bulk buyers in USA or Germany.

**Wrong keywords being targeted:**
- dispersible tablets ✗ (informational, Indian audience)
- what is dispersible tablets ✗ (informational)

**Right keywords to target (buyer intent, international):**
- "dispersible tablet manufacturer India export"
- "WHO GMP certified API supplier India"
- "bulk API manufacturer India [country]"
- "pharmaceutical contract manufacturer India MOQ"
- "API supplier India FDA approved"
- "[molecule name] API manufacturer India" (one per product)

**Why 1000 blogs won't work:** Google's Helpful Content Update penalizes thin content at scale. Quality over quantity — 10 strong pages beat 1000 mediocre ones.

---

## Correct Strategy Going Forward

### Phase 1 — Win India B2B first (0-3 months)
Create proper landing pages (not blog posts) for:
- "Third Party Pharmaceutical Manufacturing"
- "Dispersible Tablet Contract Manufacturer India"
- One page per major molecule/API Aarise makes
- Location-based page if relevant (e.g. "Pharma Manufacturer Indore")

### Phase 2 — Molecule-specific pages (3-6 months)
One dedicated page per API/molecule they manufacture:
- "[Molecule] API manufacturer India"
- "[Molecule] API supplier India export"
These rank faster because they're specific — less competition than broad terms.

### Phase 3 — Country landing pages (6-12 months)
- "Pharmaceutical API supplier for [Country]"
- "WHO GMP certified API exporter to [Country]"
- Export-angle pages (NOT import-angle — previous blogs were written wrong)

**Important:** Previous country blogs were written as "How to Import API in Ecuador" (wrong angle — that's for Ecuadorian importers). Should be rewritten as "Aarise Pharma — Dispersible Tablet API Supplier for Ecuador" (right angle — for international buyers finding an Indian supplier).

### Off-page (do immediately, faster ROI than SEO):
1. **Pharmacompass listing** — #1 platform for pharma API sourcing. Searched by verified buyers. Only 8 results for "dispersible tablet API manufacturer India" — Aarise not listed. Free to create. Sabhya should do this this week.
2. **IndiaMART** — optimize properly, not just created. All products with specs, high response rate maintained.
3. **LinkedIn company page** — B2B pharma buyers search here. Direct outreach to procurement managers in target countries.
4. **Pharmexcil directory** — government pharma export directory, builds credibility.

---

## Data Still Needed from Client (Sabhya)

To write proper buyer-intent content, we need:
1. **Full product/API list** — every molecule and formulation Aarise manufactures
2. **Certifications** — WHO GMP, ISO, any FDA DMF filings
3. **Countries they've already exported to** — even one or two
4. **Minimum order quantities (MOQ)**
5. **Their exact location/city** — matters for local SEO

Without this, content stays generic. With this, pages match actual buyer searches.

---

## Pending Actions

| Action | Who | Priority |
|---|---|---|
| Install Code Snippets plugin on aarisepharma.com | Sabhya | HIGH |
| Create Pharmacompass listing | Sabhya | HIGH — can generate leads in weeks |
| Get full product list + certifications from client | Priyansh/Sabhya | HIGH |
| Rewrite country pages with export angle | Claude/Priyansh | HIGH |
| Build buyer-intent landing pages (one per product) | Claude/Priyansh | HIGH |
| Optimize IndiaMART profile | Sabhya | MEDIUM |
| Set up LinkedIn company page | Sabhya | MEDIUM |
| Add Device breakdown + Country data to monthly reports | Priyansh | MEDIUM — next report |
| Weekly Google Sheet tracker (contractual) | Priyansh | MEDIUM |
| Healthcare: request re-indexing for country pages via GSC | Sabhya | HIGH |
| Healthcare: publish article on "research compounds" | Claude/Priyansh | HIGH |
| Healthcare: add Product schema to product pages | Claude | MEDIUM |

---

## Key Insight for Future Claude Sessions

The client is frustrated because leads are not coming. The root cause is a **keyword strategy mismatch** — site ranks for wrong audience. The fix is not more content volume, it's correct buyer-intent pages. Pharmacompass listing is the fastest path to actual leads (weeks, not months). SEO is a 4-9 month play done correctly.
