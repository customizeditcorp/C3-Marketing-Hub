#!/usr/bin/env python3
"""
Bannerbear Quick Test Script
Tests the Bannerbear API integration for JV Roofing template
"""

import requests
import time
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass

# ============================================================================
# CONFIGURATION
# ============================================================================

API_KEY = "bb_pr_68c446c743c4b27916126868d25fa3"
TEMPLATE_UID = "n1MJGd52QaAnZ7LaPV"

# ============================================================================
# EXCEPTIONS
# ============================================================================

class BannerbearError(Exception):
    """Base exception for Bannerbear errors"""
    pass

class BannerbearTimeout(BannerbearError):
    """Raised when image generation times out"""
    pass

# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class BannerbearImage:
    """Represents a generated Bannerbear image"""
    uid: str
    image_url: str
    status: str
    metadata: Optional[Dict] = None

@dataclass
class CampaignData:
    """Campaign input data"""
    campaign_id: str
    headline: str
    cta: str
    background_image_url: str
    logo_url: str
    badge_gaf_url: Optional[str] = None
    badge_malarkey_url: Optional[str] = None
    badge_cslb_url: Optional[str] = None

# ============================================================================
# BANNERBEAR CLIENT
# ============================================================================

class BannerbearClient:
    """Low-level Bannerbear API client"""
    
    BASE_URL = "https://api.bannerbear.com/v2"
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    def create_image(self, template_uid: str, modifications: List[Dict]) -> Dict:
        """Create an image (async)"""
        url = f"{self.BASE_URL}/images"
        payload = {
            "template": template_uid,
            "modifications": modifications
        }
        
        response = self.session.post(url, json=payload)
        
        # Bannerbear returns 202 (Accepted) when image is queued
        if response.status_code not in [200, 202]:
            raise BannerbearError(f"API request failed: {response.status_code} - {response.text}")
        
        return response.json()
    
    def get_image(self, image_uid: str) -> Dict:
        """Get image status"""
        url = f"{self.BASE_URL}/images/{image_uid}"
        response = self.session.get(url)
        
        if response.status_code != 200:
            raise BannerbearError(f"Failed to get image: {response.status_code}")
        
        return response.json()
    
    def create_image_sync(self, template_uid: str, modifications: List[Dict], 
                         timeout: int = 300, poll_interval: int = 3) -> BannerbearImage:
        """Create image and wait for completion"""
        
        # Create image
        result = self.create_image(template_uid, modifications)
        image_uid = result['uid']
        
        # Poll for completion
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                raise BannerbearTimeout(f"Image generation timed out after {timeout}s")
            
            image_data = self.get_image(image_uid)
            status = image_data['status']
            
            if status == 'completed':
                return BannerbearImage(
                    uid=image_uid,
                    image_url=image_data['image_url'],
                    status=status,
                    metadata=image_data
                )
            elif status == 'failed':
                raise BannerbearError(f"Image generation failed: {image_data.get('error')}")
            
            time.sleep(poll_interval)

# ============================================================================
# IMAGE GENERATOR
# ============================================================================

class BannerbearImageGenerator:
    """High-level image generator"""
    
    def __init__(self, api_key: str, template_id: str):
        self.client = BannerbearClient(api_key)
        self.template_id = template_id
    
    def generate_single(self, campaign_data: CampaignData) -> BannerbearImage:
        """Generate a single image"""
        
        modifications = [
            {"name": "headline", "text": campaign_data.headline},
            {"name": "cta", "text": campaign_data.cta},
            {"name": "background_image", "image_url": campaign_data.background_image_url},
            {"name": "logo", "image_url": campaign_data.logo_url}
        ]
        
        if campaign_data.badge_gaf_url:
            modifications.append({
                "name": "badge_gaf",
                "image_url": campaign_data.badge_gaf_url
            })
        
        if campaign_data.badge_malarkey_url:
            modifications.append({
                "name": "badge_malarkey",
                "image_url": campaign_data.badge_malarkey_url
            })
        
        if campaign_data.badge_cslb_url:
            modifications.append({
                "name": "badge_cslb",
                "image_url": campaign_data.badge_cslb_url
            })
        
        return self.client.create_image_sync(
            template_uid=self.template_id,
            modifications=modifications,
            timeout=300
        )

# ============================================================================
# MAIN TEST
# ============================================================================

def main():
    print("="*60)
    print("🧪 BANNERBEAR IMAGE GENERATOR TEST")
    print("="*60)
    print(f"\n📋 Configuration:")
    print(f"   API Key: {API_KEY[:15]}...")
    print(f"   Template: {TEMPLATE_UID}")
    
    try:
        # Initialize generator
        print("\n🚀 Initializing generator...")
        generator = BannerbearImageGenerator(API_KEY, TEMPLATE_UID)
        
        # Test data
        test_campaign = CampaignData(
            campaign_id="test_001",
            headline="Professional Inspection. Free Offer.",
            cta="Book Free Estimate",
            background_image_url="https://images.unsplash.com/photo-1632778149955-e80f8ceca2e8?w=1080",
            logo_url="https://via.placeholder.com/200x200/2E3A8C/FFFFFF?text=JV"
        )
        
        print("\n🎨 Generating test image...")
        print("   (This may take 10-30 seconds...)")
        
        image = generator.generate_single(test_campaign)
        
        print("\n" + "="*60)
        print("✅ SUCCESS!")
        print("="*60)
        print(f"\n📸 Image Generated:")
        print(f"   UID: {image.uid}")
        print(f"   Status: {image.status}")
        print(f"   URL: {image.image_url}")
        print(f"\n🌐 Open this URL in your browser:")
        print(f"   {image.image_url}")
        print("\n" + "="*60)
        
        return True
        
    except BannerbearTimeout as e:
        print(f"\n⏱️  TIMEOUT: {e}")
        print("\nThis usually means:")
        print("  - Template is rendering slowly")
        print("  - Try again in a few minutes")
        return False
        
    except BannerbearError as e:
        print(f"\n❌ ERROR: {e}")
        print("\nTroubleshooting:")
        print("  1. Check API key is valid")
        print("  2. Verify template UID in Bannerbear dashboard")
        print("  3. Check layer names match (background_image, logo, etc)")
        print("  4. Ensure you have images remaining in your plan")
        return False
        
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        print(f"   Type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
