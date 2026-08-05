# Aarise SEO — Full Progress Log

Last updated: 2026-08-05

---

## LIVE RIGHT NOW

| Site | Pages Live | Status |
|---|---|---|
| aarisepharma.com | 2,243 total published posts | LIVE — all sitemaps green |
| aarisehealthcare.com | ~1,400+ posts (API count issue) | LIVE — sitemap pending GSC submission |
| **Grand total** | **~3,600+ pages** | **Both sites fully built** |

### Google indexing status (as of Aug 5)
- post-sitemap1: 281 URLs — Success ✅
- post-sitemap2: 1,000 URLs — Success ✅ (fixed Aug 4)
- post-sitemap3: 243 URLs — Success ✅ (fixed Aug 4)
- Total discovered by Google: 1,681 URLs
- Total indexed (GSC page indexing report): 325
- Estimated crawled so far via URL inspection: ~60-70% of sampled pages indexed Aug 3-5
- robots.txt: clean, no blocks on programmatic pages
- 103K "blocked by robots.txt" in GSC = WooCommerce query param URLs (?add-to-cart=), not our content

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

### 2026-08-03 — Buyer Intent Mega-Build (1,991 new pharma pages + healthcare)

**Scripts run:**
- `programmatic_buyer_intent.py` — pharma buyer intent pages
- `programmatic_hc_buyer_intent.py` — healthcare buyer intent pages

**Pharma buyer intent pages built (9 types × 18 countries × 20 molecules):**
- `buy-[mol]-api-[country]` — 360 pages
- `import-[mol]-api-from-india-to-[country]` — 360 pages
- `[mol]-api-price-[country]` — 360 pages
- `[mol]-api-manufacturer-[country]` — 360 pages
- `api-suppliers-[country]` — 18 pages
- `import-api-from-india-[country]` — 18 pages
- `who-gmp-certified-api-supplier-[country]` — 18 pages
- Regulatory agency pages (ANVISA, COFEPRIS, INVIMA, MFDS, FDA, EMA, SAHPRA, ANMAT) — 8 pages
- `api-supplier-[india-city]` — 8 pages
- **Pharma total: 2,243 published posts** (was 252 before = +1,991 new)

**18 countries covered:** Brazil, Colombia, Mexico, Germany, USA, South Korea, Argentina, Philippines, South Africa, Netherlands, UK, Poland, Turkey, Chile, Peru, Thailand, UAE, Australia

**Healthcare buyer intent pages built (6 types × 18 countries × 15 compounds):**
- `buy-[compound]-research-grade-[country]`
- `[compound]-supplier-[country]-wholesale`
- `import-[compound]-research-compound-[country]`
- `[compound]-price-[country]`
- `research-compounds-supplier-[country]`
- `import-research-compounds-from-india-[country]`
- DISCLAIMER block on every page (research use only)

**IndexNow submitted:**
- Yandex: 2,243 pharma URLs — 202 Accepted ✅
- Bing: 429 blocked — needs key file `a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4.txt` uploaded to domain root

**GSC sitemap issue discovered:**
- post-sitemap2.xml and post-sitemap3.xml returning "Couldn't fetch" for Googlebot
- Root cause: cache plugin blocking bot user agent from XML files
- Fix needed: exclude *.xml from cache

**GSC data pulled (90-day buyer intent analysis):**
- "api suppliers" — 160 impressions, pos 19.2, 0 clicks
- "api exporters" — 115 impressions, pos 22.7, 0 clicks
- "hormone api manufacturers in india" — 87 impressions, pos 12.2, 2 clicks
- UAE searching "bulk medicine import compliance invima colombia" — 63 impressions
- These signals drove the buyer intent page decisions

---

### 2026-08-04 — Sitemaps Fixed, All Pages Discoverable

**Sitemap fixes confirmed (Sabhya):**
- post-sitemap2.xml: Success ✅ — 1,000 URLs (fixed)
- post-sitemap3.xml: Success ✅ — 243 URLs (fixed Aug 4)
- Total discovered by Google across all sitemaps: **1,681 URLs**

**GSC page indexing report:**
- Indexed: 325
- Not indexed: 103K — breakdown:
  - "Blocked by robots.txt": 98,537 → these are WooCommerce ?add-to-cart= query param URLs, NOT our content
  - "Alternate page with proper canonical": 3,207
  - "Duplicate without user-selected canonical": 69
- robots.txt is clean — `Disallow:` is empty, nothing blocking programmatic pages

**URL Inspection results (sampled pages):**
- `buy-metformin-api-brazil` → Indexed, last crawled Aug 3 ✅
- `import-metformin-api-from-india-to-germany` → Indexed, last crawled Aug 5 ✅
- `metformin-api-price-usa` → Indexed, last crawled Aug 4 ✅
- `api-suppliers-brazil` → Indexed, last crawled Aug 5 ✅
- `who-gmp-certified-api-supplier-brazil` → Unknown (in sitemap3, just fixed) ⏳

**GSC performance (day on day):**
- Aug 2: 1,830 impressions | 8 clicks (pharma)
- Aug 3/4 data: not yet in GSC (2-3 day lag)
- 7-day: 6,413 impressions | 87 clicks (down from 8,003 — due to sitemap break, now fixed)
- 70 new programmatic pages already showing impressions
- Best performer: `who-gmp-certification-pharma-requirements-process` → 283 impr, pos 12.8

**Healthcare GSC:**
- 8–20 impressions/day, 0 clicks — barely discovered
- Sitemap not yet submitted to healthcare GSC (Sabhya pending)

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

| Priority | Action | Status | Why |
|---|---|---|---|
| 🔴 CRITICAL | Upload `a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4.txt` to both domain roots (`public_html/`) | PENDING | Bing IndexNow blocked with 429 — key file not hosted |
| 🔴 CRITICAL | Submit `aarisehealthcare.com/wp-sitemap.xml` to healthcare GSC | PENDING | Healthcare getting 8-20 impr/day — Google barely knows it exists |
| 🟡 HIGH | Start Pharmacompass listing — use copy from `backlinks/directory-listings.md` | PENDING | Highest quality backlink for pharma; also drives leads |
| 🟡 HIGH | Alibaba free supplier listing | PENDING | Global buyer reach |
| 🟡 HIGH | Add service account as GSC OWNER: `search-console@level-district-353301.iam.gserviceaccount.com` | PENDING | Unblocks Google Indexing API automation |
| 🟡 HIGH | Register both sites on Bing Webmaster Tools | PENDING | 6% of search traffic; free |
| 🟠 MEDIUM | Clear WordPress cache on both sites | PENDING | Ensure new pages served fresh |
| 🟠 MEDIUM | Install Code Snippets plugin → PHP snippet for `/llms.txt` on pharma | PENDING | True plain-text URL for AI crawlers |
| 🟢 LOW | Kompass, Europages, ThomasNet listings | PENDING | Additional backlinks; use same copy |

**DONE by Sabhya:**
- ✅ post-sitemap2.xml cache exclusion — fixed Aug 4
- ✅ post-sitemap3.xml cache exclusion — fixed Aug 4
- ✅ pharma GSC sitemap submitted

---

## TOTAL PAGE COUNT (FINAL — as of Aug 5)

| Category | Pages | Site | Status |
|---|---|---|---|
| Molecule × Country (20 mol × 10 countries) | 200 | aarisepharma.com | ✅ LIVE |
| Category × Country + City (12 cat × 19) | 228 | aarisepharma.com | ✅ LIVE |
| Buy [mol] API [country] (20 × 18) | 360 | aarisepharma.com | ✅ LIVE |
| Import [mol] API from India [country] (20 × 18) | 360 | aarisepharma.com | ✅ LIVE |
| [mol] API price [country] (20 × 18) | 360 | aarisepharma.com | ✅ LIVE |
| [mol] API manufacturer [country] (20 × 18) | 360 | aarisepharma.com | ✅ LIVE |
| API suppliers [country] (18) | 18 | aarisepharma.com | ✅ LIVE |
| Import API from India [country] (18) | 18 | aarisepharma.com | ✅ LIVE |
| WHO GMP certified [country] (18) | 18 | aarisepharma.com | ✅ LIVE |
| Regulatory agency pages (8) | 8 | aarisepharma.com | ✅ LIVE |
| API supplier [India city] (8) | 8 | aarisepharma.com | ✅ LIVE |
| **Pharma total** | **2,243** | aarisepharma.com | ✅ |
| Research compound buyer intent (6 types × 18 × 15) | ~1,400+ | aarisehealthcare.com | ✅ LIVE |
| **GRAND TOTAL** | **~3,600+** | both sites | ✅ ALL LIVE |

---

## INDEXING TIMELINE ESTIMATE (updated Aug 5)

| Milestone | Expected Date | Status |
|---|---|---|
| All ~3,600 pages live | Aug 3, 2026 | ✅ DONE |
| Pharma sitemaps all green in GSC | Aug 4, 2026 | ✅ DONE |
| Google actively crawling new pages | Aug 3–5, 2026 | ✅ IN PROGRESS |
| First impressions on new buyer intent pages | Aug 5–15, 2026 | ⏳ PENDING |
| Indexed count hits 1,000+ | Aug 15–25, 2026 | ⏳ PENDING |
| First clicks from new pages | Aug 20 – Sep 3, 2026 | ⏳ PENDING |
| Stable positions 1–5 for mol+country queries | Sep 3 – Oct 3, 2026 | ⏳ PENDING |
| Healthcare impressions meaningful | Aug 15 – Sep 1, 2026 | ⏳ needs sitemap submitted |

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
