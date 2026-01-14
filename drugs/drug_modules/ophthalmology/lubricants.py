"""
Ophthalmology Drugs - Lubricants
"""
from typing import Dict, Any


LUBRICANTS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Artificial tears (Carboxymethylcellulose)": {
            "group": "Ophthalmology - Lubricant (Dry Eye)",
            "vietnamese_name": "Nước mắt nhân tạo, Carboxymethylcellulose",
            "administration": ["Ophthalmic"],
            "indications": [
                "Khô mắt (dry eye syndrome)",
                "Kích ứng mắt do môi trường (không khí khô, gió, máy điều hòa)",
                "Kích ứng mắt do đeo kính áp tròng",
                "Kích ứng mắt sau phẫu thuật mắt",
                "Kích ứng mắt do thuốc nhỏ mắt khác"
            ],
            "contraindications": [
                "Dị ứng carboxymethylcellulose hoặc bất kỳ thành phần nào"
            ],
            "dosage": {
                "adult_ophthalmic": "1-2 giọt vào mắt bị ảnh hưởng khi cần, thường 3-4 lần/ngày hoặc nhiều hơn",
                "notes": "Nước mắt nhân tạo là thuốc bôi trơn, không có tác dụng điều trị bệnh. Dùng khi cần để giảm khô mắt và kích ứng. Có thể dùng nhiều lần/ngày tùy theo nhu cầu. Không có giới hạn số lần dùng."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt nhẹ (đỏ, rát) - hiếm",
                "Nhìn mờ tạm thời - phổ biến ngay sau khi nhỏ",
                "Dị ứng - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác"
            ],
        "pregnancy": "Không phân loại - An toàn",
            "mechanism_of_action": "Carboxymethylcellulose là polymer tổng hợp, tạo thành lớp màng bảo vệ trên bề mặt mắt, giữ ẩm và bôi trơn. Carboxymethylcellulose có khả năng giữ nước cao, tạo thành gel trong nước mắt, dẫn đến: (1) Bôi trơn bề mặt mắt, (2) Giữ ẩm, giảm khô mắt, (3) Bảo vệ giác mạc và kết mạc, (4) Giảm kích ứng. Nước mắt nhân tạo không có tác dụng điều trị bệnh, chỉ có tác dụng hỗ trợ và bôi trơn. ĐẶC ĐIỂM: (1) Thuốc bôi trơn, không có tác dụng điều trị bệnh, (2) Dùng khi cần, không có giới hạn số lần dùng, (3) An toàn, ít tác dụng phụ, (4) Có thể dùng với thuốc nhỏ mắt khác (đợi 5-10 phút giữa các thuốc), (5) Nhìn mờ tạm thời ngay sau khi nhỏ - phổ biến.",
            "monitoring": [
                "Dấu hiệu khô mắt (khô, rát, ngứa) - cải thiện sau khi nhỏ",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa) - cải thiện sau khi nhỏ",
                "Thị lực - nhìn mờ tạm thời ngay sau khi nhỏ là bình thường"
            ],
            "precautions": [
                "Nhìn mờ tạm thời ngay sau khi nhỏ - phổ biến, thường hết sau vài phút",
                "Nếu dùng với thuốc nhỏ mắt khác, đợi 5-10 phút giữa các thuốc",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (một số chế phẩm có thể tương thích, một số không)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Nếu khô mắt nặng hoặc kéo dài, cần khám mắt để tìm nguyên nhân"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (bôi trơn tại chỗ)",
                "onset": "Ngay lập tức",
                "duration": "1-2 giờ (tùy theo chế phẩm)",
                "protein_binding": "Không áp dụng",
                "metabolism": "Không chuyển hóa, thải trừ qua nước mắt",
                "clearance": "Thải trừ qua nước mắt"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở (một số chế phẩm có thể dùng lâu hơn).",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng carboxymethylcellulose hoặc bất kỳ thành phần nào"
                ],
                "tương_đối": [
                    "Bệnh nhân đeo kính áp tròng - thận trọng (một số chế phẩm có thể tương thích, một số không)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified",
                "pregnancy_details": "Nước mắt nhân tạo không có phân loại FDA vì không có tác dụng toàn thân. Carboxymethylcellulose là polymer tổng hợp, không hấp thu toàn thân, an toàn trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Nước mắt nhân tạo không hấp thu toàn thân, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, không hấp thu toàn thân)",
                "notes": "Nước mắt nhân tạo không hấp thu toàn thân. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Nhìn mờ tạm thời",
                    "Kích ứng mắt nhẹ"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt nếu cần.",
                "treatment": [
                    "Rửa mắt với nước sạch hoặc nước muối sinh lý nếu cần",
                    "Nhìn mờ tạm thời thường hết sau vài phút",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt nếu cần",
                    "  - Ngừng dùng nếu dị ứng"
                ],
                "monitoring": "Theo dõi thị lực và dấu hiệu kích ứng cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.5% hoặc 1% (carboxymethylcellulose).",
                    "application": "1-2 giọt vào mắt bị ảnh hưởng khi cần, thường 3-4 lần/ngày hoặc nhiều hơn. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ.",
                    "timing": "Khi cần, không có giới hạn số lần dùng. Thường 3-4 lần/ngày hoặc nhiều hơn.",
                    "contact_lenses": "Có thể dùng với kính áp tròng (một số chế phẩm), nhưng thận trọng. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dùng khi cần, không có giới hạn số lần dùng, 2) Nhìn mờ tạm thời ngay sau khi nhỏ là bình thường, 3) Nếu dùng với thuốc nhỏ mắt khác, đợi 5-10 phút giữa các thuốc, 4) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào, 5) Nếu khô mắt nặng hoặc kéo dài, cần khám mắt để tìm nguyên nhân."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Artificial Tears (Carboxymethylcellulose)",
                    "UpToDate - Dry Eye Syndrome: Treatment",
                    "AAO Guidelines - Dry Eye Syndrome",
                    "TFOS DEWS II Report"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (improvement in dry eye symptoms)", "Signs of eye irritation (rare)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Dry Eye Syndrome",
                "TFOS DEWS II Report",
                "FDA Drug Information - Artificial Tears",
                "UpToDate - Dry Eye Syndrome Treatment"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

}

__all__ = ['LUBRICANTS_DRUGS']
