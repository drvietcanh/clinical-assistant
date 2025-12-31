"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Beta-lactams

BETA_LACTAMS_DRUGS = {
    "Amoxicillin": {
        "group": "Antibiotic - Beta-lactam (Penicillin)",
        "vietnamese_name": "Amoxicillin, Amoxil, Amoxicillin 500mg",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp trên/dưới",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn răng miệng",
            "Nhiễm khuẩn tai mũi họng",
            "Helicobacter pylori (kết hợp với PPI và clarithromycin)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam",
            "Nhiễm trùng do vi khuẩn tiết beta-lactamase (cần dùng amoxicillin-clavulanate)"
        ],
        "dosage": {
            "adult_standard": "250-500mg x 3 lần/ngày hoặc 500-875mg x 2 lần/ngày",
            "adult_severe": "500-1000mg x 3 lần/ngày",
            "adult_h_pylori": "1000mg x 2 lần/ngày (với PPI và clarithromycin)",
            "pediatric": "20-40mg/kg/ngày chia 3 lần (tối đa 500mg/lần)",
            "notes": "Uống với hoặc không có thức ăn. Dùng đủ thời gian (thường 7-10 ngày)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50% hoặc tăng khoảng cách",
            "hemodialysis": "Liều sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn, nôn",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV)",
            "Nhiễm trùng nấm Candida (oral, vaginal)",
            "Tăng men gan (hiếm)",
            "Viêm thận kẽ (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Methotrexate: tăng độc tính methotrexate",
            "Allopurinol: tăng nguy cơ phát ban",
            "Thuốc tránh thai: có thể giảm hiệu quả",
            "Probenecid: tăng nồng độ amoxicillin"
        ],
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Amoxicillin là aminopenicillin (beta-lactam antibiotic), ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs) trên màng tế bào vi khuẩn. Amoxicillin là chất tương tự penicillin nhưng có nhóm amin, giúp tăng khả năng xuyên qua màng ngoài của vi khuẩn Gram-âm và tăng phổ kháng khuẩn. Amoxicillin ức chế enzyme transpeptidase, ngăn chặn liên kết chéo giữa các chuỗi peptidoglycan trong thành tế bào vi khuẩn, dẫn đến làm suy yếu và vỡ thành tế bào khi vi khuẩn phân chia. Amoxicillin có phổ kháng khuẩn rộng: Gram-dương (Streptococcus, Enterococcus, một số Staphylococcus không kháng penicillinase), Gram-âm (H. influenzae, E. coli, Proteus mirabilis, Salmonella, Shigella), và một số kỵ khí. Không hiệu quả với vi khuẩn tiết beta-lactamase (cần kết hợp với clavulanate).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine) - hiếm viêm thận kẽ",
            "Dấu hiệu nhiễm C. difficile",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV, CMV)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Phát ban thường gặp, đặc biệt ở bệnh nhân nhiễm virus (EBV, CMV) - không phải dị ứng thật",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Uống với hoặc không có thức ăn (hấp thu tốt trong cả hai trường hợp)",
            "Dùng đúng liều và đủ thời gian để tránh kháng thuốc",
            "Không dùng cho nhiễm trùng do vi khuẩn tiết beta-lactamase (cần amoxicillin-clavulanate)",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "q8h hoặc q12h tùy liều",
            "protein_binding": "17-20%",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận (60-70% bài tiết nguyên dạng qua nước tiểu trong 6-8 giờ), cần điều chỉnh thận ở suy thận nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng bột pha suspension: bảo quản trong tủ lạnh sau khi pha, dùng trong 10-14 ngày.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ phản ứng dị ứng nặng (sốc phản vệ) ở bệnh nhân dị ứng penicillin. Phát ban thường gặp và có thể nhầm với dị ứng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Amoxicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng amoxicillin. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Amoxicillin làm giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính (giảm bạch cầu, độc gan, độc thận)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate, theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính."
                }
            ],
            "moderate": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Cơ chế chưa rõ ràng, nhưng allopurinol làm tăng nguy cơ phản ứng da nghiêm trọng với amoxicillin.",
                    "effect": "Tăng nguy cơ phát ban, phản ứng dị ứng (đặc biệt phát ban maculopapular)",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi dấu hiệu phát ban. Ngừng ngay nếu có phát ban nặng hoặc phản ứng dị ứng."
                },
                {
                    "drug": "Thuốc tránh thai nội tiết",
                    "mechanism": "Amoxicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, giảm tái hấp thu estrogen, giảm hiệu quả thuốc tránh thai.",
                    "effect": "Có thể giảm hiệu quả thuốc tránh thai, tăng nguy cơ mang thai",
                    "management": "Khuyến nghị sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng amoxicillin và 7 ngày sau khi ngừng thuốc."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết amoxicillin ở ống thận, làm tăng nồng độ amoxicillin.",
                    "effect": "Tăng nồng độ amoxicillin, tăng thời gian bán thải",
                    "management": "Có thể dùng để tăng nồng độ amoxicillin nếu cần. Theo dõi tác dụng phụ. Giảm liều amoxicillin nếu cần."
                }
            ],
            "minor": [
                {
                    "drug": "Antacids",
                    "mechanism": "Antacids có thể giảm nhẹ hấp thu amoxicillin.",
                    "effect": "Giảm nhẹ hấp thu amoxicillin",
                    "management": "Cách 2 giờ nếu có thể. Không ảnh hưởng đáng kể ở liều điều trị thông thường."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng amoxicillin hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate",
                "Dùng với allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng amoxicillin hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate",
                "Dùng với allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Amoxicillin phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.",
            "lactation": {
                "safety": "Compatible",
                "details": "Amoxicillin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Penicillin là một trong những kháng sinh an toàn nhất khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận, không chuyển hóa ở gan.",
            "moderate": "Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận.",
            "severe": "Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận.",
            "notes": "Amoxicillin chủ yếu thải qua thận (60-70% trong 6-8 giờ), không chuyển hóa ở gan. Suy gan không ảnh hưởng đến nồng độ amoxicillin."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                "Triệu chứng thần kinh: Kích động, co giật (hiếm, thường ở liều rất cao)",
                "Triệu chứng thận: Tăng creatinine, suy thận cấp (hiếm)",
                "Triệu chứng da: Phát ban, mày đay"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay amoxicillin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Điều trị triệu chứng tiêu hóa: Chống nôn nếu cần, truyền dịch nếu mất nước, theo dõi điện giải",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), theo dõi hô hấp",
                "Lọc máu (hemodialysis) có thể loại bỏ một phần amoxicillin nhưng không được khuyến nghị thường quy"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu da trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng ngay amoxicillin, rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ, theo dõi dấu hiệu sinh tồn, điều trị triệu chứng tiêu hóa và thần kinh, lọc máu có thể loại bỏ một phần nhưng không được khuyến nghị thường quy."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Hấp thu tốt trong cả hai trường hợp. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ.",
                "timing": "Uống 2-3 lần/ngày tùy liều (250-500mg x 3 lần/ngày hoặc 500-875mg x 2 lần/ngày). Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều."
            },
            "iv": {
                "reconstitution": "N/A - Chỉ có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Amoxicillin chỉ có dạng uống. Nếu cần dạng IV, dùng amoxicillin-clavulanate hoặc ampicillin."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Amoxicillin",
                "UpToDate - Amoxicillin: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },
    
    "Amoxicillin suspension": {'group': 'Antibiotic - Beta-lactam (Penicillin)', 'vietnamese_name':
        'Amoxicillin suspension, Amoxicillin sirô', 'administration': ['PO'],
        'indications': ['Nhiễm khuẩn đường hô hấp', 'Nhiễm khuẩn tai mũi họng',
        'Nhiễm khuẩn đường tiết niệu', 'Nhiễm khuẩn da mô mềm',
        'Helicobacter pylori (phối hợp)'], 'contraindications': [
        'Dị ứng penicillin', 'Dị ứng beta-lactam'], 'dosage': {
        'pediatric_otitis': '80-90mg/kg/ngày chia 2 lần (10 ngày)',
        'pediatric_pneumonia': '80-100mg/kg/ngày chia 3-4 lần', 'pediatric_uti':
        '25-50mg/kg/ngày chia 3 lần', 'pediatric_suspension_common':
        '20-40mg/kg/ngày chia 2-3 lần', 'notes':
        'Có dạng suspension 125mg/5ml, 250mg/5ml cho trẻ em. Uống với hoặc không thức ăn'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều hoặc tăng khoảng cách', 'under_30':
        'Liều thấp hơn, khoảng cách dài hơn'}, 'side_effects': ['Tiêu chảy',
        'Buồn nôn', 'Phát ban', 'Nhiễm trùng nấm Candida',
        'Giảm bạch cầu (hiếm)'], 'interactions': ['Warfarin: tăng INR',
        'Methotrexate: tăng độc tính', 'Allopurinol: tăng nguy cơ phát ban',
        'Thuốc tránh thai: có thể giảm hiệu quả'], 'pregnancy': 'B - An toàn',
        'mechanism_of_action':
        'Amoxicillin là aminopenicillin (beta-lactam antibiotic), ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs) trên màng tế bào vi khuẩn. Amoxicillin là chất tương tự penicillin nhưng có nhóm amin, giúp tăng khả năng xuyên qua màng ngoài của vi khuẩn Gram-âm và tăng phổ kháng khuẩn. Amoxicillin ức chế enzyme transpeptidase, ngăn chặn liên kết chéo giữa các chuỗi peptidoglycan trong thành tế bào vi khuẩn, dẫn đến làm suy yếu và vỡ thành tế bào khi vi khuẩn phân chia. Amoxicillin có phổ kháng khuẩn rộng: Gram-dương (Streptococcus, Enterococcus, một số Staphylococcus không kháng penicillinase), Gram-âm (H. influenzae, E. coli, Proteus mirabilis, Salmonella, Shigella), và một số kỵ khí. Không hiệu quả với vi khuẩn tiết beta-lactamase (cần kết hợp với clavulanate). Dạng suspension phù hợp cho trẻ em, dễ uống và hấp thu tốt.'
        , 'monitoring': [
        'Dấu hiệu nhiễm trùng: sốt, WBC, CRP (theo dõi đáp ứng điều trị)',
        'Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để đánh giá hiệu quả',
        'Dấu hiệu dị ứng: phát ban, mề đay, khó thở, sốc phản vệ (đặc biệt ở lần đầu tiên dùng)'
        , 'Tiêu chảy (phổ biến, có thể là nhiễm C. difficile nếu nặng)',
        'Chức năng thận (creatinine) nếu dùng liều cao hoặc suy thận',
        'Dấu hiệu nhiễm C. difficile: tiêu chảy nặng, đau bụng, sốt (cần ngừng và điều trị)'
        , 'Chức năng gan (ALT, AST) nếu có triệu chứng (hiếm)',
        'Công thức máu (giảm bạch cầu, thiếu máu hiếm)',
        'INR nếu dùng với warfarin (tăng nguy cơ chảy máu)'], 'precautions': [
        'Không dùng ở bệnh nhân dị ứng penicillin hoặc beta-lactam (phản ứng chéo với cephalosporin ~5-10%)'
        , 'Lắc kỹ suspension trước khi dùng (thuốc lắng xuống đáy)',
        'Có thể uống với hoặc không thức ăn (hấp thu tốt)',
        'Dùng đủ liều và đủ thời gian (thường 7-10 ngày) để tránh kháng thuốc',
        'Thận trọng ở bệnh nhân suy thận (giảm liều hoặc tăng khoảng cách)',
        'Thận trọng ở bệnh nhân có tiền sử nhiễm C. difficile (tăng nguy cơ tái phát)'
        , 'Thận trọng với allopurinol (tăng nguy cơ phát ban)',
        'Thận trọng với methotrexate (amoxicillin làm giảm thải trừ methotrexate, tăng độc tính)'
        , 'Có thể giảm hiệu quả thuốc tránh thai (dùng biện pháp dự phòng)',
        'Theo dõi tiêu chảy - nếu nặng hoặc kéo dài, có thể là nhiễm C. difficile',
        'Dùng đúng liều theo cân nặng ở trẻ em (tính theo mg/kg)'],
        'pharmacokinetics': {'half_life': '1-1.5 giờ', 'onset':
        '1-2 giờ (đạt nồng độ đỉnh trong máu)', 'duration':
        '6-8 giờ (dùng 2-3 lần/ngày)', 'protein_binding': '20%', 'clearance':
        'Thận: bài tiết chủ yếu qua nước tiểu (không thay đổi, 60-70% trong 6-8 giờ). Một phần nhỏ qua mật. Hấp thu tốt qua đường uống (75-90%), không bị ảnh hưởng bởi thức ăn. Dạng suspension hấp thu tương tự viên nén.'
        }, 'storage':
        'Bảo quản suspension ở nhiệt độ phòng (15-30°C) hoặc trong tủ lạnh (2-8°C) - theo hướng dẫn trên nhãn. Lắc kỹ trước khi dùng. Sau khi pha (nếu là bột pha nước): bảo quản trong tủ lạnh (2-8°C), dùng trong vòng 7-14 ngày (theo hướng dẫn). Tránh đông lạnh. Để nơi khô ráo, tránh ánh sáng trực tiếp, tránh xa tầm tay trẻ em.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Methotrexate', 'mechanism':
        'Amoxicillin làm giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate.'
        , 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, độc gan, độc thận, viêm niêm mạc)'
        , 'management':
        'Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi công thức máu, chức năng gan, thận chặt chẽ. Có thể cần giảm liều methotrexate.'
        }, {'drug': 'Allopurinol', 'mechanism':
        'Cơ chế chưa rõ ràng, nhưng allopurinol làm tăng nguy cơ phản ứng da nghiêm trọng với amoxicillin.'
        , 'effect':
        'Tăng nguy cơ phát ban nghiêm trọng, SJS, TEN (đe dọa tính mạng)',
        'management':
        'Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu phát ban. Ngừng ngay nếu có phát ban.'
        }], 'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Amoxicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, ảnh hưởng đến chuyển hóa vitamin K, tăng tác dụng warfarin.'
        , 'effect': 'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên khi dùng amoxicillin. Điều chỉnh liều warfarin nếu cần.'
        }, {'drug': 'Thuốc tránh thai (estrogen)', 'mechanism':
        'Amoxicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, giảm tái hấp thu estrogen, giảm hiệu quả thuốc tránh thai.'
        , 'effect': 'Giảm hiệu quả thuốc tránh thai, tăng nguy cơ có thai',
        'management':
        'Dùng biện pháp tránh thai dự phòng (bao cao su) trong thời gian dùng amoxicillin và 7 ngày sau.'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng penicillin - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (phản ứng chéo với cephalosporin ~5-10%)'
        , 'Dị ứng beta-lactam', 'Sốc phản vệ với penicillin trước đây'],
        'tương_đối': [
        'Dị ứng cephalosporin - thận trọng (phản ứng chéo ~5-10%)',
        'Nhiễm C. difficile trước đây - tăng nguy cơ tái phát',
        'Suy thận nặng - giảm liều hoặc tăng khoảng cách',
        'Đang dùng methotrexate - tăng độc tính methotrexate',
        'Đang dùng allopurinol - tăng nguy cơ phát ban']},
        'contraindications_detail': {'tuyệt_đối': [
        'Dị ứng penicillin - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (phản ứng chéo với cephalosporin ~5-10%)'
        , 'Dị ứng beta-lactam', 'Sốc phản vệ với penicillin trước đây'],
        'tương_đối': [
        'Dị ứng cephalosporin - thận trọng (phản ứng chéo ~5-10%)',
        'Nhiễm C. difficile trước đây - tăng nguy cơ tái phát',
        'Suy thận nặng - giảm liều hoặc tăng khoảng cách',
        'Đang dùng methotrexate - tăng độc tính methotrexate',
        'Đang dùng allopurinol - tăng nguy cơ phát ban']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Amoxicillin là category B - an toàn trong thai kỳ. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Không có bằng chứng về dị tật thai nhi. Có thể dùng trong tất cả các tam cá nguyệt.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Amoxicillin bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Có thể gây tiêu chảy nhẹ hoặc phát ban ở trẻ, nhưng hiếm.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. An toàn cho trẻ bú mẹ. Theo dõi dấu hiệu tiêu chảy hoặc phát ban ở trẻ.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận, không chuyển hóa ở gan.'
        , 'moderate':
        'Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận.',
        'severe':
        'Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận.',
        'notes':
        'Amoxicillin chủ yếu thải qua thận (60-70% trong 6-8 giờ), không chuyển hóa ở gan. Suy gan không ảnh hưởng đến nồng độ amoxicillin.'
        }, 'overdose_management': {'symptoms': [
        'Tiêu chảy nặng (có thể là nhiễm C. difficile)', 'Buồn nôn, nôn',
        'Phát ban, mề đay', 'Sốc phản vệ (hiếm nhưng nguy hiểm)',
        'Co giật (với liều rất cao, suy thận)',
        'Rối loạn điện giải (natri cao nếu dùng liều lớn)'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng amoxicillin ngay lập tức',
        'Nếu sốc phản vệ: epinephrine, corticosteroids, antihistamines, hỗ trợ hô hấp'
        ,
        'Nếu tiêu chảy nặng: điều trị C. difficile nếu xác định (metronidazole, vancomycin)'
        , 'Nếu co giật: benzodiazepines (diazepam, lorazepam)',
        'Điều chỉnh điện giải nếu cần', 'Hỗ trợ hô hấp và tuần hoàn nếu cần',
        'Theo dõi dấu hiệu sinh tồn'], 'monitoring':
        'Dấu hiệu sinh tồn, dấu hiệu dị ứng, tiêu chảy, điện giải, dấu hiệu nhiễm C. difficile'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Hấp thu tốt, không bị ảnh hưởng bởi thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.'
        , 'timing':
        'Uống 2-3 lần/ngày tùy chỉ định, cách đều. Lắc kỹ suspension trước khi dùng (thuốc lắng xuống đáy). Dùng đúng liều theo cân nặng ở trẻ em (tính theo mg/kg).'
        }, 'iv': {'reconstitution': 'N/A - chỉ có dạng uống', 'infusion_rate':
        'N/A', 'compatibility': [], 'incompatibility': [], 'notes':
        'Chỉ có dạng uống (suspension)'}}, 'references': {'primary_sources': [
        'FDA Drug Label - Amoxicillin',
        'UpToDate - Amoxicillin: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ], 'last_updated': '2025-02-04',         'evidence_level':
        'A - Dựa trên FDA drug labels và dữ liệu lâm sàng'}},
    
    "Amoxicillin-clavulanate": {'group':
        'Antibiotic - Beta-lactam (Penicillin + Beta-lactamase inhibitor)',
        'vietnamese_name': 'Amoxicillin-clavulanate, Augmentin, Amoclav',
        'administration': ['PO', 'IV'], 'indications': [
        'Nhiễm khuẩn đường hô hấp trên/dưới', 'Nhiễm khuẩn đường tiết niệu',
        'Nhiễm khuẩn da mô mềm', 'Nhiễm khuẩn răng miệng',
        'Nhiễm khuẩn tai mũi họng (Trẻ em)'], 'contraindications': [
        'Dị ứng penicillin', 'Viêm gan do amoxicillin-clavulanate trước đây',
        'Dị ứng beta-lactam'], 'dosage': {'adult_po':
        '875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày',
        'pediatric_po_suspension':
        '20-40mg amoxicillin/kg/ngày chia 2-3 lần (tối đa 875mg/125mg)',
        'pediatric_po_tablet':
        '25-45mg amoxicillin/kg/ngày chia 2 lần (trên 40kg: dùng liều người lớn)',
        'adult_iv': '1000/200mg IV mỗi 8 giờ', 'pediatric_iv':
        '90mg amoxicillin/kg/ngày chia 3 lần (tối đa 1000/200mg mỗi 8 giờ)',
        'notes':
        'Có dạng suspension cho trẻ em. Uống với thức ăn để giảm tiêu chảy'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều hoặc tăng khoảng cách', 'under_30':
        'Liều thấp hơn, khoảng cách dài hơn'}, 'side_effects': [
        'Tiêu chảy (phổ biến)', 'Buồn nôn', 'Phát ban',
        'Viêm gan (hiếm nhưng nguy hiểm)', 'Nhiễm trùng nấm Candida'],
        'interactions': ['Warfarin: tăng INR',
        'Methotrexate: tăng độc tính methotrexate',
        'Allopurinol: tăng nguy cơ phát ban',
        'Thuốc tránh thai: có thể giảm hiệu quả'], 'pregnancy': 'B - An toàn',
        'mechanism_of_action':
        'Amoxicillin: aminopenicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Clavulanate: beta-lactamase inhibitor, bảo vệ amoxicillin khỏi bị phân hủy bởi beta-lactamase. Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với H. influenzae, E. coli, và một số kỵ khí. Clavulanate không có hoạt tính kháng khuẩn riêng. Được dùng rộng rãi trong nhiễm trùng đường hô hấp, tiết niệu, da và mô mềm.'
        , 'monitoring': ['Dấu hiệu nhiễm trùng (sốt, WBC)',
        'Cấy máu và cấy từ vị trí nhiễm trùng',
        'Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan (đặc biệt với clavulanate)'
        , 'Dấu hiệu nhiễm C. difficile',
        'Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV)',
        'Chức năng thận (creatinine) - hiếm viêm thận kẽ'], 'precautions': [
        'Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)',
        'Nguy cơ viêm gan (đặc biệt do clavulanate) - thường nhất thời, hiếm nặng, tăng ở nam giới, dùng kéo dài'
        , 'Theo dõi men gan, ngừng nếu tăng nặng',
        'Phát ban thường gặp, đặc biệt ở bệnh nhân nhiễm virus (EBV, CMV) - không phải dị ứng thật'
        , 'Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy',
        'Uống với thức ăn để giảm kích ứng dạ dày và tăng hấp thu',
        'Dùng đúng liều và đủ thời gian để tránh kháng thuốc',
        'Không dùng cho nhiễm trùng do Pseudomonas hoặc Enterococcus kháng'],
        'pharmacokinetics': {'half_life': '1 giờ (amoxicillin và clavulanate)',
        'onset': '1-2 giờ (PO)', 'duration': 'q8h hoặc q12h tùy công thức',
        'protein_binding': '17-20% (amoxicillin), 22-30% (clavulanate)',
        'metabolism': 'Một phần trong gan', 'clearance':
        'Chủ yếu qua thận, cần điều chỉnh thận ở suy thận nặng'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Sau khi pha (suspension): bảo quản trong tủ lạnh 10 ngày, sau đó vứt bỏ.'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, nguy cơ viêm gan (đặc biệt do clavulanate) có thể nặng, đặc biệt ở nam giới và dùng kéo dài. Phát ban thường gặp và có thể nhầm với dị ứng.'
        , 'drug_interactions': {'major': [{'drug': 'Warfarin', 'mechanism':
        'Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.'
        , 'effect': 'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu',
        'management':
        'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng amoxicillin-clavulanate. Điều chỉnh liều warfarin nếu cần.'
        }, {'drug': 'Methotrexate', 'mechanism':
        'Amoxicillin-clavulanate ức chế bài tiết methotrexate ở ống thận, làm giảm thải trừ methotrexate.'
        , 'effect':
        'Tăng nồng độ methotrexate, tăng độc tính (giảm bạch cầu, thiếu máu, độc gan, độc thận)'
        , 'management':
        'TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate, theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính.'
        }], 'moderate': [{'drug': 'Allopurinol', 'mechanism':
        'Cơ chế chưa rõ ràng, có thể liên quan đến phản ứng miễn dịch.',
        'effect':
        'Tăng nguy cơ phát ban, phản ứng dị ứng (đặc biệt phát ban maculopapular)',
        'management':
        'Thận trọng khi dùng đồng thời. Theo dõi dấu hiệu phát ban. Ngừng ngay nếu có phát ban nặng hoặc phản ứng dị ứng.'
        }, {'drug': 'Thuốc tránh thai nội tiết', 'mechanism':
        'Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen, giảm nồng độ estrogen.'
        , 'effect':
        'Có thể giảm hiệu quả thuốc tránh thai, tăng nguy cơ mang thai',
        'management':
        'Khuyến nghị sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng amoxicillin-clavulanate và 7 ngày sau khi ngừng thuốc.'
        }, {'drug': 'Probenecid', 'mechanism':
        'Probenecid ức chế bài tiết amoxicillin ở ống thận, làm tăng nồng độ amoxicillin.'
        , 'effect': 'Tăng nồng độ amoxicillin, tăng tác dụng phụ', 'management':
        'Có thể dùng để tăng nồng độ amoxicillin nếu cần. Theo dõi tác dụng phụ. Giảm liều amoxicillin nếu cần.'
        }], 'minor': [{'drug': 'Antacids', 'mechanism':
        'Antacids có thể giảm nhẹ hấp thu amoxicillin.', 'effect':
        'Giảm nhẹ hấp thu amoxicillin', 'management':
        'Cách 2 giờ nếu có thể. Không ảnh hưởng đáng kể ở liều điều trị thông thường.'
        }]},         'contraindications': {'tuyệt_đối': [
        'Dị ứng amoxicillin, clavulanate, hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam'
        ,
        'Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao'
        ,
        'Viêm gan do amoxicillin-clavulanate trước đây - nguy cơ tái phát cao, có thể nặng hơn'
        ], 'tương_đối': [
        'Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng',
        'Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách',
        'Suy gan - thận trọng, có thể giảm chuyển hóa',
        'Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)',
        'Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát',
        'Dùng với methotrexate - tăng độc tính methotrexate',
        'Dùng với allopurinol - tăng nguy cơ phát ban']},
        'contraindications_detail': {'tuyệt_đối': [
        'Dị ứng amoxicillin, clavulanate, hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam'
        ,
        'Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao'
        ,
        'Viêm gan do amoxicillin-clavulanate trước đây - nguy cơ tái phát cao, có thể nặng hơn'
        ], 'tương_đối': [
        'Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng',
        'Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách',
        'Suy gan - thận trọng, có thể giảm chuyển hóa',
        'Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)',
        'Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát',
        'Dùng với methotrexate - tăng độc tính methotrexate',
        'Dùng với allopurinol - tăng nguy cơ phát ban']},
        'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'Amoxicillin-clavulanate phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Amoxicillin và clavulanate bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Penicillin là một trong những kháng sinh an toàn nhất khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban).'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Amoxicillin và clavulanate chuyển hóa một phần qua gan nhưng không đáng kể.'
        , 'moderate':
        'Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.'
        , 'severe':
        'Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.'
        , 'notes':
        'Amoxicillin và clavulanate chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua thận (60-70% bài tiết nguyên dạng qua nước tiểu). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, nguy cơ viêm gan do clavulanate tăng ở bệnh nhân có bệnh gan, đặc biệt nam giới và dùng kéo dài. Theo dõi chặt chẽ chức năng gan.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng',
        'Triệu chứng thần kinh: Kích động, co giật (hiếm, thường ở liều rất cao)',
        'Triệu chứng thận: Tăng creatinine, suy thận cấp (hiếm)',
        'Triệu chứng da: Phát ban, mày đay',
        'Triệu chứng gan: Tăng men gan, viêm gan (đặc biệt với clavulanate)',
        'Triệu chứng nghiêm trọng: Co giật, suy thận cấp, viêm gan nặng'],
        'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay amoxicillin-clavulanate',
        'Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)'
        , 'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2',
        'Điều trị triệu chứng tiêu hóa:', '  - Chống nôn nếu cần',
        '  - Truyền dịch nếu mất nước', '  - Theo dõi điện giải',
        'Điều trị co giật nếu có:', '  - Benzodiazepine (diazepam, lorazepam)',
        '  - Theo dõi hô hấp', 'Điều trị tăng men gan/viêm gan nếu có:',
        '  - Theo dõi ALT, AST, bilirubin', '  - Điều trị hỗ trợ gan',
        '  - Nếu viêm gan nặng: điều trị suy gan',
        'Điều trị suy thận cấp nếu có:',
        '  - Theo dõi creatinine, BUN, lượng nước tiểu',
        '  - Điều trị suy thận cấp',
        'Lọc máu (hemodialysis) có thể loại bỏ một phần amoxicillin nhưng không được khuyến nghị thường quy'
        , 'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2'],
        'monitoring':
        'Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST, bilirubin), chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu da trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (suy gan, suy thận, co giật).'
        },
        'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng ngay amoxicillin-clavulanate, rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ, theo dõi dấu hiệu sinh tồn, điều trị triệu chứng tiêu hóa và thần kinh, điều trị tăng men gan/viêm gan nếu có, lọc máu có thể loại bỏ một phần nhưng không được khuyến nghị thường quy.'},
        'administration_instructions': {'oral': {
        'with_food':
        'Uống với thức ăn để giảm kích ứng dạ dày, giảm tiêu chảy, và tăng hấp thu. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.'
        , 'timing':
        'Uống 2-3 lần/ngày tùy công thức (875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày). Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều.'
        }, 'iv': {'reconstitution':
        'Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.'
        , 'infusion_rate':
        'Truyền IV trong 30 phút (không truyền nhanh hơn). Có thể truyền trong 15-20 phút nếu cần nhưng không khuyến nghị.'
        , 'compatibility': ['NaCl 0.9%', 'D5W (Dextrose 5%)',
        "Lactated Ringer's (LR) - thận trọng, kiểm tra tương thích",
        'Nước cất vô trùng'], 'incompatibility': [
        'Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền',
        'Aminoglycosides (mất hoạt tính nếu trộn trực tiếp)',
        'Probenecid (không trộn, dùng riêng)'], 'notes':
        'Truyền IV trong 30 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha.'
        }}, 'pediatric_dosing': {'neonates':
        'Không khuyến cáo cho trẻ sơ sinh <3 tháng tuổi (dữ liệu hạn chế). Nếu cần: 30mg amoxicillin/kg/ngày IV chia 3 lần.',
        'infants':
        '3 tháng - 2 tuổi: 20-40mg amoxicillin/kg/ngày PO chia 2-3 lần (dạng suspension). Hoặc 90mg amoxicillin/kg/ngày IV chia 3 lần. Có dạng suspension 125mg/5ml, 250mg/5ml.',
        'children':
        '2-12 tuổi: 20-45mg amoxicillin/kg/ngày PO chia 2-3 lần (dạng suspension hoặc viên nén). Trên 40kg: dùng liều người lớn. Hoặc 90mg amoxicillin/kg/ngày IV chia 3 lần (tối đa 1000/200mg mỗi 8 giờ).',
        'adolescents':
        '≥12 tuổi hoặc >40kg: Liều người lớn. 875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày PO. Hoặc 1000/200mg IV mỗi 8 giờ.',
        'notes':
        'Có dạng suspension cho trẻ em (125mg/5ml, 250mg/5ml). Uống với thức ăn để giảm tiêu chảy. Tính liều theo amoxicillin (không tính clavulanate). Theo dõi dấu hiệu viêm gan (hiếm nhưng nguy hiểm).'}, 'geriatric_dosing': {'considerations':
        'Người cao tuổi có thể có suy thận phổ biến hơn, cần điều chỉnh liều. Tăng nguy cơ viêm gan (đặc biệt do clavulanate) ở nam giới, dùng kéo dài. Suy gan phổ biến hơn.',
        'dose_adjustment':
        'Điều chỉnh liều theo chức năng thận: CrCl 30-60 → giảm liều hoặc tăng khoảng cách, CrCl <30 → liều thấp hơn, khoảng cách dài hơn. Thận trọng ở suy gan.',
        'monitoring':
        'Theo dõi chức năng gan (ALT, AST) thường xuyên, đặc biệt ở nam giới, dùng kéo dài. Theo dõi chức năng thận (creatinine, CrCl). Theo dõi dấu hiệu viêm gan (vàng da, mệt mỏi). Theo dõi tiêu chảy (có thể là nhiễm C. difficile).'}, 'brand_names': {'vietnam': [
        'Amoxicillin-clavulanate', 'Augmentin', 'Amoclav', 'Clavulanate Stada'], 'common': [
        'Augmentin', 'Amoxicillin-clavulanate', 'Amoclav']}, 'cost_estimate': {'unit': 'VND',
        'range': '8,000 - 40,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Amoxicillin-clavulanate generic thường rẻ hơn (8,000-20,000 VND/viên 625mg). Augmentin (brand) thường đắt hơn (20,000-40,000 VND/viên 625mg). Dạng suspension: 100,000-200,000 VND/lọ 100ml (250mg/5ml).'}, 'references': {'primary_sources': [
        'FDA Label: Augmentin (amoxicillin-clavulanate)',
        'UpToDate: Amoxicillin-clavulanate drug information',
        'Lexicomp: Amoxicillin-clavulanate monograph',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Sanford Guide to Antimicrobial Therapy'], 'last_updated': '2025-02-03',
        'evidence_level':
        'Level 1 - FDA approved, multiple clinical trials, extensive clinical experience'
        }},
    "Ampicillin": {
        "group": "Antibiotic - Beta-lactam (Penicillin)",
        "vietnamese_name": "Ampicillin, Ampicillin sodium",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn huyết",
            "Viêm màng não do Listeria (kết hợp với gentamicin)",
            "Viêm nội tâm mạc do Enterococcus (kết hợp với gentamicin)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam",
            "Nhiễm trùng do vi khuẩn tiết beta-lactamase (cần dùng ampicillin-sulbactam)"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 4-6 giờ",
            "adult_severe": "2g IV mỗi 4 giờ",
            "adult_meningitis": "2g IV mỗi 4 giờ",
            "adult_endocarditis": "2g IV mỗi 4 giờ (kết hợp với gentamicin)",
            "pediatric_standard": "100-200mg/kg/ngày chia 4-6 lần",
            "pediatric_meningitis": "200-300mg/kg/ngày chia 4-6 lần",
            "notes": "Chỉ có dạng IV/IM. Không hiệu quả với vi khuẩn tiết beta-lactamase (cần ampicillin-sulbactam)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 6-8 giờ",
            "under_30": "1-2g IV mỗi 8-12 giờ",
            "hemodialysis": "Bổ sung liều sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn, nôn",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV)",
            "Nhiễm trùng nấm Candida",
            "Tăng men gan (hiếm)",
            "Viêm thận kẽ (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Methotrexate: tăng độc tính methotrexate",
            "Allopurinol: tăng nguy cơ phát ban",
            "Probenecid: tăng nồng độ ampicillin",
            "Aminoglycosides: không pha chung, truyền riêng"
        ],
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Ampicillin là aminopenicillin (beta-lactam antibiotic), ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs) trên màng tế bào vi khuẩn. Ampicillin có nhóm amin, giúp tăng khả năng xuyên qua màng ngoài của vi khuẩn Gram-âm và tăng phổ kháng khuẩn so với penicillin G. Ampicillin có phổ kháng khuẩn: Gram-dương (Streptococcus, Enterococcus, một số Staphylococcus không kháng penicillinase), Gram-âm (H. influenzae, E. coli, Proteus mirabilis, Salmonella, Shigella), và một số kỵ khí. Không hiệu quả với vi khuẩn tiết beta-lactamase (cần kết hợp với sulbactam). Ampicillin thường dùng IV trong bệnh viện, đặc biệt cho nhiễm trùng nặng.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine) - cần điều chỉnh liều ở suy thận",
            "Dấu hiệu nhiễm C. difficile",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV, CMV)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Công thức máu (CBC) - hiếm giảm bạch cầu"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Phát ban thường gặp, đặc biệt ở bệnh nhân nhiễm virus (EBV, CMV) - không phải dị ứng thật",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Không dùng cho nhiễm trùng do vi khuẩn tiết beta-lactamase (cần ampicillin-sulbactam)",
            "Pha trong NS hoặc D5W, truyền IV trong 15-30 phút",
            "Không pha trộn với aminoglycosides (truyền riêng biệt)",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q4h hoặc q6h",
            "protein_binding": "20%",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận (75-85% bài tiết nguyên dạng qua nước tiểu trong 6-8 giờ), cần điều chỉnh thận ở suy thận nặng"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 1 giờ, hoặc trong tủ lạnh 8 giờ. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ phản ứng dị ứng nặng (sốc phản vệ) ở bệnh nhân dị ứng penicillin. Phát ban thường gặp và có thể nhầm với dị ứng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Ampicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng ampicillin. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Ampicillin ức chế bài tiết methotrexate ở ống thận, làm giảm thải trừ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính (giảm bạch cầu, độc gan, độc thận)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate, theo dõi chặt chẽ công thức máu, chức năng gan, thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Cơ chế chưa rõ ràng, nhưng allopurinol làm tăng nguy cơ phản ứng da nghiêm trọng với ampicillin.",
                    "effect": "Tăng nguy cơ phát ban, phản ứng dị ứng",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi dấu hiệu phát ban. Ngừng ngay nếu có phát ban nặng."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ampicillin ở ống thận, làm tăng nồng độ ampicillin.",
                    "effect": "Tăng nồng độ ampicillin, tăng thời gian bán thải",
                    "management": "Có thể dùng để tăng nồng độ ampicillin nếu cần. Theo dõi tác dụng phụ."
                }
            ],
            "minor": [
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn. Ngoài ra, aminoglycosides có thể bị bất hoạt về mặt hóa học bởi beta-lactams khi pha chung.",
                    "effect": "Tăng nguy cơ độc thận, giảm hiệu quả kháng khuẩn của aminoglycosides nếu pha chung",
                    "management": "Không pha chung trong cùng một ống truyền. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ampicillin hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate",
                "Dùng với allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng ampicillin hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate",
                "Dùng với allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ampicillin phân loại B - an toàn trong thai kỳ. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ampicillin bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ampicillin chủ yếu thải qua thận, không chuyển hóa ở gan.",
            "moderate": "Không cần điều chỉnh liều. Ampicillin chủ yếu thải qua thận.",
            "severe": "Không cần điều chỉnh liều. Ampicillin chủ yếu thải qua thận.",
            "notes": "Ampicillin chủ yếu thải qua thận (75-85% trong 6-8 giờ), không chuyển hóa ở gan. Suy gan không ảnh hưởng đến nồng độ ampicillin."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy",
                "Triệu chứng thần kinh: Kích động, co giật (hiếm, thường ở liều rất cao)",
                "Triệu chứng thận: Tăng creatinine, suy thận cấp (hiếm)",
                "Triệu chứng da: Phát ban, mày đay"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay ampicillin",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị triệu chứng tiêu hóa",
                "Điều trị co giật nếu có",
                "Lọc máu có thể loại bỏ một phần ampicillin nhưng không được khuyến nghị thường quy"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận, dấu hiệu da trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng ngay ampicillin, theo dõi dấu hiệu sinh tồn, điều trị triệu chứng tiêu hóa và thần kinh, lọc máu có thể loại bỏ một phần nhưng không được khuyến nghị thường quy."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - Chỉ có dạng IV/IM",
                "timing": "N/A"
            },
            "iv": {
                "reconstitution": "Pha ampicillin với nước cất vô trùng hoặc NaCl 0.9% theo hướng dẫn nhà sản xuất. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 15-30 phút (không truyền nhanh hơn).",
                "compatibility": ["NaCl 0.9%", "D5W"],
                "incompatibility": ["Không pha với aminoglycosides trong cùng đường truyền"],
                "notes": "Chỉ có dạng IV/IM. Không pha trộn với aminoglycosides (truyền riêng biệt)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ampicillin",
                "UpToDate - Ampicillin: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },
    
    "Ampicillin-sulbactam": {
        "group": "Antibiotic - Beta-lactam (Penicillin + Beta-lactamase inhibitor)",
        "vietnamese_name": "Ampicillin-sulbactam, Unasyn",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp dưới",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn phụ khoa",
            "Nhiễm khuẩn huyết"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam",
            "Dị ứng ampicillin hoặc sulbactam"
        ],
        "dosage": {
            "adult_standard": "1.5-3g IV mỗi 6 giờ (tỷ lệ 2:1 ampicillin:sulbactam)",
            "adult_severe": "3g IV mỗi 6 giờ",
            "adult_im": "1.5g IM mỗi 6-8 giờ",
            "pediatric_iv": "150-300mg/kg/ngày (tính theo ampicillin) chia 4 lần",
            "notes": "Tỷ lệ cố định: 2 phần ampicillin : 1 phần sulbactam. Liều tối đa: 12g/ngày (ampicillin). Pha trong 50-100ml NS hoặc D5W, truyền trong 15-30 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1.5-3g IV mỗi 8 giờ",
            "under_30": "1.5g IV mỗi 12 giờ",
            "hemodialysis": "1.5g IV sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Tăng men gan (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Viêm tĩnh mạch tại vị trí tiêm"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Methotrexate: tăng độc tính methotrexate",
            "Allopurinol: tăng nguy cơ phát ban",
            "Aminoglycosides: không pha chung, truyền riêng"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ampicillin: aminopenicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), ngăn chặn quá trình transpeptidation và transglycosylation. Sulbactam: beta-lactamase inhibitor (irreversible), bảo vệ ampicillin khỏi bị phân hủy bởi beta-lactamase (TEM, SHV, OXA). Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với Enterobacteriaceae (E. coli, Klebsiella, Proteus), H. influenzae, và một số kỵ khí. Sulbactam cũng có hoạt tính kháng khuẩn riêng với Acinetobacter baumannii. Tỷ lệ cố định 2:1 (ampicillin:sulbactam) được thiết kế để tối ưu hóa hiệu quả.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Công thức máu (CBC) - hiếm giảm bạch cầu",
            "Dấu hiệu dị ứng (phát ban, mề đay)"
        ],
        "precautions": [
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Pha trong NS hoặc D5W, truyền IV trong 15-30 phút",
            "Không pha trộn với aminoglycosides (truyền riêng biệt)",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài",
            "IM: pha với lidocaine 1% để giảm đau"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (ampicillin và sulbactam)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q6h hoặc q8h",
            "protein_binding": "20% (ampicillin), 38% (sulbactam)",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận (75-85% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 1 giờ, hoặc trong tủ lạnh 8 giờ. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ phản ứng dị ứng nặng (sốc phản vệ) ở bệnh nhân dị ứng penicillin. Nguy cơ nhiễm C. difficile.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Ampicillin-sulbactam có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng ampicillin-sulbactam. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Ampicillin-sulbactam ức chế bài tiết methotrexate ở ống thận, làm giảm thải trừ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính (giảm bạch cầu, độc gan, độc thận)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate, theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính."
                }
            ],
            "moderate": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Cơ chế chưa rõ ràng, có thể liên quan đến phản ứng miễn dịch.",
                    "effect": "Tăng nguy cơ phát ban, phản ứng dị ứng",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi dấu hiệu phát ban. Ngừng ngay nếu có phát ban nặng."
                },
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn. Ngoài ra, aminoglycosides có thể bị bất hoạt về mặt hóa học bởi beta-lactams khi pha chung.",
                    "effect": "Tăng nguy cơ độc thận, giảm hiệu quả kháng khuẩn của aminoglycosides nếu pha chung",
                    "management": "Không pha chung trong cùng một ống truyền. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ampicillin ở ống thận, làm tăng nồng độ ampicillin.",
                    "effect": "Tăng nồng độ ampicillin, tăng thời gian bán thải",
                    "management": "Có thể dùng để tăng nồng độ ampicillin nếu cần. Theo dõi tác dụng phụ. Giảm liều ampicillin-sulbactam nếu cần."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng và 7 ngày sau khi ngừng."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ampicillin, sulbactam, hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Suy gan - thận trọng, có thể giảm chuyển hóa",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate",
                "Dùng với allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng ampicillin, sulbactam, hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Suy gan - thận trọng, có thể giảm chuyển hóa",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate",
                "Dùng với allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ampicillin-sulbactam phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ampicillin và sulbactam bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Penicillin là một trong những kháng sinh an toàn nhất khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ampicillin và sulbactam chuyển hóa một phần qua gan nhưng không đáng kể.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.",
            "notes": "Ampicillin và sulbactam chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua thận (75-85% bài tiết nguyên dạng qua nước tiểu). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Không cần điều chỉnh liều thường quy ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao)",
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy",
                "Triệu chứng thận: Suy thận cấp, tăng creatinine (hiếm với liều thông thường)",
                "Triệu chứng da: Phát ban, mày đay",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay ampicillin-sulbactam",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ ampicillin và sulbactam)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ ampicillin và sulbactam nếu suy thận nặng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu da, dấu hiệu dị ứng trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (suy thận cấp, co giật)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng ngay ampicillin-sulbactam, điều trị co giật nếu có, điều trị dị ứng nếu có (epinephrine nếu sốc phản vệ), điều trị suy thận cấp nếu có, lọc máu có thể loại bỏ ampicillin và sulbactam nếu suy thận nặng."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - chỉ có dạng IV/IM",
                "timing": "N/A - chỉ có dạng IV/IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Thể tích pha: 50-100ml cho liều 1.5-3g. Nồng độ pha: 30mg/ml (1.5g/50ml) đến 15mg/ml (3g/200ml). Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 15-30 phút. Tốc độ: 50ml/15 phút = ~3.3ml/phút (nhanh) hoặc 50ml/30 phút = ~1.7ml/phút (chậm).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Aminoglycosides - có thể bị bất hoạt khi pha chung, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "Truyền IV trong 15-30 phút. Không truyền quá nhanh. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
            },
            "im": {
                "reconstitution": "Pha với nước cất vô trùng hoặc lidocaine 1% (để giảm đau). Thể tích: 3-4ml cho liều 1.5g.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi). Tránh tiêm vào mạch máu.",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ tiêm. Tiêm sâu vào cơ. Không tiêm vào mạch máu."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế). Nếu cần: 150mg/kg/ngày (tính theo ampicillin) IV chia 3-4 lần.",
            "infants": "1-3 tháng: 150-300mg/kg/ngày (tính theo ampicillin) IV chia 4 lần. Theo dõi chức năng thận.",
            "children": ">3 tháng: 150-300mg/kg/ngày (tính theo ampicillin) IV chia 4 lần (tối đa 12g/ngày ampicillin). Điều chỉnh liều theo CrCl nếu suy thận.",
            "adolescents": "≥12 tuổi: Liều người lớn. 1.5-3g IV mỗi 6 giờ.",
            "notes": "Tính liều theo ampicillin (không tính sulbactam). Tỷ lệ cố định 2:1. Điều chỉnh liều theo chức năng thận. Theo dõi chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu dị ứng."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể có suy thận phổ biến hơn, cần điều chỉnh liều. Suy gan phổ biến hơn.",
            "dose_adjustment": "Điều chỉnh liều theo chức năng thận: CrCl 30-60 → 1.5-3g mỗi 8 giờ, CrCl <30 → 1.5g mỗi 12 giờ. Thận trọng ở suy gan.",
            "monitoring": "Theo dõi chức năng thận (creatinine, CrCl) thường xuyên. Theo dõi dấu hiệu nhiễm trùng. Theo dõi tiêu chảy (có thể là nhiễm C. difficile). Theo dõi dấu hiệu dị ứng."
        },
        "brand_names": {
            "vietnam": ["Unasyn", "Ampicillin-sulbactam", "Ampicillin-sulbactam Stada"],
            "common": ["Unasyn", "Ampicillin-sulbactam"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "50,000 - 150,000 VND/lọ (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Ampicillin-sulbactam generic thường rẻ hơn (50,000-100,000 VND/lọ 1.5g). Unasyn (brand) thường đắt hơn (100,000-150,000 VND/lọ 1.5g)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Unasyn (ampicillin-sulbactam)",
                "UpToDate - Ampicillin-sulbactam: Drug Information",
                "Lexicomp - Ampicillin-sulbactam Monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Sanford Guide to Antimicrobial Therapy"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
        }
    },
    
    "Dicloxacillin": {
        "group": "Antibiotic - Beta-lactam (Penicillinase-resistant Penicillin)",
        "vietnamese_name": "Dicloxacillin, Diclocil, Dynapen",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm do S. aureus (MSSA)",
            "Nhiễm khuẩn xương khớp do S. aureus",
            "Viêm nội tâm mạc do S. aureus (kết hợp với gentamicin)",
            "Nhiễm khuẩn đường hô hấp do S. aureus"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "adult_standard": "250-500mg PO x 4 lần/ngày",
            "adult_severe": "500mg PO x 4 lần/ngày",
            "pediatric": "12.5-25mg/kg/ngày PO chia 4 lần (tối đa 2g/ngày)",
            "notes": "Uống 1 giờ trước hoặc 2 giờ sau bữa ăn để tăng hấp thu"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Có thể cần giảm liều nhẹ"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn",
            "Phát ban",
            "Tăng men gan (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Probenecid: tăng nồng độ dicloxacillin"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Dicloxacillin là penicillinase-resistant penicillin (PRP), ức chế tổng hợp thành tế bào vi khuẩn. Khác với penicillin thông thường, dicloxacillin có cấu trúc vòng beta-lactam bền vững, kháng được penicillinase do S. aureus tiết ra. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - MSSA, Staphylococcus epidermidis, Streptococcus). Không hiệu quả với MRSA, Enterococcus, Gram-âm, hoặc kỵ khí. Đặc điểm: chỉ có dạng uống, hấp thu tốt khi uống lúc đói.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - hiếm",
            "Dấu hiệu nhiễm C. difficile"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins",
            "Uống 1 giờ trước hoặc 2 giờ sau bữa ăn để tăng hấp thu",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Không hiệu quả với MRSA - cần dùng vancomycin hoặc daptomycin"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "q6h",
            "protein_binding": "95-98%",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận và gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm",
        "black_box_warnings": "Không có black box warning.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dicloxacillin",
                "UpToDate - Dicloxacillin: Drug Information",
                "IDSA Guidelines - Skin and Soft Tissue Infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ dicloxacillin",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "oral": {
                      "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                      "timing": "Theo chỉ định của bác sĩ",
                      "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
                  }
              },
},
    
    "Nafcillin": {
        "group": "Antibiotic - Beta-lactam (Penicillinase-resistant Penicillin)",
        "vietnamese_name": "Nafcillin, Unipen, Nafcil",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn nặng do S. aureus (MSSA)",
            "Nhiễm khuẩn huyết do S. aureus",
            "Viêm nội tâm mạc do S. aureus",
            "Viêm tủy xương do S. aureus",
            "Nhiễm khuẩn da và mô mềm nặng"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 4-6 giờ",
            "adult_severe": "2g IV mỗi 4 giờ",
            "adult_endocarditis": "2g IV mỗi 4 giờ (kết hợp với gentamicin)",
            "pediatric": "50-100mg/kg/ngày IV chia 4-6 lần (tối đa 12g/ngày)",
            "notes": "Truyền IV trong 30-60 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (thải qua mật)"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Viêm tĩnh mạch (IV)",
            "Tăng men gan (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Độc thận (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Nafcillin là penicillinase-resistant penicillin (PRP), ức chế tổng hợp thành tế bào vi khuẩn. Kháng được penicillinase do S. aureus tiết ra. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - MSSA, Staphylococcus epidermidis, Streptococcus). Không hiệu quả với MRSA, Enterococcus, Gram-âm, hoặc kỵ khí. Đặc điểm: chỉ có dạng IV/IM, thải trừ chủ yếu qua mật (không cần điều chỉnh thận).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - hiếm",
            "Dấu hiệu nhiễm C. difficile",
            "Viêm tĩnh mạch (IV)"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins",
            "Thải trừ chủ yếu qua mật - không cần điều chỉnh thận",
            "Nguy cơ viêm tĩnh mạch - thay đổi vị trí tiêm thường xuyên",
            "Không hiệu quả với MRSA - cần dùng vancomycin hoặc daptomycin",
            "Pha trong NS hoặc D5W, truyền IV trong 30-60 phút"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "4-6 giờ (liều q4-6h)",
            "protein_binding": "90%",
            "metabolism": "Chủ yếu qua gan (mật)",
            "clearance": "Chủ yếu qua mật (80%), một phần qua thận (20%)"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng. Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nafcillin",
                "UpToDate - Nafcillin: Drug Information",
                "IDSA Guidelines - Endocarditis, Skin and Soft Tissue Infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Aminoglycosides: không pha chung",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "iv": {
                      "reconstitution": "Cần tra cứu",
                      "infusion_rate": "Cần tra cứu",
                      "compatibility": [
                          "Cần tra cứu"
                      ],
                      "incompatibility": [],
                      "notes": "Cần tra cứu thêm thông tin chi tiết."
                  }
              },
},
    
    "Oxacillin": {
        "group": "Antibiotic - Beta-lactam (Penicillinase-resistant Penicillin)",
        "vietnamese_name": "Oxacillin, Bactocill, Prostaphlin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn nặng do S. aureus (MSSA)",
            "Nhiễm khuẩn huyết do S. aureus",
            "Viêm nội tâm mạc do S. aureus",
            "Viêm tủy xương do S. aureus",
            "Nhiễm khuẩn da và mô mềm nặng"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 4-6 giờ",
            "adult_severe": "2g IV mỗi 4 giờ",
            "adult_endocarditis": "2g IV mỗi 4 giờ",
            "pediatric": "50-100mg/kg/ngày IV chia 4-6 lần (tối đa 12g/ngày)",
            "notes": "Truyền IV trong 30-60 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Có thể cần giảm liều nhẹ"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Viêm tĩnh mạch (IV)",
            "Tăng men gan (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Độc thận (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Oxacillin là penicillinase-resistant penicillin (PRP), ức chế tổng hợp thành tế bào vi khuẩn. Kháng được penicillinase do S. aureus tiết ra. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - MSSA, Staphylococcus epidermidis, Streptococcus). Không hiệu quả với MRSA, Enterococcus, Gram-âm, hoặc kỵ khí. Đặc điểm: chỉ có dạng IV/IM, thải trừ chủ yếu qua thận (cần điều chỉnh thận ở suy thận nặng).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - hiếm",
            "Chức năng thận (creatinine) - cần điều chỉnh ở suy thận nặng",
            "Dấu hiệu nhiễm C. difficile",
            "Viêm tĩnh mạch (IV)"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins",
            "Điều chỉnh liều ở suy thận nặng (CrCl <10)",
            "Nguy cơ viêm tĩnh mạch - thay đổi vị trí tiêm thường xuyên",
            "Không hiệu quả với MRSA - cần dùng vancomycin hoặc daptomycin",
            "Pha trong NS hoặc D5W, truyền IV trong 30-60 phút"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "4-6 giờ (liều q4-6h)",
            "protein_binding": "90-95%",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận (50-60%), một phần qua mật (40-50%)"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng. Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Oxacillin",
                "UpToDate - Oxacillin: Drug Information",
                "IDSA Guidelines - Endocarditis, Skin and Soft Tissue Infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Aminoglycosides: không pha chung",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "iv": {
                      "reconstitution": "Cần tra cứu",
                      "infusion_rate": "Cần tra cứu",
                      "compatibility": [
                          "Cần tra cứu"
                      ],
                      "incompatibility": [],
                      "notes": "Cần tra cứu thêm thông tin chi tiết."
                  }
              },
},
    "Penicillin V": {
        "group": "Antibiotic - Beta-lactam (Penicillin, Oral)",
        "vietnamese_name": "Penicillin V, Penicillin VK, Phenoxymethylpenicillin",
        "administration": ["PO"],
        "indications": [
            "Viêm họng do Streptococcus (phòng thấp khớp)",
            "Nhiễm trùng đường hô hấp trên",
            "Nhiễm trùng da và mô mềm nhẹ",
            "Nhiễm trùng răng miệng",
            "Phòng ngừa viêm nội tâm mạc (bệnh nhân có bệnh van tim)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam",
            "Nhiễm trùng nặng (cần penicillin G IV)"
        ],
        "dosage": {
            "adult_standard": "250-500mg x 3-4 lần/ngày",
            "adult_strep_throat": "500mg x 2-3 lần/ngày x 10 ngày",
            "adult_endocarditis_prophylaxis": "2g PO 1 giờ trước thủ thuật",
            "pediatric_standard": "25-50mg/kg/ngày chia 3-4 lần",
            "pediatric_strep_throat": "250-500mg x 2-3 lần/ngày x 10 ngày (tùy tuổi)",
            "notes": "Penicillin uống, acid-stable. Uống với hoặc không có thức ăn. Dùng đủ thời gian (thường 10 ngày cho strep throat)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (thải qua thận nhưng an toàn)"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn, nôn",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV)",
            "Nhiễm trùng nấm Candida",
            "Tăng men gan (hiếm)",
            "Phản ứng dị ứng (mày đay, sốc phản vệ)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Methotrexate: tăng độc tính methotrexate",
            "Probenecid: tăng nồng độ penicillin V",
            "Thuốc tránh thai: có thể giảm hiệu quả"
        ],
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Penicillin V (phenoxymethylpenicillin) là penicillin uống, acid-stable (khác với penicillin G bị phá hủy bởi acid dạ dày). Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs) trên màng tế bào vi khuẩn. Penicillin V ức chế enzyme transpeptidase, ngăn chặn liên kết chéo giữa các chuỗi peptidoglycan trong thành tế bào vi khuẩn, dẫn đến làm suy yếu và vỡ thành tế bào khi vi khuẩn phân chia. Phổ kháng khuẩn: Gram-dương (Streptococcus, một số Staphylococcus không kháng penicillinase), một số kỵ khí. Không hiệu quả với vi khuẩn tiết beta-lactamase hoặc Gram-âm. Penicillin V thường dùng cho nhiễm trùng nhẹ đến trung bình, đặc biệt viêm họng do Streptococcus để phòng thấp khớp.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu cần)",
            "Dấu hiệu nhiễm C. difficile",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV, CMV)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu dị ứng (mày đay, sốc phản vệ)"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Phát ban thường gặp, đặc biệt ở bệnh nhân nhiễm virus (EBV, CMV) - không phải dị ứng thật",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Uống với hoặc không có thức ăn (hấp thu tốt trong cả hai trường hợp)",
            "Dùng đúng liều và đủ thời gian để tránh kháng thuốc (đặc biệt quan trọng cho strep throat - 10 ngày)",
            "Không dùng cho nhiễm trùng nặng (cần penicillin G IV)",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "q6h hoặc q8h",
            "protein_binding": "80%",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận (60-80% bài tiết nguyên dạng qua nước tiểu trong 6 giờ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ phản ứng dị ứng nặng (sốc phản vệ) ở bệnh nhân dị ứng penicillin. Phát ban thường gặp và có thể nhầm với dị ứng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Penicillin V có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng penicillin V. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Penicillin V làm giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính (giảm bạch cầu, độc gan, độc thận)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate, theo dõi chặt chẽ công thức máu, chức năng gan, thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết penicillin V ở ống thận, làm tăng nồng độ penicillin V.",
                    "effect": "Tăng nồng độ penicillin V, tăng thời gian bán thải",
                    "management": "Có thể dùng để tăng nồng độ penicillin V nếu cần. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Thuốc tránh thai nội tiết",
                    "mechanism": "Penicillin V có thể ảnh hưởng đến hệ vi khuẩn đường ruột, giảm tái hấp thu estrogen, giảm hiệu quả thuốc tránh thai.",
                    "effect": "Có thể giảm hiệu quả thuốc tránh thai, tăng nguy cơ mang thai",
                    "management": "Khuyến nghị sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng penicillin V và 7 ngày sau khi ngừng thuốc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng penicillin V hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng penicillin V hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Penicillin V phân loại B - an toàn trong thai kỳ. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Penicillin V bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Penicillin V chủ yếu thải qua thận, không chuyển hóa ở gan. Suy gan không ảnh hưởng đến nồng độ penicillin V."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy",
                "Triệu chứng thần kinh: Kích động, co giật (hiếm, thường ở liều rất cao)",
                "Triệu chứng thận: Tăng creatinine (hiếm)",
                "Triệu chứng da: Phát ban, mày đay"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay penicillin V",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị triệu chứng tiêu hóa",
                "Điều trị co giật nếu có",
                "Lọc máu có thể loại bỏ một phần penicillin V nhưng không được khuyến nghị thường quy"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận, dấu hiệu da trong ít nhất 24 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Lọc máu có thể loại bỏ một phần nhưng không được khuyến nghị thường quy."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Hấp thu tốt trong cả hai trường hợp. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ.",
                "timing": "Uống 3-4 lần/ngày (250-500mg mỗi lần). Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều. Đặc biệt quan trọng: dùng đủ 10 ngày cho strep throat để phòng thấp khớp."
            },
            "iv": {
                "reconstitution": "N/A - Chỉ có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Penicillin V chỉ có dạng uống. Nếu cần dạng IV, dùng penicillin G."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Penicillin V",
                "UpToDate - Penicillin V: Drug Information",
                "American Heart Association guidelines (phòng thấp khớp)",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },
    
}

__all__ = ['BETA_LACTAMS_DRUGS']
