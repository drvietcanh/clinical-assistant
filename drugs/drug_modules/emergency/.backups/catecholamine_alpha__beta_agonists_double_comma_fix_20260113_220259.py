"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Catecholamine (Alpha & Beta Agonist)s

CATECHOLAMINE_ALPHA_BETA_AGONISTS_DRUGS = {
    "Dobutamine":     {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Dobutamine, Dobutrex",
        "administration": [
            "IV"
    ],
        "indications": [
            "Suy tim cấp",
            "Sốc tim (cardiogenic shock)",
            "Stress test tim (dobutamine stress echo)",
            "Sau phẫu thuật tim"
    ],
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hẹp động mạch chủ nặng - có thể gây suy tim nặng",
                "Sốc giảm thể tích (chưa bù dịch) - bù dịch trước"
    ],
            "tương_đối": [
                "Rối loạn nhịp tim nặng - có thể làm nặng",
                "Bệnh mạch vành nặng - tăng nguy cơ thiếu máu cục bộ"
    ],
        },
        "reversal_agents": None,
        "dosage": {
            "adult_heart_failure": "2.5-15 mcg/kg/phút IV infusion",
            "adult_cardiogenic_shock": "2.5-20 mcg/kg/phút IV infusion",
            "adult_stress_test": "5-40 mcg/kg/phút IV (tăng dần)",
            "notes": "Pha 250mg trong 250ml D5W = 1000 mcg/ml. Khởi đầu 2.5-5 mcg/kg/phút.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
        },
        "side_effects": [
            "Tăng nhịp tim",
            "Rối loạn nhịp tim",
            "Hạ huyết áp (do giãn mạch)",
            "Đau ngực",
            "Khó thở"
    ],
        "interactions": [
            "Beta-blockers: đối kháng tác dụng",
            "MAOIs: tăng tác dụng"
    ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {
                "cardiac": True,
            },
            "icu_critical_care_only": True,
            "look_alike_sound_alike": [],
        },
        "guideline_tags": [
            "AHA ACLS Guidelines",
            "SCCM Shock Management Guidelines",
            "ACC/AHA Heart Failure Guidelines"
    ],
        "mechanism_of_action": """Chủ yếu beta-1-adrenergic receptor agonist, một số tác dụng beta-2 và alpha-1. Kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim mạnh, tăng cung lượng tim. Kích thích beta-2 receptors → giãn mạch nhẹ. Kích thích alpha-1 receptors → co mạch nhẹ. Kết quả: tăng cung lượng tim, giảm áp lực đổ đầy tim, ít ảnh hưởng đến huyết áp.""",
        "monitoring": [
            "Huyết áp liên tục",
            "Nhịp tim và ECG (rối loạn nhịp)",
            "Cung lượng tim (nếu có thể)",
            "Áp lực đổ đầy tim (CVP, PCWP)",
            "Dấu hiệu thiếu máu cục bộ (đau ngực)"
    ],
        "precautions": [
            "Bù dịch đầy đủ trước khi dùng (tránh hạ huyết áp)",
            "Theo dõi rối loạn nhịp tim",
            "Thận trọng ở bệnh nhân bệnh mạch vành",
            "Giảm liều khi cung lượng tim đã cải thiện",
            "Không dùng trong sốc giảm thể tích"
    ],
        "pharmacokinetics": {
            "half_life": "2 phút (rất ngắn)",
            "onset": "Ngay lập tức",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Rất nhanh, bị bất hoạt bởi COMT",
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, có thể gây rối loạn nhịp tim nặng.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dobutamine",
                "ACLS Guidelines",
                "UpToDate - Dobutamine: Drug Information"
    ],
            "last_updated": "2025-02-05",
            "evidence_level": "A",
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa cập nhật chi tiết; dùng trong bối cảnh cấp cứu tim mạch khi cần thiết.",
            "lactation": {
                "safety": "Caution",
                "details": "Dùng ngắn hạn trong ICU; dữ liệu an toàn khi cho con bú hạn chế.",
                "recommendation": "Không dùng kéo dài; đánh giá lợi ích/nguy cơ từng trường hợp.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Thận trọng; chỉnh liều theo đáp ứng lâm sàng.",
            "notes": "Chủ yếu dùng ngắn hạn trong ICU với monitor huyết động liên tục.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi huyết áp, nhịp tim, dấu hiệu thiếu máu cơ tim hoặc loạn nhịp.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha trong dung dịch truyền thích hợp (NaCl 0,9%, D5W).",
                "infusion_rate": "Truyền liên tục với bơm tiêm điện; chỉnh liều theo cung lượng tim và huyết áp.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Theo dõi liên tục ECG, huyết áp và dấu hiệu suy tim.",
            },
        },
    },
    "Dopamine":     {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Dopamine, Intropin",
        "administration": [
            "IV"
    ],
        "indications": [
            "Sốc (sau khi bù dịch)",
            "Hạ huyết áp nặng",
            "Suy thận cấp (liều thấp - renal dose)",
            "Suy tim cấp"
    ],
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Pheochromocytoma - có thể gây tăng huyết áp nặng"
    ],
            "tương_đối": [
                "Rối loạn nhịp tim nặng - có thể làm nặng",
                "Bệnh mạch vành nặng - tăng nguy cơ thiếu máu cục bộ",
                "Suy thận - không dùng liều thấp cho suy thận (không có bằng chứng)"
    ],
        },
        "reversal_agents": None,
        "dosage": {
            "adult_renal_dose": "1-3 mcg/kg/phút IV (tăng tưới máu thận - không khuyến cáo)",
            "adult_cardiac_dose": "3-10 mcg/kg/phút IV (tăng cung lượng tim)",
            "adult_vasopressor_dose": "10-20 mcg/kg/phút IV (tăng huyết áp)",
            "notes": "Pha 400mg trong 250ml D5W = 1600 mcg/ml. Tác dụng phụ thuộc liều.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
        },
        "side_effects": [
            "Rối loạn nhịp tim",
            "Tăng huyết áp (liều cao)",
            "Co mạch ngoại vi (liều cao)",
            "Hoại tử mô (nếu rò rỉ)",
            "Buồn nôn, nôn"
    ],
        "interactions": [
            "MAOIs: tăng tác dụng",
            "TCAs: tăng tác dụng",
            "Beta-blockers: tăng huyết áp"
    ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {
                "cardiac": True,
            },
            "icu_critical_care_only": True,
            "look_alike_sound_alike": [],
        },
        "guideline_tags": [
            "Surviving Sepsis Campaign Guidelines 2021",
            "SCCM Shock Management Guidelines"
    ],
        "mechanism_of_action": """Tác dụng phụ thuộc liều: Liều thấp (1-3 mcg/kg/phút): kích thích dopamine receptors → tăng tưới máu thận (không khuyến cáo, không có bằng chứng). Liều trung bình (3-10 mcg/kg/phút): kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim, tăng cung lượng tim. Liều cao (10-20 mcg/kg/phút): kích thích alpha-1 receptors → co mạch, tăng huyết áp.""",
        "monitoring": [
            "Huyết áp liên tục",
            "Nhịp tim và ECG (rối loạn nhịp)",
            "Cung lượng tim (nếu có thể)",
            "Tưới máu mô",
            "Dấu hiệu hoại tử tại chỗ tiêm"
    ],
        "precautions": [
            "Truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử)",
            "Không dùng liều thấp cho suy thận (không có bằng chứng hiệu quả)",
            "Theo dõi rối loạn nhịp tim",
            "Bù dịch đầy đủ trước khi dùng",
            "Giảm liều khi huyết áp đã ổn định"
    ],
        "pharmacokinetics": {
            "half_life": "1-2 phút (rất ngắn)",
            "onset": "Ngay lập tức",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Rất nhanh, bị bất hoạt bởi MAO và COMT",
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh.",
        "black_box_warnings": "Hoại tử mô nếu rò rỉ ngoài mạch. Không dùng liều thấp cho suy thận (không có bằng chứng).",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dopamine",
                "Surviving Sepsis Campaign Guidelines",
                "UpToDate - Dopamine: Drug Information"
    ],
            "last_updated": "2025-02-05",
            "evidence_level": "A",
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa cập nhật chi tiết; dùng trong bối cảnh cấp cứu khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Thường dùng ngắn hạn trong ICU; dữ liệu cho con bú hạn chế.",
                "recommendation": "Không phải chỉ định điều trị kéo dài; tham khảo chuyên gia khi cần.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Thận trọng; ưu tiên chỉnh theo đáp ứng huyết động và chức năng cơ quan.",
            "notes": "Chủ yếu được chuyển hoá tại gan và thần kinh; dùng chủ yếu trong ICU với monitor liên tục.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi huyết áp, nhịp tim, tưới máu ngoại vi, dấu hiệu thiếu máu cơ quan đích.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha trong NaCl 0,9% hoặc D5W; truyền qua bơm tiêm điện hoặc bơm truyền.",
                "infusion_rate": "Titration theo đáp ứng huyết áp và cung lượng tim.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Ưu tiên truyền qua đường tĩnh mạch trung tâm nếu dùng kéo dài; tránh thoát mạch.",
            },
        },
    },
    "Epinephrine": {'group': 'Emergency - Catecholamine (Alpha & Beta Agonist)',vietnamese_name': 'Epinephrine, Adrenaline', 'administration': ['IV',
        'IM', 'SC', 'INH', 'IT'],indications': [
        'Sốc phản vệ (anaphylaxis)', 'Sốc (shock)',
        'Cơn hen nặng (IV/nebulizer)', 'Co thắt thanh quản'],contraindications': ['Không có trong cấp cứu ngừng tim',
        'Sốc phản vệ: không có chống chỉ định tuyệt đối'],dosage': {
        'adult_cardiac_arrest_iv': '1mg IV mỗi 3-5 phút (hoặc 0.1mg/kg)',
        'adult_cardiac_arrest_it': '2-2.5mg IT', 'adult_anaphylaxis_im':
        '0.3-0.5mg IM (0.3-0.5ml 1:1000) ở đùi ngoài', 'adult_anaphylaxis_iv':
        '0.1-0.25mg IV bolus (pha 1mg trong 10ml = 0.1mg/ml)', 'adult_shock':
        '0.1-2mcg/kg/phút IV infusion', 'pediatric_cardiac_arrest':
        '0.01mg/kg (0.1ml/kg 1:10000) IV/IT mỗi 3-5 phút',
        'pediatric_anaphylaxis_im':
        '0.01mg/kg IM (0.01ml/kg 1:1000) ở đùi ngoài (tối đa 0.5mg)', 'notes':
        '1:1000 = 1mg/ml (dùng IM/SC), 1:10000 = 0.1mg/ml (dùng IV). Đùi ngoài cho anaphylaxis'
        },renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},side_effects': ['Tim đập nhanh',
        'Tăng huyết áp', 'Lo lắng, run tay', 'Đau đầu',
        'Nhồi máu cơ tim (với liều cao)', 'Rối loạn nhịp tim',
        'Hoại tử (nếu tiêm ngoài mạch)'],interactions': [
        'Beta-blockers: đối kháng tác dụng', 'MAOIs: tăng tác dụng',
        'Tricyclic antidepressants: tăng tác dụng',
        'Digoxin: tăng nguy cơ loạn nhịp'],pregnancy':
        'C - An toàn trong cấp cứu', 'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'organ_toxicity': {'cardiac': True},icu_critical_care_only': False,
            'look_alike_sound_alike': []
        },guideline_tags': [
            'AHA ACLS Guidelines',
            'Anaphylaxis Guidelines (WAO, AAAAI)',
            'SCCM Shock Management Guidelines'
        ],mechanism_of_action':
        'Non-selective alpha và beta-adrenergic receptor agonist. Kích thích alpha-1 receptors → co mạch ngoại vi, tăng huyết áp. Kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim, tăng cung lượng tim. Kích thích beta-2 receptors → giãn phế quản, giãn mạch cơ xương. Trong ngừng tim: tăng áp lực tưới máu vành, tăng khả năng khử rung thành công.'
        , 'monitoring': ['Nhịp tim và huyết áp liên tục',
        'Điện tâm đồ (ECG) - theo dõi rối loạn nhịp',
        'Lactate máu (trong shock)', 'Đường huyết (tăng đường huyết)',
        'Dấu hiệu thiếu máu cục bộ (đau ngực, thay đổi ST)',
        'Tổn thương mô tại chỗ tiêm (hoại tử nếu tiêm ngoài mạch)'],precautions': ['TUYỆT ĐỐI KHÔNG tiêm ngoài mạch (có thể gây hoại tử)',
        'Pha loãng đúng nồng độ: 1:1000 (1mg/ml) cho IM/SC, 1:10000 (0.1mg/ml) cho IV'
        , 'Trong anaphylaxis: tiêm IM ở đùi ngoài (hấp thu nhanh hơn cánh tay)',
        'Theo dõi sát trong 20 phút đầu (nguy cơ rối loạn nhịp, tăng huyết áp)',
        'Thận trọng ở bệnh nhân bệnh mạch vành (có thể gây nhồi máu cơ tim)',
        'Tránh dùng với thuốc chẹn beta (có thể gây tăng huyết áp nặng do không đối kháng alpha)'
        , 'Tiêm IV chậm, pha loãng để tránh tăng huyết áp đột ngột'],pharmacokinetics': {'half_life': '2-3 phút (rất ngắn)', 'onset':
        'IV: ngay lập tức; IM: 5-10 phút', 'duration':
        '3-10 phút (IV), 10-30 phút (IM)', 'protein_binding':
        'Không đáng kể (catecholamine)', 'clearance':
        'Rất nhanh, bị bất hoạt bởi enzyme (MAO và COMT trong gan và mô)'},storage':
        'Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, tiêm ngoài mạch có thể gây hoại tử mô. Liều cao có thể gây nhồi máu cơ tim, đột quỵ, hoặc tử vong.'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (non-selective)', 'mechanism':
        'Beta-blockers đối kháng tác dụng beta của epinephrine, nhưng không đối kháng tác dụng alpha. Kết quả: tăng huyết áp nặng do chỉ còn tác dụng co mạch alpha, không có tác dụng giãn mạch beta-2.'
        , 'effect':
        'Tăng huyết áp nặng, nguy cơ đột quỵ, nhồi máu cơ tim, phù phổi cấp',
        'management':
        'TRÁNH dùng epinephrine với beta-blockers non-selective. Nếu cần trong cấp cứu: dùng liều thấp, theo dõi huyết áp chặt chẽ. Có thể cần thuốc giãn mạch (phentolamine) nếu tăng huyết áp nặng.'
        }, {'drug': 'MAOIs (Monoamine Oxidase Inhibitors)', 'mechanism':
        'MAOIs ức chế enzyme MAO chuyển hóa epinephrine, làm tăng nồng độ và thời gian tác dụng của epinephrine.'
        , 'effect':
        'Tăng tác dụng và thời gian tác dụng của epinephrine, tăng nguy cơ tăng huyết áp nặng, nhồi máu cơ tim, đột quỵ'
        , 'management':
        'GIẢM LIỀU epinephrine xuống 10-25% liều thông thường. Theo dõi huyết áp chặt chẽ. Trong cấp cứu: dùng liều thấp nhất có hiệu quả.'
        }, {'drug': 'Tricyclic Antidepressants (TCAs)', 'mechanism':
        'TCAs ức chế tái hấp thu norepinephrine, tăng nồng độ catecholamine, tăng tác dụng của epinephrine.'
        , 'effect':
        'Tăng tác dụng của epinephrine, tăng nguy cơ tăng huyết áp nặng, rối loạn nhịp tim'
        , 'management':
        'Thận trọng, giảm liều epinephrine. Theo dõi huyết áp và ECG chặt chẽ.'
        }],moderate': [{'drug': 'Digoxin', 'mechanism':
        'Digoxin làm tăng nhạy cảm của cơ tim với catecholamine, tăng nguy cơ rối loạn nhịp tim.'
        , 'effect':
        'Tăng nguy cơ rối loạn nhịp tim (nhịp nhanh thất, rung thất), đặc biệt ở bệnh nhân digoxin độc tính'
        , 'management':
        'Thận trọng, theo dõi ECG chặt chẽ. Kiểm tra nồng độ digoxin nếu có thể. Tránh dùng epinephrine nếu có dấu hiệu digoxin độc tính.'
        }, {'drug': 'Alpha-blockers', 'mechanism':
        'Alpha-blockers đối kháng tác dụng alpha của epinephrine, có thể làm giảm hiệu quả điều trị sốc.'
        , 'effect': 'Giảm hiệu quả điều trị sốc, có thể cần liều cao hơn',
        'management':
        'Có thể cần tăng liều epinephrine. Theo dõi đáp ứng điều trị.'}],minor': [{'drug': 'Beta-2 agonists (Salbutamol, Salmeterol)',
        'mechanism':
        'Cùng tác dụng beta-2, có thể tăng tác dụng giãn phế quản và tăng nhịp tim.'
        , 'effect': 'Tăng nhịp tim, run tay (nhẹ)', 'management':
        'Theo dõi nhịp tim. Không cần điều chỉnh liều thường quy.'}]},contraindications': {'tuyệt_đối': [
        'Không có chống chỉ định tuyệt đối trong cấp cứu ngừng tim',
        'Dị ứng epinephrine (hiếm nhưng nguy hiểm)'],tương_đối': [
        'Bệnh mạch vành - tăng nguy cơ nhồi máu cơ tim, đau thắt ngực',
        'Tăng huyết áp nặng không kiểm soát - có thể làm tăng huyết áp hơn nữa',
        'Rối loạn nhịp tim nặng - có thể làm nặng rối loạn nhịp',
        'Đột quỵ gần đây - tăng nguy cơ tái phát',
        'Pheochromocytoma - tăng nguy cơ tăng huyết áp nặng, cơn tăng huyết áp',
        'Dùng với beta-blockers non-selective - tăng huyết áp nặng',
        'Dùng với MAOIs - tăng tác dụng, cần giảm liều',
        'Dùng với TCAs - tăng tác dụng, cần thận trọng',
        'Bệnh nhân cao tuổi - tăng nhạy cảm với tác dụng phụ',
        'Bệnh nhân có bệnh mạch máu ngoại biên - tăng nguy cơ thiếu máu cục bộ'
        ],pregnancy_details':
        'Epinephrine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Epinephrine có thể qua nhau thai và có thể gây co mạch, giảm tưới máu nhau thai. Tuy nhiên, trong cấp cứu (sốc phản vệ, ngừng tim), lợi ích cứu sống mẹ vượt quá nguy cơ cho thai nhi. Sốc phản vệ và ngừng tim có thể gây tử vong cho cả mẹ và thai nhi nếu không điều trị. Epinephrine được sử dụng trong cấp cứu ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Epinephrine có thời gian bán thải rất ngắn (2-3 phút) và bị chuyển hóa nhanh. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Epinephrine có thời gian bán thải rất ngắn và không bài tiết vào sữa mẹ.'
        }},hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Epinephrine chuyển hóa nhanh bởi MAO và COMT, nhưng không phụ thuộc vào chức năng gan.'
        , 'moderate': 'Không cần điều chỉnh liều.', 'severe':
        'Không cần điều chỉnh liều. Epinephrine chuyển hóa nhanh, không tích lũy ở suy gan.'
        , 'notes':
        'Epinephrine bị chuyển hóa nhanh bởi enzyme MAO và COMT trong gan và mô, nhưng không phụ thuộc vào chức năng gan. Không cần điều chỉnh liều ở bệnh nhân suy gan.'
        },overdose_management': {'symptoms': [
        'Tăng huyết áp nặng (có thể >200/120 mmHg)',
        'Nhịp tim nhanh nặng (>150-200 bpm)', 'Nhồi máu cơ tim', 'Đột quỵ',
        'Phù phổi cấp', 'Rối loạn nhịp tim (rung nhĩ, rung thất)', 'Co giật',
        'Hoại tử mô (nếu tiêm ngoài mạch)'],antidote':
        'Không có antidote đặc hiệu. Có thể dùng thuốc giãn mạch (phentolamine, nitroglycerin) để đối kháng tác dụng alpha. Beta-blockers có thể đối kháng tác dụng beta nhưng nguy hiểm (tăng huyết áp nặng).'
        , 'treatment': ['Ngừng ngay epinephrine nếu đang truyền',
        'Theo dõi ECG và huyết áp liên tục', 'Nếu tăng huyết áp nặng:',
        '  - Phentolamine 5-10mg IV (đối kháng alpha, giảm huyết áp)',
        '  - Hoặc Nitroglycerin IV (giãn mạch, giảm huyết áp)',
        '  - Hoặc Labetalol (alpha + beta blocker) - thận trọng',
        'Nếu nhịp tim nhanh nặng:',
        '  - Beta-blocker (metoprolol, esmolol) - THẬN TRỌNG, chỉ dùng nếu không có tăng huyết áp nặng'
        , '  - Nếu có tăng huyết áp + nhịp nhanh: Labetalol',
        'Nếu nhồi máu cơ tim: Điều trị theo protocol nhồi máu cơ tim (aspirin, clopidogrel, statin, có thể cần can thiệp)'
        , 'Nếu đột quỵ: Điều trị theo protocol đột quỵ',
        'Nếu phù phổi cấp: Furosemide, nitroglycerin, hỗ trợ hô hấp',
        'Nếu rối loạn nhịp: Điều trị theo protocol rối loạn nhịp',
        'Nếu hoại tử mô (tiêm ngoài mạch):',
        '  - Phentolamine 5-10mg pha trong 10-15ml NS tiêm quanh vùng hoại tử (trong vòng 12 giờ)'
        , '  - Chườm ấm', '  - Có thể cần phẫu thuật nếu hoại tử nặng',
        'Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG trong ít nhất 2-4 giờ'
        ],monitoring':
        'Theo dõi ECG, huyết áp, nhịp tim liên tục trong ít nhất 2-4 giờ sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (nhồi máu cơ tim, đột quỵ, rối loạn nhịp).'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Phentolamine', 'mechanism':
        'Alpha-blocker, đối kháng tác dụng alpha của epinephrine (co mạch, tăng huyết áp)'
        , 'indication':
        'Tăng huyết áp nặng do quá liều epinephrine, hoại tử mô do tiêm ngoài mạch'
        , 'dose':
        '5-10mg IV cho tăng huyết áp, 5-10mg pha trong 10-15ml NS tiêm quanh vùng hoại tử (trong vòng 12 giờ)'
        }, {'agent': 'Nitroglycerin', 'mechanism': 'Giãn mạch, giảm huyết áp',
        'indication': 'Tăng huyết áp nặng do quá liều epinephrine', 'dose':
        '5-10mcg/phút IV, tăng dần đến khi đạt huyết áp mục tiêu'}, {'agent':
        'Beta-blockers (thận trọng)', 'mechanism':
        'Đối kháng tác dụng beta của epinephrine (nhịp tim nhanh)',
        'indication':
        'Nhịp tim nhanh nặng do quá liều epinephrine (CHỈ dùng nếu không có tăng huyết áp nặng)'
        , 'dose':
        'Metoprolol 5mg IV hoặc Esmolol 0.5mg/kg IV bolus, sau đó 50-200mcg/kg/phút IV infusion'
        }]},administration_instructions': {'oral': None, 'iv': {
        'reconstitution':
        'Pha loãng: 1mg epinephrine (1ml 1:1000) trong 9ml NS = 0.1mg/ml (1:10000). Hoặc dùng trực tiếp dung dịch 1:10000 nếu có.'
        , 'infusion_rate':
        'Cardiac arrest: 1mg IV bolus mỗi 3-5 phút. Anaphylaxis: 0.1-0.25mg IV bolus (pha loãng). Shock: 0.1-2mcg/kg/phút IV infusion (pha 1mg trong 250ml D5W = 4mcg/ml).'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],incompatibility': [
        'Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion.'
        ],notes':
        'QUAN TRỌNG: 1) Pha đúng nồng độ: 1:1000 (1mg/ml) cho IM/SC, 1:10000 (0.1mg/ml) cho IV, 2) TUYỆT ĐỐI KHÔNG tiêm ngoài mạch (hoại tử), 3) Trong anaphylaxis: tiêm IM ở đùi ngoài (hấp thu nhanh hơn), 4) Theo dõi huyết áp và ECG chặt chẽ, 5) Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).'
        },im': {'reconstitution': 'Dùng trực tiếp dung dịch 1:1000 (1mg/ml).',
        'injection_site':
        'Đùi ngoài (vastus lateralis) - hấp thu nhanh nhất. Có thể dùng cánh tay nhưng hấp thu chậm hơn.'
        , 'notes':
        'Anaphylaxis: 0.3-0.5mg IM ở đùi ngoài. Trẻ em: 0.01mg/kg IM ở đùi ngoài (tối đa 0.5mg). Tiêm sâu vào cơ, không tiêm vào mỡ dưới da.'
        },inhaled': {'reconstitution':
        'Dùng dung dịch 1:1000 (1mg/ml) pha trong 3-5ml NS cho nebulizer.',
        'dose':
        '0.5-1mg (0.5-1ml 1:1000) pha trong 3-5ml NS, khí dung mỗi 15-20 phút nếu cần.'
        , 'notes': 'Dùng trong cơn hen nặng. Theo dõi nhịp tim và huyết áp.'}},references': {'primary_sources': ['FDA Drug Label - Epinephrine',
        'ACLS Guidelines 2020 - American Heart Association',
        'Anaphylaxis Guidelines - World Allergy Organization',
        'UpToDate - Epinephrine: Drug Information',
        'Medscape - Epinephrine Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Epinephrine Monograph',
        'Micromedex - Epinephrine Drug Information'],last_updated':
        '2025-02-03', 'evidence_level':
        'A - Dựa trên FDA drug labels, ACLS guidelines, anaphylaxis guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }},
    
    "Milrinone": {
        "group": "Emergency - Phosphodiesterase-3 Inhibitor (Inotrope)",
        "vietnamese_name": "Milrinone, Primacor",
        "administration": ["IV"],
        "indications": [
            "Suy tim cấp (acute heart failure)",
            "Sốc tim (cardiogenic shock)",
            "Suy tim mạn tính mất bù (decompensated heart failure)",
            "Sau phẫu thuật tim (post-cardiac surgery)",
            "Bệnh nhân không đáp ứng với dobutamine"
        ],
        "contraindications": [
            "Dị ứng với milrinone",
            "Sốc giảm thể tích (chưa bù dịch)",
            "Hẹp động mạch chủ nặng",
            "Rối loạn nhịp tim nặng"
        ],
        "dosage": {
            "adult_loading": "50 mcg/kg IV bolus trong 10 phút (tùy chọn)",
            "adult_maintenance": "0.375-0.75 mcg/kg/phút IV infusion",
            "adult_max": "1.13 mcg/kg/phút (không vượt quá)",
            "notes": "Pha 20mg trong 100ml D5W = 200 mcg/ml. Có thể bắt đầu với loading dose hoặc chỉ dùng maintenance. Điều chỉnh liều theo đáp ứng huyết động."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% (CrCl 30-50: 0.25-0.5 mcg/kg/phút)",
            "under_30": "Giảm liều 50-75% (CrCl <30: 0.125-0.375 mcg/kg/phút)"
        },
        "side_effects": [
            "Rối loạn nhịp tim (nhịp nhanh thất, rung nhĩ)",
            "Hạ huyết áp (do giãn mạch)",
            "Đau đầu",
            "Buồn nôn",
            "Giảm tiểu cầu (hiếm)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Thuốc lợi tiểu: tăng nguy cơ mất nước, hạ huyết áp",
            "Thuốc hạ huyết áp: tăng nguy cơ hạ huyết áp",
            "Digoxin: không có tương tác đáng kể"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ACC/AHA Heart Failure Guidelines",
            "SCCM Shock Management Guidelines"
        ],
        "mechanism_of_action": "Milrinone là chất ức chế phosphodiesterase-3 (PDE-3), enzyme phân hủy cAMP trong tế bào cơ tim và mạch máu. Bằng cách ức chế PDE-3, milrinone tăng nồng độ cAMP trong tế bào, dẫn đến: (1) Tăng co bóp cơ tim (inotropic effect) - do tăng calcium trong tế bào cơ tim, (2) Giãn mạch (vasodilatory effect) - do giãn cơ trơn mạch máu. Kết quả: tăng cung lượng tim, giảm áp lực đổ đầy tim (preload và afterload), cải thiện huyết động. Khác với dobutamine (catecholamine), milrinone không tác động qua beta-receptors và không bị ức chế bởi beta-blockers.",
        "monitoring": [
            "Huyết áp liên tục (arterial line nếu có thể)",
            "Nhịp tim và ECG (rối loạn nhịp tim)",
            "Cung lượng tim (nếu có thể đo)",
            "Áp lực đổ đầy tim (CVP, PCWP)",
            "Lactate máu (tưới máu mô)",
            "Chức năng thận (creatinine, nước tiểu giờ)",
            "Tiểu cầu (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Bù dịch đầy đủ trước khi dùng (tránh hạ huyết áp do giãn mạch)",
            "Theo dõi rối loạn nhịp tim (tăng nguy cơ nhịp nhanh thất)",
            "Thận trọng ở bệnh nhân bệnh mạch vành (tăng nhu cầu oxy cơ tim)",
            "Giảm liều ở suy thận (thải trừ qua thận)",
            "Không dùng trong sốc giảm thể tích",
            "Có thể dùng kết hợp với dobutamine hoặc dopamine",
            "Không bị ức chế bởi beta-blockers (ưu điểm so với dobutamine)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (dài hơn dobutamine)",
            "onset": "5-15 phút sau khi bắt đầu truyền",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "70%",
            "clearance": "Thận (80-90% thải trừ qua thận dạng nguyên dạng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch đã pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "Có thể gây rối loạn nhịp tim nặng (nhịp nhanh thất, rung nhĩ). Theo dõi ECG chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc lợi tiểu (furosemide, thiazide)",
                    "mechanism": "Milrinone giãn mạch và tăng lợi tiểu, thuốc lợi tiểu tăng mất nước",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận",
                    "management": "Thận trọng. Theo dõi huyết áp, cân nặng, chức năng thận. Có thể cần giảm liều thuốc lợi tiểu hoặc bù dịch."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc hạ huyết áp (ACE inhibitors, ARBs, nitrates)",
                    "mechanism": "Tác dụng hiệp đồng giãn mạch",
                    "effect": "Tăng nguy cơ hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp chặt chẽ. Có thể cần giảm liều thuốc hạ huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng milrinone",
                "Sốc giảm thể tích chưa bù dịch đầy đủ"
            ],
            "tương_đối": [
                "Hẹp động mạch chủ nặng - tăng nguy cơ thiếu máu cục bộ",
                "Rối loạn nhịp tim nặng - tăng nguy cơ rối loạn nhịp",
                "Bệnh mạch vành - tăng nhu cầu oxy cơ tim",
                "Suy thận nặng (CrCl <30) - giảm liều 50-75%",
                "Suy gan nặng - thận trọng (chuyển hóa một phần ở gan)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Milrinone là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Milrinone có thể qua nhau thai. Trong cấp cứu (suy tim cấp, sốc tim), lợi ích cứu sống mẹ vượt quá nguy cơ cho thai nhi. Suy tim cấp và sốc tim có thể gây tử vong cho cả mẹ và thai nhi nếu không điều trị.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết milrinone có bài tiết vào sữa mẹ hay không. Thời gian bán thải 2-3 giờ, protein binding 70%. Có thể bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa một phần ở gan)",
            "severe": "Thận trọng, có thể tăng tác dụng (giảm chuyển hóa)",
            "notes": "Milrinone chuyển hóa một phần ở gan, nhưng chủ yếu thải trừ qua thận (80-90%). Suy gan có thể làm giảm chuyển hóa, nhưng ảnh hưởng ít hơn so với suy thận."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng (do giãn mạch quá mức)",
                "Rối loạn nhịp tim nặng (nhịp nhanh thất, rung nhĩ, rung thất)",
                "Nhịp tim nhanh nặng (>150 bpm)",
                "Thiếu máu cục bộ cơ tim (đau ngực, thay đổi ST)"
            ],
            "antidote": "Không có antidote đặc hiệu. Có thể dùng thuốc co mạch (norepinephrine) để đối kháng tác dụng giãn mạch. Điều trị rối loạn nhịp tim theo protocol.",
            "treatment": [
                "Ngừng ngay milrinone nếu đang truyền",
                "Theo dõi ECG và huyết áp liên tục",
                "Nếu hạ huyết áp nặng:",
                "  - Bù dịch (NS, LR) nếu chưa đủ",
                "  - Norepinephrine 0.05-2 mcg/kg/phút IV (co mạch, tăng huyết áp)",
                "  - Hoặc Vasopressin 0.03-0.04 units/phút IV",
                "Nếu rối loạn nhịp tim:",
                "  - Điều trị theo protocol rối loạn nhịp",
                "  - Nhịp nhanh thất: Amiodarone, Lidocaine",
                "  - Rung nhĩ: Rate control hoặc rhythm control",
                "Nếu nhịp tim nhanh nặng:",
                "  - Beta-blocker (metoprolol, esmolol) - THẬN TRỌNG nếu có hạ huyết áp",
                "  - Hoặc Diltiazem, Verapamil - THẬN TRỌNG",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG trong ít nhất 4-6 giờ"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim liên tục trong ít nhất 4-6 giờ sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (rối loạn nhịp, nhồi máu cơ tim)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Ngừng truyền và điều trị hỗ trợ (bù dịch, vasopressor nếu hạ huyết áp, điều trị rối loạn nhịp)."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha 20mg trong 100ml D5W = 200 mcg/ml. Hoặc pha 20mg trong 250ml D5W = 80 mcg/ml.",
                "infusion_rate": "Loading dose (tùy chọn): 50 mcg/kg IV bolus trong 10 phút. Maintenance: 0.375-0.75 mcg/kg/phút IV infusion. Tối đa: 1.13 mcg/kg/phút. Điều chỉnh liều theo đáp ứng huyết động. Giảm liều ở suy thận.",
                "compatibility": ["D5W (5% Dextrose)", "NS (0.9% NaCl) - có thể dùng nhưng D5W ưu tiên"],
                "incompatibility": [
                    "Không trộn với furosemide (kết tủa). Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) Pha đúng nồng độ: 20mg/100ml D5W = 200 mcg/ml, 2) Có thể bắt đầu với loading dose hoặc chỉ dùng maintenance, 3) Bù dịch đầy đủ trước khi dùng (tránh hạ huyết áp), 4) Theo dõi huyết áp và ECG chặt chẽ (rối loạn nhịp), 5) Giảm liều ở suy thận (CrCl 30-50: giảm 25-50%, CrCl <30: giảm 50-75%), 6) Không trộn với furosemide (kết tủa)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Milrinone (Primacor)",
                "ACLS Guidelines 2020 - American Heart Association",
                "Heart Failure Guidelines - ACC/AHA",
                "UpToDate - Milrinone: Drug Information",
                "Medscape - Milrinone Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Norepinephrine":     {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Norepinephrine, Noradrenaline, Levophed",
        "administration": [
            "IV"
    ],
        "indications": [
            "Sốc nhiễm khuẩn (septic shock)",
            "Sốc tim (cardiogenic shock)",
            "Sốc giảm thể tích (sau khi bù dịch)",
            "Hạ huyết áp nặng trong cấp cứu"
    ],
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [
                "Thiếu máu cục bộ mô - có thể làm nặng",
                "Pheochromocytoma - thận trọng",
                "Bệnh mạch vành nặng - có thể gây thiếu máu cục bộ"
    ],
        },
        "reversal_agents": None,
        "dosage": {
            "adult_shock": "0.05-2 mcg/kg/phút IV infusion (khởi đầu 0.05-0.1 mcg/kg/phút)",
            "adult_septic_shock": "0.05-2 mcg/kg/phút IV infusion",
            "adult_cardiogenic_shock": "0.05-2 mcg/kg/phút IV infusion",
            "notes": """Pha 4mg trong 250ml D5W = 16 mcg/ml. Truyền qua đường tĩnh mạch trung tâm để tránh hoại tử nếu rò rỉ.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
        },
        "side_effects": [
            "Tăng huyết áp",
            "Co mạch ngoại vi (giảm tưới máu mô)",
            "Hoại tử mô (nếu rò rỉ ngoài mạch)",
            "Rối loạn nhịp tim (hiếm)",
            "Tăng đường huyết",
            "Giảm tưới máu thận (với liều cao)"
    ],
        "interactions": [
            "MAOIs: tăng tác dụng",
            "TCAs: tăng tác dụng",
            "Beta-blockers: tăng huyết áp nặng"
    ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {
                "cardiac": True,
            },
            "icu_critical_care_only": True,
            "look_alike_sound_alike": [],
        },
        "guideline_tags": [
            "Surviving Sepsis Campaign Guidelines 2021",
            "SCCM Shock Management Guidelines",
            "AHA ACLS Guidelines"
    ],
        "mechanism_of_action": """Chủ yếu alpha-adrenergic receptor agonist (alpha-1 và alpha-2), một số tác dụng beta-1. Kích thích alpha-1 receptors → co mạch ngoại vi mạnh, tăng huyết áp. Kích thích beta-1 receptors → tăng nhịp tim và co bóp cơ tim nhẹ. Không có tác dụng beta-2 (không giãn phế quản). Trong sốc: tăng huyết áp và tưới máu cơ quan quan trọng.""",
        "monitoring": [
            "Huyết áp liên tục (arterial line nếu có thể)",
            "Nhịp tim và ECG",
            "Lactate máu (tưới máu mô)",
            "Đường huyết",
            "Tưới máu mô (da, thận, chi)",
            "Dấu hiệu hoại tử tại chỗ tiêm"
    ],
        "precautions": [
            "TUYỆT ĐỐI phải truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử nếu rò rỉ)",
            "Theo dõi tưới máu mô (da, thận) - có thể giảm với liều cao",
            "Bù dịch đầy đủ trước khi dùng (trừ sốc tim)",
            "Giảm liều khi huyết áp đã ổn định",
            "Theo dõi lactate để đánh giá tưới máu mô"
    ],
        "pharmacokinetics": {
            "half_life": "1-2 phút (rất ngắn)",
            "onset": "Ngay lập tức sau khi bắt đầu truyền",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Rất nhanh, bị bất hoạt bởi MAO và COMT",
        },
        "storage": """Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).""",
        "black_box_warnings": "Hoại tử mô nếu rò rỉ ngoài mạch - phải truyền qua đường tĩnh mạch trung tâm.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Norepinephrine",
                "Surviving Sepsis Campaign Guidelines",
                "UpToDate - Norepinephrine: Drug Information"
    ],
            "last_updated": "2025-02-05",
            "evidence_level": "A",
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng chủ yếu trong cấp cứu; cân nhắc lợi ích/nguy cơ cho mẹ và thai.",
            "lactation": {
                "safety": "Caution",
                "details": "Dùng ngắn hạn trong ICU; dữ liệu cho con bú rất hạn chế.",
                "recommendation": "Không dùng kéo dài; tham khảo chuyên gia khi cần.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Thận trọng; chỉnh liều theo đáp ứng huyết động.",
            "notes": "Truyền qua bơm tiêm điện với monitor liên tục; ưu tiên đường trung tâm.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi huyết áp, tưới máu ngoại vi, tổn thương đầu chi và cơ quan đích khi dùng liều cao/kéo dài.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha trong NaCl 0,9% hoặc dung dịch thích hợp; truyền qua bơm tiêm điện.",
                "infusion_rate": "Titration theo MAP mục tiêu; thường truyền qua đường trung tâm.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Theo dõi chặt ECG, huyết áp xâm lấn (nếu có) và tưới máu ngoại vi.",
            },
        },
    },
    "Phenylephrine": {
        "group": "Emergency - Alpha-1 Adrenergic Agonist (Pure)",
        "vietnamese_name": "Phenylephrine, Neosynephrine",
        "administration": ["IV"],
        "indications": [
            "Hạ huyết áp trong gây mê (anesthesia-induced hypotension)",
            "Sốc giảm thể tích (sau khi bù dịch)",
            "Hạ huyết áp do gây tê tủy sống/ngoài màng cứng",
            "Sốc nhiễm khuẩn (thay thế hoặc bổ sung norepinephrine trong một số trường hợp)",
            "Hạ huyết áp nặng trong ICU"
        ],
        "contraindications": [
            "Thiếu máu cục bộ mô nặng (chi, ruột, tim) - thận trọng",
            "Sốc giảm thể tích chưa bù dịch đầy đủ",
            "Bệnh mạch máu ngoại biên nặng"
        ],
        "dosage": {
            "adult_anesthesia": "0.5-1.5 mcg/kg/phút IV infusion (khởi đầu)",
            "adult_shock": "0.5-6 mcg/kg/phút IV infusion",
            "adult_max": "10 mcg/kg/phút IV infusion (không vượt quá)",
            "adult_bolus": "50-200 mcg IV bolus (trong gây mê)",
            "notes": "Pha 10mg trong 250ml NS = 40 mcg/ml. Khởi đầu 0.5-1.5 mcg/kg/phút, tăng dần theo đáp ứng. Thuốc lựa chọn trong gây mê. Ít dùng trong ICU so với norepinephrine."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Phản xạ nhịp chậm (baroreceptor reflex - do tăng huyết áp)",
            "Co mạch ngoại vi (thiếu máu cục bộ chi, ruột)",
            "Tăng huyết áp nặng (nếu liều cao)",
            "Giảm tưới máu thận (với liều cao)",
            "Hoại tử mô (nếu rò rỉ ngoài mạch)",
            "Đau đầu, buồn nôn"
        ],
        "interactions": [
            "MAOIs: tăng tác dụng",
            "TCAs: tăng tác dụng",
            "Beta-blockers: tăng huyết áp nặng (do không đối kháng alpha)",
            "Alpha-blockers: đối kháng tác dụng"
        ],
        "pregnancy": "C - An toàn trong cấp cứu và gây mê",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ASA Anesthesia Guidelines",
            "SCCM Shock Management Guidelines"
        ],
        "mechanism_of_action": "Phenylephrine là alpha-1-adrenergic receptor agonist thuần túy (không có tác dụng beta). Kích thích alpha-1 receptors trên cơ trơn mạch máu → co mạch ngoại vi mạnh, tăng huyết áp. Không có tác dụng beta-1 (không tăng nhịp tim, không tăng co bóp cơ tim) và không có tác dụng beta-2 (không giãn phế quản). Tăng huyết áp có thể kích hoạt phản xạ baroreceptor → nhịp chậm phản xạ. Trong gây mê: tăng huyết áp nhanh mà không tăng nhịp tim (ưu điểm so với epinephrine).",
        "monitoring": [
            "Huyết áp liên tục (arterial line nếu có thể)",
            "Nhịp tim và ECG (theo dõi nhịp chậm phản xạ)",
            "Tưới máu mô (da, thận, chi) - nguy cơ thiếu máu cục bộ",
            "Lactate máu (tưới máu mô)",
            "Dấu hiệu hoại tử tại chỗ tiêm",
            "Nước tiểu giờ (diuresis - có thể giảm với liều cao)"
        ],
        "precautions": [
            "Truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử nếu rò rỉ)",
            "Bù dịch đầy đủ trước khi dùng (tránh sốc giảm thể tích)",
            "Theo dõi nhịp chậm phản xạ (có thể cần atropine nếu nhịp chậm nặng)",
            "Thận trọng ở bệnh nhân có bệnh mạch máu ngoại biên, bệnh mạch vành",
            "Giảm liều khi huyết áp đã ổn định",
            "Ít dùng trong ICU so với norepinephrine (do không tăng cung lượng tim)",
            "Thuốc lựa chọn trong gây mê (tăng huyết áp mà không tăng nhịp tim)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (dài hơn catecholamine)",
            "onset": "Ngay lập tức sau khi bắt đầu truyền",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Chuyển hóa ở gan (MAO), thải trừ qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Kiểm tra màu sắc trước dùng.",
        "black_box_warnings": "Hoại tử mô nếu rò rỉ ngoài mạch - phải truyền qua đường tĩnh mạch trung tâm.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (non-selective)",
                    "mechanism": "Beta-blockers không đối kháng tác dụng alpha của phenylephrine, nhưng ngăn chặn phản xạ nhịp chậm. Kết quả: tăng huyết áp nặng mà không có nhịp chậm bù trừ.",
                    "effect": "Tăng huyết áp nặng, nguy cơ đột quỵ, nhồi máu cơ tim",
                    "management": "TRÁNH dùng phenylephrine với beta-blockers non-selective. Nếu cần: dùng liều thấp, theo dõi huyết áp chặt chẽ."
                },
                {
                    "drug": "MAOIs (Monoamine Oxidase Inhibitors)",
                    "mechanism": "MAOIs ức chế enzyme MAO chuyển hóa phenylephrine, làm tăng nồng độ và thời gian tác dụng.",
                    "effect": "Tăng tác dụng và thời gian tác dụng, tăng nguy cơ tăng huyết áp nặng",
                    "management": "GIẢM LIỀU phenylephrine xuống 10-25% liều thông thường. Theo dõi huyết áp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Tricyclic Antidepressants (TCAs)",
                    "mechanism": "TCAs ức chế tái hấp thu norepinephrine, tăng tác dụng của phenylephrine.",
                    "effect": "Tăng tác dụng, tăng nguy cơ tăng huyết áp nặng",
                    "management": "Thận trọng, giảm liều. Theo dõi huyết áp chặt chẽ."
                },
                {
                    "drug": "Alpha-blockers",
                    "mechanism": "Alpha-blockers đối kháng tác dụng alpha của phenylephrine.",
                    "effect": "Giảm hiệu quả điều trị, có thể cần liều cao hơn",
                    "management": "Có thể cần tăng liều. Theo dõi đáp ứng điều trị."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng phenylephrine (hiếm)",
                "Thiếu máu cục bộ mô nặng (chi, ruột, tim) - thận trọng"
            ],
            "tương_đối": [
                "Sốc giảm thể tích chưa bù dịch đầy đủ - bù dịch trước",
                "Bệnh mạch máu ngoại biên nặng - tăng nguy cơ thiếu máu cục bộ",
                "Bệnh mạch vành - tăng nguy cơ thiếu máu cục bộ cơ tim",
                "Suy thận nặng - có thể giảm tưới máu thận",
                "Dùng với beta-blockers non-selective - tăng huyết áp nặng",
                "Dùng với MAOIs - tăng tác dụng, cần giảm liều",
                "Bệnh nhân cao tuổi - tăng nhạy cảm với tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Phenylephrine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Phenylephrine có thể qua nhau thai và có thể gây co mạch, giảm tưới máu nhau thai. Tuy nhiên, trong cấp cứu và gây mê, lợi ích vượt quá nguy cơ. Phenylephrine được sử dụng rộng rãi trong gây mê sản khoa để điều trị hạ huyết áp do gây tê tủy sống/ngoài màng cứng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Phenylephrine có thời gian bán thải 2-3 giờ và chuyển hóa ở gan. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Phenylephrine không bài tiết vào sữa mẹ ở nồng độ đáng kể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa ở gan)",
            "severe": "Thận trọng, có thể tăng tác dụng (giảm chuyển hóa)",
            "notes": "Phenylephrine chuyển hóa ở gan bởi MAO. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng. Tuy nhiên, do thời gian bán thải dài (2-3 giờ), tích lũy ít hơn so với catecholamine."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng huyết áp nặng (có thể >200/120 mmHg)",
                "Nhịp chậm phản xạ (do tăng huyết áp)",
                "Thiếu máu cục bộ chi, ruột, cơ tim",
                "Nhồi máu cơ tim",
                "Đột quỵ",
                "Hoại tử mô (nếu rò rỉ ngoài mạch)"
            ],
            "antidote": "Không có antidote đặc hiệu. Có thể dùng thuốc giãn mạch (phentolamine, nitroglycerin) để đối kháng tác dụng alpha. Atropine có thể dùng nếu nhịp chậm nặng.",
            "treatment": [
                "Ngừng ngay phenylephrine nếu đang truyền",
                "Theo dõi ECG và huyết áp liên tục",
                "Nếu tăng huyết áp nặng:",
                "  - Phentolamine 5-10mg IV (đối kháng alpha, giảm huyết áp)",
                "  - Hoặc Nitroglycerin IV (giãn mạch, giảm huyết áp)",
                "Nếu nhịp chậm nặng:",
                "  - Atropine 0.5-1mg IV (chống nhịp chậm phản xạ)",
                "Nếu thiếu máu cục bộ:",
                "  - Ngừng phenylephrine",
                "  - Điều trị hỗ trợ (giảm đau, chống đông nếu cần)",
                "Nếu hoại tử mô (tiêm ngoài mạch):",
                "  - Phentolamine 5-10mg pha trong 10-15ml NS tiêm quanh vùng hoại tử (trong vòng 12 giờ)",
                "  - Chườm ấm",
                "  - Có thể cần phẫu thuật nếu hoại tử nặng",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG trong ít nhất 2-4 giờ"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim liên tục trong ít nhất 2-4 giờ sau khi dùng. Theo dõi tưới máu mô (da, chi, thận). Theo dõi lâu hơn nếu có biến chứng (nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Phentolamine",
                    "mechanism": "Alpha-blocker, đối kháng tác dụng alpha của phenylephrine (co mạch, tăng huyết áp)",
                    "indication": "Tăng huyết áp nặng do quá liều phenylephrine, hoại tử mô do tiêm ngoài mạch",
                    "dose": "5-10mg IV cho tăng huyết áp, 5-10mg pha trong 10-15ml NS tiêm quanh vùng hoại tử (trong vòng 12 giờ)"
                },
                {
                    "agent": "Nitroglycerin",
                    "mechanism": "Giãn mạch, giảm huyết áp",
                    "indication": "Tăng huyết áp nặng do quá liều phenylephrine",
                    "dose": "5-10mcg/phút IV, tăng dần đến khi đạt huyết áp mục tiêu"
                },
                {
                    "agent": "Atropine",
                    "mechanism": "Chống nhịp chậm phản xạ (do tăng huyết áp)",
                    "indication": "Nhịp chậm nặng do phản xạ baroreceptor",
                    "dose": "0.5-1mg IV, lặp lại nếu cần"
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha 10mg trong 250ml NS = 40 mcg/ml. Hoặc pha 10mg trong 100ml NS = 100 mcg/ml.",
                "infusion_rate": "Khởi đầu 0.5-1.5 mcg/kg/phút IV infusion. Tăng dần 0.5 mcg/kg/phút mỗi 10 phút theo đáp ứng. Liều thường dùng: 0.5-6 mcg/kg/phút. Tối đa: 10 mcg/kg/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."
                ],
                "notes": "QUAN TRỌNG: 1) Pha đúng nồng độ: 10mg/250ml NS = 40 mcg/ml, 2) TUYỆT ĐỐI phải truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử nếu rò rỉ), 3) Khởi đầu liều thấp (0.5-1.5 mcg/kg/phút), 4) Theo dõi huyết áp và nhịp tim chặt chẽ (nhịp chậm phản xạ), 5) Bù dịch đầy đủ trước khi dùng, 6) Thuốc lựa chọn trong gây mê (tăng huyết áp mà không tăng nhịp tim)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Phenylephrine",
                "ACLS Guidelines 2020 - American Heart Association",
                "Surviving Sepsis Campaign Guidelines",
                "UpToDate - Phenylephrine: Drug Information",
                "Anesthesia Guidelines - Phenylephrine for spinal/epidural hypotension",
                "Medscape - Phenylephrine Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Vasopressin": {
        "group": "Emergency - Vasopressor (Non-catecholamine)",
        "vietnamese_name": "Vasopressin, Arginine vasopressin",
        "administration": ["IV"],
        "indications": [
            "Sốc nhiễm khuẩn (septic shock) cần vasopressor liều cao",
            "Sốc giãn mạch (vasodilatory shock) kháng catecholamine",
            "Hạ huyết áp nặng trong ICU (dùng kèm norepinephrine)"
        ],
        "contraindications": [
            "Thiếu máu cục bộ mô nặng (chi, ruột, tim) - thận trọng",
            "Sốc giảm thể tích chưa bù dịch đầy đủ"
        ],
        "dosage": {
            "adult_shock_fixed_dose": "0.03 units/phút IV liên tục (0.01–0.03 units/phút)",
            "adult_shock_high_dose": "0.04–0.06 units/phút IV (tránh vượt quá nếu không có chỉ định chuyên sâu)",
            "notes": "Dùng như thuốc bổ sung (add‑on) cho norepinephrine, KHÔNG thay thế hoàn toàn norepinephrine. Không titrate nhanh theo huyết áp như catecholamine."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Co mạch ngoại vi (lạnh đầu chi, tím đầu ngón)",
            "Thiếu máu cục bộ chi, ruột, cơ tim (liều cao, dùng kéo dài)",
            "Hạ natri máu (nếu dùng kéo dài)",
            "Đau đầu, buồn nôn"
        ],
        "interactions": [
            "Các vasopressor khác (norepinephrine, epinephrine, dopamine): tăng nguy cơ thiếu máu cục bộ chi",
            "Sodium bicarbonate: KHÔNG pha chung cùng line (môi trường kiềm làm giảm hiệu lực vasopressors)"
        ],,
"pregnancy": "C - Có thể dùng trong cấp cứu nếu lợi ích > nguy cơ",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True, "renal": True},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "Surviving Sepsis Campaign Guidelines 2021",
            "SCCM Shock Management Guidelines"
        ],
        "mechanism_of_action": "Vasopressin là hormon nội sinh (arginine vasopressin). Kích thích V1a receptors trên cơ trơn mạch máu → co mạch mạnh, tăng huyết áp; kích thích V2 receptors tại ống góp thận → tăng tái hấp thu nước. Trong sốc nhiễm khuẩn, bệnh nhân thường thiếu tương đối vasopressin nội sinh, nên bổ sung liều thấp giúp phục hồi trương lực mạch mà không làm tăng nhịp tim.",
        "monitoring": [
            "Huyết áp động mạch (ưu tiên arterial line)",
            "Tưới máu chi (màu da, nhiệt độ, refill mao mạch)",
            "Dấu hiệu thiếu máu cục bộ ruột (đau bụng, chướng bụng, lactate tăng)",
            "Điện giải, đặc biệt natri máu",
            "Nước tiểu giờ (diuresis)"
        ],
        "precautions": [
            "Không dùng đơn độc liều cao để thay norepinephrine – chỉ dùng như thuốc bổ sung.",
            "Tránh vượt quá 0.06 units/phút trừ khi có chỉ định và theo dõi rất sát.",
            "Thận trọng ở bệnh nhân có bệnh mạch máu ngoại vi, bệnh mạch vành, nguy cơ thiếu máu cục bộ ruột.",
            "Bù dịch đầy đủ trước khi dùng (tránh sốc giảm thể tích).",
            "Dùng line truyền riêng, không pha chung với sodium bicarbonate."
        ],
        "pharmacokinetics": {
            "half_life": "10–20 phút",
            "onset": "Vài phút sau khi bắt đầu truyền",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan, thận và phân hủy bởi peptidase."
        },
        "storage": "Bảo quản theo hướng dẫn chế phẩm (thường 2–8°C), tránh đông lạnh. Dung dịch đã pha: dùng trong thời gian khuyến cáo của nhà sản xuất, tránh ánh sáng trực tiếp.",
        "black_box_warnings": None,
        "references": {
            "primary_sources": [
                "Surviving Sepsis Campaign Guidelines 2021",
                "UpToDate - Vasopressin for vasodilatory shock",
                "FDA Drug Label - Vasopressin"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Các vasopressor khác (norepinephrine, epinephrine, dopamine): tăng nguy cơ thiếu máu cục bộ chi",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Sodium bicarbonate: KHÔNG pha chung cùng line (môi trường kiềm làm giảm hiệu lực vasopressors)",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "C - Có thể dùng trong cấp cứu nếu lợi ích > nguy cơ",
                  "pregnancy_details": "Category C - Có thể dùng trong cấp cứu nếu lợi ích > nguy cơ - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng",
                  "severe": "Thận trọng, có thể giảm liều",
                  "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
              },
              "overdose_management": {
                  "symptoms": [
                      "Tăng huyết áp nặng",
                      "Thiếu máu cục bộ chi, ruột",
                      "Loạn nhịp tim",
                      "Phù phổi"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Điều trị hỗ trợ: hạ huyết áp nếu cần",
                      "Theo dõi tưới máu chi, ruột",
                      "Điều trị triệu chứng"
                  ],
                  "monitoring": "Theo dõi huyết áp, tưới máu chi, dấu hiệu thiếu máu cục bộ"
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
    
}

__all__ = ['CATECHOLAMINE_ALPHA_BETA_AGONISTS_DRUGS']
