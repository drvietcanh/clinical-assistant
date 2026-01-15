"""
Fixed-Dose Combination Drugs for Diabetes
Metformin + DPP-4 inhibitor, Metformin + SGLT2 inhibitor, Metformin + Sulfonylurea
"""

DIABETES_FIXED_DOSE_COMBINATIONS = {
    "Metformin/Dapagliflozin": {
        "group": "Diabetes - Biguanide + SGLT2 Inhibitor (Fixed-Dose Combination)",
        "vietnamese_name": "Metformin/Dapagliflozin, Xigduo XR",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2 (khi cần phối hợp metformin và dapagliflozin).",
            "Giảm nguy cơ suy tim và bệnh thận mạn ở bệnh nhân đái tháo đường type 2.",
        ],
        "contraindications": [
            "Dị ứng với metformin, dapagliflozin, hoặc SGLT2 inhibitor.",
            "Đái tháo đường type 1.",
            "Nhiễm toan ceton do đái tháo đường.",
            "Suy thận nặng (eGFR <25 ml/min/1.73m²).",
            "Nhiễm toan lactic.",
            "Suy gan nặng.",
        ],
        "dosage": {
            "adult_start": "Metformin XR 1000mg/Dapagliflozin 5mg PO x 1 lần/ngày với bữa ăn tối (eGFR ≥60).",
            "adult_usual": "Metformin XR 1000mg/Dapagliflozin 10mg PO x 1 lần/ngày với bữa ăn tối (eGFR ≥60).",
            "adult_max": "Metformin XR 2000mg/Dapagliflozin 10mg PO x 1 lần/ngày với bữa ăn tối (eGFR ≥60).",
            "dm_t2": "Khởi đầu: Metformin XR 1000mg/Dapagliflozin 5mg PO x 1 lần/ngày với bữa ăn tối. Tăng dần: Metformin XR 1000mg/Dapagliflozin 10mg PO x 1 lần/ngày. Có thể tăng metformin lên 2000mg nếu cần. Điều chỉnh theo đường huyết và chức năng thận.",
            "heart_failure": "Metformin XR 1000mg/Dapagliflozin 10mg PO x 1 lần/ngày với bữa ăn tối (không phụ thuộc đái tháo đường, eGFR ≥25).",
            "ckd": "Metformin XR 1000mg/Dapagliflozin 10mg PO x 1 lần/ngày với bữa ăn tối (eGFR ≥25, không phụ thuộc đái tháo đường).",
            "elderly": "Khởi đầu liều thấp hơn: Metformin XR 500mg/Dapagliflozin 5mg PO x 1 lần/ngày với bữa ăn tối, tăng dần chậm. Người cao tuổi nhạy cảm hơn với tác dụng phụ (mất nước, hạ huyết áp, nhiễm trùng đường tiết niệu).",
            "pediatric_dosing": {
                "neonates": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "infants": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "children": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "adolescents": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "notes": "Không có chỉ định cho trẻ em. Dữ liệu về an toàn và hiệu quả ở trẻ em còn hạn chế."
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi có nguy cơ cao mất nước, hạ huyết áp, nhiễm trùng đường tiết niệu, và suy thận. Chức năng thận thường giảm theo tuổi.",
                "dose_adjustment": "Khởi đầu liều thấp hơn: Metformin XR 500mg/Dapagliflozin 5mg PO x 1 lần/ngày. Tăng dần chậm. Theo dõi chặt chẽ chức năng thận, huyết áp, và dấu hiệu mất nước. Không dùng nếu eGFR <25.",
                "monitoring": "Theo dõi chức năng thận (eGFR, creatinine), huyết áp, dấu hiệu mất nước, và dấu hiệu nhiễm trùng đường tiết niệu/nấm sinh dục thường xuyên hơn."
            },
            "renal_adjustment_dosage": {
                "normal": "Metformin XR 1000-2000mg/Dapagliflozin 10mg PO x 1 lần/ngày với bữa ăn tối (eGFR ≥60).",
                "30_60": "Giảm liều metformin (500-1000mg XR). Dapagliflozin 10mg PO x 1 lần/ngày nếu eGFR ≥25. Theo dõi chặt chẽ chức năng thận.",
                "under_30": "CHỐNG CHỈ ĐỊNH nếu eGFR <25. Không dùng nếu eGFR <25 ml/min/1.73m².",
                "dialysis": "CHỐNG CHỈ ĐỊNH",
                "notes": "Metformin chống chỉ định ở suy thận nặng (CrCl <30 hoặc eGFR <30). Dapagliflozin chống chỉ định ở eGFR <25. Cần kiểm tra eGFR trước khi bắt đầu và định kỳ."
            },
            "hepatic_adjustment_dosage": {
                "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
                "moderate": "Thận trọng. Theo dõi chức năng gan chặt chẽ.",
                "severe": "CHỐNG CHỈ ĐỊNH - Suy gan nặng. Metformin chống chỉ định ở suy gan nặng.",
                "notes": "Metformin chống chỉ định ở suy gan nặng (nguy cơ nhiễm toan lactic). Dapagliflozin chuyển hóa một phần qua gan (UGT). Suy gan nặng làm tăng nguy cơ nhiễm toan lactic."
            },
            "administration_route": "PO (uống)",
            "frequency": "1 lần/ngày (XR formulation)",
            "with_food": "PHẢI uống với bữa ăn (bữa ăn tối) để giảm tác dụng phụ tiêu hóa của metformin.",
            "timing": "Uống 1 lần/ngày với bữa ăn tối. Uống cùng giờ mỗi ngày để dễ nhớ.",
            "notes": "Uống với bữa ăn tối. Điều chỉnh liều dựa trên đáp ứng đường huyết và chức năng thận. CHỐNG CHỈ ĐỊNH nếu eGFR <25. Nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục. Lợi ích tim mạch và thận."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Giảm liều metformin; dapagliflozin không cần chỉnh liều nếu eGFR ≥25.",
            "under_30": "Không dùng nếu eGFR <25 ml/min/1.73m².",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (do metformin).",
            "Nhiễm trùng đường tiết niệu và đường sinh dục (do dapagliflozin).",
            "Mất nước, hạ huyết áp (do dapagliflozin).",
            "Nhiễm toan lactic (do metformin).",
            "Nhiễm toan ceton (do dapagliflozin).",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết.",
            "Diuretics: tăng nguy cơ mất nước, hạ huyết áp.",
        ],
        "pregnancy": "C: metformin; C: dapagliflozin - thận trọng trong thai kỳ.",
        "mechanism_of_action": (
            "Metformin là biguanide, giảm sản xuất glucose ở gan, tăng sử dụng glucose ở ngoại vi. "
            "Dapagliflozin là SGLT2 inhibitor, ức chế tái hấp thu glucose ở thận, tăng bài tiết glucose qua nước tiểu. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm đường huyết. "
            "Cả hai đều có lợi ích tim mạch và thận."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) trước và trong điều trị.",
            "Chức năng thận (creatinine, eGFR) trước và trong điều trị.",
            "Nhiễm trùng đường tiết niệu và đường sinh dục.",
            "Dấu hiệu mất nước, hạ huyết áp.",
            "Dấu hiệu nhiễm toan lactic và nhiễm toan ceton.",
        ],
        "precautions": [
            "Không dùng nếu eGFR <25 ml/min/1.73m².",
            "Không dùng cho đái tháo đường type 1.",
            "Nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục.",
            "Nguy cơ mất nước, hạ huyết áp.",
            "Nguy cơ nhiễm toan lactic và nhiễm toan ceton.",
            "Uống với bữa ăn.",
        ],
        "pharmacokinetics": {
            "half_life": "Metformin: ~6.2 giờ; Dapagliflozin: ~12.9 giờ.",
            "onset": "Giảm đường huyết trong vài ngày đến 1 tuần.",
            "duration": "24 giờ (XR dùng 1 lần/ngày).",
            "protein_binding": "Metformin: không đáng kể; Dapagliflozin: ~91%.",
            "clearance": "Metformin: thải qua thận; Dapagliflozin: chuyển hóa ở gan (UGT), thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Nhiễm toan lactic: metformin có thể gây nhiễm toan lactic. "
            "Nhiễm toan ceton: dapagliflozin có thể gây nhiễm toan ceton."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết.",
                    "management": "Giảm liều insulin/sulfonylurea khi bắt đầu phối hợp.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với metformin, dapagliflozin, hoặc SGLT2 inhibitor.",
                "Đái tháo đường type 1.",
                "Nhiễm toan ceton do đái tháo đường.",
                "Suy thận nặng (eGFR <25 ml/min/1.73m²).",
                "Nhiễm toan lactic.",
                "Suy gan nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 25-60) - giảm liều metformin.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Thận trọng trong thai kỳ. Insulin là lựa chọn ưu tiên.",
            "lactation": {
                "safety": "Caution",
                "details": "Thận trọng khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Chống chỉ định.",
            "notes": "Metformin chống chỉ định ở suy gan nặng. Dapagliflozin chuyển hóa một phần qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ đường huyết.", "Nhiễm toan lactic.", "Mất nước, hạ huyết áp.", "Nhiễm toan ceton."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ đường huyết: glucose IV nếu cần.",
                "Điều trị nhiễm toan lactic và nhiễm toan ceton: bù dịch, bicarbonate, insulin nếu cần.",
            ],
            "monitoring": "Đường huyết, lactate máu, ketone máu, pH máu, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống với bữa ăn.",
                "timing": "Uống 1 lần/ngày với bữa ăn tối.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Xigduo XR (metformin/dapagliflozin)",
                "DECLARE-TIMI 58 Study",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCTs (DECLARE-TIMI 58)",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["genitourinary"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["eGFR", "Genital/urinary infections"],
            },
            "guideline_tags": [
                "ADA 2024 Standards of Care - Diabetes",
                "AACE/ACE 2023 Type 2 Diabetes Guidelines",
                "FDA Black Box Warning - Fournier's Gangrene (rare)",
            ]
    },

    "Metformin/Empagliflozin": {
        "group": "Diabetes - Biguanide + SGLT2 Inhibitor (Fixed-Dose Combination)",
        "vietnamese_name": "Metformin/Empagliflozin, Synjardy, Synjardy XR",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2 (khi cần phối hợp metformin và empagliflozin).",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch.",
        ],
        "contraindications": [
            "Dị ứng với metformin, empagliflozin, hoặc SGLT2 inhibitor.",
            "Đái tháo đường type 1.",
            "Nhiễm toan ceton do đái tháo đường.",
            "Suy thận nặng (eGFR <30 ml/min/1.73m²).",
            "Nhiễm toan lactic.",
            "Suy gan nặng.",
        ],
        "dosage": {
            "adult_start": "Metformin 500mg/Empagliflozin 5mg PO x 2 lần/ngày với bữa ăn (eGFR ≥60).",
            "adult_usual": "Metformin 1000mg/Empagliflozin 5mg hoặc Metformin 1000mg/Empagliflozin 12.5mg PO x 2 lần/ngày với bữa ăn (eGFR ≥60).",
            "adult_max": "Metformin 1000mg/Empagliflozin 12.5mg PO x 2 lần/ngày (eGFR ≥60).",
            "adult_xr": "Metformin XR 1000mg/Empagliflozin 5mg hoặc Metformin XR 1000mg/Empagliflozin 12.5mg PO x 1 lần/ngày với bữa ăn tối (eGFR ≥60).",
            "dm_t2": "Khởi đầu: Metformin 500mg/Empagliflozin 5mg PO x 2 lần/ngày với bữa ăn. Tăng dần: Metformin 1000mg/Empagliflozin 5mg PO x 2 lần/ngày, sau đó Metformin 1000mg/Empagliflozin 12.5mg PO x 2 lần/ngày nếu cần. Dạng XR: 1 lần/ngày với bữa ăn tối. Điều chỉnh theo đường huyết và chức năng thận.",
            "heart_failure": "Metformin 1000mg/Empagliflozin 10mg PO x 2 lần/ngày với bữa ăn (không phụ thuộc đái tháo đường, eGFR ≥20).",
            "ckd": "Metformin 1000mg/Empagliflozin 10mg PO x 2 lần/ngày với bữa ăn (eGFR ≥20, không phụ thuộc đái tháo đường).",
            "elderly": "Khởi đầu liều thấp hơn: Metformin 500mg/Empagliflozin 5mg PO x 2 lần/ngày với bữa ăn, tăng dần chậm. Người cao tuổi nhạy cảm hơn với tác dụng phụ (mất nước, hạ huyết áp, nhiễm trùng đường tiết niệu).",
            "pediatric_dosing": {
                "neonates": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "infants": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "children": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "adolescents": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "notes": "Không có chỉ định cho trẻ em. Dữ liệu về an toàn và hiệu quả ở trẻ em còn hạn chế."
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi có nguy cơ cao mất nước, hạ huyết áp, nhiễm trùng đường tiết niệu, và suy thận. Chức năng thận thường giảm theo tuổi.",
                "dose_adjustment": "Khởi đầu liều thấp hơn: Metformin 500mg/Empagliflozin 5mg PO x 2 lần/ngày. Tăng dần chậm. Theo dõi chặt chẽ chức năng thận, huyết áp, và dấu hiệu mất nước. Không dùng nếu eGFR <20.",
                "monitoring": "Theo dõi chức năng thận (eGFR, creatinine), huyết áp, dấu hiệu mất nước, và dấu hiệu nhiễm trùng đường tiết niệu/nấm sinh dục thường xuyên hơn."
            },
            "renal_adjustment_dosage": {
                "normal": "Metformin 1000mg/Empagliflozin 5-12.5mg PO x 2 lần/ngày với bữa ăn (eGFR ≥60).",
                "30_60": "Giảm liều metformin (500-1000mg). Empagliflozin 10mg PO x 2 lần/ngày nếu eGFR ≥30. Theo dõi chặt chẽ chức năng thận.",
                "under_30": "CHỐNG CHỈ ĐỊNH nếu eGFR <30. Không dùng nếu eGFR <30 ml/min/1.73m².",
                "dialysis": "CHỐNG CHỈ ĐỊNH",
                "notes": "Metformin chống chỉ định ở suy thận nặng (CrCl <30 hoặc eGFR <30). Empagliflozin chống chỉ định ở eGFR <20. Cần kiểm tra eGFR trước khi bắt đầu và định kỳ."
            },
            "hepatic_adjustment_dosage": {
                "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
                "moderate": "Thận trọng. Theo dõi chức năng gan chặt chẽ.",
                "severe": "CHỐNG CHỈ ĐỊNH - Suy gan nặng. Metformin chống chỉ định ở suy gan nặng.",
                "notes": "Metformin chống chỉ định ở suy gan nặng (nguy cơ nhiễm toan lactic). Empagliflozin chuyển hóa một phần qua gan (glucuronidation). Suy gan nặng làm tăng nguy cơ nhiễm toan lactic."
            },
            "administration_route": "PO (uống)",
            "frequency": "2 lần/ngày (immediate-release) hoặc 1 lần/ngày (XR formulation)",
            "with_food": "PHẢI uống với bữa ăn để giảm tác dụng phụ tiêu hóa của metformin.",
            "timing": "Uống 2 lần/ngày với bữa sáng và bữa tối (hoặc 1 lần/ngày với bữa ăn tối nếu dùng XR). Uống cùng giờ mỗi ngày.",
            "notes": "Uống với bữa ăn. Điều chỉnh liều dựa trên đáp ứng đường huyết và chức năng thận. CHỐNG CHỈ ĐỊNH nếu eGFR <30. Nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục. Lợi ích tim mạch và thận rất lớn (EMPA-REG OUTCOME)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Giảm liều metformin; empagliflozin không cần chỉnh liều nếu eGFR ≥30.",
            "under_30": "Không dùng nếu eGFR <30 ml/min/1.73m².",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (do metformin) - thường giảm sau vài tuần.",
            "Nhiễm trùng đường tiết niệu (do empagliflozin).",
            "Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu) - do empagliflozin.",
            "Mất nước, hạ huyết áp (do empagliflozin).",
            "Nhiễm toan lactic (do metformin) - hiếm nhưng nghiêm trọng.",
            "Nhiễm toan ceton (do empagliflozin) - hiếm.",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết - có thể cần giảm liều.",
            "Diuretics: tăng nguy cơ mất nước, hạ huyết áp.",
        ],
        "pregnancy": "C: metformin; C: empagliflozin - thận trọng trong thai kỳ.",
        "mechanism_of_action": (
            "Metformin là biguanide, giảm sản xuất glucose ở gan, tăng sử dụng glucose ở ngoại vi, "
            "và cải thiện độ nhạy insulin. Empagliflozin là SGLT2 inhibitor, ức chế tái hấp thu glucose ở thận, "
            "làm tăng bài tiết glucose qua nước tiểu, giảm đường huyết. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm đường huyết với cơ chế bổ sung. "
            "Cả hai đều có lợi ích tim mạch và thận."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) trước và trong điều trị.",
            "Chức năng thận (creatinine, eGFR) trước và trong điều trị - QUAN TRỌNG.",
            "Chức năng gan (ALT, AST) trước và trong điều trị.",
            "Nhiễm trùng đường tiết niệu và đường sinh dục.",
            "Dấu hiệu mất nước, hạ huyết áp.",
            "Dấu hiệu nhiễm toan lactic (do metformin).",
            "Dấu hiệu nhiễm toan ceton (do empagliflozin).",
        ],
        "precautions": [
            "QUAN TRỌNG: Không dùng nếu eGFR <30 ml/min/1.73m² - nguy cơ nhiễm toan lactic và không hiệu quả empagliflozin.",
            "Không dùng cho đái tháo đường type 1 - nguy cơ nhiễm toan ceton.",
            "Ngừng metformin trước phẫu thuật lớn hoặc thủ thuật có cản quang.",
            "Nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục - vệ sinh tốt, uống nhiều nước.",
            "Nguy cơ mất nước, hạ huyết áp - đặc biệt ở người cao tuổi, dùng diuretics.",
            "Nguy cơ nhiễm toan ceton - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính.",
            "Uống với bữa ăn để giảm tác dụng phụ tiêu hóa của metformin.",
        ],
        "pharmacokinetics": {
            "half_life": "Metformin: ~6.2 giờ; Empagliflozin: ~12.4 giờ.",
            "onset": "Giảm đường huyết trong vài ngày đến 1 tuần.",
            "duration": "12 giờ (dùng 2 lần/ngày) hoặc 24 giờ (XR dùng 1 lần/ngày).",
            "protein_binding": "Metformin: không đáng kể; Empagliflozin: ~86.2%.",
            "clearance": "Metformin: thải qua thận; Empagliflozin: chuyển hóa ở gan (glucuronidation), thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Nhiễm toan lactic: metformin có thể gây nhiễm toan lactic, đặc biệt ở suy thận, suy gan, hoặc thiếu oxy. "
            "Ngừng ngay nếu có triệu chứng. Nhiễm toan ceton: empagliflozin có thể gây nhiễm toan ceton, "
            "đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết.",
                    "management": "Giảm liều insulin/sulfonylurea khi bắt đầu phối hợp. Theo dõi đường huyết chặt chẽ.",
                },
            ],
            "moderate": [
                {
                    "drug": "Loop diuretics (furosemide, torsemide)",
                    "mechanism": "Cả hai đều gây mất nước.",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp.",
                    "management": "Thận trọng. Theo dõi huyết áp, cân nặng, chức năng thận.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với metformin, empagliflozin, hoặc SGLT2 inhibitor.",
                "Đái tháo đường type 1.",
                "Nhiễm toan ceton do đái tháo đường.",
                "Suy thận nặng (eGFR <30 ml/min/1.73m²).",
                "Nhiễm toan lactic.",
                "Suy gan nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 30-60) - giảm liều metformin.",
                "Suy gan trung bình - thận trọng.",
                "Phẫu thuật lớn hoặc thủ thuật có cản quang - ngừng metformin trước.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Metformin và empagliflozin đều phân loại C. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, "
                "nhưng insulin là lựa chọn ưu tiên trong thai kỳ."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Metformin bài tiết vào sữa mẹ ở nồng độ thấp. Chưa rõ empagliflozin.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Chống chỉ định.",
            "notes": "Metformin chống chỉ định ở suy gan nặng. Empagliflozin chuyển hóa một phần qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết.",
                "Nhiễm toan lactic (do metformin).",
                "Mất nước, hạ huyết áp.",
                "Nhiễm toan ceton (do empagliflozin).",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ đường huyết: glucose IV nếu cần.",
                "Điều trị nhiễm toan lactic: bù dịch, bicarbonate, lọc máu nếu cần.",
                "Điều trị nhiễm toan ceton: insulin, bù dịch, bicarbonate nếu cần.",
                "Bù dịch nếu mất nước, hạ huyết áp.",
            ],
            "monitoring": "Đường huyết, lactate máu, ketone máu, pH máu, điện giải, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống với bữa ăn để giảm tác dụng phụ tiêu hóa của metformin.",
                "timing": "Uống 2 lần/ngày với bữa sáng và bữa tối (hoặc 1 lần/ngày với bữa tối nếu dùng XR).",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Synjardy (metformin/empagliflozin), Synjardy XR",
                "EMPA-REG OUTCOME Study",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCTs (EMPA-REG OUTCOME)",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["genitourinary"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["eGFR", "Genital/urinary infections"],
            },
            "guideline_tags": [
                "ADA 2024 Standards of Care - Diabetes",
                "AACE/ACE 2023 Type 2 Diabetes Guidelines",
                "FDA Black Box Warning - Fournier's Gangrene (rare)",
            ]
    },

    "Metformin/Glibenclamide":     {
        "group": "Diabetes - Biguanide + Sulfonylurea (Fixed-Dose Combination)",
        "vietnamese_name": "Metformin/Glibenclamide, Glucovance",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đái tháo đường type 2 (khi cần phối hợp metformin và glibenclamide)."
    ],
        "contraindications": [
            "Dị ứng với metformin, glibenclamide, hoặc sulfonylurea.",
            "Đái tháo đường type 1.",
            "Nhiễm toan ceton do đái tháo đường.",
            "Suy thận nặng (CrCl <30 ml/min/1.73m²).",
            "Nhiễm toan lactic.",
            "Suy gan nặng."
    ],
        "dosage": {
            "adult_start": "Metformin 500mg/Glibenclamide 2.5mg PO x 2 lần/ngày với bữa ăn (CrCl ≥60).",
            "adult_usual": "Metformin 500mg/Glibenclamide 5mg PO x 2 lần/ngày với bữa ăn (CrCl ≥60).",
            "adult_max": "Metformin 500mg/Glibenclamide 5mg PO x 2 lần/ngày (CrCl ≥60).",
            "dm_t2": "Khởi đầu: Metformin 500mg/Glibenclamide 2.5mg PO x 2 lần/ngày với bữa ăn. Tăng dần: Metformin 500mg/Glibenclamide 5mg PO x 2 lần/ngày nếu cần. Điều chỉnh theo đường huyết và chức năng thận. Nguy cơ hạ đường huyết cao.",
            "elderly": "Khởi đầu liều thấp hơn: Metformin 250mg/Glibenclamide 1.25mg PO x 2 lần/ngày với bữa ăn, tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết.",
            "pediatric_dosing": {
                "neonates": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "infants": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "children": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "adolescents": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "notes": "Không có chỉ định cho trẻ em. Dữ liệu về an toàn và hiệu quả ở trẻ em còn hạn chế."
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi có nguy cơ hạ đường huyết cao hơn do suy thận, suy gan, bỏ bữa, tương tác thuốc. Hạ đường huyết có thể nghiêm trọng và kéo dài.",
                "dose_adjustment": "Khởi đầu liều thấp hơn: Metformin 250mg/Glibenclamide 1.25mg PO x 2 lần/ngày. Tăng dần chậm hơn. Điều chỉnh liều theo chức năng thận, gan. Tránh dùng ở suy thận nặng (CrCl <30).",
                "monitoring": "Theo dõi đường huyết chặt chẽ. Theo dõi dấu hiệu hạ đường huyết. Theo dõi chức năng thận, gan định kỳ. Cảnh báo bệnh nhân về dấu hiệu và cách xử trí hạ đường huyết."
            },
            "renal_adjustment_dosage": {
                "normal": "Metformin 500mg/Glibenclamide 2.5-5mg PO x 2 lần/ngày với bữa ăn (CrCl ≥60).",
                "30_60": "Giảm liều metformin (250-500mg). Glibenclamide: Khởi đầu 1.25mg PO x 2 lần/ngày, tăng dần thận trọng. Theo dõi sát đường huyết.",
                "under_30": "CHỐNG CHỈ ĐỊNH - Không dùng nếu CrCl <30 (CrCl <30 hoặc eGFR <30).",
                "dialysis": "CHỐNG CHỈ ĐỊNH",
                "notes": "Metformin chống chỉ định ở suy thận nặng (CrCl <30). Glibenclamide chống chỉ định ở suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết nghiêm trọng."
            },
            "hepatic_adjustment_dosage": {
                "mild": "Thận trọng. Theo dõi chức năng gan.",
                "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan và đường huyết chặt chẽ.",
                "severe": "CHỐNG CHỈ ĐỊNH - Suy gan nặng. Metformin và glibenclamide đều chống chỉ định ở suy gan nặng.",
                "notes": "Metformin chống chỉ định ở suy gan nặng (nguy cơ nhiễm toan lactic). Glibenclamide chuyển hóa ở gan, suy gan nặng làm tăng nguy cơ hạ đường huyết nghiêm trọng."
            },
            "administration_route": "PO (uống)",
            "frequency": "2 lần/ngày",
            "with_food": "PHẢI uống với bữa ăn để giảm tác dụng phụ tiêu hóa của metformin và tránh hạ đường huyết.",
            "timing": "Uống 2 lần/ngày với bữa sáng và bữa tối. Uống cùng giờ mỗi ngày. Không bỏ bữa sau khi uống.",
            "notes": "Uống với bữa ăn. Điều chỉnh liều dựa trên đáp ứng đường huyết và chức năng thận. CHỐNG CHỈ ĐỊNH nếu CrCl <30. Nguy cơ hạ đường huyết cao (do glibenclamide) - theo dõi chặt chẽ. Nguy cơ nhiễm toan lactic (do metformin)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Giảm liều metformin; thận trọng với glibenclamide.",
            "under_30": "CHỐNG CHỈ ĐỊNH - không dùng nếu CrCl <30 ml/min/1.73m².",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (do metformin).",
            "Hạ đường huyết (do glibenclamide) - phổ biến và nghiêm trọng.",
            "Tăng cân (do glibenclamide).",
            "Nhiễm toan lactic (do metformin) - hiếm nhưng nghiêm trọng."
    ],
        "interactions": [
            "Rượu: tăng nguy cơ hạ đường huyết và nhiễm toan lactic.",
            "Beta-blocker: che dấu triệu chứng hạ đường huyết."
    ],
        "pregnancy": "B: metformin; C: glibenclamide - thận trọng trong thai kỳ.",
        "mechanism_of_action": """Metformin giảm sản xuất glucose ở gan, tăng sử dụng glucose ở ngoại vi. Glibenclamide kích thích tế bào beta tiết insulin. Phối hợp hai thuốc có tác dụng hiệp đồng giảm đường huyết.""",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) trước và trong điều trị.",
            "Chức năng thận (creatinine, CrCl) - QUAN TRỌNG.",
            "Dấu hiệu hạ đường huyết - phổ biến và nghiêm trọng.",
            "Dấu hiệu nhiễm toan lactic."
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH nếu CrCl <30 ml/min/1.73m².",
            "Nguy cơ hạ đường huyết cao (do glibenclamide) - theo dõi chặt chẽ.",
            "Nguy cơ nhiễm toan lactic - ngừng ngay nếu có triệu chứng.",
            "Uống với bữa ăn.",
            "TRÁNH RƯỢU hoàn toàn."
    ],
        "pharmacokinetics": {
            "half_life": "Metformin: ~6.2 giờ; Glibenclamide: ~10 giờ.",
            "onset": "Glibenclamide: 2-4 giờ; Metformin: vài ngày.",
            "duration": "12 giờ (dùng 2 lần/ngày).",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm.",
        "black_box_warnings": """Nhiễm toan lactic: metformin có thể gây nhiễm toan lactic. Hạ đường huyết: glibenclamide có thể gây hạ đường huyết nghiêm trọng.""",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Glucovance (metformin/glibenclamide)",
                "ADA/EASD Diabetes Guidelines 2024"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "",
        },
        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": [],
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Metformin/Pioglitazone":     {
        "group": "Diabetes - Biguanide + Thiazolidinedione (Fixed-Dose Combination)",
        "vietnamese_name": "Metformin/Pioglitazone, Actoplus Met",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đái tháo đường type 2 (khi cần phối hợp metformin và pioglitazone)."
    ],
        "contraindications": [
            "Dị ứng với metformin, pioglitazone, hoặc TZD.",
            "Đái tháo đường type 1.",
            "Suy tim (NYHA class III-IV).",
            "Suy thận nặng (CrCl <30 ml/min/1.73m²).",
            "Nhiễm toan lactic.",
            "Suy gan nặng.",
            "Ung thư bàng quang."
    ],
        "dosage": {
            "adult_start": "Metformin 500mg/Pioglitazone 15mg PO x 2 lần/ngày với bữa ăn (CrCl ≥60).",
            "adult_usual": "Metformin 500mg/Pioglitazone 15mg hoặc Metformin 850mg/Pioglitazone 15mg PO x 2 lần/ngày với bữa ăn (CrCl ≥60).",
            "adult_max": "Metformin 850mg/Pioglitazone 15mg PO x 2 lần/ngày (CrCl ≥60).",
            "dm_t2": "Khởi đầu: Metformin 500mg/Pioglitazone 15mg PO x 2 lần/ngày với bữa ăn. Tăng dần: Metformin 850mg/Pioglitazone 15mg PO x 2 lần/ngày nếu cần. Tác dụng chậm (2-4 tuần cho pioglitazone). Điều chỉnh theo đường huyết và chức năng thận.",
            "elderly": "Khởi đầu liều thấp hơn: Metformin 250mg/Pioglitazone 15mg PO x 2 lần/ngày với bữa ăn, tăng dần chậm. Người cao tuổi nhạy cảm hơn với giữ nước, suy tim, và gãy xương.",
            "pediatric_dosing": {
                "neonates": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "infants": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "children": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "adolescents": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "notes": "Không có chỉ định cho trẻ em. Dữ liệu về an toàn và hiệu quả ở trẻ em còn hạn chế."
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi có nguy cơ cao giữ nước, suy tim, và gãy xương. Chức năng gan có thể giảm.",
                "dose_adjustment": "Khởi đầu liều thấp hơn: Metformin 250mg/Pioglitazone 15mg PO x 2 lần/ngày. Theo dõi chặt chẽ dấu hiệu suy tim, phù, và chức năng gan. Cân nhắc liều thấp hơn.",
                "monitoring": "Theo dõi chức năng gan (ALT, AST), dấu hiệu suy tim (khó thở, phù, tăng cân), và nguy cơ gãy xương. Giáo dục bệnh nhân về các dấu hiệu cần báo cáo."
            },
            "renal_adjustment_dosage": {
                "normal": "Metformin 500-850mg/Pioglitazone 15mg PO x 2 lần/ngày với bữa ăn (CrCl ≥60).",
                "30_60": "Giảm liều metformin (250-500mg). Pioglitazone không cần điều chỉnh liều. Thận trọng.",
                "under_30": "CHỐNG CHỈ ĐỊNH - Không dùng nếu CrCl <30 (CrCl <30 hoặc eGFR <30).",
                "dialysis": "CHỐNG CHỈ ĐỊNH",
                "notes": "Metformin chống chỉ định ở suy thận nặng (CrCl <30). Pioglitazone không thải trừ qua thận đáng kể, không cần điều chỉnh liều ở suy thận. Tuy nhiên, thận trọng ở bệnh nhân suy thận nặng do các bệnh lý đi kèm."
            },
            "hepatic_adjustment_dosage": {
                "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
                "moderate": "Thận trọng, theo dõi chức năng gan chặt chẽ. Ngừng nếu ALT >3x ULN.",
                "severe": "CHỐNG CHỈ ĐỊNH - Suy gan nặng. Metformin và pioglitazone đều chống chỉ định ở suy gan nặng.",
                "notes": "Metformin chống chỉ định ở suy gan nặng (nguy cơ nhiễm toan lactic). Pioglitazone chuyển hóa ở gan qua CYP2C8 và CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc gan. Ngừng nếu ALT >3x ULN."
            },
            "administration_route": "PO (uống)",
            "frequency": "2 lần/ngày",
            "with_food": "PHẢI uống với bữa ăn để giảm tác dụng phụ tiêu hóa của metformin.",
            "timing": "Uống 2 lần/ngày với bữa sáng và bữa tối. Uống cùng giờ mỗi ngày.",
            "notes": "Uống với bữa ăn. Điều chỉnh liều dựa trên đáp ứng đường huyết và chức năng thận. CHỐNG CHỈ ĐỊNH nếu CrCl <30 hoặc suy tim (NYHA class III-IV). Nguy cơ giữ nước, phù, suy tim (do pioglitazone). Nguy cơ nhiễm toan lactic (do metformin). Nguy cơ gãy xương (đặc biệt ở phụ nữ)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Giảm liều metformin.",
            "under_30": "CHỐNG CHỈ ĐỊNH - không dùng nếu CrCl <30 ml/min/1.73m².",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (do metformin).",
            "Giữ nước, phù (do pioglitazone) - tăng nguy cơ suy tim.",
            "Tăng cân (do pioglitazone).",
            "Gãy xương (phụ nữ có nguy cơ tăng).",
            "Nhiễm toan lactic (do metformin).",
            "Ung thư bàng quang (tăng nhẹ nguy cơ do pioglitazone)."
    ],
        "interactions": [
            "Insulin: tăng nguy cơ suy tim, phù."
    ],
        "pregnancy": "B: metformin; C: pioglitazone - thận trọng trong thai kỳ.",
        "mechanism_of_action": """Metformin giảm sản xuất glucose ở gan, tăng sử dụng glucose ở ngoại vi. Pioglitazone tăng nhạy cảm với insulin ở mô ngoại vi. Phối hợp hai thuốc có tác dụng hiệp đồng giảm đường huyết.""",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) trước và trong điều trị.",
            "Chức năng thận (creatinine, CrCl) - QUAN TRỌNG.",
            "Dấu hiệu suy tim, phù (do pioglitazone).",
            "Dấu hiệu nhiễm toan lactic.",
            "Gãy xương (đặc biệt ở phụ nữ)."
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH nếu suy tim (NYHA class III-IV).",
            "CHỐNG CHỈ ĐỊNH nếu CrCl <30 ml/min/1.73m².",
            "Nguy cơ giữ nước, phù, suy tim - ngừng ngay nếu có dấu hiệu.",
            "Nguy cơ nhiễm toan lactic.",
            "Uống với bữa ăn."
    ],
        "pharmacokinetics": {
            "half_life": "Metformin: ~6.2 giờ; Pioglitazone: 16-24 giờ.",
            "onset": "Metformin: vài ngày; Pioglitazone: 2-4 tuần.",
            "duration": "12 giờ (dùng 2 lần/ngày).",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm.",
        "black_box_warnings": "Suy tim: pioglitazone có thể gây suy tim. Nhiễm toan lactic: metformin có thể gây nhiễm toan lactic.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Actoplus Met (metformin/pioglitazone)",
                "ADA/EASD Diabetes Guidelines 2024"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "",
        },
        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": [],
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Metformin/Sitagliptin": {
        "group": "Diabetes - Biguanide + DPP-4 Inhibitor (Fixed-Dose Combination)",
        "vietnamese_name": "Metformin/Sitagliptin, Janumet, Janumet XR",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2 (khi cần phối hợp metformin và sitagliptin).",
        ],
        "contraindications": [
            "Dị ứng với metformin, sitagliptin, hoặc DPP-4 inhibitor.",
            "Suy thận nặng (eGFR <30 ml/min/1.73m²).",
            "Nhiễm toan lactic.",
            "Nhiễm toan ceton do đái tháo đường.",
            "Suy gan nặng.",
        ],
        "dosage": {
            "adult_start": "Metformin 500mg/Sitagliptin 50mg PO x 2 lần/ngày với bữa ăn (eGFR ≥60).",
            "adult_usual": "Metformin 1000mg/Sitagliptin 50mg PO x 2 lần/ngày với bữa ăn (eGFR ≥60).",
            "adult_max": "Metformin 1000mg/Sitagliptin 50mg PO x 2 lần/ngày (eGFR ≥60).",
            "adult_xr": "Metformin XR 1000mg/Sitagliptin 100mg PO x 1 lần/ngày với bữa ăn tối (eGFR ≥60).",
            "dm_t2": "Khởi đầu: Metformin 500mg/Sitagliptin 50mg PO x 2 lần/ngày với bữa ăn. Tăng dần: Metformin 1000mg/Sitagliptin 50mg PO x 2 lần/ngày nếu cần. Dạng XR: 1 lần/ngày với bữa ăn tối. Điều chỉnh theo đường huyết và chức năng thận. Ít gây hạ đường huyết.",
            "elderly": "Khởi đầu liều thấp hơn: Metformin 250mg/Sitagliptin 50mg PO x 2 lần/ngày với bữa ăn, tăng dần chậm. Người cao tuổi nhạy cảm hơn với tác dụng phụ tiêu hóa. Điều chỉnh liều sitagliptin theo CrCl.",
            "pediatric_dosing": {
                "neonates": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "infants": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "children": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "adolescents": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "notes": "Không có chỉ định cho trẻ em. Dữ liệu về an toàn và hiệu quả ở trẻ em còn hạn chế."
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ tiêu hóa (buồn nôn, nôn, tiêu chảy). Chức năng thận có thể giảm, cần điều chỉnh liều sitagliptin theo CrCl.",
                "dose_adjustment": "Khởi đầu liều thấp hơn: Metformin 250mg/Sitagliptin 50mg PO x 2 lần/ngày. Tăng liều từ từ và theo dõi chặt chẽ tác dụng phụ. Điều chỉnh liều sitagliptin theo CrCl. Theo dõi chức năng thận.",
                "monitoring": "Theo dõi chức năng thận (CrCl, eGFR), dấu hiệu tác dụng phụ tiêu hóa, và dấu hiệu viêm tụy cấp. Giáo dục bệnh nhân về cách xử trí buồn nôn."
            },
            "renal_adjustment_dosage": {
                "normal": "Metformin 1000mg/Sitagliptin 50mg PO x 2 lần/ngày với bữa ăn (eGFR ≥60).",
                "30_60": "Giảm liều metformin (500mg). Sitagliptin 50mg PO x 2 lần/ngày (eGFR 30-60). Theo dõi chặt chẽ chức năng thận.",
                "under_30": "CHỐNG CHỈ ĐỊNH - Không dùng nếu eGFR <30 (eGFR <30).",
                "dialysis": "CHỐNG CHỈ ĐỊNH",
                "notes": "Metformin chống chỉ định ở suy thận nặng (CrCl <30 hoặc eGFR <30). Sitagliptin thải trừ chủ yếu qua thận, cần điều chỉnh liều ở suy thận: 50mg x 2 lần/ngày (eGFR 30-60), 25mg x 2 lần/ngày (eGFR <30). Tuy nhiên, phối hợp với metformin nên tránh ở eGFR <30."
            },
            "hepatic_adjustment_dosage": {
                "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
                "moderate": "Thận trọng. Theo dõi chức năng gan chặt chẽ.",
                "severe": "CHỐNG CHỈ ĐỊNH - Suy gan nặng. Metformin chống chỉ định ở suy gan nặng.",
                "notes": "Metformin không chuyển hóa qua gan nhưng chống chỉ định ở suy gan nặng (nguy cơ nhiễm toan lactic). Sitagliptin chuyển hóa một phần qua gan. Suy gan nặng làm tăng nguy cơ nhiễm toan lactic."
            },
            "administration_route": "PO (uống)",
            "frequency": "2 lần/ngày (immediate-release) hoặc 1 lần/ngày (XR formulation)",
            "with_food": "PHẢI uống với bữa ăn để giảm tác dụng phụ tiêu hóa của metformin.",
            "timing": "Uống 2 lần/ngày với bữa sáng và bữa tối (hoặc 1 lần/ngày với bữa ăn tối nếu dùng XR). Uống cùng giờ mỗi ngày.",
            "notes": "Uống với bữa ăn để giảm tác dụng phụ tiêu hóa. Điều chỉnh liều dựa trên đáp ứng đường huyết và chức năng thận. CHỐNG CHỈ ĐỊNH nếu eGFR <30. Nguy cơ nhiễm toan lactic (do metformin). Nguy cơ viêm tụy cấp (do sitagliptin) - hiếm nhưng nghiêm trọng. Ít gây hạ đường huyết."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Giảm liều metformin; sitagliptin không cần chỉnh liều.",
            "under_30": "Không dùng nếu eGFR <30 ml/min/1.73m².",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy, đau bụng (do metformin) - thường giảm sau vài tuần.",
            "Nhiễm trùng đường hô hấp trên (do sitagliptin).",
            "Nhiễm toan lactic (do metformin) - hiếm nhưng nghiêm trọng.",
            "Viêm tụy cấp (do sitagliptin) - hiếm nhưng nghiêm trọng.",
            "Hạ đường huyết (khi dùng với insulin hoặc sulfonylurea).",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết - có thể cần giảm liều.",
            "Digoxin: sitagliptin có thể tăng nhẹ nồng độ digoxin.",
        ],
        "pregnancy": "B: metformin; B: sitagliptin - thận trọng trong thai kỳ.",
        "mechanism_of_action": (
            "Metformin là biguanide, giảm sản xuất glucose ở gan, tăng sử dụng glucose ở ngoại vi, "
            "và cải thiện độ nhạy insulin. Sitagliptin là DPP-4 inhibitor, ức chế enzyme DPP-4, "
            "làm tăng nồng độ GLP-1 và GIP nội sinh, dẫn đến tăng giải phóng insulin phụ thuộc glucose "
            "và giảm giải phóng glucagon. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm đường huyết với cơ chế bổ sung."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) trước và trong điều trị.",
            "Chức năng thận (creatinine, eGFR) trước và trong điều trị - QUAN TRỌNG.",
            "Chức năng gan (ALT, AST) trước và trong điều trị.",
            "Dấu hiệu nhiễm toan lactic (đau bụng, buồn nôn, nôn, khó thở, mệt mỏi) - nguy hiểm.",
            "Dấu hiệu viêm tụy cấp (đau bụng trên, buồn nôn, nôn) - nguy hiểm.",
            "Dấu hiệu hạ đường huyết khi dùng với insulin/sulfonylurea.",
        ],
        "precautions": [
            "QUAN TRỌNG: Không dùng nếu eGFR <30 ml/min/1.73m² - nguy cơ nhiễm toan lactic.",
            "Ngừng metformin trước phẫu thuật lớn hoặc thủ thuật có cản quang (nguy cơ nhiễm toan lactic).",
            "Nguy cơ nhiễm toan lactic - ngừng ngay nếu có triệu chứng, điều trị tại bệnh viện.",
            "Nguy cơ viêm tụy cấp - ngừng ngay nếu có đau bụng trên nghiêm trọng.",
            "Uống với bữa ăn để giảm tác dụng phụ tiêu hóa của metformin.",
            "Giảm liều insulin/sulfonylurea khi bắt đầu phối hợp để tránh hạ đường huyết.",
        ],
        "pharmacokinetics": {
            "half_life": "Metformin: ~6.2 giờ; Sitagliptin: ~12.4 giờ.",
            "onset": "Giảm đường huyết trong vài ngày đến 1 tuần.",
            "duration": "12 giờ (dùng 2 lần/ngày) hoặc 24 giờ (XR dùng 1 lần/ngày).",
            "protein_binding": "Metformin: không đáng kể; Sitagliptin: ~38%.",
            "clearance": "Metformin: thải qua thận (không chuyển hóa); Sitagliptin: thải qua thận (ít chuyển hóa).",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Nhiễm toan lactic: metformin có thể gây nhiễm toan lactic, đặc biệt ở suy thận, "
            "suy gan, hoặc thiếu oxy. Ngừng ngay nếu có triệu chứng. "
            "Viêm tụy cấp: sitagliptin có thể gây viêm tụy cấp, có thể tử vong."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea (glibenclamide, gliclazide)",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết.",
                    "management": "Giảm liều insulin/sulfonylurea khi bắt đầu phối hợp. Theo dõi đường huyết chặt chẽ.",
                },
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Sitagliptin có thể tăng nhẹ nồng độ digoxin.",
                    "effect": "Tăng nguy cơ độc tính digoxin.",
                    "management": "Thận trọng. Theo dõi nồng độ digoxin.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với metformin, sitagliptin, hoặc DPP-4 inhibitor.",
                "Suy thận nặng (eGFR <30 ml/min/1.73m²).",
                "Nhiễm toan lactic.",
                "Nhiễm toan ceton do đái tháo đường.",
                "Suy gan nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 30-60) - giảm liều metformin.",
                "Suy gan trung bình - thận trọng.",
                "Phẫu thuật lớn hoặc thủ thuật có cản quang - ngừng metformin trước.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": (
                "Metformin và sitagliptin đều phân loại B. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, "
                "nhưng insulin là lựa chọn ưu tiên trong thai kỳ. Theo dõi đường huyết chặt chẽ."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Metformin bài tiết vào sữa mẹ ở nồng độ thấp. Chưa rõ sitagliptin.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Chống chỉ định.",
            "notes": "Metformin không chuyển hóa qua gan nhưng chống chỉ định ở suy gan nặng (nguy cơ nhiễm toan lactic). Sitagliptin chuyển hóa một phần qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (nếu dùng với insulin/sulfonylurea).",
                "Nhiễm toan lactic (do metformin) - nguy hiểm.",
                "Buồn nôn, nôn, tiêu chảy nặng.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ đường huyết: glucose IV nếu cần.",
                "Điều trị nhiễm toan lactic: bù dịch, bicarbonate, lọc máu nếu cần - điều trị tại ICU.",
                "Điều trị hỗ trợ.",
            ],
            "monitoring": "Đường huyết, lactate máu, pH máu, điện giải, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống với bữa ăn để giảm tác dụng phụ tiêu hóa của metformin.",
                "timing": "Uống 2 lần/ngày với bữa sáng và bữa tối (hoặc 1 lần/ngày với bữa tối nếu dùng XR).",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Janumet (metformin/sitagliptin), Janumet XR",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },

}

__all__ = ["DIABETES_FIXED_DOSE_COMBINATIONS"]

