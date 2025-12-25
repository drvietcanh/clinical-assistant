"""
HIV Antiretrovirals (ARVs) - core first-line agents
Includes NRTIs, NNRTIs, and INSTIs commonly used in Vietnam
"""

HIV_ARVS = {
    "Tenofovir disoproxil fumarate (TDF)": {
        "group": "Antiviral - Nucleotide reverse transcriptase inhibitor (NRTI)",
        "vietnamese_name": "Tenofovir disoproxil fumarate (TDF)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 kết hợp đa thuốc (backbone NRTI).",
            "Dự phòng trước phơi nhiễm (PrEP) khi kết hợp emtricitabine/lamivudine.",
            "Điều trị viêm gan B mạn (HBV) – ưu tiên khi đồng nhiễm HIV/HBV.",
        ],
        "contraindications": [
            "Dị ứng với tenofovir hoặc tá dược.",
            "CrCl <30 mL/phút nếu không thể theo dõi sát hoặc hiệu chỉnh liều.",
        ],
        "dosage": {
            "hiv_hbv": "300mg PO mỗi ngày, uống cùng hoặc không cùng thức ăn.",
            "prep": "300mg PO mỗi ngày (thường kết hợp emtricitabine).",
            "post_exposure_prophylaxis": "300mg PO mỗi ngày, kết hợp đa thuốc trong 28 ngày.",
            "notes": "Uống nhiều nước; theo dõi CrCl và phospho mỗi 3-6 tháng.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "300mg mỗi 48 giờ.",
            "under_30": "Tránh dùng nếu có lựa chọn khác; nếu bắt buộc: mỗi 72–96 giờ và theo dõi sát.",
        },
        "side_effects": [
            "Tăng creatinine, giảm phospho máu; hiếm gặp hội chứng Fanconi (độc thận ống lượn gần).",
            "Giảm mật độ xương (osteopenia/osteoporosis).",
            "Buồn nôn, mệt mỏi, đau đầu nhẹ.",
        ],
        "interactions": [
            "Thuốc độc thận (aminoglycoside, NSAID liều cao): tăng nguy cơ độc thận.",
            "Didanosine: tăng nồng độ didanosine, tăng độc tính; tránh nếu có thể.",
        ],
        "pregnancy": "B: có thể dùng trong thai kỳ khi lợi ích vượt nguy cơ; an toàn trong PrEP/điều trị HIV/HBV.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"renal": True, "bone": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["TDF vs TAF"]
        },
        "guideline_tags": [
            "WHO 2024 HIV/PrEP",
            "DHHS/CDC HIV 2024",
            "AASLD/EASL HBV 2023-2024"
        ],
        "mechanism_of_action": (
            "Tiền chất nucleotide adenosine monophosphate; phosphoryl hóa thành tenofovir diphosphate, "
            "ức chế cạnh tranh HIV-1 reverse transcriptase và gây kết thúc chuỗi DNA virus. "
            "Hoạt tính với HIV-1, HBV."
        ),
        "monitoring": [
            "Creatinine, eGFR/CrCl mỗi 3-6 tháng.",
            "Phospho, dấu hiệu hội chứng Fanconi (tiểu nhiều, yếu cơ, hạ phospho).",
            "HBV DNA/HIV RNA và CD4 theo phác đồ điều trị.",
        ],
        "precautions": [
            "Độc thận ống lượn gần: tránh phối hợp nhiều thuốc độc thận; uống đủ nước.",
            "Giảm mật độ xương: cân nhắc bổ sung calcium/vitamin D, đánh giá DEXA nếu nguy cơ cao.",
            "Bùng phát HBV khi ngừng: giảm dần hoặc chuyển thuốc chống HBV nếu đồng nhiễm.",
        ],
        "pharmacokinetics": {
            "half_life": "Kỳ tế bào ~60 giờ (dạng hoạt tính); huyết tương ~17 giờ.",
            "onset": "Vài giờ sau liều đầu.",
            "duration": "Dùng 1 lần/ngày nhờ tích lũy trong tế bào.",
            "protein_binding": "<1%.",
            "clearance": "Thải trừ chủ yếu qua thận (lọc cầu thận và bài tiết ống thận).",
        },
        "storage": "Bảo quản ở 20–25°C, giữ kín, tránh ẩm.",
        "black_box_warnings": (
            "Nguy cơ toan lactic và gan to nhiễm mỡ (hiếm, lớp NRTI). "
            "Bùng phát viêm gan B nặng khi ngừng thuốc ở bệnh nhân đồng nhiễm HBV."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Didanosine",
                    "mechanism": "TDF làm tăng nồng độ didanosine và độc tính ty thể.",
                    "effect": "Tăng nguy cơ viêm tụy, nhiễm toan lactic, độc tính thần kinh.",
                    "management": "Tránh phối hợp nếu có thể; nếu bắt buộc, giảm liều didanosine và theo dõi sát.",
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc độc thận (NSAID liều cao, aminoglycoside, amphotericin B)",
                    "mechanism": "Tác dụng cộng dồn độc thận.",
                    "effect": "Tăng nguy cơ suy thận, hội chứng Fanconi.",
                    "management": "Tránh phối hợp; nếu dùng, theo dõi creatinine, phospho chặt chẽ.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn với tenofovir."],
            "tương_đối": [
                "CrCl <30 mL/phút hoặc đang chạy thận (cân nhắc TAF hoặc thuốc khác).",
                "Loãng xương/giảm mật độ xương nặng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Được khuyến cáo trong phác đồ bầu bí (WHO/CDC).",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa thấp; WHO cho phép tiếp tục điều trị khi cho bú.",
                "recommendation": "Có thể tiếp tục nếu cần điều trị/PrEP; theo dõi chức năng thận mẹ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều; thận trọng nếu đồng thời suy thận.",
            "severe": "Dữ liệu hạn chế; theo dõi sát, ưu tiên thuốc khác nếu xơ gan mất bù.",
            "notes": "Chủ yếu thải qua thận, ít chuyển hóa gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng creatinine, hạ phospho, dấu hiệu Fanconi.",
                "Buồn nôn, đau bụng, mệt mỏi.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc, bù dịch, điều chỉnh điện giải (phospho, kali).",
                "Hỗ trợ thận; lọc máu loại bỏ một phần tenofovir.",
            ],
            "monitoring": "Creatinine, phospho, điện giải, nước tiểu, dấu hiệu lâm sàng.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Uống 1 lần/ngày, cố định giờ để duy trì nồng độ.",
            }
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on HIV Prevention, Testing, Treatment (2024)",
                "DHHS/CDC HIV Treatment Guidelines",
                "HBV treatment guidelines (AASLD/EASL)",
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Lamivudine (3TC)": {
        "group": "Antiviral - Nucleoside reverse transcriptase inhibitor (NRTI)",
        "vietnamese_name": "Lamivudine (3TC)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 kết hợp đa thuốc (backbone NRTI).",
            "Điều trị HBV mạn (đơn trị ít được ưu tiên do kháng sớm).",
        ],
        "contraindications": ["Dị ứng với lamivudine."],
        "dosage": {
            "hiv": "300mg PO mỗi ngày (hoặc 150mg x 2 lần/ngày).",
            "hbv": "100mg PO mỗi ngày (liều HBV riêng).",
            "notes": "Điều chỉnh liều theo chức năng thận; giữ liều đủ khi kết hợp với DTG/TDF.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "150mg mỗi ngày.",
            "under_30": "50–100mg mỗi ngày tùy CrCl; chạy thận: 25–50mg sau lọc.",
        },
        "side_effects": [
            "Thường nhẹ: nhức đầu, buồn nôn, mệt.",
            "Hiếm: toan lactic/gan to nhiễm mỡ (nhóm NRTI).",
        ],
        "interactions": [
            "Ít tương tác qua CYP; chú ý phối hợp với emtricitabine (trùng cơ chế, không dùng chung).",
        ],
        "pregnancy": "B: an toàn, được khuyến cáo trong thai kỳ.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["3TC vs FTC"]
        },
        "guideline_tags": [
            "WHO 2024 HIV",
            "DHHS/CDC HIV 2024",
            "AASLD/EASL HBV 2023-2024"
        ],
        "mechanism_of_action": (
            "Nucleoside analog cytidine; phosphoryl hóa thành 3TC-TP, "
            "ức chế cạnh tranh HIV-1 reverse transcriptase và kết thúc chuỗi DNA virus; "
            "hoạt tính với HBV."
        ),
        "monitoring": [
            "Creatinine/eGFR để chỉnh liều.",
            "Men gan (ALT/AST), HBV DNA nếu đồng nhiễm HBV.",
            "HIV RNA và CD4 theo phác đồ.",
        ],
        "precautions": [
            "Bùng phát HBV khi ngừng ở người đồng nhiễm HBV.",
            "Điều chỉnh liều theo thận để tránh tích lũy.",
        ],
        "pharmacokinetics": {
            "half_life": "10–15 giờ (huyết tương); 16–19 giờ (nội bào).",
            "onset": "Nhanh, nồng độ đỉnh 1–1.5 giờ.",
            "duration": "Dùng 1–2 lần/ngày.",
            "protein_binding": "<36%.",
            "clearance": "Thải trừ qua thận (bài tiết ống thận).",
        },
        "storage": "Bảo quản 20–25°C, tránh ẩm.",
        "black_box_warnings": (
            "Nguy cơ toan lactic và gan to nhiễm mỡ (hiếm, nhóm NRTI). "
            "Bùng phát viêm gan B khi ngừng thuốc ở bệnh nhân đồng nhiễm HBV."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Emtricitabine",
                    "mechanism": "Trùng cơ chế và cấu trúc (cytidine analog).",
                    "effect": "Không tăng hiệu quả, nguy cơ kháng chéo.",
                    "management": "Không phối hợp 3TC và FTC chung phác đồ.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn với lamivudine."],
            "tương_đối": [
                "Đồng nhiễm HBV: thận trọng khi ngừng, cần kế hoạch duy trì thuốc kháng HBV.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Được khuyến cáo trong phác đồ thai kỳ (WHO/CDC).",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa; WHO cho phép tiếp tục điều trị khi cho bú.",
                "recommendation": "Có thể tiếp tục; theo dõi chức năng thận và men gan.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Không cần chỉnh; theo dõi men gan nếu đồng nhiễm HBV.",
            "severe": "Dữ liệu hạn chế; theo dõi sát, ưu tiên duy trì để tránh bùng phát HBV.",
            "notes": "Chủ yếu thải trừ qua thận.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, mệt, hiếm gặp toan lactic."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc, điều trị hỗ trợ, theo dõi lactate và men gan.",
                "Chạy thận loại bỏ một phần lamivudine.",
            ],
            "monitoring": "Dấu hiệu lâm sàng, men gan, lactate, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Uống 1 lần/ngày (hoặc 2 lần/ngày 150mg).",
            }
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on HIV (2024)",
                "DHHS/CDC HIV Treatment Guidelines",
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Dolutegravir (DTG)": {
        "group": "Antiviral - Integrase strand transfer inhibitor (INSTI)",
        "vietnamese_name": "Dolutegravir (DTG)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 kết hợp đa thuốc (first-line ưu tiên).",
            "Phác đồ PEP khi cần INSTI (kết hợp TDF/3TC).",
        ],
        "contraindications": ["Dị ứng với dolutegravir."],
        "dosage": {
            "standard": "50mg PO mỗi ngày.",
            "with_rifampin": "50mg PO x 2 lần/ngày (do cảm ứng UGT/CYP3A).",
            "insti_resistance": "50mg PO x 2 lần/ngày khi nghi ngờ/kháng INSTI.",
            "notes": "Uống cách antacid/iron/calcium ít nhất 2 giờ trước hoặc 6 giờ sau.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh.",
            "under_30": "Không cần chỉnh; thận trọng nếu chạy thận (dữ liệu hạn chế).",
        },
        "side_effects": [
            "Mất ngủ, đau đầu (thường nhẹ).",
            "Tăng nhẹ creatinine do ức chế OCT2 (không giảm GFR thực).",
            "Tăng cân (nhẹ-moderate) khi dùng dài hạn.",
            "Hiếm: tăng men gan, phản ứng quá mẫn.",
        ],
        "interactions": [
            "Rifampin: giảm nồng độ DTG (cần tăng liều).",
            "Antacid chứa Al/Mg, sắt, calcium: giảm hấp thu (uống cách thời gian).",
            "Carbamazepine/phenytoin: cảm ứng, giảm nồng độ DTG.",
        ],
        "pregnancy": "Safe/Preferred: WHO khuyến cáo DTG cho phụ nữ mang thai và tuổi sinh sản.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO 2024 HIV",
            "DHHS/CDC HIV 2024",
            "IAS-USA 2024"
        ],
        "mechanism_of_action": (
            "Ức chế integrase strand transfer của HIV-1, ngăn tích hợp DNA virus vào DNA vật chủ, "
            "từ đó ngăn sao chép và sản sinh virion mới."
        ),
        "monitoring": [
            "HIV RNA, CD4 theo phác đồ.",
            "Creatinine (tăng nhẹ giả tạo), men gan nếu viêm gan đồng nhiễm.",
            "Tương tác thuốc khi dùng cùng rifampin/antacid.",
        ],
        "precautions": [
            "Tách liều với antacid/iron/calcium để tránh giảm hấp thu.",
            "Điều chỉnh liều khi dùng với rifampin hoặc các chất cảm ứng mạnh.",
            "Theo dõi tăng cân dài hạn.",
        ],
        "pharmacokinetics": {
            "half_life": "14 giờ.",
            "onset": "Nồng độ đỉnh ~2–3 giờ.",
            "duration": "Dùng 1 lần/ngày nhờ half-life dài.",
            "protein_binding": "~99%.",
            "clearance": "Chuyển hóa qua UGT1A1 (chủ yếu) và CYP3A.",
        },
        "storage": "Bảo quản 20–25°C, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng UGT1A1/CYP3A làm giảm nồng độ DTG.",
                    "effect": "Nguy cơ thất bại điều trị.",
                    "management": "Tăng liều DTG lên 50mg x 2 lần/ngày khi dùng cùng.",
                }
            ],
            "moderate": [
                {
                    "drug": "Antacid chứa Al/Mg, sắt, calcium",
                    "mechanism": "Tạo phức chelat, giảm hấp thu DTG.",
                    "effect": "Giảm AUC, nguy cơ thất bại điều trị.",
                    "management": "Uống DTG trước antacid 2 giờ hoặc sau 6 giờ.",
                },
                {
                    "drug": "Carbamazepine, phenytoin, phenobarbital",
                    "mechanism": "Cảm ứng UGT/CYP3A.",
                    "effect": "Giảm nồng độ DTG.",
                    "management": "Tránh nếu có thể; nếu dùng, cân nhắc tăng liều và theo dõi tải lượng virus.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn với dolutegravir."],
            "tương_đối": [
                "Đang dùng rifampin/cảm ứng mạnh (cần chỉnh liều).",
                "Suy gan trung bình-nặng: thận trọng, dữ liệu hạn chế.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified (preferred in pregnancy per WHO).",
            "pregnancy_details": "DTG được khuyến cáo do hiệu quả cao, khởi phát nhanh, ít tương tác.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết thấp vào sữa; có thể tiếp tục điều trị theo khuyến cáo WHO.",
                "recommendation": "Theo dõi trẻ, duy trì tuân thủ liều.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Thận trọng, theo dõi men gan.",
            "severe": "Dữ liệu hạn chế; cân nhắc INSTI khác/giảm liều và theo dõi sát.",
            "notes": "Chuyển hóa qua gan; tăng phơi nhiễm ở suy gan nặng chưa rõ.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu, mất ngủ; hiếm khi độc tính nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ, than hoạt nếu uống quá liều gần đây.",
                "Theo dõi ECG, dấu hiệu sinh tồn; DTG gắn protein cao, lọc máu ít hiệu quả.",
            ],
            "monitoring": "Dấu hiệu lâm sàng, men gan, tải lượng virus (sau ổn định).",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "1 lần/ngày; nếu dùng antacid/Fe/Ca, tách liều 2 giờ trước hoặc 6 giờ sau.",
            }
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on HIV (2024)",
                "DHHS/CDC HIV Treatment Guidelines",
                "IAS-USA HIV treatment recommendations",
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Efavirenz (EFV)": {
        "group": "Antiviral - Non-nucleoside reverse transcriptase inhibitor (NNRTI)",
        "vietnamese_name": "Efavirenz (EFV)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 kết hợp đa thuốc (phác đồ NNRTI cổ điển).",
        ],
        "contraindications": [
            "Dị ứng với efavirenz.",
            "Dùng đồng thời với midazolam, triazolam, ergot (tương tác CYP3A).",
        ],
        "dosage": {
            "standard": "600mg PO mỗi tối, uống lúc đói (giảm chóng mặt/mất ngủ).",
            "hepatic_mild": "Không cần chỉnh; theo dõi men gan.",
            "notes": "Tránh uống cùng bữa nhiều mỡ (tăng hấp thu và tác dụng phụ thần kinh).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh (chuyển hóa gan).",
            "30_60": "Không cần chỉnh.",
            "under_30": "Không cần chỉnh.",
        },
        "side_effects": [
            "Chóng mặt, mất ngủ, ác mộng, thay đổi tâm trạng (thường giảm sau 2–4 tuần).",
            "Phát ban, có thể hội chứng Stevens-Johnson (hiếm).",
            "Tăng men gan, tăng lipid nhẹ.",
        ],
        "interactions": [
            "Cảm ứng và ức chế CYP3A4/CYP2B6 (phức tạp): ảnh hưởng nhiều thuốc (rifampin, azole, statin, CCB, thuốc an thần).",
        ],
        "pregnancy": "Khuyến cáo tránh trong quý 1 do dữ liệu dị tật ống thần kinh cũ; hiện có thể dùng nếu lợi ích vượt trội (WHO cho phép).",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "neuropsychiatric": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO 2024 HIV",
            "DHHS/CDC HIV 2024"
        ],
        "mechanism_of_action": (
            "Gắn vào vị trí allosteric của HIV-1 reverse transcriptase, "
            "gây biến đổi cấu hình và ức chế sao chép DNA virus (không cạnh tranh nucleoside)."
        ),
        "monitoring": [
            "HIV RNA, CD4 theo phác đồ.",
            "Men gan, lipid máu.",
            "Triệu chứng thần kinh/tâm thần trong 2–4 tuần đầu.",
            "Phát ban/Stevens-Johnson (hiếm).",
        ],
        "precautions": [
            "Dùng buổi tối, lúc đói để giảm tác dụng phụ thần kinh.",
            "Thận trọng ở bệnh nhân rối loạn tâm thần, động kinh (có thể làm nặng).",
            "Tránh phối hợp thuốc chuyển hóa qua CYP3A/CYP2B6 có cửa sổ hẹp trừ khi giám sát.",
        ],
        "pharmacokinetics": {
            "half_life": "40–55 giờ (dài, cho phép 1 lần/ngày).",
            "onset": "Nồng độ đỉnh ~3–5 giờ.",
            "duration": "1 lần/ngày; tác dụng phụ thần kinh thường giảm sau 2–4 tuần.",
            "protein_binding": "~99%.",
            "clearance": "Chuyển hóa gan (CYP2B6, CYP3A4); bài tiết qua phân/nhẹ qua thận.",
        },
        "storage": "Bảo quản 20–25°C, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Midazolam, triazolam, ergot derivatives",
                    "mechanism": "Ức chế/ cảm ứng CYP3A gây thay đổi nồng độ lớn.",
                    "effect": "Nguy cơ độc tính hoặc giảm hiệu lực thuốc nền.",
                    "management": "Chống chỉ định phối hợp.",
                }
            ],
            "moderate": [
                {
                    "drug": "Rifampin, rifabutin",
                    "mechanism": "Cảm ứng CYP; giảm nồng độ EFV.",
                    "effect": "Nguy cơ thất bại điều trị.",
                    "management": "Cân nhắc tăng liều EFV lên 800mg với rifampin; theo dõi tải lượng virus.",
                },
                {
                    "drug": "Voriconazole",
                    "mechanism": "EFV cảm ứng CYP, giảm nồng độ voriconazole; voriconazole ức chế CYP, tăng EFV.",
                    "effect": "Giảm hiệu lực voriconazole, tăng độc tính EFV.",
                    "management": "Tránh phối hợp hoặc điều chỉnh liều theo khuyến cáo (tăng voriconazole, giảm EFV).",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với efavirenz.",
                "Dùng cùng midazolam, triazolam, ergot alkaloids.",
            ],
            "tương_đối": [
                "Tiền sử rối loạn tâm thần, động kinh.",
                "Bệnh gan mạn (HBV/HCV đồng nhiễm) – theo dõi men gan.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D (cũ); hiện WHO cho phép nếu lợi ích vượt trội sau tư vấn.",
            "pregnancy_details": "Tránh quý 1 nếu có lựa chọn khác; có thể dùng từ quý 2 trở đi hoặc khi lợi ích vượt nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa; WHO cho phép tiếp tục điều trị khi cho bú.",
                "recommendation": "Theo dõi trẻ về an thần/phát ban; ưu tiên phác đồ INSTI nếu sẵn có.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh, theo dõi men gan.",
            "moderate": "Thận trọng, theo dõi men gan chặt; cân nhắc thuốc khác nếu ALT/AST cao.",
            "severe": "Tránh nếu xơ gan Child-Pugh B/C do dữ liệu hạn chế và nguy cơ tích lũy.",
            "notes": "Chuyển hóa gan mạnh qua CYP2B6/3A4.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng tác dụng phụ thần kinh (ảo giác, lú lẫn), chóng mặt nặng.",
                "Buồn nôn, nôn.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Than hoạt nếu uống quá liều sớm.",
                "Hỗ trợ triệu chứng, theo dõi thần kinh và men gan.",
            ],
            "monitoring": "Dấu hiệu thần kinh, men gan, ECG nếu nguy cơ kéo dài QT (hiếm).",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống lúc đói hoặc bữa ít chất béo để giảm tác dụng phụ thần kinh.",
                "timing": "Uống buổi tối trước khi ngủ để hạn chế chóng mặt/ác mộng.",
            }
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on HIV (2024)",
                "DHHS/CDC HIV Treatment Guidelines",
                "IAS-USA HIV treatment recommendations",
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Emtricitabine (FTC)": {
        "group": "Antiviral - Nucleoside reverse transcriptase inhibitor (NRTI)",
        "vietnamese_name": "Emtricitabine (FTC)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 kết hợp đa thuốc (backbone NRTI).",
            "Dự phòng trước phơi nhiễm (PrEP) khi kết hợp tenofovir (TDF hoặc TAF).",
            "Hỗ trợ điều trị HBV (hoạt tính với HBV, nhưng không dùng đơn trị).",
        ],
        "contraindications": ["Dị ứng với emtricitabine."],
        "dosage": {
            "hiv": "200mg PO mỗi ngày.",
            "prep": "200mg PO mỗi ngày khi dùng với TDF/TAF.",
            "notes": "Không dùng chung với lamivudine (3TC).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "200mg mỗi 48 giờ.",
            "under_30": "Cân nhắc giảm còn 200mg mỗi 72–96 giờ; chạy thận: sau lọc.",
        },
        "side_effects": [
            "Nhức đầu, mệt, buồn nôn (nhẹ).",
            "Tăng sắc tố lòng bàn tay/bàn chân (hiếm).",
            "Hiếm: toan lactic/gan to nhiễm mỡ.",
        ],
        "interactions": [
            "Ít qua CYP; tránh phối hợp 3TC (trùng cơ chế).",
        ],
        "pregnancy": "B: an toàn, khuyến cáo trong thai kỳ.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["FTC vs 3TC"]
        },
        "guideline_tags": [
            "WHO 2024 HIV/PrEP",
            "DHHS/CDC HIV 2024"
        ],
        "mechanism_of_action": (
            "Cytidine analog; phosphoryl hóa thành FTC-TP, ức chế cạnh tranh reverse transcriptase HIV-1 "
            "và kết thúc chuỗi DNA; có hoạt tính với HBV."
        ),
        "monitoring": [
            "Creatinine/eGFR để chỉnh liều.",
            "Men gan, HBV DNA nếu đồng nhiễm HBV.",
            "HIV RNA và CD4 theo phác đồ.",
        ],
        "precautions": [
            "Không phối hợp với lamivudine.",
            "Nguy cơ bùng phát HBV khi ngừng ở bệnh nhân đồng nhiễm.",
        ],
        "pharmacokinetics": {
            "half_life": "10 giờ (huyết tương), 39 giờ (nội bào).",
            "onset": "Cmax ~1–2 giờ.",
            "duration": "Dùng 1 lần/ngày.",
            "protein_binding": "<4%.",
            "clearance": "Thận (bài tiết ống thận).",
        },
        "storage": "20–25°C, tránh ẩm.",
        "black_box_warnings": (
            "Nguy cơ toan lactic/gan to nhiễm mỡ (hiếm, nhóm NRTI). "
            "Bùng phát HBV khi ngừng ở bệnh nhân đồng nhiễm HBV."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Lamivudine",
                    "mechanism": "Trùng cơ chế (cytidine analog).",
                    "effect": "Không tăng hiệu quả, nguy cơ kháng chéo.",
                    "management": "Không phối hợp FTC và 3TC chung phác đồ.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn với emtricitabine."],
            "tương_đối": [
                "Đồng nhiễm HBV: thận trọng khi ngừng, cần kế hoạch duy trì kháng HBV.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Được khuyến cáo trong phác đồ thai kỳ (WHO/CDC).",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa thấp; WHO cho phép tiếp tục điều trị khi cho bú.",
                "recommendation": "Có thể tiếp tục; theo dõi chức năng thận/men gan.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Không cần chỉnh; theo dõi men gan nếu đồng nhiễm HBV.",
            "severe": "Dữ liệu hạn chế; theo dõi sát.",
            "notes": "Chủ yếu thải trừ qua thận.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, mệt; hiếm toan lactic."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc, hỗ trợ triệu chứng.",
                "Chạy thận loại bỏ một phần FTC.",
            ],
            "monitoring": "Men gan, lactate, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "1 lần/ngày; dùng cố định với nền NRTI/INSTI.",
            }
        },
        "references": {
            "primary_sources": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV Treatment Guidelines"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Tenofovir alafenamide (TAF)": {
        "group": "Antiviral - Nucleotide reverse transcriptase inhibitor (NRTI)",
        "vietnamese_name": "Tenofovir alafenamide (TAF)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 (kết hợp đa thuốc).",
            "Điều trị HBV mạn (liều HBV riêng).",
            "PrEP khi kết hợp FTC (không cho receptive vaginal sex theo nhãn cũ; cập nhật cân nhắc theo guideline mới nếu có).",
        ],
        "contraindications": ["Dị ứng với TAF."],
        "dosage": {
            "hiv": "10–25mg PO mỗi ngày tùy nền (với booster hoặc không).",
            "hbv": "25mg PO mỗi ngày, uống với thức ăn.",
            "notes": "Uống với thức ăn; không dùng đơn trị HIV.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; theo dõi thận.",
            "under_30": "Tránh nếu CrCl <15 không lọc; chạy thận: dữ liệu hạn chế.",
        },
        "side_effects": [
            "Buồn nôn, đau đầu.",
            "Ít ảnh hưởng mật độ xương/thận hơn TDF, nhưng vẫn cần theo dõi.",
        ],
        "interactions": [
            "P-gp inducers (rifampin, carbamazepine) giảm nồng độ.",
            "Boosted PIs/cobicistat có thể tăng phơi nhiễm TAF (theo nhãn).",
        ],
        "pregnancy": "Có thể dùng; dữ liệu đang tăng, ưu tiên TDF nếu cần bằng chứng lâu dài.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"renal": True, "bone": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["TDF vs TAF"]
        },
        "guideline_tags": [
            "WHO 2024 HIV/PrEP",
            "DHHS/CDC HIV 2024",
            "AASLD/EASL HBV 2024"
        ],
        "mechanism_of_action": (
            "Tiền chất tenofovir thế hệ mới, được hoạt hóa chủ yếu trong tế bào lympho/gan, "
            "ức chế cạnh tranh reverse transcriptase HIV-1 và HBV, gây kết thúc chuỗi DNA."
        ),
        "monitoring": [
            "Creatinine/eGFR, phospho (ít hơn TDF nhưng vẫn cần).",
            "HBV DNA, ALT nếu điều trị HBV.",
            "HIV RNA, CD4 theo phác đồ.",
        ],
        "precautions": [
            "Không dùng đơn trị HIV.",
            "Tránh cảm ứng mạnh P-gp (rifampin, carbamazepine).",
            "Theo dõi thận và xương nếu dùng kéo dài.",
            "Bùng phát HBV khi ngừng ở người đồng nhiễm.",
        ],
        "pharmacokinetics": {
            "half_life": "~0.5 giờ (huyết tương tiền thuốc); chất chuyển hóa nội bào kéo dài.",
            "onset": "Nồng độ nội bào đạt đỉnh trong vài giờ.",
            "duration": "1 lần/ngày.",
            "protein_binding": "~80%.",
            "clearance": "Gan (esterase, cathepsin A); thận thải trừ tenofovir mức thấp hơn TDF.",
        },
        "storage": "Bảo quản 20–25°C, tránh ẩm.",
        "black_box_warnings": "Bùng phát HBV khi ngừng; toan lactic/gan to nhiễm mỡ (hiếm, nhóm NRTI).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                    "mechanism": "Cảm ứng P-gp làm giảm hấp thu/ phơi nhiễm TAF.",
                    "effect": "Giảm hiệu quả điều trị.",
                    "management": "Tránh phối hợp.",
                }
            ],
            "moderate": [
                {
                    "drug": "Boosted PIs/cobicistat",
                    "mechanism": "Ức chế P-gp tăng phơi nhiễm TAF.",
                    "effect": "Tăng nồng độ tenofovir; có thể tăng độc tính thận.",
                    "management": "Theo dõi chức năng thận; cân nhắc nền không booster nếu phù hợp.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn TAF."],
            "tương_đối": [
                "Suy thận nặng không lọc.",
                "Đồng nhiễm HBV: thận trọng khi ngừng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified; kinh nghiệm hạn chế hơn TDF",
            "pregnancy_details": "Có thể cân nhắc; TDF vẫn là chuẩn có dữ liệu nhiều.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế; theo dõi trẻ.",
                "recommendation": "Cân nhắc lợi ích/nguy cơ; TDF có dữ liệu nhiều hơn.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Thận trọng.",
            "severe": "Dữ liệu hạn chế; theo dõi sát.",
            "notes": "Thải chủ yếu qua thận sau chuyển hóa; suy gan có thể tăng phơi nhiễm tiền thuốc.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu; lý thuyết độc thận/xương hiếm."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ; than hoạt nếu mới uống.",
                "Theo dõi thận, điện giải.",
            ],
            "monitoring": "Creatinine, phospho, men gan.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để tối ưu hấp thu.",
                "timing": "1 lần/ngày; dùng cố định với nền ART.",
            }
        },
        "references": {
            "primary_sources": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV Guidelines",
                "AASLD/EASL HBV 2024"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Bictegravir (BIC)": {
        "group": "Antiviral - Integrase strand transfer inhibitor (INSTI)",
        "vietnamese_name": "Bictegravir (BIC)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 first-line (trong FDC bictegravir/emtricitabine/tenofovir alafenamide).",
        ],
        "contraindications": [
            "Dị ứng với bictegravir.",
            "Dùng đồng thời rifampin (giảm mạnh nồng độ).",
        ],
        "dosage": {
            "standard": "50mg PO mỗi ngày (thường trong FDC).",
            "notes": "Tránh rifampin; antacid/Fe/Ca cần tách liều.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh.",
            "under_30": "Tránh nếu eGFR <30 khi dùng chung TAF/FTC (theo nhãn FDC).",
        },
        "side_effects": [
            "Buồn nôn, nhức đầu.",
            "Tăng nhẹ creatinine (ức chế OCT2, không giảm GFR thực).",
            "Tăng cân nhẹ.",
        ],
        "interactions": [
            "Rifampin (chống chỉ định), rifabutin (cân nhắc).",
            "Antacid/Fe/Ca: giảm hấp thu, cần tách liều.",
            "Carbamazepine/phenytoin: cảm ứng, giảm nồng độ.",
        ],
        "pregnancy": "Có thể dùng; dữ liệu đang tăng, DTG có nhiều bằng chứng hơn.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO 2024 HIV",
            "DHHS/CDC HIV 2024",
            "IAS-USA 2024"
        ],
        "mechanism_of_action": (
            "Ức chế integrase strand transfer của HIV-1, ngăn tích hợp DNA virus vào DNA vật chủ."
        ),
        "monitoring": [
            "HIV RNA, CD4.",
            "Creatinine (tăng nhẹ giả tạo).",
            "Men gan nếu đồng nhiễm HBV/HCV.",
        ],
        "precautions": [
            "Tách liều với antacid/Fe/Ca (uống BIC 2 giờ trước hoặc 6 giờ sau).",
            "Tránh rifampin; thận trọng với rifabutin/rifapentine.",
            "Theo dõi tăng cân dài hạn.",
        ],
        "pharmacokinetics": {
            "half_life": "17 giờ.",
            "onset": "Cmax ~2–4 giờ.",
            "duration": "1 lần/ngày.",
            "protein_binding": "~99%.",
            "clearance": "UGT1A1/CYP3A.",
        },
        "storage": "Bảo quản 20–25°C, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng UGT/CYP mạnh, giảm AUC >75%.",
                    "effect": "Thất bại điều trị.",
                    "management": "CHỐNG CHỈ ĐỊNH.",
                }
            ],
            "moderate": [
                {
                    "drug": "Antacid/Fe/Ca",
                    "mechanism": "Tạo phức chelat, giảm hấp thu.",
                    "effect": "Giảm AUC.",
                    "management": "Uống BIC 2h trước hoặc 6h sau; hoặc dùng cùng với bữa ăn chứa Fe/Ca được phép theo nhãn.",
                },
                {
                    "drug": "Carbamazepine/phenytoin",
                    "mechanism": "Cảm ứng UGT/CYP.",
                    "effect": "Giảm nồng độ BIC.",
                    "management": "Tránh nếu có thể; chọn INSTI khác/điều chỉnh nền.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn", "Rifampin phối hợp"],
            "tương_đối": [
                "Dùng thuốc cảm ứng mạnh khác (carbamazepine, phenytoin).",
                "Suy gan trung bình-nặng (dữ liệu hạn chế).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified; dữ liệu đang tăng",
            "pregnancy_details": "Có thể cân nhắc; DTG có bằng chứng rộng hơn.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Đánh giá lợi ích/nguy cơ; theo dõi trẻ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Thận trọng.",
            "severe": "Dữ liệu hạn chế; cân nhắc tránh.",
            "notes": "Chuyển hóa qua gan UGT1A1/CYP3A.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu; độc tính nặng hiếm."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ; than hoạt nếu mới uống.",
            ],
            "monitoring": "Dấu hiệu sinh tồn, men gan.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể với hoặc không.",
                "timing": "1 lần/ngày; tách antacid/Fe/Ca nếu dạng chelat.",
            }
        },
        "references": {
            "primary_sources": [
                "WHO 2024 HIV",
                "DHHS/CDC HIV Treatment Guidelines",
                "IAS-USA 2024"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Cobicistat (COBI)": {
        "group": "Pharmacokinetic booster (CYP3A inhibitor)",
        "vietnamese_name": "Cobicistat",
        "administration": ["PO"],
        "indications": [
            "Tăng cường nồng độ ARV chuyển hóa qua CYP3A (elvitegravir, atazanavir, darunavir) trong các FDC/nền có COBI.",
        ],
        "contraindications": [
            "Dị ứng với cobicistat.",
            "Dùng với thuốc phụ thuộc CYP3A để thanh thải có cửa sổ hẹp (ví dụ amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO).",
        ],
        "dosage": {
            "standard": "150mg PO mỗi ngày (trong FDC hoặc viên rời).",
            "notes": "Dùng cùng thuốc đích (PI/INSTI) và thức ăn nếu theo nhãn của thuốc đích.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; theo dõi creatinine (tăng giả do ức chế OCT2).",
            "under_30": "Theo nhãn FDC: tránh dùng nếu eGFR <30 (do TAF/FTC kèm).",
        },
        "side_effects": [
            "Buồn nôn, tiêu chảy.",
            "Tăng nhẹ creatinine (ức chế vận chuyển ống thận, không giảm GFR thực).",
            "Vàng da nhẹ nếu phối hợp atazanavir (tăng bilirubin gián tiếp).",
        ],
        "interactions": [
            "Ức chế mạnh CYP3A, P-gp, OATP1B1/3: nhiều tương tác thuốc.",
        ],
        "pregnancy": "Tránh dùng trong thai kỳ (nồng độ giảm, ưu tiên ritonavir hoặc không booster).",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "DHHS/CDC HIV 2024",
            "WHO 2024 HIV"
        ],
        "mechanism_of_action": (
            "Ức chế CYP3A và P-gp, làm tăng phơi nhiễm thuốc ARV mục tiêu (PI/INSTI) mà không có "
            "hoạt tính kháng virus độc lập."
        ),
        "monitoring": [
            "Creatinine (tăng giả).",
            "Men gan, bilirubin nếu dùng với atazanavir.",
            "Theo dõi tương tác thuốc (CYP3A/P-gp).",
        ],
        "precautions": [
            "Rà soát tương tác CYP3A/P-gp/OATP trước kê đơn.",
            "Tránh dùng với thuốc cửa sổ hẹp phụ thuộc CYP3A để thải trừ.",
            "Tăng creatinine giả: giải thích cho bệnh nhân, không phản ánh suy thận thật nếu eGFR ổn định.",
        ],
        "pharmacokinetics": {
            "half_life": "3–4 giờ.",
            "onset": "Cmax ~1–2 giờ.",
            "duration": "Tác dụng ức chế CYP kéo dài đủ cho liều ngày 1 lần.",
            "protein_binding": "~98%.",
            "clearance": "Gan (CYP3A).",
        },
        "storage": "20–25°C, khô ráo.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO",
                    "mechanism": "Ức chế CYP3A mạnh làm tăng phơi nhiễm thuốc cửa sổ hẹp.",
                    "effect": "Nguy cơ độc tính nặng.",
                    "management": "CHỐNG CHỈ ĐỊNH.",
                }
            ],
            "moderate": [
                {
                    "drug": "Statins (simvastatin, lovastatin)",
                    "mechanism": "Ức chế CYP3A tăng AUC statin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân.",
                    "management": "Tránh; dùng pravastatin/rosuvastatin liều thấp và theo dõi.",
                },
                {
                    "drug": "DOACs (apixaban, rivaroxaban)",
                    "mechanism": "Ức chế CYP3A/P-gp tăng nồng độ DOAC.",
                    "effect": "Tăng chảy máu.",
                    "management": "Tránh hoặc giảm liều theo khuyến cáo, theo dõi chảy máu.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn COBI.",
                "Phối hợp thuốc cửa sổ hẹp phụ thuộc CYP3A (amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO).",
            ],
            "tương_đối": [
                "Suy gan trung bình-nặng.",
                "Suy thận <30 (theo FDC có TAF/FTC).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified",
            "pregnancy_details": "Không ưu tiên trong thai kỳ do nồng độ giảm; chọn ritonavir hoặc phác đồ không cần booster.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Đánh giá lợi ích/nguy cơ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh nhưng theo dõi men gan.",
            "moderate": "Thận trọng.",
            "severe": "Tránh (dữ liệu hạn chế).",
            "notes": "Chuyển hóa qua gan; ức chế CYP3A mạnh.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, tăng bilirubin (nếu dùng với ATV), ức chế quá mức CYP3A."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ, than hoạt nếu mới uống.",
                "Theo dõi ECG, men gan, dấu hiệu độc tính thuốc phối hợp.",
            ],
            "monitoring": "Dấu hiệu sinh tồn, men gan, tương tác thuốc kèm.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Theo thuốc đích (đa số PI cần thức ăn).",
                "timing": "1 lần/ngày cùng thuốc đích.",
            }
        },
        "references": {
            "primary_sources": [
                "DHHS/CDC HIV Treatment Guidelines",
                "WHO 2024 HIV"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Ritonavir (low-dose booster)": {
        "group": "Pharmacokinetic booster (CYP3A inhibitor; PI at high dose)",
        "vietnamese_name": "Ritonavir (liều thấp tăng cường PI)",
        "administration": ["PO"],
        "indications": [
            "Tăng cường nồng độ protease inhibitors (lopinavir, atazanavir, darunavir…).",
        ],
        "contraindications": [
            "Dị ứng ritonavir.",
            "Dùng với thuốc phụ thuộc CYP3A cửa sổ hẹp (amiodarone, ergot, alfuzosin, triazolam/midazolam PO…).",
        ],
        "dosage": {
            "booster": "100mg PO 1–2 lần/ngày tùy PI.",
            "notes": "Uống với thức ăn để giảm khó tiêu; không dùng như đơn trị ART.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh.",
            "under_30": "Không cần chỉnh; theo dõi nếu kèm TDF.",
        },
        "side_effects": [
            "Buồn nôn, tiêu chảy, vị khó chịu.",
            "Tăng triglycerid/cholesterol.",
            "Tăng men gan.",
            "Thay đổi mỡ phân bố (dùng lâu, liều PI đầy đủ).",
        ],
        "interactions": [
            "Ức chế mạnh CYP3A/CYP2D6/P-gp → rất nhiều tương tác.",
        ],
        "pregnancy": "Có thể dùng; được kinh nghiệm lâu dài hơn COBI.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "metabolic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "DHHS/CDC HIV 2024",
            "WHO 2024 HIV"
        ],
        "mechanism_of_action": (
            "Ức chế CYP3A/CYP2D6 và P-gp, tăng phơi nhiễm PI mục tiêu; liều thấp không nhằm hoạt tính kháng virus chính."
        ),
        "monitoring": [
            "Men gan, lipid (TG/LDL).",
            "Dấu hiệu tương tác thuốc (chảy máu với DOAC, an thần với benzo...).",
            "Glucose nếu dùng dài hạn (nguy cơ đề kháng insulin).",
        ],
        "precautions": [
            "Rà soát tương tác CYP3A/CYP2D6/P-gp kỹ trước kê đơn.",
            "Uống với thức ăn để giảm khó chịu tiêu hóa.",
            "Thận trọng bệnh gan, tăng TG nền.",
        ],
        "pharmacokinetics": {
            "half_life": "3–5 giờ (ức chế CYP kéo dài hơn).",
            "onset": "Cmax ~2–4 giờ.",
            "duration": "Dùng 1–2 lần/ngày tùy PI.",
            "protein_binding": "~98–99%.",
            "clearance": "Gan (CYP3A/2D6).",
        },
        "storage": "Viên: 20–25°C; dung dịch cần bảo quản lạnh sau mở (theo nhãn).",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO",
                    "mechanism": "Ức chế CYP3A mạnh tăng phơi nhiễm.",
                    "effect": "Nguy cơ độc tính nặng.",
                    "management": "CHỐNG CHỈ ĐỊNH.",
                }
            ],
            "moderate": [
                {
                    "drug": "Statins (simvastatin, lovastatin)",
                    "mechanism": "Ức chế CYP3A tăng AUC statin.",
                    "effect": "Nguy cơ tiêu cơ vân.",
                    "management": "Tránh; dùng pravastatin/rosuvastatin liều thấp.",
                },
                {
                    "drug": "DOACs (apixaban, rivaroxaban)",
                    "mechanism": "Ức chế CYP3A/P-gp.",
                    "effect": "Tăng chảy máu.",
                    "management": "Tránh hoặc giảm liều/giám sát chặt.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn ritonavir.",
                "Phối hợp thuốc cửa sổ hẹp phụ thuộc CYP3A.",
            ],
            "tương_đối": [
                "Bệnh gan mạn, tăng TG/LDL nặng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng liều booster; đã có kinh nghiệm trong thai kỳ hơn COBI.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết thấp vào sữa; dữ liệu hạn chế.",
                "recommendation": "Theo dõi trẻ; cân nhắc lợi ích/nguy cơ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, có thể không cần chỉnh.",
            "moderate": "Thận trọng, theo dõi men gan.",
            "severe": "Tránh nếu có thể.",
            "notes": "Chuyển hóa qua gan; tăng phơi nhiễm ở suy gan.",
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, tiêu chảy, chóng mặt; lý thuyết kéo dài QT/PR ở liều cao."],
            "antidote": "Không có.",
            "treatment": [
                "Than hoạt nếu uống gần đây.",
                "Theo dõi ECG, điện giải, dấu hiệu sinh tồn.",
            ],
            "monitoring": "ECG, men gan, glucose, lipid.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm rối loạn tiêu hóa.",
                "timing": "1–2 lần/ngày tùy PI nền.",
            }
        },
        "references": {
            "primary_sources": [
                "DHHS/CDC HIV Treatment Guidelines",
                "WHO 2024 HIV"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based",
        },
    },

    "Tenofovir disoproxil fumarate/Emtricitabine (TDF/FTC)": {
        "group": "Antiviral - NRTI fixed-dose combination",
        "vietnamese_name": "TDF/FTC (Truvada và tương đương)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 (backbone NRTI) khi kết hợp INSTI/NNRTI/PI.",
            "Dự phòng trước phơi nhiễm (PrEP).",
            "Hỗ trợ phòng lây truyền mẹ-con khi phối hợp phác đồ đầy đủ."
        ],
        "contraindications": [
            "Dị ứng với bất kỳ thành phần nào.",
            "CrCl <30 mL/phút (trừ khi có giám sát rất sát/điều chỉnh đặc biệt)."
        ],
        "dosage": {
            "hiv": "TDF 300mg + FTC 200mg PO mỗi ngày.",
            "prep": "TDF 300mg + FTC 200mg PO mỗi ngày.",
            "notes": "Uống cố định giờ; uống với nước, có thể cùng hoặc không cùng thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Uống mỗi 48 giờ.",
            "under_30": "Tránh; chạy thận: mỗi 7 ngày sau lọc (chỉ khi buộc phải dùng, theo guideline)."
        },
        "side_effects": [
            "Buồn nôn, nhức đầu, mệt.",
            "Tăng creatinine, giảm phospho (TDF).",
            "Giảm mật độ xương (TDF)."
        ],
        "interactions": [
            "Thuốc độc thận (aminoglycoside, NSAID liều cao): tăng độc thận.",
            "Boosted PI/cobicistat: tăng phơi nhiễm TDF → tăng nguy cơ thận/xương."
        ],
        "pregnancy": "TDF/FTC được khuyến cáo an toàn trong thai kỳ và PrEP.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"renal": True, "bone": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["TDF vs TAF"]
        },
        "guideline_tags": [
            "WHO 2024 HIV/PrEP",
            "DHHS/CDC HIV 2024"
        ],
        "mechanism_of_action": (
            "Kết hợp nucleotide (TDF) và nucleoside (FTC) ức chế cạnh tranh HIV reverse transcriptase, "
            "gây kết thúc chuỗi DNA virus; có hoạt tính với HBV."
        ),
        "monitoring": [
            "Creatinine/eGFR, phospho mỗi 3–6 tháng.",
            "HBV DNA/ALT nếu đồng nhiễm.",
            "HIV RNA, CD4; xét nghiệm HIV định kỳ trong PrEP."
        ],
        "precautions": [
            "Không phối hợp thêm 3TC/FTC khác (trùng cơ chế).",
            "Theo dõi thận/xương; cân nhắc TAF/FTC nếu nguy cơ cao.",
            "Bùng phát HBV khi ngừng ở người đồng nhiễm."
        ],
        "pharmacokinetics": {
            "half_life": "TDF ~17h huyết tương; FTC 10h huyết tương, 39h nội bào.",
            "onset": "Nồng độ đỉnh 1–2h.",
            "duration": "1 lần/ngày.",
            "protein_binding": "TDF <1%; FTC <4%.",
            "clearance": "Thận (lọc cầu thận/bài tiết ống thận)."
        },
        "storage": "20–25°C, khô ráo.",
        "black_box_warnings": "Toan lactic/gan to nhiễm mỡ (nhóm NRTI, hiếm); bùng phát HBV khi ngừng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc độc thận (aminoglycoside, amphotericin B, cisplatin, high-dose NSAID)",
                    "mechanism": "Cộng hưởng độc thận.",
                    "effect": "Tăng nguy cơ suy thận.",
                    "management": "Tránh nếu có thể; theo dõi creatinine/eGFR sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Boosted PI/cobicistat",
                    "mechanism": "Tăng phơi nhiễm TDF qua ức chế P-gp.",
                    "effect": "Tăng độc thận/xương.",
                    "management": "Theo dõi thận; cân nhắc TAF/FTC nếu phù hợp."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn thành phần."],
            "tương_đối": [
                "CrCl <30 mL/phút hoặc chạy thận (chỉ dùng nếu buộc phải và theo guideline).",
                "Nguy cơ loãng xương cao."
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B (TDF, FTC)",
            "pregnancy_details": "Khuyến cáo dùng trong thai kỳ (điều trị/PrEP).",
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết ít vào sữa; được phép tiếp tục.",
                "recommendation": "Theo dõi trẻ sơ sinh nếu dùng kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Không cần chỉnh.",
            "severe": "Thận trọng; dữ liệu hạn chế.",
            "notes": "Thải qua thận; suy gan ít ảnh hưởng PK."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu; lý thuyết độc thận/xương."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ; theo dõi điện giải.",
                "Lọc máu loại bỏ TDF/FTC một phần."
            ],
            "monitoring": "Creatinine, phospho, men gan, lactate."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể với hoặc không.",
                "timing": "1 lần/ngày; PrEP cần tuân thủ liên tục."
            }
        },
        "references": {
            "primary_sources": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV Treatment Guidelines"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based"
        }
    },

    "Tenofovir alafenamide/Emtricitabine (TAF/FTC)": {
        "group": "Antiviral - NRTI fixed-dose combination",
        "vietnamese_name": "TAF/FTC (Descovy và tương đương)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 (backbone NRTI) khi kết hợp INSTI/NNRTI/PI.",
            "PrEP (không cho receptive vaginal sex theo nhãn cũ; theo dõi cập nhật guideline)."
        ],
        "contraindications": [
            "Dị ứng với thành phần.",
            "eGFR <30 mL/phút (theo nhãn)."
        ],
        "dosage": {
            "hiv_prep": "TAF 25mg + FTC 200mg PO mỗi ngày (uống với thức ăn).",
            "notes": "Ưu tiên khi nguy cơ thận/xương cao; không dùng đơn trị HIV."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; theo dõi thận.",
            "under_30": "Tránh nếu eGFR <30 (không lọc)."
        },
        "side_effects": [
            "Buồn nôn, đau đầu.",
            "Nguy cơ thận/xương thấp hơn TDF nhưng vẫn cần theo dõi."
        ],
        "interactions": [
            "P-gp inducers (rifampin, carbamazepine) giảm nồng độ TAF.",
            "Boosted PI/cobicistat tăng phơi nhiễm TAF; theo dõi thận."
        ],
        "pregnancy": "Có thể dùng; dữ liệu ít hơn TDF, TDF vẫn chuẩn trong thai kỳ.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"renal": True, "bone": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["TDF vs TAF"]
        },
        "guideline_tags": [
            "WHO 2024 HIV/PrEP",
            "DHHS/CDC HIV 2024"
        ],
        "mechanism_of_action": "Nucleotide + nucleoside analog ức chế reverse transcriptase HIV-1, kết thúc chuỗi DNA; hoạt tính HBV.",
        "monitoring": [
            "Creatinine/eGFR, phospho.",
            "HBV DNA/ALT nếu đồng nhiễm.",
            "HIV RNA, CD4; test HIV định kỳ trong PrEP."
        ],
        "precautions": [
            "Tránh cảm ứng mạnh P-gp.",
            "Không dùng đơn trị HIV.",
            "Theo dõi thận/xương dù nguy cơ thấp hơn TDF."
        ],
        "pharmacokinetics": {
            "half_life": "~0.5h tiền thuốc; tenofovir nội bào kéo dài.",
            "onset": "Nồng độ nội bào đạt trong vài giờ.",
            "duration": "1 lần/ngày.",
            "protein_binding": "~80% (TAF).",
            "clearance": "Gan (esterase/cathepsin A), thận thải tenofovir mức thấp."
        },
        "storage": "20–25°C, tránh ẩm.",
        "black_box_warnings": "Bùng phát HBV khi ngừng; toan lactic/gan to nhiễm mỡ (hiếm).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                    "mechanism": "Cảm ứng P-gp giảm nồng độ TAF.",
                    "effect": "Giảm hiệu quả.",
                    "management": "Tránh."
                }
            ],
            "moderate": [
                {
                    "drug": "Boosted PI/cobicistat",
                    "mechanism": "Ức chế P-gp tăng phơi nhiễm TAF.",
                    "effect": "Tăng nguy cơ độc thận.",
                    "management": "Theo dõi thận; cân nhắc nền không booster."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn thành phần."],
            "tương_đối": [
                "eGFR <30 mL/phút.",
                "Đồng nhiễm HBV: thận trọng khi ngừng."
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified; dữ liệu hạn chế",
            "pregnancy_details": "Có thể cân nhắc; TDF nhiều bằng chứng hơn.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Đánh giá lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Thận trọng.",
            "severe": "Dữ liệu hạn chế.",
            "notes": "Thải chủ yếu qua thận sau chuyển hóa; suy gan có thể tăng phơi nhiễm tiền thuốc."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu; lý thuyết độc thận hiếm."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ; than hoạt nếu mới uống.",
                "Theo dõi thận."
            ],
            "monitoring": "Creatinine, phospho, men gan."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn.",
                "timing": "1 lần/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV Treatment Guidelines"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based"
        }
    },

    "Bictegravir/Emtricitabine/Tenofovir alafenamide (BIC/FTC/TAF)": {
        "group": "Antiviral - Single tablet regimen (INSTI + NRTI backbone)",
        "vietnamese_name": "Bictegravir/Emtricitabine/Tenofovir alafenamide (Biktarvy)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 first-line cho người lớn/thanh thiếu niên đủ điều kiện (eGFR ≥30)."
        ],
        "contraindications": [
            "Dị ứng thành phần.",
            "Dùng rifampin (cảm ứng mạnh).",
            "eGFR <30 mL/phút."
        ],
        "dosage": {
            "standard": "BIC 50mg + FTC 200mg + TAF 25mg PO mỗi ngày.",
            "notes": "Không cần booster; tách antacid/Fe/Ca nếu dạng chelat."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh.",
            "under_30": "Tránh (theo nhãn)."
        },
        "side_effects": [
            "Buồn nôn, nhức đầu.",
            "Tăng nhẹ creatinine (BIC ức chế OCT2).",
            "Tăng cân nhẹ.",
            "Hiếm: độc thận/xương (TAF thấp hơn TDF)."
        ],
        "interactions": [
            "Rifampin: chống chỉ định.",
            "Antacid/Fe/Ca: giảm hấp thu BIC, cần tách liều.",
            "Carbamazepine/phenytoin: cảm ứng, giảm nồng độ."
        ],
        "pregnancy": "Có thể dùng; DTG có bằng chứng rộng hơn, nhưng BIC đang được chấp nhận dần.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"renal": True, "bone": True, "hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO 2024 HIV",
            "DHHS/CDC HIV 2024",
            "IAS-USA 2024"
        ],
        "mechanism_of_action": "INSTI (BIC) chặn tích hợp + NRTI backbone (FTC/TAF) ức chế RT và kết thúc chuỗi DNA HIV.",
        "monitoring": [
            "HIV RNA, CD4.",
            "Creatinine/eGFR (tăng nhẹ giả tạo; theo dõi thực thận).",
            "Men gan nếu đồng nhiễm HBV/HCV."
        ],
        "precautions": [
            "Tách antacid/Fe/Ca (BIC 2h trước hoặc 6h sau; có thể dùng cùng bữa ăn chứa Fe/Ca).",
            "Tránh rifampin; thận trọng với rifabutin/rifapentine.",
            "Theo dõi thận/xương dù nguy cơ thấp hơn TDF."
        ],
        "pharmacokinetics": {
            "half_life": "BIC ~17h; FTC 10h; TAF tiền thuốc ngắn, hoạt tính nội bào dài.",
            "onset": "Cmax 1–4h.",
            "duration": "1 lần/ngày.",
            "protein_binding": "BIC ~99%; TAF ~80%; FTC <4%.",
            "clearance": "BIC qua UGT1A1/CYP3A; FTC/TAF thải thận (tenofovir) + gan."
        },
        "storage": "20–25°C, tránh ẩm.",
        "black_box_warnings": "Bùng phát HBV khi ngừng; toan lactic/gan to nhiễm mỡ (nhóm NRTI, hiếm).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng mạnh UGT/CYP, giảm AUC BIC >75%.",
                    "effect": "Thất bại điều trị.",
                    "management": "CHỐNG CHỈ ĐỊNH."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacid/Fe/Ca",
                    "mechanism": "Tạo phức chelat giảm hấp thu BIC.",
                    "effect": "Giảm hiệu quả.",
                    "management": "Uống BIC/FTC/TAF 2h trước hoặc 6h sau; bữa ăn chứa Fe/Ca được phép."
                },
                {
                    "drug": "Carbamazepine/phenytoin",
                    "mechanism": "Cảm ứng UGT/CYP.",
                    "effect": "Giảm nồng độ.",
                    "management": "Tránh nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Quá mẫn", "Rifampin", "eGFR <30 mL/phút"],
            "tương_đối": [
                "Thuốc cảm ứng mạnh khác (carbamazepine, phenytoin).",
                "Suy gan trung bình-nặng (dữ liệu hạn chế)."
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified",
            "pregnancy_details": "Có thể dùng; dữ liệu đang tăng. DTG có bằng chứng rộng hơn.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Đánh giá lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Thận trọng.",
            "severe": "Dữ liệu hạn chế; cân nhắc tránh.",
            "notes": "BIC chuyển hóa gan; FTC/TAF ít bị ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, đau đầu; độc tính nặng hiếm."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ; than hoạt nếu mới uống."
            ],
            "monitoring": "Dấu hiệu sinh tồn, men gan, creatinine."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể với hoặc không.",
                "timing": "1 lần/ngày; tách antacid/Fe/Ca nếu dạng chelat."
            }
        },
        "references": {
            "primary_sources": [
                "WHO 2024 HIV",
                "DHHS/CDC HIV Treatment Guidelines",
                "IAS-USA 2024"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based"
        }
    },

    "Efavirenz/Tenofovir disoproxil fumarate/Emtricitabine (EFV/TDF/FTC)": {
        "group": "Antiviral - Single tablet regimen (NNRTI + NRTI backbone)",
        "vietnamese_name": "Efavirenz/TDF/FTC (Atripla và tương đương)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 người lớn (phác đồ cổ điển NNRTI, không còn first-line ưu tiên)."
        ],
        "contraindications": [
            "Dị ứng thành phần.",
            "Dùng đồng thời midazolam/triazolam/ergot (EFV tương tác).",
            "CrCl <50 mL/phút (cần chỉnh TDF/FTC đơn lẻ; FDC không chỉnh được)."
        ],
        "dosage": {
            "standard": "EFV 600mg + TDF 300mg + FTC 200mg PO mỗi tối, uống lúc đói để giảm tác dụng phụ thần kinh.",
            "notes": "Không thích hợp nếu cần chỉnh liều TDF/FTC do thận."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không dùng FDC; chuyển sang thành phần đơn lẻ để chỉnh liều.",
            "under_30": "Tránh."
        },
        "side_effects": [
            "Chóng mặt, ác mộng, mất ngủ (EFV, thường giảm sau 2–4 tuần).",
            "Phát ban, tăng men gan.",
            "Tăng creatinine/phospho giảm (TDF), giảm mật độ xương."
        ],
        "interactions": [
            "EFV cảm ứng/ức chế CYP3A/2B6: tương tác nhiều thuốc (rifampin, azole, statin, CCB, thuốc an thần).",
            "TDF độc thận; tăng nguy cơ với thuốc độc thận."
        ],
        "pregnancy": "Tránh quý 1 nếu có lựa chọn khác; có thể dùng từ quý 2 trở đi.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "neuropsychiatric": True, "renal": True, "bone": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["TDF vs TAF"]
        },
        "guideline_tags": [
            "WHO 2024 HIV (NNRTI legacy option)",
            "DHHS/CDC HIV 2024"
        ],
        "mechanism_of_action": "NNRTI (EFV) ức chế allosteric RT + NRTI (TDF/FTC) ức chế cạnh tranh, kết thúc chuỗi DNA HIV.",
        "monitoring": [
            "HIV RNA, CD4.",
            "Men gan, lipid.",
            "Triệu chứng thần kinh/tâm thần 2–4 tuần đầu.",
            "Creatinine/eGFR, phospho, mật độ xương nếu nguy cơ cao."
        ],
        "precautions": [
            "Uống buổi tối, lúc đói để giảm tác dụng phụ thần kinh.",
            "Tránh ở người rối loạn tâm thần/động kinh nếu có lựa chọn khác.",
            "Không dùng FDC nếu cần chỉnh liều TDF/FTC vì suy thận."
        ],
        "pharmacokinetics": {
            "half_life": "EFV 40–55h; TDF ~17h; FTC 10h huyết tương.",
            "onset": "Cmax EFV 3–5h.",
            "duration": "1 lần/ngày.",
            "protein_binding": "EFV ~99%; TDF <1%; FTC <4%.",
            "clearance": "EFV gan (CYP2B6/3A4); TDF/FTC thận."
        },
        "storage": "20–25°C, khô ráo.",
        "black_box_warnings": "Toan lactic/gan to nhiễm mỡ (NRTI, hiếm); cảnh báo thần kinh EFV; bùng phát HBV khi ngừng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Midazolam, triazolam, ergot",
                    "mechanism": "EFV ức chế/cảm ứng CYP3A gây thay đổi nồng độ lớn.",
                    "effect": "Nguy cơ độc tính/giảm hiệu lực.",
                    "management": "Chống chỉ định phối hợp."
                }
            ],
            "moderate": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng CYP, giảm EFV; EFV cũng cảm ứng CYP.",
                    "effect": "Giảm nồng độ; có thể cần EFV 800mg theo guideline.",
                    "management": "Cân nhắc tăng liều EFV và theo dõi virus."
                },
                {
                    "drug": "Voriconazole",
                    "mechanism": "Tương tác hai chiều CYP3A/CYP2B6.",
                    "effect": "Giảm voriconazole, tăng EFV.",
                    "management": "Tránh hoặc chỉnh liều theo khuyến cáo."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn thành phần.",
                "Phối hợp midazolam/triazolam/ergot."
            ],
            "tương_đối": [
                "Rối loạn tâm thần/động kinh.",
                "CrCl <50 (không dùng FDC; cần dạng đơn lẻ chỉnh liều)."
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D (cũ); hiện WHO cho phép sau quý 1 khi lợi ích vượt trội",
            "pregnancy_details": "Tránh quý 1 nếu có lựa chọn khác; có thể dùng từ quý 2.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa; theo dõi trẻ về an thần/phát ban.",
                "recommendation": "Cân nhắc INSTI-first nếu sẵn có."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh, theo dõi men gan.",
            "moderate": "Thận trọng; theo dõi chặt.",
            "severe": "Tránh do thiếu dữ liệu/tăng nguy cơ tích lũy.",
            "notes": "EFV chuyển hóa gan; TDF/FTC thận."
        },
        "overdose_management": {
            "symptoms": ["Tăng tác dụng phụ thần kinh EFV, buồn nôn, chóng mặt; nguy cơ độc thận (TDF)."],
            "antidote": "Không có.",
            "treatment": [
                "Than hoạt nếu mới uống.",
                "Hỗ trợ triệu chứng; theo dõi thần kinh và thận."
            ],
            "monitoring": "Men gan, creatinine, triệu chứng thần kinh."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống lúc đói/bữa ít mỡ để giảm tác dụng phụ thần kinh (EFV).",
                "timing": "1 lần/ngày buổi tối."
            }
        },
        "references": {
            "primary_sources": [
                "WHO 2024 HIV (NNRTI legacy)",
                "DHHS/CDC HIV Treatment Guidelines"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "Guideline-based (legacy option)"
        }
    },

    "Rilpivirine (RPV)": {
        "group": "Antiviral - Non-nucleoside reverse transcriptase inhibitor (NNRTI)",
        "vietnamese_name": "Rilpivirine (RPV)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 (tải lượng ban đầu ≤100.000 copies/mL, CD4 >200) kết hợp backbone NRTI.",
            "Dạng LAI khi phối hợp cabotegravir (không đề cập chi tiết tại đây)."
        ],
        "contraindications": [
            "Dị ứng với rilpivirine.",
            "Dùng đồng thời rifampin, carbamazepine, phenytoin, St. John’s wort (cảm ứng CYP3A mạnh).",
            "Dùng đồng thời PPIs liều chuẩn/cao (giảm hấp thu)."
        ],
        "dosage": {
            "standard": "25mg PO mỗi ngày, uống cùng bữa ăn.",
            "notes": "Cần bữa ăn (≥390 kcal) để tăng hấp thu; tránh PPI, antacid/H2 tách thời gian."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; thận trọng.",
            "under_30": "Thận trọng; theo dõi do dữ liệu hạn chế."
        },
        "side_effects": [
            "Đau đầu, buồn nôn.",
            "Mất ngủ, trầm cảm (hiếm).",
            "Tăng QT nhẹ trên ECG (hiếm)."
        ],
        "interactions": [
            "Cảm ứng CYP3A (rifampin, carbamazepine, phenytoin, St. John’s wort): giảm nồng độ → tránh.",
            "PPI/antacid/H2: giảm hấp thu do tăng pH.",
            "Macrolide/azole/clarithromycin: có thể tăng nồng độ (ức chế CYP3A)."
        ],
        "pregnancy": "Có thể dùng; INSTI-first vẫn ưu tiên.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "cardiac": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO 2024 HIV (NNRTI alternative)",
            "DHHS/CDC HIV 2024"
        ],
        "mechanism_of_action": "NNRTI gắn allosteric vào HIV-1 RT, ức chế sao chép và kết thúc chuỗi DNA virus.",
        "monitoring": [
            "HIV RNA, CD4.",
            "Men gan.",
            "Triệu chứng trầm cảm/mất ngủ.",
            "ECG nếu có yếu tố kéo dài QT hoặc phối hợp thuốc kéo dài QT."
        ],
        "precautions": [
            "Uống cùng bữa ăn đủ calo; tránh PPI, tách antacid/H2.",
            "Không dùng nếu tải lượng ban đầu cao >100k hoặc CD4 <200 (tăng nguy cơ thất bại).",
            "Tránh cảm ứng CYP3A mạnh."
        ],
        "pharmacokinetics": {
            "half_life": "45 giờ.",
            "onset": "Cmax ~4–5 giờ (uống với thức ăn).",
            "duration": "1 lần/ngày.",
            "protein_binding": "~99%.",
            "clearance": "Gan (CYP3A)."
        },
        "storage": "20–25°C, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                    "mechanism": "Cảm ứng CYP3A → giảm AUC RPV.",
                    "effect": "Thất bại điều trị.",
                    "management": "CHỐNG CHỈ ĐỊNH."
                },
                {
                    "drug": "Proton pump inhibitors (omeprazole, etc.)",
                    "mechanism": "Tăng pH dạ dày giảm hấp thu RPV.",
                    "effect": "Giảm AUC, thất bại điều trị.",
                    "management": "CHỐNG CHỈ ĐỊNH với PPI."
                }
            ],
            "moderate": [
                {
                    "drug": "H2 blockers (ranitidine, famotidine)",
                    "mechanism": "Tăng pH, giảm hấp thu.",
                    "effect": "Giảm AUC.",
                    "management": "Uống H2 ≥12h trước hoặc ≥4h sau RPV."
                },
                {
                    "drug": "Antacid chứa Al/Mg/Ca",
                    "mechanism": "Tăng pH, chelat.",
                    "effect": "Giảm hấp thu.",
                    "management": "Uống antacid ≥2h trước hoặc ≥4h sau RPV."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn.",
                "Dùng rifampin/carbamazepine/phenytoin/St. John’s wort.",
                "Dùng PPI."
            ],
            "tương_đối": [
                "QT kéo dài hoặc thuốc kéo dài QT.",
                "CD4 <200 hoặc tải lượng >100k.",
                "Suy gan trung bình-nặng."
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified",
            "pregnancy_details": "Có thể cân nhắc; INSTI-first ưu tiên.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Đánh giá lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Thận trọng.",
            "severe": "Tránh do dữ liệu hạn chế.",
            "notes": "Chuyển hóa gan CYP3A."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, nhức đầu, kéo dài QT (hiếm)."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ; than hoạt nếu mới uống.",
                "Theo dõi ECG nếu nghi kéo dài QT."
            ],
            "monitoring": "ECG, men gan, triệu chứng thần kinh/tâm lý."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống cùng bữa ăn đủ calo.",
                "timing": "1 lần/ngày; tách antacid/H2 theo khuyến cáo."
            }
        },
        "references": {
            "primary_sources": [
                "DHHS/CDC HIV Treatment Guidelines",
                "WHO 2024 HIV (NNRTI alternative)"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based"
        }
    },

    "Darunavir (boosted with ritonavir/cobicistat)": {
        "group": "Antiviral - Protease inhibitor (boosted)",
        "vietnamese_name": "Darunavir (tăng cường ritonavir hoặc cobicistat)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 ở người lớn/thanh thiếu niên, first-line hoặc salvage, luôn dùng kèm booster (RTV/COBI) + backbone NRTI."
        ],
        "contraindications": [
            "Dị ứng sulfonamide (thận trọng/có thể chống chỉ định nếu nặng).",
            "Dùng cùng thuốc phụ thuộc CYP3A cửa sổ hẹp (amiodarone, ergot, alfuzosin, triazolam/midazolam PO)."
        ],
        "dosage": {
            "naive": "Darunavir 800mg + ritonavir 100mg PO mỗi ngày (với thức ăn).",
            "experienced_with_resistance": "Darunavir 600mg + ritonavir 100mg PO x 2 lần/ngày.",
            "with_cobicistat": "Darunavir 800mg + cobicistat 150mg PO mỗi ngày (FDC/cùng viên), với thức ăn.",
            "notes": "Luôn dùng với booster; uống với thức ăn để tăng hấp thu và giảm khó chịu tiêu hóa."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; theo dõi nếu dùng TDF backbone.",
            "under_30": "Không cần chỉnh; lưu ý thành phần nền (TDF) nếu có."
        },
        "side_effects": [
            "Buồn nôn, tiêu chảy, đau đầu.",
            "Tăng men gan; phát ban (do thành phần sulfonamide).",
            "Tăng lipid, tăng glucose (hiếm hơn một số PI khác)."
        ],
        "interactions": [
            "Ức chế mạnh CYP3A (qua booster) → rất nhiều tương tác (statin, DOAC, benzo, kháng loạn nhịp).",
            "Inducers mạnh (rifampin, carbamazepine) giảm nồng độ darunavir → tránh."
        ],
        "pregnancy": "Có thể dùng; kinh nghiệm với ritonavir nhiều hơn cobicistat trong thai kỳ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "metabolic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "DHHS/CDC HIV 2024",
            "WHO 2024 HIV",
            "IAS-USA 2024"
        ],
        "mechanism_of_action": "PI ức chế protease HIV-1, ngăn cắt polyprotein Gag-Pol, tạo virion không trưởng thành; cần booster ức chế CYP3A để đạt nồng độ điều trị.",
        "monitoring": [
            "HIV RNA, CD4.",
            "Men gan (ALT/AST, bilirubin).",
            "Lipid (TG/LDL), glucose.",
            "Dấu hiệu phát ban/ quá mẫn sulfonamide."
        ],
        "precautions": [
            "Luôn dùng với booster + thức ăn.",
            "Rà soát tương tác CYP3A/P-gp kỹ (statin, DOAC, benzo, kháng loạn nhịp).",
            "Thận trọng tiền sử dị ứng sulfonamide.",
            "Theo dõi men gan ở viêm gan đồng nhiễm HBV/HCV."
        ],
        "pharmacokinetics": {
            "half_life": "~15 giờ khi boosted QD; ~7–8 giờ BID.",
            "onset": "Cmax 2.5–4 giờ (với thức ăn).",
            "duration": "QD hoặc BID tùy kháng.",
            "protein_binding": "~95%.",
            "clearance": "Gan (CYP3A); cần booster để đạt nồng độ."
        },
        "storage": "20–25°C, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO",
                    "mechanism": "Ức chế CYP3A (booster) tăng phơi nhiễm thuốc cửa sổ hẹp.",
                    "effect": "Nguy cơ độc tính nặng.",
                    "management": "CHỐNG CHỈ ĐỊNH."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng CYP3A mạnh giảm nồng độ darunavir.",
                    "effect": "Thất bại điều trị.",
                    "management": "CHỐNG CHỈ ĐỊNH."
                }
            ],
            "moderate": [
                {
                    "drug": "Statins (simvastatin, lovastatin)",
                    "mechanism": "Ức chế CYP3A tăng AUC statin.",
                    "effect": "Nguy cơ tiêu cơ vân.",
                    "management": "Tránh; dùng pravastatin/rosuvastatin liều thấp."
                },
                {
                    "drug": "DOACs (apixaban, rivaroxaban)",
                    "mechanism": "Ức chế CYP3A/P-gp tăng nồng độ.",
                    "effect": "Tăng chảy máu.",
                    "management": "Tránh hoặc giảm liều/giám sát theo khuyến cáo."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn darunavir/sulfonamide nặng.",
                "Phối hợp thuốc cửa sổ hẹp phụ thuộc CYP3A.",
                "Phối hợp rifampin."
            ],
            "tương_đối": [
                "Bệnh gan mạn; đồng nhiễm HBV/HCV.",
                "Tăng lipid nặng."
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified (PI; kinh nghiệm với RTV hơn COBI)",
            "pregnancy_details": "Có thể dùng; ưu tiên ritonavir booster trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Đánh giá lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh; theo dõi men gan.",
            "moderate": "Thận trọng; có thể tăng phơi nhiễm.",
            "severe": "Tránh do thiếu dữ liệu và nguy cơ tích lũy.",
            "notes": "Chuyển hóa gan qua CYP3A; booster làm tăng AUC."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, nôn, chóng mặt; lý thuyết kéo dài PR/QT khi ức chế CYP quá mức."],
            "antidote": "Không có.",
            "treatment": [
                "Than hoạt nếu mới uống.",
                "Điều trị hỗ trợ; theo dõi ECG, men gan."
            ],
            "monitoring": "ECG, men gan, dấu hiệu tương tác thuốc kèm."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống với thức ăn để tăng hấp thu.",
                "timing": "QD (naive) hoặc BID (kháng); dùng kèm booster cùng lúc."
            }
        },
        "references": {
            "primary_sources": [
                "DHHS/CDC HIV Treatment Guidelines",
                "WHO 2024 HIV",
                "IAS-USA 2024"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based"
        }
    },

    "Atazanavir (boosted with ritonavir/cobicistat)": {
        "group": "Antiviral - Protease inhibitor (boosted)",
        "vietnamese_name": "Atazanavir (tăng cường ritonavir/cobicistat)",
        "administration": ["PO"],
        "indications": [
            "Điều trị HIV-1 ở người lớn/thanh thiếu niên, luôn dùng kèm booster (RTV/COBI) + backbone NRTI."
        ],
        "contraindications": [
            "Dị ứng với atazanavir.",
            "Dùng đồng thời PPI liều cao (giảm hấp thu), rifampin (cảm ứng mạnh), thuốc phụ thuộc CYP3A cửa sổ hẹp (amiodarone, ergot, alfuzosin, triazolam/midazolam PO).",
            "Tiền sử sỏi mật/sỏi thận nặng: thận trọng."
        ],
        "dosage": {
            "naive": "Atazanavir 300mg + ritonavir 100mg PO mỗi ngày với thức ăn.",
            "with_cobicistat": "Atazanavir 300mg + cobicistat 150mg PO mỗi ngày với thức ăn.",
            "experienced_without_resistance": "300/100mg QD; nếu dùng tenofovir cần booster bắt buộc.",
            "notes": "Luôn uống với thức ăn để tăng hấp thu; tránh PPI liều chuẩn/cao, H2/antacid cần tách thời gian."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; theo dõi bilirubin/gan.",
            "under_30": "Không cần chỉnh; thận trọng nếu dùng TDF (độc thận)."
        },
        "side_effects": [
            "Tăng bilirubin gián tiếp (vàng da, vàng mắt không do gan), vàng da thường thoáng qua.",
            "Buồn nôn, tiêu chảy.",
            "Sỏi mật/sỏi thận (ít gặp).",
            "Tăng PR, hiếm block AV.",
            "Tăng men gan."
        ],
        "interactions": [
            "Ức chế CYP3A (qua booster) → nhiều tương tác (statin, DOAC, benzo).",
            "Thuốc tăng pH dạ dày (PPI/H2/antacid) giảm hấp thu atazanavir.",
            "Inducer mạnh (rifampin, carbamazepine) giảm nồng độ → tránh."
        ],
        "pregnancy": "Có thể dùng; ưu tiên ritonavir booster. Tránh PPI, quản lý H2/antacid theo khuyến cáo.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "cardiac": True, "biliary": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "DHHS/CDC HIV 2024",
            "WHO 2024 HIV",
            "IAS-USA 2024"
        ],
        "mechanism_of_action": "PI ức chế protease HIV-1, ngăn cắt polyprotein Gag-Pol; cần booster ức chế CYP3A để đạt nồng độ.",
        "monitoring": [
            "HIV RNA, CD4.",
            "Bilirubin toàn phần/trực tiếp (tăng gián tiếp thường gặp).",
            "Men gan.",
            "ECG nếu có yếu tố kéo dài PR/block AV.",
            "Lipid/glucose (ít ảnh hưởng hơn một số PI khác)."
        ],
        "precautions": [
            "Luôn dùng với booster + thức ăn.",
            "Tránh PPI; H2 uống ≥12h trước hoặc ≥4h sau; antacid cách 2h.",
            "Theo dõi vàng da; tư vấn tính chất lành tính do tăng bilirubin gián tiếp.",
            "Rà soát tương tác CYP3A/P-gp (statin/DOAC/benzo/antiarrhythmic)."
        ],
        "pharmacokinetics": {
            "half_life": "~7 giờ (boosted).",
            "onset": "Cmax 2.5–3 giờ với thức ăn.",
            "duration": "1 lần/ngày.",
            "protein_binding": "~86%.",
            "clearance": "Gan (CYP3A); cần booster."
        },
        "storage": "20–25°C, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin; amiodarone/dronedarone/ergot/alfuzosin/triazolam/midazolam PO",
                    "mechanism": "Cảm ứng mạnh giảm AUC hoặc ức chế CYP3A tăng độc tính.",
                    "effect": "Thất bại điều trị hoặc độc tính nặng.",
                    "management": "CHỐNG CHỈ ĐỊNH."
                },
                {
                    "drug": "Proton pump inhibitors (omeprazole, etc.)",
                    "mechanism": "Tăng pH giảm hấp thu atazanavir.",
                    "effect": "Giảm nồng độ, thất bại điều trị.",
                    "management": "Tránh; nếu bất khả, dùng H2/antacid theo khuyến cáo."
                }
            ],
            "moderate": [
                {
                    "drug": "H2 blockers",
                    "mechanism": "Tăng pH dạ dày.",
                    "effect": "Giảm AUC.",
                    "management": "Dùng atazanavir với thức ăn ≥2h trước hoặc ≥10–12h sau H2; theo nhãn.",
                },
                {
                    "drug": "Antacid/chelator",
                    "mechanism": "Tăng pH/chelat.",
                    "effect": "Giảm hấp thu.",
                    "management": "Cách 2h trước hoặc sau atazanavir.",
                },
                {
                    "drug": "Statins (simvastatin/lovastatin)",
                    "mechanism": "Ức chế CYP3A tăng AUC statin.",
                    "effect": "Nguy cơ tiêu cơ vân.",
                    "management": "Tránh; dùng pravastatin/rosuvastatin liều thấp."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn.",
                "Phối hợp rifampin hoặc thuốc cửa sổ hẹp phụ thuộc CYP3A.",
                "PPI liều chuẩn/cao."
            ],
            "tương_đối": [
                "Block AV, kéo dài PR.",
                "Tiền sử sỏi mật/thận.",
                "Suy gan."
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified",
            "pregnancy_details": "Có thể dùng; ưu tiên ritonavir booster; tránh PPI, quản lý H2/antacid đúng cách.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Đánh giá lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh; theo dõi men gan/bilirubin.",
            "moderate": "Thận trọng.",
            "severe": "Tránh do dữ liệu hạn chế.",
            "notes": "Chuyển hóa qua gan CYP3A; tăng phơi nhiễm ở suy gan."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, vàng da (bilirubin tăng), rối loạn dẫn truyền (kéo dài PR)."],
            "antidote": "Không có.",
            "treatment": [
                "Than hoạt nếu mới uống.",
                "Theo dõi ECG, bilirubin, men gan.",
                "Điều trị hỗ trợ."
            ],
            "monitoring": "ECG, men gan, bilirubin."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống với thức ăn.",
                "timing": "1 lần/ngày cùng booster; tránh/giãn antacid/H2/PPI theo hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "DHHS/CDC HIV Treatment Guidelines",
                "WHO 2024 HIV",
                "IAS-USA 2024"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based"
        }
    },

    "Cabotegravir + Rilpivirine (Long-acting IM)": {
        "group": "Antiviral - Long-acting INSTI + NNRTI (injectable)",
        "vietnamese_name": "Cabotegravir + Rilpivirine tiêm dài hạn",
        "administration": ["IM"],
        "indications": [
            "Điều trị duy trì HIV-1 ở người đã ức chế virus ổn định (VL <50 copies/mL), không có kháng CAB/RPV, không thất bại điều trị gần đây."
        ],
        "contraindications": [
            "Dị ứng với cabotegravir hoặc rilpivirine.",
            "Dùng đồng thời rifampin, carbamazepine, phenytoin, St. John’s wort (cảm ứng mạnh).",
            "Dùng đồng thời PPI (giảm hấp thu RPV nếu dùng lead-in oral; với IM không áp dụng nhưng cần thận trọng chuyển đổi)."
        ],
        "dosage": {
            "oral_lead_in_optional": "Cabotegravir 30mg PO + RPV 25mg PO mỗi ngày x ~28 ngày (tùy phác đồ).",
            "loading_im": "600mg CAB IM + 900mg RPV IM (mông đối bên) ngày 1.",
            "maintenance_im": "400mg CAB IM + 600mg RPV IM mỗi 1 tháng; hoặc 600/900mg mỗi 2 tháng theo phác đồ nhãn.",
            "missed_dose": "Nếu trễ, dùng oral bridging CAB 30mg + RPV 25mg hàng ngày cho đến khi tiêm lại.",
            "notes": "Tiêm sâu bắp (ventrogluteal). Cần lịch hẹn đều đặn; đánh giá kháng trước khi chuyển."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; theo dõi.",
            "under_30": "Dữ liệu hạn chế; thận trọng."
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, sưng, đỏ).",
            "Sốt nhẹ, mệt, đau đầu.",
            "Tăng men gan hiếm.",
            "Hiếm: kéo dài QT (RPV)."
        ],
        "interactions": [
            "Cảm ứng UGT/CYP3A (rifampin, carbamazepine, phenytoin, St. John’s wort): giảm nồng độ CAB/RPV.",
            "RPV tương tác pH: tránh PPI nếu dùng lead-in hoặc oral bridge; antacid/H2 tách thời gian.",
            "CYP3A inhibitors mạnh có thể tăng RPV (ít ý nghĩa lâm sàng với IM nhưng lưu ý)."
        ],
        "pregnancy": "Dữ liệu hạn chế; cân nhắc chuyển sang phác đồ uống đã biết an toàn.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "cardiac": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "DHHS/CDC HIV 2024",
            "WHO 2024 HIV",
            "IAS-USA 2024"
        ],
        "mechanism_of_action": "Cabotegravir ức chế integrase; rilpivirine ức chế allosteric RT; dạng tiêm depot phóng thích kéo dài duy trì ức chế virus.",
        "monitoring": [
            "HIV RNA định kỳ; kiểm tra VL trước chuyển và sau liều đầu.",
            "Men gan.",
            "ECG nếu có nguy cơ QT (RPV).",
            "Theo dõi phản ứng tại chỗ tiêm."
        ],
        "precautions": [
            "Chỉ dùng cho người đã ức chế virus, không có kháng CAB/RPV.",
            "Tuân thủ lịch tiêm; nếu trễ cần bridge bằng đường uống.",
            "Tránh inducer mạnh UGT/CYP3A; quản lý pH với RPV khi dùng đường uống bridge/lead-in.",
            "Đánh giá thai kỳ; cân nhắc phác đồ uống nếu cần."
        ],
        "pharmacokinetics": {
            "half_life": "CAB IM ~5–12 tuần; RPV IM ~13–28 tuần (tùy cá thể).",
            "onset": "Nồng độ đạt mức điều trị sau liều tải IM; oral lead-in giúp đánh giá dung nạp.",
            "duration": "Duy trì 4–8 tuần tùy lịch.",
            "protein_binding": "CAB >99%; RPV ~99%.",
            "clearance": "CAB: UGT1A1; RPV: CYP3A; thải chậm do depot."
        },
        "storage": "Bảo quản lọ/bơm tiêm theo nhãn; tránh đông lạnh, lắc nhẹ trước tiêm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                    "mechanism": "Cảm ứng UGT/CYP3A làm giảm nồng độ kéo dài.",
                    "effect": "Thất bại điều trị.",
                    "management": "CHỐNG CHỈ ĐỊNH."
                }
            ],
            "moderate": [
                {
                    "drug": "PPI (nếu oral lead-in/bridge)",
                    "mechanism": "Tăng pH giảm hấp thu RPV.",
                    "effect": "Giảm AUC RPV đường uống.",
                    "management": "Tránh PPI trong giai đoạn oral; H2/antacid tách thời gian."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn.",
                "Dùng inducer mạnh (rifampin, carbamazepine, phenytoin, St. John’s wort)."
            ],
            "tương_đối": [
                "Nguy cơ QT hoặc thuốc kéo dài QT (do RPV).",
                "Suy gan trung bình-nặng.",
                "Thai kỳ (dữ liệu hạn chế)."
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified",
            "pregnancy_details": "Dữ liệu hạn chế; cân nhắc phác đồ uống an toàn hơn.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Đánh giá lợi ích/nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh; theo dõi men gan.",
            "moderate": "Thận trọng.",
            "severe": "Tránh; dữ liệu hạn chế.",
            "notes": "CYP3A/UGT chuyển hóa; kéo dài phơi nhiễm ở suy gan có thể xảy ra."
        },
        "overdose_management": {
            "symptoms": ["Tăng phản ứng tại chỗ tiêm, nhức đầu, kéo dài QT (RPV, hiếm)."],
            "antidote": "Không có.",
            "treatment": [
                "Điều trị hỗ trợ; do depot nên không loại bỏ nhanh được.",
                "Theo dõi ECG nếu nghi kéo dài QT."
            ],
            "monitoring": "ECG, men gan, triệu chứng lâm sàng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Lead-in/bridge: uống cùng thức ăn (RPV cần bữa ăn).",
                "timing": "1 lần/ngày trong giai đoạn lead-in/bridge."
            },
            "im": {
                "site": "Tiêm sâu bắp vùng mông (ventrogluteal), hai bên luân phiên.",
                "timing": "Liều tải ngày 1; duy trì mỗi 1 hoặc 2 tháng tùy phác đồ.",
                "notes": "Không tiêm IV/subcut; đảm bảo lịch hẹn đều đặn."
            }
        },
        "references": {
            "primary_sources": [
                "DHHS/CDC HIV Treatment Guidelines",
                "WHO 2024 HIV",
                "IAS-USA 2024"
            ],
            "last_updated": "2025-12-24",
            "evidence_level": "High – guideline-based"
        }
    }
}

__all__ = ["HIV_ARVS"]

