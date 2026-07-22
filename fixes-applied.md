# Fixes Applied Log

## July 23, 2026 — Overnight SEO Fixes

### Fix 1: Noindexed 286 Duplicate Product Pages
**Problem:** Every product had two identical published pages — `/compound-name/` and `/compound-name-2/`. Google split ranking signals between them, ranking neither properly.  
**Fix:** Set `noindex` on all 286 `-2` suffix duplicate pages via Yoast meta.  
**Impact:** Ranking signals now consolidate on the original canonical pages. Expect position improvements in 1-2 weeks as Google re-crawls.

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
