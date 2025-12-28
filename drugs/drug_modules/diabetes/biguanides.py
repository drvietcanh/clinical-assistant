"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Biguanides

BIGUANIDES_DRUGS = {
    "Metformin": {'group': 'Diabetes - Biguanide', 'vietnamese_name':
        'Metformin, Glucophage', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2', 'Hội chứng buồng trứng đa nang (PCOS)',
        'Dự phòng đái tháo đường'], 'contraindications': [
        'Suy thận (CrCl <30 hoặc eGFR <30)', 'Toan chuyển hóa',
        'Nhiễm toan lactic', 'Suy gan nặng', 'Suy tim nặng',
        'Dùng thuốc cản quang (tạm ngừng)'], 'dosage': {'adult_start':
        '500mg x 2 lần/ngày với bữa ăn', 'adult_usual':
        '500-1000mg x 2-3 lần/ngày', 'adult_max':
        '1000mg x 2 lần/ngày (2000mg/ngày)', 'extended_release':
        '500-2000mg x 1 lần/ngày với bữa ăn tối', 'notes':
        'Khởi đầu với liều thấp, tăng dần. Tạm ngừng khi dùng thuốc cản quang'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, giảm liều', 'under_30': 'Chống chỉ định'}, 'side_effects':
        ['Buồn nôn, nôn', 'Tiêu chảy', 'Đau bụng',
        'Nhiễm toan lactic (hiếm nhưng nguy hiểm)', 'Hạ đường huyết (ít khi)',
        'Thiếu vitamin B12 (dùng lâu dài)'], 'interactions': [
        'Thuốc cản quang: tăng nguy cơ nhiễm toan lactic - ngừng 48h trước và sau',
        'Rượu: tăng nguy cơ nhiễm toan lactic',
        'Furosemide: có thể tăng nồng độ metformin'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Ức chế sản xuất glucose ở gan, tăng nhạy cảm với insulin ở mô ngoại vi, giảm hấp thu glucose ở ruột'
        , 'monitoring': ['HbA1c mỗi 3 tháng', 'Đường huyết đói và sau ăn',
        'Creatinine, eGFR mỗi 3-6 tháng', 'Vitamin B12 mỗi 1-2 năm',
        'Lactate nếu nghi ngờ nhiễm toan lactic (đau cơ, khó thở, đau bụng)'],
        'precautions': ['Ngừng 48h trước và sau khi dùng thuốc cản quang',
        'Theo dõi nhiễm toan lactic ở bệnh nhân suy tim, suy gan, suy thận',
        'Bổ sung vitamin B12 nếu dùng lâu dài',
        'Tránh rượu (tăng nguy cơ nhiễm toan lactic)'], 'pharmacokinetics': {
        'half_life': '6.2 giờ', 'onset': '1-2 giờ', 'duration': '10-12 giờ',
        'protein_binding': 'Minimal', 'clearance': 'Thận (chủ yếu)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Nhiễm toan lactic - có thể tử vong. Nguy cơ cao ở suy thận, suy tim, suy gan, nhiễm trùng nặng'
        , 'drug_interactions': {'major': [{'drug':
        'Thuốc cản quang (iodinated contrast media)', 'mechanism':
        'Tăng nguy cơ nhiễm toan lactic do suy thận cấp', 'effect':
        'Nguy cơ nhiễm toan lactic, suy thận cấp, tử vong', 'management':
        'NGỪNG METFORMIN 48 GIỜ TRƯỚC và 48 GIỜ SAU khi dùng thuốc cản quang. Đánh giá chức năng thận trước khi dùng lại.'
        }, {'drug': 'Rượu (ethanol)', 'mechanism':
        'Tăng sản xuất lactate, giảm chuyển hóa lactate', 'effect':
        'Tăng nguy cơ nhiễm toan lactic', 'management':
        'TRÁNH RƯỢU hoàn toàn khi dùng metformin. Cảnh báo bệnh nhân về nguy cơ.'
        }], 'moderate': [{'drug': 'Furosemide', 'mechanism':
        'Có thể tăng nồng độ metformin, tăng nguy cơ nhiễm toan lactic',
        'effect': 'Tăng nguy cơ nhiễm toan lactic', 'management':
        'Thận trọng. Theo dõi chức năng thận, lactate. Có thể cần giảm liều metformin.'
        }, {'drug': 'Cimetidine', 'mechanism':
        'Giảm thải trừ metformin qua thận', 'effect':
        'Tăng nồng độ metformin, tăng nguy cơ độc tính', 'management':
        'Thận trọng. Theo dõi lactate. Có thể cần giảm liều metformin.'}],
        'minor': [{'drug': 'Warfarin', 'mechanism':
        'Metformin có thể tăng nhẹ tác dụng chống đông', 'effect':
        'Tăng nhẹ INR', 'management':
        'Theo dõi INR. Điều chỉnh liều warfarin nếu cần.'}]},
        'contraindications': {'tuyệt_đối': [
        'Suy thận nặng (CrCl <30 hoặc eGFR <30)', 'Nhiễm toan lactic',
        'Suy gan nặng', 'Suy tim nặng (NYHA class III-IV)',
        'Dùng thuốc cản quang (tạm ngừng 48h trước và sau)',
        'Nhiễm trùng nặng (tăng nguy cơ nhiễm toan lactic)', 'Dị ứng metformin'
        ], 'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát',
        'Suy gan nhẹ đến trung bình - thận trọng',
        'Suy tim nhẹ đến trung bình - thận trọng',
        'Người cao tuổi - tăng nguy cơ nhiễm toan lactic',
        'Uống rượu - tăng nguy cơ nhiễm toan lactic',
        'Phẫu thuật lớn - tạm ngừng trước và sau phẫu thuật']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Không có bằng chứng về nguy cơ gây dị tật thai nhi ở động vật. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Được sử dụng rộng rãi trong thai kỳ, đặc biệt ở bệnh nhân đái tháo đường thai kỳ và PCOS. Theo dõi đường huyết chặt chẽ trong thai kỳ. Có thể dùng với insulin.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Metformin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. An toàn và được khuyến nghị trong thời kỳ cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường.'
        }}, 'hepatic_adjustment': {'mild': 'Thận trọng', 'moderate':
        'Thận trọng, có thể cần giảm liều', 'severe': 'CHỐNG CHỈ ĐỊNH', 'notes':
        'Metformin chuyển hóa một phần ở gan. Suy gan làm giảm chuyển hóa lactate, tăng nguy cơ nhiễm toan lactic. Không dùng ở suy gan nặng. Thận trọng ở suy gan nhẹ đến trung bình.'
        }, 'overdose_management': {'symptoms': ['Buồn nôn, nôn, tiêu chảy',
        'Đau bụng',
        'Nhiễm toan lactic (pH <7.35, lactate >5 mmol/L) - nguy hiểm',
        'Hạ đường huyết (hiếm)', 'Suy thận cấp',
        'Hôn mê, tử vong (nếu nhiễm toan lactic nặng)'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và lọc máu', 'treatment':
        ['Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính (hiệu quả hạn chế)',
        'Điều trị nhiễm toan lactic: Bicarbonate IV, lọc máu (hemodialysis) để loại bỏ metformin'
        , 'Hỗ trợ hô hấp và tuần hoàn',
        'Theo dõi lactate, pH máu, điện giải, chức năng thận',
        'Lọc máu nếu lactate >5 mmol/L hoặc nhiễm toan lactic nặng',
        'Điều trị hạ đường huyết nếu có: Glucose IV',
        'Theo dõi ít nhất 24-48 giờ'], 'monitoring':
        'Lactate máu, pH máu, điện giải, chức năng thận, glucose máu, dấu hiệu sống, ý thức'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị nhiễm toan lactic nếu có (bicarbonate IV, lọc máu nếu cần). Điều trị hạ đường huyết nếu có.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với bữa ăn để giảm buồn nôn, tiêu chảy. Có thể giảm tác dụng phụ đường tiêu hóa.'
        , 'timing':
        'Uống 2-3 lần/ngày với bữa ăn. Dạng extended-release: 1 lần/ngày với bữa ăn tối. Khởi đầu với liều thấp (500mg x 2 lần/ngày), tăng dần để giảm tác dụng phụ.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'pediatric_dosing': {
        'neonates': 'Không khuyến cáo cho trẻ <10 tuổi',
        'infants': 'Không khuyến cáo cho trẻ <10 tuổi',
        'children': '10-17 tuổi: 500mg x 2 lần/ngày với bữa ăn, tăng dần đến 2000mg/ngày. Chỉ dùng cho đái tháo đường type 2. Theo dõi chức năng thận',
        'adolescents': '500mg x 2 lần/ngày với bữa ăn, tăng dần đến 1000mg x 2 lần/ngày (2000mg/ngày). Liều người lớn',
        'notes': 'Dùng cho đái tháo đường type 2 ở trẻ em ≥10 tuổi. Khởi đầu với liều thấp, tăng dần. Uống với bữa ăn. Theo dõi chức năng thận, đường huyết, vitamin B12'
    }, 'geriatric_dosing': {
        'considerations': 'Người cao tuổi có nguy cơ cao nhiễm toan lactic. Suy thận phổ biến hơn. Chức năng thận có thể giảm nhanh',
        'dose_adjustment': 'Khởi đầu với liều thấp hơn (250-500mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo CrCl. Theo dõi chức năng thận thường xuyên hơn (mỗi 3 tháng)',
        'monitoring': 'Theo dõi chức năng thận (creatinine, eGFR) thường xuyên hơn (mỗi 3 tháng). Theo dõi lactate nếu có triệu chứng. Theo dõi vitamin B12. Cảnh báo về nhiễm toan lactic'
    }, 'brand_names': {
        'vietnam': ['Glucophage', 'Metformin Stada', 'Metformin', 'Diaformin', 'Metforal'],
        'common': ['Glucophage', 'Metformin', 'Fortamet', 'Riomet']
    }, 'cost_estimate': {
        'unit': 'VND',
        'range': '2,000 - 10,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note': 'Giá thay đổi theo thương hiệu và nhà thuốc. Metformin generic thường rẻ hơn (2,000-5,000 VND/viên 500mg).'
    },         'references': {'primary_sources': [
        'FDA Drug Label - Glucophage (metformin)',
        'UpToDate - Metformin: Drug information',
        'UK Prospective Diabetes Study (UKPDS)',
        'American Diabetes Association guidelines',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - Multiple large RCTs (UKPDS) and extensive clinical experience'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Lactic acidosis (rare but serious)', 'Renal toxicity (contraindicated if CrCl <30)'],
            'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': True,
            'requires_monitoring': ['Renal function (CrCl, eGFR)', 'Lactate levels if symptoms', 'Vitamin B12 (long-term use)']
        },
        'guideline_tags': [
            'ADA Diabetes Guidelines',
            'AACE/ACE Diabetes Guidelines',
            'EASD Guidelines',
            'UKPDS Study',
            'FDA Drug Safety Communication - Metformin and Contrast Media'
        ]}}

__all__ = ['BIGUANIDES_DRUGS']
