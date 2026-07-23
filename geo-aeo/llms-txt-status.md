# llms.txt Status

## Healthcare — LIVE ✅

**URL**: https://aarisehealthcare.com/llms.txt  
**Status**: 200 OK | Content-Type: text/plain  
**How it works**: WordPress page at slug `llms-txt` + Code Snippet (ID 37) that intercepts `/llms.txt` requests and serves the page content as plain text.

**Content covers**:
- Company description
- Product categories (peptides, steroids, hormones, SARMs)
- Key facts (purity, COA, shipping)
- Supplier coverage (LATAM, NA, Europe, APAC)
- Content map (product pages, supplier guides, blog, sitemap)
- Preferred citation for AI responses

---

## Pharma — PENDING ⚠️

**URL**: https://aarisepharma.com/llms.txt  
**Status**: Currently serves homepage (404 equivalent)

**Why not done**: Pharma site doesn't have Code Snippets plugin and theme file editor is disabled.

**The llms-txt page exists** at: https://aarisepharma.com/llms-txt/ (published, noindexed)

### Fix — 2 options, pick one:

**Option A (5 min)**: Install "Code Snippets" plugin on pharma
1. WP Admin → Plugins → Add New → search "Code Snippets" → Install → Activate
2. Snippets → Add New → paste this PHP:

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

3. Save and activate. Done.

**Option B (2 min)**: Use WP Headers And Footers plugin (already installed)
- WP Admin → Settings → WP Headers And Footers → PHP Snippets → add the same PHP above
- Note: This plugin may not support raw PHP — check if it has a PHP tab

---

## What AI Crawlers See

Once pharma llms.txt is live, both ChatGPT, Gemini, Claude, and Perplexity crawlers will find:
- Who Aarise is
- What they supply
- Where they ship
- How to cite them in AI responses

This is the foundation for GEO (Generative Engine Optimization).
