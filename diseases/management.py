"""
Disease Management and Statistics System
Quản lý và thống kê bệnh theo chuyên khoa
"""

from typing import Dict, List, Optional
from diseases.data import Disease, DISEASES_DATABASE, get_diseases_by_category, get_category_list


def get_specialty_statistics() -> Dict[str, Dict]:
    """
    Thống kê bệnh theo chuyên khoa
    
    Returns:
        Dictionary với thông tin thống kê cho mỗi chuyên khoa
    """
    stats = {}
    categories = get_category_list()
    
    for category in categories:
        diseases = get_diseases_by_category(category)
        stats[category] = {
            "total_diseases": len(diseases),
            "disease_ids": [d.id for d in diseases],
            "disease_names": [d.name for d in diseases],
            "disease_names_vn": [d.name_vn for d in diseases],
        }
    
    return stats


def get_disease_by_id(disease_id: str) -> Optional[Disease]:
    """
    Tìm bệnh theo ID
    
    Args:
        disease_id: ID của bệnh
        
    Returns:
        Disease object hoặc None
    """
    for disease in DISEASES_DATABASE:
        if disease.id == disease_id:
            return disease
    return None


def search_diseases_by_keyword(keyword: str, category: Optional[str] = None) -> List[Disease]:
    """
    Tìm kiếm bệnh theo từ khóa (tên, định nghĩa, triệu chứng)
    
    Args:
        keyword: Từ khóa tìm kiếm
        category: Lọc theo chuyên khoa (optional)
        
    Returns:
        List các bệnh phù hợp
    """
    keyword_lower = keyword.lower()
    diseases_to_search = get_diseases_by_category(category) if category else DISEASES_DATABASE
    
    results = []
    for disease in diseases_to_search:
        # Tìm trong tên (tiếng Anh và tiếng Việt)
        if (keyword_lower in disease.name.lower() or 
            keyword_lower in disease.name_vn.lower()):
            results.append(disease)
            continue
        
        # Tìm trong định nghĩa
        if keyword_lower in disease.definition.lower():
            results.append(disease)
            continue
        
        # Tìm trong triệu chứng
        for symptom in disease.symptoms:
            if keyword_lower in symptom.lower():
                results.append(disease)
                break
        
        # Tìm trong nguyên nhân
        for cause in disease.causes:
            if keyword_lower in cause.lower():
                results.append(disease)
                break
    
    return results


def get_diseases_by_icd10(icd10_code: str) -> List[Disease]:
    """
    Tìm bệnh theo mã ICD-10
    
    Args:
        icd10_code: Mã ICD-10
        
    Returns:
        List các bệnh có mã ICD-10 tương ứng
    """
    results = []
    for disease in DISEASES_DATABASE:
        if icd10_code in disease.icd10_codes:
            results.append(disease)
    return results


def get_diseases_by_drug(drug_name: str) -> List[Disease]:
    """
    Tìm bệnh sử dụng một loại thuốc
    
    Args:
        drug_name: Tên thuốc
        
    Returns:
        List các bệnh sử dụng thuốc đó
    """
    drug_lower = drug_name.lower()
    results = []
    for disease in DISEASES_DATABASE:
        for drug in disease.related_drugs:
            if drug_lower in drug.lower():
                results.append(disease)
                break
    return results


def get_specialty_summary() -> str:
    """
    Tóm tắt thống kê tất cả chuyên khoa
    
    Returns:
        String tóm tắt
    """
    stats = get_specialty_statistics()
    total_diseases = len(DISEASES_DATABASE)
    
    summary = f"=== TỔNG QUAN HỆ THỐNG BỆNH ===\n"
    summary += f"Tổng số bệnh: {total_diseases}\n"
    summary += f"Số chuyên khoa: {len(stats)}\n\n"
    
    summary += "=== CHI TIẾT THEO CHUYÊN KHOA ===\n"
    for category, info in sorted(stats.items()):
        summary += f"\n{category}:\n"
        summary += f"  - Số bệnh: {info['total_diseases']}\n"
        summary += f"  - Danh sách: {', '.join(info['disease_names_vn'])}\n"
    
    return summary


def export_specialty_data(category: str) -> Dict:
    """
    Xuất dữ liệu của một chuyên khoa
    
    Args:
        category: Tên chuyên khoa
        
    Returns:
        Dictionary chứa dữ liệu bệnh của chuyên khoa
    """
    diseases = get_diseases_by_category(category)
    return {
        "category": category,
        "total": len(diseases),
        "diseases": [
            {
                "id": d.id,
                "name": d.name,
                "name_vn": d.name_vn,
                "icd10_codes": d.icd10_codes,
                "related_drugs": d.related_drugs,
                "related_scores": d.related_scores,
            }
            for d in diseases
        ]
    }

