# Aarise SEO — Full Progress Log

Last updated: 2026-08-03

---

## LIVE RIGHT NOW

| Site | Pages Live | Status |
|---|---|---|
| aarisepharma.com | 200 molecule x country pages | IN PROGRESS (175/200 done, Netherlands running) |
| aarisehealthcare.com | 300 research compound pages | QUEUED (fires when pharma finishes) |
| aarisepharma.com | 228 category x country x city pages | QUEUED (fires after healthcare) |
| **Total new pages** | **728** | **Building overnight** |

---

## DATE-WISE ACTIVITY LOG

### 2026-07-28 — Initial SEO Audit & Page Upgrades

**What was done:**
- Full SEO audit of aarisepharma.com and aarisehealthcare.com
- Identified 5 highest-potential pages for content upgrades (buyer-intent queries)
- Rewrote and republished 5 pages with:
  - Expanded H2/H3 structure
  - FAQ sections (5 questions each)
  - FAQPage JSON-LD schema markup
  - Organization schema markup
  - Stronger CTAs and regulatory documentation sections

**Pages upgraded (aarisepharma.com):**
1. Hyderabad API Supplier page
2. Steroid API Supplier page
3. Third Party Pharmaceutical Manufacturer page
4. Dispersible Tablet Manufacturer page
5. WHO GMP Certified API Supplier page

**Research done:**
- GSC data analysis: pharma site had 8,400 impressions / 312 clicks / avg position 18.3
- Healthcare site had almost zero buyer-intent impressions (10 queries / 0 clicks in 90 days)
- Identified gap: no competitor has molecule × country specific pages

---

### 2026-07-29 — GEO / AEO (AI Search Optimization)

**What was done:**
- Created llms.txt files for both sites (AI crawler instruction files)
  - `aarisepharma.com/llms-txt/` — LIVE
  - `aarisehealthcare.com/llms-txt/` — LIVE
- Published both as WordPress pages
- Committed to GitHub: `d:\aarise-seo-repo\geo-aeo\`

**Why:** llms.txt tells AI crawlers (Claude, ChatGPT, Perplexity) what the site is about and which pages to cite when users ask AI search queries like "best API supplier from India"

**Pending (Sabhya):**
- Install Code Snippets plugin on pharma → add PHP snippet for true `/llms.txt` plain text URL
- Same for healthcare site

---

### 2026-07-30 — Unicode / Emoji Bug Fix

**Problem found:** Live pages showed `????` instead of flag emojis, `??` instead of phone icon, `?` instead of `≥` symbol
**Root cause:** WordPress MySQL database on 3-byte `utf8` charset — 4-byte emoji (flag sequences, phone emoji) silently dropped to `?`
**Fix:** Added `strip_emoji()` function to all page-push scripts — maps flag emoji to country names in plain text, strips all 4-byte characters before sending to WP REST API
**Status:** Fixed. All 5 upgraded pages re-pushed with clean text.

---

### 2026-07-31 — Programmatic SEO Strategy Decided

**Research done:**
- GSC Links report: pharma has 96 external links but 70 are from own network = only 6 real backlinks
- Healthcare has 6 external links, 3 own network = ~0 real backlinks
- This is why buyer-intent rankings are stuck at positions 8–15 — not enough authority
- **Strategy pivot:** Build programmatic page volume first to create surface area, then build backlinks

**Programmatic SEO plan decided:**
1. Molecule × Country pages for pharma (20 molecules × 10 countries = 200 pages)
2. Research Compound × Country pages for healthcare (15 compounds × 10 countries × 2 templates = 300 pages)
3. Category × Country + Category × City pages for pharma (12 categories × 19 pages = 228 pages)

**Why this works:**
- Zero competition for "metformin api supplier brazil" type queries
- Expect position 1–3 rankings within 4–6 weeks of indexing
- No Indian API supplier competitor has this level of page coverage
- 728 pages creates massive internal link equity and topic authority signal

---

### 2026-08-01 — Pharma 200-Page Script (Run 1 & 2, failed)

**Script:** `programmatic_molecule_country.py`

**Run 1 failure:** `ChunkedEncodingError` — server dropped connection during Mexico batch
- Cause: 0.5s delay between posts overloaded shared hosting
- Fix: Added 60s timeout, 3-attempt retry, 2s delay between posts

**Run 2 failure:** `JSONDecodeError` in `slug_exists()` — server returned empty body
- Cause: Server returned empty 200 response to slug check under load
- Fix: Check `if not r.text.strip()` before calling `.json()`, retry with 5s sleep

**Pages published before failures:** Brazil (20), Colombia (20), Mexico (18/20)

---

### 2026-08-02 — Pharma 200-Page Script (Run 3, running overnight)

**Script:** `programmatic_molecule_country.py` (all fixes applied)
**Started:** ~04:29 AM
**Status at 2026-08-03:** 
- Brazil ✓ (20/20) 
- Colombia ✓ (20/20) 
- Mexico ✓ (20/20) 
- Germany ✓ (20/20) 
- USA ✓ (20/20) 
- South Korea: IN PROGRESS 
- Argentina: QUEUED 
- Philippines: QUEUED 
- South Africa: QUEUED 
- Netherlands: QUEUED

**Slug pattern:** `{molecule}-api-supplier-{country}` e.g. `metformin-api-supplier-brazil`

---

### 2026-08-03 — Healthcare + Category Scripts Written & Queued

**Healthcare script:** `programmatic_healthcare.py`
- 15 research compounds × 10 countries × 2 URL templates = 300 pages
- Template 1: `buy-{compound}-research-compound-{country}`
- Template 2: `{compound}-supplier-{country}-research-grade`
- Compounds: BPC-157, Semaglutide, Tirzepatide, Retatrutide, TB-500, Ipamorelin, CJC-1295, Melanotan-2, HGH Fragment 176-191, HCG, Testosterone Enanthate, Nandrolone Decanoate, Follistatin-344, Epithalon, AOD-9604
- DISCLAIMER block on every page (research use only, not for human consumption)

**Category script:** `programmatic_category.py`
- 12 categories × (1 root + 10 countries + 8 India cities) = 228 pages
- Categories: Anti-Diabetic, Corticosteroid, Antibiotic, Cardiovascular, Hormone, NSAID, Proton Pump Inhibitor, Steroid, Respiratory, Third Party Manufacturer, Dispersible Tablet, WHO GMP Certified API
- India cities: Mumbai, Delhi, Hyderabad, Bangalore, Chennai, Ahmedabad, Pune, Kolkata
- Countries: Brazil, Colombia, Mexico, Germany, USA, South Korea, Argentina, Philippines, South Africa, Netherlands

**Watcher script:** `wait_and_fire_healthcare.py`
- Monitors for Netherlands pharma pages → fires healthcare → fires category
- Runs fully automatically overnight

**Backlinks research:**
- Pharmacompass, Alibaba, Kompass, Europages, ThomasNet, IndiaMART prioritised
- Directory listing copy written: `d:\aarise-seo-repo\backlinks\directory-listings.md`
- Short (100w) + long (300w) company profiles ready to paste
- 4 product listings written for API, CMO, Corticosteroids, Dispersible Tablets
- Sabhya to submit starting with Pharmacompass + Alibaba (highest impact)

---

## PENDING ACTIONS — SABHYA

| Priority | Action | Why |
|---|---|---|
| HIGH | Submit XML sitemap to GSC — `aarisepharma.com/wp-sitemap.xml` | Tells Google about all 428+ new pages; speeds up crawl |
| HIGH | Submit XML sitemap to GSC — `aarisehealthcare.com/wp-sitemap.xml` | Same for healthcare |
| HIGH | Start Pharmacompass listing — use copy from `backlinks/directory-listings.md` | Highest quality backlink for pharma; also drives leads |
| HIGH | Alibaba free supplier listing | Second highest quality backlink; global buyer reach |
| MEDIUM | Clear WordPress cache on both sites | Ensure new pages are served fresh |
| MEDIUM | Install Code Snippets plugin → PHP snippet for `/llms.txt` on pharma | True plain-text URL for AI crawlers |
| MEDIUM | Add service account as GSC OWNER: `search-console@level-district-353301.iam.gserviceaccount.com` | Unblocks Google Indexing API automation |
| MEDIUM | Register both sites on Bing Webmaster Tools | 6% of search traffic; free |
| LOW | Kompass, Europages, ThomasNet listings | Additional backlinks; use same copy |

---

## TOTAL PAGE COUNT (when all scripts finish)

| Category | Pages | Site |
|---|---|---|
| Molecule × Country | 200 | aarisepharma.com |
| Category root pages | 12 | aarisepharma.com |
| Category × Country | 120 | aarisepharma.com |
| Category × India City | 96 | aarisepharma.com |
| Research Compound × Country (template 1) | 150 | aarisehealthcare.com |
| Research Compound × Country (template 2) | 150 | aarisehealthcare.com |
| **TOTAL NEW PAGES** | **728** | both sites |

---

## INDEXING TIMELINE ESTIMATE

| Milestone | Expected Date |
|---|---|
| All 728 pages live | 2026-08-04 (overnight) |
| Google first crawl (via sitemap submission) | 2026-08-07 to 2026-08-17 |
| First rankings appear | 2026-08-18 to 2026-09-03 |
| Stable position 1-3 for molecule+country queries | 2026-09-03 to 2026-10-03 |
| GSC impressions uplift visible | 2026-08-17 to 2026-09-03 |

**Note:** Submit both sitemaps to GSC immediately after pages finish — this is the single biggest thing Sabhya can do to accelerate indexing.

---

## KEYWORD STRATEGY SUMMARY

**aarisepharma.com targets:**
- `[molecule] api supplier [country]` — 200 pages, position 1 expected (zero competition)
- `[category] api supplier [country]` — 120 pages, position 2-5 expected
- `[category] api supplier [india city]` — 96 pages, position 1-3 expected (domestic buyers)
- `[category] api supplier` — 12 pages, position 5-15 expected (competitive)

**aarisehealthcare.com targets:**
- `buy [compound] research compound [country]` — 150 pages
- `[compound] supplier [country] research grade` — 150 pages
- Both: position 1-3 expected (very low competition for research compound sourcing queries)

---

## FILES IN THIS REPO

```
geo-aeo/
  llms-pharma.txt          — llms.txt content for aarisepharma.com
  llms-healthcare.txt      — llms.txt content for aarisehealthcare.com
  llms-txt-status.md       — deployment status and Sabhya pending actions

backlinks/
  directory-listings.md    — full copy for Pharmacompass, Alibaba, Kompass etc.

scripts/
  gsc_request_indexing.py  — Google Indexing API (blocked; needs GSC OWNER setup)

SEO-PROGRESS.md            — this file
```
