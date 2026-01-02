"""
Drug Pricing Module
Pricing information for Vietnamese market
"""

from typing import Dict, Optional

# Drug pricing data structure
# Format: {drug_name: {price_vnd: float, price_usd: Optional[float], source: str, last_updated: str}}
DRUG_PRICING = {
    # Example structure - to be populated with actual data
    # "Paracetamol": {
    #     "price_vnd": 5000,
    #     "price_usd": 0.2,
    #     "source": "VN Drug Price Database",
    #     "last_updated": "2025-01-30"
    # }
}

def get_drug_price(drug_name: str) -> Optional[Dict]:
    """
    Get pricing information for a drug
    
    Args:
        drug_name: Drug name
    
    Returns:
        Dict with pricing info or None
    """
    return DRUG_PRICING.get(drug_name)


def format_price(price_vnd: float, show_usd: bool = False) -> str:
    """
    Format price for display
    
    Args:
        price_vnd: Price in VND
        show_usd: Show USD equivalent
    
    Returns:
        Formatted price string
    """
    formatted = f"{price_vnd:,.0f} VNĐ"
    if show_usd and price_vnd > 0:
        usd_price = price_vnd / 24000  # Approximate exchange rate
        formatted += f" (~${usd_price:.2f} USD)"
    return formatted


__all__ = ['DRUG_PRICING', 'get_drug_price', 'format_price']

