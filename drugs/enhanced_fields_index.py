"""
Enhanced Fields Index System - Hệ thống chỉ mục thống nhất cho 14 Enhanced Fields
Giúp tìm kiếm, sửa chữa, bổ sung fields dễ dàng
"""

from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict
from .drug_database import DRUG_DATABASE
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS

# ============================================================================
# ĐỊNH NGHĨA 14 ENHANCED FIELDS
# ============================================================================

# 6 Fields cơ bản (bắt buộc)
CORE_FIELDS = [
    "mechanism_of_action",
    "monitoring",
    "precautions",
    "pharmacokinetics",
    "storage",
    "black_box_warnings",
]

# 8 Fields bổ sung (tùy chọn nhưng khuyến nghị)
EXTENDED_FIELDS = [
    "drug_interactions",
    "contraindications",  # hoặc contraindications_detail
    "pregnancy_lactation",
    "hepatic_adjustment",
    "overdose_management",
    "reversal_agents",
    "administration_instructions",
    "references",
]

# Tất cả 14 fields
ALL_ENHANCED_FIELDS = CORE_FIELDS + EXTENDED_FIELDS

# Meta fields (bổ sung)
META_FIELDS = [
    "risk_flags",
    "guideline_tags",
    "availability_vietnam",
]

# Tất cả fields (14 + meta)
ALL_FIELDS = ALL_ENHANCED_FIELDS + META_FIELDS

# Field aliases (tên khác nhau nhưng cùng ý nghĩa)
FIELD_ALIASES = {
    "contraindications_detail": "contraindications",
    "contraindications": "contraindications",
}

# ============================================================================
# FIELD METADATA - Thông tin về mỗi field
# ============================================================================

FIELD_METADATA = {
    # === 6 FIELDS CƠ BẢN ===
    "mechanism_of_action": {
        "type": "string",
        "required": True,
        "description": "Cơ chế tác dụng của thuốc",
        "min_length": 50,
        "max_length": 2000,
        "category": "core",
        "searchable": True,
    },
    "monitoring": {
        "type": "list",
        "required": True,
        "description": "Các thông số cần theo dõi",
        "min_items": 1,
        "category": "core",
        "searchable": True,
    },
    "precautions": {
        "type": "list",
        "required": True,
        "description": "Các lưu ý và thận trọng",
        "min_items": 1,
        "category": "core",
        "searchable": True,
    },
    "pharmacokinetics": {
        "type": "dict",
        "required": True,
        "description": "Thông tin dược động học",
        "subfields": ["half_life", "onset", "duration", "protein_binding", "clearance"],
        "category": "core",
        "searchable": False,
    },
    "storage": {
        "type": "string",
        "required": True,
        "description": "Điều kiện bảo quản",
        "min_length": 10,
        "category": "core",
        "searchable": True,
    },
    "black_box_warnings": {
        "type": "string_or_none",
        "required": True,
        "description": "Cảnh báo hộp đen (hoặc None)",
        "category": "core",
        "searchable": True,
    },
    
    # === 8 FIELDS BỔ SUNG ===
    "drug_interactions": {
        "type": "dict",
        "required": False,
        "description": "Tương tác thuốc chi tiết",
        "subfields": ["major", "moderate", "minor"],
        "category": "extended",
        "searchable": True,
    },
    "contraindications": {
        "type": "dict",
        "required": False,
        "description": "Chống chỉ định chi tiết",
        "subfields": ["tuyệt_đối", "tương_đối"],
        "category": "extended",
        "searchable": True,
    },
    "pregnancy_lactation": {
        "type": "dict",
        "required": False,
        "description": "Thông tin thai kỳ và cho con bú",
        "subfields": ["fda_category", "pregnancy_details", "lactation"],
        "category": "extended",
        "searchable": True,
    },
    "hepatic_adjustment": {
        "type": "dict",
        "required": False,
        "description": "Điều chỉnh liều ở suy gan",
        "subfields": ["mild", "moderate", "severe", "notes"],
        "category": "extended",
        "searchable": True,
    },
    "overdose_management": {
        "type": "dict",
        "required": False,
        "description": "Xử trí quá liều",
        "subfields": ["symptoms", "antidote", "treatment", "monitoring"],
        "category": "extended",
        "searchable": True,
    },
    "reversal_agents": {
        "type": "dict_or_none",
        "required": False,
        "description": "Thuốc đối kháng",
        "subfields": ["available", "agents"],
        "category": "extended",
        "searchable": True,
    },
    "administration_instructions": {
        "type": "dict",
        "required": False,
        "description": "Hướng dẫn dùng thuốc",
        "subfields": ["oral", "iv"],
        "category": "extended",
        "searchable": True,
    },
    "references": {
        "type": "dict",
        "required": False,
        "description": "Nguồn tham khảo",
        "subfields": ["primary_sources", "last_updated", "evidence_level"],
        "category": "extended",
        "searchable": True,
    },
    
    # === META FIELDS ===
    "risk_flags": {
        "type": "dict",
        "required": False,
        "description": "Cờ cảnh báo rủi ro",
        "category": "meta",
        "searchable": True,
    },
    "guideline_tags": {
        "type": "dict",
        "required": False,
        "description": "Thẻ hướng dẫn lâm sàng",
        "category": "meta",
        "searchable": True,
    },
    "availability_vietnam": {
        "type": "dict",
        "required": False,
        "description": "Tình trạng có sẵn tại Việt Nam",
        "category": "meta",
        "searchable": True,
    },
}

# ============================================================================
# BUILD INDEX - Xây dựng chỉ mục
# ============================================================================

_field_index = None

def _build_field_index():
    """Xây dựng chỉ mục cho tất cả fields"""
    global _field_index
    
    if _field_index is not None:
        return _field_index
    
    index = {
        "by_field": defaultdict(list),  # field_name -> [(drug_name, has_field, value)]
        "by_drug": {},  # drug_name -> {field: exists, ...}
        "missing_fields": defaultdict(list),  # field_name -> [drug_names missing]
        "complete_drugs": [],  # Drugs with all 14 fields
        "incomplete_drugs": [],  # Drugs missing some fields
    }
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        # Apply overrides if exists
        if drug_name in EXTRA_ENHANCED_FIELDS:
            drug_data = {**drug_data, **EXTRA_ENHANCED_FIELDS[drug_name]}
        
        drug_fields = {}
        missing_fields = []
        
        # Check each field
        for field in ALL_ENHANCED_FIELDS:
            # Check aliases
            field_to_check = FIELD_ALIASES.get(field, field)
            
            has_field = field_to_check in drug_data and drug_data[field_to_check] is not None
            
            # Special handling for black_box_warnings (can be None)
            if field == "black_box_warnings":
                has_field = field_to_check in drug_data  # Exists even if None
            
            drug_fields[field] = has_field
            
            if has_field:
                value = drug_data.get(field_to_check)
                index["by_field"][field].append((drug_name, True, value))
            else:
                missing_fields.append(field)
                index["missing_fields"][field].append(drug_name)
        
        index["by_drug"][drug_name] = drug_fields
        
        # Categorize
        if len(missing_fields) == 0:
            index["complete_drugs"].append(drug_name)
        else:
            index["incomplete_drugs"].append((drug_name, missing_fields))
    
    _field_index = index
    return index

# ============================================================================
# SEARCH FUNCTIONS - Tìm kiếm
# ============================================================================

def get_field_index():
    """Lấy chỉ mục fields (build nếu chưa có)"""
    return _build_field_index()

def find_drugs_with_field(field_name: str, has_field: bool = True) -> List[str]:
    """
    Tìm thuốc có/không có field
    
    Args:
        field_name: Tên field
        has_field: True nếu tìm thuốc có field, False nếu tìm thuốc thiếu field
    
    Returns:
        List of drug names
    """
    index = get_field_index()
    field = FIELD_ALIASES.get(field_name, field_name)
    
    if has_field:
        return [drug for drug, has, _ in index["by_field"].get(field, []) if has]
    else:
        return index["missing_fields"].get(field, [])

def find_drugs_missing_fields(field_names: List[str], missing_all: bool = False) -> List[Tuple[str, List[str]]]:
    """
    Tìm thuốc thiếu fields
    
    Args:
        field_names: List tên fields cần kiểm tra
        missing_all: True nếu phải thiếu TẤT CẢ fields, False nếu thiếu BẤT KỲ field nào
    
    Returns:
        List of (drug_name, missing_fields)
    """
    index = get_field_index()
    results = []
    
    for drug_name, drug_fields in index["by_drug"].items():
        missing = [f for f in field_names if not drug_fields.get(f, False)]
        
        if missing_all:
            if len(missing) == len(field_names):
                results.append((drug_name, missing))
        else:
            if missing:
                results.append((drug_name, missing))
    
    return results

def find_drugs_with_complete_fields(count: int = 14) -> List[str]:
    """
    Tìm thuốc có đủ số lượng fields
    
    Args:
        count: Số lượng fields cần có (mặc định 14)
    
    Returns:
        List of drug names
    """
    index = get_field_index()
    
    if count == 14:
        return index["complete_drugs"]
    
    results = []
    for drug_name, drug_fields in index["by_drug"].items():
        field_count = sum(1 for has_field in drug_fields.values() if has_field)
        if field_count >= count:
            results.append(drug_name)
    
    return results

def get_drug_field_status(drug_name: str) -> Dict[str, bool]:
    """
    Lấy trạng thái fields của một thuốc
    
    Returns:
        Dict {field_name: has_field}
    """
    index = get_field_index()
    return index["by_drug"].get(drug_name, {})

def search_fields_by_content(query: str, field_name: Optional[str] = None) -> List[Tuple[str, str, str]]:
    """
    Tìm kiếm trong nội dung của fields
    
    Args:
        query: Từ khóa tìm kiếm
        field_name: Giới hạn trong field cụ thể (tùy chọn)
    
    Returns:
        List of (drug_name, field_name, matched_content)
    """
    query_lower = query.lower()
    results = []
    
    fields_to_search = [field_name] if field_name else ALL_ENHANCED_FIELDS
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        # Apply overrides
        if drug_name in EXTRA_ENHANCED_FIELDS:
            drug_data = {**drug_data, **EXTRA_ENHANCED_FIELDS[drug_name]}
        
        for field in fields_to_search:
            field_to_check = FIELD_ALIASES.get(field, field)
            
            if field_to_check not in drug_data:
                continue
            
            value = drug_data[field_to_check]
            
            # Search in value
            if isinstance(value, str):
                if query_lower in value.lower():
                    # Extract snippet
                    idx = value.lower().find(query_lower)
                    snippet = value[max(0, idx-50):idx+len(query)+50]
                    results.append((drug_name, field, snippet))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str) and query_lower in item.lower():
                        results.append((drug_name, field, item))
            elif isinstance(value, dict):
                # Search in dict values
                for k, v in value.items():
                    if isinstance(v, str) and query_lower in v.lower():
                        results.append((drug_name, field, f"{k}: {v}"))
                    elif isinstance(v, list):
                        for item in v:
                            if isinstance(item, str) and query_lower in item.lower():
                                results.append((drug_name, field, item))
    
    return results

# ============================================================================
# STATISTICS - Thống kê
# ============================================================================

def get_field_statistics() -> Dict:
    """Thống kê về fields"""
    index = get_field_index()
    
    total_drugs = len(DRUG_DATABASE)
    
    stats = {
        "total_drugs": total_drugs,
        "complete_drugs": len(index["complete_drugs"]),
        "incomplete_drugs": len(index["incomplete_drugs"]),
        "field_coverage": {},
        "missing_field_counts": {},
    }
    
    # Coverage for each field
    for field in ALL_ENHANCED_FIELDS:
        has_count = len(find_drugs_with_field(field, has_field=True))
        missing_count = len(find_drugs_with_field(field, has_field=False))
        
        stats["field_coverage"][field] = {
            "has": has_count,
            "missing": missing_count,
            "coverage_percent": (has_count / total_drugs * 100) if total_drugs > 0 else 0,
        }
    
    # Missing field counts
    for drug_name, missing_fields in index["incomplete_drugs"]:
        count = len(missing_fields)
        if count not in stats["missing_field_counts"]:
            stats["missing_field_counts"][count] = 0
        stats["missing_field_counts"][count] += 1
    
    return stats

def print_field_statistics():
    """In thống kê fields"""
    stats = get_field_statistics()
    
    print("=" * 80)
    print("THỐNG KÊ ENHANCED FIELDS")
    print("=" * 80)
    print(f"\nTổng số thuốc: {stats['total_drugs']}")
    print(f"Thuốc đủ 14 fields: {stats['complete_drugs']} ({stats['complete_drugs']/stats['total_drugs']*100:.1f}%)")
    print(f"Thuốc thiếu fields: {stats['incomplete_drugs']} ({stats['incomplete_drugs']/stats['total_drugs']*100:.1f}%)")
    
    print("\n" + "=" * 80)
    print("ĐỘ PHỦ SÓNG TỪNG FIELD")
    print("=" * 80)
    print(f"\n{'Field':<30} {'Có':<10} {'Thiếu':<10} {'% Phủ sóng':<15}")
    print("-" * 80)
    
    for field, data in sorted(stats["field_coverage"].items()):
        has = data["has"]
        missing = data["missing"]
        coverage = data["coverage_percent"]
        print(f"{field:<30} {has:<10} {missing:<10} {coverage:>6.1f}%")
    
    print("\n" + "=" * 80)
    print("PHÂN BỐ SỐ LƯỢNG FIELD THIẾU")
    print("=" * 80)
    for count in sorted(stats["missing_field_counts"].keys()):
        drug_count = stats["missing_field_counts"][count]
        print(f"Thiếu {count} field(s): {drug_count} thuốc")

# ============================================================================
# FIELD TEMPLATES - Template cho từng field
# ============================================================================

def get_field_template(field_name: str) -> Dict:
    """Lấy template cho một field"""
    from .enhanced_fields_schema import create_enhanced_fields_template
    
    template = create_enhanced_fields_template()
    return template.get(field_name, {})

def get_all_field_templates() -> Dict:
    """Lấy template cho tất cả fields"""
    from .enhanced_fields_schema import create_enhanced_fields_template
    return create_enhanced_fields_template()

