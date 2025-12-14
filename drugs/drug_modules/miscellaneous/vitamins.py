"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Vitamins

VITAMINS_DRUGS = {
    "Folic Acid": {'group': 'Hematology - Vitamin', 'vietnamese_name': 'Acid Folic',
        'administration': ['PO'], 'indications': ['Thiếu máu do thiếu folate',
        'Dự phòng dị tật ống thần kinh trong thai kỳ',
        'Bệnh hồng cầu hình liềm', 'Đang dùng methotrexate'],
        'contraindications': ['Dị ứng'], 'dosage': {'adult_deficiency':
        '1-5mg x 1 lần/ngày', 'pregnancy': '0.4-0.8mg x 1 lần/ngày',
        'methotrexate': '5-10mg/tuần (24h sau methotrexate)', 'notes':
        'Dùng kèm vitamin B12 khi thiếu máu'}, 'side_effects': [
        'Hiếm khi có tác dụng phụ', 'Phản ứng dị ứng (hiếm)'], 'interactions':
        [
        'Methotrexate: giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính)',
        'Phenytoin: giảm nồng độ phenytoin'], 'pregnancy':
        'A - Khuyến nghị dùng trong thai kỳ', 'mechanism_of_action':
        'Folic acid (folate, vitamin B9) là coenzyme cần thiết cho tổng hợp DNA và RNA, đặc biệt quan trọng trong quá trình phân chia tế bào. Folic acid được chuyển đổi thành tetrahydrofolate (THF), tham gia vào các phản ứng methyl transfer, tổng hợp purine và pyrimidine (các nucleotide của DNA/RNA). Folic acid cần thiết cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Thiếu folic acid gây thiếu máu hồng cầu to do giảm tổng hợp DNA, dẫn đến tế bào hồng cầu chưa trưởng thành. Folic acid cũng được dùng để giảm độc tính của methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate).'
        , 'monitoring': [
        'Hemoglobin, MCV (mean corpuscular volume) - theo dõi đáp ứng điều trị thiếu máu'
        , 'Nồng độ folate trong máu (nếu cần)',
        'Nồng độ vitamin B12 (thiếu B12 có thể che dấu bởi folic acid)',
        'Đáp ứng điều trị (giảm triệu chứng thiếu máu)',
        'Dấu hiệu dị ứng (hiếm)'], 'precautions': [
        'Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)'
        , 'Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid',
        'Dự phòng dị tật ống thần kinh: bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu'
        ,
        'Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)',
        'Liều cao (>1mg/ngày) có thể che dấu thiếu B12',
        'An toàn trong thai kỳ và cho con bú', 'Hiếm khi có tác dụng phụ',
        'Thận trọng ở bệnh nhân ung thư (folic acid có thể kích thích tế bào ung thư)'
        ], 'pharmacokinetics': {'half_life': 'Không áp dụng (vitamin)', 'onset':
        'Vài ngày đến vài tuần (tác dụng tích tụ)', 'duration':
        'Phụ thuộc vào dự trữ trong cơ thể', 'protein_binding': 'Không đáng kể',
        'clearance': 'Thận (thải trừ qua nước tiểu), một phần dự trữ trong gan'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings': None, 'drug_interactions': {'moderate': [{'drug':
        'Methotrexate', 'mechanism':
        'Folic acid giảm hiệu quả methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate)'
        , 'effect':
        'Giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính methotrexate)',
        'management':
        'Dùng folic acid 24 giờ sau methotrexate (không dùng cùng lúc). Theo dõi đáp ứng điều trị methotrexate'
        }, {'drug': 'Phenytoin', 'mechanism':
        'Folic acid giảm nồng độ phenytoin (cơ chế chưa rõ)', 'effect':
        'Giảm nồng độ phenytoin, giảm hiệu quả chống co giật', 'management':
        'Theo dõi nồng độ phenytoin, có thể cần tăng liều phenytoin'}]},
        'contraindications': {'tuyệt_đối': ['Dị ứng folic acid'], 'tương_đối':
        ['Ung thư - thận trọng (folic acid có thể kích thích tế bào ung thư)',
        'Thiếu vitamin B12 chưa được điều trị - thận trọng (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)'
        ]}, 'pregnancy_lactation': {'fda_category': 'A', 'pregnancy_details':
        'Khuyến nghị dùng trong thai kỳ. Folic acid rất quan trọng cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Nên bắt đầu trước khi có thai 1 tháng và tiếp tục trong 3 tháng đầu thai kỳ. Liều dự phòng: 0.4-0.8mg/ngày. Liều điều trị thiếu máu: 1-5mg/ngày.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Folic acid bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Folic acid trong sữa mẹ có lợi cho trẻ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Liều thường dùng (0.4-5mg/ngày) an toàn cho trẻ bú mẹ'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi liều', 'moderate':
        'Không đổi liều', 'severe': 'Không đổi liều', 'notes':
        'Folic acid là vitamin, không chuyển hóa ở gan. Suy gan không ảnh hưởng đến folic acid'
        }, 'overdose_management': {'symptoms': [
        'Hiếm khi có triệu chứng (folic acid ít độc)', 'Phản ứng dị ứng (hiếm)',
        'Có thể che dấu thiếu B12 nếu dùng liều cao (>1mg/ngày)'], 'antidote':
        'Không có thuốc giải độc đặc hiệu', 'treatment': [
        'Ngừng thuốc nếu có phản ứng dị ứng',
        'Điều trị hỗ trợ: Truyền dịch nếu cần',
        'Kiểm tra nồng độ vitamin B12 nếu dùng liều cao lâu dài',
        'Điều trị dị ứng nếu có (antihistamine, corticosteroid)'], 'monitoring':
        'Triệu chứng lâm sàng, dấu hiệu dị ứng, nồng độ vitamin B12 (nếu dùng liều cao lâu dài)'
        }, 'reversal_agents': {'available': False, 'agents': None, 'notes':
        'Không có thuốc giải độc đặc hiệu. Folic acid ít độc, hiếm khi cần điều trị đặc biệt'
        }, 'administration_instructions': {'oral': {'with_food':
        'Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ (nếu có)'
        , 'timing':
        'Với thiếu máu: 1-5mg x 1 lần/ngày. Với dự phòng dị tật ống thần kinh: 0.4-0.8mg x 1 lần/ngày (bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu). Với methotrexate: 5-10mg/tuần (dùng 24 giờ sau methotrexate, không dùng cùng lúc)'
        , 'notes':
        'Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12). Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid. Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)'
        }}, 'references': {'primary_sources': ['FDA Drug Label - Folic Acid',
        'UpToDate - Folic acid drug information',
        'CDC Guidelines for folic acid supplementation in pregnancy',
        'WHO Guidelines for folic acid supplementation',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - Guidelines dựa trên chứng cứ từ CDC, WHO và FDA'}},
    "Vitamin C": {
        'group': 'Vitamins/Supplements - Vitamin C',
        'vietnamese_name': 'Vitamin C, Ascorbic Acid',
        'administration': ['PO', 'IV'],
        'indications': [
            'Thiếu vitamin C (scurvy)',
            'Dự phòng thiếu vitamin C',
            'Hỗ trợ miễn dịch',
            'Vết thương chậm lành',
            'Bệnh nhân lọc máu (thiếu vitamin C)',
            'Nhiễm trùng (hỗ trợ)'
        ],
        'contraindications': [
            'Dị ứng vitamin C',
            'Bệnh thận oxalate (tăng nguy cơ sỏi thận)'
        ],
        'dosage': {
            'adult_deficiency': '100-200mg x 2-3 lần/ngày (PO)',
            'adult_maintenance': '60-100mg x 1 lần/ngày',
            'adult_iv': '200-500mg IV (bệnh nhân lọc máu)',
            'pediatric': '30-50mg x 1 lần/ngày',
            'notes': 'Liều cao (>1g/ngày) có thể gây tiêu chảy'
        },
        'side_effects': [
            'Tiêu chảy (liều cao >1g/ngày)',
            'Buồn nôn',
            'Sỏi thận oxalate (liều cao lâu dài)',
            'Tăng hấp thu sắt (có thể gây quá tải sắt)'
        ],
        'interactions': [
            'Sắt: tăng hấp thu sắt',
            'Warfarin: có thể giảm hiệu quả warfarin (liều cao)',
            'Aspirin: tăng bài tiết vitamin C'
        ],
        'pregnancy': 'A - An toàn',
        'mechanism_of_action': 'Vitamin C (ascorbic acid) là vitamin tan trong nước, đóng vai trò quan trọng như một chất chống oxy hóa và cofactor cho nhiều enzyme. Vitamin C cần thiết cho tổng hợp collagen (protein chính của mô liên kết, xương, sụn, mạch máu), giúp vết thương lành nhanh. Vitamin C cũng tham gia vào tổng hợp catecholamines (dopamine, norepinephrine), carnitine, và chuyển hóa cholesterol. Vitamin C hoạt động như chất chống oxy hóa, bảo vệ tế bào khỏi tổn thương do gốc tự do, và tái tạo vitamin E (tocopherol) từ dạng oxy hóa. Vitamin C cũng tăng cường chức năng miễn dịch (tăng hoạt động của bạch cầu, tăng sản xuất interferon). Thiếu vitamin C gây scurvy (chảy máu nướu, vết thương chậm lành, yếu mệt).',
        'monitoring': [
            'Đáp ứng điều trị (giảm triệu chứng thiếu vitamin C)',
            'Dấu hiệu tiêu chảy (nếu dùng liều cao >1g/ngày)',
            'Nồng độ oxalate trong nước tiểu (nếu dùng liều cao lâu dài)',
            'Chức năng thận (nếu có nguy cơ sỏi thận)'
        ],
        'precautions': [
            'Liều cao (>1g/ngày) có thể gây tiêu chảy - giảm liều nếu có',
            'Thận trọng với bệnh nhân có tiền sử sỏi thận oxalate (tăng nguy cơ)',
            'Tăng hấp thu sắt - thận trọng với bệnh nhân quá tải sắt (hemochromatosis)',
            'An toàn trong thai kỳ và cho con bú',
            'Hấp thu tốt từ thức ăn (trái cây, rau quả)',
            'Không cần bổ sung nếu ăn đủ trái cây và rau quả'
        ],
        'pharmacokinetics': {
            'half_life': '10-20 ngày (dự trữ trong cơ thể)',
            'onset': 'Vài ngày đến vài tuần (tác dụng tích tụ)',
            'duration': 'Phụ thuộc vào dự trữ trong cơ thể',
            'protein_binding': 'Không đáng kể',
            'clearance': 'Thận: bài tiết qua nước tiểu (liều cao), dự trữ trong mô (liều bình thường)'
        },
        'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Vitamin C dễ bị oxy hóa khi tiếp xúc với không khí, ánh sáng, nhiệt độ cao.',
        'black_box_warnings': None,
        'drug_interactions': {
            'moderate': [
                {
                    'drug': 'Sắt',
                    'mechanism': 'Vitamin C tăng hấp thu sắt (chuyển Fe3+ thành Fe2+)',
                    'effect': 'Tăng hấp thu sắt, có thể gây quá tải sắt',
                    'management': 'Thận trọng với bệnh nhân hemochromatosis. Có thể dùng cùng để tăng hấp thu sắt khi thiếu máu thiếu sắt.'
                },
                {
                    'drug': 'Warfarin',
                    'mechanism': 'Vitamin C liều cao có thể giảm hiệu quả warfarin (cơ chế chưa rõ)',
                    'effect': 'Giảm hiệu quả warfarin',
                    'management': 'Thận trọng. Theo dõi INR nếu dùng liều cao vitamin C.'
                }
            ],
            'minor': []
        },
        'contraindications': {
            'tuyệt_đối': [
                'Dị ứng vitamin C',
                'Bệnh thận oxalate nặng'
            ],
            'tương_đối': [
                'Bệnh nhân có tiền sử sỏi thận oxalate - thận trọng (tăng nguy cơ)',
                'Hemochromatosis - thận trọng (tăng hấp thu sắt)'
            ]
        },
        'pregnancy_lactation': {
            'fda_category': 'A',
            'pregnancy_details': 'An toàn trong thai kỳ. Vitamin C cần thiết cho sự phát triển bình thường của thai nhi. Liều khuyến nghị: 85mg/ngày trong thai kỳ.',
            'lactation': {
                'safety': 'Compatible',
                'details': 'Vitamin C bài tiết vào sữa mẹ. An toàn cho trẻ bú mẹ. Liều khuyến nghị: 120mg/ngày khi cho con bú.',
                'recommendation': 'Có thể dùng an toàn khi cho con bú.'
            }
        },
        'hepatic_adjustment': {
            'mild': 'Không đổi',
            'moderate': 'Không đổi',
            'severe': 'Không đổi',
            'notes': 'Vitamin C là vitamin, không chuyển hóa ở gan. Suy gan không ảnh hưởng đến vitamin C.'
        },
        'overdose_management': {
            'symptoms': [
                'Tiêu chảy (liều cao >1g/ngày)',
                'Buồn nôn, nôn',
                'Sỏi thận oxalate (liều cao lâu dài)',
                'Tăng hấp thu sắt (có thể gây quá tải sắt)'
            ],
            'antidote': 'Không có antidote đặc hiệu',
            'treatment': [
                'Ngừng thuốc nếu có triệu chứng',
                'Giảm liều nếu tiêu chảy',
                'Điều trị hỗ trợ: truyền dịch nếu cần',
                'Theo dõi chức năng thận nếu có nguy cơ sỏi thận'
            ],
            'monitoring': 'Triệu chứng lâm sàng, chức năng thận'
        },
        'reversal_agents': {
            'available': False,
            'agents': []
        },
        'administration_instructions': {
            'oral': {
                'with_food': 'Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ.',
                'timing': 'Dùng 1-3 lần/ngày tùy liều. Liều cao nên chia nhỏ để tránh tiêu chảy.'
            },
            'iv': {
                'reconstitution': 'Pha loãng trong NS hoặc D5W',
                'infusion_rate': 'Truyền chậm (200-500mg trong 30-60 phút)',
                'compatibility': ['NS', 'D5W'],
                'incompatibility': [],
                'notes': 'Dùng cho bệnh nhân lọc máu hoặc không thể uống.'
            }
        },
        'references': {
            'primary_sources': [
                'FDA Drug Label - Vitamin C (Ascorbic Acid)',
                'UpToDate - Vitamin C drug information',
                'WHO Guidelines for vitamin C supplementation'
            ],
            'last_updated': '2025-02-05',
            'evidence_level': 'High - Guidelines dựa trên chứng cứ từ WHO và FDA'
        }
    },
    "Vitamin E": {
        'group': 'Vitamins/Supplements - Vitamin E',
        'vietnamese_name': 'Vitamin E, Alpha-tocopherol',
        'administration': ['PO'],
        'indications': [
            'Thiếu vitamin E (hiếm)',
            'Dự phòng thiếu vitamin E',
            'Chống oxy hóa',
            'Bệnh nhân kém hấp thu chất béo',
            'Thiếu máu tan máu ở trẻ sinh non'
        ],
        'contraindications': [
            'Dị ứng vitamin E',
            'Đang dùng warfarin (tăng nguy cơ chảy máu)'
        ],
        'dosage': {
            'adult_standard': '15-30mg (22-33 IU) x 1 lần/ngày',
            'adult_max': '1000mg/ngày',
            'pediatric': '5-10mg/ngày',
            'notes': 'Liều cao (>400 IU/ngày) có thể tăng nguy cơ chảy máu'
        },
        'side_effects': [
            'Chảy máu (liều cao >400 IU/ngày)',
            'Buồn nôn',
            'Tiêu chảy',
            'Mệt mỏi',
            'Tăng nguy cơ đột quỵ xuất huyết (liều cao)'
        ],
        'interactions': [
            'Warfarin: tăng nguy cơ chảy máu',
            'Aspirin: tăng nguy cơ chảy máu',
            'Chất béo: tăng hấp thu vitamin E'
        ],
        'pregnancy': 'A - An toàn',
        'mechanism_of_action': 'Vitamin E (alpha-tocopherol) là vitamin tan trong chất béo, hoạt động chủ yếu như một chất chống oxy hóa mạnh. Vitamin E bảo vệ màng tế bào khỏi tổn thương do gốc tự do (lipid peroxidation), đặc biệt quan trọng cho tế bào thần kinh, tế bào cơ, và tế bào hồng cầu. Vitamin E ức chế quá trình oxy hóa LDL cholesterol, giúp ngăn ngừa xơ vữa động mạch. Vitamin E cũng có vai trò trong chức năng miễn dịch, tổng hợp DNA, và điều hòa biểu hiện gen. Vitamin E được tái tạo từ dạng oxy hóa bởi vitamin C. Thiếu vitamin E (hiếm) gây thiếu máu tan máu, bệnh thần kinh ngoại biên, và yếu cơ. Vitamin E cần chất béo để hấp thu tốt.',
        'monitoring': [
            'Đáp ứng điều trị (giảm triệu chứng thiếu vitamin E)',
            'Dấu hiệu chảy máu (nếu dùng liều cao >400 IU/ngày)',
            'INR (nếu dùng với warfarin)',
            'Chức năng gan (nếu dùng liều cao lâu dài)'
        ],
        'precautions': [
            'Liều cao (>400 IU/ngày) có thể tăng nguy cơ chảy máu - thận trọng',
            'KHÔNG dùng với warfarin (tăng nguy cơ chảy máu nghiêm trọng)',
            'Thận trọng với aspirin và các thuốc chống đông khác',
            'Cần chất béo để hấp thu tốt - nên dùng với thức ăn có chất béo',
            'An toàn trong thai kỳ và cho con bú (liều bình thường)',
            'Liều cao có thể tăng nguy cơ đột quỵ xuất huyết',
            'Không cần bổ sung nếu ăn đủ thực phẩm giàu vitamin E (dầu thực vật, hạt, rau xanh)'
        ],
        'pharmacokinetics': {
            'half_life': 'Vài ngày đến vài tuần (dự trữ trong mô mỡ)',
            'onset': 'Vài ngày đến vài tuần (tác dụng tích tụ)',
            'duration': 'Phụ thuộc vào dự trữ trong cơ thể',
            'protein_binding': 'Không đáng kể',
            'clearance': 'Gan: chuyển hóa, bài tiết qua mật. Dự trữ trong mô mỡ và gan.'
        },
        'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Vitamin E dễ bị oxy hóa khi tiếp xúc với không khí, ánh sáng.',
        'black_box_warnings': None,
        'drug_interactions': {
            'major': [
                {
                    'drug': 'Warfarin',
                    'mechanism': 'Vitamin E ức chế vitamin K-dependent clotting factors, tăng tác dụng warfarin',
                    'effect': 'Tăng nguy cơ chảy máu nghiêm trọng',
                    'management': 'CHỐNG CHỈ ĐỊNH dùng với warfarin. Nếu cần dùng, theo dõi INR chặt chẽ và giảm liều warfarin.'
                }
            ],
            'moderate': [
                {
                    'drug': 'Aspirin, NSAIDs, Clopidogrel',
                    'mechanism': 'Cả hai đều ảnh hưởng đến đông máu',
                    'effect': 'Tăng nguy cơ chảy máu',
                    'management': 'Thận trọng. Theo dõi dấu hiệu chảy máu.'
                }
            ],
            'minor': []
        },
        'contraindications': {
            'tuyệt_đối': [
                'Dị ứng vitamin E',
                'Đang dùng warfarin - CHỐNG CHỈ ĐỊNH'
            ],
            'tương_đối': [
                'Đang dùng aspirin, NSAIDs, clopidogrel - thận trọng (tăng nguy cơ chảy máu)',
                'Bệnh nhân có nguy cơ chảy máu - thận trọng',
                'Liều cao >400 IU/ngày - tăng nguy cơ đột quỵ xuất huyết'
            ]
        },
        'pregnancy_lactation': {
            'fda_category': 'A',
            'pregnancy_details': 'An toàn trong thai kỳ với liều bình thường (15-30mg/ngày). Liều cao (>400 IU/ngày) không khuyến nghị trong thai kỳ do tăng nguy cơ chảy máu.',
            'lactation': {
                'safety': 'Compatible',
                'details': 'Vitamin E bài tiết vào sữa mẹ. An toàn cho trẻ bú mẹ với liều bình thường.',
                'recommendation': 'Có thể dùng an toàn khi cho con bú với liều bình thường.'
            }
        },
        'hepatic_adjustment': {
            'mild': 'Không đổi',
            'moderate': 'Không đổi',
            'severe': 'Thận trọng, có thể giảm liều',
            'notes': 'Vitamin E chuyển hóa ở gan và bài tiết qua mật. Suy gan nặng có thể ảnh hưởng đến chuyển hóa.'
        },
        'overdose_management': {
            'symptoms': [
                'Chảy máu (liều cao >400 IU/ngày)',
                'Buồn nôn, nôn',
                'Tiêu chảy',
                'Mệt mỏi',
                'Tăng nguy cơ đột quỵ xuất huyết'
            ],
            'antidote': 'Không có antidote đặc hiệu',
            'treatment': [
                'Ngừng thuốc nếu có triệu chứng chảy máu',
                'Điều trị chảy máu nếu có (vitamin K, FFP nếu cần)',
                'Theo dõi INR nếu dùng với warfarin',
                'Điều trị hỗ trợ: truyền dịch nếu cần'
            ],
            'monitoring': 'Dấu hiệu chảy máu, INR, huyết áp, dấu hiệu đột quỵ'
        },
        'reversal_agents': {
            'available': False,
            'agents': []
        },
        'administration_instructions': {
            'oral': {
                'with_food': 'NÊN dùng với thức ăn có chất béo để tăng hấp thu. Vitamin E tan trong chất béo, hấp thu tốt hơn khi có chất béo.',
                'timing': 'Dùng 1 lần/ngày với thức ăn. Tránh dùng liều cao >400 IU/ngày.'
            },
            'iv': {
                'reconstitution': 'Không có dạng IV thường dùng',
                'infusion_rate': 'N/A',
                'compatibility': [],
                'incompatibility': [],
                'notes': 'Vitamin E chủ yếu dùng đường uống.'
            }
        },
        'references': {
            'primary_sources': [
                'FDA Drug Label - Vitamin E (Alpha-tocopherol)',
                'UpToDate - Vitamin E drug information',
                'WHO Guidelines for vitamin E supplementation'
            ],
            'last_updated': '2025-02-05',
            'evidence_level': 'High - Guidelines dựa trên chứng cứ từ WHO và FDA'
        }
    }
}

__all__ = ['VITAMINS_DRUGS']
