"""
Hepatitis Antivirals
Ribavirin for hepatitis C treatment
"""

HEPATITIS_ANTIVIRALS = {
    "Entecavir": {
        "group": "Infectious Disease - Antiviral (HBV)",
        "vietnamese_name": "Entecavir, Baraclude",
        "administration": ["PO"],
        "indications": [
            "Viêm gan B mạn (HBV) - có hoặc không xơ gan bù"
        ],
        "contraindications": [
            "Dị ứng",
            "Bệnh nhân đồng nhiễm HIV chưa điều trị (nguy cơ kháng lamivudine/entecavir)"
        ],
        "dosage": {
            "naive": "0.5mg x 1 lần/ngày, uống lúc đói",
            "lamivudine_resistance_or_decompensated": "1mg x 1 lần/ngày, uống lúc đói",
            "notes": "Uống cách bữa ăn ít nhất 2 giờ (trước và sau)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm 50% hoặc dùng cách ngày",
            "under_30": "Giảm 75% hoặc dùng mỗi 3 ngày; chạy thận: dùng sau lọc"
        },
        "side_effects": [
            "Đau đầu, mệt",
            "Tăng men gan thoáng qua",
            "Toan lactic (hiếm, nguy cơ cao hơn ở xơ gan mất bù)"
        ],
        "interactions": [
            "Ít tương tác đáng kể; thận trọng với thuốc độc thận"
        ],
        "pregnancy": "C (ưu tiên tenofovir ở phụ nữ mang thai)",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "AASLD 2024 HBV",
            "EASL 2023 HBV"
        ],
        "mechanism_of_action": "Nucleoside analog (guanosine) ức chế HBV DNA polymerase/reverse transcriptase, gây kết thúc chuỗi.",
        "monitoring": [
            "HBV DNA, ALT mỗi 3-6 tháng",
            "Chức năng thận định kỳ (điều chỉnh liều)",
            "Dấu hiệu toan lactic ở bệnh nhân xơ gan mất bù"
        ],
        "precautions": [
            "Nguy cơ bùng phát HBV sau ngừng thuốc - giảm liều hoặc theo dõi sát",
            "Điều chỉnh liều ở suy thận",
            "Không đơn trị ở bệnh nhân đồng nhiễm HIV chưa được ART"
        ],
        "pharmacokinetics": {
            "half_life": "128-149 giờ (pha cuối)",
            "onset": "Giảm HBV DNA trong vài tuần",
            "duration": "Dùng hằng ngày, dài hạn",
            "protein_binding": "<1%",
            "clearance": "Thận (bài tiết ống thận)"
        },
        "storage": "Nhiệt độ phòng, tránh ẩm.",
        "black_box_warnings": "Bùng phát viêm gan sau ngừng điều trị; nguy cơ toan lactic và gan to nhiễm mỡ với nucleos(t)ide analogs.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc độc thận (aminoglycoside, amphotericin B, cisplatin)",
                    "mechanism": "Tăng nguy cơ suy thận → tăng nồng độ entecavir",
                    "effect": "Tăng độc tính",
                    "management": "Tránh nếu có thể; theo dõi creatinine, điều chỉnh liều."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": ["Dị ứng entecavir"],
            "tương_đối": [
                "Đồng nhiễm HIV chưa điều trị",
                "Suy thận (cần chỉnh liều)",
                "Xơ gan mất bù (theo dõi toan lactic)"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng entecavir"],
            "tương_đối": [
                "Đồng nhiễm HIV chưa điều trị",
                "Suy thận (cần chỉnh liều)",
                "Xơ gan mất bù (theo dõi toan lactic)"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Lọc máu có thể loại bỏ entecavir một phần."
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ưu tiên tenofovir nếu có thai. Dữ liệu hạn chế.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết sữa; cân nhắc ngừng cho bú hoặc chọn thuốc khác.",
                "recommendation": "Cân nhắc lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Không cần chỉnh nhưng theo dõi toan lactic",
            "severe": "Thận trọng; theo dõi sát ALT/AST và toan lactic",
            "notes": "Chủ yếu thải qua thận; độc tính gan liên quan nhóm nucleoside."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, tăng men gan, toan lactic (hiếm)"],
            "antidote": "Không có",
            "treatment": [
                "Điều trị hỗ trợ, theo dõi toan chuyển hóa",
                "Lọc máu có thể loại bỏ entecavir một phần"
            ],
            "monitoring": "Creatinine, men gan, khí máu nếu nghi ngờ toan lactic"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống lúc đói (cách bữa ăn ≥2 giờ)",
                "timing": "1 lần/ngày, cố định thời điểm"
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "AASLD 2024 HBV Guidance",
                "EASL 2023 HBV Guidelines",
                "Baraclude Prescribing Information"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "A - Dữ liệu thử nghiệm lâm sàng và hướng dẫn chuyên ngành"
        }
    },

    "Ledipasvir": {
        "group": "Infectious Disease - Antiviral (HCV NS5A inhibitor)",
        "vietnamese_name": "Ledipasvir (phối hợp Sofosbuvir/Ledipasvir - Harvoni)",
        "administration": ["PO"],
        "indications": [
            "Viêm gan C mạn genotype 1, 4, 5, 6 (phối hợp cố định với sofosbuvir)"
        ],
        "contraindications": [
            "Dị ứng",
            "Dùng đơn trị (không có dạng đơn thành phần lưu hành)",
            "Dùng với rifampin, carbamazepine, St. John’s wort (giảm nồng độ)"
        ],
        "dosage": {
            "adult": "Ledipasvir 90mg + Sofosbuvir 400mg x 1 lần/ngày",
            "duration": "12 tuần (đa số); 8 tuần nếu không xơ gan, tải lượng thấp; 24 tuần nếu xơ gan mất bù hoặc thất bại trước đó",
            "notes": "Uống cùng hoặc không cùng thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Tránh hoặc theo dõi sát; cân nhắc phác đồ khác ở eGFR <30"
        },
        "side_effects": [
            "Mệt mỏi, đau đầu",
            "Buồn nôn",
            "Tăng bilirubin nhẹ",
            "Nhịp chậm khi phối hợp amiodarone (qua sofosbuvir)"
        ],
        "interactions": [
            "Thuốc kháng acid/PPIs: giảm hấp thu ledipasvir (pH phụ thuộc)",
            "P-gp inducers (rifampin, carbamazepine): giảm nồng độ",
            "Amiodarone: nguy cơ nhịp chậm (do sofosbuvir thành phần)"
        ],
        "pregnancy": "B (không phối hợp ribavirin); tránh nếu phác đồ có ribavirin",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "AASLD/IDSA HCV 2024",
            "EASL HCV 2024"
        ],
        "mechanism_of_action": "Ức chế NS5A của HCV, chặn nhân lên và lắp ráp virus; dùng phối hợp với sofosbuvir để ngăn đề kháng.",
        "monitoring": [
            "HCV RNA, ALT",
            "Nhịp tim nếu có amiodarone (tránh)",
            "Tương tác pH: đảm bảo khoảng cách với PPI/antacid"
        ],
        "precautions": [
            "Không phối hợp với rifampin, carbamazepine, St. John’s wort",
            "Antacid: dùng cách ≥4 giờ; PPI: omeprazole tối đa 20mg dùng cùng lúc trước ăn",
            "Tránh amiodarone; theo dõi nếu buộc dùng",
            "Bùng phát HBV: sàng lọc HBV trước điều trị HCV"
        ],
        "pharmacokinetics": {
            "half_life": "47 giờ",
            "onset": "Giảm HCV RNA trong tuần đầu khi phối hợp",
            "duration": "1 lần/ngày",
            "protein_binding": "99.8%",
            "clearance": "Chủ yếu qua mật/phân; bài tiết thận tối thiểu"
        },
        "storage": "Nhiệt độ phòng, khô ráo.",
        "black_box_warnings": "Nguy cơ bùng phát HBV khi điều trị HCV.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                    "mechanism": "Cảm ứng P-gp/BCRP → giảm nồng độ",
                    "effect": "Thất bại điều trị",
                    "management": "TRÁNH phối hợp."
                }
            ],
            "moderate": [
                {
                    "drug": "PPI/antacid",
                    "mechanism": "Tăng pH dạ dày làm giảm hấp thu ledipasvir",
                    "effect": "Giảm hiệu quả",
                    "management": "Uống Harvoni cùng PPI liều thấp (omeprazole ≤20mg) trước ăn; antacid cách 4 giờ."
                },
                {
                    "drug": "Amiodarone",
                    "mechanism": "Nhịp chậm qua thành phần sofosbuvir",
                    "effect": "Nguy cơ block/nhịp chậm nặng",
                    "management": "Tránh; nếu bắt buộc, theo dõi ECG."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": ["Dị ứng", "Phối hợp rifampin/carbamazepine/St. John's wort"],
            "tương_đối": [
                "Suy thận nặng (eGFR <30)",
                "Dùng PPI/antacid liều cao",
                "Đồng nhiễm HBV chưa điều trị"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng", "Phối hợp rifampin/carbamazepine/St. John's wort"],
            "tương_đối": [
                "Suy thận nặng (eGFR <30)",
                "Dùng PPI/antacid liều cao",
                "Đồng nhiễm HBV chưa điều trị"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Tránh nếu phác đồ kèm ribavirin (X). Nếu không có ribavirin, dữ liệu hạn chế nhưng không cho thấy độc tính rõ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết; cân nhắc ngừng cho bú.",
                "recommendation": "Quyết định theo lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Không cần chỉnh",
            "severe": "Thận trọng ở Child-Pugh C; tham khảo phác đồ chuyên khoa",
            "notes": "Chuyển hóa qua gan/bile; dữ liệu hạn chế ở xơ gan mất bù."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu; lý thuyết kéo dài QT/nhịp chậm (thành phần sofosbuvir)"],
            "antidote": "Không có",
            "treatment": [
                "Điều trị hỗ trợ",
                "Theo dõi ECG, điện giải"
            ],
            "monitoring": "ECG, dấu hiệu sinh tồn"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể với hoặc không",
                "timing": "1 lần/ngày; tránh antacid gần thời điểm uống"
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "AASLD/IDSA HCV Guidance 2024",
                "Harvoni Prescribing Information"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "A - Hướng dẫn chuyên ngành và dữ liệu pha 3"
        }
    },

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
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hematologic": True, "teratogenic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
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
        "guideline_tags": [
            "AASLD/IDSA HCV 2024",
            "WHO viral hepatitis 2024"
        ],
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
        "contraindications_detail": {
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
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Lọc máu có thể giúp loại bỏ ribavirin (half-life dài, tích tụ trong tế bào)."
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
            "last_updated": "2025-12-24",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    }

    ,
    "Sofosbuvir": {
        "group": "Infectious Disease - Antiviral (HCV NS5B inhibitor)",
        "vietnamese_name": "Sofosbuvir, Sovaldi",
        "administration": ["PO"],
        "indications": [
            "Viêm gan C mạn (HCV) phối hợp thuốc khác (không đơn trị)"
        ],
        "contraindications": [
            "Dùng đơn trị (không hiệu quả)",
            "Dùng với amiodarone (nguy cơ nhịp chậm nghiêm trọng)",
            "Dị ứng"
        ],
        "dosage": {
            "adult": "400mg x 1 lần/ngày, phối hợp (ví dụ với ledipasvir, velpatasvir, daclatasvir...)",
            "notes": "Uống cùng hoặc không cùng thức ăn; luôn phối hợp."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, theo dõi",
            "under_30": "Dữ liệu hạn chế; tránh nếu eGFR <30 trừ khi phác đồ cho phép"
        },
        "side_effects": [
            "Mệt, đau đầu",
            "Buồn nôn",
            "Thiếu máu (khi phối hợp ribavirin)",
            "Nhịp chậm nặng khi phối hợp amiodarone"
        ],
        "interactions": [
            "Amiodarone: nguy cơ nhịp chậm, chống phối hợp",
            "P-gp inducers (rifampin, carbamazepine): giảm hiệu quả",
            "Acid giảm dạ dày ít ảnh hưởng khi đơn thành phần"
        ],
        "pregnancy": "B (nhưng phụ thuộc thuốc phối hợp, ví dụ ribavirin = X)",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "AASLD/IDSA HCV 2024",
            "EASL HCV 2024"
        ],
        "mechanism_of_action": "Nucleotide analog ức chế NS5B RNA-dependent RNA polymerase của HCV, gây kết thúc chuỗi.",
        "monitoring": [
            "HCV RNA, ALT mỗi 4-8 tuần",
            "Nhịp tim nếu phải phối hợp amiodarone (tránh)",
            "Công thức máu nếu phối hợp ribavirin"
        ],
        "precautions": [
            "KHÔNG dùng đơn trị; luôn phối hợp theo phác đồ HCV",
            "Tránh với amiodarone; nếu bất khả kháng, theo dõi ECG 48 giờ đầu",
            "Điều chỉnh/giám sát ở suy thận nặng"
        ],
        "pharmacokinetics": {
            "half_life": "0.4 giờ (sofosbuvir), 27 giờ (GS-331007 chất chuyển hóa hoạt tính)",
            "onset": "Giảm HCV RNA nhanh trong tuần đầu",
            "duration": "1 lần/ngày",
            "protein_binding": "61-65%",
            "clearance": "Chuyển hóa gan; thải qua thận (chất chuyển hóa)"
        },
        "storage": "Nhiệt độ phòng, chai kín.",
        "black_box_warnings": "Nguy cơ bùng phát HBV khi điều trị HCV - sàng lọc HBV trước điều trị.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Cộng hưởng gây nhịp chậm nặng",
                    "effect": "Nhịp chậm, block nhĩ thất, ngừng tim",
                    "management": "TRÁNH; nếu bắt buộc, theo dõi ECG liên tục 48-72 giờ."
                }
            ],
            "moderate": [
                {
                    "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                    "mechanism": "Cảm ứng P-gp/CYP làm giảm nồng độ",
                    "effect": "Giảm hiệu quả, thất bại điều trị",
                    "management": "Tránh phối hợp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": ["Dị ứng", "Phối hợp amiodarone"],
            "tương_đối": [
                "Suy thận nặng (eGFR <30)",
                "Phụ nữ có thai nếu phác đồ chứa ribavirin (X)",
                "Đồng nhiễm HBV chưa được điều trị (nguy cơ bùng phát)"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng", "Phối hợp amiodarone"],
            "tương_đối": [
                "Suy thận nặng (eGFR <30)",
                "Phụ nữ có thai nếu phác đồ chứa ribavirin (X)",
                "Đồng nhiễm HBV chưa được điều trị (nguy cơ bùng phát)"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Thẩm tách loại bỏ chất chuyển hóa một phần."
        },
        "pregnancy_lactation": {
            "fda_category": "B (đơn thành phần)",
            "pregnancy_details": "Đánh giá theo phác đồ phối hợp; nếu có ribavirin: chống chỉ định thai kỳ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết; cân nhắc ngừng cho bú.",
                "recommendation": "Quyết định theo lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Không cần chỉnh",
            "severe": "Thận trọng ở Child-Pugh C (phối hợp thuốc khác)",
            "notes": "Chưa thấy thay đổi đáng kể riêng sofosbuvir; phụ thuộc thuốc phối hợp."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu; có thể nhịp chậm nếu có amiodarone"],
            "antidote": "Không có",
            "treatment": [
                "Điều trị hỗ trợ, theo dõi ECG",
                "Thẩm tách loại bỏ chất chuyển hóa một phần"
            ],
            "monitoring": "ECG nếu nghi nhịp chậm, dấu hiệu lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể với hoặc không; uống cùng phác đồ khác vào cùng thời điểm mỗi ngày",
                "timing": "1 lần/ngày"
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "AASLD/IDSA HCV Guidance 2024",
                "Sovaldi Prescribing Information"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "A - Hướng dẫn chuyên ngành và dữ liệu pha 3"
        }
    },

    "Sofosbuvir/Velpatasvir": {
        "group": "Infectious Disease - Antiviral (HCV NS5B + NS5A inhibitor FDC)",
        "vietnamese_name": "Sofosbuvir/Velpatasvir (Epclusa)",
        "administration": ["PO"],
        "indications": [
            "Viêm gan C mạn tất cả genotype (1–6), có hoặc không xơ gan.",
            "Kết hợp ribavirin ở xơ gan mất bù nếu cần."
        ],
        "contraindications": [
            "Dị ứng thành phần.",
            "Dùng với amiodarone (nguy cơ nhịp chậm nặng qua sofosbuvir).",
            "Cảm ứng mạnh P-gp/CYP (rifampin, carbamazepine, St. John’s wort)."
        ],
        "dosage": {
            "adult": "Sofosbuvir 400mg + Velpatasvir 100mg x 1 lần/ngày, 12 tuần.",
            "decomp_cirrhosis": "Thêm ribavirin và/hoặc kéo dài theo hướng dẫn chuyên khoa.",
            "notes": "Uống cùng hoặc không cùng thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Thận trọng; theo dõi.",
            "under_30": "Tránh hoặc tham khảo chuyên khoa (dữ liệu hạn chế ở eGFR <30)."
        },
        "side_effects": [
            "Đau đầu, mệt.",
            "Buồn nôn.",
            "Nhịp chậm khi phối hợp amiodarone (tránh)."
        ],
        "interactions": [
            "Amiodarone: nhịp chậm nặng (tránh).",
            "P-gp/CYP inducers (rifampin, carbamazepine, phenytoin, St. John’s wort): giảm nồng độ.",
            "Acid giảm dạ dày (PPI/antacid): giảm hấp thu velpatasvir."
        ],
        "pregnancy": "B nếu không có ribavirin; nếu phối hợp ribavirin: chống chỉ định thai kỳ.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "AASLD/IDSA HCV 2024",
            "EASL HCV 2024"
        ],
        "mechanism_of_action": "FDC ức chế NS5B (sofosbuvir) và NS5A (velpatasvir), chặn sao chép và lắp ráp HCV, hiệu quả pangenotypic.",
        "monitoring": [
            "HCV RNA, ALT mỗi 4-8 tuần.",
            "Nhịp tim nếu buộc dùng amiodarone (tránh).",
            "HBV serology/HBV DNA (nguy cơ bùng phát HBV)."
        ],
        "precautions": [
            "Sàng lọc HBV trước điều trị; theo dõi bùng phát HBV.",
            "Tránh amiodarone; nếu buộc dùng, theo dõi ECG liên tục 48–72 giờ.",
            "PPI/antacid: dùng omeprazole ≤20mg cùng thời điểm trước ăn; antacid cách ≥4 giờ."
        ],
        "pharmacokinetics": {
            "half_life": "Sofosbuvir 0.4h (tiền thuốc), chất chuyển hóa 27h; Velpatasvir ~15h.",
            "onset": "Giảm HCV RNA nhanh trong tuần đầu.",
            "duration": "1 lần/ngày.",
            "protein_binding": "Sofosbuvir ~61–65%; Velpatasvir ~99%.",
            "clearance": "Sofosbuvir chuyển hóa gan, thải thận chất chuyển hóa; Velpatasvir thải qua mật/phân."
        },
        "storage": "Nhiệt độ phòng, khô ráo.",
        "black_box_warnings": "Nguy cơ bùng phát HBV khi điều trị HCV – sàng lọc HBV trước điều trị.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Cộng hưởng gây nhịp chậm nặng (qua sofosbuvir).",
                    "effect": "Nguy cơ block/nhịp chậm nghiêm trọng.",
                    "management": "TRÁNH; nếu bắt buộc, theo dõi ECG liên tục 48–72 giờ."
                },
                {
                    "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                    "mechanism": "Cảm ứng P-gp/CYP giảm nồng độ sofosbuvir/velpatasvir.",
                    "effect": "Thất bại điều trị.",
                    "management": "CHỐNG CHỈ ĐỊNH."
                }
            ],
            "moderate": [
                {
                    "drug": "PPI/antacid",
                    "mechanism": "Tăng pH giảm hấp thu velpatasvir.",
                    "effect": "Giảm hiệu quả.",
                    "management": "PPI: omeprazole ≤20mg dùng cùng thời điểm trước ăn; antacid cách ≥4 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": ["Dị ứng", "Phối hợp amiodarone", "Phối hợp rifampin/carbamazepine/phenytoin/St. John's wort"],
            "tương_đối": [
                "Suy thận nặng (eGFR <30)",
                "Phụ nữ có thai nếu phác đồ kèm ribavirin",
                "Đồng nhiễm HBV chưa điều trị"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng", "Phối hợp amiodarone", "Phối hợp rifampin/carbamazepine/phenytoin/St. John's wort"],
            "tương_đối": [
                "Suy thận nặng (eGFR <30)",
                "Phụ nữ có thai nếu phác đồ kèm ribavirin",
                "Đồng nhiễm HBV chưa điều trị"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "pregnancy_lactation": {
            "fda_category": "B (không ribavirin); X nếu có ribavirin",
            "pregnancy_details": "An toàn tương đối nếu không dùng ribavirin; nếu kèm ribavirin thì chống chỉ định thai kỳ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết; cân nhắc ngừng cho bú.",
                "recommendation": "Đánh giá lợi ích/nguy cơ; tránh nếu kèm ribavirin."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Không cần chỉnh.",
            "severe": "Thận trọng ở Child-Pugh B/C; tham khảo chuyên khoa (thường cần ribavirin/xem xét kéo dài).",
            "notes": "Chuyển hóa gan; dữ liệu có ở xơ gan mất bù khi phối hợp ribavirin."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu; nhịp chậm nếu có amiodarone."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ.",
                "Theo dõi ECG.",
                "Thẩm tách loại bỏ một phần chất chuyển hóa sofosbuvir."
            ],
            "monitoring": "ECG, dấu hiệu sinh tồn, HCV RNA/ALT theo dõi đáp ứng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể với hoặc không.",
                "timing": "1 lần/ngày; tránh antacid gần thời điểm uống; tuân thủ đủ 12 tuần."
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "AASLD/IDSA HCV Guidance 2024",
                "Epclusa Prescribing Information"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "A - Hướng dẫn chuyên ngành và dữ liệu pha 3"
        }
    },
    "Tenofovir": {
        "group": "Infectious Disease - Antiviral (HBV, HIV)",
        "vietnamese_name": "Tenofovir disoproxil fumarate (TDF), Tenofovir alafenamide (TAF)",
        "administration": ["PO"],
        "indications": [
            "Viêm gan B mạn",
            "Điều trị hoặc dự phòng HIV (phối hợp ART) - ghi chú tương tác"
        ],
        "contraindications": [
            "Dị ứng",
            "Không dùng đơn trị ở HIV"
        ],
        "dosage": {
            "hbv_tdf": "300mg x 1 lần/ngày",
            "hbv_taf": "25mg x 1 lần/ngày (uống với thức ăn)",
            "notes": "Ưu tiên TAF nếu nguy cơ độc thận/loãng xương; TDF phổ biến và rẻ hơn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "TDF: 300mg mỗi 48 giờ; TAF: thận trọng, dữ liệu hạn chế",
            "under_30": "TDF: tránh nếu có thể; chạy thận: 300mg mỗi tuần sau lọc; TAF: tránh nếu CrCl <15 (không lọc)"
        },
        "side_effects": [
            "Suy thận, tăng creatinine",
            "Giảm mật độ xương (TDF)",
            "Buồn nôn, tiêu chảy",
            "Tăng men gan thoáng qua"
        ],
        "interactions": [
            "Thuốc độc thận (aminoglycoside, NSAID liều cao)",
            "Phối hợp ART (cobicistat, boosted PIs) có thể tăng nồng độ TDF",
            "P-gp inducers/inhibitors ảnh hưởng hấp thu TAF"
        ],
        "pregnancy": "B (TDF được khuyến cáo cho thai kỳ HBV/HIV)",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"renal": True, "bone": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["TDF vs TAF"]
        },
        "guideline_tags": [
            "AASLD 2024 HBV",
            "EASL 2023 HBV",
            "WHO HIV 2024"
        ],
        "mechanism_of_action": "Nucleotide analog (adenosine monophosphate) ức chế HBV DNA polymerase và HIV reverse transcriptase, gây kết thúc chuỗi.",
        "monitoring": [
            "Creatinine, eGFR mỗi 3-6 tháng",
            "Phosphat huyết, mật độ xương nếu dùng dài hạn",
            "HBV DNA, ALT",
            "HIV test trước khi đơn trị HBV (tránh kháng HIV)"
        ],
        "precautions": [
            "Điều chỉnh liều khi suy thận (đặc biệt TDF)",
            "Theo dõi mật độ xương ở bệnh nhân nguy cơ",
            "Nguy cơ bùng phát HBV khi ngừng thuốc",
            "Không đơn trị ở bệnh nhân có hoặc nguy cơ HIV chưa được kiểm soát"
        ],
        "pharmacokinetics": {
            "half_life": "TDF: ~17 giờ; TAF: ~17 giờ (tiền thuốc, nồng độ nội bào cao hơn)",
            "onset": "Giảm HBV DNA trong vài tuần",
            "duration": "Dùng hằng ngày, dài hạn",
            "protein_binding": "TDF: <1%; TAF: ~80%",
            "clearance": "Thận (lọc cầu thận và bài tiết ống thận)"
        },
        "storage": "Nhiệt độ phòng, khô ráo.",
        "black_box_warnings": "Bùng phát viêm gan sau ngừng; acid lactic/gan to nhiễm mỡ (nhóm NRTI).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc độc thận (aminoglycoside, amphotericin B, cisplatin, high-dose NSAID)",
                    "mechanism": "Cộng hưởng độc thận",
                    "effect": "Tăng nguy cơ suy thận",
                    "management": "Tránh nếu có thể; theo dõi creatinine/eGFR sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Boosted protease inhibitors hoặc cobicistat",
                    "mechanism": "Tăng nồng độ TDF qua ức chế P-gp",
                    "effect": "Tăng độc thận",
                    "management": "Cân nhắc TAF thay TDF; nếu dùng TDF, theo dõi thận."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": ["Dị ứng tenofovir"],
            "tương_đối": [
                "Suy thận hoặc dùng thuốc độc thận",
                "Nguy cơ loãng xương cao (ưu tiên TAF)",
                "Nghi ngờ/đồng nhiễm HIV chưa điều trị (không đơn trị)"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng tenofovir"],
            "tương_đối": [
                "Suy thận hoặc dùng thuốc độc thận",
                "Nguy cơ loãng xương cao (ưu tiên TAF)",
                "Nghi ngờ/đồng nhiễm HIV chưa điều trị (không đơn trị)"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Lọc máu loại bỏ TDF; TAF dữ liệu hạn chế."
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "TDF an toàn và khuyến cáo cho thai kỳ HBV/HIV; dữ liệu về TAF ít hơn nhưng có vẻ an toàn.",
            "lactation": {
                "safety": "TDF: Compatible",
                "details": "Bài tiết ít vào sữa; được dùng trong dự phòng lây truyền mẹ-con.",
                "recommendation": "Có thể dùng; theo dõi trẻ sơ sinh nếu kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Không cần chỉnh",
            "severe": "Thận trọng ở Child-Pugh C; ưu tiên theo dõi thận/xương",
            "notes": "Thải qua thận; suy gan ít ảnh hưởng dược động học."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu, suy thận, toan lactic (hiếm)"],
            "antidote": "Không có",
            "treatment": [
                "Ngừng thuốc, điều trị hỗ trợ",
                "Lọc máu loại bỏ TDF; TAF dữ liệu hạn chế"
            ],
            "monitoring": "Creatinine, phosphat, men gan, lactate"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "TDF: có thể với hoặc không; TAF: nên uống với thức ăn",
                "timing": "1 lần/ngày, giờ cố định"
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "AASLD 2024 HBV Guidance",
                "EASL 2023 HBV Guidelines",
                "WHO consolidated HIV guidelines 2024"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "A - Hướng dẫn chuyên ngành và dữ liệu thử nghiệm lâm sàng"
        }
    },

}

__all__ = ['HEPATITIS_ANTIVIRALS']
