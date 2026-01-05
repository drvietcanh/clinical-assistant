"""
Bisphosphonates for Osteoporosis Treatment
Alendronate, Risedronate, Ibandronate, Zoledronic acid
"""

BISPHOSPHONATES_DRUGS = {
    "Alendronate": {
        "group": "Endocrinology - Bisphosphonate (Osteoporosis)",
        "vietnamese_name": "Alendronate, Fosamax",
        "administration": ["PO"],
        "indications": [
            "Loãng xương sau mãn kinh.",
            "Loãng xương ở nam giới.",
            "Loãng xương do corticosteroid.",
            "Bệnh Paget xương.",
        ],
        "contraindications": [
            "Dị ứng với alendronate.",
            "Hẹp thực quản, rối loạn vận động thực quản.",
            "Không thể đứng hoặc ngồi thẳng ít nhất 30 phút.",
            "Suy thận nặng (CrCl <35 ml/min).",
            "Hạ calci máu.",
        ],
        "dosage": {
            "adult_osteoporosis_daily": "10mg PO mỗi ngày.",
            "adult_osteoporosis_weekly": "70mg PO mỗi tuần (khuyến cáo).",
            "adult_paget": "40mg PO mỗi ngày x 6 tháng.",
            "notes": "Uống lúc đói, ít nhất 30 phút trước ăn hoặc uống thuốc khác. Uống với nước lọc (≥200ml). Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <35 ml/min.",
        },
        "side_effects": [
            "Kích ứng thực quản, đau bụng trên, khó nuốt (nếu không uống đúng cách).",
            "Đau cơ, đau xương, đau khớp.",
            "Hoại tử xương hàm (ONJ) - hiếm nhưng nghiêm trọng.",
            "Gãy xương đùi không điển hình - hiếm.",
            "Hạ calci máu, hạ phospho máu.",
            "Viêm dạ dày, loét dạ dày.",
        ],
        "interactions": [
            "Calcium, sắt, antacids: giảm hấp thu alendronate - dùng cách xa ít nhất 30 phút.",
            "NSAIDs: tăng nguy cơ kích ứng dạ dày.",
        ],
        "pregnancy": "C: tránh dùng trong thai kỳ.",
        "mechanism_of_action": (
            "Alendronate là bisphosphonate thế hệ 2, ức chế hủy xương bằng cách gắn vào hydroxyapatite "
            "trong xương và ức chế enzyme farnesyl pyrophosphate synthase (FPPS) trong tế bào hủy xương (osteoclasts). "
            "FPPS cần thiết cho quá trình prenylation protein, giúp tế bào hủy xương hoạt động. "
            "Bằng cách ức chế FPPS, alendronate làm giảm hoạt động và gây apoptosis của tế bào hủy xương, "
            "dẫn đến giảm hủy xương và tăng mật độ xương. Alendronate có ái lực cao với xương, "
            "gắn vào bề mặt xương đang được tái cấu trúc và tồn tại trong xương nhiều năm."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 1-2 năm.",
            "Calci máu, phospho máu trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước điều trị - không dùng nếu CrCl <35 ml/min.",
            "Dấu hiệu kích ứng thực quản (đau ngực, khó nuốt).",
            "Dấu hiệu hoại tử xương hàm (đau hàm, sưng, răng lung lay, chảy mủ).",
            "Dấu hiệu gãy xương đùi không điển hình (đau đùi, háng).",
        ],
        "precautions": [
            "QUAN TRỌNG: Uống lúc đói, ít nhất 30 phút trước ăn hoặc uống thuốc khác.",
            "Uống với nước lọc (≥200ml), không uống với nước khoáng, cà phê, trà, nước hoa quả.",
            "Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống để tránh kích ứng thực quản.",
            "Không nằm ngay sau khi uống.",
            "Dùng cách xa calcium, sắt, antacids ít nhất 30 phút.",
            "Nguy cơ hoại tử xương hàm: đánh giá răng miệng trước điều trị, tránh phẫu thuật răng trong khi dùng.",
            "Nguy cơ gãy xương đùi không điển hình: theo dõi đau đùi, háng.",
            "Không dùng nếu CrCl <35 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Hơn 10 năm (trong xương), ~10 giờ (trong máu).",
            "onset": "Giảm markers hủy xương trong 1-3 tháng, tăng mật độ xương trong 6-12 tháng.",
            "duration": "Tác dụng kéo dài nhiều năm sau khi ngừng (do gắn vào xương).",
            "protein_binding": "~78% (gắn với xương).",
            "clearance": "Gắn vào xương (50%), thải qua thận (50%).",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Hoại tử xương hàm (ONJ): có thể xảy ra, đặc biệt ở bệnh nhân phẫu thuật răng, "
            "ung thư, dùng corticosteroid. Đánh giá răng miệng trước điều trị. "
            "Gãy xương đùi không điển hình: tăng nguy cơ gãy xương đùi không điển hình."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium, Sắt, Antacids, Multivitamins có calcium/sắt",
                    "mechanism": "Tạo phức hợp không hòa tan với alendronate, giảm hấp thu.",
                    "effect": "Giảm hấp thu alendronate, giảm hiệu quả.",
                    "management": "Dùng cách xa ít nhất 30 phút. Uống alendronate trước, sau đó mới uống calcium/sắt.",
                },
            ],
            "moderate": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Cả hai đều có thể gây kích ứng dạ dày.",
                    "effect": "Tăng nguy cơ kích ứng dạ dày, loét dạ dày.",
                    "management": "Thận trọng. Có thể cần dùng PPI hoặc H2 blocker.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với alendronate hoặc bisphosphonate.",
                "Hẹp thực quản, rối loạn vận động thực quản.",
                "Không thể đứng hoặc ngồi thẳng ít nhất 30 phút.",
                "Suy thận nặng (CrCl <35 ml/min).",
                "Hạ calci máu.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 35-60) - thận trọng, cân nhắc giảm liều.",
                "Tiền sử bệnh dạ dày - tăng nguy cơ kích ứng.",
                "Phẫu thuật răng gần đây hoặc dự kiến - tăng nguy cơ ONJ.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Có thể ảnh hưởng đến phát triển xương thai nhi.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều (không chuyển hóa qua gan).",
            "notes": "Alendronate không chuyển hóa qua gan, thải qua thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng thực quản nặng, đau ngực, khó nuốt.",
                "Hạ calci máu.",
                "Đau bụng, buồn nôn, nôn.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Uống sữa hoặc antacid để che phủ thực quản.",
                "Không gây nôn (có thể làm tổn thương thực quản thêm).",
                "Điều trị hạ calci máu: calcium IV nếu cần.",
                "Theo dõi tại bệnh viện.",
            ],
            "monitoring": "Calci máu, dấu hiệu kích ứng thực quản, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống lúc đói, ít nhất 30 phút trước ăn hoặc uống thuốc khác.",
                "timing": "Uống vào buổi sáng, lúc đói, với nước lọc (≥200ml). Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống.",
                "notes": "QUAN TRỌNG: Uống với nước lọc, không uống với nước khoáng, cà phê, trà, nước hoa quả. Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fosamax (alendronate)",
                "FIT Study - Fracture Intervention Trial",
                "NOF Guidelines - Osteoporosis Treatment 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCTs (FIT)",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "CRITICAL - Esophageal irritation/ulceration (if not taken correctly - must take on empty stomach, remain upright 30 minutes)",
                "dental": "Black Box Warning - Osteonecrosis of the jaw (ONJ) - rare but serious",
                "skeletal": "Black Box Warning - Atypical femur fractures - rare but serious",
                "metabolic": "Hypocalcemia, hypophosphatemia"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Dental evaluation before treatment (ONJ risk)",
                "Black Box Warning - Signs of ONJ (jaw pain, swelling, loose teeth, discharge) - CRITICAL",
                "Black Box Warning - Atypical femur fracture signs (thigh, groin pain) - CRITICAL",
                "CRITICAL - Administration technique: empty stomach, ≥200ml water, remain upright 30 minutes",
                "Serum calcium, phosphorus (before and during treatment)",
                "Renal function (creatinine, eGFR - contraindicated if CrCl <35 ml/min)",
                "Bone density (DEXA scan) before treatment and after 1-2 years",
                "Calcium, iron, antacids interaction (take at least 30 minutes apart)"
            ],
            "look_alike_sound_alike": ["Alendronate", "Ibandronate", "Risedronate"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Osteonecrosis of the Jaw (ONJ)",
            "FDA Black Box Warning - Atypical Femur Fractures",
            "NOF Guidelines - Osteoporosis Treatment 2024",
            "ASBMR Guidelines - Bisphosphonate Use",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Ibandronate": {
        "group": "Endocrinology - Bisphosphonate (Osteoporosis)",
        "vietnamese_name": "Ibandronate, Boniva",
        "administration": ["PO", "IV"],
        "indications": [
            "Loãng xương sau mãn kinh (PO hoặc IV).",
        ],
        "contraindications": [
            "Dị ứng với ibandronate.",
            "Hẹp thực quản, rối loạn vận động thực quản (PO).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ calci máu.",
        ],
        "dosage": {
            "adult_po_monthly": "150mg PO mỗi tháng.",
            "adult_iv_quarterly": "3mg IV mỗi 3 tháng.",
            "notes": "PO: uống lúc đói, ít nhất 60 phút trước ăn. Uống với nước lọc (≥200ml). Đứng hoặc ngồi thẳng ít nhất 60 phút sau khi uống. IV: truyền tĩnh mạch trong 15-30 giây.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Kích ứng thực quản (PO).",
            "Đau cơ, đau xương, đau khớp.",
            "Sốt, ớn lạnh, đau cơ sau tiêm IV (phản ứng giống cúm).",
            "Hoại tử xương hàm (ONJ) - hiếm.",
            "Gãy xương đùi không điển hình - hiếm.",
        ],
        "interactions": [
            "Calcium, sắt, antacids: giảm hấp thu (PO) - dùng cách xa ít nhất 60 phút.",
        ],
        "pregnancy": "C: tránh dùng trong thai kỳ.",
        "mechanism_of_action": (
            "Ibandronate là bisphosphonate thế hệ 2, ức chế hủy xương bằng cách gắn vào hydroxyapatite "
            "trong xương và ức chế enzyme farnesyl pyrophosphate synthase (FPPS) trong tế bào hủy xương. "
            "Giảm hoạt động và gây apoptosis của tế bào hủy xương, dẫn đến giảm hủy xương và tăng mật độ xương."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 1-2 năm.",
            "Calci máu, phospho máu trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước điều trị.",
            "Dấu hiệu hoại tử xương hàm.",
            "Dấu hiệu gãy xương đùi không điển hình.",
        ],
        "precautions": [
            "PO: uống lúc đói, ít nhất 60 phút trước ăn. Đứng hoặc ngồi thẳng ít nhất 60 phút sau khi uống.",
            "IV: có thể gây phản ứng giống cúm sau tiêm (sốt, ớn lạnh, đau cơ) - thường tự hết trong 24-48 giờ.",
            "Dùng cách xa calcium, sắt, antacids ít nhất 60 phút (PO).",
            "Nguy cơ hoại tử xương hàm: đánh giá răng miệng trước điều trị.",
        ],
        "pharmacokinetics": {
            "half_life": "Hơn 10 năm (trong xương), ~10-60 giờ (trong máu).",
            "onset": "Giảm markers hủy xương trong 1-3 tháng.",
            "duration": "Tác dụng kéo dài nhiều năm sau khi ngừng.",
            "protein_binding": "~86-99% (gắn với xương).",
            "clearance": "Gắn vào xương, thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Hoại tử xương hàm (ONJ): có thể xảy ra. Đánh giá răng miệng trước điều trị. "
            "Gãy xương đùi không điển hình: tăng nguy cơ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium, Sắt, Antacids (PO)",
                    "mechanism": "Giảm hấp thu ibandronate.",
                    "effect": "Giảm hiệu quả.",
                    "management": "Dùng cách xa ít nhất 60 phút.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ibandronate.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ calci máu.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Hẹp thực quản (PO).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Ibandronate không chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Kích ứng thực quản (PO).", "Hạ calci máu.", "Phản ứng giống cúm (IV)."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Uống sữa hoặc antacid (PO).", "Điều trị hạ calci máu nếu cần.", "Điều trị hỗ trợ phản ứng giống cúm (IV)."],
            "monitoring": "Calci máu, dấu hiệu kích ứng thực quản, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống lúc đói, ít nhất 60 phút trước ăn.",
                "timing": "Uống vào buổi sáng, lúc đói, với nước lọc (≥200ml). Đứng hoặc ngồi thẳng ít nhất 60 phút sau khi uống.",
            },
            "iv": {
                "reconstitution": "Dung dịch tiêm sẵn dùng.",
                "infusion_rate": "Truyền tĩnh mạch trong 15-30 giây.",
                "compatibility": ["Normal saline", "D5W"],
                "incompatibility": [],
                "notes": "Có thể gây phản ứng giống cúm sau tiêm (sốt, ớn lạnh, đau cơ) - thường tự hết trong 24-48 giờ.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Boniva (ibandronate)", "NOF Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "CRITICAL - Esophageal irritation (PO - if not taken correctly - must take on empty stomach, remain upright 60 minutes)",
                "dental": "Black Box Warning - Osteonecrosis of the jaw (ONJ) - rare but serious",
                "skeletal": "Black Box Warning - Atypical femur fractures - rare but serious",
                "metabolic": "Hypocalcemia",
                "systemic": "Flu-like reaction (IV - common, usually self-limiting 24-48 hours)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Dental evaluation before treatment (ONJ risk)",
                "Black Box Warning - Signs of ONJ (jaw pain, swelling, loose teeth, discharge) - CRITICAL",
                "Black Box Warning - Atypical femur fracture signs (thigh, groin pain) - CRITICAL",
                "CRITICAL - Administration technique (PO): empty stomach, ≥200ml water, remain upright 60 minutes",
                "CRITICAL - IV: flu-like reaction (fever, chills, muscle pain - common, usually self-limiting)",
                "Serum calcium, phosphorus (before and during treatment)",
                "Renal function (creatinine, eGFR - contraindicated if CrCl <30 ml/min)",
                "Bone density (DEXA scan) before treatment and after 1-2 years",
                "Calcium, iron, antacids interaction (PO - take at least 60 minutes apart)"
            ],
            "look_alike_sound_alike": ["Ibandronate", "Alendronate", "Risedronate"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Osteonecrosis of the Jaw (ONJ)",
            "FDA Black Box Warning - Atypical Femur Fractures",
            "NOF Guidelines - Osteoporosis Treatment 2024",
            "ASBMR Guidelines - Bisphosphonate Use",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Risedronate": {
        "group": "Endocrinology - Bisphosphonate (Osteoporosis)",
        "vietnamese_name": "Risedronate, Actonel",
        "administration": ["PO"],
        "indications": [
            "Loãng xương sau mãn kinh.",
            "Loãng xương ở nam giới.",
            "Loãng xương do corticosteroid.",
            "Bệnh Paget xương.",
        ],
        "contraindications": [
            "Dị ứng với risedronate.",
            "Hẹp thực quản, rối loạn vận động thực quản.",
            "Không thể đứng hoặc ngồi thẳng ít nhất 30 phút.",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ calci máu.",
        ],
        "dosage": {
            "adult_osteoporosis_daily": "5mg PO mỗi ngày.",
            "adult_osteoporosis_weekly": "35mg PO mỗi tuần (khuyến cáo).",
            "adult_osteoporosis_monthly": "150mg PO mỗi tháng.",
            "adult_paget": "30mg PO mỗi ngày x 2 tháng.",
            "notes": "Uống lúc đói, ít nhất 30 phút trước ăn hoặc uống thuốc khác. Uống với nước lọc (≥200ml). Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Kích ứng thực quản, đau bụng trên, khó nuốt.",
            "Đau cơ, đau xương, đau khớp.",
            "Hoại tử xương hàm (ONJ) - hiếm.",
            "Gãy xương đùi không điển hình - hiếm.",
            "Hạ calci máu, hạ phospho máu.",
        ],
        "interactions": [
            "Calcium, sắt, antacids: giảm hấp thu - dùng cách xa ít nhất 30 phút.",
            "NSAIDs: tăng nguy cơ kích ứng dạ dày.",
        ],
        "pregnancy": "C: tránh dùng trong thai kỳ.",
        "mechanism_of_action": (
            "Risedronate là bisphosphonate thế hệ 2, ức chế hủy xương bằng cách gắn vào hydroxyapatite "
            "trong xương và ức chế enzyme farnesyl pyrophosphate synthase (FPPS) trong tế bào hủy xương. "
            "Giảm hoạt động và gây apoptosis của tế bào hủy xương, dẫn đến giảm hủy xương và tăng mật độ xương."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 1-2 năm.",
            "Calci máu, phospho máu trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước điều trị.",
            "Dấu hiệu kích ứng thực quản.",
            "Dấu hiệu hoại tử xương hàm.",
            "Dấu hiệu gãy xương đùi không điển hình.",
        ],
        "precautions": [
            "Uống lúc đói, ít nhất 30 phút trước ăn hoặc uống thuốc khác.",
            "Uống với nước lọc (≥200ml).",
            "Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống.",
            "Dùng cách xa calcium, sắt, antacids ít nhất 30 phút.",
            "Nguy cơ hoại tử xương hàm: đánh giá răng miệng trước điều trị.",
        ],
        "pharmacokinetics": {
            "half_life": "Hơn 10 năm (trong xương), ~1.5 giờ (trong máu).",
            "onset": "Giảm markers hủy xương trong 1-3 tháng.",
            "duration": "Tác dụng kéo dài nhiều năm sau khi ngừng.",
            "protein_binding": "~24% (gắn với xương).",
            "clearance": "Gắn vào xương, thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Hoại tử xương hàm (ONJ): có thể xảy ra. Đánh giá răng miệng trước điều trị. "
            "Gãy xương đùi không điển hình: tăng nguy cơ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium, Sắt, Antacids",
                    "mechanism": "Giảm hấp thu risedronate.",
                    "effect": "Giảm hiệu quả.",
                    "management": "Dùng cách xa ít nhất 30 phút.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với risedronate.",
                "Hẹp thực quản.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ calci máu.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Tiền sử bệnh dạ dày.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Risedronate không chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Kích ứng thực quản.", "Hạ calci máu."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Uống sữa hoặc antacid.", "Điều trị hạ calci máu nếu cần."],
            "monitoring": "Calci máu, dấu hiệu kích ứng thực quản.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống lúc đói, ít nhất 30 phút trước ăn.",
                "timing": "Uống vào buổi sáng, lúc đói, với nước lọc (≥200ml). Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Actonel (risedronate)", "NOF Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "CRITICAL - Esophageal irritation/ulceration (if not taken correctly - must take on empty stomach, remain upright 30 minutes)",
                "dental": "Black Box Warning - Osteonecrosis of the jaw (ONJ) - rare but serious",
                "skeletal": "Black Box Warning - Atypical femur fractures - rare but serious",
                "metabolic": "Hypocalcemia, hypophosphatemia"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Dental evaluation before treatment (ONJ risk)",
                "Black Box Warning - Signs of ONJ (jaw pain, swelling, loose teeth, discharge) - CRITICAL",
                "Black Box Warning - Atypical femur fracture signs (thigh, groin pain) - CRITICAL",
                "CRITICAL - Administration technique: empty stomach, ≥200ml water, remain upright 30 minutes",
                "Serum calcium, phosphorus (before and during treatment)",
                "Renal function (creatinine, eGFR - contraindicated if CrCl <30 ml/min)",
                "Bone density (DEXA scan) before treatment and after 1-2 years",
                "Calcium, iron, antacids interaction (take at least 30 minutes apart)"
            ],
            "look_alike_sound_alike": ["Risedronate", "Alendronate", "Ibandronate"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Osteonecrosis of the Jaw (ONJ)",
            "FDA Black Box Warning - Atypical Femur Fractures",
            "NOF Guidelines - Osteoporosis Treatment 2024",
            "ASBMR Guidelines - Bisphosphonate Use",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Zoledronic acid": {
        "group": "Endocrinology - Bisphosphonate (Osteoporosis/Cancer)",
        "vietnamese_name": "Zoledronic acid, Reclast, Zometa",
        "administration": ["IV"],
        "indications": [
            "Loãng xương sau mãn kinh (Reclast - 5mg mỗi năm).",
            "Loãng xương ở nam giới (Reclast).",
            "Loãng xương do corticosteroid (Reclast).",
            "Tăng calci máu do ung thư (Zometa - 4mg).",
            "Ung thư di căn xương (Zometa - 4mg mỗi 3-4 tuần).",
            "Đa u tủy xương (Zometa - 4mg mỗi 3-4 tuần).",
        ],
        "contraindications": [
            "Dị ứng với zoledronic acid.",
            "Suy thận nặng (CrCl <35 ml/min cho Reclast, <30 ml/min cho Zometa).",
            "Hạ calci máu.",
        ],
        "dosage": {
            "adult_osteoporosis": "Reclast: 5mg IV mỗi năm, truyền trong ít nhất 15 phút.",
            "adult_hypercalcemia": "Zometa: 4mg IV x 1 lần, truyền trong ít nhất 15 phút.",
            "adult_cancer_bone": "Zometa: 4mg IV mỗi 3-4 tuần, truyền trong ít nhất 15 phút.",
            "notes": "Truyền tĩnh mạch trong ít nhất 15 phút. Đảm bảo đủ dịch trước và sau truyền. Theo dõi chức năng thận.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều hoặc kéo dài thời gian truyền.",
            "under_30": "Không dùng nếu CrCl <35 ml/min (Reclast) hoặc <30 ml/min (Zometa).",
        },
        "side_effects": [
            "Sốt, ớn lạnh, đau cơ, đau khớp sau tiêm (phản ứng giống cúm) - phổ biến, thường tự hết trong 24-48 giờ.",
            "Đau đầu, mệt mỏi.",
            "Hoại tử xương hàm (ONJ) - đặc biệt ở bệnh nhân ung thư, phẫu thuật răng.",
            "Suy thận cấp - đặc biệt nếu truyền quá nhanh hoặc không đủ dịch.",
            "Rối loạn nhịp tim (AF) - hiếm.",
            "Gãy xương đùi không điển hình - hiếm.",
            "Hạ calci máu, hạ phospho máu, hạ magie máu.",
        ],
        "interactions": [
            "Aminoglycosides: tăng nguy cơ hạ calci máu.",
            "Thalidomide: tăng nguy cơ suy thận.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ.",
        "mechanism_of_action": (
            "Zoledronic acid là bisphosphonate thế hệ 3, mạnh nhất, ức chế hủy xương bằng cách gắn vào hydroxyapatite "
            "trong xương và ức chế enzyme farnesyl pyrophosphate synthase (FPPS) trong tế bào hủy xương. "
            "Giảm hoạt động và gây apoptosis của tế bào hủy xương, dẫn đến giảm hủy xương và tăng mật độ xương. "
            "Ở bệnh nhân ung thư, zoledronic acid cũng có tác dụng chống ung thư và giảm đau xương."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 1-2 năm (Reclast).",
            "Calci máu, phospho máu, magie máu trước và sau truyền.",
            "Creatinine, eGFR (CrCl) trước mỗi lần truyền - QUAN TRỌNG.",
            "Dấu hiệu hoại tử xương hàm (đau hàm, sưng, răng lung lay).",
            "Dấu hiệu suy thận cấp (giảm lượng nước tiểu, tăng creatinine).",
            "Dấu hiệu gãy xương đùi không điển hình.",
            "ECG nếu có triệu chứng tim mạch (rối loạn nhịp tim).",
        ],
        "precautions": [
            "QUAN TRỌNG: Truyền tĩnh mạch trong ít nhất 15 phút (không được truyền nhanh hơn).",
            "Đảm bảo đủ dịch trước và sau truyền để tránh suy thận cấp.",
            "Theo dõi chức năng thận trước mỗi lần truyền - ngừng nếu CrCl giảm.",
            "Nguy cơ hoại tử xương hàm: đánh giá răng miệng trước điều trị, tránh phẫu thuật răng trong khi dùng.",
            "Phản ứng giống cúm sau tiêm (sốt, ớn lạnh, đau cơ) - phổ biến, có thể dùng acetaminophen để giảm triệu chứng.",
            "Không dùng nếu CrCl <35 ml/min (Reclast) hoặc <30 ml/min (Zometa).",
            "Bổ sung calcium và vitamin D trước và trong điều trị.",
        ],
        "pharmacokinetics": {
            "half_life": "Hơn 10 năm (trong xương), ~146 giờ (trong máu).",
            "onset": "Giảm markers hủy xương trong vài ngày đến 1 tuần.",
            "duration": "Tác dụng kéo dài nhiều năm sau khi ngừng (do gắn vào xương).",
            "protein_binding": "~22% (gắn với xương).",
            "clearance": "Gắn vào xương, thải qua thận (không chuyển hóa).",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C) trước khi pha; sau khi pha có thể bảo quản ở nhiệt độ phòng tối đa 24 giờ.",
        "black_box_warnings": (
            "Suy thận cấp: có thể xảy ra, đặc biệt nếu truyền quá nhanh hoặc không đủ dịch. "
            "Theo dõi chức năng thận trước mỗi lần truyền. Hoại tử xương hàm (ONJ): "
            "có thể xảy ra, đặc biệt ở bệnh nhân ung thư, phẫu thuật răng. "
            "Gãy xương đùi không điển hình: tăng nguy cơ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin)",
                    "mechanism": "Cả hai đều có thể gây hạ calci máu và suy thận.",
                    "effect": "Tăng nguy cơ hạ calci máu, suy thận cấp.",
                    "management": "Thận trọng. Theo dõi calci máu và chức năng thận chặt chẽ.",
                },
            ],
            "moderate": [
                {
                    "drug": "Thalidomide",
                    "mechanism": "Cả hai đều có thể gây suy thận.",
                    "effect": "Tăng nguy cơ suy thận cấp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với zoledronic acid.",
                "Suy thận nặng (CrCl <35 ml/min cho Reclast, <30 ml/min cho Zometa).",
                "Hạ calci máu.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, cân nhắc giảm liều hoặc kéo dài thời gian truyền.",
                "Phẫu thuật răng gần đây hoặc dự kiến - tăng nguy cơ ONJ.",
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp tim.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Có thể gây hại cho thai nhi.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều (không chuyển hóa qua gan).",
            "notes": "Zoledronic acid không chuyển hóa qua gan, thải qua thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ calci máu nặng.",
                "Suy thận cấp.",
                "Phản ứng giống cúm nặng.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ calci máu: calcium IV.",
                "Điều trị suy thận cấp: bù dịch, theo dõi chức năng thận.",
                "Điều trị hỗ trợ phản ứng giống cúm: acetaminophen, NSAIDs.",
            ],
            "monitoring": "Calci máu, phospho máu, magie máu, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với 100ml normal saline hoặc D5W.",
                "infusion_rate": "Truyền tĩnh mạch trong ít nhất 15 phút (KHÔNG được truyền nhanh hơn).",
                "compatibility": ["Normal saline", "D5W"],
                "incompatibility": ["Calcium-containing solutions"],
                "notes": "QUAN TRỌNG: Truyền trong ít nhất 15 phút. Đảm bảo đủ dịch trước và sau truyền. Có thể gây phản ứng giống cúm sau tiêm.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Reclast (zoledronic acid), Zometa (zoledronic acid)",
                "HORIZON-PFT Study - Zoledronic acid for osteoporosis",
                "NOF Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCTs (HORIZON-PFT)",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "dental": "Black Box Warning - Osteonecrosis of the jaw (ONJ) - especially in cancer patients, dental procedures",
                "skeletal": "Black Box Warning - Atypical femur fractures - rare but serious",
                "renal": "CRITICAL - Acute kidney injury (especially if infused too fast or inadequate hydration)",
                "metabolic": "Hypocalcemia, hypophosphatemia, hypomagnesemia",
                "cardiovascular": "Atrial fibrillation (rare)",
                "systemic": "Flu-like reaction (common, usually self-limiting 24-48 hours)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": [
                "Black Box Warning - Dental evaluation before treatment (ONJ risk) - CRITICAL",
                "Black Box Warning - Signs of ONJ (jaw pain, swelling, loose teeth, discharge) - CRITICAL",
                "Black Box Warning - Atypical femur fracture signs (thigh, groin pain) - CRITICAL",
                "CRITICAL - Renal function (creatinine, eGFR) before and after infusion - contraindicated if CrCl <35 ml/min (Reclast) or <30 ml/min (Zometa)",
                "CRITICAL - Infusion rate: at least 15 minutes (NOT faster) - CRITICAL to prevent acute kidney injury",
                "CRITICAL - Adequate hydration before and after infusion - CRITICAL to prevent acute kidney injury",
                "Serum calcium, phosphorus, magnesium (before and during treatment)",
                "ECG (atrial fibrillation risk)",
                "Flu-like reaction monitoring (fever, chills, muscle pain - common, usually self-limiting)"
            ],
            "look_alike_sound_alike": ["Zoledronic acid", "Zoledronate", "Zometa", "Reclast"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Osteonecrosis of the Jaw (ONJ)",
            "FDA Black Box Warning - Atypical Femur Fractures",
            "FDA Black Box Warning - Acute Kidney Injury",
            "NOF Guidelines - Osteoporosis Treatment 2024",
            "ASBMR Guidelines - Bisphosphonate Use",
            "ASCO Guidelines - Cancer Bone Metastases",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
}

__all__ = ["BISPHOSPHONATES_DRUGS"]

