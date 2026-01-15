"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Thiazolidinedione (TZD)s

THIAZOLIDINEDIONE_TZDS_DRUGS = {
    "Pioglitazone": {'group': 'Diabetes - Thiazolidinedione (TZD)',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        'vietnamese_name':
        'Pioglitazone, Actos', 'administration': ['PO'],
        'indications': [
        'Đái tháo đường type 2'],
        'contraindications': [
        'Suy tim (NYHA class III-IV)', 'Bệnh gan nặng', 'Ung thư bàng quang',
        'Gãy xương (phụ nữ có nguy cơ)'],
        'dosage': {
            'adult_start': '15-30mg PO x 1 lần/ngày',
            'adult_usual': '15-45mg PO x 1 lần/ngày. Thường 15-30mg/ngày, có thể tăng lên 45mg nếu cần.',
            'adult_max': '45mg/ngày',
            'dm_t2': 'Khởi đầu 15-30mg PO x 1 lần/ngày. Có thể tăng lên 45mg sau ít nhất 2-4 tuần nếu cần và dung nạp tốt. Tối đa 45mg/ngày. Tác dụng chậm (2-4 tuần) - cần kiên nhẫn.',
            'elderly': 'Khởi đầu 15mg PO x 1 lần/ngày, tăng dần chậm hơn. Người cao tuổi nhạy cảm hơn với tác dụng phụ (giữ nước, phù, suy tim). Thận trọng đặc biệt với suy tim.',
            'pregnancy': 'Category C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ.',
            'renal_adjustment_dosage': {
                'normal': '15-45mg PO x 1 lần/ngày (CrCl ≥60)',
                '30_60': '15-45mg PO x 1 lần/ngày (CrCl 30-60). Không cần điều chỉnh liều đặc biệt, nhưng thận trọng với suy tim.',
                'under_30': 'Thận trọng, có thể cần giảm liều. 15-30mg PO x 1 lần/ngày (CrCl <30). Theo dõi chức năng thận và dấu hiệu suy tim chặt chẽ.',
                'dialysis': 'Thận trọng. Có thể dùng 15-30mg PO x 1 lần/ngày. Theo dõi chức năng thận và dấu hiệu suy tim chặt chẽ.'
            },
            'hepatic_adjustment_dosage': {
                'mild': '15-45mg PO x 1 lần/ngày. Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.',
                'moderate': 'Thận trọng, theo dõi chức năng gan chặt chẽ. 15-30mg PO x 1 lần/ngày. Ngừng nếu ALT >3x ULN.',
                'severe': 'CHỐNG CHỈ ĐỊNH - Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc gan.'
            },
            'administration_route': 'PO (uống)',
            'frequency': '1 lần/ngày',
            'with_food': 'Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày.',
            'timing': 'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày (sáng, trưa, tối). Uống cùng giờ mỗi ngày để dễ nhớ. Không phụ thuộc bữa ăn.',
            'titration': 'Tăng liều từ từ: Tuần 1-4: 15-30mg/ngày. Tuần 5-8: 30-45mg/ngày (nếu cần và dung nạp tốt). Đánh giá hiệu quả sau mỗi 2-4 tuần. Tác dụng chậm (2-4 tuần) - cần kiên nhẫn.',
            'notes': 'Uống bất kỳ lúc nào, không cần thức ăn. Tác dụng chậm (2-4 tuần) - cần kiên nhẫn. Gây giữ nước, phù - tăng nguy cơ suy tim. CHỐNG CHỈ ĐỊNH ở suy tim (NYHA class III-IV). Ngừng ngay nếu có dấu hiệu suy tim. Tránh dùng với insulin nếu có thể (tăng nguy cơ suy tim, phù). Tăng nguy cơ gãy xương ở phụ nữ. Tăng nhẹ nguy cơ ung thư bàng quang.'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'},
        'side_effects': [
        'Giữ nước, phù (tăng nguy cơ suy tim)', 'Tăng cân',
        'Gãy xương (phụ nữ có nguy cơ tăng)', 'Thiếu máu',
        'Tăng LDL cholesterol', 'Ung thư bàng quang (tăng nhẹ nguy cơ)'],
        'interactions': ['Insulin: tăng nguy cơ suy tim, phù',
        'Digoxin: có thể tăng nồng độ digoxin'],
        'mechanism_of_action':
        'Pioglitazone là thiazolidinedione (TZD), hoạt động như agonist của PPAR-gamma (peroxisome proliferator-activated receptor gamma). Khi gắn vào PPAR-gamma trong nhân tế bào, pioglitazone kích hoạt phiên mã các gen liên quan đến chuyển hóa glucose và lipid, tăng nhạy cảm với insulin ở mô ngoại vi (cơ, mỡ, gan). Thuốc giảm đề kháng insulin, tăng sử dụng glucose ở mô ngoại vi, giảm sản xuất glucose ở gan, và giảm giải phóng acid béo tự do từ mô mỡ. Tác dụng chậm (2-4 tuần), và có thể gây giữ nước, tăng cân'
        , 'monitoring': ['HbA1c mỗi 3 tháng', 'Đường huyết đói',
        'Chức năng gan (ALT, AST) trước và trong 12 tháng đầu (nguy cơ độc gan)',
        'Dấu hiệu suy tim (khó thở, phù, tăng cân) - đặc biệt khi dùng với insulin'
        , 'Dấu hiệu gãy xương (đặc biệt ở phụ nữ)', 'Công thức máu (thiếu máu)',
        'Lipid (LDL cholesterol có thể tăng)',
        'Ung thư bàng quang (tăng nhẹ nguy cơ - cần theo dõi)'],
        'precautions':
        ['Không dùng nếu suy tim (NYHA class III-IV)',
        'Ngừng ngay nếu có dấu hiệu suy tim',
        'Tránh dùng với insulin nếu có thể (tăng nguy cơ suy tim, phù)',
        'Tác dụng chậm (2-4 tuần) - cần kiên nhẫn',
        'Có thể gây giữ nước và phù (tăng nguy cơ suy tim)',
        'Có thể gây tăng cân', 'Tăng nguy cơ gãy xương ở phụ nữ (cần theo dõi)',
        'Tăng nhẹ nguy cơ ung thư bàng quang (cần theo dõi)',
        'Ngừng nếu ALT >3x ULN (nguy cơ độc gan)',
        'Có thể dùng trong thai kỳ (category C)'],
        'pharmacokinetics': {
        'half_life': '16-24 giờ (dài)', 'onset': '2-4 tuần (giảm HbA1c)',
        'duration': '24 giờ', 'protein_binding': '>99%', 'clearance':
        'Gan (chuyển hóa qua CYP2C8, CYP3A4), thận (thải trừ)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Có thể gây suy tim hoặc làm trầm trọng suy tim hiện có. Không dùng nếu suy tim (NYHA class III-IV). Ngừng ngay nếu có dấu hiệu suy tim. Có thể gây độc gan - ngừng nếu ALT >3x ULN'
        , 'drug_interactions': {'major': [{'drug': 'Insulin', 'mechanism':
        'Cả hai đều tăng giữ nước, tác dụng cộng dồn.', 'effect':
        'Tăng nguy cơ suy tim, phù, giữ nước nghiêm trọng', 'management':
        'Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu suy tim, phù. Có thể cần giảm liều insulin.'
        }, {'drug': 'Digoxin', 'mechanism':
        'Pioglitazone có thể tăng nồng độ digoxin.', 'effect':
        'Tăng nồng độ digoxin, tăng nguy cơ độc tính', 'management':
        'Theo dõi nồng độ digoxin và điều chỉnh liều nếu cần.'}, {'drug':
        'Gemfibrozil', 'mechanism':
        'Gemfibrozil ức chế CYP2C8, làm giảm chuyển hóa pioglitazone.',
        'effect': 'Tăng nồng độ pioglitazone, tăng nguy cơ tác dụng phụ',
        'management': 'Thận trọng. Có thể cần giảm liều pioglitazone.'}],
        'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Đái tháo đường type 1 - không hiệu quả (cần insulin)',
        'Suy tim (NYHA class III-IV) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ suy tim)',
        'Bệnh gan nặng - chống chỉ định (nguy cơ độc gan)',
        'Ung thư bàng quang - chống chỉ định (tăng nguy cơ)'],
        'tương_đối': [
        'Suy tim (NYHA class I-II) - thận trọng, theo dõi sát',
        'Gãy xương (phụ nữ có nguy cơ tăng) - thận trọng',
        'Có thai - category C, thận trọng', 'Suy thận nặng - thận trọng',
        'Đang dùng insulin - tăng nguy cơ suy tim']},
        'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Pioglitazone là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt đầu. Có thể gây giữ nước, phù ở mẹ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không biết pioglitazone có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.'
        }},
        'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Theo dõi chức năng gan.', 'moderate':
        'Thận trọng, theo dõi chức năng gan chặt chẽ. Ngừng nếu ALT >3x ULN.',
        'severe':
        'Chống chỉ định. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc gan.',
        'notes':
        'Pioglitazone chuyển hóa ở gan qua CYP2C8 và CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc gan. Ngừng nếu ALT >3x ULN hoặc có dấu hiệu độc gan.'
        },
        'overdose_management': {'symptoms': ['Suy tim, phù nặng, giữ nước',
        'Hạ đường huyết (nếu dùng với insulin/sulfonylurea)',
        'Độc gan (vàng da, tăng ALT/AST)', 'Thiếu máu nặng'],
        'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng pioglitazone ngay lập tức',
        'Nếu suy tim: điều trị suy tim (diuretics, ACE inhibitors), theo dõi chặt chẽ'
        'Nếu hạ đường huyết: glucose đường uống hoặc IV, theo dõi đường huyết',
        'Nếu độc gan: điều trị hỗ trợ gan, theo dõi ALT/AST',
        'Nếu thiếu máu: điều trị hỗ trợ, có thể cần truyền máu',
        'Theo dõi dấu hiệu sinh tồn, chức năng gan, chức năng tim'],
        'monitoring':
        'Dấu hiệu suy tim, phù, đường huyết, chức năng gan, công thức máu, dấu hiệu sinh tồn'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có suy tim, độc tính gan, hoặc phản ứng dị ứng nghiêm trọng.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Không ảnh hưởng hấp thu.',
        'timing': 'Uống 1 lần/ngày, bất kỳ lúc nào, cùng thời điểm mỗi ngày.'},
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': [],
        }},
        'references': {'primary_sources': [
        'FDA Drug Label - Pioglitazone (Actos)',
        'UpToDate - Pioglitazone: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ],
        'evidence_level':
        'A - Dựa trên FDA drug labels và dữ liệu lâm sàng'}},
    
    "Rosiglitazone": {
        "group": "Diabetes - Thiazolidinedione (TZD)",
        "vietnamese_name": "Rosiglitazone, Avandia",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Kết hợp với metformin hoặc sulfonylurea"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Suy tim (NYHA class III-IV)",
            "Bệnh gan nặng",
            "Gãy xương (phụ nữ có nguy cơ)"
        ],
        "dosage": {
            "adult_start": "4mg PO x 1 lần/ngày hoặc 2mg PO x 2 lần/ngày",
            "adult_usual": "4-8mg PO/ngày (chia 1-2 lần). Thường 4mg x 1 lần/ngày hoặc 2mg x 2 lần/ngày, có thể tăng lên 8mg/ngày nếu cần.",
            "adult_max": "8mg/ngày",
            "dm_t2": "Khởi đầu 4mg PO x 1 lần/ngày hoặc 2mg PO x 2 lần/ngày. Có thể tăng lên 8mg/ngày (4mg x 2 lần/ngày hoặc 8mg x 1 lần/ngày) sau ít nhất 2-4 tuần nếu cần và dung nạp tốt. Tối đa 8mg/ngày. Tác dụng chậm (2-4 tuần) - cần kiên nhẫn.",
            "elderly": "Khởi đầu 2mg PO x 2 lần/ngày hoặc 4mg PO x 1 lần/ngày, tăng dần chậm hơn. Người cao tuổi nhạy cảm hơn với tác dụng phụ (giữ nước, phù, suy tim). Thận trọng đặc biệt với suy tim.",
            "pregnancy": "Category C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ.",
            "renal_adjustment_dosage": {
                "normal": "4-8mg PO/ngày chia 1-2 lần (CrCl ≥60)",
                "30_60": "4-8mg PO/ngày chia 1-2 lần (CrCl 30-60). Không cần điều chỉnh liều đặc biệt, nhưng thận trọng với suy tim.",
                "under_30": "Thận trọng, có thể cần giảm liều. 2-4mg PO x 2 lần/ngày hoặc 4mg PO x 1 lần/ngày (CrCl <30). Theo dõi chức năng thận và dấu hiệu suy tim chặt chẽ.",
                "dialysis": "Thận trọng. Có thể dùng 2-4mg PO x 2 lần/ngày hoặc 4mg PO x 1 lần/ngày. Theo dõi chức năng thận và dấu hiệu suy tim chặt chẽ."
            },
            "hepatic_adjustment_dosage": {
                "mild": "4-8mg PO/ngày chia 1-2 lần. Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.",
                "moderate": "Thận trọng, theo dõi chức năng gan chặt chẽ. 2-4mg PO x 2 lần/ngày hoặc 4mg PO x 1 lần/ngày. Ngừng nếu ALT >3x ULN.",
                "severe": "CHỐNG CHỈ ĐỊNH - Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc gan."
            },
            "administration_route": "PO (uống)",
            "frequency": "1-2 lần/ngày (thường 1 lần/ngày với liều ≤4mg, chia 2 lần với liều >4mg)",
            "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày.",
            "timing": "Uống 1-2 lần/ngày. Với liều ≤4mg: 1 lần/ngày (sáng hoặc tối). Với liều >4mg: chia 2 lần/ngày (sáng và tối). Uống cùng giờ mỗi ngày để dễ nhớ. Không phụ thuộc bữa ăn.",
            "titration": "Tăng liều từ từ: Tuần 1-4: 4mg/ngày (1 lần hoặc chia 2 lần). Tuần 5-8: 8mg/ngày (4mg x 2 lần/ngày hoặc 8mg x 1 lần/ngày) nếu cần và dung nạp tốt. Đánh giá hiệu quả sau mỗi 2-4 tuần. Tác dụng chậm (2-4 tuần) - cần kiên nhẫn.",
            "notes": "Uống bất kỳ lúc nào, không cần thức ăn. Tác dụng chậm (2-4 tuần) - cần kiên nhẫn. Gây giữ nước, phù - tăng nguy cơ suy tim. CHỐNG CHỈ ĐỊNH ở suy tim (NYHA class III-IV). Ngừng ngay nếu có dấu hiệu suy tim. Có thể tăng nguy cơ nhồi máu cơ tim (controversial, đã bị hạn chế sử dụng ở một số nước). Tăng nguy cơ gãy xương ở phụ nữ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Giữ nước, phù (tăng nguy cơ suy tim)",
            "Tăng cân",
            "Gãy xương (phụ nữ có nguy cơ tăng)",
            "Thiếu máu",
            "Tăng LDL cholesterol",
            "Tăng nguy cơ nhồi máu cơ tim (controversial)"
        ],
        "interactions": [
            "Insulin: tăng nguy cơ suy tim, phù",
            "Digoxin: có thể tăng nồng độ digoxin",
            "Gemfibrozil: tăng nồng độ rosiglitazone"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Rosiglitazone là thiazolidinedione (TZD), hoạt động như agonist của PPAR-gamma (peroxisome proliferator-activated receptor gamma). Khi gắn vào PPAR-gamma trong nhân tế bào, rosiglitazone kích hoạt phiên mã các gen liên quan đến chuyển hóa glucose và lipid, tăng nhạy cảm với insulin ở mô ngoại vi (cơ, mỡ, gan). Thuốc giảm đề kháng insulin, tăng sử dụng glucose ở mô ngoại vi, giảm sản xuất glucose ở gan, và giảm giải phóng acid béo tự do từ mô mỡ. Tác dụng chậm (2-4 tuần), và có thể gây giữ nước, tăng cân. Rosiglitazone có thể tăng nguy cơ nhồi máu cơ tim (controversial, đã bị hạn chế sử dụng ở một số nước).",
        "monitoring": [
            "HbA1c mỗi 3 tháng",
            "Đường huyết đói",
            "Chức năng gan (ALT, AST) trước và trong 12 tháng đầu (nguy cơ độc gan)",
            "Dấu hiệu suy tim (khó thở, phù, tăng cân) - đặc biệt khi dùng với insulin",
            "Dấu hiệu gãy xương (đặc biệt ở phụ nữ)",
            "Công thức máu (thiếu máu)",
            "Lipid (LDL cholesterol có thể tăng)",
            "Tim mạch (ECG, triệu chứng đau ngực) - theo dõi nguy cơ nhồi máu cơ tim"
        ],
        "precautions": [
            "Không dùng nếu suy tim (NYHA class III-IV)",
            "Ngừng ngay nếu có dấu hiệu suy tim",
            "Tránh dùng với insulin nếu có thể (tăng nguy cơ suy tim, phù)",
            "Tác dụng chậm (2-4 tuần) - cần kiên nhẫn",
            "Có thể gây giữ nước và phù (tăng nguy cơ suy tim)",
            "Có thể gây tăng cân",
            "Tăng nguy cơ gãy xương ở phụ nữ (cần theo dõi)",
            "Tăng nguy cơ nhồi máu cơ tim (controversial - đã bị hạn chế sử dụng ở một số nước)",
            "Ngừng nếu ALT >3x ULN (nguy cơ độc gan)",
            "Có thể dùng trong thai kỳ (category C)"
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (ngắn hơn pioglitazone)",
            "onset": "2-4 tuần (giảm HbA1c)",
            "duration": "24 giờ",
            "protein_binding": ">99%",
            "clearance": "Gan (chuyển hóa qua CYP2C8, CYP2C9), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Có thể gây suy tim hoặc làm trầm trọng suy tim hiện có. Không dùng nếu suy tim (NYHA class III-IV). Ngừng ngay nếu có dấu hiệu suy tim. Có thể gây độc gan - ngừng nếu ALT >3x ULN. Tăng nguy cơ nhồi máu cơ tim (controversial - đã bị hạn chế sử dụng ở một số nước).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin",
                    "mechanism": "Cả hai đều tăng giữ nước, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ suy tim, phù, giữ nước nghiêm trọng",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu suy tim, phù. Có thể cần giảm liều insulin."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Rosiglitazone có thể tăng nồng độ digoxin.",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Gemfibrozil ức chế CYP2C8, tăng nồng độ rosiglitazone",
                    "effect": "Tăng nồng độ rosiglitazone, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi dấu hiệu tác dụng phụ. Có thể cần giảm liều rosiglitazone."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Suy tim (NYHA class III-IV)",
                "Bệnh gan nặng",
                "Dị ứng rosiglitazone hoặc TZD"
            ],
            "tương_đối": [
                "Suy tim nhẹ-trung bình (NYHA class I-II) - thận trọng, theo dõi sát",
                "Bệnh tim mạch - tăng nguy cơ nhồi máu cơ tim",
                "Gãy xương (phụ nữ có nguy cơ tăng)",
                "Có thai - category C"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Rosiglitazone bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Theo dõi men gan.",
            "moderate": "Thận trọng, theo dõi men gan. Có thể cần giảm liều.",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Rosiglitazone chuyển hóa ở gan qua CYP2C8 và CYP2C9. Suy gan làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ độc gan. CHỐNG CHỈ ĐỊNH ở suy gan nặng. Ngừng nếu ALT >3x ULN."
        },
        "overdose_management": {
            "symptoms": [
                "Giữ nước, phù",
                "Suy tim",
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Độc gan (tăng ALT, AST)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng rosiglitazone ngay lập tức",
                "Điều trị suy tim nếu có (diuretics, ACE inhibitors)",
                "Điều trị hạ đường huyết nếu có (glucose)",
                "Theo dõi chức năng gan",
                "Theo dõi tại bệnh viện"
            ],
            "monitoring": "Dấu hiệu sinh tồn, chức năng gan, dấu hiệu suy tim, đường huyết"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày.",
                "timing": "Uống 1-2 lần/ngày. Có thể uống 4mg x 1 lần/ngày hoặc 2mg x 2 lần/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Rosiglitazone (Avandia)",
                "UpToDate - Rosiglitazone: Drug Information",
                "Nissen SE, Wolski K. Effect of rosiglitazone on the risk of myocardial infarction and death from cardiovascular causes. N Engl J Med. 2007",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs (controversial về nguy cơ tim mạch)"
        }
    },
}

__all__ = ['THIAZOLIDINEDIONE_TZDS_DRUGS']
