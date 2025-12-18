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
            "last_updated": "2025-02-18",
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
            "last_updated": "2025-02-18",
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
            "last_updated": "2025-02-18",
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
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
    },
}

__all__ = ["HIV_ARVS"]

