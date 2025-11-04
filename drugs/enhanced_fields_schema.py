"""
Enhanced Fields Schema - Cấu Trúc Chuẩn cho Enhanced Fields
Hướng dẫn và template để thêm enhanced fields cho các thuốc trong database

NOTE: Schema data đã được tách ra file enhanced_fields_schema_data.py
File này chứa functions và import data để giữ backward compatibility
"""

from .enhanced_fields_schema_data import (
    ENHANCED_FIELDS_SCHEMA,
    EXAMPLE_ENHANCED_FIELDS
)

# ============================================================================
# TEMPLATE FUNCTION - Tạo Enhanced Fields Mẫu
# ============================================================================

def create_enhanced_fields_template():
    """
    Trả về template rỗng cho enhanced fields
    Sử dụng để copy-paste khi thêm enhanced fields cho thuốc mới
    """
    return {
        # === 6 FIELDS CƠ BẢN ===
        "mechanism_of_action": "",  # Mô tả cơ chế tác dụng (50-200 từ)
        "monitoring": [],  # List các thông số cần monitor
        "precautions": [],  # List các lưu ý và thận trọng
        "pharmacokinetics": {
            "half_life": "",  # Thời gian bán thải
            "onset": "",  # Thời gian bắt đầu tác dụng
            "duration": "",  # Thời gian tác dụng
            "protein_binding": "",  # Tỷ lệ gắn protein
            "clearance": ""  # Đường thải trừ
        },
        "storage": "",  # Điều kiện bảo quản
        "black_box_warnings": None,  # Cảnh báo hộp đen hoặc None
        
        # === 8 FIELDS BỔ SUNG ===
        "drug_interactions": {
            "major": [],  # List dict: {"drug": "...", "mechanism": "...", "effect": "...", "management": "..."}
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "absolute": [],  # List chống chỉ định tuyệt đối
            "relative": []  # List chống chỉ định tương đối
        },
        "pregnancy_lactation": {
            "fda_category": "",  # A/B/C/D/X
            "pregnancy_details": "",  # Chi tiết về thai kỳ
            "lactation": {
                "safety": "",  # Compatible/Incompatible/Caution
                "details": "",  # Chi tiết
                "recommendation": ""  # Khuyến nghị
            }
        },
        "hepatic_adjustment": {
            "mild": "",  # Điều chỉnh cho suy gan nhẹ
            "moderate": "",  # Điều chỉnh cho suy gan trung bình
            "severe": "",  # Điều chỉnh cho suy gan nặng
            "notes": ""  # Ghi chú thêm
        },
        "overdose_management": {
            "symptoms": [],  # List triệu chứng quá liều
            "antidote": "",  # Antidote nếu có (hoặc "Không có")
            "treatment": [],  # List các bước xử trí
            "monitoring": ""  # Theo dõi cần thiết
        },
        "reversal_agents": None,  # None nếu không có, hoặc dict với "available": True và "agents": []
        "administration_instructions": {
            "oral": {
                "with_food": "",  # Uống với/không thức ăn
                "timing": ""  # Thời điểm uống
            },
            "iv": {
                "reconstitution": "",  # Cách pha
                "infusion_rate": "",  # Tốc độ truyền
                "compatibility": [],  # Dịch tương thích
                "incompatibility": [],  # Dịch không tương thích
                "notes": ""  # Ghi chú
            }
        },
        "references": {
            "primary_sources": [],  # List nguồn chính
            "last_updated": "",  # Ngày cập nhật (YYYY-MM-DD)
            "evidence_level": ""  # Mức độ chứng cứ
        }
    }


# ============================================================================
# VALIDATION FUNCTION - Kiểm Tra Tính Hợp Lệ
# ============================================================================

def validate_enhanced_fields(drug_name, enhanced_fields):
    """
    Kiểm tra tính hợp lệ của enhanced fields
    
    Args:
        drug_name: Tên thuốc
        enhanced_fields: Dictionary chứa enhanced fields
    
    Returns:
        tuple: (is_valid: bool, errors: list of strings)
    """
    errors = []
    
    # Kiểm tra tất cả các field bắt buộc
    required_fields = ["mechanism_of_action", "monitoring", "precautions", 
                      "pharmacokinetics", "storage", "black_box_warnings"]
    
    for field in required_fields:
        if field not in enhanced_fields:
            errors.append(f"{drug_name}: Thiếu field '{field}'")
    
    # Kiểm tra kiểu dữ liệu
    if "mechanism_of_action" in enhanced_fields:
        if not isinstance(enhanced_fields["mechanism_of_action"], str):
            errors.append(f"{drug_name}: 'mechanism_of_action' phải là string")
        elif len(enhanced_fields["mechanism_of_action"]) < 50:
            errors.append(f"{drug_name}: 'mechanism_of_action' quá ngắn (<50 ký tự)")
    
    if "monitoring" in enhanced_fields:
        if not isinstance(enhanced_fields["monitoring"], list):
            errors.append(f"{drug_name}: 'monitoring' phải là list")
        elif len(enhanced_fields["monitoring"]) == 0:
            errors.append(f"{drug_name}: 'monitoring' không được rỗng")
    
    if "precautions" in enhanced_fields:
        if not isinstance(enhanced_fields["precautions"], list):
            errors.append(f"{drug_name}: 'precautions' phải là list")
        elif len(enhanced_fields["precautions"]) == 0:
            errors.append(f"{drug_name}: 'precautions' không được rỗng")
    
    if "pharmacokinetics" in enhanced_fields:
        if not isinstance(enhanced_fields["pharmacokinetics"], dict):
            errors.append(f"{drug_name}: 'pharmacokinetics' phải là dict")
        else:
            pk = enhanced_fields["pharmacokinetics"]
            required_pk_fields = ["half_life", "onset", "duration", 
                                 "protein_binding", "clearance"]
            for pk_field in required_pk_fields:
                if pk_field not in pk:
                    errors.append(f"{drug_name}: 'pharmacokinetics' thiếu '{pk_field}'")
    
    if "storage" in enhanced_fields:
        if not isinstance(enhanced_fields["storage"], str):
            errors.append(f"{drug_name}: 'storage' phải là string")
        elif len(enhanced_fields["storage"]) < 10:
            errors.append(f"{drug_name}: 'storage' quá ngắn (<10 ký tự)")
    
    if "black_box_warnings" in enhanced_fields:
        value = enhanced_fields["black_box_warnings"]
        if value is not None and not isinstance(value, str):
            errors.append(f"{drug_name}: 'black_box_warnings' phải là string hoặc None")
    
    # === VALIDATION CHO 8 FIELDS BỔ SUNG (Optional) ===
    
    # drug_interactions
    if "drug_interactions" in enhanced_fields and enhanced_fields["drug_interactions"] is not None:
        if not isinstance(enhanced_fields["drug_interactions"], dict):
            errors.append(f"{drug_name}: 'drug_interactions' phải là dict hoặc None")
        else:
            di = enhanced_fields["drug_interactions"]
            for severity in ["major", "moderate", "minor"]:
                if severity in di:
                    if not isinstance(di[severity], list):
                        errors.append(f"{drug_name}: 'drug_interactions.{severity}' phải là list")
                    else:
                        for item in di[severity]:
                            if not isinstance(item, dict):
                                errors.append(f"{drug_name}: 'drug_interactions.{severity}' items phải là dict")
                            else:
                                required_keys = ["drug", "mechanism", "effect", "management"]
                                for key in required_keys:
                                    if key not in item:
                                        errors.append(f"{drug_name}: 'drug_interactions.{severity}' item thiếu key '{key}'")
    
    # contraindications
    if "contraindications" in enhanced_fields and enhanced_fields["contraindications"] is not None:
        if not isinstance(enhanced_fields["contraindications"], dict):
            errors.append(f"{drug_name}: 'contraindications' phải là dict hoặc None")
        else:
            ci = enhanced_fields["contraindications"]
            for ci_type in ["absolute", "relative"]:
                if ci_type in ci and not isinstance(ci[ci_type], list):
                    errors.append(f"{drug_name}: 'contraindications.{ci_type}' phải là list")
    
    # pregnancy_lactation
    if "pregnancy_lactation" in enhanced_fields and enhanced_fields["pregnancy_lactation"] is not None:
        if not isinstance(enhanced_fields["pregnancy_lactation"], dict):
            errors.append(f"{drug_name}: 'pregnancy_lactation' phải là dict hoặc None")
        else:
            pl = enhanced_fields["pregnancy_lactation"]
            if "lactation" in pl and not isinstance(pl["lactation"], dict):
                errors.append(f"{drug_name}: 'pregnancy_lactation.lactation' phải là dict")
    
    # hepatic_adjustment
    if "hepatic_adjustment" in enhanced_fields and enhanced_fields["hepatic_adjustment"] is not None:
        if not isinstance(enhanced_fields["hepatic_adjustment"], dict):
            errors.append(f"{drug_name}: 'hepatic_adjustment' phải là dict hoặc None")
    
    # overdose_management
    if "overdose_management" in enhanced_fields and enhanced_fields["overdose_management"] is not None:
        if not isinstance(enhanced_fields["overdose_management"], dict):
            errors.append(f"{drug_name}: 'overdose_management' phải là dict hoặc None")
        else:
            od = enhanced_fields["overdose_management"]
            if "symptoms" in od and not isinstance(od["symptoms"], list):
                errors.append(f"{drug_name}: 'overdose_management.symptoms' phải là list")
            if "treatment" in od and not isinstance(od["treatment"], list):
                errors.append(f"{drug_name}: 'overdose_management.treatment' phải là list")
    
    # reversal_agents
    if "reversal_agents" in enhanced_fields:
        ra = enhanced_fields["reversal_agents"]
        if ra is not None:
            if not isinstance(ra, dict):
                errors.append(f"{drug_name}: 'reversal_agents' phải là dict hoặc None")
            else:
                if "available" in ra and not isinstance(ra["available"], bool):
                    errors.append(f"{drug_name}: 'reversal_agents.available' phải là bool")
                if "agents" in ra and not isinstance(ra["agents"], list):
                    errors.append(f"{drug_name}: 'reversal_agents.agents' phải là list")
    
    # administration_instructions
    if "administration_instructions" in enhanced_fields and enhanced_fields["administration_instructions"] is not None:
        if not isinstance(enhanced_fields["administration_instructions"], dict):
            errors.append(f"{drug_name}: 'administration_instructions' phải là dict hoặc None")
    
    # references
    if "references" in enhanced_fields and enhanced_fields["references"] is not None:
        if not isinstance(enhanced_fields["references"], dict):
            errors.append(f"{drug_name}: 'references' phải là dict hoặc None")
        else:
            ref = enhanced_fields["references"]
            if "primary_sources" in ref and not isinstance(ref["primary_sources"], list):
                errors.append(f"{drug_name}: 'references.primary_sources' phải là list")
    
    return len(errors) == 0, errors


# ============================================================================
# HELPER FUNCTION - Tạo Enhanced Fields từ Thông Tin Thuốc
# ============================================================================

def generate_enhanced_fields_guidelines():
    """
    Trả về hướng dẫn chi tiết cách tạo enhanced fields
    """
    return """
# ============================================================================
# HƯỚNG DẪN TẠO ENHANCED FIELDS CHO THUỐC
# ============================================================================

## BƯỚC 1: Thu thập thông tin
- Xem lại thông tin hiện có trong drug database (dosage, indications, side_effects)
- Tìm kiếm thông tin từ:
  * FDA Drug Labels
  * UpToDate, Medscape
  * Goodman & Gilman, Katzung
  * Nhà sản xuất thuốc
  * Clinical guidelines

## BƯỚC 2: Điền từng field

### 1. mechanism_of_action
- Mô tả cách thuốc hoạt động
- Bắt đầu với target/receptor/enzyme
- Giải thích chuỗi phản ứng
- Độ dài: 50-200 từ

### 2. monitoring
- Liệt kê xét nghiệm lab, dấu hiệu lâm sàng cần theo dõi
- Bao gồm tần suất (nếu có)
- Sắp xếp từ quan trọng nhất → ít quan trọng
- 3-10 mục

### 3. precautions
- Các lưu ý thực hành lâm sàng
- Cách dùng, liều khởi đầu
- Điều kiện đặc biệt
- 4-8 mục

### 4. pharmacokinetics
- half_life: Thời gian bán thải
- onset: Thời gian bắt đầu tác dụng
- duration: Thời gian tác dụng
- protein_binding: % gắn protein
- clearance: Đường thải trừ (thận/gan)

### 5. storage
- Nhiệt độ bảo quản
- Ánh sáng, độ ẩm
- Điều kiện đặc biệt

### 6. black_box_warnings
- Chỉ điền nếu có Black Box Warning
- Hoặc cảnh báo nghiêm trọng quan trọng
- None nếu không có

## BƯỚC 3: Kiểm tra
- Chạy validate_enhanced_fields() để kiểm tra
- Đảm bảo tất cả field đều có giá trị hợp lệ
- Kiểm tra chính tả và ngữ pháp

## BƯỚC 4: Thêm vào database
- Mở file drugs/drug_database.py
- Tìm thuốc cần enhance
- Thêm enhanced fields vào dictionary của thuốc đó
- Kiểm tra lại bằng check_enhanced_fields.py
"""


# ============================================================================
# EXAMPLE - Ví Dụ Hoàn Chỉnh
# ============================================================================

# ============================================================================
# EXPORT
# ============================================================================

__all__ = [
    'ENHANCED_FIELDS_SCHEMA',
    'create_enhanced_fields_template',
    'validate_enhanced_fields',
    'generate_enhanced_fields_guidelines',
    'EXAMPLE_ENHANCED_FIELDS'
]
