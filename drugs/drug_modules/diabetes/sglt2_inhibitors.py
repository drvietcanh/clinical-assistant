"""Diabetes Medications
Active module - contains all diabetes drug data"""

# SGLT2 Inhibitors

SGLT2_INHIBITORS_DRUGS = {
    "Canagliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Canagliflozin, Invokana",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm nguy cơ tim mạch",
            "Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton do đái tháo đường",
            "Suy thận nặng (eGFR <30)",
            "Đang lọc máu",
            "Nhiễm trùng đường tiết niệu tái phát"
        ],
        "dosage": {
            "adult_type2_dm": "100-300mg x 1 lần/ngày",
            "adult_heart_failure": "100mg x 1 lần/ngày",
            "adult_ckd": "100mg x 1 lần/ngày (eGFR ≥30)",
            "notes": "Uống trước bữa ăn đầu tiên. Giảm đường huyết nhẹ. Liều 300mg có thể tăng nguy cơ tác dụng phụ."
        },
        "renal_adjustment": {
            "normal": "100-300mg/ngày",
            "30_60": "100mg/ngày (eGFR ≥30)",
            "under_30": "CHỐNG CHỈ ĐỊNH - không dùng nếu eGFR <30"
        },
        "side_effects": [
            "Nhiễm trùng đường tiết niệu",
            "Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu)",
            "Mất nước, hạ huyết áp",
            "Nhiễm toan ceton (hiếm)",
            "Gãy xương tăng nhẹ",
            "Hoại thư Fournier (hiếm nhưng nguy hiểm)",
            "Cắt cụt chi dưới (tăng nguy cơ nhẹ)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết",
            "Diuretics: tăng nguy cơ mất nước",
            "Digoxin: tăng nhẹ nồng độ digoxin",
            "Rifampin: giảm nồng độ canagliflozin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Canagliflozin là chất ức chế chọn lọc sodium-glucose cotransporter 2 (SGLT2) ở ống lượn gần của thận. SGLT2 chịu trách nhiệm tái hấp thu 90% glucose từ nước tiểu. Bằng cách ức chế SGLT2, canagliflozin ngăn chặn tái hấp thu glucose, làm tăng bài tiết glucose qua nước tiểu (glucosuria), từ đó giảm đường huyết. Cơ chế này không phụ thuộc vào insulin, giúp giảm đường huyết mà không tăng nguy cơ hạ đường huyết (trừ khi dùng với insulin hoặc sulfonylurea). Ngoài ra, canagliflozin có lợi ích tim mạch và thận: giảm thể tích tuần hoàn, giảm huyết áp, giảm albumin niệu, và cải thiện kết cục tim mạch. Nghiên cứu CANVAS đã chứng minh lợi ích tim mạch. Canagliflozin có thể tăng nhẹ nguy cơ cắt cụt chi dưới.",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết",
            "Chức năng thận (eGFR, creatinine) - không dùng nếu eGFR <30",
            "Nhiễm trùng đường tiết niệu (UTI) - triệu chứng, cấy nước tiểu nếu cần",
            "Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu) - đặc biệt ở phụ nữ",
            "Dấu hiệu mất nước, hạ huyết áp (đặc biệt ở người cao tuổi, dùng diuretics)",
            "Nhiễm toan ceton (DKA) - glucose máu, ketone, pH máu nếu có triệu chứng",
            "Hoại thư Fournier (nhiễm trùng vùng sinh dục nặng) - hiếm nhưng nguy hiểm",
            "Gãy xương (đặc biệt ở người cao tuổi)",
            "Dấu hiệu nhiễm trùng, loét, đau ở chi dưới (nguy cơ cắt cụt chi)"
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 (tăng nguy cơ nhiễm toan ceton)",
            "CHỐNG CHỈ ĐỊNH nếu eGFR <30 - không hiệu quả",
            "Tăng nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục - vệ sinh tốt, uống nhiều nước",
            "Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính, nhịn ăn",
            "Nguy cơ mất nước, hạ huyết áp - đặc biệt ở người cao tuổi, dùng diuretics, suy tim",
            "Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea - có thể cần giảm liều",
            "Hoại thư Fournier - hiếm nhưng nguy hiểm, cần chú ý vệ sinh vùng sinh dục",
            "Tăng nhẹ nguy cơ cắt cụt chi dưới - theo dõi dấu hiệu nhiễm trùng, loét, đau ở chi dưới",
            "Uống nhiều nước để giảm nguy cơ nhiễm trùng",
            "Uống trước bữa ăn đầu tiên"
        ],
        "pharmacokinetics": {
            "half_life": "10-13 giờ",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa qua UGT1A9, UGT2B4), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính. Nguy cơ cắt cụt chi dưới - tăng nhẹ nguy cơ. Hoại thư Fournier - hiếm nhưng nguy hiểm. Không dùng nếu eGFR <30.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng UGT1A9 và UGT2B4, tăng chuyển hóa canagliflozin",
                    "effect": "Giảm nồng độ canagliflozin, giảm hiệu quả",
                    "management": "Có thể cần tăng liều canagliflozin. Theo dõi đường huyết."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "Tác dụng cộng dồn giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Có thể cần giảm liều insulin hoặc sulfonylurea."
                },
                {
                    "drug": "Diuretics",
                    "mechanism": "Cả hai đều gây mất nước, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp",
                    "management": "Thận trọng. Theo dõi dấu hiệu mất nước, hạ huyết áp. Có thể cần giảm liều diuretics."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Canagliflozin có thể tăng nhẹ nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <30) - CHỐNG CHỈ ĐỊNH",
                "Đang lọc máu",
                "Dị ứng canagliflozin hoặc SGLT2 inhibitor"
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 30-60) - dùng liều 100mg/ngày",
                "Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ",
                "Bệnh tim mạch - thận trọng",
                "Có thai - category C"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Canagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Canagliflozin chuyển hóa một phần qua gan nhưng chủ yếu thải qua thận.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị và độc tính.",
            "notes": "Canagliflozin chuyển hóa một phần qua gan (UGT1A9, UGT2B4) nhưng chủ yếu thải qua thận. Suy gan thường không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Mất nước, hạ huyết áp",
                "Nhiễm toan ceton (hiếm)"
            ],
            "antidote": "Glucose (nếu hạ đường huyết)",
            "treatment": [
                "Ngừng canagliflozin nếu cần",
                "Điều trị hạ đường huyết nếu có (glucose)",
                "Truyền dịch nếu mất nước, hạ huyết áp",
                "Điều trị nhiễm toan ceton nếu có",
                "Theo dõi tại bệnh viện"
            ],
            "monitoring": "Đường huyết, dấu hiệu sinh tồn, dấu hiệu mất nước, ketone máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống trước bữa ăn đầu tiên (không cần ăn)",
                "timing": "Uống 1 lần/ngày, trước bữa ăn đầu tiên. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Canagliflozin (Invokana)",
                "CANVAS Study - New England Journal of Medicine",
                "UpToDate - Canagliflozin: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple large RCTs (CANVAS) showing cardiovascular benefit"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Diabetic ketoacidosis (rare)", "Fournier gangrene (rare but serious)", "Lower limb amputation (slight increased risk)", "Acute kidney injury (rare, usually due to dehydration)", "Bone fractures (slight increased risk)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Renal function (eGFR - do not use if <30)", "Signs of UTI/genital infections", "Signs of DKA", "Blood pressure", "Volume status", "Signs of lower limb infection/ulceration"]
        },
        "guideline_tags": [
            "ADA Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "CANVAS Study",
            "FDA Drug Safety Communication - SGLT2 Inhibitors and DKA, Lower Limb Amputation"
        ]
    },

    "Dapagliflozin": {'group': 'Diabetes - SGLT2 Inhibitor', 'vietnamese_name':
        'Dapagliflozin, Forxiga', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2', 'Suy tim với phân suất tống máu giảm (HFrEF)',
        'Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường'],
        'contraindications': ['Đái tháo đường type 1', 'Nhiễm toan ceton',
        'Suy thận nặng (eGFR <25)', 'Đang lọc máu',
        'Nhiễm trùng đường tiết niệu tái phát'], 'dosage': {'adult_type2_dm':
        '5-10mg x 1 lần/ngày', 'adult_heart_failure': '10mg x 1 lần/ngày',
        'adult_ckd': '10mg x 1 lần/ngày (eGFR ≥25)', 'notes':
        'Uống bất kỳ lúc nào'}, 'renal_adjustment': {'normal': '5-10mg/ngày',
        '30_60': '10mg/ngày (eGFR ≥25)', 'under_30': 'Không dùng nếu eGFR <25'},
        'side_effects': ['Nhiễm trùng đường tiết niệu',
        'Nhiễm trùng đường sinh dục', 'Mất nước', 'Nhiễm toan ceton (hiếm)'],
        'interactions': ['Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết',
        'Diuretics: mất nước'], 'pregnancy': 'C', 'mechanism_of_action':
        'Dapagliflozin là chất ức chế chọn lọc sodium-glucose cotransporter 2 (SGLT2) ở ống lượn gần của thận. SGLT2 chịu trách nhiệm tái hấp thu 90% glucose từ nước tiểu. Bằng cách ức chế SGLT2, dapagliflozin ngăn chặn tái hấp thu glucose, làm tăng bài tiết glucose qua nước tiểu (glucosuria), từ đó giảm đường huyết. Cơ chế này không phụ thuộc vào insulin, giúp giảm đường huyết mà không tăng nguy cơ hạ đường huyết (trừ khi dùng với insulin hoặc sulfonylurea). Dapagliflozin có lợi ích tim mạch và thận: giảm thể tích tuần hoàn, giảm huyết áp, giảm albumin niệu, và cải thiện kết cục tim mạch ở bệnh nhân suy tim và bệnh thận mạn. Các nghiên cứu DECLARE-TIMI 58 và DAPA-HF đã chứng minh lợi ích tim mạch và thận.'
        , 'monitoring': [
        'Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết',
        'Chức năng thận (eGFR, creatinine) - không dùng nếu eGFR <25',
        'Nhiễm trùng đường tiết niệu (UTI) - triệu chứng, cấy nước tiểu nếu cần',
        'Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu) - đặc biệt ở phụ nữ'
        ,
        'Dấu hiệu mất nước, hạ huyết áp (đặc biệt ở người cao tuổi, dùng diuretics)'
        ,
        'Nhiễm toan ceton (DKA) - glucose máu, ketone, pH máu nếu có triệu chứng',
        'Hoại thư Fournier (nhiễm trùng vùng sinh dục nặng) - hiếm nhưng nguy hiểm'
        ], 'precautions': [
        'Không dùng cho đái tháo đường type 1 (tăng nguy cơ nhiễm toan ceton)',
        'Không dùng nếu eGFR <25 - không hiệu quả',
        'Tăng nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục - vệ sinh tốt, uống nhiều nước'
        ,
        'Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính, nhịn ăn'
        ,
        'Nguy cơ mất nước, hạ huyết áp - đặc biệt ở người cao tuổi, dùng diuretics, suy tim'
        ,
        'Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea - có thể cần giảm liều'
        ,
        'Hoại thư Fournier - hiếm nhưng nguy hiểm, cần chú ý vệ sinh vùng sinh dục'
        , 'Uống nhiều nước để giảm nguy cơ nhiễm trùng',
        'Có thể dùng bất kỳ lúc nào, không cần ăn',
        'Lợi ích tim mạch và thận độc lập với tác dụng giảm đường huyết'],
        'pharmacokinetics': {'half_life': '12.9 giờ', 'onset': '1 giờ',
        'duration': '24 giờ', 'protein_binding': '91%', 'clearance':
        'Gan: chuyển hóa qua glucuronidation (phần lớn). Thận: bài tiết một phần nguyên dạng và metabolites. Không cần điều chỉnh liều ở suy gan, nhưng không dùng nếu eGFR <25.'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Insulin, Sulfonylurea (glibenclamide, gliclazide)', 'mechanism':
        'Tác dụng hiệp đồng giảm đường huyết', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Giảm liều insulin hoặc sulfonylurea khi bắt đầu dapagliflozin. Theo dõi đường huyết chặt chẽ.'
        }, {'drug': 'Loop diuretics (furosemide, torsemide)', 'mechanism':
        'Tăng bài tiết natri và nước', 'effect':
        'Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp', 'management':
        'Thận trọng. Theo dõi huyết áp, cân nặng, chức năng thận. Có thể cần giảm liều diuretic.'
        }], 'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Dapagliflozin có thể tăng nhẹ nồng độ digoxin', 'effect':
        'Tăng nguy cơ độc tính digoxin', 'management':
        'Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần.'}, {
        'drug': 'Thiazide diuretics (hydrochlorothiazide)', 'mechanism':
        'Tăng bài tiết natri và nước', 'effect':
        'Tăng nguy cơ mất nước, hạ huyết áp', 'management':
        'Thận trọng. Theo dõi huyết áp, cân nặng.'}], 'minor': [{'drug':
        'UDP-glucuronosyltransferase (UGT) inducers', 'mechanism':
        'Có thể giảm nồng độ dapagliflozin', 'effect':
        'Giảm hiệu quả dapagliflozin', 'management':
        'Thận trọng. Theo dõi đường huyết.'}]}, 'contraindications': {
        'tuyệt_đối': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <25)',
        'Đang lọc máu', 'Dị ứng dapagliflozin'], 'tương_đối': [
        'Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng',
        'Suy tim nặng - tăng nguy cơ mất nước',
        'Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp',
        'Dùng diuretics - tăng nguy cơ mất nước',
        'Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Không có nghiên cứu đầy đủ ở người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Không nên dùng trong 3 tháng đầu trừ khi thực sự cần thiết. Có thể gây hạ đường huyết ở thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Dapagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi (không chuyển hóa đáng kể qua gan)', 'notes':
        'Dapagliflozin chủ yếu chuyển hóa qua glucuronidation ở gan, nhưng không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chưa có nghiên cứu đầy đủ ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': ['Hạ đường huyết', 'Mất nước',
        'Hạ huyết áp', 'Nhiễm toan ceton (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Điều trị hạ đường huyết: Glucose 15-20g PO hoặc dextrose IV',
        'Bù dịch nếu mất nước, hạ huyết áp', 'Theo dõi đường huyết, điện giải',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính không hiệu quả (do không hấp thu qua đường tiêu hóa tốt)',
        'Theo dõi chức năng thận',
        'Nếu có nhiễm toan ceton: điều trị theo protocol DKA'], 'monitoring':
        'Đường huyết, huyết áp, cân nặng, chức năng thận, điện giải, dấu hiệu nhiễm toan ceton'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị nhiễm toan ceton theo protocol DKA nếu có. Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.',
        'timing':
        'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }},         'references': {'primary_sources': [
        'FDA Drug Label - Forxiga (dapagliflozin)',
        'DECLARE-TIMI 58 Study - New England Journal of Medicine',
        'DAPA-HF Study - New England Journal of Medicine',
        'UpToDate - Dapagliflozin: Drug information'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple large RCTs (DECLARE-TIMI 58, DAPA-HF)'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Diabetic ketoacidosis (rare)', 'Fournier gangrene (rare but serious)', 'Acute kidney injury (rare, usually due to dehydration)'],
            'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Blood glucose', 'Renal function (eGFR - do not use if <25)', 'Signs of UTI/genital infections', 'Signs of DKA', 'Blood pressure', 'Volume status']
        },
        'guideline_tags': [
            'ADA Diabetes Guidelines',
            'AACE/ACE Diabetes Guidelines',
            'DECLARE-TIMI 58 Study',
            'DAPA-HF Study',
            'FDA Drug Safety Communication - SGLT2 Inhibitors and DKA'
        ],
        "black_box_warnings": None,
},
    
    "Empagliflozin": {'group': 'Diabetes - SGLT2 Inhibitor', 'vietnamese_name':
        'Empagliflozin, Jardiance', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2', 'Suy tim với phân suất tống máu giảm (HFrEF)',
        'Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường',
        'Giảm nguy cơ tim mạch'], 'contraindications': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <20)',
        'Đang lọc máu', 'Nhiễm trùng đường tiết niệu tái phát'], 'dosage': {
        'adult_type2_dm': '10-25mg x 1 lần/ngày', 'adult_heart_failure':
        '10mg x 1 lần/ngày', 'adult_ckd': '10mg x 1 lần/ngày (eGFR ≥20)',
        'notes': 'Uống bất kỳ lúc nào, không cần ăn. Giảm đường huyết nhẹ'},
        'renal_adjustment': {'normal': '10-25mg/ngày', '30_60':
        '10mg/ngày (eGFR ≥30)', 'under_30': 'Không dùng nếu eGFR <20'},
        'side_effects': ['Nhiễm trùng đường tiết niệu',
        'Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu)',
        'Mất nước, hạ huyết áp', 'Nhiễm toan ceton (hiếm)',
        'Gãy xương tăng nhẹ', 'Hoại thư Fournier (hiếm nhưng nguy hiểm)'],
        'interactions': ['Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết',
        'Diuretics: tăng nguy cơ mất nước', 'Digoxin: tăng nhẹ nồng độ digoxin'
        ], 'pregnancy': 'C', 'mechanism_of_action':
        'Empagliflozin là chất ức chế chọn lọc sodium-glucose cotransporter 2 (SGLT2) ở ống lượn gần của thận. SGLT2 chịu trách nhiệm tái hấp thu 90% glucose từ nước tiểu. Bằng cách ức chế SGLT2, empagliflozin ngăn chặn tái hấp thu glucose, làm tăng bài tiết glucose qua nước tiểu (glucosuria), từ đó giảm đường huyết. Cơ chế này không phụ thuộc vào insulin, giúp giảm đường huyết mà không tăng nguy cơ hạ đường huyết (trừ khi dùng với insulin hoặc sulfonylurea). Ngoài ra, empagliflozin có lợi ích tim mạch và thận: giảm thể tích tuần hoàn, giảm huyết áp, giảm albumin niệu, và cải thiện kết cục tim mạch ở bệnh nhân suy tim và bệnh thận mạn. Các nghiên cứu EMPA-REG OUTCOME, EMPEROR-Reduced, và EMPEROR-Preserved đã chứng minh lợi ích tim mạch và thận.'
        , 'monitoring': [
        'Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết',
        'Chức năng thận (eGFR, creatinine) - không dùng nếu eGFR <20',
        'Nhiễm trùng đường tiết niệu (UTI) - triệu chứng, cấy nước tiểu nếu cần',
        'Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu) - đặc biệt ở phụ nữ'
        ,
        'Dấu hiệu mất nước, hạ huyết áp (đặc biệt ở người cao tuổi, dùng diuretics)'
        ,
        'Nhiễm toan ceton (DKA) - glucose máu, ketone, pH máu nếu có triệu chứng',
        'Hoại thư Fournier (nhiễm trùng vùng sinh dục nặng) - hiếm nhưng nguy hiểm'
        , 'Gãy xương (đặc biệt ở người cao tuổi)'], 'precautions': [
        'Không dùng cho đái tháo đường type 1 (tăng nguy cơ nhiễm toan ceton)',
        'Không dùng nếu eGFR <20 (empagliflozin) hoặc <25 (dapagliflozin) - không hiệu quả'
        ,
        'Tăng nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục - vệ sinh tốt, uống nhiều nước'
        ,
        'Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính, nhịn ăn'
        ,
        'Nguy cơ mất nước, hạ huyết áp - đặc biệt ở người cao tuổi, dùng diuretics, suy tim'
        ,
        'Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea - có thể cần giảm liều'
        ,
        'Hoại thư Fournier - hiếm nhưng nguy hiểm, cần chú ý vệ sinh vùng sinh dục'
        , 'Uống nhiều nước để giảm nguy cơ nhiễm trùng',
        'Có thể dùng bất kỳ lúc nào, không cần ăn',
        'Lợi ích tim mạch và thận độc lập với tác dụng giảm đường huyết'],
        'pharmacokinetics': {'half_life': '12.4 giờ', 'onset': '1 giờ',
        'duration': '24 giờ', 'protein_binding': '86.2%', 'clearance':
        'Gan: chuyển hóa qua glucuronidation (phần lớn). Thận: bài tiết một phần nguyên dạng và metabolites. Không cần điều chỉnh liều ở suy gan, nhưng không dùng nếu eGFR <20.'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Insulin, Sulfonylurea (glibenclamide, gliclazide)', 'mechanism':
        'Tác dụng hiệp đồng giảm đường huyết', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Giảm liều insulin hoặc sulfonylurea khi bắt đầu empagliflozin. Theo dõi đường huyết chặt chẽ.'
        }, {'drug': 'Loop diuretics (furosemide, torsemide)', 'mechanism':
        'Tăng bài tiết natri và nước', 'effect':
        'Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp', 'management':
        'Thận trọng. Theo dõi huyết áp, cân nặng, chức năng thận. Có thể cần giảm liều diuretic.'
        }], 'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Empagliflozin có thể tăng nhẹ nồng độ digoxin', 'effect':
        'Tăng nguy cơ độc tính digoxin', 'management':
        'Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần.'}, {
        'drug': 'Thiazide diuretics (hydrochlorothiazide)', 'mechanism':
        'Tăng bài tiết natri và nước', 'effect':
        'Tăng nguy cơ mất nước, hạ huyết áp', 'management':
        'Thận trọng. Theo dõi huyết áp, cân nặng.'}], 'minor': [{'drug':
        'UDP-glucuronosyltransferase (UGT) inducers', 'mechanism':
        'Có thể giảm nồng độ empagliflozin', 'effect':
        'Giảm hiệu quả empagliflozin', 'management':
        'Thận trọng. Theo dõi đường huyết.'}]}, 'contraindications': {
        'tuyệt_đối': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <20)',
        'Đang lọc máu', 'Dị ứng empagliflozin'], 'tương_đối': [
        'Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng',
        'Suy tim nặng - tăng nguy cơ mất nước',
        'Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp',
        'Dùng diuretics - tăng nguy cơ mất nước',
        'Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Không có nghiên cứu đầy đủ ở người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Không nên dùng trong 3 tháng đầu trừ khi thực sự cần thiết. Có thể gây hạ đường huyết ở thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Empagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi (không chuyển hóa đáng kể qua gan)', 'notes':
        'Empagliflozin chủ yếu chuyển hóa qua glucuronidation ở gan, nhưng không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chưa có nghiên cứu đầy đủ ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': ['Hạ đường huyết', 'Mất nước',
        'Hạ huyết áp', 'Nhiễm toan ceton (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Điều trị hạ đường huyết: Glucose 15-20g PO hoặc dextrose IV',
        'Bù dịch nếu mất nước, hạ huyết áp', 'Theo dõi đường huyết, điện giải',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính không hiệu quả (do không hấp thu qua đường tiêu hóa tốt)',
        'Theo dõi chức năng thận',
        'Nếu có nhiễm toan ceton: điều trị theo protocol DKA'], 'monitoring':
        'Đường huyết, huyết áp, cân nặng, chức năng thận, điện giải, dấu hiệu nhiễm toan ceton'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị nhiễm toan ceton theo protocol DKA nếu có. Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.',
        'timing':
        'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }},         'references': {'primary_sources': [
        'FDA Drug Label - Jardiance (empagliflozin)',
        'EMPA-REG OUTCOME Study - New England Journal of Medicine',
        'EMPEROR-Reduced Study - New England Journal of Medicine',
        'EMPEROR-Preserved Study - New England Journal of Medicine',
        'UpToDate - Empagliflozin: Drug information'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple large RCTs (EMPA-REG OUTCOME, EMPEROR-Reduced, EMPEROR-Preserved)'
        },
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Diabetic ketoacidosis (rare)', 'Fournier gangrene (rare but serious)', 'Acute kidney injury (rare, usually due to dehydration)'],
            'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Blood glucose', 'Renal function (eGFR - do not use if <20)', 'Signs of UTI/genital infections', 'Signs of DKA', 'Blood pressure', 'Volume status']
        },
        'guideline_tags': [
            'ADA Diabetes Guidelines',
            'AACE/ACE Diabetes Guidelines',
            'EMPA-REG OUTCOME Study',
            'EMPEROR-Reduced Study',
            'EMPEROR-Preserved Study',
            'FDA Drug Safety Communication - SGLT2 Inhibitors and DKA'
        ],
        "black_box_warnings": None,
},
    "Ertugliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Ertugliflozin, Steglatro",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2.",
            "Suy tim với phân suất tống máu giảm (HFrEF) - dữ liệu hạn chế hơn empagliflozin/dapagliflozin.",
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton do đái tháo đường",
            "Suy thận nặng (eGFR <30)",
            "Đang lọc máu",
        ],
        "dosage": {
            "adult_type2_dm": "5-15mg x 1 lần/ngày",
            "notes": "Uống bất kỳ lúc nào, không cần ăn. Có thể dùng đơn trị hoặc phối hợp.",
        },
        "renal_adjustment": {
            "normal": "5-15mg/ngày",
            "30_60": "5mg/ngày (eGFR ≥30)",
            "under_30": "Không dùng nếu eGFR <30",
        },
        "side_effects": [
            "Nhiễm trùng đường tiết niệu",
            "Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu)",
            "Mất nước, hạ huyết áp",
            "Nhiễm toan ceton (hiếm)",
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết",
            "Diuretics: tăng nguy cơ mất nước",
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Ertugliflozin là chất ức chế chọn lọc SGLT2 ở ống lượn gần của thận, "
            "ngăn chặn tái hấp thu glucose, làm tăng bài tiết glucose qua nước tiểu, "
            "từ đó giảm đường huyết. Cơ chế không phụ thuộc insulin. "
            "Có lợi ích tim mạch và thận tương tự các SGLT2 inhibitors khác."
        ),
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu)",
            "Chức năng thận (eGFR, creatinine)",
            "Nhiễm trùng đường tiết niệu và đường sinh dục",
            "Dấu hiệu mất nước, hạ huyết áp",
            "Nhiễm toan ceton nếu có triệu chứng",
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1",
            "Không dùng nếu eGFR <30",
            "Tăng nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục",
            "Nguy cơ nhiễm toan ceton",
            "Nguy cơ mất nước, hạ huyết áp",
            "Giảm liều insulin/sulfonylurea khi bắt đầu",
        ],
        "pharmacokinetics": {
            "half_life": "16-17 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "~95%",
            "clearance": "Gan (chuyển hóa qua UGT), thận (thải trừ một phần)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": (
            "Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính. "
            "Không dùng nếu eGFR <30."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "Tác dụng cộng dồn giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Có thể cần giảm liều insulin hoặc sulfonylurea.",
                },
                {
                    "drug": "Diuretics",
                    "mechanism": "Cả hai đều gây mất nước, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp",
                    "management": "Thận trọng. Theo dõi dấu hiệu mất nước, hạ huyết áp.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <30)",
                "Đang lọc máu",
                "Dị ứng ertugliflozin",
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 30-60) - dùng liều 5mg/ngày",
                "Nhiễm trùng đường tiết niệu tái phát",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ",
                "recommendation": "Thận trọng khi cho con bú",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "Ertugliflozin chuyển hóa qua gan (UGT) nhưng không cần chỉnh liều ở suy gan nhẹ đến trung bình",
        },
        "overdose_management": {
            "symptoms": ["Hạ đường huyết", "Mất nước", "Hạ huyết áp"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hạ đường huyết: Glucose IV nếu cần",
                "Bù dịch nếu mất nước, hạ huyết áp",
                "Theo dõi đường huyết, điện giải",
            ],
            "monitoring": "Đường huyết, dấu hiệu sinh tồn, dấu hiệu mất nước",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống bất kỳ lúc nào, không cần ăn",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Steglatro (ertugliflozin)",
                "ADA/EASD Diabetes Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Diabetic ketoacidosis (rare)", "Fournier gangrene (rare but serious)", "Acute kidney injury (rare, usually due to dehydration)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Renal function (eGFR - do not use if <30)", "Signs of UTI/genital infections", "Signs of DKA", "Blood pressure", "Volume status"]
        },
        "guideline_tags": [
            "ADA/EASD Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "FDA Drug Safety Communication - SGLT2 Inhibitors and DKA"
        ],
              "reversal_agents": {
              "available": False,
              "agents": []
          },
},
}

__all__ = ['SGLT2_INHIBITORS_DRUGS']
