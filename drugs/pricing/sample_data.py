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

