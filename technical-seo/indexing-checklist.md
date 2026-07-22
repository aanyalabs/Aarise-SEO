# Indexing Checklist & Submission Log

## How to Submit URLs for Indexing in GSC

1. Go to Google Search Console → select property
2. Paste URL in the search bar at the top → press Enter
3. Click "Request Indexing" button
4. Repeat for each URL (GSC limits: ~10-12 requests/day per property)

**Bulk indexing:** GSC does not support bulk URL submission. For many pages, ensure they are in the sitemap and Google will crawl them. Only manually request indexing for your most important pages.

---

## Sitemap Status

### aarisehealthcare.com
- **Sitemap:** `aarisehealthcare.com/sitemap_index.xml`
- **SEO plugin:** RankMath (auto-generates sitemap)
- **Last GSC read:** July 21, 2026

### aarisepharma.com
- **Sitemap:** `aarisepharma.com/sitemap_index.xml`  
- **SEO plugin:** Yoast (auto-generates sitemap)
- **Last GSC read:** July 21, 2026
- **Note:** GSC removed the "Resubmit sitemap" button. To force re-read: GSC → Sitemaps → enter the URL again in "Add a new sitemap" field

---

## robots.txt Status

### aarisepharma.com
- ✅ Reviewed and confirmed correct
- 100,731 URLs blocked = WooCommerce `?add-to-cart=` and transient parameters
- These should be blocked — this is correct behavior

### aarisehealthcare.com
- Not flagged as an issue
- Standard WordPress/WooCommerce robots.txt

---

## Crawl Budget Issues to Fix

| Site | Issue | Count | Fix |
|------|-------|-------|-----|
| aarisepharma.com | Product-tag archive pages crawled-not-indexed | 738 | Yoast → Taxonomies → Product Tags → noindex |
| aarisehealthcare.com | Pingback comment spam | 52 | WP Settings → Discussion → disable pingbacks |

---

## GSC Index Coverage Summary

### aarisehealthcare.com
| Status | Count | Action |
|--------|-------|--------|
| Indexed | Core pages ✅ | — |
| Alternative page with proper canonical | 2,964 | ✅ Non-issue (WooCommerce variants) |

### aarisepharma.com  
| Status | Count | Action |
|--------|-------|--------|
| Indexed | Core pages ✅ | — |
| Blocked by robots.txt | 100,731 | ✅ Correct |
| Crawled, not indexed | 738 | ⚠️ Fix: noindex product tags |
