"""
Oncology - Chemotherapy Agents
Common chemotherapy drugs for cancer treatment
"""

CHEMOTHERAPY_DRUGS = {
    "Cisplatin": {
        "group": "Oncology - Platinum-based Chemotherapy",
        "vietnamese_name": "Cisplatin, Platinol",
        "brand_names": "Platinol, Platinol-AQ",
        "indications": [
            "Ung thư tinh hoàn (Testicular cancer)",
            "Ung thư buồng trứng (Ovarian cancer)",
            "Ung thư bàng quang (Bladder cancer)",
            "Ung thư phổi (Lung cancer - NSCLC, SCLC)",
            "Ung thư đầu-cổ (Head and neck cancer)",
            "Ung thư cổ tử cung (Cervical cancer)"
        ],
        "contraindications": [
            "Suy thận nặng (CrCl <30ml/min)",
            "Suy tủy xương nặng",
            "Mất thính giác đã có từ trước",
            "Mang thai"
        ],
        "dosage": {
            "testicular_cancer": "20 mg/m² IV mỗi ngày x 5 ngày, lặp lại mỗi 3-4 tuần",
            "ovarian_cancer": "75-100 mg/m² IV mỗi 3-4 tuần",
            "notes": "Cần hydration tích cực (1-2L NS trước và sau) để bảo vệ thận"
        },
        "side_effects": [
            "Buồn nôn, nôn NGHIÊM TRỌNG (cần antiemetic mạnh)",
            "Độc thận (Nephrotoxicity) - Tăng Cr, giảm Mg, K",
            "Độc tai (Ototoxicity) - Mất thính giác tần số cao, tinnitus",
            "Độc thần kinh ngoại biên (Peripheral neuropathy)",
            "Suy tủy xương (Myelosuppression)",
            "Phản ứng dị ứng/phản vệ"
        ],
        "interactions": [
            "Aminoglycosides, Loop diuretics: Tăng độc thận và độc tai",
            "Phenytoin: Giảm nồng độ phenytoin",
            "Thuốc độc thận khác: Tăng nguy cơ suy thận"
        ],
        "mechanism_of_action": "Platinum compound tạo DNA crosslinks, ngăn cản DNA replication và transcription → Chết tế bào ung thư.",
        "monitoring": [
            "Chức năng thận (Cr, BUN, CrCl) - Trước mỗi liều",
            "Điện giải (Mg, K, Ca) - Thường xuyên",
            "CBC - Theo dõi suy tủy",
            "Thính lực (Audiometry) - Định kỳ",
            "Dấu hiệu neuropathy"
        ],
        "precautions": [
            "HYDRATION BẮT BUỘC: 1-2L NS trước và sau để bảo vệ thận",
            "Antiemetic mạnh (5-HT3 antagonist + Dexamethasone + NK1 antagonist)",
            "Bổ sung Mg, K thường xuyên",
            "Tránh dùng với thuốc độc thận khác",
            "Độc tính tích lũy - Giới hạn liều tích lũy"
        ],
        "pregnancy_lactation": "Pregnancy Category D - Gây dị tật thai nhi. Tránh thai trong và sau điều trị.",
        "black_box_warnings": "Phản ứng dị ứng nghiêm trọng (anaphylaxis). Suy tủy xương. Độc thận. Độc tai. Chỉ sử dụng bởi bác sĩ có kinh nghiệm hóa trị."
    },

    "Carboplatin": {
        "group": "Oncology - Platinum-based Chemotherapy",
        "vietnamese_name": "Carboplatin, Paraplatin",
        "brand_names": "Paraplatin",
        "indications": [
            "Ung thư buồng trứng (Ovarian cancer) - First-line",
            "Ung thư phổi (NSCLC, SCLC)",
            "Ung thư đầu-cổ",
            "Ung thư bàng quang"
        ],
        "contraindications": [
            "Suy tủy xương nặng",
            "Chảy máu nặng",
            "Dị ứng platinum compounds"
        ],
        "dosage": {
            "calvert_formula": "Liều (mg) = AUC x (GFR + 25). AUC thường 5-7",
            "standard": "300-400 mg/m² IV mỗi 4 tuần",
            "notes": "Ít độc thận hơn Cisplatin, không cần hydration mạnh"
        },
        "side_effects": [
            "Suy tủy xương (NGHIÊM TRỌNG) - Thrombocytopenia đặc biệt",
            "Buồn nôn, nôn (nhẹ hơn Cisplatin)",
            "Độc thận (nhẹ hơn Cisplatin)",
            "Phản ứng dị ứng",
            "Độc gan (tăng men gan)"
        ],
        "interactions": [
            "Thuốc suy tủy khác: Tăng nguy cơ nhiễm trùng, chảy máu",
            "Nephrotoxic drugs: Tăng độc thận"
        ],
        "mechanism_of_action": "Tương tự Cisplatin - Platinum compound tạo DNA crosslinks.",
        "monitoring": [
            "CBC với platelet - Trước mỗi liều và thường xuyên",
            "Chức năng thận (Cr, CrCl)",
            "Chức năng gan (AST, ALT)",
            "Dấu hiệu nhiễm trùng, chảy máu"
        ],
        "precautions": [
            "Ưu tiên hơn Cisplatin nếu lo ngại độc thận/tai",
            "Giảm liều nếu suy thận (dùng Calvert formula)",
            "Theo dõi platelet chặt chẽ - Nadir thường ngày 14-21",
            "Có thể cần truyền platelet nếu <20,000"
        ],
        "pregnancy_lactation": "Pregnancy Category D - Gây dị tật.",
        "black_box_warnings": "Suy tủy xương nghiêm trọng. Phản ứng dị ứng. Chỉ sử dụng bởi bác sĩ có kinh nghiệm hóa trị."
    },

    "Paclitaxel": {
        "group": "Oncology - Taxane Chemotherapy",
        "vietnamese_name": "Paclitaxel, Taxol",
        "brand_names": "Taxol, Abraxane (nab-paclitaxel)",
        "indications": [
            "Ung thư vú (Breast cancer)",
            "Ung thư buồng trứng (Ovarian cancer)",
            "Ung thư phổi (NSCLC)",
            "Ung thư tụy (với Gemcitabine - Abraxane)",
            "Sarcoma Kaposi liên quan AIDS"
        ],
        "contraindications": [
            "Neutrophil <1500/mm³",
            "Dị ứng Paclitaxel hoặc Cremophor (dung môi)",
            "Mang thai"
        ],
        "dosage": {
            "breast_ovarian": "175 mg/m² IV trong 3h, mỗi 3 tuần",
            "weekly": "80 mg/m² IV trong 1h, hàng tuần",
            "premedication": "BẮT BUỘC: Dexamethasone 20mg PO 12h và 6h trước + Diphenhydramine 50mg IV + H2 blocker"
        },
        "side_effects": [
            "Phản ứng quá mẫn (Hypersensitivity) - Có thể nghiêm trọng",
            "Suy tủy xương - Neutropenia",
            "Neuropathy ngoại biên (Peripheral neuropathy) - Tích lũy",
            "Đau khớp, đau cơ (Arthralgia, myalgia)",
            "Rụng tóc (Alopecia) - Phổ biến",
            "Buồn nôn, nôn"
        ],
        "interactions": [
            "CYP3A4 inhibitors (Ketoconazole): Tăng độc tính paclitaxel",
            "CYP3A4 inducers (Rifampin): Giảm hiệu quả",
            "Doxorubicin: Tăng độc tim nếu dùng trước paclitaxel"
        ],
        "mechanism_of_action": "Ổn định microtubules, ngăn cản depolymerization → Ngừng phân bào tế bào ở G2/M phase.",
        "monitoring": [
            "CBC với diff - Trước mỗi liều",
            "Dấu hiệu phản ứng quá mẫn (15 phút đầu truyền)",
            "Neuropathy (khám lâm sàng)",
            "Chức năng gan (AST, ALT, bilirubin)"
        ],
        "precautions": [
            "PREMEDICATION BẮT BUỘC để phòng phản ứng quá mẫn",
            "Theo dõi sát 15 phút đầu - Nguy cơ anaphylaxis cao nhất",
            "Giảm liều nếu neuropathy grade ≥3",
            "Tránh mang thai - Dùng KB hiệu quả",
            "Abraxane (nab-paclitaxel) không cần premedication"
        ],
        "pregnancy_lactation": "Pregnancy Category D - Gây dị tật.",
        "black_box_warnings": "Phản ứng quá mẫn nghiêm trọng và tử vong. Suy tủy xương. Chỉ sử dụng bởi bác sĩ có kinh nghiệm hóa trị. Cần premedication."
    },

    "Docetaxel": {
        "group": "Oncology - Taxane Chemotherapy",
        "vietnamese_name": "Docetaxel, Taxotere",
        "brand_names": "Taxotere",
        "indications": [
            "Ung thư vú (Breast cancer)",
            "Ung thư phổi (NSCLC)",
            "Ung thư tuyến tiền liệt (Prostate cancer)",
            "Ung thư dạ dày (Gastric cancer)",
            "Ung thư đầu-cổ"
        ],
        "contraindications": [
            "Neutrophil <1500/mm³",
            "Suy gan nặng (bilirubin >ULN)",
            "Dị ứng docetaxel hoặc polysorbate 80"
        ],
        "dosage": {
            "standard": "75-100 mg/m² IV trong 1h, mỗi 3 tuần",
            "prostate": "75 mg/m² mỗi 3 tuần (với Prednisone)",
            "premedication": "Dexamethasone 8mg PO BID x 3 ngày, bắt đầu 1 ngày trước"
        },
        "side_effects": [
            "Suy tủy xương - Neutropenia (nghiêm trọng)",
            "Phù (Fluid retention) - Tích lũy theo liều",
            "Neuropathy ngoại biên",
            "Rụng tóc",
            "Buồn nôn, nôn",
            "Stomatitis (viêm loét miệng)",
            "Phản ứng quá mẫn"
        ],
        "interactions": [
            "CYP3A4 inhibitors/inducers: Ảnh hưởng nồng độ docetaxel",
            "Thuốc suy tủy khác: Tăng nguy cơ nhiễm trùng"
        ],
        "mechanism_of_action": "Tương tự Paclitaxel - Ổn định microtubules, ngừng phân bào.",
        "monitoring": [
            "CBC với diff - Trước mỗi liều",
            "Chức năng gan (AST, ALT, bilirubin, ALP)",
            "Cân nặng, phù",
            "Neuropathy",
            "Dấu hiệu nhiễm trùng"
        ],
        "precautions": [
            "Premedication với corticosteroid BẮT BUỘC để giảm phù và phản ứng quá mẫn",
            "Có thể cần diuretics nếu phù nặng",
            "Giảm liều nếu suy gan",
            "Cân nhắc G-CSF nếu neutropenia kéo dài"
        ],
        "pregnancy_lactation": "Pregnancy Category D",
        "black_box_warnings": "Suy tủy xương nghiêm trọng. Phản ứng quá mẫn. Phù và độc gan ở bệnh nhân suy gan. Chỉ sử dụng bởi bác sĩ có kinh nghiệm."
    },

    "Doxorubicin": {
        "group": "Oncology - Anthracycline Chemotherapy",
        "vietnamese_name": "Doxorubicin, Adriamycin",
        "brand_names": "Adriamycin, Doxil (liposomal)",
        "indications": [
            "Ung thư vú (Breast cancer)",
            "Lymphoma (Hodgkin, NHL)",
            "Ung thư phổi",
            "Ung thư buồng trứng",
            "Sarcoma",
            "Bạch cầu cấp (ALL, AML)"
        ],
        "contraindications": [
            "Suy tim nặng (EF <40%)",
            "Nhồi máu cơ tim gần đây",
            "Suy tủy xương nặng",
            "Đã dùng liều tích lũy tối đa anthracycline"
        ],
        "dosage": {
            "standard": "60-75 mg/m² IV mỗi 21 ngày",
            "cumulative_limit": "GIỚI HẠN TÍCH LŨY: 450-550 mg/m² (nguy cơ suy tim)",
            "notes": "Màu đỏ - Nước tiểu có thể chuyển màu đỏ (bình thường)"
        },
        "side_effects": [
            "Độc tim (Cardiotoxicity) - SỰ KIỆN NGHIÊM TRỌNG NHẤT",
            "Suy tủy xương",
            "Rụng tóc (100%)",
            "Buồn nôn, nôn",
            "Viêm loét miệng (Mucositis)",
            "Ngoại tràn (Extravasation) → Hoại tử mô nghiêm trọng",
            "Nước tiểu/nước mắt/mồ hôi chuyển màu đỏ (vô hại)"
        ],
        "interactions": [
            "Trastuzumab, Pertuzumab: Tăng NGHIÊM TRỌNG nguy cơ suy tim",
            "Paclitaxel: Tăng độc tim nếu dùng sau doxorubicin",
            "Cyclosporine: Tăng độc tính doxorubicin"
        ],
        "mechanism_of_action": "Intercalate vào DNA, ức chế topoisomerase II, tạo free radicals → Phá hủy DNA và màng tế bào.",
        "monitoring": [
            "Chức năng tim (ECHO hoặc MUGA scan) - Trước điều trị, sau mỗi 100-150 mg/m², và khi có triệu chứng",
            "CBC với diff",
            "Chức năng gan (AST, ALT, bilirubin)",
            "Dấu hiệu ngoại tràn khi truyền"
        ],
        "precautions": [
            "THEO DÕI LIỀU TÍCH LŨY - Ngừng khi đạt 450-550 mg/m²",
            "Đánh giá chức năng tim trước và trong điều trị",
            "TRÁNH NGOẠI TRÀN - Vesicant mạnh, gây hoại tử mô",
            "Nếu ngoại tràn: Ngừng ngay, chườm lạnh, dexrazoxane antidote",
            "Giảm liều nếu suy gan",
            "Dexrazoxane có thể bảo vệ tim (nếu liều tích lũy cao)"
        ],
        "pregnancy_lactation": "Pregnancy Category D",
        "black_box_warnings": "Độc tim nghiêm trọng và suy tim. Suy tủy xương. Ngoại tràn gây hoại tử mô nghiêm trọng. Độc gan ở bệnh nhân suy gan. Chỉ sử dụng bởi bác sĩ có kinh nghiệm."
    },

    "Cyclophosphamide": {
        "group": "Oncology - Alkylating Agent",
        "vietnamese_name": "Cyclophosphamide, Cytoxan",
        "brand_names": "Cytoxan, Endoxan",
        "indications": [
            "Lymphoma (Hodgkin, NHL)",
            "Bạch cầu (ALL, CLL, AML)",
            "Ung thư vú",
            "Ung thư buồng trứng",
            "Myeloma đa phát",
            "Bệnh tự miễn (Lupus, Vasculitis) - Liều thấp"
        ],
        "contraindications": [
            "Suy tủy xương nặng",
            "Viêm bàng quang xuất huyết",
            "Tắc nghẽn đường tiết niệu"
        ],
        "dosage": {
            "cancer": "500-1500 mg/m² IV mỗi 2-4 tuần (liều cao)",
            "oral": "50-100 mg/m²/ngày PO (liều thấp)",
            "autoimmune": "500-1000 mg IV pulse therapy",
            "notes": "Cần hydration và Mesna để bảo vệ bàng quang"
        },
        "side_effects": [
            "Suy tủy xương",
            "Viêm bàng quang xuất huyết (Hemorrhagic cystitis) - Đặc trưng",
            "Buồn nôn, nôn",
            "Rụng tóc",
            "Vô sinh (Infertility) - Đặc biệt ở liều cao",
            "Ung thư bàng quang thứ phát (lâu dài)",
            "SIADH (Hội chứng tiết ADH không phù hợp)"
        ],
        "interactions": [
            "Allopurinol: Tăng độc tính cyclophosphamide",
            "Warfarin: Tăng INR",
            "Thuốc suy tủy khác: Tăng nguy cơ nhiễm trùng"
        ],
        "mechanism_of_action": "Alkylating agent - Tạo DNA crosslinks → Ngăn cản DNA replication.",
        "monitoring": [
            "CBC với diff",
            "Nước tiểu (hematuria - máu tiểu)",
            "Điện giải (Na - SIADH)",
            "Chức năng thận (BUN, Cr)"
        ],
        "precautions": [
            "HYDRATION TÍCH CỰC (2-3L/ngày) để phòng viêm bàng quang",
            "MESNA (2-mercaptoethane sulfonate) - Bảo vệ bàng quang ở liều cao",
            "Uống nhiều nước, đi tiểu thường xuyên",
            "Tư vấn bảo tồn sinh sản trước điều trị (đặc biệt bệnh nhân trẻ)",
            "Theo dõi lâu dài - Nguy cơ ung thư bàng quang"
        ],
        "pregnancy_lactation": "Pregnancy Category D - Gây dị tật.",
        "black_box_warnings": "Suy tủy xương. Viêm bàng quang xuất huyết. Ung thư bàng quang thứ phát. Độc tim ở liều cao. Chỉ sử dụng bởi bác sĩ có kinh nghiệm."
    },

    "5-Fluorouracil": {
        "group": "Oncology - Antimetabolite (Pyrimidine analog)",
        "vietnamese_name": "5-Fluorouracil, 5-FU",
        "brand_names": "Adrucil, Efudex (topical)",
        "indications": [
            "Ung thư đại trực tràng (Colorectal cancer) - Phổ biến nhất",
            "Ung thư vú",
            "Ung thư dạ dày",
            "Ung thư tụy",
            "Ung thư đầu-cổ",
            "Ung thư da (topical)"
        ],
        "contraindications": [
            "Thiếu hụt DPD (Dihydropyrimidine dehydrogenase) - Độc tính nghiêm trọng",
            "Suy tủy xương nặng",
            "Nhiễm trùng nặng",
            "Mang thai"
        ],
        "dosage": {
            "bolus": "400-600 mg/m² IV bolus",
            "infusion": "2400-3000 mg/m² IV continuous infusion 46h (phổ biến trong FOLFOX, FOLFIRI)",
            "topical": "Cream 5% - Bôi 2 lần/ngày cho ung thư da"
        },
        "side_effects": [
            "Suy tủy xương",
            "Viêm loét miệng (Mucositis, stomatitis)",
            "Tiêu chảy (Diarrhea) - Có thể nghiêm trọng",
            "Hội chứng bàn tay-bàn chân (Hand-foot syndrome) - Đỏ, đau, bong tróc da",
            "Buồn nôn, nôn",
            "Độc tim (hiếm) - Đau ngực, nhồi máu",
            "Độc thần kinh (hiếm)"
        ],
        "interactions": [
            "Leucovorin (Folinic acid): Tăng hiệu quả 5-FU (dùng kèm cố ý)",
            "Warfarin: Tăng INR",
            "Phenytoin: Tăng nồng độ phenytoin"
        ],
        "mechanism_of_action": "Pyrimidine analog ức chế thymidylate synthase → Ngăn cản tổng hợp DNA.",
        "monitoring": [
            "CBC với diff",
            "Chức năng thận, gan",
            "Dấu hiệu mucositis (miệng)",
            "Tiêu chảy",
            "Hand-foot syndrome",
            "Triệu chứng tim mạch (đau ngực)"
        ],
        "precautions": [
            "Test DPD deficiency nếu có tiền sử gia đình hoặc độc tính bất thường",
            "Leucovorin (folinic acid) thường dùng kèm để tăng hiệu quả",
            "Loperamide cho tiêu chảy",
            "Chăm sóc miệng tốt để phòng mucositis",
            "Kem dưỡng ẩm cho hand-foot syndrome",
            "Ngừng nếu tiêu chảy hoặc mucositis grade ≥3"
        ],
        "pregnancy_lactation": "Pregnancy Category D",
        "black_box_warnings": "Suy tủy xương nghiêm trọng. Tiêu chảy và mucositis nghiêm trọng có thể gây tử vong. Chỉ sử dụng bởi bác sĩ có kinh nghiệm."
    },

    "Gemcitabine": {
        "group": "Oncology - Antimetabolite (Pyrimidine analog)",
        "vietnamese_name": "Gemcitabine, Gemzar",
        "brand_names": "Gemzar",
        "indications": [
            "Ung thư tụy (Pancreatic cancer) - First-line",
            "Ung thư phổi (NSCLC)",
            "Ung thư buồng trứng",
            "Ung thư bàng quang",
            "Ung thư vú"
        ],
        "contraindications": [
            "Dị ứng gemcitabine",
            "Mang thai"
        ],
        "dosage": {
            "standard": "1000 mg/m² IV trong 30 phút, ngày 1, 8, 15 của chu kỳ 28 ngày",
            "pancreatic": "1000 mg/m² hàng tuần x 7 tuần, sau đó hàng tuần x 3/4 tuần",
            "notes": "Tốc độ truyền 10 mg/m²/phút (không truyền nhanh)"
        },
        "side_effects": [
            "Suy tủy xương",
            "Hội chứng giống cúm (Flu-like syndrome) - Sốt, ớn lạnh, đau cơ",
            "Phù, tăng cân",
            "Phát ban da",
            "Tăng men gan",
            "Buồn nôn, nôn (nhẹ)",
            "Hội chứng phổi (hiếm nhưng nghiêm trọng)"
        ],
        "interactions": [
            "Cisplatin: Tăng độc thận",
            "Thuốc suy tủy khác: Tăng nguy cơ nhiễm trùng"
        ],
        "mechanism_of_action": "Nucleoside analog ức chế DNA synthesis.",
        "monitoring": [
            "CBC với diff, platelet - Trước mỗi liều",
            "Chức năng thận (Cr, BUN)",
            "Chức năng gan (AST, ALT, bilirubin)",
            "Dấu hiệu hội chứng phổi (khó thở, ho)"
        ],
        "precautions": [
            "Truyền ĐÚNG TỐC ĐỘ (10 mg/m²/phút) - Truyền nhanh tăng độc tính",
            "Acetaminophen có thể giảm flu-like symptoms",
            "Giảm liều hoặc delay nếu suy tủy",
            "Ngừng nếu nghi ngờ hội chứng phổi"
        ],
        "pregnancy_lactation": "Pregnancy Category D",
        "black_box_warnings": "Suy tủy xương. Hội chứng phổi nghiêm trọng. Chỉ sử dụng bởi bác sĩ có kinh nghiệm."
    },

    "Methotrexate": {
        "group": "Oncology - Antimetabolite (Folate antagonist) / DMARD",
        "vietnamese_name": "Methotrexate, MTX",
        "brand_names": "Trexall, Rheumatrex, Otrexup",
        "indications": [
            "Ung thư (Liều cao): ALL, Lymphoma, Osteosarcoma, Choriocarcinoma",
            "Viêm khớp dạng thấp (RA) - Liều thấp",
            "Lupus, Psoriasis",
            "Thai ngoài tử cung (Ectopic pregnancy)"
        ],
        "contraindications": [
            "Mang thai (gây dị tật nghiêm trọng)",
            "Cho con bú",
            "Suy gan, suy thận nặng",
            "Suy tủy xương",
            "Nghiện rượu"
        ],
        "dosage": {
            "cancer_high_dose": "1-12 g/m² IV (cần leucovorin rescue)",
            "RA_low_dose": "7.5-25 mg PO/SC/IM mỗi tuần",
            "ectopic": "50 mg/m² IM single dose (nếu β-hCG <5000, không vỡ)",
            "leucovorin_rescue": "BẮT BUỘC với liều cao: Bắt đầu 24h sau MTX, tiếp tục đến MTX level <0.05 μmol/L"
        },
        "side_effects": [
            "Suy tủy xương",
            "Viêm loét miệng (Mucositis)",
            "Độc gan (Hepatotoxicity) - Xơ gan nếu dùng lâu dài",
            "Độc thận (ở liều cao)",
            "Độc phổi (Pneumonitis) - Hiếm nhưng nghiêm trọng",
            "Buồn nôn, nôn, tiêu chảy",
            "Gây dị tật thai nhi (Teratogenic)"
        ],
        "interactions": [
            "NSAIDs, Aspirin: Tăng độc tính MTX (giảm thải qua thận)",
            "Proton pump inhibitors: Tăng MTX level",
            "Trimethoprim: Tăng độc tính (cả 2 đều chống folate)",
            "Penicillins: Giảm thải MTX"
        ],
        "mechanism_of_action": "Ức chế dihydrofolate reductase → Ngăn cản tổng hợp DNA/RNA.",
        "monitoring": [
            "CBC với diff",
            "Chức năng gan (AST, ALT) - Định kỳ",
            "Chức năng thận (Cr, BUN)",
            "MTX level (nếu liều cao) - Đảm bảo <0.05 μmol/L trước ngừng leucovorin",
            "Chest X-ray nếu nghi ngờ độc phổi"
        ],
        "precautions": [
            "LEUCOVORIN RESCUE BẮT BUỘC với liều cao (>100 mg/m²)",
            "HYDRATION TÍCH CỰC + kiềm hóa nước tiểu (NaHCO3) để tăng thải MTX",
            "Folic acid 1mg/ngày khi dùng liều thấp (RA) - Giảm tác dụng phụ",
            "TRÁNH THAI nghiêm ngặt - Gây dị tật nghiêm trọng",
            "Tránh NSAIDs khi dùng MTX liều cao",
            "Không uống rượu - Tăng nguy cơ xơ gan"
        ],
        "pregnancy_lactation": "Pregnancy Category X - CHỐNG CHỈ ĐỊNH tuyệt đối. Gây dị tật nghiêm trọng và sẩy thai.",
        "black_box_warnings": "Gây dị tật nghiêm trọng và tử vong thai nhi. Suy tủy xương. Độc gan, xơ gan. Độc thận. Độc phổi. Chỉ sử dụng bởi bác sĩ có kinh nghiệm. Cần leucovorin rescue với liều cao."
    }
}
