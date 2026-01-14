"""
Corticosteroids (Thuốc Corticoid) - sử dụng bộ dữ liệu đầy đủ từ
`endocrinology_other.corticosteroids` và bổ sung Prednisone với enhanced fields.
"""

from ..endocrinology_other.corticosteroids.long_acting import LONG_ACTING
from ..endocrinology_other.corticosteroids.short_intermediate_acting import (
    SHORT_INTERMEDIATE_ACTING,
)

PREDNISONE_ENHANCED = {
    "group": "Endocrinology - Corticosteroid (Oral)",
    "vietnamese_name": "Prednisone (tiền dược của prednisolone)",
    "brand_names": {
        "common": ["Deltasone", "Prednisone"],
        "vietnam": ["Prednisone 5mg", "Prednisolone 5mg"],
    },
    "administration": ["PO"],
    "indications": [
        "Viêm khớp dạng thấp, lupus",
        "Hen phế quản/COPD đợt cấp",
        "Bệnh viêm ruột (IBD)",
        "Dị ứng nặng",
        "Hội chứng thận hư",
        "Điều trị thay thế trong suy thượng thận (khi không có hydrocortisone)",
    ],
    "contraindications_detail": {
        "tuyệt_đối": [
            "Nhiễm nấm toàn thân chưa điều trị",
            "Dị ứng với prednisone/corticosteroid",
            "Tiêm vaccine sống liều cao khi đang dùng liều ức chế miễn dịch",
        ],
        "tương_đối": [
            "Nhiễm trùng đang hoạt động",
            "Đái tháo đường, tăng huyết áp, suy tim",
            "Loãng xương, loét dạ dày",
            "Rối loạn tâm thần",
            "Suy gan nặng (giảm khả năng chuyển hóa thành prednisolone)",
        ],
    },
    "dosage": {
        "antiinflammatory": "5-60mg/ngày tùy chỉ định; giảm dần khi đáp ứng.",
        "asthma_exacerbation": "40-60mg/ngày x 5-7 ngày.",
        "copd_exacerbation": "40mg/ngày x 5 ngày.",
        "notes": "Uống buổi sáng; nếu dùng >2 tuần phải taper để tránh suy thượng thận.",
    },
    "side_effects": [
        "Tăng đường huyết, tăng huyết áp",
        "Tăng cân, Cushingoid",
        "Loãng xương, đau dạ dày/loét",
        "Ức chế miễn dịch, tăng nguy cơ nhiễm trùng",
        "Rối loạn tâm thần, mất ngủ",
        "Ức chế trục HPA (ngừng đột ngột gây suy thượng thận)",
    ],
    "mechanism_of_action": "Glucocorticoid tổng hợp; prednisone là tiền dược, chuyển hóa thành prednisolone tại gan; ức chế phospholipase A2, giảm cytokine viêm, ức chế miễn dịch.",
    "monitoring": [
        "Đường huyết, huyết áp",
        "Cân nặng, phù",
        "Mật độ xương nếu dùng kéo dài",
        "Dấu hiệu nhiễm trùng, loét dạ dày",
        "Dấu hiệu suy thượng thận khi giảm/ngừng",
    ],
    "precautions": [
        "Không ngừng đột ngột nếu dùng >2 tuần; taper dần.",
        "Dùng với thức ăn vào buổi sáng để giảm kích ứng dạ dày và ức chế HPA.",
        "Bổ sung calci + vitamin D nếu dùng dài ngày; cân nhắc PPI nếu nguy cơ loét.",
        "Theo dõi đường huyết chặt ở bệnh nhân đái tháo đường.",
    ],
    "drug_interactions": {
        "major": [
            {
                "drug": "Ketoconazole/itraconazole",
                "mechanism": "Ức chế CYP3A4 → tăng nồng độ prednisone/prednisolone.",
                "effect": "Tăng nguy cơ Cushing, tăng đường huyết.",
                "management": "Cân nhắc giảm liều steroid; theo dõi tác dụng phụ.",
            },
            {
                "drug": "Rifampin, carbamazepine, phenytoin",
                "mechanism": "Cảm ứng CYP3A4 → giảm nồng độ steroid.",
                "effect": "Giảm hiệu quả; nguy cơ suy thượng thận.",
                "management": "Có thể cần tăng liều; theo dõi lâm sàng.",
            },
            {
                "drug": "Warfarin",
                "mechanism": "Thay đổi chuyển hóa/vitamin K phụ thuộc.",
                "effect": "INR có thể tăng hoặc giảm.",
                "management": "Theo dõi INR chặt khi bắt đầu/ngừng steroid.",
            },
        ],
        "moderate": [
            {
                "drug": "NSAIDs",
                "mechanism": "Tăng nguy cơ loét/xuất huyết tiêu hóa.",
                "effect": "Nguy cơ loét/ xuất huyết GI tăng.",
                "management": "Tránh/giảm thời gian dùng; cân nhắc PPI.",
            },
        ],
        "minor": [
            {
                "drug": "Thuốc hạ đường huyết",
                "mechanism": "Steroid tăng đường huyết, giảm hiệu quả.",
                "effect": "Tăng glucose máu.",
                "management": "Điều chỉnh liều thuốc đái tháo đường; theo dõi đường huyết.",
            }
        ],
    },
    "renal_adjustment": {
        "normal": "Không cần chỉnh liều.",
        "30_60": "Không cần chỉnh liều; theo dõi giữ nước/điện giải.",
        "under_30": "Không cần chỉnh liều; thận trọng giữ nước và hạ kali.",
    },
    "hepatic_adjustment": {
        "mild": "Không cần chỉnh liều đáng kể.",
        "moderate": "Thận trọng; prednisone cần chuyển hóa thành prednisolone.",
        "severe": "Cân nhắc dùng prednisolone thay vì prednisone.",
        "notes": "Theo dõi dấu hiệu đáp ứng; prednisone là tiền dược.",
    },
    "overdose_management": {
        "symptoms": [
            "Cushingoid, tăng đường huyết, loét dạ dày",
            "Rối loạn tâm thần, giữ nước, hạ kali",
            "Suy thượng thận cấp nếu ngừng đột ngột sau dùng dài",
        ],
        "antidote": "Không có antidote đặc hiệu.",
        "treatment": [
            "Giảm/ngừng thuốc từ từ (không ngừng đột ngột).",
            "Điều trị hỗ trợ: kiểm soát đường huyết, PPI nếu loét.",
            "Bổ sung kali nếu hạ kali; lợi tiểu nếu phù.",
            "Steroid stress dose nếu có dấu hiệu suy thượng thận.",
        ],
        "monitoring": "Dấu hiệu sinh tồn, đường huyết, điện giải, triệu chứng suy thượng thận.",
    },
    "reversal_agents": None,
    "administration_instructions": {
        "oral": {
            "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày.",
            "timing": "Ưu tiên buổi sáng; chia liều nếu liều cao.",
            "notes": "Nếu dùng dài ngày, taper dần khi ngừng.",
        }
    },
    "black_box_warnings": "Ngừng đột ngột sau dùng kéo dài có thể gây suy thượng thận; tăng nguy cơ nhiễm trùng nghiêm trọng khi dùng liều ức chế miễn dịch.",
    "risk_flags": {
        "high_alert": True,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": {
            "metabolic": "Tăng đường huyết, giữ nước",
            "gastrointestinal": "Loét dạ dày/ xuất huyết",
            "endocrine": "Ức chế trục HPA nếu ngừng đột ngột",
            "skeletal": "Loãng xương nếu dùng kéo dài",
        },
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": [
            "Đường huyết, huyết áp",
            "Điện giải (natri/kali) nếu liều cao",
            "Dấu hiệu nhiễm trùng",
            "Dấu hiệu suy thượng thận khi giảm/ngừng",
            "INR khi dùng kèm warfarin",
        ],
    },
    "guideline_tags": [
        "FDA Black Box Warning - Adrenal Insufficiency (nếu ngừng đột ngột)",
        "FDA Black Box Warning - Serious Infections (liều cao/ức chế miễn dịch)",
        "ACR Guidelines - Rheumatoid Arthritis",
        "WHO Essential Medicines List",
    ],
    "last_updated": "2025-02-19",
}

CORTICOSTEROIDS_DRUGS = {
    **SHORT_INTERMEDIATE_ACTING,
    **LONG_ACTING,
    "Prednisone": PREDNISONE_ENHANCED,
}
