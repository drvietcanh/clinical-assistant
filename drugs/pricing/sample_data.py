"""
Sample Drug Pricing Data
Example pricing data for Vietnamese market (to be expanded)
"""

from typing import Dict, Optional

# Sample pricing data (VN market)
SAMPLE_DRUG_PRICING: Dict[str, Dict] = {
    "Paracetamol": {
        "price_vnd": 5000,
        "price_usd": 0.21,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 500mg",
        "generic_available": True
    },
    "Amoxicillin": {
        "price_vnd": 15000,
        "price_usd": 0.63,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 500mg",
        "generic_available": True
    },
    "Metformin": {
        "price_vnd": 8000,
        "price_usd": 0.33,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 500mg",
        "generic_available": True
    },
    "Atorvastatin": {
        "price_vnd": 25000,
        "price_usd": 1.04,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 20mg",
        "generic_available": True
    },
    "Omeprazole": {
        "price_vnd": 12000,
        "price_usd": 0.50,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 20mg",
        "generic_available": True
    },
    "Warfarin": {
        "price_vnd": 3000,
        "price_usd": 0.13,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 5mg",
        "generic_available": True
    },
    "Aspirin": {
        "price_vnd": 2000,
        "price_usd": 0.08,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 100mg",
        "generic_available": True
    },
    "Clopidogrel": {
        "price_vnd": 18000,
        "price_usd": 0.75,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 75mg",
        "generic_available": True
    },
    "Furosemide": {
        "price_vnd": 4000,
        "price_usd": 0.17,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 40mg",
        "generic_available": True
    },
    "Amlodipine": {
        "price_vnd": 10000,
        "price_usd": 0.42,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 5mg",
        "generic_available": True
    },
    "Losartan": {
        "price_vnd": 12000,
        "price_usd": 0.50,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "viên 50mg",
        "generic_available": True
    },
    "Insulin Glargine": {
        "price_vnd": 250000,
        "price_usd": 10.42,
        "source": "VN Drug Price Database 2024",
        "last_updated": "2024-12-01",
        "unit": "lọ 1000 IU",
        "generic_available": False
    }
}


def get_sample_pricing(drug_name: str) -> Optional[Dict]:
    """
    Get sample pricing for a drug
    
    Args:
        drug_name: Drug name
    
    Returns:
        Pricing dict or None
    """
    return SAMPLE_DRUG_PRICING.get(drug_name)


__all__ = ['SAMPLE_DRUG_PRICING', 'get_sample_pricing']

