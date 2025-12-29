"""
Medical Image Search Functions
Search and retrieve medical image information
"""

from typing import List, Optional
from medical_images.data import (
    MEDICAL_IMAGES_DATABASE,
    get_images_by_category,
    get_images_by_type,
    MedicalImage
)


def search_images(query: str, category: Optional[str] = None, image_type: Optional[str] = None) -> List[MedicalImage]:
    """
    Search medical images
    
    Args:
        query: Search query
        category: Optional category filter
        image_type: Optional image type filter
        
    Returns:
        List of matching MedicalImage objects
    """
    if not query:
        return []
    
    query_lower = query.lower().strip()
    
    # Get images to search
    images_to_search = MEDICAL_IMAGES_DATABASE
    if category:
        images_to_search = get_images_by_category(category)
    if image_type:
        images_to_search = [img for img in images_to_search if img.image_type == image_type]
    
    results = []
    for img in images_to_search:
        # Search in title, description, findings, diagnosis
        if (query_lower in img.title.lower() or
            query_lower in img.title_vn.lower() or
            query_lower in img.description.lower() or
            query_lower in img.findings.lower() or
            query_lower in img.diagnosis.lower()):
            results.append(img)
    
    return results


def get_image_info(image_id: str) -> Optional[MedicalImage]:
    """
    Get detailed information about a medical image
    
    Args:
        image_id: Image ID
        
    Returns:
        MedicalImage object or None
    """
    for img in MEDICAL_IMAGES_DATABASE:
        if img.id == image_id:
            return img
    return None

