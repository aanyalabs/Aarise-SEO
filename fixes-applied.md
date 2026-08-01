# Fixes Applied Log

## August 1, 2026 — 18-Country Expansion, Site Fixes, and New Blog Content (wachas)

Client (Sabhya) expanded the country target list from 4 to 18: USA, Mexico, Peru, Brazil, Colombia, Chile, Argentina, Guatemala, Ecuador, Spain, Germany, Poland, Turkey, South Korea, Vietnam, Canada, Russia, Netherlands — across both sites. Below is the full record of what was built, what broke and got fixed along the way, and what's still open. Everything here was verified live (HTTP 200, rendered content, valid schema) before being logged — not just claimed. See the correction under the July 23 entry below for why that distinction matters.

### 1. Country expansion — 148 new pages

| Site | Tier-1 hubs | Tier-2/3 depth | Supporting pages | Total new |
|---|---|---|---|---|
| aarisepharma.com | 10 new (Guatemala, Spain, Germany, Poland, Turkey, South Korea, Vietnam, Canada, Russia, Netherlands) — IDs 10793-10802 | 120 (15 countries × 8: Buy + Catalog pages for Steroid/Peptide/Pharma/Hormone) | 2 (`/pharma-api-export-markets/` cross-link hub, `/api/` product page) | **132** |
| aarisehealthcare.com | 15 new (all net-new countries) — IDs 1006123-1006137 | Deliberately deferred — see §6 | 1 (`/research-compounds-supplier-network/` cross-link hub) | **16** |

Pharma got full tier-1→3 depth on all 18 countries because GSC data showed real, growing demand in all of them already. Healthcare got tier-1 hubs only for the 15 net-new countries — its problem was ranking position (20-80 avg), not country coverage, so building 8 speculative product-depth pages per country with zero demand signal yet would have just created unproven thin content. This was a deliberate, evidence-led call, not a shortcut.

Brazil, Argentina, Chile, Colombia, and Ecuador were **not** net-new on Pharma — they already had pages, but angled wrong ("how a local importer navigates customs" instead of "Aarise as the export supplier"), so those 5 were rewritten in place (same URL) rather than counted as new.

### 2. Bugs found and fixed (not part of the original scope — discovered during execution)

**WPBakery Page Builder deactivated site-wide (Pharma).** An auto-update (8.7.3 → 8.7.4) triggered WordPress's fatal-error protection, which silently deactivated the plugin. Every `[vc_row]`/`[vc_column]` shortcode sitewide stopped parsing and rendered as literal bracket text — this broke Home, About Us, Third-Party-Manufacturing, Contact Us, Products, the mega-menu, and the dispersible-tablets page (the site's single highest-traffic page, 33,000+ impressions/month). Fixed by reactivating the plugin via REST (`POST /wp-json/wp/v2/plugins/js_composer/js_composer {"status":"active"}`). One-line fix once the actual cause was found — this is also what caused the "critical error" outage screenshots sent earlier; the plugin issue and the outage were the same root cause, not two separate incidents.

**Healthcare: 291 of 623 pages (~half the site) were live, fully-indexable exact-title duplicates.** `-2`-suffixed pages matching a base-slug page, both published, both `index,follow`. **This directly contradicts the July 23 "Fix 1" claim below** ("noindexed 286 duplicate pages") — every pair checked in this pass was still fully indexable, and GSC's own Validation report independently confirmed "Failed" on this exact issue. The earlier noindex attempt never actually took effect. Real fix: a generic Code Snippet 301-redirects any `-2`-suffix page to its base-slug counterpart, plus bulk-drafted all 291 confirmed duplicates. Verified: published pages 623 → 332.

**Two batch-publish scripts created live duplicate posts on Pharma (24 total, both incidents caught and fixed).** Root cause both times: a script died partway through a batch (background job silently killed once; a foreground 2-minute Bash timeout the other time), and the resume logic re-ran against a stale "what's missing" list instead of re-checking live site state, creating `-2` duplicates of posts that had actually already succeeded. First incident: 18 duplicates across Canada/Russia/Netherlands tier-2/3 pages (caught while pulling exact page counts for a client question). Second incident: 6 duplicates across the new country buyer-guide posts (caught immediately, mid-run). Both fixed by setting the duplicates to `draft` (note: `DELETE` was blocked twice by the Claude Code auto-mode classifier as a higher-risk action — `POST status=draft`, already proven safe from the Healthcare dedup fix, worked cleanly instead). **Lesson for any future batch-publish work: always re-verify live site state before resuming or retrying a script — never trust the script's own success/fail log.**

**Doubled-word bug ("Research Research Steroid Compound")** across 24 Healthcare posts, and an **"Active [Pharmaceutical Ingredients]" truncation bug** (a sitewide find-replace defect, 16 instances across Pharma) — both found and fixed, verified zero remaining via full-site regex rescan.

### 3. GSC access and indexing verification

The service account referenced throughout this repo (`search-console@level-district-353301.iam.gserviceaccount.com`) had **zero access to either property** — contrary to what the repo's own docs assumed. Sabhya added it as `siteFullUser` on both `aarisepharma.com` and `aarisehealthcare.com` (confirmed 2026-07-30). First full indexing sweep of all 153 new/changed URLs from the country expansion: 55/153 (36%) already indexed with no manual action, 96 not yet crawled (normal for pages 1-3 weeks old), 1 crawled-not-indexed, 1 canonical-mismatch. Full breakdown and the manual "Request Indexing" worklist (trimmed to only the ~98 that still need it) are in `technical-seo/indexing-request-queue-2026-07-28.md` / `.csv`.

### 4. Monthly report overhaul

The June report significantly under-reported both sites (Pharma 439 vs. actual 983 clicks; Healthcare reported as 0 clicks when the real number was 20) and omitted the one metric that answers the client's actual complaint ("no leads") — GA4 already had `form_submit: 37` for the period, unreported. Full analysis and a redesigned 9-section report structure (leads-first, country tracker, promise tracker, honest "DATA PENDING" instead of invented numbers) is in the plan doc; the generator lives in `scripts/new_monthly_report.py` + `scripts/xlsx_reader.py` (stdlib-only .xlsx reader — `openpyxl`/`pandas` aren't installed on this machine). Sample output: `reports/monthly/Aarise_Combined_SEO_Report_NEW_TEMPLATE.docx`.

### 5. New blog content (34 posts, distinct from the country expansion pages above)

Two rounds, per explicit client request via WhatsApp (Sabhya: "individual blog bana do... rank karta hai jaldi... products/ingredients pe rank nahi karna").

**Round 1 — general educational content (4 posts, 2/site):** WHO-GMP/DMF/CEP certifications explainer, API import timeline (Pharma); Certificate of Analysis guide, "Research Use Only" explainer (Healthcare). IDs: 10994, 10995 (Pharma), 1006163, 1006164 (Healthcare).

**Round 2 — country-specific buyer guides (30 posts, 15/site):** one per country lacking this angle already. Important design choice: these do **not** target the same keyword as each country's existing hub page — that would cannibalize the hub instead of helping it rank. Instead each is a "buyer's sourcing guide" (documentation, realistic shipping timelines, what causes import delays) that internally links to the hub page using the hub's actual target keyword as anchor text, which is the real mechanism for helping a specific page rank faster. Zero ingredient/product keywords used, per the client's explicit instruction. IDs: Pharma 10998-11012, Healthcare 1006165-1006179.

Combined with the 148 expansion pages, **total new content this cycle: 182 pages across both sites**, all published 2026-07-27 through 2026-08-01.

### 6. Outstanding / deferred (not yet done — flagging so nobody assumes it's covered)

- Healthcare tier-2/3 depth pages — intentionally held pending real GSC data on the just-published hub pages.
- Leads & Enquiries GA4 Key Events — needs a live API pull with the right scope (currently `DATA PENDING` in the report).
- Competitor Snapshot — needs a SERP rank-tracking tool, not currently in place.
- Weekly Google Sheet tracker — contractual, never set up.
- WooCommerce "select options" text appearing as junk indexed queries — minor, flagged, not fixed.
- Guatemala's pharma regulator body — no single confirmed national authority found in research; using the Ministry of Public Health's pharmaceutical department pending confirmation.

---

## July 23, 2026 — Overnight SEO Fixes

### Fix 1: Noindexed 286 Duplicate Product Pages
**Problem:** Every product had two identical published pages — `/compound-name/` and `/compound-name-2/`. Google split ranking signals between them, ranking neither properly.  
**Fix:** Set `noindex` on all 286 `-2` suffix duplicate pages via Yoast meta.  
**Impact:** Ranking signals now consolidate on the original canonical pages. Expect position improvements in 1-2 weeks as Google re-crawls.

> **Correction (2026-08-01, wachas):** This fix never actually took effect. Re-checked live on 2026-07-28 — found 291 duplicate pairs still fully published and `index,follow`, and GSC's own Validation report independently showed "Failed" on this exact issue. (Also note: this site runs RankMath, not Yoast — the meta field this fix targeted wasn't even the one the live site reads.) Real fix applied: a Code Snippet 301-redirecting every `-2` page to its base-slug counterpart, plus bulk-drafting all 291 confirmed duplicates. See the August 1, 2026 entry above for the full writeup. Flagging this clearly so nobody relies on the original "impact" note above — it didn't happen.

### Fix 2: Meta Descriptions on All 91 Posts
**Problem:** Zero meta descriptions across all 91 posts. Google was auto-generating ugly, irrelevant snippets — killing CTR.  
**Fix:** Generated and pushed unique, keyword-targeted meta descriptions to all 91 posts:
- Supplier pages: country + compound type + COA + shipping mention
- Catalog pages: compound category + specifications mention
- Guide pages: compound name + mechanism + purity mention  
**Impact:** Higher CTR as Google now shows compelling descriptions in search results.

### Fix 3: Meta Descriptions on 293 Original Product Pages
**Problem:** Same zero-meta issue on all product pages.  
**Fix:** Generated unique meta descriptions for all 293 product pages using compound name, category (peptide/steroid/hormone/SARM), CAS number where available, purity claim, and COA mention.

### Fix 4: FAQ Schema on All Supplier/Buy Posts
**Problem:** No structured data on supplier pages — missing from Google AI Overviews and rich results.  
**Fix:** Added FAQ schema (JSON-LD) to all supplier and buy posts covering:
- What compounds are available for [country]?
- How long does shipping take?
- Do you provide COA?
- What is the minimum order?

### Fix 5: Noindexed WooCommerce System Pages
**Problem:** Cart, checkout, my-account pages being crawled and wasting crawl budget.  
**Fix:** Set noindex on all WooCommerce system pages.

---

## Country Pages Expanded (July 23, 2026)

The 4 main supplier pages were fully rewritten with ~800 words each, FAQ sections, and FAQ schema:

| Page | Post ID | Changes |
|------|---------|---------|
| Paraguay supplier | 1004963 | Full rewrite + DINAVISA reg info + FAQ schema + meta desc |
| Peru supplier | 1004959 | Full rewrite + DIGEMID reg info + FAQ schema + meta desc |
| Mexico supplier | 1004955 | Full rewrite + COFEPRIS reg info + FAQ schema + meta desc |
| US supplier | 1004967 | Full rewrite + FDA RUO info + FAQ schema + meta desc |

---

## Pending (Requires Sabhya Access)

| Task | Who | Where |
|------|-----|-------|
| Remove footer Recent Products widget | Sabhya | WP Admin → Appearance → Widgets |
| Turn off pingbacks + trash 52 comments | Sabhya | WP Admin → Settings → Discussion |
| Fix author display name (shows as email) | Sabhya | WP Admin → Users |
| Add service account to healthcare GSC | Sabhya | GSC → Settings → Users → add search-console@level-district-353301.iam.gserviceaccount.com |
| Add service account to pharma GA4 | Sabhya | GA4 → Admin → Property Access Management → add same email |
| Request indexing for 4 updated pages | Sabhya | GSC → URL Inspection → Request Indexing for Paraguay/Peru/Mexico/US pages |

---

## Scripts Written (in /scripts/)

| Script | Purpose |
|--------|---------|
| `fix_all.py` | Noindex 286 dupes + meta on 91 posts |
| `fix_product_pages.py` | Meta on 293 product pages + FAQ schema + WooCommerce noindex |
| `update_paraguay.py` | Full Paraguay page rewrite |
| `update_peru_mexico_us.py` | Full Peru, Mexico, US page rewrites |
| `ga4_pull.py` | Pull GA4 data for healthcare site (property 535124183) |
| `ga4_pharma.py` | Pull GA4 data for pharma site (property 450152213 — needs access) |
| `gsc_pull.py` | Pull GSC data for both sites |
