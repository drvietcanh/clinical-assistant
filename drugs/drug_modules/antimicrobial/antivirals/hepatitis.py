"""
Hepatitis Antivirals
Ribavirin for hepatitis C treatment
"""

HEPATITIS_ANTIVIRALS = {
    "Ribavirin": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Ribavirin, Rebetol",
        "administration": ["PO", "IV", "Inhalation"],
        "indications": [
            "Viêm gan C (kết hợp với interferon)",
            "Viêm gan C (kết hợp với sofosbuvir)",
            "Sốt Lassa (IV)",
            "RSV ở trẻ sơ sinh (inhalation)"
        ],
        "contraindications": [
            "Có thai (nam và nữ)",
            "Suy thận nặng",
            "Bệnh tim nặng",
            "Thiếu máu nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_hcv": "800-1200mg/ngày chia 2 lần (tùy genotype và trọng lượng)",
            "adult_hcv_sofosbuvir": "1000mg/ngày (nếu >75kg) hoặc 800mg/ngày (<75kg)",
            "adult_iv": "30-35mg/kg x 1 lần (loading), sau đó 15-20mg/kg mỗi 6 giờ",
            "notes": "Rất độc. Nam và nữ phải dùng biện pháp tránh thai 6 tháng sau khi ngừng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Không dùng"
        },
        "side_effects": [
            "Thiếu máu (phổ biến, có thể nặng)",
            "Giảm bạch cầu",
            "Dị tật thai nhi (nam và nữ - chống chỉ định tuyệt đối nếu có thai)",
            "Rối loạn tâm thần",
            "Rối loạn hô hấp (inhalation)",
            "Rất độc"
        ],
        "interactions": [
            "Zidovudine: tăng độc tính",
            "Didanosine: tăng độc tính",
            "Azathioprine: tăng độc tính"
        ],
        "pregnancy": "X - Chống chỉ định tuyệt đối",
        "mechanism_of_action": "Ribavirin là nucleoside analog (guanosine), ức chế tổng hợp RNA và DNA của virus. Thuốc được phosphoryl hóa trong tế bào thành ribavirin triphosphate, ức chế RNA polymerase của virus, gây đột biến và ngăn chặn sao chép virus. Ribavirin cũng ức chế inosine monophosphate dehydrogenase (IMPDH), làm giảm GTP nội bào, ảnh hưởng đến tổng hợp RNA virus. Thuốc có tác dụng phổ rộng trên nhiều virus RNA, đặc biệt hiệu quả trong điều trị viêm gan C khi kết hợp với interferon hoặc sofosbuvir. Ribavirin rất độc, gây thiếu máu, dị tật thai nhi, và các tác dụng phụ nghiêm trọng khác.",
        "monitoring": [
            "Công thức máu (CBC) - theo dõi thiếu máu, giảm bạch cầu, giảm tiểu cầu - mỗi 2-4 tuần",
            "Hemoglobin (Hb) - mục tiêu: giữ >10g/dL, nếu <8.5g/dL cần giảm liều hoặc ngừng",
            "Chức năng thận (creatinine, BUN) - trước khi bắt đầu và định kỳ",
            "Chức năng gan (ALT, AST, bilirubin) - theo dõi đáp ứng điều trị HCV",
            "Tâm thần (trầm cảm, rối loạn tâm thần) - đặc biệt khi dùng với interferon",
            "Dấu hiệu quá liều (thiếu máu nặng, mệt mỏi)",
            "Xét nghiệm thai (nam và nữ) - trước khi bắt đầu và định kỳ"
        ],
        "precautions": [
            "Rất độc - chỉ dùng khi thật sự cần thiết",
            "Chống chỉ định tuyệt đối trong thai kỳ (nam và nữ) - gây dị tật thai nhi nghiêm trọng",
            "Nam và nữ phải dùng biện pháp tránh thai hiệu quả trong và 6 tháng sau khi ngừng",
            "Kiểm tra thai trước khi bắt đầu điều trị (nam và nữ)",
            "Không dùng nếu CrCl <50 (suy thận nặng)",
            "Giảm liều 50% nếu CrCl 30-50",
            "Thận trọng ở bệnh nhân bệnh tim (nguy cơ thiếu máu)",
            "Theo dõi sát hemoglobin - nếu <8.5g/dL: giảm liều hoặc ngừng",
            "Có thể cần truyền máu nếu thiếu máu nặng",
            "Thận trọng ở bệnh nhân có tiền sử rối loạn tâm thần (đặc biệt khi dùng với interferon)"
        ],
        "pharmacokinetics": {
            "half_life": "298 giờ (12.4 ngày) - rất dài, tích tụ trong tế bào",
            "onset": "2-4 giờ",
            "duration": "Rất dài do half-life dài",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (chủ yếu), một phần qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định tuyệt đối trong thai kỳ (nam và nữ) - gây dị tật thai nhi và tử vong thai nhi. Có thể gây thiếu máu nặng, đe dọa tính mạng. Có thể gây rối loạn tâm thần nghiêm trọng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Zidovudine (AZT)",
                    "mechanism": "Cả hai đều gây thiếu máu và giảm bạch cầu, tác dụng cộng dồn làm tăng nguy cơ độc tính huyết học nghiêm trọng.",
                    "effect": "Tăng nguy cơ thiếu máu nặng, giảm bạch cầu, giảm tiểu cầu, đe dọa tính mạng",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi CBC chặt chẽ mỗi 1-2 tuần. Có thể cần giảm liều hoặc ngừng một trong hai thuốc nếu có thiếu máu nặng."
                },
                {
                    "drug": "Didanosine",
                    "mechanism": "Cả hai đều gây độc tính ty thể và thiếu máu, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ thiếu máu, độc tính ty thể, viêm tụy, nhiễm toan lactic",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, theo dõi CBC, chức năng tụy, và lactate chặt chẽ."
                },
                {
                    "drug": "Azathioprine",
                    "mechanism": "Cả hai đều ức chế tổng hợp purine và gây độc tính tủy xương, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ thiếu máu, giảm bạch cầu, giảm tiểu cầu nghiêm trọng",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, theo dõi CBC chặt chẽ, giảm liều hoặc ngừng nếu có độc tính huyết học."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Có thai (nam và nữ) - chống chỉ định tuyệt đối, gây dị tật thai nhi và tử vong thai nhi",
                "Suy thận nặng (CrCl <50 ml/min) - không dùng",
                "Bệnh tim nặng (suy tim, bệnh mạch vành không ổn định) - nguy cơ thiếu máu làm nặng bệnh tim",
                "Thiếu máu nặng (Hb <8.5g/dL) - không bắt đầu điều trị",
                "Dị ứng ribavirin"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-50) - giảm liều 50%, theo dõi chặt chẽ",
                "Bệnh tim nhẹ đến trung bình - thận trọng, theo dõi sát hemoglobin",
                "Thiếu máu nhẹ đến trung bình (Hb 8.5-10g/dL) - có thể cần giảm liều hoặc truyền máu",
                "Tiền sử rối loạn tâm thần - tăng nguy cơ rối loạn tâm thần, đặc biệt khi dùng với interferon",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ (nam và nữ). Ribavirin gây dị tật thai nhi nghiêm trọng, tử vong thai nhi, và sẩy thai. Nam và nữ phải dùng biện pháp tránh thai hiệu quả trong và 6 tháng sau khi ngừng thuốc. Kiểm tra thai trước khi bắt đầu điều trị (nam và nữ).",
            "lactation": {
                "safety": "Incompatible",
                "details": "Ribavirin bài tiết vào sữa mẹ. Thuốc rất độc, có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng ribavirin. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi chức năng gan",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Ribavirin chuyển hóa một phần qua gan. Thải trừ chủ yếu qua thận. Suy gan có thể làm tăng nồng độ và độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Thiếu máu nặng (Hb <8.5g/dL)",
                "Giảm bạch cầu, giảm tiểu cầu",
                "Mệt mỏi, khó thở",
                "Rối loạn tâm thần",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay ribavirin",
                "Theo dõi CBC, chức năng thận, chức năng gan",
                "Truyền máu nếu thiếu máu nặng (Hb <8.5g/dL)",
                "Supportive care",
                "Lọc máu có thể giúp loại bỏ ribavirin (half-life dài, tích tụ trong tế bào)",
                "Theo dõi tâm thần nếu có rối loạn tâm thần"
            ],
            "monitoring": "CBC mỗi ngày, chức năng thận, chức năng gan, dấu hiệu lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Chia 2 lần/ngày, uống với thức ăn"
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Truyền trong 30-60 phút",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Loading dose: 30-35mg/kg x 1 lần, sau đó 15-20mg/kg mỗi 6 giờ. Theo dõi chức năng thận."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ribavirin (Rebetol)",
                "UpToDate - Ribavirin Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    }
}

__all__ = ['HEPATITIS_ANTIVIRALS']
