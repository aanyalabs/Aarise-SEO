# Pharma Site — Content Drafts & Briefs

## Page 1: Active Pharmaceutical Ingredients (API)

**Target URL:** `aarisepharma.com/active-pharmaceutical-ingredients/`  
**Target keywords:** active pharmaceutical ingredients, api pharmaceutical, api manufacturing, api pharma, active pharmaceutical ingredient manufacturers  
**Volume:** 500K (head) + 500/month (realistic long-tail)  
**Competition:** Low (index 6-25)  
**Status:** BRIEF READY — needs writing

### Content Brief
- H1: "Active Pharmaceutical Ingredients (API) — Manufacturer & Exporter from India"
- Open with a direct definition (40-60 words for AEO): "Active Pharmaceutical Ingredients (APIs) are the biologically active components in a drug that produce the intended therapeutic effect. Aarise Pharmaceuticals manufactures pharmaceutical-grade APIs including steroids, peptides, and generic drug substances at our GMP-certified facility in Haridwar, India."
- Sections: What is an API? → Our API product range → Manufacturing process → Quality certifications → Export markets → FAQ
- FAQ schema required

---

## Page 2: API Manufacturing Plant India

**Target URL:** `aarisepharma.com/api-manufacturing-plant-india/`  
**Target keywords:** pharmaceutical manufacturing plant (+900% YoY), api manufacturing industry, api manufacturer india  
**Volume:** 500/month  
**Competition:** Low (index 6)  
**Status:** BRIEF READY — needs writing

### Content Brief
- H1: "API Manufacturing Plant in Haridwar, India — GMP Certified"
- Include: facility details, certifications, capacity, product categories manufactured
- FAQ schema required

---

## Page 3: Pharma Exporter India to Latin America

**Target URL:** `aarisepharma.com/pharma-exporter-india-latin-america/`  
**Target keywords:** pharma exporter india latin america, generic drug manufacturer india, pharmaceutical supplier india  
**Volume:** 500/month  
**Competition:** Low  
**Status:** BRIEF READY — needs writing

### Content Brief
- H1: "Pharmaceutical Exporter from India to Latin America — APIs & Generic Formulations"
- Target markets: Mexico, Peru, Paraguay, Bolivia, Colombia
- Sections: Why India? → Our export process → Regulatory compliance by country → Products → Contact

---

## FAQ Schema for Dispersible Tablets Page (HIGHEST PRIORITY)

Add this JSON-LD to the dispersible tablets page `<head>` or via Yoast custom schema:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What are dispersible tablets used for?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dispersible tablets are used for patients who have difficulty swallowing standard tablets, including children and the elderly. They dissolve in water to form a suspension. Common uses include pain relief (paracetamol), antibiotics (amoxicillin), and antacids."
      }
    },
    {
      "@type": "Question",
      "name": "What is a dispersible tablet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A dispersible tablet is a solid oral dosage form designed to be dissolved or dispersed in water before administration. It breaks down rapidly in liquid, forming a uniform suspension that is easier to swallow than a conventional tablet."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between dispersible and soluble tablets?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dispersible tablets form a suspension (particles remain but are distributed evenly in liquid), while soluble tablets dissolve completely to form a clear solution. Both are designed for patients who cannot swallow standard tablets."
      }
    },
    {
      "@type": "Question",
      "name": "Who manufactures dispersible tablets in India?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Aarise Pharmaceuticals is a GMP-certified dispersible tablet manufacturer in Haridwar, India. We produce dispersible tablet formulations for domestic and international pharmaceutical markets."
      }
    }
  ]
}
```

**How to add in Yoast:**
WordPress → Edit the dispersible tablets page → Yoast SEO → Schema → Custom Schema → paste JSON
