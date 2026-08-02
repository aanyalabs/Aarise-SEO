# llms.txt Status

## Healthcare — LIVE ✅

**URL**: https://aarisehealthcare.com/llms.txt  
**Status**: 200 OK | Content-Type: text/plain  
**How it works**: WordPress page at slug `llms-txt` + Code Snippet (ID 37) that intercepts `/llms.txt` requests and serves the page content as plain text.

**Content covers**:
- Company description (research compound supplier, pharma grade with COA)
- Product categories (peptides, steroids, hormones, SARMs)
- Key facts (purity, COA, shipping)
- Target buyers (research institutions, licensed pharmaceutical manufacturers)
- Disclaimer language for AI crawlers

**Content file**: `llms-healthcare.txt` in this folder

---

## Pharma — LIVE ✅

**URL**: https://aarisepharma.com/llms-txt/ (WordPress page, published)  
**Status**: Published to WordPress via REST API on 2026-08-03  

**Content covers**:
- WHO GMP certified manufacturer description
- Key pages with URLs (Home, About, Products, Contact)
- All 6 service pages with descriptions
- Key facts: certifications, capacity, 18 export countries, 100+ APIs, MOQ, contact

**Content file**: `llms-pharma.txt` in this folder

### Pending for Pharma — Sabhya action needed:
To make `/llms.txt` work as a direct URL (instead of `/llms-txt/`), Sabhya needs to either:

**Option A — Install Code Snippets plugin (5 min)**:
1. WP Admin → Plugins → Add New → "Code Snippets" → Install → Activate
2. Snippets → Add New → paste this PHP → Save & Activate:

```php
add_action('init', function() {
    if ( isset($_SERVER['REQUEST_URI']) ) {
        $uri = strtok($_SERVER['REQUEST_URI'], '?');
        if ( $uri === '/llms.txt' ) {
            $page = get_page_by_path('llms-txt');
            if ($page) {
                $content = $page->post_content;
                $content = strip_tags($content);
                $content = html_entity_decode($content, ENT_QUOTES | ENT_HTML5, 'UTF-8');
                $content = preg_replace('/\n{3,}/', "\n\n", $content);
                $content = trim($content);
                header('Content-Type: text/plain; charset=utf-8');
                header('Cache-Control: public, max-age=86400');
                echo $content;
                exit;
            }
        }
    }
}, 1);
```

**Option B — .htaccess redirect (2 min)**:
Add to .htaccess (above `# BEGIN WordPress`):
```
RedirectMatch 301 ^/llms.txt$ /llms-txt/
```

---

## FAQPage Schema — LIVE ✅

Injected JSON-LD FAQPage schema into all 5 upgraded pharma pages on 2026-08-03:

| Page | Post ID | FAQs |
|------|---------|------|
| WHO GMP | 10448 | 4 FAQs (FDA vs WHO, certificate access, country support, audit) |
| COA MSDS | 10403 | 4 FAQs (pre-order COA, NABL lab, DMF support, API list) |
| Third Party Manufacturing | 10430 | 4 FAQs (what is 3PM, regulated markets, MOQ, timeline) |
| Steroid API Mumbai | 10710 | 4 FAQs (Mumbai supply, MOQ, pharmacopeial grade, export) |
| Hyderabad API | 10717 | 4 FAQs (direct Hyderabad supply, grades, MOQ, export) |

Schema injected as `<!-- AARISE-SCHEMA-START -->` blocks in post content.

---

## What AI Crawlers See

With both llms.txt files live and FAQPage schema on 5 pages:
- ChatGPT, Gemini, Claude, Perplexity crawlers find the llms.txt and understand the site's purpose
- FAQPage schema creates AI-citation-ready Q&A pairs for the most buyer-intent queries
- Organization schema identifies Aarise as a named entity in schema.org's knowledge graph

This is the foundation for GEO (Generative Engine Optimization) — getting cited in AI-generated answers.
