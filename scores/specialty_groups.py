"""
Specialty Groups Configuration
Tổ chức lại chuyên khoa theo nhóm logic cho navigation
"""

from typing import Dict, List

# Specialty Groups theo workflow lâm sàng
SPECIALTY_GROUPS = {
    "critical_care_emergency": {
        "id": "critical_care_emergency",
        "name": "🚨 Critical Care & Emergency",
        "icon": "🚨",
        "description": "Scores cho cấp cứu và hồi sức",
        "specialties": [
            "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)",
            "🦴 Chấn thương & Chỉnh Hình (Trauma/Orthopedics)",
        ],
        "priority": 1,
        "default_expanded": True
    },
    "organ_systems": {
        "id": "organ_systems",
        "name": "💊 Organ Systems",
        "icon": "💊",
        "description": "Scores theo hệ cơ quan",
        "specialties": [
            "❤️ Tim mạch (Cardiology)",
            "🫁 Hô hấp (Respiratory)",
            "🧠 Thần kinh (Neurology)",
            "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)",
            "🩺 Huyết học & Đông máu (Hematology)",
            "🧪 Thận - Điện giải (Nephrology)",
        ],
        "priority": 2,
        "default_expanded": True
    },
    "special_populations": {
        "id": "special_populations",
        "name": "👥 Special Populations",
        "icon": "👥",
        "description": "Scores cho nhóm đặc biệt",
        "specialties": [
            "👴 Lão khoa (Geriatrics)",  # NEW - sẽ được thêm
            "👶 Nhi khoa (Pediatrics)",
            "🤰 Sản khoa (Obstetrics)",
        ],
        "priority": 3,
        "default_expanded": False
    },
    "specialized_fields": {
        "id": "specialized_fields",
        "name": "🔬 Specialized Fields",
        "icon": "🔬",
        "description": "Chuyên khoa chuyên sâu",
        "specialties": [
            "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)",
            "🦠 Nhiễm khuẩn (Infectious Disease)",
            "🎗️ Ung thư (Oncology)",
            "🧠 Tâm thần - Tâm Lý (Psychiatry/Psychology)",
            "🦴 Thấp khớp - Miễn dịch (Rheumatology/Immunology)",
            "🩹 Da liễu (Dermatology)",
            "👂 Tai Mũi Họng (ENT)",
            "👁️ Mắt (Ophthalmology)",
            "😣 Đánh giá đau (Pain Assessment)",
            "🔪 Phẫu thuật & Gây mê (Surgery/Anesthesia)",
            "🛏️ Chăm sóc điều dưỡng (Nursing Care)",
        ],
        "priority": 4,
        "default_expanded": False
    }
}

# Helper functions
def get_all_groups() -> Dict:
    """Get all specialty groups"""
    return SPECIALTY_GROUPS

def get_group_by_id(group_id: str) -> Dict:
    """Get specialty group by ID"""
    return SPECIALTY_GROUPS.get(group_id)

def get_specialties_in_group(group_id: str) -> List[str]:
    """Get list of specialties in a group"""
    group = SPECIALTY_GROUPS.get(group_id)
    if group:
        return group.get("specialties", [])
    return []

def get_group_for_specialty(specialty_name: str) -> str:
    """Get group ID for a given specialty name"""
    for group_id, group_info in SPECIALTY_GROUPS.items():
        if specialty_name in group_info.get("specialties", []):
            return group_id
    return "specialized_fields"  # Default
