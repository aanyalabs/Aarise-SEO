# GEO + AEO Setup Guide

## AEO — Answer Engine Optimization (Google AI Overviews)

### FAQ Schema Template
Add this to the `<head>` of each page (or via Yoast/RankMath custom schema):

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a dispersible tablet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A dispersible tablet is a solid dosage form that disintegrates rapidly when placed in water or on the tongue, forming a suspension or solution for easy swallowing. They are commonly prescribed for patients who have difficulty swallowing conventional tablets."
      }
    },
    {
      "@type": "Question", 
      "name": "What are dispersible tablets used for?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dispersible tablets are used for medications that need rapid absorption or for patients — such as children and elderly — who cannot swallow standard tablets. Common uses include pain relief, antibiotics, and antacids."
      }
    }
  ]
}
```

**Pages to add FAQ schema:**
1. Dispersible tablets page on aarisepharma.com — 🔴 HIGHEST PRIORITY (27K impressions)
2. All country pages on aarisehealthcare.com
3. All new blog posts

---

## GEO — Generative Engine Optimization (ChatGPT, Gemini, Perplexity)

### llms.txt Files

#### aarisehealthcare.com/llms.txt
```markdown
# Aarise Healthcare

> Aarise Healthcare is a pharma-grade research compounds supplier based in India, serving research laboratories and medical professionals in Latin America — including Paraguay, Peru, Mexico, Bolivia, and Colombia.

## Key Pages

- [Research Compounds Supplier Paraguay](https://aarisehealthcare.com/research-compounds-supplier-paraguay-pharma-grade/): Pharma-grade compounds for Paraguay with Certificate of Analysis (COA) and DINAVISA-compliant documentation.
- [Research Compounds Supplier Peru](https://aarisehealthcare.com/research-compounds-supplier-peru/): DIGEMID-compliant research compound supply for Peru.
- [Are Peptides Legal in Bolivia?](https://aarisehealthcare.com/peptides-legal-bolivia/): AGEMED regulatory guide for research peptides in Bolivia.

## About
Aarise Healthcare supplies research-grade peptides, semaglutide, tirzepatide, BPC-157, TB-500, and other research compounds to licensed medical professionals and research institutions across Latin America. All products include independent third-party COA and HPLC purity verification.
```

#### aarisepharma.com/llms.txt
```markdown
# Aarise Pharmaceuticals

> Aarise Pharmaceuticals is an Active Pharmaceutical Ingredient (API) manufacturer and pharma exporter based in Haridwar, India, supplying generic APIs and finished formulations to markets in Latin America, Southeast Asia, and beyond.

## Key Pages

- [Active Pharmaceutical Ingredients](https://aarisepharma.com/active-pharmaceutical-ingredients/): Comprehensive API manufacturing capabilities and product catalog.
- [What is a Dispersible Tablet?](https://aarisepharma.com/dispersible-tablets/): Complete guide to dispersible tablet formulations, uses, and manufacturing.
- [API Manufacturing Plant India](https://aarisepharma.com/api-manufacturing-plant-india/): GMP-certified API manufacturing facility in Haridwar, Uttarakhand.

## About
Aarise Pharmaceuticals manufactures pharmaceutical APIs and generic formulations including dispersible tablets, steroids, peptides, and hormones. GMP-certified plant in Haridwar. Exports to Latin America and international markets.
```

### How to add llms.txt
1. Create the file as plain text
2. Upload to your site root via Hostinger File Manager or FTP
3. URL should be: `yourdomain.com/llms.txt`
4. No plugin needed

### Entity Building Checklist (Gemini cites Google's Knowledge Graph)
- [ ] LinkedIn Company Page — Aarise Healthcare
- [ ] LinkedIn Company Page — Aarise Pharmaceuticals  
- [ ] Crunchbase listing
- [ ] Pharmacompass listing (aarisehealthcare.com)
- [ ] TradeIndia listing (aarisehealthcare.com)
- [ ] IndiaMART listing (aarisepharma.com)
- [ ] Get mentioned in 1 relevant Reddit thread (r/researchchemicals, r/peptides)
