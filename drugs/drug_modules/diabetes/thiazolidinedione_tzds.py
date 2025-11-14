"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Thiazolidinedione (TZD)s

THIAZOLIDINEDIONE_TZDS_DRUGS = {
    "Pioglitazone": {'group': 'Diabetes - Thiazolidinedione (TZD)', 'vietnamese_name':
        'Pioglitazone, Actos', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2'], 'contraindications': ['Đái tháo đường type 1',
        'Suy tim (NYHA class III-IV)', 'Bệnh gan nặng', 'Ung thư bàng quang',
        'Gãy xương (phụ nữ có nguy cơ)'], 'dosage': {'adult_start':
        '15-30mg x 1 lần/ngày', 'adult_usual': '15-45mg x 1 lần/ngày',
        'adult_max': '45mg/ngày', 'notes':
        'Uống bất kỳ lúc nào. Tác dụng chậm (2-4 tuần). Gây giữ nước'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'}, 'side_effects': [
        'Giữ nước, phù (tăng nguy cơ suy tim)', 'Tăng cân',
        'Gãy xương (phụ nữ có nguy cơ tăng)', 'Thiếu máu',
        'Tăng LDL cholesterol', 'Ung thư bàng quang (tăng nhẹ nguy cơ)'],
        'interactions': ['Insulin: tăng nguy cơ suy tim, phù',
        'Digoxin: có thể tăng nồng độ digoxin'], 'pregnancy': 'C',
        'mechanism_of_action':
        'Pioglitazone là thiazolidinedione (TZD), hoạt động như agonist của PPAR-gamma (peroxisome proliferator-activated receptor gamma). Khi gắn vào PPAR-gamma trong nhân tế bào, pioglitazone kích hoạt phiên mã các gen liên quan đến chuyển hóa glucose và lipid, tăng nhạy cảm với insulin ở mô ngoại vi (cơ, mỡ, gan). Thuốc giảm đề kháng insulin, tăng sử dụng glucose ở mô ngoại vi, giảm sản xuất glucose ở gan, và giảm giải phóng acid béo tự do từ mô mỡ. Tác dụng chậm (2-4 tuần), và có thể gây giữ nước, tăng cân'
        , 'monitoring': ['HbA1c mỗi 3 tháng', 'Đường huyết đói',
        'Chức năng gan (ALT, AST) trước và trong 12 tháng đầu (nguy cơ độc gan)',
        'Dấu hiệu suy tim (khó thở, phù, tăng cân) - đặc biệt khi dùng với insulin'
        , 'Dấu hiệu gãy xương (đặc biệt ở phụ nữ)', 'Công thức máu (thiếu máu)',
        'Lipid (LDL cholesterol có thể tăng)',
        'Ung thư bàng quang (tăng nhẹ nguy cơ - cần theo dõi)'], 'precautions':
        ['Không dùng nếu suy tim (NYHA class III-IV)',
        'Ngừng ngay nếu có dấu hiệu suy tim',
        'Tránh dùng với insulin nếu có thể (tăng nguy cơ suy tim, phù)',
        'Tác dụng chậm (2-4 tuần) - cần kiên nhẫn',
        'Có thể gây giữ nước và phù (tăng nguy cơ suy tim)',
        'Có thể gây tăng cân', 'Tăng nguy cơ gãy xương ở phụ nữ (cần theo dõi)',
        'Tăng nhẹ nguy cơ ung thư bàng quang (cần theo dõi)',
        'Ngừng nếu ALT >3x ULN (nguy cơ độc gan)',
        'Có thể dùng trong thai kỳ (category C)'], 'pharmacokinetics': {
        'half_life': '16-24 giờ (dài)', 'onset': '2-4 tuần (giảm HbA1c)',
        'duration': '24 giờ', 'protein_binding': '>99%', 'clearance':
        'Gan (chuyển hóa qua CYP2C8, CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Có thể gây suy tim hoặc làm trầm trọng suy tim hiện có. Không dùng nếu suy tim (NYHA class III-IV). Ngừng ngay nếu có dấu hiệu suy tim. Có thể gây độc gan - ngừng nếu ALT >3x ULN'
        , 'drug_interactions': {'major': [{'drug': 'Insulin', 'mechanism':
        'Cả hai đều tăng giữ nước, tác dụng cộng dồn.', 'effect':
        'Tăng nguy cơ suy tim, phù, giữ nước nghiêm trọng', 'management':
        'Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu suy tim, phù. Có thể cần giảm liều insulin.'
        }], 'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Pioglitazone có thể tăng nồng độ digoxin.', 'effect':
        'Tăng nồng độ digoxin, tăng nguy cơ độc tính', 'management':
        'Theo dõi nồng độ digoxin và điều chỉnh liều nếu cần.'}, {'drug':
        'Gemfibrozil', 'mechanism':
        'Gemfibrozil ức chế CYP2C8, làm giảm chuyển hóa pioglitazone.',
        'effect': 'Tăng nồng độ pioglitazone, tăng nguy cơ tác dụng phụ',
        'management': 'Thận trọng. Có thể cần giảm liều pioglitazone.'}],
        'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Đái tháo đường type 1 - không hiệu quả (cần insulin)',
        'Suy tim (NYHA class III-IV) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ suy tim)',
        'Bệnh gan nặng - chống chỉ định (nguy cơ độc gan)',
        'Ung thư bàng quang - chống chỉ định (tăng nguy cơ)'], 'tương_đối': [
        'Suy tim (NYHA class I-II) - thận trọng, theo dõi sát',
        'Gãy xương (phụ nữ có nguy cơ tăng) - thận trọng',
        'Có thai - category C, thận trọng', 'Suy thận nặng - thận trọng',
        'Đang dùng insulin - tăng nguy cơ suy tim']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Pioglitazone là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt đầu. Có thể gây giữ nước, phù ở mẹ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không biết pioglitazone có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Theo dõi chức năng gan.', 'moderate':
        'Thận trọng, theo dõi chức năng gan chặt chẽ. Ngừng nếu ALT >3x ULN.',
        'severe':
        'Chống chỉ định. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc gan.',
        'notes':
        'Pioglitazone chuyển hóa ở gan qua CYP2C8 và CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc gan. Ngừng nếu ALT >3x ULN hoặc có dấu hiệu độc gan.'
        }, 'overdose_management': {'symptoms': ['Suy tim, phù nặng, giữ nước',
        'Hạ đường huyết (nếu dùng với insulin/sulfonylurea)',
        'Độc gan (vàng da, tăng ALT/AST)', 'Thiếu máu nặng'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng pioglitazone ngay lập tức',
        'Nếu suy tim: điều trị suy tim (diuretics, ACE inhibitors), theo dõi chặt chẽ'
        ,
        'Nếu hạ đường huyết: glucose đường uống hoặc IV, theo dõi đường huyết',
        'Nếu độc gan: điều trị hỗ trợ gan, theo dõi ALT/AST',
        'Nếu thiếu máu: điều trị hỗ trợ, có thể cần truyền máu',
        'Theo dõi dấu hiệu sinh tồn, chức năng gan, chức năng tim'],
        'monitoring':
        'Dấu hiệu suy tim, phù, đường huyết, chức năng gan, công thức máu, dấu hiệu sinh tồn'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Không ảnh hưởng hấp thu.',
        'timing': 'Uống 1 lần/ngày, bất kỳ lúc nào, cùng thời điểm mỗi ngày.'},
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Pioglitazone (Actos)',
        'UpToDate - Pioglitazone: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ], 'last_updated': '2025-02-04', 'evidence_level':
        'A - Dựa trên FDA drug labels và dữ liệu lâm sàng'}}}

__all__ = ['THIAZOLIDINEDIONE_TZDS_DRUGS']
