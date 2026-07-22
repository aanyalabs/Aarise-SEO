# Technical SEO Audit Findings

**Date:** July 2026  
**Tools used:** Google Search Console, GA4, manual inspection, Apify SERP scraper

---

## aarisehealthcare.com

### Issue 1 — 114–131 Internal Links Per Page 🔴 CRITICAL
**Source:** WooCommerce "Recent Products" widget in footer — appears on every page  
**Impact:** Link equity dilution across all pages; Google devalues each link when there are 100+  
**Fix:** WP Admin → Appearance → Widgets → remove the Recent Products widget  
**Effort:** 5 minutes

### Issue 2 — Author Shows as Email Address 🟡 MEDIUM
**Current:** Author displayed as `sabhya@urbansingapore.com`  
**Impact:** Kills E-E-A-T (Experience, Expertise, Authoritativeness, Trust) signals  
**Fix:** WP Admin → Users → Edit user → change Display Name to real name, add bio  
**Effort:** 10 minutes

### Issue 3 — 52 Pending Pingback Comments 🟡 MEDIUM
**Impact:** Spam signals, crawl budget waste  
**Fix:** WP Admin → Settings → Discussion → uncheck "Allow link notifications from other blogs" → Comments → bulk trash all 52  
**Effort:** 5 minutes

### Issue 4 — 2,964 "Alternative page with proper canonical" in GSC 🟢 LOW (non-issue)
**Status:** ✅ CONFIRMED NOT A PROBLEM  
**Details:** Blog post canonicals checked and confirmed correct (pointing to self). The 2,964 count comes from WooCommerce product page variants, not SEO pages.

### Issue 5 — Wrong Keyword Strategy 🔴 CRITICAL (strategic)
**Details:** All "buy research [compound] [country]" keywords verified at 0-10 searches/month via Keyword Planner  
**Fix:** Pivot to regulatory/legal intent pages ("are peptides legal in X?") — see keyword-research/healthcare-site-keywords.md

---

## aarisepharma.com

### Issue 1 — 100,731 Pages Blocked by robots.txt 🟢 LOW (non-issue)
**Status:** ✅ CONFIRMED CORRECT  
**Details:** robots.txt reviewed — blocked URLs are WooCommerce `?add-to-cart=` and transient parameters. Correct to block.

### Issue 2 — 738 Product-Tag Pages Crawled-Not-Indexed 🟡 MEDIUM
**Source:** WooCommerce product tag archive pages (`/product-tag/xyz/`)  
**Impact:** Crawl budget waste; Google crawls these but doesn't index them  
**Fix:** Yoast → Search Appearance → Taxonomies → Product Tags → toggle off (noindex)  
**Effort:** 2 minutes

### Issue 3 — Dispersible Tablets Page: 27,796 Impressions, ~0% CTR 🔴 CRITICAL
**Details:** Ranking #2 for "dispersible tablets uses" and "dispersible tablet meaning" but almost nobody clicks  
**Root cause:** No FAQ schema = not appearing as rich result / AI Overview  
**Fix:** Add FAQ schema markup to the dispersible tablets page  
**Effort:** 30 minutes  
**Impact:** Could 5-10x click-through rate

### Issue 4 — Sitemap Resubmit Button Missing in GSC
**Status:** ✅ RESOLVED (not a bug)  
**Details:** GSC removed the resubmit button in 2025. Workaround: re-enter sitemap URL in "Add a new sitemap" box to force re-read.
