"""
Mapping Rules cho việc chuẩn hóa cấu trúc field
Định nghĩa các quy tắc chuyển đổi từ cấu trúc cũ sang cấu trúc mới
"""
from typing import Dict, List, Any, Optional, Union
from collections import OrderedDict

# ============================================================================
# CẤU TRÚC CHUẨN
# ============================================================================

STANDARD_STRUCTURES = {
    'pregnancy_lactation': {
        'type': 'dict',
        'required_keys': ['fda_category', 'pregnancy_details', 'lactation'],
        'lactation_nested_keys': ['safety', 'details', 'recommendation']
    },
    'hepatic_adjustment': {
        'type': 'dict',
        'required_keys': ['mild', 'moderate', 'severe', 'notes']
    },
    'overdose_management': {
        'type': 'dict',
        'required_keys': ['symptoms', 'antidote', 'treatment', 'monitoring']
    },
    'drug_interactions': {
        'type': 'dict',
        'required_keys': ['major', 'moderate', 'minor']
    },
    'references': {
        'type': 'dict',
        'required_keys': ['primary_sources', 'last_updated', 'evidence_level']
    }
}

# ============================================================================
# MAPPING RULES - Đổi tên keys
# ============================================================================

KEY_RENAME_MAP = {
    'pregnancy_lactation': {
        'pregnancy_category': 'fda_category',
        'pregnancy_notes': 'pregnancy_details',
        'lactation_details': None  # Cần chuyển thành nested dict
    },
    'hepatic_adjustment': {
        'adjustment': None  # Cần chuyển đổi đặc biệt
    },
    'contraindications': {
        'absolute': 'tuyệt_đối',
        'relative': 'tương_đối'
    },
    'references': {
        'guidelines': 'primary_sources',
        'primary': 'primary_sources',
        'other': None  # Có thể merge vào primary_sources
    }
}

# ============================================================================
# TEMPLATE CHUẨN
# ============================================================================

STANDARD_TEMPLATES = {
    'pregnancy_lactation': {
        'fda_category': '',
        'pregnancy_details': '',
        'lactation': {
            'safety': '',
            'details': '',
            'recommendation': ''
        }
    },
    'hepatic_adjustment': {
        'mild': '',
        'moderate': '',
        'severe': '',
        'notes': ''
    },
    'overdose_management': {
        'symptoms': [],
        'antidote': '',
        'treatment': [],
        'monitoring': ''
    },
    'drug_interactions': {
        'major': [],
        'moderate': [],
        'minor': []
    },
    'references': {
        'primary_sources': [],
        'last_updated': '',
        'evidence_level': ''
    }
}

# ============================================================================
# HÀM CHUYỂN ĐỔI
# ============================================================================

def standardize_pregnancy_lactation(value: Any) -> Dict[str, Any]:
    """
    Chuẩn hóa pregnancy_lactation field
    
    Các trường hợp:
    1. String -> Dict với cấu trúc chuẩn
    2. Dict với lactation_details -> Dict với lactation nested dict
    3. Dict với pregnancy_category/pregnancy_notes -> Đổi tên keys
    4. Dict thiếu keys -> Thêm keys thiếu
    """
    template = STANDARD_TEMPLATES['pregnancy_lactation'].copy()
    
    # Nếu là string, chuyển thành dict
    if isinstance(value, str):
        if value.strip():
            template['pregnancy_details'] = value
        return template
    
    # Nếu không phải dict, trả về template
    if not isinstance(value, dict):
        return template
    
    result = template.copy()
    
    # Xử lý fda_category
    if 'fda_category' in value:
        result['fda_category'] = value['fda_category']
    elif 'pregnancy_category' in value:
        result['fda_category'] = value['pregnancy_category']
    else:
        result['fda_category'] = ''
    
    # Xử lý pregnancy_details
    if 'pregnancy_details' in value:
        result['pregnancy_details'] = value['pregnancy_details']
    elif 'pregnancy_notes' in value:
        result['pregnancy_details'] = value['pregnancy_notes']
    else:
        result['pregnancy_details'] = ''
    
    # Xử lý lactation
    if 'lactation' in value and isinstance(value['lactation'], dict):
        # Đã có cấu trúc nested dict
        result['lactation'] = {
            'safety': value['lactation'].get('safety', ''),
            'details': value['lactation'].get('details', ''),
            'recommendation': value['lactation'].get('recommendation', '')
        }
    elif 'lactation_details' in value:
        # Chuyển lactation_details thành nested dict
        lactation_details = value['lactation_details'] if isinstance(value['lactation_details'], str) else ''
        result['lactation'] = {
            'safety': '',
            'details': lactation_details,
            'recommendation': ''
        }
    else:
        # Giữ nguyên nếu đã có, hoặc dùng template
        if 'lactation' in value:
            result['lactation'] = value['lactation']
        else:
            result['lactation'] = template['lactation'].copy()
    
    return result

def standardize_hepatic_adjustment(value: Any) -> Dict[str, Any]:
    """
    Chuẩn hóa hepatic_adjustment field
    
    Các trường hợp:
    1. Dict thiếu notes -> Thêm notes
    2. Dict với adjustment -> Chuyển đổi (đặt vào notes hoặc phân tích)
    """
    template = STANDARD_TEMPLATES['hepatic_adjustment'].copy()
    
    # Nếu không phải dict, trả về template
    if not isinstance(value, dict):
        return template
    
    result = template.copy()
    
    # Xử lý các keys chuẩn
    for key in ['mild', 'moderate', 'severe']:
        if key in value:
            result[key] = value[key]
    
    # Xử lý notes
    if 'notes' in value:
        result['notes'] = value['notes']
    elif 'adjustment' in value:
        # Chuyển adjustment thành notes
        adjustment_value = value['adjustment']
        if isinstance(adjustment_value, str):
            result['notes'] = adjustment_value
        else:
            result['notes'] = str(adjustment_value)
    
    return result

def standardize_overdose_management(value: Any) -> Dict[str, Any]:
    """
    Chuẩn hóa overdose_management field
    
    Các trường hợp:
    1. String -> Dict với cấu trúc chuẩn
    2. Dict thiếu monitoring -> Thêm monitoring
    3. Dict với treatment là string -> Chuyển thành list
    """
    template = STANDARD_TEMPLATES['overdose_management'].copy()
    
    # Nếu là string, chuyển thành dict
    if isinstance(value, str):
        if value.strip():
            template['treatment'] = [value]
        return template
    
    # Nếu không phải dict, trả về template
    if not isinstance(value, dict):
        return template
    
    result = template.copy()
    
    # Xử lý symptoms
    if 'symptoms' in value:
        if isinstance(value['symptoms'], list):
            result['symptoms'] = value['symptoms']
        elif isinstance(value['symptoms'], str):
            result['symptoms'] = [value['symptoms']] if value['symptoms'].strip() else []
        else:
            result['symptoms'] = []
    
    # Xử lý antidote
    if 'antidote' in value:
        if value['antidote'] is None:
            result['antidote'] = ''
        else:
            result['antidote'] = str(value['antidote'])
    else:
        result['antidote'] = ''
    
    # Xử lý treatment
    if 'treatment' in value:
        if isinstance(value['treatment'], list):
            result['treatment'] = value['treatment']
        elif isinstance(value['treatment'], str):
            # Chuyển string thành list (split by newline hoặc giữ nguyên)
            if '\n' in value['treatment']:
                result['treatment'] = [line.strip() for line in value['treatment'].split('\n') if line.strip()]
            else:
                result['treatment'] = [value['treatment']] if value['treatment'].strip() else []
        else:
            result['treatment'] = []
    
    # Xử lý monitoring
    if 'monitoring' in value:
        result['monitoring'] = str(value['monitoring']) if value['monitoring'] else ''
    else:
        result['monitoring'] = ''
    
    return result

def standardize_contraindications(value: Any) -> Dict[str, Any]:
    """
    Chuẩn hóa contraindications field
    
    Các trường hợp:
    1. List -> Giữ nguyên (tương thích ngược) hoặc chuyển thành dict
    2. Dict với absolute/relative -> Đổi tên thành tuyệt_đối/tương_đối
    """
    # Nếu là list, giữ nguyên (tương thích ngược)
    if isinstance(value, list):
        return value
    
    # Nếu không phải dict, trả về list rỗng
    if not isinstance(value, dict):
        return []
    
    result = {}
    
    # Xử lý đổi tên keys
    if 'tuyệt_đối' in value:
        result['tuyệt_đối'] = value['tuyệt_đối'] if isinstance(value['tuyệt_đối'], list) else []
    elif 'absolute' in value:
        result['tuyệt_đối'] = value['absolute'] if isinstance(value['absolute'], list) else []
    else:
        result['tuyệt_đối'] = []
    
    if 'tương_đối' in value:
        result['tương_đối'] = value['tương_đối'] if isinstance(value['tương_đối'], list) else []
    elif 'relative' in value:
        result['tương_đối'] = value['relative'] if isinstance(value['relative'], list) else []
    else:
        result['tương_đối'] = []
    
    return result

def standardize_drug_interactions(value: Any) -> Dict[str, Any]:
    """
    Chuẩn hóa drug_interactions field
    
    Các trường hợp:
    1. Dict thiếu minor -> Thêm minor
    2. Dict thiếu moderate -> Thêm moderate
    3. Dict thiếu major -> Thêm major
    """
    template = STANDARD_TEMPLATES['drug_interactions'].copy()
    
    # Nếu không phải dict, trả về template
    if not isinstance(value, dict):
        return template
    
    result = template.copy()
    
    # Copy các keys có sẵn
    for key in ['major', 'moderate', 'minor']:
        if key in value:
            if isinstance(value[key], list):
                result[key] = value[key]
            else:
                result[key] = []
    
    return result

def standardize_administration_instructions(value: Any) -> Dict[str, Any]:
    """
    Chuẩn hóa administration_instructions field
    
    Các trường hợp:
    1. String -> Dict với cấu trúc chuẩn
    2. Dict với preparation/administration/monitoring -> Chuyển đổi
    3. Dict rỗng -> Giữ nguyên
    """
    # Nếu là string, chuyển thành dict
    if isinstance(value, str):
        if value.strip():
            return {'oral': {'instructions': value}}
        return {}
    
    # Nếu không phải dict, trả về dict rỗng
    if not isinstance(value, dict):
        return {}
    
    # Nếu dict rỗng, giữ nguyên
    if not value:
        return {}
    
    # Kiểm tra nếu là cấu trúc cũ (preparation, administration, monitoring)
    if 'preparation' in value or 'administration' in value or 'monitoring' in value:
        # Chuyển đổi cấu trúc cũ
        result = {}
        if 'administration' in value:
            admin_value = value['administration']
            if isinstance(admin_value, str):
                # Giả định là oral nếu không rõ
                result['oral'] = {'instructions': admin_value}
        return result
    
    # Giữ nguyên nếu đã là cấu trúc dựa trên đường dùng
    return value

def standardize_references(value: Any) -> Dict[str, Any]:
    """
    Chuẩn hóa references field
    
    Các trường hợp:
    1. String -> Dict với cấu trúc chuẩn
    2. Dict với guidelines/primary/other -> Đổi tên keys
    3. Dict thiếu keys -> Thêm keys thiếu
    """
    template = STANDARD_TEMPLATES['references'].copy()
    
    # Nếu là string, chuyển thành dict
    if isinstance(value, str):
        if value.strip():
            template['primary_sources'] = [value]
        return template
    
    # Nếu không phải dict, trả về template
    if not isinstance(value, dict):
        return template
    
    result = template.copy()
    
    # Xử lý primary_sources
    if 'primary_sources' in value:
        if isinstance(value['primary_sources'], list):
            result['primary_sources'] = value['primary_sources']
        else:
            result['primary_sources'] = []
    else:
        # Kiểm tra các keys cũ
        sources = []
        if 'primary' in value:
            if isinstance(value['primary'], list):
                sources.extend(value['primary'])
            elif isinstance(value['primary'], str):
                sources.append(value['primary'])
        if 'guidelines' in value:
            if isinstance(value['guidelines'], list):
                sources.extend(value['guidelines'])
            elif isinstance(value['guidelines'], str):
                sources.append(value['guidelines'])
        if 'other' in value:
            if isinstance(value['other'], list):
                sources.extend(value['other'])
            elif isinstance(value['other'], str):
                sources.append(value['other'])
        result['primary_sources'] = sources
    
    # Xử lý last_updated
    if 'last_updated' in value:
        result['last_updated'] = str(value['last_updated'])
    else:
        result['last_updated'] = ''
    
    # Xử lý evidence_level
    if 'evidence_level' in value:
        result['evidence_level'] = str(value['evidence_level'])
    else:
        result['evidence_level'] = ''
    
    return result

# ============================================================================
# HÀM TỔNG HỢP
# ============================================================================

STANDARDIZATION_FUNCTIONS = {
    'pregnancy_lactation': standardize_pregnancy_lactation,
    'hepatic_adjustment': standardize_hepatic_adjustment,
    'overdose_management': standardize_overdose_management,
    'contraindications': standardize_contraindications,
    'drug_interactions': standardize_drug_interactions,
    'administration_instructions': standardize_administration_instructions,
    'references': standardize_references
}

def standardize_field(field_name: str, value: Any) -> Any:
    """
    Chuẩn hóa một field
    
    Args:
        field_name: Tên field
        value: Giá trị hiện tại
    
    Returns:
        Giá trị đã chuẩn hóa
    """
    if field_name in STANDARDIZATION_FUNCTIONS:
        return STANDARDIZATION_FUNCTIONS[field_name](value)
    return value

def standardize_all_fields(drug_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Chuẩn hóa tất cả các field trong drug_data
    
    Args:
        drug_data: Dữ liệu thuốc
    
    Returns:
        Dữ liệu thuốc đã chuẩn hóa
    """
    result = drug_data.copy()
    
    for field_name in STANDARDIZATION_FUNCTIONS.keys():
        if field_name in result:
            result[field_name] = standardize_field(field_name, result[field_name])
    
    return result

