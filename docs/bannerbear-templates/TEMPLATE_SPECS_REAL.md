# JV Roofing - Bannerbear Templates Specifications

**Documentación de templates reales creados manualmente en Bannerbear**

---

## 📊 Templates Overview

| Template Name | UID | Dimensions | Format | Status |
|---------------|-----|------------|--------|--------|
| **JV Roofing - Stories 9:16** | `l9E7G65kozz35PLe3R` | 1080×1920 | Vertical (Instagram Stories/Reels) | ✅ Active |
| **JV Roofing - Feed 4:5** | `Kp21rAZj1y3eb6eLnd` | 1080×1350 | Portrait (Instagram Feed) | ✅ Active |
| **JV Roofing - Feed 1:1** | `8BK3vWZJ7a3y5Jzk1a` | 1080×1080 | Square (Instagram/Facebook Feed) | ✅ Active |

---

## 🎨 Template Structure

**All templates share the same layer structure:**

### Layers (10 total)

1. **background solid color** - Fondo sólido de color
   - Type: Color fill
   - Default: Transparent or brand color

2. **background_image** - Foto principal
   - Type: Image
   - Variable: Yes
   - Default: Worker on roof photo

3. **headline** - Texto principal
   - Type: Text
   - Variable: Yes
   - Example: "Leaking Roof? Storm Damage?"

4. **subtitle** - Texto secundario
   - Type: Text
   - Variable: Yes
   - Example: "⭐5.0 Licensed Roofers • Serving SLO Since 2010"

5. **cta** - Call to action
   - Type: Text
   - Variable: Yes
   - Example: "Book Free Estimate"

6. **badge_gaf** - Certificación GAF
   - Type: Image
   - Variable: Yes
   - Asset: badge_gaf.png

7. **badge_malarkey** - Certificación Malarkey
   - Type: Image
   - Variable: Yes
   - Asset: badge_malarkey.png

8. **badge_cslb** - Licencia CSLB
   - Type: Image
   - Variable: Yes
   - Asset: badge_cslb.png

9. **background solid color top** - Fondo superior
   - Type: Color fill
   - Default: Brand color overlay

10. **logo** - Logo JV Roofing
    - Type: Image
    - Variable: Yes
    - Asset: JVrofiinglogoFullcolor.svg

---

## 🎨 Brand Colors

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Navy Blue** | `#343585` | Primary brand color, backgrounds |
| **Red** | `#E52933` | CTA buttons, accents |
| **White** | `#FFFFFF` | Text, overlays |

---

## 📐 Template Details

### 1. Stories 9:16 (1080×1920)

**Format:** Vertical  
**Use Case:** Instagram Stories, Instagram Reels, Facebook Stories  
**Template UID:** `l9E7G65kozz35PLe3R`

**Layout:**
- Logo positioned in upper area
- Background image covers full canvas
- Headline and subtitle in middle-lower section
- CTA button below subtitle
- 3 badges arranged horizontally at bottom
- Navy overlay on top section
- White/Navy color scheme for text

**Preview URL:**
```
https://images.bannerbear.com/direct/5OPnVJ1PJJDvZA6rYb/templates/000/000/303/081/l9E7G65kozz35PLe3R/76b23d036b864d206d81191acfa3194d3944399c.png
```

**Generated Example:**
```
https://images.bannerbear.com/direct/5OPnVJ1PJJDvZA6rYb/requests/000/112/891/263/DdWb1LGkNYN8wg2Z670OKvRAP/9458618a4868b8a3da4a61ae6a3194a81ee47785.png
```

---

### 2. Feed 4:5 (1080×1350)

**Format:** Portrait  
**Use Case:** Instagram Feed (portrait posts)  
**Template UID:** `Kp21rAZj1y3eb6eLnd`

**Layout:**
- Similar to Stories but more compact vertically
- Logo in upper area
- Background image optimized for 4:5 ratio
- Text elements positioned for portrait viewing
- CTA and badges at bottom
- Maintains brand color scheme

**Preview URL:**
```
https://api.bannerbear.com/v2/templates/Kp21rAZj1y3eb6eLnd/preview
```

**Generated Example:**
```
https://images.bannerbear.com/direct/5OPnVJ1PJJDvZA6rYb/requests/000/112/891/335/MRj52Zwoa6xr4X70YxWkdO3eE/42b9a92f325bfce8d5dced5e009012dce91638de.png
```

---

### 3. Feed 1:1 (1080×1080)

**Format:** Square  
**Use Case:** Instagram Feed, Facebook Feed  
**Template UID:** `8BK3vWZJ7a3y5Jzk1a`

**Layout:**
- Square format optimized for feed visibility
- Logo positioned top center or top left
- Background image fills square canvas
- Text elements centered or positioned for balance
- CTA and badges arranged to fit square format
- Most compact layout of the three

**Preview URL:**
```
https://api.bannerbear.com/v2/templates/8BK3vWZJ7a3y5Jzk1a/preview
```

**Generated Example:**
```
https://images.bannerbear.com/direct/5OPnVJ1PJJDvZA6rYb/requests/000/112/891/386/nE38ekNX9Qn3X2OgYMamprWxZ/b8f33dbe917febec5644d7e501367a87dd44c98c.png
```

---

## 📦 Assets

**All assets are stored in GitHub:**

```
C3-Marketing-Hub/assets/jv-roofing/
├── JVrofiinglogoFullcolor.svg       (Logo - SVG vectorial)
├── 222A2584copia.jpg                (Background photo - Worker on roof)
├── badge_gaf.png                    (GAF Certified badge)
├── badge_malarkey.png               (Malarkey Certified badge)
└── badge_cslb.png                   (CSLB License badge)
```

**GitHub Raw URLs:**
- Logo: `https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/JVrofiinglogoFullcolor.svg`
- Background: `https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/222A2584copia.jpg`
- Badge GAF: `https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/badge_gaf.png`
- Badge Malarkey: `https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/badge_malarkey.png`
- Badge CSLB: `https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/badge_cslb.png`

---

## 🔧 API Usage

### Generate Image Example

```python
import requests

API_KEY = "bb_pr_68c446c743c4b27916126868d25fa3"
TEMPLATE_UID = "l9E7G65kozz35PLe3R"  # Stories 9:16

payload = {
    "template": TEMPLATE_UID,
    "modifications": [
        {
            "name": "background_image",
            "image_url": "https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/222A2584copia.jpg"
        },
        {
            "name": "logo",
            "image_url": "https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/JVrofiinglogoFullcolor.svg"
        },
        {
            "name": "headline",
            "text": "Leaking Roof? Storm Damage?"
        },
        {
            "name": "subtitle",
            "text": "⭐5.0 Licensed Roofers • Serving SLO Since 2010"
        },
        {
            "name": "cta",
            "text": "Book Free Estimate"
        },
        {
            "name": "badge_gaf",
            "image_url": "https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/badge_gaf.png"
        },
        {
            "name": "badge_malarkey",
            "image_url": "https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/badge_malarkey.png"
        },
        {
            "name": "badge_cslb",
            "image_url": "https://raw.githubusercontent.com/customizeditcorp/C3-Marketing-Hub/main/assets/jv-roofing/badge_cslb.png"
        }
    ]
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://api.bannerbear.com/v2/images",
    headers=headers,
    json=payload
)

print(response.json())
```

---

## ✅ Validation

**All templates have been validated:**

- ✅ Layouts match manual designs created in Bannerbear dashboard
- ✅ All 10 layers present and functional
- ✅ Assets load correctly from GitHub
- ✅ Brand colors applied consistently
- ✅ Text is legible and well-positioned
- ✅ Badges visible and properly sized
- ✅ Images generated successfully via API

**Test images generated:** 2025-11-05  
**Validated by:** Luis (Client)  
**Status:** Production Ready ✅

---

## 📝 Notes

1. **Template positions are fixed** - Layouts were manually adjusted in Bannerbear dashboard for optimal visual balance
2. **API only allows modification of content** - Cannot change positions via API, only text and images
3. **SVG support** - Logo uses SVG for scalability across all formats
4. **Asset hosting** - All assets hosted on GitHub for reliability and version control
5. **Copy variations** - Text can be modified per campaign while maintaining layout integrity

---

## 🚀 Next Steps

1. ✅ Templates created and validated
2. ✅ Assets uploaded to GitHub
3. ✅ API integration tested
4. ⏳ Batch generation script ready
5. ⏳ Integration with GHL workflow
6. ⏳ Webhook automation setup
7. ⏳ Production deployment

---

**Last Updated:** 2025-11-05  
**Created By:** Luis (manual) + Manus (documentation)  
**Template Designer:** Claude (wireframes) + Luis (final layouts)
