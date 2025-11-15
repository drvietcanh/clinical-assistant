"""
Polyene Antifungals - Antifungal Medications
"""

POLYENES_DRUGS = {
    "Nystatin": {
        "group": "Infectious Disease - Antifungal (Polyene)",
        "vietnamese_name": "Nystatin, Mycostatin",
        "administration": ["PO (suspension, tablet)", "Topical"],
        "indications": [
            "Nhiễm nấm Candida miệng (oral candidiasis/thrush)",
            "Nhiễm nấm Candida thực quản",
            "Nhiễm nấm Candida da (topical)",
            "Nhiễm nấm Candida âm đạo (topical)"
        ],
        "contraindications": [
            "Dị ứng nystatin"
        ],
        "dosage": {
            "adult_oral_suspension": "400,000-600,000 đơn vị x 4 lần/ngày",
            "adult_oral_tablet": "500,000-1,000,000 đơn vị x 4 lần/ngày",
            "adult_topical": "Bôi 2-3 lần/ngày",
            "notes": "Không hấp thu qua đường tiêu hóa. Chỉ tác dụng tại chỗ. Súc miệng và nuốt (suspension)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn (hiếm, PO)",
            "Tiêu chảy (hiếm, PO)",
            "Kích ứng da (hiếm, topical)",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Rất ít tương tác (không hấp thu hệ thống)"
        ],
        "pregnancy": "C - An toàn (không hấp thu)",
        "mechanism_of_action": "Nystatin là polyene antifungal, gắn với ergosterol trong màng tế bào nấm, tạo lỗ thủng trong màng, làm rò rỉ các ion và chất dinh dưỡng, dẫn đến chết tế bào nấm. Thuốc có ái lực cao với ergosterol (có trong nấm) nhưng không gắn với cholesterol (có trong tế bào người), nên an toàn cho tế bào người. Nystatin không hấp thu qua đường tiêu hóa hoặc qua da, nên chỉ tác dụng tại chỗ. Thuốc hiệu quả trên Candida species, đặc biệt Candida albicans, thường dùng cho nhiễm nấm miệng, thực quản, và da.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng, giảm mảng trắng trong miệng)",
            "Dấu hiệu dị ứng (ban da, kích ứng)",
            "Triệu chứng tiêu hóa (buồn nôn, tiêu chảy) - hiếm",
            "Tái nhiễm (nếu điều trị không đủ hoặc yếu tố nguy cơ vẫn còn)"
        ],
        "precautions": [
            "Suspension: súc miệng kỹ, giữ trong miệng vài phút, sau đó nuốt (cho nhiễm nấm thực quản)",
            "Tablet: ngậm trong miệng cho tan (cho nhiễm nấm miệng)",
            "Topical: bôi đều, rửa sạch tay sau khi bôi",
            "Tiếp tục điều trị 48 giờ sau khi hết triệu chứng",
            "Với nhiễm nấm miệng: điều trị 7-14 ngày",
            "Với nhiễm nấm thực quản: điều trị 14-21 ngày",
            "An toàn trong thai kỳ và cho con bú (không hấp thu)",
            "Rất ít tác dụng phụ do không hấp thu hệ thống",
            "Thận trọng ở bệnh nhân có vết thương mở rộng (topical)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu)",
            "onset": "Tác dụng tại chỗ ngay lập tức",
            "duration": "Tác dụng tại chỗ trong vài giờ",
            "protein_binding": "Không áp dụng (không vào máu)",
            "clearance": "Không hấp thu, thải trừ qua phân (PO) hoặc rửa trôi (topical)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh, lắc kỹ trước khi dùng (suspension)",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nystatin"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "An toàn trong thai kỳ. Nystatin không hấp thu qua đường tiêu hóa hoặc qua da, nên không vào máu và không ảnh hưởng đến thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Nystatin không hấp thu hệ thống, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Nystatin không hấp thu hệ thống, không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn (hiếm)",
                "Tiêu chảy (hiếm)",
                "Kích ứng da (topical)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Rửa miệng/da nếu cần",
                "Supportive care",
                "Theo dõi triệu chứng"
            ],
            "monitoring": "Triệu chứng lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Suspension: súc miệng kỹ, giữ trong miệng vài phút, sau đó nuốt (cho nhiễm nấm thực quản). Tablet: ngậm trong miệng cho tan (cho nhiễm nấm miệng)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Nystatin chỉ có dạng PO và topical, không có dạng IV."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nystatin (Mycostatin)",
                "UpToDate - Nystatin Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    }
}

__all__ = ['POLYENES_DRUGS']
