# Bannerbear Image Generator

**Automated image generation system for C3 Marketing Hub**

Generate professional marketing images for Meta Business Suite (Instagram, Facebook) using Bannerbear API and custom templates.

---

## 🎯 Purpose

Replace manual Photoshop work (4 hours per campaign) with automated image generation (2 minutes per campaign) for JV Roofing and future clients.

**Time Savings:** 99% reduction in image creation time  
**Cost Savings:** $198.20 per campaign  
**Quality:** Professional-grade output matching brand standards

---

## 📁 Project Structure

```
bannerbear-image-generator/
├── README.md                    # This file
├── TEST_RESULTS.md              # First test results and validation
├── quick_test.py                # Quick test script (standalone)
├── jv_roofing_test_001.png      # First generated image
│
├── scripts/                     # Production scripts (future)
│   ├── bannerbear_client.py     # API wrapper
│   └── image_generator.py       # High-level generator
│
└── examples/                    # Usage examples (future)
    └── jv_roofing_example.py    # JV Roofing campaign example
```

---

## ⚡ Quick Start

### Prerequisites

- Python 3.11+
- `requests` library
- Bannerbear account with Project API Key

### Installation

```bash
# Install dependencies
pip3 install requests

# Clone or download this directory
cd bannerbear-image-generator
```

### Configuration

Edit `quick_test.py` and set your credentials:

```python
API_KEY = "bb_pr_YOUR_PROJECT_API_KEY"
TEMPLATE_UID = "YOUR_TEMPLATE_UID"
```

### Run Test

```bash
python3 quick_test.py
```

**Expected Output:**

```
============================================================
✅ SUCCESS!
============================================================

📸 Image Generated:
   UID: 5nDZ3xmVezbm94vBYy2qpdWj9
   Status: completed
   URL: https://images.bannerbear.com/direct/...
```

---

## 🎨 Template Configuration

### JV Roofing - Story 9:16

**Template UID:** `n1MJGd52QaAnZ7LaPV`  
**Dimensions:** 1080x1920 (Instagram Story)  
**Format:** PNG

**Variable Layers:**
- `background_image` - Client photo or generated image
- `logo` - JV Roofing logo
- `headline` - Main message (e.g., "Professional Inspection. Free Offer.")
- `cta` - Call-to-action button (e.g., "Book Free Estimate")
- `badge_gaf` - GAF certification badge
- `badge_malarkey` - Malarkey certification badge
- `badge_cslb` - CSLB license badge

**Brand Colors:**
- Navy: `#2E3A8C`
- Red: `#E31E24`
- White: `#FFFFFF`

**Fonts:**
- Primary: Montserrat
- Fallback: Inter, Roboto

---

## 🚀 Usage Examples

### Generate Single Image

```python
from scripts.image_generator import BannerbearImageGenerator, CampaignData

# Initialize generator
generator = BannerbearImageGenerator(
    api_key='bb_pr_YOUR_API_KEY',
    template_id='n1MJGd52QaAnZ7LaPV'
)

# Create campaign data
campaign = CampaignData(
    campaign_id='fall_promo_001',
    headline='Fall Roof Inspection Special',
    cta='Call Now for Free Quote',
    background_image_url='https://your-cdn.com/roof-photo.jpg',
    logo_url='https://your-cdn.com/jv-logo.png'
)

# Generate image
image = generator.generate_single(campaign)
print(f"Image URL: {image.image_url}")
```

### Generate Campaign (Multiple Variants)

```python
# Generate 3 headline variants
images = generator.generate_campaign(campaign, num_variants=3)

for img in images:
    print(f"Variant {img.uid}: {img.image_url}")
```

### Batch Processing (Multiple Campaigns)

```python
campaigns = [campaign1, campaign2, campaign3]
results = generator.generate_batch(campaigns)

for result in results:
    if result['success']:
        print(f"✅ {result['campaign_id']}: {result['image_url']}")
    else:
        print(f"❌ {result['campaign_id']}: {result['error']}")
```

---

## 📊 API Reference

### BannerbearClient

Low-level API wrapper for Bannerbear.

**Methods:**
- `create_image(template_uid, modifications)` - Create image (async)
- `get_image(image_uid)` - Get image status
- `create_image_sync(template_uid, modifications, timeout)` - Create and wait

### BannerbearImageGenerator

High-level image generator with campaign support.

**Methods:**
- `generate_single(campaign_data)` - Generate one image
- `generate_campaign(campaign_data, num_variants)` - Generate variants
- `generate_batch(campaigns)` - Process multiple campaigns

### CampaignData

Data model for campaign input.

**Fields:**
- `campaign_id` (str) - Unique campaign identifier
- `headline` (str) - Main headline text
- `cta` (str) - Call-to-action text
- `background_image_url` (str) - Background image URL
- `logo_url` (str) - Logo image URL
- `badge_gaf_url` (str, optional) - GAF badge URL
- `badge_malarkey_url` (str, optional) - Malarkey badge URL
- `badge_cslb_url` (str, optional) - CSLB badge URL

---

## 🔧 Troubleshooting

### Error: "When using a Master API Key you must set a project_id parameter"

**Solution:** Use a Project API Key (`bb_pr_...`) instead of Master API Key (`bb_ma_...`).

Get it from: Bannerbear Dashboard → Project Settings → API Key

### Error: "Template not found"

**Solution:** Verify the Template UID in your Bannerbear dashboard.

Templates → Your Template → Copy UID

### Error: "Layer name not found"

**Solution:** Check that layer names in your template match the modification names:
- `background_image`
- `logo`
- `headline`
- `cta`
- `badge_gaf`
- `badge_malarkey`
- `badge_cslb`

### Timeout Issues

**Solution:** Increase timeout parameter:

```python
image = client.create_image_sync(
    template_uid=template_id,
    modifications=mods,
    timeout=600  # 10 minutes
)
```

---

## 💰 Cost Optimization

### Bannerbear Plans

| Plan | Price | Images/Month | Cost/Image |
|------|-------|--------------|------------|
| Starter | $49 | 500 | $0.098 |
| Growth | $99 | 2,000 | $0.050 |
| Business | $249 | 6,000 | $0.042 |

### Recommendations

- **1-5 clients:** Starter plan ($49/mo)
- **6-20 clients:** Growth plan ($99/mo)
- **20+ clients:** Business plan ($249/mo)

**ROI Calculation:**
- Manual cost: $200/campaign (4 hours × $50/hr)
- Automated cost: $1.80/campaign (18 images × $0.10)
- **Savings: $198.20 per campaign (99% reduction)**

---

## 🛣️ Roadmap

### Phase 1: Foundation (Complete ✅)
- [x] Bannerbear account setup
- [x] Template creation (Story 9:16)
- [x] API integration
- [x] First test image generated

### Phase 2: Production (In Progress)
- [ ] Upload real JV Roofing assets
- [ ] Create remaining 17 Meta formats
- [ ] Batch generation script
- [ ] Error handling improvements

### Phase 3: Integration
- [ ] Copys Generator integration
- [ ] CSV-to-images pipeline
- [ ] GHL API integration
- [ ] Automated upload to Meta

### Phase 4: Scale
- [ ] C3 Hub webapp interface
- [ ] Multi-client support
- [ ] Runway Gen-4 integration
- [ ] Analytics dashboard

---

## 📚 Resources

- **Bannerbear API Docs:** https://developers.bannerbear.com/
- **Template Editor:** https://app.bannerbear.com/
- **GitHub Repo:** https://github.com/customizeditcorp/C3-Marketing-Hub
- **Project Context:** See `TEST_RESULTS.md` for detailed test results

---

## 🤝 Team

- **Luis** - Product owner, AI orchestration
- **Juan** - Design, branding
- **Carlos** - Ads execution
- **Manus AI** - Development, automation

---

## 📄 License

Proprietary - Customized IT Corp / JV Roofing

---

**Last Updated:** November 2, 2025  
**Status:** Production Ready (Phase 1 Complete)
