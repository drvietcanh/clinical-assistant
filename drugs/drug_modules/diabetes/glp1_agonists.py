"""
GLP-1 Receptor Agonists (Glucagon-like Peptide-1 Receptor Agonists)
Thuốc đái tháo đường và giảm cân mới nhất - Thế hệ sau insulin
Semaglutide, Liraglutide, Dulaglutide, Exenatide
"""

GLP1_AGONISTS_DRUGS = {
    "Semaglutide": {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Semaglutide, Ozempic, Wegovy, Rybelsus",
        "administration": ["SC", "PO"],
        "indications": [
            "Đái tháo đường type 2 (SC: Ozempic, PO: Rybelsus).",
            "Giảm cân ở bệnh nhân béo phì (Wegovy - SC).",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch.",
        ],
        "contraindications": [
            "Dị ứng với semaglutide hoặc tá dược.",
            "Tiền sử hoặc nguy cơ cao ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
            "Đái tháo đường type 1.",
            "Nhiễm toan ceton do đái tháo đường.",
        ],
        "dosage": {
            "sc_dm_initial": "0.25mg SC mỗi tuần x 4 tuần.",
            "sc_dm_maintenance": "0.5mg SC mỗi tuần; có thể tăng lên 1mg hoặc 2mg mỗi tuần nếu cần.",
            "sc_weight_loss": "Wegovy: 0.25mg SC mỗi tuần, tăng dần đến 2.4mg mỗi tuần.",
            "po_dm": "Rybelsus: 3mg PO mỗi ngày x 30 ngày, sau đó tăng lên 7mg hoặc 14mg mỗi ngày.",
            "notes": "SC: tiêm dưới da bụng, đùi hoặc cánh tay, bất kỳ ngày nào trong tuần. PO: uống lúc đói, ít nhất 30 phút trước ăn, chỉ với nước (không quá 120ml).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; thận trọng ở suy thận nặng.",
            "under_30": "Thận trọng, dữ liệu hạn chế; cân nhắc giảm liều hoặc tránh.",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (thường giảm sau vài tuần).",
            "Giảm cảm giác thèm ăn, giảm cân.",
            "Viêm tụy (hiếm nhưng nghiêm trọng).",
            "Bệnh lý túi mật (sỏi mật, viêm túi mật).",
            "Tăng nhịp tim.",
            "Suy thận cấp (hiếm, thường do mất nước).",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết (cần giảm liều).",
            "Thuốc chậm làm rỗng dạ dày: có thể làm chậm hấp thu thuốc khác.",
            "Warfarin: có thể tăng INR (theo dõi).",
        ],
        "pregnancy": "C: thận trọng, chỉ dùng khi lợi ích vượt trội nguy cơ.",
        "mechanism_of_action": (
            "Semaglutide là chất chủ vận thụ thể GLP-1 (glucagon-like peptide-1) tổng hợp, "
            "bắt chước tác dụng của GLP-1 nội sinh. GLP-1 được giải phóng từ tế bào L ở ruột non "
            "khi có thức ăn, kích thích giải phóng insulin phụ thuộc glucose, ức chế giải phóng glucagon, "
            "làm chậm làm rỗng dạ dày, và tăng cảm giác no. Semaglutide có thời gian bán thải dài (~1 tuần) "
            "nhờ gắn với albumin, cho phép tiêm 1 lần/tuần (SC) hoặc uống 1 lần/ngày (PO). "
            "Ngoài giảm đường huyết, semaglutide có lợi ích tim mạch và giảm cân đáng kể."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) để đánh giá hiệu quả.",
            "Cân nặng, BMI.",
            "Dấu hiệu viêm tụy (đau bụng trên, buồn nôn, nôn).",
            "Dấu hiệu bệnh lý túi mật (đau bụng trên bên phải).",
            "Nhịp tim, ECG nếu có triệu chứng tim mạch.",
            "Chức năng thận (creatinine, eGFR) nếu có triệu chứng mất nước.",
            "Dấu hiệu hạ đường huyết khi dùng với insulin/sulfonylurea.",
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 hoặc nhiễm toan ceton.",
            "Nguy cơ viêm tụy: ngừng ngay nếu có đau bụng trên nghiêm trọng.",
            "Nguy cơ bệnh lý túi mật: theo dõi triệu chứng đau bụng trên bên phải.",
            "Giảm liều insulin/sulfonylurea khi bắt đầu semaglutide để tránh hạ đường huyết.",
            "PO (Rybelsus): PHẢI uống lúc đói, ít nhất 30 phút trước ăn, chỉ với nước (≤120ml).",
            "SC: luân phiên vị trí tiêm (bụng, đùi, cánh tay).",
            "Bắt đầu liều thấp và tăng dần để giảm tác dụng phụ tiêu hóa.",
        ],
        "pharmacokinetics": {
            "half_life": "~1 tuần (SC), ~1 tuần (PO).",
            "onset": "Giảm đường huyết trong vài ngày đến 1 tuần.",
            "duration": "SC: 1 tuần; PO: 24 giờ (nhưng tác dụng kéo dài do half-life dài).",
            "protein_binding": ">99% (gắn với albumin).",
            "clearance": "Chuyển hóa qua protease và thải qua thận.",
        },
        "storage": "SC: Bảo quản trong tủ lạnh (2-8°C) trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng (≤30°C) tối đa 56 ngày. PO: Bảo quản ở nhiệt độ phòng (≤30°C), tránh ẩm.",
        "black_box_warnings": (
            "Nguy cơ ung thư tuyến giáp thể tủy (MTC) ở động vật thí nghiệm. "
            "Không dùng ở bệnh nhân có tiền sử MTC hoặc MEN-2. "
            "Nguy cơ viêm tụy cấp (có thể tử vong)."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea (glibenclamide, gliclazide)",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết.",
                    "management": "Giảm liều insulin/sulfonylurea khi bắt đầu semaglutide. Theo dõi đường huyết chặt chẽ.",
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc chậm làm rỗng dạ dày (atropine, opioid)",
                    "mechanism": "Semaglutide làm chậm làm rỗng dạ dày, có thể làm chậm hấp thu thuốc khác.",
                    "effect": "Giảm hấp thu thuốc khác, giảm hiệu quả.",
                    "management": "Thận trọng với thuốc có cửa sổ hẹp. Có thể cần điều chỉnh thời gian dùng.",
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Semaglutide có thể ảnh hưởng đến đông máu.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu.",
                    "management": "Theo dõi INR thường xuyên khi bắt đầu semaglutide.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với semaglutide hoặc tá dược.",
                "Tiền sử ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
                "Đái tháo đường type 1.",
                "Nhiễm toan ceton do đái tháo đường.",
            ],
            "tương_đối": [
                "Tiền sử viêm tụy.",
                "Tiền sử bệnh lý túi mật.",
                "Suy thận nặng (eGFR <30) - thận trọng.",
                "Suy tim nặng - thận trọng.",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ tiêu hóa.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Dữ liệu hạn chế ở người. Chỉ dùng khi lợi ích vượt trội nguy cơ. "
                "Có thể gây hạ đường huyết ở thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Thận trọng, dữ liệu hạn chế.",
            "notes": "Semaglutide chuyển hóa qua protease, không phụ thuộc gan đáng kể.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng.",
                "Hạ đường huyết (nếu dùng với insulin/sulfonylurea).",
                "Đau bụng, viêm tụy.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ: bù dịch nếu mất nước.",
                "Điều trị hạ đường huyết: glucose IV nếu cần.",
                "Theo dõi viêm tụy: ngừng thuốc, điều trị hỗ trợ.",
            ],
            "monitoring": "Đường huyết, điện giải, dấu hiệu viêm tụy, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dung dịch tiêm sẵn dùng trong bút tiêm.",
                "injection_site": "Tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
                "timing": "Tiêm 1 lần/tuần, bất kỳ ngày nào trong tuần, cùng giờ mỗi tuần.",
                "notes": "Bảo quản trong tủ lạnh trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng ≤30°C tối đa 56 ngày.",
            },
            "oral": {
                "with_food": "PHẢI uống lúc đói, ít nhất 30 phút trước ăn.",
                "timing": "Uống 1 lần/ngày, chỉ với nước (không quá 120ml), không uống với thức ăn hoặc thuốc khác.",
                "notes": "QUAN TRỌNG: Uống lúc đói, ít nhất 30 phút trước ăn, chỉ với nước. Không uống với thức ăn hoặc thuốc khác sẽ giảm hấp thu.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ozempic (semaglutide SC), Wegovy (semaglutide SC), Rybelsus (semaglutide PO)",
                "SUSTAIN trials - Semaglutide cardiovascular outcomes",
                "STEP trials - Semaglutide for weight loss",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, multiple large RCTs",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Pancreatitis (rare but serious)", "Thyroid C-cell tumors (MTC risk in animals)", "Acute kidney injury (rare, usually due to dehydration)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Signs of pancreatitis", "Thyroid function (if symptoms)", "Renal function (if dehydration)", "Weight", "Heart rate"]
        },
        "guideline_tags": [
            "ADA/EASD Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "SUSTAIN Trials",
            "STEP Trials",
            "FDA Black Box Warning - Thyroid C-cell tumors"
        ],
    },

    "Liraglutide": {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Liraglutide, Victoza, Saxenda",
        "administration": ["SC"],
        "indications": [
            "Đái tháo đường type 2 (Victoza).",
            "Giảm cân ở bệnh nhân béo phì (Saxenda - liều cao hơn).",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch.",
        ],
        "contraindications": [
            "Dị ứng với liraglutide hoặc tá dược.",
            "Tiền sử hoặc nguy cơ cao ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
            "Đái tháo đường type 1.",
            "Nhiễm toan ceton do đái tháo đường.",
        ],
        "dosage": {
            "sc_dm_initial": "0.6mg SC mỗi ngày x 1 tuần.",
            "sc_dm_maintenance": "1.2mg SC mỗi ngày; có thể tăng lên 1.8mg mỗi ngày nếu cần.",
            "sc_weight_loss": "Saxenda: 0.6mg SC mỗi ngày, tăng dần đến 3mg mỗi ngày.",
            "notes": "Tiêm dưới da bụng, đùi hoặc cánh tay, bất kỳ thời điểm nào trong ngày.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; thận trọng ở suy thận nặng.",
            "under_30": "Thận trọng, dữ liệu hạn chế; cân nhắc giảm liều hoặc tránh.",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (thường giảm sau vài tuần).",
            "Giảm cảm giác thèm ăn, giảm cân.",
            "Viêm tụy (hiếm nhưng nghiêm trọng).",
            "Bệnh lý túi mật (sỏi mật, viêm túi mật).",
            "Tăng nhịp tim.",
            "Suy thận cấp (hiếm, thường do mất nước).",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết (cần giảm liều).",
            "Thuốc chậm làm rỗng dạ dày: có thể làm chậm hấp thu thuốc khác.",
        ],
        "pregnancy": "C: thận trọng, chỉ dùng khi lợi ích vượt trội nguy cơ.",
        "mechanism_of_action": (
            "Liraglutide là chất chủ vận thụ thể GLP-1 tổng hợp, bắt chước tác dụng của GLP-1 nội sinh. "
            "Kích thích giải phóng insulin phụ thuộc glucose, ức chế giải phóng glucagon, "
            "làm chậm làm rỗng dạ dày, và tăng cảm giác no. Liraglutide có thời gian bán thải ~13 giờ "
            "nhờ gắn với albumin, cho phép tiêm 1 lần/ngày. "
            "Có lợi ích tim mạch và giảm cân."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) để đánh giá hiệu quả.",
            "Cân nặng, BMI.",
            "Dấu hiệu viêm tụy (đau bụng trên, buồn nôn, nôn).",
            "Dấu hiệu bệnh lý túi mật (đau bụng trên bên phải).",
            "Nhịp tim, ECG nếu có triệu chứng tim mạch.",
            "Chức năng thận (creatinine, eGFR) nếu có triệu chứng mất nước.",
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 hoặc nhiễm toan ceton.",
            "Nguy cơ viêm tụy: ngừng ngay nếu có đau bụng trên nghiêm trọng.",
            "Nguy cơ bệnh lý túi mật: theo dõi triệu chứng đau bụng trên bên phải.",
            "Giảm liều insulin/sulfonylurea khi bắt đầu liraglutide.",
            "SC: luân phiên vị trí tiêm (bụng, đùi, cánh tay).",
            "Bắt đầu liều thấp và tăng dần để giảm tác dụng phụ tiêu hóa.",
        ],
        "pharmacokinetics": {
            "half_life": "~13 giờ.",
            "onset": "Giảm đường huyết trong vài ngày.",
            "duration": "24 giờ (tiêm 1 lần/ngày).",
            "protein_binding": ">98% (gắn với albumin).",
            "clearance": "Chuyển hóa qua protease và thải qua thận.",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C) trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng (≤30°C) tối đa 30 ngày.",
        "black_box_warnings": (
            "Nguy cơ ung thư tuyến giáp thể tủy (MTC) ở động vật thí nghiệm. "
            "Không dùng ở bệnh nhân có tiền sử MTC hoặc MEN-2. "
            "Nguy cơ viêm tụy cấp (có thể tử vong)."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết.",
                    "management": "Giảm liều insulin/sulfonylurea khi bắt đầu liraglutide. Theo dõi đường huyết chặt chẽ.",
                }
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với liraglutide.",
                "Tiền sử ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
                "Đái tháo đường type 1.",
                "Nhiễm toan ceton do đái tháo đường.",
            ],
            "tương_đối": [
                "Tiền sử viêm tụy.",
                "Tiền sử bệnh lý túi mật.",
                "Suy thận nặng (eGFR <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Thận trọng, dữ liệu hạn chế.",
            "notes": "Liraglutide chuyển hóa qua protease, không phụ thuộc gan đáng kể.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, nôn nặng.", "Hạ đường huyết.", "Đau bụng, viêm tụy."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hỗ trợ: bù dịch.", "Điều trị hạ đường huyết: glucose IV nếu cần."],
            "monitoring": "Đường huyết, điện giải, dấu hiệu viêm tụy.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dung dịch tiêm sẵn dùng trong bút tiêm.",
                "injection_site": "Tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
                "timing": "Tiêm 1 lần/ngày, bất kỳ thời điểm nào trong ngày, cùng giờ mỗi ngày.",
                "notes": "Bảo quản trong tủ lạnh trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng ≤30°C tối đa 30 ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Victoza (liraglutide), Saxenda (liraglutide)",
                "LEADER trial - Liraglutide cardiovascular outcomes",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCT (LEADER)",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Pancreatitis (rare but serious)", "Thyroid C-cell tumors (MTC risk in animals)", "Acute kidney injury (rare, usually due to dehydration)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Signs of pancreatitis", "Thyroid function (if symptoms)", "Renal function (if dehydration)", "Weight", "Heart rate"]
        },
        "guideline_tags": [
            "ADA/EASD Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "LEADER Trial",
            "FDA Black Box Warning - Thyroid C-cell tumors"
        ],
    },

    "Dulaglutide": {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Dulaglutide, Trulicity",
        "administration": ["SC"],
        "indications": [
            "Đái tháo đường type 2.",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch.",
        ],
        "contraindications": [
            "Dị ứng với dulaglutide hoặc tá dược.",
            "Tiền sử hoặc nguy cơ cao ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
            "Đái tháo đường type 1.",
            "Nhiễm toan ceton do đái tháo đường.",
        ],
        "dosage": {
            "sc_initial": "0.75mg SC mỗi tuần.",
            "sc_maintenance": "1.5mg SC mỗi tuần; có thể tăng lên 3mg hoặc 4.5mg mỗi tuần nếu cần.",
            "notes": "Tiêm dưới da bụng, đùi hoặc cánh tay, bất kỳ ngày nào trong tuần.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; thận trọng ở suy thận nặng.",
            "under_30": "Thận trọng, dữ liệu hạn chế; cân nhắc giảm liều hoặc tránh.",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (thường giảm sau vài tuần).",
            "Giảm cảm giác thèm ăn, giảm cân.",
            "Viêm tụy (hiếm nhưng nghiêm trọng).",
            "Bệnh lý túi mật (sỏi mật, viêm túi mật).",
            "Tăng nhịp tim.",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết (cần giảm liều).",
        ],
        "pregnancy": "C: thận trọng, chỉ dùng khi lợi ích vượt trội nguy cơ.",
        "mechanism_of_action": (
            "Dulaglutide là chất chủ vận thụ thể GLP-1 tổng hợp, bắt chước tác dụng của GLP-1 nội sinh. "
            "Kích thích giải phóng insulin phụ thuộc glucose, ức chế giải phóng glucagon, "
            "làm chậm làm rỗng dạ dày, và tăng cảm giác no. Dulaglutide có thời gian bán thải ~5 ngày "
            "nhờ cấu trúc Fc fusion, cho phép tiêm 1 lần/tuần. "
            "Có lợi ích tim mạch."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) để đánh giá hiệu quả.",
            "Cân nặng, BMI.",
            "Dấu hiệu viêm tụy (đau bụng trên, buồn nôn, nôn).",
            "Dấu hiệu bệnh lý túi mật (đau bụng trên bên phải).",
            "Nhịp tim, ECG nếu có triệu chứng tim mạch.",
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 hoặc nhiễm toan ceton.",
            "Nguy cơ viêm tụy: ngừng ngay nếu có đau bụng trên nghiêm trọng.",
            "Nguy cơ bệnh lý túi mật: theo dõi triệu chứng đau bụng trên bên phải.",
            "Giảm liều insulin/sulfonylurea khi bắt đầu dulaglutide.",
            "SC: luân phiên vị trí tiêm (bụng, đùi, cánh tay).",
            "Bắt đầu liều thấp và tăng dần để giảm tác dụng phụ tiêu hóa.",
        ],
        "pharmacokinetics": {
            "half_life": "~5 ngày.",
            "onset": "Giảm đường huyết trong vài ngày đến 1 tuần.",
            "duration": "1 tuần (tiêm 1 lần/tuần).",
            "protein_binding": "N/A (Fc fusion protein).",
            "clearance": "Chuyển hóa qua protease và thải qua thận.",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C) trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng (≤30°C) tối đa 14 ngày.",
        "black_box_warnings": (
            "Nguy cơ ung thư tuyến giáp thể tủy (MTC) ở động vật thí nghiệm. "
            "Không dùng ở bệnh nhân có tiền sử MTC hoặc MEN-2. "
            "Nguy cơ viêm tụy cấp (có thể tử vong)."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết.",
                    "management": "Giảm liều insulin/sulfonylurea khi bắt đầu dulaglutide. Theo dõi đường huyết chặt chẽ.",
                }
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với dulaglutide.",
                "Tiền sử ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
                "Đái tháo đường type 1.",
                "Nhiễm toan ceton do đái tháo đường.",
            ],
            "tương_đối": [
                "Tiền sử viêm tụy.",
                "Tiền sử bệnh lý túi mật.",
                "Suy thận nặng (eGFR <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Thận trọng, dữ liệu hạn chế.",
            "notes": "Dulaglutide chuyển hóa qua protease, không phụ thuộc gan đáng kể.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, nôn nặng.", "Hạ đường huyết.", "Đau bụng, viêm tụy."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hỗ trợ: bù dịch.", "Điều trị hạ đường huyết: glucose IV nếu cần."],
            "monitoring": "Đường huyết, điện giải, dấu hiệu viêm tụy.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dung dịch tiêm sẵn dùng trong bút tiêm.",
                "injection_site": "Tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
                "timing": "Tiêm 1 lần/tuần, bất kỳ ngày nào trong tuần, cùng giờ mỗi tuần.",
                "notes": "Bảo quản trong tủ lạnh trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng ≤30°C tối đa 14 ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Trulicity (dulaglutide)",
                "REWIND trial - Dulaglutide cardiovascular outcomes",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCT (REWIND)",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Pancreatitis (rare but serious)", "Thyroid C-cell tumors (MTC risk in animals)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Signs of pancreatitis", "Thyroid function (if symptoms)", "Weight", "Heart rate"]
        },
        "guideline_tags": [
            "ADA/EASD Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "REWIND Trial",
            "FDA Black Box Warning - Thyroid C-cell tumors"
        ],
    },

    "Exenatide": {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Exenatide, Byetta, Bydureon",
        "administration": ["SC"],
        "indications": [
            "Đái tháo đường type 2 (Byetta: 2 lần/ngày, Bydureon: 1 lần/tuần).",
        ],
        "contraindications": [
            "Dị ứng với exenatide hoặc tá dược.",
            "Tiền sử hoặc nguy cơ cao ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
            "Đái tháo đường type 1.",
            "Nhiễm toan ceton do đái tháo đường.",
            "Suy thận nặng (eGFR <30) - chống chỉ định.",
        ],
        "dosage": {
            "sc_twice_daily": "Byetta: 5mcg SC x 2 lần/ngày trong 1 tháng, sau đó tăng lên 10mcg x 2 lần/ngày.",
            "sc_once_weekly": "Bydureon: 2mg SC mỗi tuần.",
            "notes": "Byetta: tiêm trong vòng 60 phút trước bữa sáng và tối. Bydureon: tiêm bất kỳ ngày nào trong tuần.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "CHỐNG CHỈ ĐỊNH - không dùng nếu eGFR <30.",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (thường giảm sau vài tuần).",
            "Giảm cảm giác thèm ăn, giảm cân.",
            "Viêm tụy (hiếm nhưng nghiêm trọng).",
            "Bệnh lý túi mật (sỏi mật, viêm túi mật).",
            "Suy thận cấp (hiếm, thường do mất nước).",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết (cần giảm liều).",
            "Thuốc chậm làm rỗng dạ dày: có thể làm chậm hấp thu thuốc khác.",
        ],
        "pregnancy": "C: thận trọng, chỉ dùng khi lợi ích vượt trội nguy cơ.",
        "mechanism_of_action": (
            "Exenatide là chất chủ vận thụ thể GLP-1 tổng hợp (từ nọc bọ cạp Gila), "
            "bắt chước tác dụng của GLP-1 nội sinh. Kích thích giải phóng insulin phụ thuộc glucose, "
            "ức chế giải phóng glucagon, làm chậm làm rỗng dạ dày, và tăng cảm giác no. "
            "Byetta có thời gian bán thải ~2.4 giờ (tiêm 2 lần/ngày). "
            "Bydureon là dạng extended-release với thời gian bán thải ~2 tuần (tiêm 1 lần/tuần)."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) để đánh giá hiệu quả.",
            "Cân nặng, BMI.",
            "Dấu hiệu viêm tụy (đau bụng trên, buồn nôn, nôn).",
            "Dấu hiệu bệnh lý túi mật (đau bụng trên bên phải).",
            "Chức năng thận (creatinine, eGFR) - đặc biệt quan trọng với exenatide.",
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 hoặc nhiễm toan ceton.",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (eGFR <30).",
            "Nguy cơ viêm tụy: ngừng ngay nếu có đau bụng trên nghiêm trọng.",
            "Nguy cơ bệnh lý túi mật: theo dõi triệu chứng đau bụng trên bên phải.",
            "Giảm liều insulin/sulfonylurea khi bắt đầu exenatide.",
            "SC: luân phiên vị trí tiêm (bụng, đùi, cánh tay).",
            "Bắt đầu liều thấp và tăng dần để giảm tác dụng phụ tiêu hóa.",
        ],
        "pharmacokinetics": {
            "half_life": "Byetta: ~2.4 giờ; Bydureon: ~2 tuần.",
            "onset": "Giảm đường huyết trong vài ngày.",
            "duration": "Byetta: 12 giờ (tiêm 2 lần/ngày); Bydureon: 1 tuần (tiêm 1 lần/tuần).",
            "protein_binding": "N/A.",
            "clearance": "Thải qua thận (chủ yếu).",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C) trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng (≤25°C) tối đa 30 ngày.",
        "black_box_warnings": (
            "Nguy cơ ung thư tuyến giáp thể tủy (MTC) ở động vật thí nghiệm. "
            "Không dùng ở bệnh nhân có tiền sử MTC hoặc MEN-2. "
            "Nguy cơ viêm tụy cấp (có thể tử vong). "
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (eGFR <30)."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết.",
                    "management": "Giảm liều insulin/sulfonylurea khi bắt đầu exenatide. Theo dõi đường huyết chặt chẽ.",
                }
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với exenatide.",
                "Tiền sử ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
                "Đái tháo đường type 1.",
                "Nhiễm toan ceton do đái tháo đường.",
                "Suy thận nặng (eGFR <30) - CHỐNG CHỈ ĐỊNH.",
            ],
            "tương_đối": [
                "Tiền sử viêm tụy.",
                "Tiền sử bệnh lý túi mật.",
                "Suy thận trung bình (eGFR 30-60) - thận trọng, cân nhắc giảm liều.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Thận trọng, dữ liệu hạn chế.",
            "notes": "Exenatide thải qua thận, không phụ thuộc gan đáng kể.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, nôn nặng.", "Hạ đường huyết.", "Đau bụng, viêm tụy."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hỗ trợ: bù dịch.", "Điều trị hạ đường huyết: glucose IV nếu cần."],
            "monitoring": "Đường huyết, điện giải, dấu hiệu viêm tụy, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dung dịch tiêm sẵn dùng trong bút tiêm (Byetta) hoặc bột pha (Bydureon).",
                "injection_site": "Tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
                "timing": "Byetta: tiêm trong vòng 60 phút trước bữa sáng và tối. Bydureon: tiêm 1 lần/tuần, bất kỳ ngày nào trong tuần.",
                "notes": "Bảo quản trong tủ lạnh trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng ≤25°C tối đa 30 ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Byetta (exenatide), Bydureon (exenatide extended-release)",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Pancreatitis (rare but serious)", "Thyroid C-cell tumors (MTC risk in animals)", "Acute kidney injury (contraindicated if eGFR <30)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Blood glucose", "Renal function (CrCl, eGFR) - CRITICAL", "Signs of pancreatitis", "Thyroid function (if symptoms)", "Weight"]
        },
        "guideline_tags": [
            "ADA/EASD Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "FDA Black Box Warning - Thyroid C-cell tumors and Renal Impairment"
        ],
    },

    "Tirzepatide": {
        "group": "Diabetes - GIP/GLP-1 Dual Agonist",
        "vietnamese_name": "Tirzepatide, Mounjaro, Zepbound",
        "administration": ["SC"],
        "indications": [
            "Đái tháo đường type 2 (Mounjaro).",
            "Giảm cân ở bệnh nhân béo phì (Zepbound - liều cao hơn).",
        ],
        "contraindications": [
            "Dị ứng với tirzepatide hoặc tá dược.",
            "Tiền sử hoặc nguy cơ cao ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
            "Đái tháo đường type 1.",
            "Nhiễm toan ceton do đái tháo đường.",
        ],
        "dosage": {
            "sc_dm_initial": "2.5mg SC mỗi tuần x 4 tuần.",
            "sc_dm_maintenance": "5mg SC mỗi tuần; có thể tăng lên 7.5mg, 10mg, hoặc 15mg mỗi tuần nếu cần.",
            "sc_weight_loss": "Zepbound: 2.5mg SC mỗi tuần x 4 tuần, sau đó tăng dần đến 5mg, 7.5mg, 10mg, hoặc 12.5mg mỗi tuần.",
            "notes": "SC: tiêm dưới da bụng, đùi hoặc cánh tay, bất kỳ ngày nào trong tuần, cùng giờ mỗi tuần.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; thận trọng ở suy thận nặng.",
            "under_30": "Thận trọng, dữ liệu hạn chế; cân nhắc giảm liều hoặc tránh.",
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy (thường giảm sau vài tuần, có thể nghiêm trọng hơn so với GLP-1 đơn thuần).",
            "Giảm cảm giác thèm ăn, giảm cân (hiệu quả cao hơn GLP-1 đơn thuần).",
            "Viêm tụy (hiếm nhưng nghiêm trọng).",
            "Bệnh lý túi mật (sỏi mật, viêm túi mật).",
            "Tăng nhịp tim.",
            "Suy thận cấp (hiếm, thường do mất nước).",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết (cần giảm liều).",
            "Thuốc chậm làm rỗng dạ dày: có thể làm chậm hấp thu thuốc khác.",
        ],
        "pregnancy": "C: thận trọng, chỉ dùng khi lợi ích vượt trội nguy cơ.",
        "mechanism_of_action": (
            "Tirzepatide là chất chủ vận kép thụ thể GIP (glucose-dependent insulinotropic polypeptide) và GLP-1 "
            "(glucagon-like peptide-1), thuốc đầu tiên trong nhóm này. GIP và GLP-1 đều là incretin hormones "
            "được giải phóng từ ruột khi có thức ăn. Tirzepatide kích thích cả hai thụ thể → tăng giải phóng insulin "
            "phụ thuộc glucose, ức chế giải phóng glucagon, làm chậm làm rỗng dạ dày, và tăng cảm giác no. "
            "Tác dụng kép này cho hiệu quả giảm đường huyết và giảm cân cao hơn so với GLP-1 đơn thuần. "
            "Tirzepatide có thời gian bán thải ~5 ngày nhờ gắn với albumin, cho phép tiêm 1 lần/tuần. "
            "Hiệu quả giảm HbA1c và giảm cân cao nhất trong các thuốc điều trị đái tháo đường hiện tại."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) để đánh giá hiệu quả.",
            "Cân nặng, BMI.",
            "Dấu hiệu viêm tụy (đau bụng trên, buồn nôn, nôn).",
            "Dấu hiệu bệnh lý túi mật (đau bụng trên bên phải).",
            "Nhịp tim, ECG nếu có triệu chứng tim mạch.",
            "Chức năng thận (creatinine, eGFR) nếu có triệu chứng mất nước.",
            "Dấu hiệu hạ đường huyết khi dùng với insulin/sulfonylurea.",
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 hoặc nhiễm toan ceton.",
            "Nguy cơ viêm tụy: ngừng ngay nếu có đau bụng trên nghiêm trọng.",
            "Nguy cơ bệnh lý túi mật: theo dõi triệu chứng đau bụng trên bên phải.",
            "Giảm liều insulin/sulfonylurea khi bắt đầu tirzepatide để tránh hạ đường huyết.",
            "SC: luân phiên vị trí tiêm (bụng, đùi, cánh tay).",
            "Bắt đầu liều thấp và tăng dần để giảm tác dụng phụ tiêu hóa (có thể nghiêm trọng hơn GLP-1 đơn thuần).",
            "Theo dõi chặt chẽ tác dụng phụ tiêu hóa - có thể nghiêm trọng hơn so với GLP-1 đơn thuần.",
        ],
        "pharmacokinetics": {
            "half_life": "~5 ngày.",
            "onset": "Giảm đường huyết trong vài ngày đến 1 tuần.",
            "duration": "1 tuần (tiêm 1 lần/tuần).",
            "protein_binding": ">99% (gắn với albumin).",
            "clearance": "Chuyển hóa qua protease và thải qua thận.",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C) trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng (≤30°C) tối đa 56 ngày.",
        "black_box_warnings": (
            "Nguy cơ ung thư tuyến giáp thể tủy (MTC) ở động vật thí nghiệm. "
            "Không dùng ở bệnh nhân có tiền sử MTC hoặc MEN-2. "
            "Nguy cơ viêm tụy cấp (có thể tử vong)."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea (glibenclamide, gliclazide)",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết.",
                    "management": "Giảm liều insulin/sulfonylurea khi bắt đầu tirzepatide. Theo dõi đường huyết chặt chẽ.",
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc chậm làm rỗng dạ dày (atropine, opioid)",
                    "mechanism": "Tirzepatide làm chậm làm rỗng dạ dày, có thể làm chậm hấp thu thuốc khác.",
                    "effect": "Giảm hấp thu thuốc khác, giảm hiệu quả.",
                    "management": "Thận trọng với thuốc có cửa sổ hẹp. Có thể cần điều chỉnh thời gian dùng.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với tirzepatide hoặc tá dược.",
                "Tiền sử ung thư tuyến giáp thể tủy (MTC) hoặc MEN-2.",
                "Đái tháo đường type 1.",
                "Nhiễm toan ceton do đái tháo đường.",
            ],
            "tương_đối": [
                "Tiền sử viêm tụy.",
                "Tiền sử bệnh lý túi mật.",
                "Suy thận nặng (eGFR <30) - thận trọng.",
                "Suy tim nặng - thận trọng.",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ tiêu hóa.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Dữ liệu hạn chế ở người. Chỉ dùng khi lợi ích vượt trội nguy cơ. "
                "Có thể gây hạ đường huyết ở thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Thận trọng, dữ liệu hạn chế.",
            "notes": "Tirzepatide chuyển hóa qua protease, không phụ thuộc gan đáng kể.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng.",
                "Hạ đường huyết (nếu dùng với insulin/sulfonylurea).",
                "Đau bụng, viêm tụy.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ: bù dịch nếu mất nước.",
                "Điều trị hạ đường huyết: glucose IV nếu cần.",
                "Theo dõi viêm tụy: ngừng thuốc, điều trị hỗ trợ.",
            ],
            "monitoring": "Đường huyết, điện giải, dấu hiệu viêm tụy, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dung dịch tiêm sẵn dùng trong bút tiêm.",
                "injection_site": "Tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
                "timing": "Tiêm 1 lần/tuần, bất kỳ ngày nào trong tuần, cùng giờ mỗi tuần.",
                "notes": "Bảo quản trong tủ lạnh trước khi mở; sau khi mở có thể bảo quản ở nhiệt độ phòng ≤30°C tối đa 56 ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mounjaro (tirzepatide), Zepbound (tirzepatide)",
                "SURPASS trials - Tirzepatide efficacy and safety",
                "SURMOUNT trials - Tirzepatide for weight loss",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved (2022), multiple large RCTs, highest efficacy",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Pancreatitis (rare but serious)", "Thyroid C-cell tumors (MTC risk in animals)", "Acute kidney injury (rare, usually due to dehydration)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Signs of pancreatitis", "Thyroid function (if symptoms)", "Renal function (if dehydration)", "Weight", "Heart rate", "GI symptoms (may be more severe than GLP-1 alone)"]
        },
        "guideline_tags": [
            "ADA/EASD Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "SURPASS Trials",
            "SURMOUNT Trials",
            "FDA Black Box Warning - Thyroid C-cell tumors"
        ],
    },
}

__all__ = ["GLP1_AGONISTS_DRUGS"]

