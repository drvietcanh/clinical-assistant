"""
Gout & Hyperuricemia Drugs (Thuốc điều trị Gout & Tăng acid uric)
"""

GOUT_DRUGS = {
    "Allopurinol":     {
        "group": "Rheumatology - Gout (Xanthine Oxidase Inhibitor)",
        "vietnamese_name": "Allopurinol, Zyloric, Zyloprim",
        "brand_names": {
            "common": [
                "Zyloprim",
                "Zyloric"
            ],
            "vietnam": [
                "Allopurinol 100mg",
                "Allopurinol 300mg",
                "Zyloric 100mg",
                "Zyloric 300mg",
                "Sadapron"
            ],
        },
        "manufacturer": {
            "primary": "GlaxoSmithKline (GSK) - Zyloprim, Zyloric",
            "vietnam": [
                "GlaxoSmithKline (GSK)",
                "Các công ty dược phẩm Việt Nam (generic - Allopurinol, Sadapron, v.v.)"
            ],
            "notes": "GlaxoSmithKline (GSK) là nhà sản xuất gốc của Zyloprim/Zyloric (allopurinol). Có nhiều sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Gout mạn tính (hạ acid uric máu, phòng ngừa cơn gout)",
            "Tăng acid uric do hóa trị ung thư (tumor lysis syndrome)",
            "Sỏi thận do acid uric",
            "Tăng acid uric máu không triệu chứng (khi cần thiết)"
        ],
        "contraindications": [
            "Quá mẫn với Allopurinol (đặc biệt: người mang gen HLA-B*5801 - Black Box Warning)",
            "Cơn Gout cấp đang diễn tiến (không khởi trị lúc này, nhưng nếu đang dùng thì tiếp tục)",
            "Dùng chung với Azathioprine hoặc Mercaptopurine (CHỐNG CHỈ ĐỊNH tuyệt đối - tăng độc tính tủy xương)"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với Allopurinol (đặc biệt: người mang gen HLA-B*5801 - Black Box Warning - SJS/TEN)",
                "Dùng chung với Azathioprine hoặc Mercaptopurine (CHỐNG CHỈ ĐỊNH tuyệt đối - tăng độc tính tủy xương nghiêm trọng)",
                "Cơn Gout cấp đang diễn tiến (không khởi trị lúc này)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <10 ml/min) - giảm liều, thận trọng",
                "Suy gan - thận trọng, có thể tăng nguy cơ độc tính",
                "Người Việt Nam/Á Đông - tăng nguy cơ SJS/TEN, nên sàng lọc HLA-B*5801 trước khi dùng",
                "Phụ nữ có thai - tránh dùng trừ khi lợi ích vượt trội"
            ]
        },
        "dosage": {
            "adult_gout_initial": "100mg uống 1 lần/ngày, tăng dần mỗi 2-4 tuần đến 300mg/ngày (thường dùng)",
            "adult_gout_maintenance": "200-600mg/ngày (tùy đáp ứng, max 800mg/ngày)",
            "adult_gout_max": "800mg/ngày (chia 2-3 lần nếu >300mg)",
            "adult_tumor_lysis_syndrome": "600-800mg/ngày (chia 2-3 lần), bắt đầu 1-2 ngày trước hóa trị",
            "adult_renal_crcl_30_60": "100-200mg/ngày",
            "adult_renal_crcl_10_30": "100mg/ngày hoặc 100mg cách ngày",
            "adult_renal_crcl_under_10": "100mg cách ngày hoặc 100mg 3 lần/tuần",
            "adult_hemodialysis": "100-300mg sau mỗi lần lọc máu (không dùng giữa các lần lọc)",
            "notes": "QUAN TRỌNG: Cần sàng lọc gen HLA-B*5801 ở người Việt Nam/Á Đông trước khi dùng để tránh hội chứng Steven-Johnson/TEN. Khởi phát cơn Gout cấp khi mới bắt đầu điều trị - nên phối hợp Colchicine/NSAID trong 3-6 tháng đầu. Uống với nhiều nước (≥2 lít/ngày) để tránh sỏi thận. Uống sau ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "100-200mg/ngày (CrCl 30-60 ml/min)",
            "10_30": "100mg/ngày hoặc 100mg cách ngày (CrCl 10-30 ml/min)",
            "under_10": "100mg cách ngày hoặc 100mg 3 lần/tuần (CrCl <10 ml/min)",
            "dialysis": "100-300mg sau mỗi lần lọc máu (không dùng giữa các lần lọc)",
            "notes": "Allopurinol và oxypurinol (metabolite) thải trừ qua thận. Cần điều chỉnh liều ở suy thận để tránh tích lũy và tăng nguy cơ độc tính."
        },
        "side_effects": [
            "Dị ứng da (nhẹ đến nghiêm trọng - SJS/TEN) - Black Box Warning, đặc biệt ở người mang gen HLA-B*5801",
            "Khởi phát cơn Gout cấp khi mới bắt đầu điều trị (nên phối hợp Colchicine/NSAID trong 3-6 tháng đầu)",
            "Buồn nôn, nôn, tiêu chảy",
            "Đau đầu, chóng mặt",
            "Tăng men gan, viêm gan (hiếm)",
            "Ức chế tủy xương (giảm bạch cầu, giảm tiểu cầu) - hiếm",
            "Suy thận (hiếm)",
            "Phát ban, ngứa"
        ],
        "mechanism_of_action": "Allopurinol và oxypurinol (metabolite hoạt động) ức chế Xanthine Oxidase, enzyme chuyển hóa Hypoxanthine -> Xanthine -> Acid Uric. Bằng cách ức chế Xanthine Oxidase, allopurinol làm giảm sản xuất acid uric, giảm nồng độ acid uric trong máu và nước tiểu, phòng ngừa hình thành sỏi thận và cơn gout.",
        "monitoring": [
            "Acid uric máu (Target <6 mg/dL cho gout, <7 mg/dL cho tăng acid uric không triệu chứng)",
            "Chức năng thận (CrCl) - trước và trong điều trị (cần điều chỉnh liều)",
            "Dấu hiệu dị ứng da (phát ban, SJS/TEN) - Black Box Warning, ngừng ngay nếu có",
            "Công thức máu (nếu có triệu chứng ức chế tủy xương)",
            "Men gan (nếu có triệu chứng viêm gan)",
            "Dấu hiệu cơn gout cấp (có thể khởi phát khi mới bắt đầu điều trị)"
        ],
        "interactions": [
            "Azathioprine, Mercaptopurine: CHỐNG CHỈ ĐỊNH - allopurinol ức chế chuyển hóa, tăng độc tính tủy xương nghiêm trọng",
            "Warfarin: allopurinol có thể tăng tác dụng chống đông, tăng INR - theo dõi INR chặt chẽ",
            "Theophylline: allopurinol có thể tăng nồng độ theophylline - theo dõi nồng độ, giảm liều theophylline nếu cần",
            "ACE inhibitors (captopril, enalapril): tăng nguy cơ phản ứng quá mẫn",
            "Thiazide diuretics: tăng nguy cơ phản ứng quá mẫn",
            "Amoxicillin, Ampicillin: tăng nguy cơ phát ban",
            "Cyclophosphamide: tăng độc tính tủy xương",
            "Didanosine: tăng nồng độ didanosine - tránh dùng chung"
        ],
        "pregnancy": "C - Tránh dùng trừ khi lợi ích vượt trội",
        "precautions": [
            "QUAN TRỌNG: Sàng lọc gen HLA-B*5801 ở người Việt Nam/Á Đông trước khi dùng để tránh SJS/TEN",
            "Ngừng ngay nếu có dấu hiệu dị ứng da (phát ban, SJS/TEN) - Black Box Warning",
            "Khởi phát cơn Gout cấp khi mới bắt đầu - phối hợp Colchicine/NSAID trong 3-6 tháng đầu",
            "Uống với nhiều nước (≥2 lít/ngày) để tránh sỏi thận",
            "Uống sau ăn để giảm kích ứng dạ dày",
            "Điều chỉnh liều theo chức năng thận (CrCl)",
            "CHỐNG CHỈ ĐỊNH dùng chung với Azathioprine/Mercaptopurine",
            "Theo dõi INR nếu dùng với warfarin",
            "Theo dõi nồng độ theophylline nếu dùng với theophylline"
        ],
        "pharmacokinetics": {
            "half_life": "Allopurinol: 1-2 giờ; Oxypurinol (metabolite hoạt động): 15-30 giờ (bình thường), 50-100 giờ (suy thận)",
            "onset": "Giảm acid uric máu trong 1-2 tuần",
            "duration": "12-24 giờ (do oxypurinol có half-life dài)",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (allopurinol và oxypurinol thải trừ qua thận). Cần điều chỉnh liều ở suy thận.",
            "metabolism": "Chuyển hóa thành oxypurinol (metabolite hoạt động) bởi xanthine oxidase và aldehyde oxidase"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Phản ứng da nghiêm trọng (SJS/TEN): có thể xảy ra, đặc biệt ở người mang gen HLA-B*5801 (phổ biến ở người Việt Nam/Á Đông). Ngừng ngay nếu có dấu hiệu phản ứng da. Sàng lọc HLA-B*5801 trước khi dùng ở người có nguy cơ cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Azathioprine, Mercaptopurine",
                    "mechanism": "Allopurinol ức chế xanthine oxidase, enzyme chuyển hóa azathioprine/mercaptopurine, làm tăng nồng độ và độc tính",
                    "effect": "Tăng độc tính tủy xương nghiêm trọng (giảm bạch cầu, giảm tiểu cầu, suy tủy) - có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng chung. Giảm liều azathioprine/mercaptopurine xuống 25-33% nếu bắt buộc phải dùng chung (rất hiếm)."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Allopurinol có thể ức chế chuyển hóa warfarin, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu/ngừng allopurinol. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Allopurinol có thể ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline, tăng nguy cơ độc tính (buồn nôn, nôn, co giật, rối loạn nhịp tim)",
                    "management": "Theo dõi nồng độ theophylline. Giảm liều theophylline nếu cần."
                },
                {
                    "drug": "ACE inhibitors (captopril, enalapril), Thiazide diuretics",
                    "mechanism": "Cộng gộp nguy cơ phản ứng quá mẫn",
                    "effect": "Tăng nguy cơ phản ứng quá mẫn, phát ban",
                    "management": "Thận trọng. Theo dõi dấu hiệu phản ứng quá mẫn."
                },
                {
                    "drug": "Amoxicillin, Ampicillin",
                    "mechanism": "Cộng gộp nguy cơ phát ban",
                    "effect": "Tăng nguy cơ phát ban",
                    "management": "Thận trọng. Theo dõi dấu hiệu phát ban."
                }
            ],
            "minor": [
                {
                    "drug": "Cyclophosphamide",
                    "mechanism": "Cộng gộp độc tính tủy xương",
                    "effect": "Tăng độc tính tủy xương",
                    "management": "Thận trọng. Theo dõi công thức máu."
                },
                {
                    "drug": "Didanosine",
                    "mechanism": "Allopurinol có thể tăng nồng độ didanosine",
                    "effect": "Tăng nồng độ didanosine, tăng nguy cơ độc tính",
                    "management": "Tránh dùng chung nếu có thể."
                }
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ trừ khi lợi ích vượt trội. Dữ liệu an toàn hạn chế. Có thể ảnh hưởng đến phát triển thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Allopurinol và oxypurinol bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú nếu lợi ích vượt trội. Theo dõi trẻ sơ sinh."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể tăng nguy cơ độc tính",
            "severe": "Thận trọng, tránh dùng nếu có thể",
            "notes": "Allopurinol chuyển hóa một phần qua gan. Suy gan có thể tăng nguy cơ độc tính (viêm gan, ức chế tủy xương). Thận trọng ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Phát ban, phản ứng da nghiêm trọng (SJS/TEN)",
                "Ức chế tủy xương (giảm bạch cầu, giảm tiểu cầu)",
                "Viêm gan, suy gan",
                "Suy thận"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng allopurinol ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ: truyền dịch, theo dõi dấu hiệu sống",
                "Điều trị phản ứng da: chăm sóc da, điều trị SJS/TEN nếu có",
                "Điều trị ức chế tủy xương: truyền máu, tiểu cầu, G-CSF nếu cần",
                "Lọc máu có thể giúp loại bỏ allopurinol và oxypurinol (nhưng hiệu quả hạn chế do oxypurinol có half-life dài)"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu, chức năng gan, chức năng thận, dấu hiệu phản ứng da"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống sau ăn để giảm kích ứng dạ dày",
                "timing": "Uống 1-3 lần/ngày tùy liều. Uống với nhiều nước (≥2 lít/ngày) để tránh sỏi thận.",
                "notes": "Uống sau ăn để giảm kích ứng dạ dày. Uống với nhiều nước (≥2 lít/ngày) để tránh sỏi thận. Khởi đầu với liều thấp (100mg/ngày), tăng dần mỗi 2-4 tuần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Allopurinol (Zyloprim)",
                "ACR Guidelines - Gout Management",
                "UpToDate - Allopurinol: Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, ACR guidelines"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"dermatologic": "Black Box Warning - Severe skin reactions (SJS/TEN - HLA-B*5801 carriers, especially Asians)", "hepatic": "Hepatotoxicity (rare)", "renal": "Nephrotoxicity (rare)"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": "Rare",
            "requires_monitoring": ["Black Box Warning - HLA-B*5801 screening (especially Asians - SJS/TEN risk)", "Skin reactions (Black Box Warning - SJS/TEN signs, stop immediately)", "Serum uric acid (target <6 mg/dL)", "Renal function (dose adjustment required)", "Hepatic function (hepatotoxicity risk)", "Azathioprine/mercaptopurine interaction (contraindicated - severe myelosuppression)"],
            "look_alike_sound_alike": ["Allopurinol", "Allopurinol"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Severe Skin Reactions (SJS/TEN - HLA-B*5801 carriers)",
            "ACR Guidelines - Gout Management",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    "Colchicine":     {
        "group": "Rheumatology - Gout (Anti-inflammatory)",
        "vietnamese_name": "Colchicine, Colcrys",
        "brand_names": {
            "common": [
                "Colcrys",
                "Mitigare"
            ],
            "vietnam": [
                "Colchicine 0.5mg",
                "Colchicine 1mg",
                "Colgout"
            ],
        },
        "manufacturer": {
            "primary": "Takeda Pharmaceuticals (Colcrys), Hikma Pharmaceuticals (Mitigare)",
            "vietnam": [
                "Takeda Pharmaceuticals",
                "Hikma Pharmaceuticals",
                "Các công ty dược phẩm Việt Nam (generic - Colchicine, Colgout, v.v.)"
            ],
            "notes": "Takeda Pharmaceuticals là nhà sản xuất gốc của Colcrys (colchicine). Có nhiều sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Cơn Gout cấp (Acute Gout)",
            "Dự phòng cơn Gout cấp khi bắt đầu dùng Allopurinol/Febuxostat",
            "Sốt Địa Trung Hải (Familial Mediterranean Fever - FMF)",
            "Bệnh Behçet",
            "Viêm màng ngoài tim tái phát"
        ],
        "contraindications": [
            "Suy thận nặng + Suy gan nặng (CHỐNG CHỈ ĐỊNH tuyệt đối)",
            "Dùng chung chất ức chế P-gp/CYP3A4 mạnh (Clarithromycin, Ketoconazole, Itraconazole, Ritonavir, Cyclosporine) ở người suy thận/gan - Black Box Warning",
            "Dị ứng với colchicine"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Suy thận nặng + Suy gan nặng (CHỐNG CHỈ ĐỊNH tuyệt đối)",
                "Dùng chung chất ức chế P-gp/CYP3A4 mạnh (Clarithromycin, Ketoconazole, Itraconazole, Ritonavir, Cyclosporine) ở người suy thận/gan - Black Box Warning - có thể tử vong",
                "Dị ứng với colchicine"
            ],
            "tương_đối": [
                "Suy thận trung bình - giảm liều, thận trọng",
                "Suy gan trung bình - giảm liều, thận trọng",
                "Người cao tuổi - giảm liều, tăng nguy cơ độc tính",
                "Phụ nữ có thai - tránh dùng trừ khi lợi ích vượt trội"
            ]
        },
        "dosage": {
            "adult_acute_gout": "1.2mg (hoặc 1mg) ngay khi có triệu chứng, sau đó 0.6mg (hoặc 0.5mg) sau 1 giờ. Tổng liều ngày đầu không quá 1.8mg. Có thể lặp lại sau 12 giờ nếu cần (tổng tối đa 1.2mg trong 12 giờ tiếp theo).",
            "adult_acute_gout_alternative": "1.2mg x 1 lần, sau đó 0.6mg sau 1 giờ. Tổng liều ngày đầu không quá 1.8mg.",
            "adult_prophylaxis_gout": "0.5-0.6mg x 1-2 lần/ngày (thường 0.6mg x 1 lần/ngày)",
            "adult_fmf": "1.2-2.4mg/ngày (chia 1-2 lần)",
            "adult_renal_crcl_30_60": "Giảm liều 50%",
            "adult_renal_crcl_under_30": "Giảm liều 75% hoặc tránh dùng",
            "adult_hepatic_impairment": "Giảm liều 50%",
            "elderly": "Giảm liều, thận trọng",
            "notes": "QUAN TRỌNG: Liều cao (uống mỗi 2h đến khi tiêu chảy) KHÔNG CÒN ĐƯỢC KHUYẾN CÁO do độc tính cao. CHỐNG CHỈ ĐỊNH dùng chung với chất ức chế P-gp/CYP3A4 mạnh ở người suy thận/gan - có thể tử vong (Black Box Warning). Điều chỉnh liều theo chức năng thận và gan."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "Giảm liều 50% (CrCl 30-60 ml/min)",
            "under_30": "Giảm liều 75% hoặc tránh dùng (CrCl <30 ml/min)",
            "dialysis": "Tránh dùng hoặc giảm liều đáng kể",
            "notes": "Colchicine thải trừ qua thận và gan. Cần điều chỉnh liều ở suy thận. CHỐNG CHỈ ĐỊNH nếu suy thận nặng + suy gan nặng."
        },
        "side_effects": [
            "Tiêu chảy, buồn nôn, nôn (thường gặp, đặc biệt ở liều cao) - dose-limiting toxicity",
            "Đau bụng, chuột rút",
            "Ức chế tủy xương (giảm bạch cầu, giảm tiểu cầu, thiếu máu) - hiếm, dùng lâu dài",
            "Độc tính cơ (myopathy, rhabdomyolysis) - hiếm, dùng lâu dài",
            "Suy thận (hiếm, thường do độc tính cơ)",
            "Rụng tóc (hiếm)",
            "Phát ban"
        ],
        "mechanism_of_action": "Colchicine ức chế sự di cư của bạch cầu trung tính vào ổ viêm bằng cách gắn vào tubulin, ngăn chặn sự hình thành microtubule, ức chế quá trình thực bào và giải phóng các chất trung gian gây viêm. Colchicine cũng ức chế sự hình thành và giải phóng các tinh thể acid uric, giảm viêm và đau trong cơn gout cấp.",
        "monitoring": [
            "Công thức máu (CBC) - theo dõi ức chế tủy xương (dùng lâu dài)",
            "CK (creatine kinase) - theo dõi độc tính cơ (nếu đau cơ, dùng lâu dài)",
            "Chức năng thận (CrCl) - trước và trong điều trị (cần điều chỉnh liều)",
            "Chức năng gan - trước và trong điều trị (cần điều chỉnh liều)",
            "Triệu chứng tiêu hóa (tiêu chảy, buồn nôn) - dose-limiting",
            "Tương tác thuốc (P-gp/CYP3A4 inhibitors) - Black Box Warning"
        ],
        "interactions": [
            "Chất ức chế P-gp/CYP3A4 mạnh (Clarithromycin, Ketoconazole, Itraconazole, Ritonavir, Cyclosporine): CHỐNG CHỈ ĐỊNH ở người suy thận/gan - Black Box Warning - tăng nồng độ colchicine, có thể tử vong",
            "Statins (atorvastatin, simvastatin): tăng nguy cơ độc tính cơ (myopathy, rhabdomyolysis)",
            "Fibrates (gemfibrozil, fenofibrate): tăng nguy cơ độc tính cơ",
            "Macrolides (erythromycin, clarithromycin): tăng nồng độ colchicine",
            "Verapamil, Diltiazem: tăng nồng độ colchicine",
            "Digoxin: colchicine có thể tăng nồng độ digoxin"
        ],
        "pregnancy": "C - Tránh dùng trừ khi lợi ích vượt trội",
        "precautions": [
            "QUAN TRỌNG: CHỐNG CHỈ ĐỊNH dùng chung với chất ức chế P-gp/CYP3A4 mạnh ở người suy thận/gan - Black Box Warning - có thể tử vong",
            "Liều cao (uống mỗi 2h đến khi tiêu chảy) KHÔNG CÒN ĐƯỢC KHUYẾN CÁO do độc tính cao",
            "Điều chỉnh liều theo chức năng thận và gan",
            "Ngừng ngay nếu có triệu chứng độc tính (tiêu chảy nặng, đau cơ, yếu cơ, giảm bạch cầu)",
            "Thận trọng ở người cao tuổi - tăng nguy cơ độc tính",
            "Thận trọng khi dùng với statins hoặc fibrates - tăng nguy cơ độc tính cơ",
            "Theo dõi công thức máu và CK nếu dùng lâu dài"
        ],
        "pharmacokinetics": {
            "half_life": "27-31 giờ (bình thường), tăng đáng kể ở suy thận/gan hoặc dùng với P-gp/CYP3A4 inhibitors",
            "onset": "12-24 giờ (cơn gout cấp)",
            "duration": "24-48 giờ",
            "protein_binding": "30-50%",
            "clearance": "Thận (thải trừ một phần) và gan (chuyển hóa qua CYP3A4, bài tiết qua P-gp). Cần điều chỉnh liều ở suy thận và gan.",
            "metabolism": "Chuyển hóa qua CYP3A4, bài tiết qua P-gp. Chất ức chế P-gp/CYP3A4 làm tăng nồng độ colchicine đáng kể."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tương tác thuốc gây tử vong: CHỐNG CHỈ ĐỊNH dùng chung với chất ức chế P-gp/CYP3A4 mạnh (Clarithromycin, Ketoconazole, Itraconazole, Ritonavir, Cyclosporine) ở người suy thận hoặc suy gan - có thể gây tử vong do tăng nồng độ colchicine. Độc tính: tiêu chảy nặng, ức chế tủy xương, độc tính cơ có thể xảy ra, đặc biệt ở liều cao hoặc dùng lâu dài.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Chất ức chế P-gp/CYP3A4 mạnh (Clarithromycin, Ketoconazole, Itraconazole, Ritonavir, Cyclosporine)",
                    "mechanism": "Ức chế chuyển hóa (CYP3A4) và bài tiết (P-gp) của colchicine, tăng nồng độ colchicine đáng kể",
                    "effect": "Tăng nồng độ colchicine, tăng độc tính nghiêm trọng (tiêu chảy nặng, ức chế tủy xương, độc tính cơ) - có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI ở người suy thận hoặc suy gan - Black Box Warning. Ở người bình thường: giảm liều colchicine 50-75% hoặc tránh dùng chung."
                }
            ],
            "moderate": [
                {
                    "drug": "Statins (atorvastatin, simvastatin), Fibrates (gemfibrozil, fenofibrate)",
                    "mechanism": "Cộng gộp độc tính cơ",
                    "effect": "Tăng nguy cơ độc tính cơ (myopathy, rhabdomyolysis)",
                    "management": "Thận trọng. Theo dõi CK, triệu chứng đau cơ. Ngừng nếu có dấu hiệu độc tính cơ."
                },
                {
                    "drug": "Macrolides (erythromycin, clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ colchicine",
                    "effect": "Tăng nồng độ colchicine, tăng độc tính",
                    "management": "Thận trọng. Giảm liều colchicine hoặc tránh dùng chung."
                },
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Ức chế P-gp, tăng nồng độ colchicine",
                    "effect": "Tăng nồng độ colchicine, tăng độc tính",
                    "management": "Thận trọng. Giảm liều colchicine."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Colchicine có thể tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Thận trọng. Theo dõi nồng độ digoxin."
                }
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ trừ khi lợi ích vượt trội. Colchicine có thể ảnh hưởng đến phân chia tế bào. Dữ liệu an toàn hạn chế.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Colchicine bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú nếu lợi ích vượt trội. Theo dõi trẻ sơ sinh."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Giảm liều 50%",
            "severe": "CHỐNG CHỈ ĐỊNH nếu kèm suy thận nặng, nếu không thì giảm liều 75% hoặc tránh dùng",
            "notes": "Colchicine chuyển hóa qua gan (CYP3A4) và bài tiết qua P-gp. Cần điều chỉnh liều ở suy gan. CHỐNG CHỈ ĐỊNH nếu suy gan nặng + suy thận nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng, buồn nôn, nôn (dose-limiting toxicity)",
                "Ức chế tủy xương (giảm bạch cầu, giảm tiểu cầu, thiếu máu)",
                "Độc tính cơ (myopathy, rhabdomyolysis) - đau cơ, yếu cơ, tăng CK",
                "Suy thận (thường do rhabdomyolysis)",
                "Rối loạn điện giải (do tiêu chảy nặng)",
                "Có thể tử vong nếu không điều trị"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng colchicine ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ: truyền dịch, bù điện giải, theo dõi dấu hiệu sống",
                "Điều trị ức chế tủy xương: truyền máu, tiểu cầu, G-CSF nếu cần",
                "Điều trị rhabdomyolysis: truyền dịch, điều chỉnh điện giải, lọc máu nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài)"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu, CK, chức năng thận, điện giải, dấu hiệu độc tính cơ"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Acute gout: 1.2mg (hoặc 1mg) ngay khi có triệu chứng, sau đó 0.6mg (hoặc 0.5mg) sau 1 giờ. Prophylaxis: 0.5-0.6mg x 1-2 lần/ngày.",
                "notes": "QUAN TRỌNG: Liều cao (uống mỗi 2h đến khi tiêu chảy) KHÔNG CÒN ĐƯỢC KHUYẾN CÁO. Tổng liều ngày đầu không quá 1.8mg cho cơn gout cấp."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Colchicine (Colcrys)",
                "ACR Guidelines - Gout Management",
                "UpToDate - Colchicine: Drug Information",
                "EULAR Recommendations - Gout Management",
                "Nhà thuốc An Khang - Colchicine",
                "MIMS Vietnam - Colchicine"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines, extensive clinical data"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"gastrointestinal": "Severe diarrhea (dose-limiting toxicity)", "hematologic": "Bone marrow suppression (rare, long-term use)", "musculoskeletal": "Myopathy (rare, long-term use)", "renal": "Nephrotoxicity (with renal/hepatic impairment + P-gp/CYP3A4 inhibitors)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["CBC (bone marrow suppression risk with long-term use)", "CK (myopathy risk with long-term use)", "Renal function (nephrotoxicity risk, especially with P-gp/CYP3A4 inhibitors)", "Hepatic function (hepatotoxicity risk, especially with P-gp/CYP3A4 inhibitors)", "P-gp/CYP3A4 interactions (clarithromycin, ketoconazole - contraindicated with renal/hepatic impairment)", "GI symptoms (diarrhea - dose-limiting)"],
            "look_alike_sound_alike": ["Colchicine", "Colestipol"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Fatal Drug Interactions (P-gp/CYP3A4 inhibitors with renal/hepatic impairment)",
            "ACR Guidelines - Gout Management",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    "Febuxostat":     {
        "group": "Rheumatology - Gout (Xanthine Oxidase Inhibitor)",
        "vietnamese_name": "Febuxostat, Feburic, Uloric",
        "brand_names": {
            "common": [
                "Uloric",
                "Adenuric"
            ],
            "vietnam": [
                "Feburic 40mg",
                "Feburic 80mg",
                "Febus"
            ],
        },
        "manufacturer": {
            "primary": "Takeda Pharmaceuticals (Uloric), Menarini Group (Adenuric)",
            "vietnam": [
                "Takeda Pharmaceuticals",
                "Menarini Group",
                "Các công ty dược phẩm Việt Nam (generic - Feburic, Febus, v.v.)"
            ],
            "notes": "Takeda Pharmaceuticals là nhà sản xuất gốc của Uloric (febuxostat). Có các sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Gout mạn tính (khi không dung nạp hoặc không đáp ứng Allopurinol)",
            "Tăng acid uric máu không triệu chứng (khi cần thiết)",
            "Không cần chỉnh liều ở suy thận nhẹ-trung bình (ưu điểm so với Allopurinol)"
        ],
        "contraindications": [
            "Dùng chung với Azathioprine hoặc Mercaptopurine (CHỐNG CHỈ ĐỊNH tuyệt đối - tăng độc tính tủy xương)",
            "Dị ứng với febuxostat"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dùng chung với Azathioprine hoặc Mercaptopurine (CHỐNG CHỈ ĐỊNH tuyệt đối - tăng độc tính tủy xương nghiêm trọng)",
                "Dị ứng với febuxostat"
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ tử vong tim mạch (Black Box Warning - cao hơn allopurinol)",
                "Suy gan nặng - thận trọng, có thể tăng nguy cơ độc tính",
                "Phụ nữ có thai - tránh dùng trừ khi lợi ích vượt trội"
            ]
        },
        "dosage": {
            "adult_gout_initial": "40mg uống 1 lần/ngày",
            "adult_gout_maintenance": "40mg hoặc 80mg uống 1 lần/ngày (tùy đáp ứng, max 80mg/ngày)",
            "adult_gout_max": "80mg/ngày",
            "adult_renal_crcl_30_60": "Không cần chỉnh liều (ưu điểm so với allopurinol)",
            "adult_renal_crcl_under_30": "Thận trọng, có thể cần giảm liều",
            "adult_hepatic_impairment": "Thận trọng, có thể cần giảm liều",
            "notes": "QUAN TRỌNG: Cảnh báo an toàn về tim mạch (Cardiovascular death risk) cao hơn Allopurinol (FDA Boxed Warning - vẫn cần thận trọng). Khởi phát cơn Gout cấp khi mới bắt đầu điều trị - nên phối hợp Colchicine/NSAID trong 3-6 tháng đầu. Uống với hoặc không có thức ăn. Không cần chỉnh liều ở suy thận nhẹ-trung bình (ưu điểm so với allopurinol)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "Không cần chỉnh liều (CrCl 30-60 ml/min) - ưu điểm so với allopurinol",
            "under_30": "Thận trọng, có thể cần giảm liều (CrCl <30 ml/min)",
            "dialysis": "Thận trọng, có thể cần giảm liều",
            "notes": "Febuxostat chuyển hóa chủ yếu qua gan, thải trừ một phần qua thận. Không cần chỉnh liều ở suy thận nhẹ-trung bình (ưu điểm so với allopurinol)."
        },
        "side_effects": [
            "Khởi phát cơn Gout cấp khi mới bắt đầu điều trị (nên phối hợp Colchicine/NSAID trong 3-6 tháng đầu)",
            "Tăng nguy cơ tử vong tim mạch (Black Box Warning - cao hơn allopurinol)",
            "Tăng men gan, viêm gan (hiếm)",
            "Buồn nôn, đau đầu",
            "Phát ban",
            "Ức chế tủy xương (hiếm)"
        ],
        "mechanism_of_action": "Febuxostat ức chế chọn lọc và mạnh Xanthine Oxidase (cả dạng oxy hóa và khử), enzyme chuyển hóa Hypoxanthine -> Xanthine -> Acid Uric. Febuxostat ức chế Xanthine Oxidase mạnh hơn allopurinol, làm giảm sản xuất acid uric hiệu quả hơn. Khác với allopurinol, febuxostat không chuyển hóa thành purine analog, nên không tích lũy trong thận như allopurinol.",
        "monitoring": [
            "Acid uric máu (Target <6 mg/dL cho gout)",
            "Men gan (ALT, AST) - trước và trong điều trị (nguy cơ viêm gan)",
            "Biến cố tim mạch (Black Box Warning - tăng nguy cơ tử vong tim mạch so với allopurinol)",
            "Dấu hiệu cơn gout cấp (có thể khởi phát khi mới bắt đầu điều trị)",
            "Chức năng thận (không cần chỉnh liều ở suy thận nhẹ-trung bình nhưng vẫn nên theo dõi)"
        ],
        "interactions": [
            "Azathioprine, Mercaptopurine: CHỐNG CHỈ ĐỊNH - febuxostat ức chế xanthine oxidase, tăng độc tính tủy xương nghiêm trọng",
            "Theophylline: febuxostat có thể tăng nồng độ theophylline - theo dõi nồng độ",
            "Warfarin: có thể tăng tác dụng chống đông - theo dõi INR",
            "NSAIDs: có thể tăng nguy cơ tác dụng phụ"
        ],
        "pregnancy": "C - Tránh dùng trừ khi lợi ích vượt trội",
        "precautions": [
            "QUAN TRỌNG: Tăng nguy cơ tử vong tim mạch (Black Box Warning - cao hơn allopurinol) - cân nhắc kỹ trước khi dùng, đặc biệt ở bệnh nhân có bệnh tim mạch",
            "Khởi phát cơn Gout cấp khi mới bắt đầu - phối hợp Colchicine/NSAID trong 3-6 tháng đầu",
            "CHỐNG CHỈ ĐỊNH dùng chung với Azathioprine/Mercaptopurine",
            "Theo dõi men gan (nguy cơ viêm gan)",
            "Theo dõi biến cố tim mạch",
            "Không cần chỉnh liều ở suy thận nhẹ-trung bình (ưu điểm so với allopurinol)",
            "Thận trọng ở suy gan nặng"
        ],
        "pharmacokinetics": {
            "half_life": "5-8 giờ (bình thường), tăng ở suy gan",
            "onset": "Giảm acid uric máu trong 1-2 tuần",
            "duration": "12-24 giờ",
            "protein_binding": "99.2%",
            "clearance": "Gan (chuyển hóa chủ yếu qua UGT và CYP). Thận (thải trừ một phần). Không cần chỉnh liều ở suy thận nhẹ-trung bình.",
            "metabolism": "Chuyển hóa chủ yếu qua gan (UGT và CYP). Không tích lũy trong thận như allopurinol."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tăng nguy cơ tử vong tim mạch: febuxostat có nguy cơ tử vong tim mạch cao hơn allopurinol (Black Box Warning). Cân nhắc kỹ trước khi dùng, đặc biệt ở bệnh nhân có bệnh tim mạch. CHỐNG CHỈ ĐỊNH dùng chung với Azathioprine/Mercaptopurine - tăng độc tính tủy xương nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Azathioprine, Mercaptopurine",
                    "mechanism": "Febuxostat ức chế xanthine oxidase, enzyme chuyển hóa azathioprine/mercaptopurine, làm tăng nồng độ và độc tính",
                    "effect": "Tăng độc tính tủy xương nghiêm trọng (giảm bạch cầu, giảm tiểu cầu, suy tủy) - có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng chung."
                }
            ],
            "moderate": [
                {
                    "drug": "Theophylline",
                    "mechanism": "Febuxostat có thể ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ theophylline. Giảm liều theophylline nếu cần."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Febuxostat có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu/ngừng febuxostat. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "minor": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Cộng gộp tác dụng phụ",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng."
                }
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ trừ khi lợi ích vượt trội. Dữ liệu an toàn hạn chế. Có thể ảnh hưởng đến phát triển thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Febuxostat có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "Febuxostat chuyển hóa chủ yếu qua gan (UGT và CYP). Suy gan có thể tăng nguy cơ độc tính (viêm gan). Thận trọng ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Tăng men gan, viêm gan",
                "Ức chế tủy xương (hiếm)",
                "Biến cố tim mạch (tăng nguy cơ)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng febuxostat ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ: truyền dịch, theo dõi dấu hiệu sống",
                "Điều trị viêm gan: hỗ trợ gan, theo dõi men gan",
                "Điều trị ức chế tủy xương: truyền máu, tiểu cầu, G-CSF nếu cần",
                "Theo dõi biến cố tim mạch"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu, men gan, chức năng thận, ECG, dấu hiệu biến cố tim mạch"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Uống 1 lần/ngày. Khởi đầu: 40mg/ngày. Maintenance: 40mg hoặc 80mg/ngày tùy đáp ứng.",
                "notes": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu. Khởi đầu với 40mg/ngày, tăng lên 80mg/ngày nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Uloric (febuxostat)",
                "ACR Guidelines - Gout Management",
                "UpToDate - Febuxostat: Drug Information",
                "CARES Study - Cardiovascular Safety of Febuxostat vs Allopurinol",
                "EULAR Recommendations - Gout Management",
                "Nhà thuốc An Khang - Febuxostat",
                "MIMS Vietnam - Febuxostat"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines, large RCTs (CARES study)"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiovascular", "hepatic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Cardiovascular events (Black Box Warning - increased risk of cardiovascular death vs allopurinol)", "Liver function (ALT, AST - hepatotoxicity risk)", "Serum uric acid", "Azathioprine/mercaptopurine interactions (contraindicated)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cardiovascular Death Risk (higher than allopurinol)",
            "FDA Black Box Warning - Azathioprine/Mercaptopurine Interaction (contraindicated)",
            "ACR Guidelines - Gout Management"
        ],
    },
    "Lesinurad":     {
        "group": "Rheumatology - Gout (URAT1 Inhibitor, Uricosuric)",
        "vietnamese_name": "Lesinurad, Zurampic",
        "brand_names": {
            "common": [
                "Zurampic"
            ],
            "vietnam": [
                "Lesinurad",
                "Zurampic"
            ],
        },
        "manufacturer": {
            "primary": "AstraZeneca (Zurampic)",
            "vietnam": [
                "AstraZeneca",
                "Các công ty dược phẩm Việt Nam (generic - nếu có)"
            ],
            "notes": "AstraZeneca là nhà sản xuất gốc của Zurampic (lesinurad). Thuốc được phê duyệt năm 2015."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Gout mạn tính (kết hợp với allopurinol hoặc febuxostat khi đơn trị không đủ hiệu quả)",
            "Tăng acid uric máu không đáp ứng với allopurinol hoặc febuxostat đơn độc",
            "KHÔNG được dùng đơn độc - phải kết hợp với allopurinol hoặc febuxostat"
        ],
        "contraindications": [
            "Dùng đơn độc (CHỐNG CHỈ ĐỊNH - phải kết hợp với allopurinol hoặc febuxostat)",
            "Suy thận nặng (CrCl <45 ml/min)",
            "Sỏi thận do acid uric hoặc sỏi thận tái phát",
            "Dị ứng với lesinurad"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dùng đơn độc (CHỐNG CHỈ ĐỊNH - phải kết hợp với allopurinol hoặc febuxostat)",
                "Suy thận nặng (CrCl <45 ml/min)",
                "Sỏi thận do acid uric hoặc sỏi thận tái phát",
                "Dị ứng với lesinurad"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 45-60 ml/min) - thận trọng, theo dõi chức năng thận",
                "Tiền sử sỏi thận - tăng nguy cơ sỏi thận",
                "Phụ nữ có thai - tránh dùng trừ khi lợi ích vượt trội"
            ]
        },
        "dosage": {
            "adult_gout_combination": "200mg uống 1 lần/ngày, PHẢI kết hợp với allopurinol (≥300mg/ngày) hoặc febuxostat (≥40mg/ngày)",
            "adult_renal_crcl_45_60": "Thận trọng, theo dõi chức năng thận",
            "adult_renal_crcl_under_45": "CHỐNG CHỈ ĐỊNH (CrCl <45 ml/min)",
            "notes": "QUAN TRỌNG: KHÔNG được dùng đơn độc - phải kết hợp với allopurinol (≥300mg/ngày) hoặc febuxostat (≥40mg/ngày). Uống với thức ăn và nước đầy đủ (≥2 lít/ngày) để tránh sỏi thận. Uống cùng lúc với allopurinol hoặc febuxostat."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "45_60": "Thận trọng, theo dõi chức năng thận (CrCl 45-60 ml/min)",
            "under_45": "CHỐNG CHỈ ĐỊNH - không dùng (CrCl <45 ml/min)",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Lesinurad thải trừ qua thận. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <45 ml/min). Tăng nguy cơ sỏi thận nếu không uống đủ nước."
        },
        "side_effects": [
            "Sỏi thận, sỏi niệu quản (tăng nguy cơ nếu không uống đủ nước)",
            "Suy thận cấp (hiếm)",
            "Buồn nôn, đau đầu",
            "Phát ban",
            "Tăng men gan (hiếm)"
        ],
        "mechanism_of_action": "Lesinurad là URAT1 (urate transporter 1) inhibitor, ức chế tái hấp thu acid uric ở ống thận gần, tăng bài tiết acid uric qua nước tiểu. Lesinurad hoạt động bằng cách ức chế URAT1 và OAT4 (organic anion transporter 4), giảm tái hấp thu acid uric từ nước tiểu vào máu. Khi kết hợp với allopurinol hoặc febuxostat (ức chế sản xuất acid uric), lesinurad tăng đào thải acid uric, giúp đạt mục tiêu acid uric máu hiệu quả hơn.",
        "monitoring": [
            "Acid uric máu (Target <6 mg/dL cho gout)",
            "Chức năng thận (CrCl) - trước và trong điều trị (CHỐNG CHỈ ĐỊNH nếu CrCl <45 ml/min)",
            "Dấu hiệu sỏi thận (đau lưng, đau bụng, tiểu máu)",
            "Lượng nước uống (≥2 lít/ngày để tránh sỏi thận)",
            "Men gan (nếu có triệu chứng)"
        ],
        "interactions": [
            "Aspirin liều thấp (≤325mg/ngày): có thể giảm hiệu quả lesinurad - tránh dùng",
            "Aspirin liều cao (>325mg/ngày): có thể giảm hiệu quả lesinurad - tránh dùng",
            "Chất ức chế CYP2C9 mạnh (fluconazole, amiodarone): có thể tăng nồng độ lesinurad - thận trọng",
            "NSAIDs: có thể tăng nguy cơ suy thận - thận trọng",
            "Thuốc lợi tiểu: có thể tăng nguy cơ sỏi thận - thận trọng"
        ],
        "pregnancy": "C - Tránh dùng trừ khi lợi ích vượt trội",
        "precautions": [
            "QUAN TRỌNG: KHÔNG được dùng đơn độc - phải kết hợp với allopurinol (≥300mg/ngày) hoặc febuxostat (≥40mg/ngày)",
            "Uống với thức ăn và nước đầy đủ (≥2 lít/ngày) để tránh sỏi thận",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <45 ml/min)",
            "Thận trọng ở tiền sử sỏi thận - tăng nguy cơ sỏi thận",
            "Tránh dùng với aspirin (liều thấp hoặc cao) - giảm hiệu quả",
            "Theo dõi chức năng thận định kỳ",
            "Theo dõi dấu hiệu sỏi thận"
        ],
        "pharmacokinetics": {
            "half_life": "5 giờ",
            "onset": "Giảm acid uric máu trong 1-2 tuần",
            "duration": "12-24 giờ",
            "protein_binding": "98%",
            "clearance": "Thận (thải trừ chủ yếu qua thận). CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <45 ml/min).",
            "metabolism": "Chuyển hóa qua gan (CYP2C9). Chất ức chế CYP2C9 mạnh có thể tăng nồng độ lesinurad."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Suy thận cấp: có thể xảy ra, đặc biệt khi dùng đơn độc hoặc không uống đủ nước. CHỐNG CHỈ ĐỊNH dùng đơn độc - phải kết hợp với allopurinol hoặc febuxostat. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <45 ml/min).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aspirin (liều thấp hoặc cao)",
                    "mechanism": "Aspirin ức chế tác dụng uricosuric của lesinurad",
                    "effect": "Giảm hiệu quả lesinurad, giảm bài tiết acid uric",
                    "management": "Tránh dùng với aspirin. Nếu cần dùng aspirin liều thấp để phòng ngừa tim mạch, cân nhắc không dùng lesinurad."
                }
            ],
            "moderate": [
                {
                    "drug": "Chất ức chế CYP2C9 mạnh (fluconazole, amiodarone)",
                    "mechanism": "Ức chế chuyển hóa lesinurad, tăng nồng độ",
                    "effect": "Tăng nồng độ lesinurad, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "NSAIDs",
                    "mechanism": "Cộng gộp nguy cơ suy thận",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận."
                },
                {
                    "drug": "Thuốc lợi tiểu",
                    "mechanism": "Giảm thể tích nước tiểu, tăng nguy cơ sỏi thận",
                    "effect": "Tăng nguy cơ sỏi thận",
                    "management": "Thận trọng. Đảm bảo uống đủ nước (≥2 lít/ngày)."
                }
            ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ trừ khi lợi ích vượt trội. Dữ liệu an toàn hạn chế. Có thể ảnh hưởng đến phát triển thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Lesinurad có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, tránh dùng nếu có thể",
            "notes": "Lesinurad chuyển hóa một phần qua gan (CYP2C9). Suy gan có thể tăng nguy cơ độc tính. Thận trọng ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Sỏi thận, sỏi niệu quản (đau lưng, đau bụng, tiểu máu)",
                "Suy thận cấp",
                "Buồn nôn, nôn",
                "Tăng men gan"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng lesinurad ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ: truyền dịch, theo dõi dấu hiệu sống",
                "Điều trị sỏi thận: truyền dịch, giảm đau, can thiệp nếu cần",
                "Điều trị suy thận cấp: truyền dịch, lọc máu nếu cần"
            ],
            "monitoring": "Dấu hiệu sống, chức năng thận, dấu hiệu sỏi thận, men gan"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn",
                "timing": "Uống 1 lần/ngày (200mg), cùng lúc với allopurinol hoặc febuxostat. Uống với nước đầy đủ (≥2 lít/ngày).",
                "notes": "QUAN TRỌNG: Uống với thức ăn và nước đầy đủ (≥2 lít/ngày) để tránh sỏi thận. PHẢI kết hợp với allopurinol (≥300mg/ngày) hoặc febuxostat (≥40mg/ngày)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zurampic (lesinurad)",
                "ACR Guidelines - Gout Management",
                "UpToDate - Lesinurad: Drug Information",
                "EULAR Recommendations - Gout Management"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal"],
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": True,
            "requires_monitoring": [
                "Black Box Warning - Must be used in combination with allopurinol or febuxostat (NOT monotherapy)",
                "Renal function (CrCl - contraindicated if <45 ml/min)",
                "Kidney stones (increased risk - ensure adequate hydration ≥2L/day)",
                "Acute renal failure (Black Box Warning - risk if monotherapy or inadequate hydration)",
                "Serum uric acid (target <6 mg/dL)",
                "Aspirin interaction (contraindicated - reduces efficacy)"
            ]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Acute Renal Failure (if monotherapy or inadequate hydration)",
            "FDA Black Box Warning - Must be used in combination with allopurinol or febuxostat (NOT monotherapy)",
            "ACR Guidelines - Gout Management",
            "EULAR Recommendations - Gout Management"
        ],
        "last_updated": "2025-01-20"
    },
    "Pegloticase":     {
        "group": "Rheumatology - Gout (Uricase Enzyme)",
        "vietnamese_name": "Pegloticase, Krystexxa",
        "brand_names": {
            "common": [
                "Krystexxa"
            ],
            "vietnam": [
                "Pegloticase",
                "Krystexxa"
            ],
        },
        "manufacturer": {
            "primary": "Horizon Therapeutics (Krystexxa)",
            "vietnam": [
                "Horizon Therapeutics",
                "Các công ty dược phẩm Việt Nam (generic - nếu có)"
            ],
            "notes": "Horizon Therapeutics là nhà sản xuất gốc của Krystexxa (pegloticase). Thuốc được phê duyệt năm 2010."
        },
        "administration": [
            "IV (Truyền tĩnh mạch)"
        ],
        "indications": [
            "Gout mạn tính không đáp ứng hoặc không dung nạp với các liệu pháp hạ acid uric khác (allopurinol, febuxostat)",
            "Gout mạn tính kháng trị (refractory gout)",
            "Tăng acid uric máu nặng không đáp ứng với điều trị thông thường"
        ],
        "contraindications": [
            "Dị ứng với pegloticase hoặc bất kỳ thành phần nào của thuốc",
            "G6PD deficiency (thiếu G6PD) - CHỐNG CHỈ ĐỊNH tuyệt đối (nguy cơ tan máu)",
            "Dùng đồng thời với các thuốc hạ acid uric khác (allopurinol, febuxostat, probenecid) - có thể giảm hiệu quả"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với pegloticase hoặc bất kỳ thành phần nào của thuốc",
                "G6PD deficiency (thiếu G6PD) - CHỐNG CHỈ ĐỊNH tuyệt đối (nguy cơ tan máu nghiêm trọng)",
                "Dùng đồng thời với các thuốc hạ acid uric khác (allopurinol, febuxostat, probenecid) - có thể giảm hiệu quả"
            ],
            "tương_đối": [
                "Tiền sử phản ứng dị ứng nghiêm trọng - tăng nguy cơ phản vệ",
                "Suy tim sung huyết - tăng nguy cơ phản ứng dị ứng",
                "Phụ nữ có thai - tránh dùng trừ khi lợi ích vượt trội"
            ]
        },
        "dosage": {
            "adult_gout_refractory": "8mg IV truyền tĩnh mạch (ít nhất 120 phút) mỗi 2 tuần/lần",
            "adult_infusion_rate": "Truyền CHẬM trong ít nhất 120 phút (2 giờ), không được truyền nhanh hơn",
            "adult_premedication": "Khuyến cáo dùng premedication: corticosteroid (methylprednisolone 125mg IV) + antihistamine (diphenhydramine) trước truyền để giảm nguy cơ phản ứng dị ứng",
            "notes": "QUAN TRỌNG: Phải kiểm tra G6PD trước khi dùng - CHỐNG CHỈ ĐỊNH nếu thiếu G6PD. Truyền CHẬM trong ít nhất 120 phút. Khuyến cáo dùng premedication để giảm nguy cơ phản ứng dị ứng. Ngừng các thuốc hạ acid uric khác (allopurinol, febuxostat) trước khi bắt đầu pegloticase. Theo dõi sát trong và sau truyền để phát hiện phản ứng dị ứng."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "Không cần chỉnh liều (CrCl 30-60 ml/min)",
            "under_30": "Thận trọng, có thể cần điều chỉnh (CrCl <30 ml/min)",
            "dialysis": "Có thể dùng, nhưng thận trọng",
            "notes": "Pegloticase là enzyme, không phụ thuộc vào chức năng thận để thải trừ. Không cần điều chỉnh liều ở suy thận."
        },
        "side_effects": [
            "Phản ứng dị ứng nghiêm trọng, phản vệ (rất thường gặp - Black Box Warning) - có thể xảy ra trong hoặc sau truyền",
            "Tan máu (hemolysis) ở bệnh nhân thiếu G6PD - CHỐNG CHỈ ĐỊNH",
            "Methemoglobinemia ở bệnh nhân thiếu G6PD",
            "Khởi phát cơn gout cấp (thường gặp trong 6 tháng đầu)",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Phát ban, ngứa",
            "Tăng huyết áp"
        ],
        "mechanism_of_action": "Pegloticase là uricase enzyme (urate oxidase) được pegylate hóa, chuyển hóa acid uric thành allantoin (chất dễ hòa tan và dễ đào thải qua nước tiểu). Bằng cách chuyển hóa acid uric thành allantoin, pegloticase làm giảm nhanh và mạnh nồng độ acid uric trong máu. Pegloticase được dùng cho bệnh nhân gout mạn tính kháng trị, không đáp ứng hoặc không dung nạp với các liệu pháp hạ acid uric khác.",
        "monitoring": [
            "G6PD trước khi bắt đầu điều trị - CHỐNG CHỈ ĐỊNH nếu thiếu G6PD",
            "Phản ứng dị ứng, phản vệ trong và sau truyền - Black Box Warning (theo dõi sát trong ít nhất 1 giờ sau truyền)",
            "Acid uric máu (giảm nhanh trong vài giờ sau truyền)",
            "Dấu hiệu tan máu (thiếu máu, vàng da) - đặc biệt ở bệnh nhân thiếu G6PD",
            "Methemoglobinemia (xanh tím, khó thở) - đặc biệt ở bệnh nhân thiếu G6PD",
            "Dấu hiệu cơn gout cấp (có thể khởi phát trong 6 tháng đầu)",
            "Huyết áp (có thể tăng)"
        ],
        "interactions": [
            "Các thuốc hạ acid uric khác (allopurinol, febuxostat, probenecid): có thể giảm hiệu quả pegloticase - ngừng trước khi bắt đầu pegloticase",
            "Các thuốc ức chế miễn dịch: có thể tăng nguy cơ nhiễm trùng",
            "Các thuốc gây tan máu: tăng nguy cơ tan máu ở bệnh nhân thiếu G6PD"
        ],
        "pregnancy": "C - Tránh dùng trừ khi lợi ích vượt trội",
        "precautions": [
            "QUAN TRỌNG: Phải kiểm tra G6PD trước khi dùng - CHỐNG CHỈ ĐỊNH nếu thiếu G6PD (nguy cơ tan máu nghiêm trọng)",
            "QUAN TRỌNG: Nguy cơ phản ứng dị ứng nghiêm trọng, phản vệ - Black Box Warning (theo dõi sát trong và sau truyền)",
            "Khuyến cáo dùng premedication: corticosteroid + antihistamine trước truyền để giảm nguy cơ phản ứng dị ứng",
            "Truyền CHẬM trong ít nhất 120 phút, không được truyền nhanh hơn",
            "Ngừng các thuốc hạ acid uric khác (allopurinol, febuxostat) trước khi bắt đầu pegloticase",
            "Theo dõi sát trong và sau truyền (ít nhất 1 giờ) để phát hiện phản ứng dị ứng",
            "Khởi phát cơn gout cấp có thể xảy ra trong 6 tháng đầu - phối hợp Colchicine/NSAID để dự phòng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (enzyme, không phải thuốc hóa học)",
            "onset": "Giảm acid uric máu trong vài giờ sau truyền",
            "duration": "2 tuần (truyền mỗi 2 tuần)",
            "protein_binding": "Không áp dụng",
            "clearance": "Chuyển hóa acid uric thành allantoin, không phụ thuộc vào chức năng thận để thải trừ. Không cần điều chỉnh liều ở suy thận.",
            "metabolism": "Enzyme, chuyển hóa acid uric thành allantoin"
        },
        "storage": "Bảo quản ở 2-8°C (tủ lạnh), tránh đông lạnh, tránh ánh sáng. Sau khi pha, dùng ngay hoặc trong 4 giờ nếu bảo quản ở 2-8°C.",
        "black_box_warnings": "Phản ứng dị ứng nghiêm trọng, phản vệ: có thể xảy ra trong hoặc sau truyền, có thể đe dọa tính mạng. Theo dõi sát trong và sau truyền. CHỐNG CHỈ ĐỊNH ở bệnh nhân thiếu G6PD - nguy cơ tan máu nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Các thuốc hạ acid uric khác (allopurinol, febuxostat, probenecid)",
                    "mechanism": "Có thể giảm hiệu quả pegloticase",
                    "effect": "Giảm hiệu quả pegloticase, giảm khả năng hạ acid uric",
                    "management": "Ngừng các thuốc hạ acid uric khác trước khi bắt đầu pegloticase."
                }
            ],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch",
                    "mechanism": "Cộng gộp ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Theo dõi dấu hiệu nhiễm trùng."
                }
            ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ trừ khi lợi ích vượt trội. Dữ liệu an toàn hạn chế. Có thể ảnh hưởng đến phát triển thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Pegloticase có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Pegloticase là enzyme, không phụ thuộc vào chức năng gan để chuyển hóa. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng dị ứng nghiêm trọng, phản vệ (khó thở, phù mạch, sốc)",
                "Tan máu (thiếu máu, vàng da) - đặc biệt ở bệnh nhân thiếu G6PD",
                "Methemoglobinemia (xanh tím, khó thở) - đặc biệt ở bệnh nhân thiếu G6PD"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng truyền ngay lập tức nếu có phản ứng dị ứng",
                "Điều trị phản vệ: epinephrine, corticosteroid, antihistamine, truyền dịch, hỗ trợ hô hấp",
                "Điều trị tan máu: truyền máu nếu cần, theo dõi hemoglobin",
                "Điều trị methemoglobinemia: methylene blue nếu cần",
                "Theo dõi sát tại bệnh viện"
            ],
            "monitoring": "Dấu hiệu sống, dấu hiệu phản vệ, hemoglobin, methemoglobin, dấu hiệu tan máu"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 8mg trong 250ml NaCl 0,9% hoặc D5W.",
                "infusion_rate": "Truyền CHẬM trong ít nhất 120 phút (2 giờ), không được truyền nhanh hơn. Dùng dây truyền riêng với bộ lọc.",
                "compatibility": ["NaCl 0,9%", "D5W"],
                "incompatibility": [
                    "Trộn chung với thuốc khác",
                    "Dung dịch chứa chất bảo quản"
                ],
                "premedication": "Khuyến cáo: corticosteroid (methylprednisolone 125mg IV) + antihistamine (diphenhydramine) trước truyền để giảm nguy cơ phản ứng dị ứng",
                "notes": "QUAN TRỌNG: Phải kiểm tra G6PD trước khi dùng. Truyền CHẬM trong ít nhất 120 phút. Theo dõi sát trong và sau truyền (ít nhất 1 giờ) để phát hiện phản ứng dị ứng. Khuyến cáo dùng premedication."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Krystexxa (pegloticase)",
                "ACR Guidelines - Gout Management",
                "UpToDate - Pegloticase: Drug Information",
                "EULAR Recommendations - Gout Management"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines, large RCTs"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hematologic", "immunologic"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - G6PD screening (contraindicated if G6PD deficiency - severe hemolysis risk)",
                "Black Box Warning - Anaphylaxis (severe allergic reactions during or after infusion - monitor closely for at least 1 hour post-infusion)",
                "Hemolysis (in G6PD deficient patients - contraindicated)",
                "Methemoglobinemia (in G6PD deficient patients - contraindicated)",
                "Serum uric acid (rapid decrease within hours after infusion)",
                "Acute gout flares (common in first 6 months - prophylaxis with colchicine/NSAID recommended)"
            ]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Anaphylaxis (severe allergic reactions)",
            "FDA Black Box Warning - G6PD Deficiency (contraindicated - severe hemolysis risk)",
            "ACR Guidelines - Gout Management",
            "EULAR Recommendations - Gout Management"
        ],
        "last_updated": "2025-01-20"
    },
    "Probenecid":     {
        "group": "Rheumatology - Gout (Uricosuric Agent)",
        "vietnamese_name": "Probenecid",
        "brand_names": {
            "common": [
                "Probalan",
                "Benemid"
            ],
            "vietnam": [
                "Probenecid",
                "Probalan"
            ],
        },
        "manufacturer": {
            "primary": "Multiple manufacturers (Merck, Mylan, v.v.)",
            "vietnam": [
                "Nhiều nhà sản xuất (Merck, Mylan, v.v.)",
                "Các công ty dược phẩm Việt Nam (generic)"
            ],
            "notes": "Probenecid có nhiều nhà sản xuất do là thuốc generic. Merck là một trong những nhà sản xuất ban đầu."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Gout mạn tính (tăng bài tiết acid uric qua thận)",
            "Tăng nồng độ kháng sinh beta-lactam trong máu (penicillin, cephalosporin) - chỉ định phụ",
            "Điều trị bệnh giang mai (kết hợp với penicillin)"
        ],
        "contraindications": [
            "Sỏi thận do acid uric hoặc sỏi thận tái phát",
            "Suy thận nặng (CrCl <30 ml/min)",
            "Dị ứng với probenecid",
            "Aspirin liều cao (>325mg/ngày) - giảm hiệu quả probenecid"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Sỏi thận do acid uric hoặc sỏi thận tái phát",
                "Suy thận nặng (CrCl <30 ml/min)",
                "Dị ứng với probenecid"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60 ml/min) - thận trọng, có thể cần giảm liều",
                "Tiền sử sỏi thận - tăng nguy cơ sỏi thận",
                "Aspirin liều cao (>325mg/ngày) - giảm hiệu quả probenecid",
                "Phụ nữ có thai - tránh dùng trừ khi lợi ích vượt trội"
            ]
        },
        "dosage": {
            "adult_gout_initial": "250mg uống 2 lần/ngày trong tuần đầu",
            "adult_gout_maintenance": "500mg uống 2 lần/ngày (có thể tăng đến 1-2g/ngày nếu cần)",
            "adult_gout_max": "2g/ngày (chia 2-4 lần)",
            "adult_antibiotic_adjunct": "500mg uống 4 lần/ngày (để tăng nồng độ penicillin/cephalosporin)",
            "adult_renal_crcl_30_60": "Thận trọng, có thể cần giảm liều",
            "adult_renal_crcl_under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30 ml/min)",
            "notes": "Uống với thức ăn và nước đầy đủ (≥2 lít/ngày) để tránh sỏi thận. Tránh dùng với aspirin liều cao (>325mg/ngày) - giảm hiệu quả. Kiềm hóa nước tiểu (sodium bicarbonate hoặc potassium citrate) có thể giúp giảm nguy cơ sỏi thận."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "Thận trọng, có thể cần giảm liều (CrCl 30-60 ml/min)",
            "under_30": "CHỐNG CHỈ ĐỊNH - không dùng (CrCl <30 ml/min)",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Probenecid thải trừ qua thận. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 ml/min). Tăng nguy cơ sỏi thận nếu không uống đủ nước."
        },
        "side_effects": [
            "Sỏi thận, sỏi niệu quản (tăng nguy cơ nếu không uống đủ nước)",
            "Buồn nôn, nôn, đau đầu",
            "Phát ban, ngứa",
            "Chóng mặt",
            "Suy thận cấp (hiếm)"
        ],
        "mechanism_of_action": "Probenecid là uricosuric agent, ức chế tái hấp thu acid uric ở ống thận gần, tăng bài tiết acid uric qua nước tiểu. Probenecid cũng ức chế bài tiết các acid hữu cơ khác ở ống thận, làm tăng nồng độ penicillin và các kháng sinh beta-lactam khác trong máu (chỉ định phụ).",
        "monitoring": [
            "Acid uric máu (Target <6 mg/dL cho gout)",
            "Chức năng thận (CrCl) - trước và trong điều trị (CHỐNG CHỈ ĐỊNH nếu CrCl <30 ml/min)",
            "Dấu hiệu sỏi thận (đau lưng, đau bụng, tiểu máu)",
            "Lượng nước uống (≥2 lít/ngày để tránh sỏi thận)",
            "pH nước tiểu (kiềm hóa nước tiểu có thể giúp giảm nguy cơ sỏi thận)"
        ],
        "interactions": [
            "Aspirin liều cao (>325mg/ngày): giảm hiệu quả probenecid - tránh dùng",
            "Penicillin, Cephalosporin: probenecid tăng nồng độ kháng sinh trong máu (chỉ định phụ)",
            "Methotrexate: probenecid tăng nồng độ methotrexate, tăng độc tính - thận trọng",
            "NSAIDs: có thể tăng nguy cơ suy thận - thận trọng",
            "Acyclovir, Ganciclovir: probenecid tăng nồng độ, tăng độc tính - thận trọng"
        ],
        "pregnancy": "B - Tương đối an toàn, nhưng nên tránh dùng trừ khi cần thiết",
        "precautions": [
            "Uống với thức ăn và nước đầy đủ (≥2 lít/ngày) để tránh sỏi thận",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 ml/min)",
            "Thận trọng ở tiền sử sỏi thận - tăng nguy cơ sỏi thận",
            "Tránh dùng với aspirin liều cao (>325mg/ngày) - giảm hiệu quả",
            "Kiềm hóa nước tiểu (sodium bicarbonate hoặc potassium citrate) có thể giúp giảm nguy cơ sỏi thận",
            "Theo dõi chức năng thận định kỳ",
            "Theo dõi dấu hiệu sỏi thận"
        ],
        "pharmacokinetics": {
            "half_life": "6-12 giờ",
            "onset": "Giảm acid uric máu trong 1-2 tuần",
            "duration": "12-24 giờ",
            "protein_binding": "85-95%",
            "clearance": "Thận (thải trừ chủ yếu qua thận). CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 ml/min).",
            "metabolism": "Chuyển hóa một phần qua gan, thải trừ chủ yếu qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aspirin liều cao (>325mg/ngày)",
                    "mechanism": "Aspirin ức chế tác dụng uricosuric của probenecid",
                    "effect": "Giảm hiệu quả probenecid, giảm bài tiết acid uric",
                    "management": "Tránh dùng với aspirin liều cao. Aspirin liều thấp (≤325mg/ngày) có thể chấp nhận được."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Probenecid ức chế bài tiết methotrexate, tăng nồng độ methotrexate",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính (ức chế tủy xương, độc gan)",
                    "management": "Thận trọng. Giảm liều methotrexate hoặc tránh dùng chung."
                }
            ],
            "moderate": [
                {
                    "drug": "Penicillin, Cephalosporin",
                    "mechanism": "Probenecid ức chế bài tiết kháng sinh, tăng nồng độ kháng sinh",
                    "effect": "Tăng nồng độ kháng sinh trong máu (chỉ định phụ - có thể hữu ích)",
                    "management": "Có thể dùng để tăng nồng độ kháng sinh nếu cần. Theo dõi tác dụng phụ của kháng sinh."
                },
                {
                    "drug": "Acyclovir, Ganciclovir",
                    "mechanism": "Probenecid ức chế bài tiết, tăng nồng độ",
                    "effect": "Tăng nồng độ acyclovir/ganciclovir, tăng độc tính",
                    "management": "Thận trọng. Giảm liều acyclovir/ganciclovir nếu cần."
                },
                {
                    "drug": "NSAIDs",
                    "mechanism": "Cộng gộp nguy cơ suy thận",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận."
                }
            ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Tương đối an toàn trong thai kỳ, nhưng nên tránh dùng trừ khi cần thiết. Dữ liệu an toàn hạn chế.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Probenecid bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú nếu lợi ích vượt trội. Theo dõi trẻ sơ sinh."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, tránh dùng nếu có thể",
            "notes": "Probenecid chuyển hóa một phần qua gan. Suy gan có thể tăng nguy cơ độc tính. Thận trọng ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Sỏi thận, sỏi niệu quản (đau lưng, đau bụng, tiểu máu)",
                "Suy thận cấp",
                "Buồn nôn, nôn",
                "Chóng mặt"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng probenecid ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ: truyền dịch, theo dõi dấu hiệu sống",
                "Điều trị sỏi thận: truyền dịch, giảm đau, can thiệp nếu cần",
                "Điều trị suy thận cấp: truyền dịch, lọc máu nếu cần"
            ],
            "monitoring": "Dấu hiệu sống, chức năng thận, dấu hiệu sỏi thận"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn",
                "timing": "Uống 2-4 lần/ngày tùy liều. Gout: 250mg x 2 lần/ngày tuần đầu, sau đó 500mg x 2 lần/ngày. Uống với nước đầy đủ (≥2 lít/ngày).",
                "notes": "Uống với thức ăn và nước đầy đủ (≥2 lít/ngày) để tránh sỏi thận. Kiềm hóa nước tiểu có thể giúp giảm nguy cơ sỏi thận."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Probenecid",
                "ACR Guidelines - Gout Management",
                "UpToDate - Probenecid: Drug Information",
                "EULAR Recommendations - Gout Management"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines, extensive clinical data"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": [
                "Renal function (CrCl - contraindicated if <30 ml/min)",
                "Kidney stones (increased risk - ensure adequate hydration ≥2L/day)",
                "Serum uric acid (target <6 mg/dL)",
                "Aspirin interaction (high dose >325mg/day reduces efficacy)",
                "Methotrexate interaction (increases methotrexate levels - reduce dose)"
            ]
        },
        "guideline_tags": [
            "ACR Guidelines - Gout Management",
            "EULAR Recommendations - Gout Management",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-01-20"
    },
}
