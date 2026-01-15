"""
Cholesterol Absorption Inhibitors
"""

CHOLESTEROL_ABSORPTION_INHIBITORS = {
    "Bempedoic acid": {
        "group": "Cardiovascular - ATP-Citrate Lyase Inhibitor",
        "vietnamese_name": "Bempedoic acid, Nexletol, Nexlizet (kết hợp với ezetimibe)",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu tiên phát hoặc tăng cholesterol máu gia đình dị hợp tử (heterozygous familial hypercholesterolemia) - đơn trị hoặc kết hợp với statin",
            "Dự phòng biến cố tim mạch ở bệnh nhân không dung nạp statin hoặc cần giảm LDL-C thêm (CLEAR Outcomes study)",
            "Kết hợp với ezetimibe (Nexlizet) để tăng hiệu quả giảm LDL-C - giảm thêm ~38% LDL-C so với placebo",
            "Bệnh nhân có nguy cơ tim mạch cao cần giảm LDL-C nhưng không dung nạp statin hoặc cần giảm LDL-C thêm",
            "Bệnh nhân đã dùng statin nhưng chưa đạt mục tiêu LDL-C"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với bempedoic acid hoặc bất kỳ thành phần nào của thuốc",
                "Bệnh gút đang hoạt động",
                "Tăng acid uric máu không kiểm soát"
            ],
            "tương_đối": [
                "Tiền sử bệnh gút - tăng nguy cơ tái phát, cần điều trị dự phòng",
                "Suy thận nặng (eGFR <30) - thận trọng, dữ liệu hạn chế; không khuyến cáo nếu eGFR <30",
                "Suy gan nặng - thận trọng, dữ liệu hạn chế"
            ]
        },
        "dosage": {
            "adult_monotherapy": "180mg PO x 1 lần/ngày",
            "adult_with_ezetimibe": "Nexlizet: Bempedoic acid 180mg + Ezetimibe 10mg PO x 1 lần/ngày",
            "adult_with_statin": "180mg PO x 1 lần/ngày (có thể dùng cùng hoặc không cùng statin, nhưng giảm liều simvastatin xuống ≤20mg/ngày và pravastatin xuống ≤40mg/ngày)",
            "pediatric": {
                "notes": "Chưa được nghiên cứu ở trẻ em <18 tuổi. Không khuyến cáo sử dụng ở trẻ em."
            },
            "geriatric": {
                "dosing": "180mg PO x 1 lần/ngày (không cần điều chỉnh liều)",
                "notes": "Người cao tuổi (≥65 tuổi) không cần điều chỉnh liều. Dữ liệu an toàn tương tự như người trẻ tuổi."
            },
            "notes": "Uống bất kỳ lúc nào trong ngày, có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu. Có thể dùng cùng hoặc không cùng statin. Khuyến khích uống cùng giờ mỗi ngày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, dữ liệu hạn chế; không khuyến cáo nếu eGFR <30.",
        },
        "side_effects": [
            "Tăng acid uric máu, bệnh gút (phổ biến - ~2-3%) - đặc biệt ở người có tiền sử gút",
            "Tăng men gan (ALT, AST) - thường nhẹ, hiếm khi nghiêm trọng",
            "Đau cơ, đau khớp - ít gặp hơn statin (do chỉ hoạt động ở gan)",
            "Nhiễm trùng đường hô hấp trên (URI) - phổ biến",
            "Đau lưng - phổ biến",
            "Đau bụng, rối loạn tiêu hóa - ít gặp",
            "Tăng CK (creatine kinase) - đặc biệt khi dùng với simvastatin/pravastatin liều cao",
            "Mệt mỏi - ít gặp",
            "Đau đầu - ít gặp"
        ],
        "interactions": [
            "Simvastatin >20mg/ngày: tăng nguy cơ đau cơ, tăng CK, tiêu cơ vân (GIẢM LIỀU SIMVASTATIN XUỐNG ≤20MG/NGÀY)",
            "Pravastatin >40mg/ngày: tăng nguy cơ đau cơ, tăng CK (GIẢM LIỀU PRAVASTATIN XUỐNG ≤40MG/NGÀY)",
            "Ezetimibe: có thể dùng cùng (Nexlizet) - tác dụng cộng dồn giảm LDL-C",
            "Các statin khác (atorvastatin, rosuvastatin, lovastatin): không có tương tác đáng kể, có thể dùng cùng",
            "Warfarin: không có tương tác đáng kể",
            "Allopurinol, febuxostat: có thể dùng để điều trị dự phòng bệnh gút"
        ],
        "pregnancy": "X - Chống chỉ định trong thai kỳ. Bempedoic acid có thể gây hại cho thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả khi dùng bempedoic acid.",
        "mechanism_of_action": (
            "Bempedoic acid là tiền thuốc, được chuyển hóa thành bempedoyl-CoA trong gan, "
            "ức chế ATP-citrate lyase (ACL), enzyme quan trọng trong tổng hợp cholesterol ở gan. "
            "ACL chuyển đổi citrate thành acetyl-CoA, bước đầu tiên trong tổng hợp cholesterol. "
            "Bằng cách ức chế ACL, bempedoic acid giảm tổng hợp cholesterol ở gan, "
            "dẫn đến tăng biểu hiện thụ thể LDL và giảm LDL-C (~18-25% khi dùng đơn trị). "
            "Khác với statin (ức chế HMG-CoA reductase), bempedoic acid chỉ hoạt động ở gan "
            "(do cần chuyển hóa thành dạng hoạt tính), nên ít gây đau cơ hơn statin."
        ),
        "monitoring": [
            "Lipid profile (LDL-C, HDL-C, TG, total cholesterol, non-HDL-C) - kiểm tra trước điều trị, sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "Acid uric máu trước điều trị và trong điều trị (mỗi 3-6 tháng) - nguy cơ tăng acid uric và bệnh gút, đặc biệt ở người có tiền sử gút",
            "Men gan (ALT, AST, bilirubin) - trước điều trị và trong điều trị (mỗi 3-6 tháng). Ngừng nếu ALT/AST >3x ULN",
            "CK (creatine kinase) nếu có đau cơ hoặc yếu cơ - đặc biệt khi dùng với simvastatin/pravastatin",
            "Dấu hiệu bệnh gút (đau khớp, sưng khớp, đỏ da quanh khớp) - đặc biệt ở người có tiền sử gút. Điều trị dự phòng nếu cần",
            "Triệu chứng đau cơ, yếu cơ - theo dõi và đánh giá, đặc biệt khi dùng với simvastatin/pravastatin",
            "Đáp ứng điều trị - đánh giá giảm LDL-C sau 4-8 tuần, điều chỉnh liều hoặc thêm thuốc nếu cần"
        ],
        "precautions": [
            "Tăng acid uric máu và bệnh gút: theo dõi acid uric máu trước và trong điều trị. Điều trị dự phòng với allopurinol hoặc febuxostat nếu có tiền sử gút hoặc acid uric máu cao. Ngừng nếu bệnh gút đang hoạt động.",
            "Tăng men gan: theo dõi ALT, AST trước và trong điều trị. Ngừng nếu ALT/AST >3x ULN hoặc có triệu chứng tổn thương gan.",
            "GIẢM LIỀU SIMVASTATIN XUỐNG ≤20MG/NGÀY khi dùng với bempedoic acid (tăng nguy cơ đau cơ, tiêu cơ vân).",
            "GIẢM LIỀU PRAVASTATIN XUỐNG ≤40MG/NGÀY khi dùng với bempedoic acid (tăng nguy cơ đau cơ).",
            "Ít gây đau cơ hơn statin (do chỉ hoạt động ở gan, không ở cơ). Có thể dùng cho bệnh nhân không dung nạp statin.",
            "Có thể dùng cùng hoặc không cùng statin. Không có tương tác dược động học với atorvastatin, rosuvastatin, lovastatin.",
            "Uống bất kỳ lúc nào trong ngày, có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
            "Giảm LDL-C khoảng 18-25% khi dùng đơn trị. Kết hợp với ezetimibe (Nexlizet): giảm thêm ~38% LDL-C so với placebo.",
            "Thận trọng ở bệnh nhân suy thận nặng (eGFR <30) - dữ liệu hạn chế, không khuyến cáo.",
            "Thận trọng ở bệnh nhân suy gan nặng - dữ liệu hạn chế."
        ],
        "pharmacokinetics": {
            "half_life": "~21 giờ (bempedoic acid), ~21 giờ (bempedoyl-CoA - dạng hoạt tính)",
            "onset": "Giảm LDL-C bắt đầu trong 2-4 tuần, đạt tối đa sau 4-8 tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "bioavailability": "Không rõ (bempedoic acid là tiền thuốc, chuyển hóa thành bempedoyl-CoA ở gan)",
            "protein_binding": ">99% (bempedoic acid và bempedoyl-CoA)",
            "volume_of_distribution": "Không rõ, nhưng phân bố chủ yếu ở gan (nơi chuyển hóa thành dạng hoạt tính)",
            "metabolism": "Chuyển hóa ở gan thành bempedoyl-CoA (dạng hoạt tính) qua ACSVL1 (very long-chain acyl-CoA synthetase 1). Chỉ hoạt động ở gan do cần enzyme ACSVL1 để chuyển hóa. Không qua CYP450, nên ít tương tác với các thuốc chuyển hóa qua CYP450.",
            "clearance": "Chuyển hóa ở gan thành bempedoyl-CoA (dạng hoạt tính), thải qua thận (~70%) và phân (~30%). Tổng clearance: ~2-3 L/h.",
            "absorption": "Hấp thu nhanh sau khi uống. Thời gian đạt nồng độ đỉnh (Tmax): ~3.5 giờ cho bempedoic acid.",
            "food_effect": "Không ảnh hưởng đáng kể đến hấp thu. Có thể uống với hoặc không thức ăn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng trực tiếp. Để xa tầm tay trẻ em. Không sử dụng sau khi hết hạn.",
        "black_box_warnings": (
            "Tăng acid uric máu và bệnh gút: có thể gây bệnh gút, đặc biệt ở người có tiền sử gút. "
            "Theo dõi acid uric máu và điều trị dự phòng nếu cần."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Simvastatin >20mg/ngày",
                    "mechanism": "Bempedoic acid ức chế OATP1B1 (organic anion transporting polypeptide 1B1), làm giảm thải trừ simvastatin qua gan, dẫn đến tăng nồng độ simvastatin trong máu",
                    "effect": "Tăng nguy cơ đau cơ, yếu cơ, tăng CK, tiêu cơ vân (rhabdomyolysis)",
                    "management": "GIẢM LIỀU SIMVASTATIN XUỐNG ≤20MG/NGÀY khi dùng với bempedoic acid. Theo dõi CK và triệu chứng đau cơ chặt chẽ. Ngừng nếu có dấu hiệu tiêu cơ vân."
                },
                {
                    "drug": "Pravastatin >40mg/ngày",
                    "mechanism": "Bempedoic acid ức chế OATP1B1, làm giảm thải trừ pravastatin qua gan, dẫn đến tăng nồng độ pravastatin trong máu",
                    "effect": "Tăng nguy cơ đau cơ, yếu cơ, tăng CK",
                    "management": "GIẢM LIỀU PRAVASTATIN XUỐNG ≤40MG/NGÀY khi dùng với bempedoic acid. Theo dõi CK và triệu chứng đau cơ chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Ezetimibe",
                    "mechanism": "Không có tương tác dược động học đáng kể. Cả hai đều giảm LDL-C qua cơ chế khác nhau",
                    "effect": "Tác dụng cộng dồn giảm LDL-C (giảm thêm ~38% so với placebo khi dùng cùng)",
                    "management": "Có thể dùng cùng (Nexlizet). Không cần điều chỉnh liều."
                }
            ],
            "minor": [
                {
                    "drug": "Atorvastatin, Rosuvastatin, Lovastatin",
                    "mechanism": "Không có tương tác dược động học đáng kể với các statin này",
                    "effect": "Có thể dùng cùng, không tăng nguy cơ đau cơ",
                    "management": "Có thể dùng cùng với các statin này mà không cần điều chỉnh liều."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Không có tương tác đáng kể",
                    "effect": "Không ảnh hưởng đến INR",
                    "management": "Không cần điều chỉnh liều warfarin. Theo dõi INR như bình thường."
                },
                {
                    "drug": "Allopurinol, Febuxostat",
                    "mechanism": "Không có tương tác đáng kể",
                    "effect": "Có thể dùng để điều trị dự phòng bệnh gút",
                    "management": "Có thể dùng cùng để điều trị dự phòng bệnh gút nếu cần."
                }
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bempedoic acid.",
                "Bệnh gút đang hoạt động.",
                "Tăng acid uric máu không kiểm soát.",
            ],
            "tương_đối": [
                "Tiền sử bệnh gút - tăng nguy cơ tái phát, cần điều trị dự phòng.",
                "Suy thận nặng (eGFR <30) - thận trọng, dữ liệu hạn chế.",
                "Suy gan nặng - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. Bempedoic acid có thể gây hại cho thai nhi. "
                "Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả khi dùng bempedoic acid."
            ),
            "lactation": {
                "safety": "Incompatible",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, theo dõi men gan.",
            "severe": "Không khuyến cáo, dữ liệu hạn chế.",
            "notes": "Bempedoic acid chuyển hóa ở gan thành dạng hoạt tính. Suy gan có thể ảnh hưởng đến chuyển hóa.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng acid uric máu, bệnh gút (đau khớp, sưng khớp) - phổ biến nhất",
                "Tăng men gan (ALT, AST) - có thể kèm triệu chứng tổn thương gan",
                "Đau cơ, yếu cơ, tăng CK - đặc biệt nếu dùng với simvastatin/pravastatin liều cao",
                "Rối loạn tiêu hóa (đau bụng, buồn nôn)",
                "Mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ triệu chứng.",
            "treatment": [
                "Ngừng bempedoic acid ngay lập tức",
                "Rửa dạ dày nếu mới uống <1 giờ và bệnh nhân tỉnh táo",
                "Than hoạt tính nếu mới uống <2 giờ",
                "Điều trị bệnh gút: NSAID (ibuprofen, naproxen), colchicine, hoặc allopurinol/febuxostat nếu cần",
                "Theo dõi men gan (ALT, AST, bilirubin), CK, acid uric máu",
                "Điều trị hỗ trợ triệu chứng",
                "Không cần lọc máu (bempedoic acid không được loại bỏ hiệu quả qua lọc máu)"
            ],
            "monitoring": "Acid uric máu, men gan (ALT, AST, bilirubin), CK, lipid profile, triệu chứng lâm sàng, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu cho bempedoic acid. Điều trị hỗ trợ triệu chứng. Ngừng thuốc và điều trị các biến chứng (bệnh gút, tăng men gan, đau cơ) nếu có."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống bất kỳ lúc nào trong ngày, có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Có thể dùng cùng hoặc không cùng statin. Khuyến khích uống cùng giờ mỗi ngày để dễ nhớ.",
                "missed_dose": "Nếu quên uống, uống ngay khi nhớ ra. Nếu gần đến giờ uống liều tiếp theo, bỏ qua liều đã quên và uống liều tiếp theo đúng giờ. Không uống gấp đôi liều.",
                "special_populations": {
                    "elderly": "Không cần điều chỉnh liều ở người cao tuổi",
                    "pediatric": "Chưa được nghiên cứu ở trẻ em <18 tuổi. Không khuyến cáo sử dụng.",
                    "renal_impairment": "Thận trọng ở suy thận nặng (eGFR <30). Không khuyến cáo nếu eGFR <30.",
                    "hepatic_impairment": "Thận trọng ở suy gan nặng. Dữ liệu hạn chế."
                },
                "drug_separation": "Có thể dùng cùng lúc với statin (nhưng giảm liều simvastatin xuống ≤20mg/ngày và pravastatin xuống ≤40mg/ngày). Có thể dùng cùng với ezetimibe (Nexlizet)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống (viên nén). Không có dạng tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nexletol (bempedoic acid), Nexlizet (bempedoic acid + ezetimibe) - https://www.accessdata.fda.gov/drugsatfda_docs/label/",
                "CLEAR Outcomes trial - Nissen SE, et al. Bempedoic Acid and Cardiovascular Outcomes in Statin-Intolerant Patients. N Engl J Med. 2023;388(15):1353-64.",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "ACC/AHA Guidelines - Cholesterol Management Update (2024)",
                "ESC/EAS Guidelines - Dyslipidemia Management (2019)",
                "UpToDate - Bempedoic acid: Drug information (updated 2024)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCT (CLEAR Outcomes) showing cardiovascular benefit in statin-intolerant patients. Reduces major adverse cardiovascular events."
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Moderate", "metabolic": "Moderate (hyperuricemia, gout)"}
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ACC/AHA 2024 Cholesterol Management Update",
            "ESC/EAS 2019 Dyslipidemia Guidelines"
        ],
    },
    "Ezetimibe": {
        "group": "Cardiovascular - Cholesterol Absorption Inhibitor",
        "vietnamese_name": "Ezetimibe, Ezetrol, Zetia, Ezetimibe Stada",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu tiên phát (đơn trị hoặc kết hợp với statin)",
            "Tăng cholesterol máu gia đình dị hợp tử (heterozygous familial hypercholesterolemia) - đơn trị hoặc kết hợp với statin",
            "Tăng cholesterol máu đồng hợp tử (homozygous familial hypercholesterolemia) - kết hợp với statin và các thuốc khác",
            "Bệnh nhân không dung nạp statin hoặc cần giảm LDL-C thêm (dùng đơn trị)",
            "Dự phòng biến cố tim mạch ở bệnh nhân hội chứng mạch vành cấp (ACS) - kết hợp với simvastatin (IMPROVE-IT study)",
            "Bệnh thận mạn (CKD) - kết hợp với simvastatin để giảm biến cố tim mạch (SHARP study)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với ezetimibe hoặc bất kỳ thành phần nào của thuốc"
            ],
            "tương_đối": [
                "Bệnh gan hoạt động (khi dùng với statin) - statin chống chỉ định, nhưng có thể dùng ezetimibe đơn trị",
                "Có thai (khi dùng với statin) - statin chống chỉ định trong thai kỳ (category X), ezetimibe category C",
                "Dùng với cyclosporine - giảm liều ezetimibe xuống 5mg/ngày",
                "Dùng với fibrates - tăng nguy cơ sỏi mật, thận trọng"
            ]
        },
        "dosage": {
            "adult_monotherapy": "10mg PO x 1 lần/ngày",
            "adult_with_statin": "10mg PO x 1 lần/ngày (kết hợp với statin bất kỳ)",
            "adult_with_fenofibrate": "10mg PO x 1 lần/ngày (kết hợp với fenofibrate)",
            "pediatric": {
                "10_17_years": "10mg PO x 1 lần/ngày (đơn trị hoặc kết hợp với statin)",
                "under_10_years": "Chưa được nghiên cứu, không khuyến cáo",
                "notes": "FDA-approved cho trẻ em ≥10 tuổi với tăng cholesterol máu gia đình dị hợp tử"
            },
            "geriatric": {
                "dosing": "10mg PO x 1 lần/ngày (không cần điều chỉnh liều)",
                "notes": "Người cao tuổi (≥65 tuổi) không cần điều chỉnh liều. Dữ liệu an toàn tương tự như người trẻ tuổi."
            },
            "notes": "Uống bất kỳ lúc nào trong ngày, có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu. Có thể dùng cùng lúc với statin hoặc cách xa. Dùng cách xa cholestyramine, colestipol, colesevelam ít nhất 2 giờ."
        },
        "renal_adjustment": {
            "normal": "Không cần điều chỉnh liều",
            "30_60": "Không cần điều chỉnh liều",
            "under_30": "Không cần điều chỉnh liều (đã được nghiên cứu trong CKD - SHARP study)"
        },
        "side_effects": [
            "Rối loạn tiêu hóa (tiêu chảy, đau bụng, đầy hơi) - phổ biến nhất (~2-4%), thường nhẹ và tự hết",
            "Đau khớp, đau cơ - ít gặp hơn statin đơn trị",
            "Mệt mỏi, yếu cơ",
            "Đau đầu",
            "Tăng men gan (ALT, AST) - khi dùng với statin, hiếm khi đơn trị",
            "Đau cơ, tiêu cơ vân - khi dùng với statin, ít hơn statin đơn trị",
            "Sỏi mật - tăng nguy cơ khi dùng với fibrates",
            "Phát ban, ngứa - hiếm gặp",
            "Tăng CK (creatine kinase) - khi dùng với statin"
        ],
        "interactions": [
            "Cholestyramine, Colestipol, Colesevelam: giảm hấp thu ezetimibe - dùng cách xa ít nhất 2 giờ",
            "Fibrates (Fenofibrate, Gemfibrozil): tăng nguy cơ sỏi mật - thận trọng, theo dõi dấu hiệu sỏi mật",
            "Cyclosporine: tăng nồng độ ezetimibe - giảm liều ezetimibe xuống 5mg/ngày",
            "Statin: không có tương tác dược động học, có thể dùng cùng lúc hoặc cách xa",
            "Warfarin: không có tương tác đáng kể",
            "Digoxin: không có tương tác đáng kể"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Cân nhắc lợi ích/nguy cơ.",
        "mechanism_of_action": "Ezetimibe ức chế hấp thu cholesterol ở ruột non bằng cách ức chế protein NPC1L1 (Niemann-Pick C1-Like 1) ở bờ bàn chải của tế bào ruột. NPC1L1 chịu trách nhiệm vận chuyển cholesterol từ lòng ruột vào tế bào ruột. Bằng cách ức chế protein này, ezetimibe làm giảm hấp thu cholesterol từ thức ăn và từ mật (cholesterol được tái hấp thu), dẫn đến giảm cholesterol toàn phần và LDL cholesterol. Ezetimibe giảm LDL cholesterol khoảng 15-20% khi dùng đơn trị, và giảm thêm 15-20% khi kết hợp với statin (tác dụng cộng dồn). Ezetimibe không ảnh hưởng đến hấp thu triglyceride, vitamin tan trong dầu, hoặc acid mật. Thuốc tác dụng tại ruột, ít hấp thu vào máu (chuyển hóa thành ezetimibe-glucuronide ở ruột và gan).",
        "monitoring": [
            "Lipid profile (LDL-C, HDL-C, TG, total cholesterol, non-HDL-C) - kiểm tra trước điều trị, sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "Chức năng gan (ALT, AST, bilirubin) - trước điều trị và trong điều trị (mỗi 3-6 tháng), đặc biệt khi dùng với statin",
            "Dấu hiệu tác dụng phụ tiêu hóa (tiêu chảy, đau bụng, đầy hơi) - thường nhẹ và tự hết",
            "Dấu hiệu sỏi mật (đau bụng phải trên, vàng da) - khi dùng với fibrates, theo dõi chặt chẽ",
            "CK (creatine kinase) nếu có đau cơ hoặc yếu cơ - đặc biệt khi dùng với statin",
            "Triệu chứng đau khớp, đau cơ - theo dõi và đánh giá",
            "Đáp ứng điều trị - đánh giá giảm LDL-C sau 4-8 tuần, điều chỉnh liều hoặc thêm thuốc nếu cần"
        ],
        "precautions": [
            "Uống bất kỳ lúc nào trong ngày, có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
            "Có thể dùng cùng lúc với statin hoặc cách xa. Không có tương tác dược động học với statin.",
            "Giảm LDL cholesterol khoảng 15-20% khi dùng đơn trị. Hiệu quả giảm LDL-C tương tự ở các nhóm tuổi và giới tính.",
            "Kết hợp với statin: giảm thêm 15-20% LDL-C so với statin đơn trị (tác dụng cộng dồn). Hiệu quả tương tự với tất cả các statin.",
            "Ít tác dụng phụ hơn statin (đặc biệt đau cơ, tiêu cơ vân). Có thể dùng cho bệnh nhân không dung nạp statin.",
            "Dùng cách xa cholestyramine, colestipol, colesevelam ít nhất 2 giờ (giảm hấp thu ezetimibe). Dùng ezetimibe trước hoặc sau các thuốc này.",
            "Thận trọng khi dùng với fibrates (fenofibrate, gemfibrozil) - tăng nguy cơ sỏi mật. Theo dõi dấu hiệu sỏi mật (đau bụng phải trên, vàng da).",
            "Giảm liều xuống 5mg/ngày khi dùng với cyclosporine (tăng nồng độ ezetimibe). Theo dõi lipid profile và tác dụng phụ.",
            "Theo dõi men gan khi dùng với statin (tăng nguy cơ tăng men gan). Ngừng nếu ALT/AST >3x ULN.",
            "Không ảnh hưởng đến hấp thu triglyceride, vitamin tan trong dầu, hoặc acid mật.",
            "Có thể dùng ở bệnh nhân suy thận (đã được nghiên cứu trong CKD - SHARP study).",
            "Thận trọng ở bệnh nhân suy gan nặng khi dùng với statin (statin chống chỉ định ở bệnh gan hoạt động)."
        ],
        "pharmacokinetics": {
            "half_life": "22 giờ (ezetimibe), 24 giờ (ezetimibe-glucuronide - dạng hoạt tính)",
            "onset": "Giảm LDL-C bắt đầu trong 2 tuần, đạt tối đa sau 4-6 tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "bioavailability": "Không rõ (ezetimibe-glucuronide là dạng hoạt tính chính)",
            "protein_binding": ">90% (ezetimibe và ezetimibe-glucuronide)",
            "volume_of_distribution": "Không rõ, nhưng phân bố chủ yếu ở ruột và gan",
            "metabolism": "Chuyển hóa nhanh ở ruột và gan thành ezetimibe-glucuronide (dạng hoạt tính chính) qua UDP-glucuronosyltransferase. Không qua CYP450, nên ít tương tác với các thuốc chuyển hóa qua CYP450.",
            "clearance": "Chủ yếu qua phân (78% - chủ yếu là ezetimibe-glucuronide), một phần qua thận (11%). Tổng clearance: ~3.5-4.5 L/h/kg.",
            "absorption": "Hấp thu nhanh sau khi uống. Thời gian đạt nồng độ đỉnh (Tmax): 4-12 giờ cho ezetimibe, 1-2 giờ cho ezetimibe-glucuronide.",
            "food_effect": "Không ảnh hưởng đáng kể đến hấp thu. Có thể uống với hoặc không thức ăn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Để xa tầm tay trẻ em. Không sử dụng sau khi hết hạn.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cholestyramine, Colestipol, Colesevelam (bile acid sequestrants)",
                    "mechanism": "Bile acid sequestrants liên kết với ezetimibe trong ruột, giảm hấp thu ezetimibe",
                    "effect": "Giảm nồng độ ezetimibe trong máu, giảm hiệu quả giảm LDL-C",
                    "management": "Dùng cách xa ít nhất 2 giờ. Dùng ezetimibe trước hoặc sau bile acid sequestrants ít nhất 2 giờ. Khuyến khích dùng ezetimibe ít nhất 2 giờ trước hoặc 4 giờ sau bile acid sequestrants."
                }
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Cyclosporine ức chế P-glycoprotein và có thể ảnh hưởng đến chuyển hóa ezetimibe, làm tăng nồng độ ezetimibe trong máu",
                    "effect": "Tăng nồng độ ezetimibe và ezetimibe-glucuronide, tăng nguy cơ tác dụng phụ",
                    "management": "Giảm liều ezetimibe xuống 5mg/ngày khi dùng với cyclosporine. Theo dõi lipid profile và tác dụng phụ (rối loạn tiêu hóa, đau khớp)."
                },
                {
                    "drug": "Fibrates (Fenofibrate, Gemfibrozil)",
                    "mechanism": "Cả ezetimibe và fibrates đều ảnh hưởng đến chuyển hóa cholesterol và bài tiết mật, có thể làm tăng nguy cơ hình thành sỏi mật",
                    "effect": "Tăng nguy cơ sỏi mật, đặc biệt với gemfibrozil",
                    "management": "Thận trọng khi dùng cùng. Theo dõi dấu hiệu sỏi mật (đau bụng phải trên, vàng da). Có thể dùng với fenofibrate (đã được nghiên cứu trong một số thử nghiệm), nhưng thận trọng hơn với gemfibrozil."
                }
            ],
            "minor": [
                {
                    "drug": "Statin (tất cả các statin)",
                    "mechanism": "Không có tương tác dược động học đáng kể. Ezetimibe không ảnh hưởng đến chuyển hóa statin qua CYP450.",
                    "effect": "Tác dụng cộng dồn giảm LDL-C (giảm thêm 15-20% so với statin đơn trị)",
                    "management": "Có thể dùng cùng lúc hoặc cách xa. Không cần điều chỉnh liều statin."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Không có tương tác đáng kể",
                    "effect": "Không ảnh hưởng đến INR",
                    "management": "Không cần điều chỉnh liều warfarin. Theo dõi INR như bình thường."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Không có tương tác đáng kể",
                    "effect": "Không ảnh hưởng đến nồng độ digoxin",
                    "management": "Không cần điều chỉnh liều digoxin."
                }
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ezetimibe hoặc bất kỳ thành phần nào của thuốc"
            ],
            "tương_đối": [
                "Bệnh gan hoạt động (khi dùng với statin) - statin chống chỉ định, nhưng có thể dùng ezetimibe đơn trị",
                "Có thai (khi dùng với statin) - statin chống chỉ định trong thai kỳ (category X), ezetimibe category C",
                "Dùng với cyclosporine - giảm liều ezetimibe xuống 5mg/ngày",
                "Dùng với fibrates - tăng nguy cơ sỏi mật, thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ezetimibe phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Cân nhắc lợi ích/nguy cơ. Nếu dùng với statin: statin chống chỉ định trong thai kỳ (category X).",
            "lactation": {
                "safety": "Compatible",
                "details": "Ezetimibe và ezetimibe-glucuronide bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều (khi dùng đơn trị)",
            "severe": "Thận trọng khi dùng với statin (statin chống chỉ định ở bệnh gan hoạt động). Có thể dùng ezetimibe đơn trị.",
            "notes": "Ezetimibe chuyển hóa ở ruột và gan thành ezetimibe-glucuronide. Suy gan có thể ảnh hưởng nhẹ đến chuyển hóa, nhưng thường không cần điều chỉnh liều khi dùng đơn trị. Khi dùng với statin: statin chống chỉ định ở bệnh gan hoạt động."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn tiêu hóa (tiêu chảy, đau bụng, đầy hơi) - phổ biến nhất",
                "Mệt mỏi, yếu cơ",
                "Đau khớp, đau cơ",
                "Đau đầu",
                "Buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ezetimibe ngay lập tức",
                "Rửa dạ dày nếu mới uống <1 giờ và bệnh nhân tỉnh táo",
                "Than hoạt tính nếu mới uống <2 giờ",
                "Điều trị hỗ trợ triệu chứng (bù nước nếu tiêu chảy nhiều)",
                "Theo dõi triệu chứng và dấu hiệu sinh tồn",
                "Không cần lọc máu (ezetimibe không được loại bỏ hiệu quả qua lọc máu)"
            ],
            "monitoring": "Triệu chứng lâm sàng, dấu hiệu sinh tồn, lipid profile (nếu cần), chức năng gan nếu có triệu chứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu cho ezetimibe. Điều trị hỗ trợ triệu chứng. Ezetimibe có độc tính thấp và các triệu chứng quá liều thường nhẹ."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu. Có thể uống cùng lúc với bữa ăn hoặc khi đói.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày (sáng, trưa, tối đều được). Có thể dùng cùng lúc với statin hoặc cách xa. Khuyến khích uống cùng giờ mỗi ngày để dễ nhớ.",
                "missed_dose": "Nếu quên uống, uống ngay khi nhớ ra. Nếu gần đến giờ uống liều tiếp theo, bỏ qua liều đã quên và uống liều tiếp theo đúng giờ. Không uống gấp đôi liều.",
                "special_populations": {
                    "elderly": "Không cần điều chỉnh liều ở người cao tuổi",
                    "pediatric": "FDA-approved cho trẻ em ≥10 tuổi, liều giống người lớn (10mg/ngày)",
                    "renal_impairment": "Không cần điều chỉnh liều ở bệnh nhân suy thận",
                    "hepatic_impairment": "Không cần điều chỉnh liều khi dùng đơn trị. Thận trọng khi dùng với statin."
                },
                "drug_separation": "Dùng cách xa cholestyramine, colestipol, colesevelam ít nhất 2 giờ. Có thể dùng ezetimibe trước hoặc sau các thuốc này."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống (viên nén). Không có dạng tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ezetimibe (Zetia) - https://www.accessdata.fda.gov/drugsatfda_docs/label/",
                "UpToDate - Ezetimibe: Drug information (updated 2024)",
                "IMPROVE-IT Study - Cannon CP, et al. Ezetimibe Added to Statin Therapy after Acute Coronary Syndromes. N Engl J Med. 2015;372(25):2387-97.",
                "SHARP Study - Baigent C, et al. The effects of lowering LDL cholesterol with simvastatin plus ezetimibe in patients with chronic kidney disease (Study of Heart and Renal Protection): a randomised placebo-controlled trial. Lancet. 2011;377(9784):2181-92.",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "ACC/AHA Guidelines - Cholesterol Management Update (2024)",
                "ESC/EAS Guidelines - Dyslipidemia Management (2019)",
                "KDIGO Clinical Practice Guideline - Lipid Management in CKD (2013)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Multiple large RCTs (IMPROVE-IT, SHARP) showing cardiovascular benefit when combined with statin. FDA-approved for monotherapy and combination therapy."
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "gastrointestinal": "Low"}
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ACC/AHA 2024 Cholesterol Management Update",
            "ESC/EAS 2019 Dyslipidemia Guidelines",
            "KDIGO 2013 Lipid Management in CKD"
        ]
    },

}

__all__ = ['CHOLESTEROL_ABSORPTION_INHIBITORS']






















