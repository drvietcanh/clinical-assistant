"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Antiemetic (5-HT3 Antagonist)s

ANTIEMETIC_5_HT3_ANTAGONISTS_DRUGS = {
    "Ondansetron": {'group': 'Gastrointestinal - Antiemetic (5-HT3 Antagonist)',
        'vietnamese_name': 'Ondansetron, Zofran', 'administration': ['PO', 'IV',
        'IM'], 'indications': ['Buồn nôn, nôn sau hóa trị',
        'Buồn nôn, nôn sau phẫu thuật', 'Buồn nôn, nôn do xạ trị',
        'Buồn nôn, nôn do nhiều nguyên nhân'], 'contraindications': [
        'Dị ứng ondansetron', 'QT kéo dài', 'Dùng với apomorphine'], 'dosage':
        {'adult_po': '8mg x 2-3 lần/ngày', 'adult_iv_im':
        '4-8mg x 2-3 lần/ngày', 'adult_chemotherapy':
        '8mg IV trước hóa trị, sau đó 8mg PO x 2 lần/ngày x 3 ngày',
        'adult_surgery': '4mg IV trước khi gây mê', 'notes':
        'Rất hiệu quả cho buồn nôn do hóa trị và phẫu thuật'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['QT kéo dài', 'Nhức đầu',
        'Chóng mặt', 'Táo bón', 'Mệt mỏi'], 'interactions': [
        'Apomorphine: chống chỉ định',
        'Thuốc QT kéo dài: tăng nguy cơ loạn nhịp',
        'CYP2D6 inhibitors: tăng nồng độ ondansetron'], 'pregnancy': 'B',
        'mechanism_of_action':
        '5-HT3 (serotonin) receptor antagonist. Ức chế chọn lọc receptor 5-HT3 ở ngoại vi (dây thần kinh phế vị) và trung ương (chemoreceptor trigger zone trong area postrema). Ngăn cản tác dụng của serotonin, dẫn đến giảm nôn và buồn nôn. Được dùng trong dự phòng và điều trị nôn do hóa trị, xạ trị, và sau phẫu thuật. Hiệu quả hơn metoclopramide và không gây tác dụng phụ ngoại tháp như metoclopramide.'
        , 'monitoring': ['Tần suất nôn và buồn nôn',
        'ECG (QT kéo dài - nguy cơ rối loạn nhịp tim, đặc biệt ở liều cao)',
        'Điện giải (kali, magie) - hạ kali, hạ magie tăng nguy cơ QT kéo dài',
        'Dấu hiệu tắc ruột (ondansetron có thể che dấu triệu chứng)',
        'Chức năng gan (ALT, AST) - hiếm tăng men gan'], 'precautions': [
        'QT kéo dài → không dùng ở bệnh nhân có QT kéo dài, rối loạn nhịp tim, hoặc dùng các thuốc kéo dài QT khác'
        ,
        'Nguy cơ tăng ở liều cao (> 16mg đơn liều), hạ kali, hạ magie, suy gan',
        'Có thể che dấu triệu chứng tắc ruột - thận trọng ở bệnh nhân có nguy cơ',
        'Giảm liều ở suy gan nặng (giảm chuyển hóa)',
        'Liều thường: 4-8mg (PO/IV), có thể lặp lại mỗi 8 giờ',
        'Liều tối đa: 32mg/ngày (để giảm nguy cơ QT kéo dài)',
        'Có thể dùng trước hóa trị/xạ trị để dự phòng',
        'An toàn trong thai kỳ (category B)'], 'pharmacokinetics': {'half_life':
        '3-6 giờ (bình thường), kéo dài ở suy gan', 'onset':
        '30 phút (PO), ngay lập tức (IV)', 'duration': '4-8 giờ',
        'protein_binding': '70-76%', 'metabolism':
        'Gan (CYP1A2, CYP2D6, CYP3A4) - chuyển hóa mạnh', 'clearance':
        'Chủ yếu qua gan, cần điều chỉnh ở suy gan'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Dung dịch tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.'
        , 'black_box_warnings':
        'Nguy cơ QT kéo dài, có thể gây rối loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Nguy cơ tăng ở liều cao, hạ kali, hạ magie, suy gan, hoặc dùng với các thuốc kéo dài QT khác. Không dùng vượt quá liều khuyến cáo.'
        , 'drug_interactions': {'major': [{'drug': 'Apomorphine', 'mechanism':
        'Ondansetron ức chế 5-HT3 receptor, đối kháng với apomorphine',
        'effect': 'Giảm hiệu quả apomorphine, có thể gây hạ huyết áp nặng',
        'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng ondansetron với apomorphine.'}],
        'moderate': [{'drug':
        'Thuốc kéo dài QT (amiodarone, quinolone, macrolide, haloperidol, etc.)',
        'mechanism': 'Tác dụng hiệp đồng kéo dài QT interval', 'effect':
        'Tăng nguy cơ QT kéo dài, torsades de pointes, loạn nhịp tim',
        'management':
        'Tránh dùng cùng hoặc thận trọng. Theo dõi ECG. Giảm liều ondansetron.'
        }, {'drug': 'CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)',
        'mechanism': 'Ức chế chuyển hóa ondansetron qua CYP2D6', 'effect':
        'Tăng nồng độ ondansetron, tăng nguy cơ QT kéo dài', 'management':
        'Thận trọng, giảm liều ondansetron nếu cần'}], 'minor': []},
        'contraindications': {'tuyệt_đối': ['Dị ứng ondansetron',
        'Dùng với apomorphine - CHỐNG CHỈ ĐỊNH tuyệt đối',
        'QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH'],
        'tương_đối': ['Suy gan nặng - giảm liều 50% (tối đa 8mg/ngày)',
        'Hạ kali, hạ magie - tăng nguy cơ QT kéo dài, bổ sung trước khi dùng',
        'Đang dùng thuốc kéo dài QT - thận trọng, giảm liều',
        'Người già - thận trọng, giảm liều', 'Rối loạn nhịp tim - thận trọng']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Ondansetron là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu trên người không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Thường dùng để điều trị buồn nôn, nôn trong thai kỳ (hyperemesis gravidarum).'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ondansetron bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.',
        'recommendation': 'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}
        }, 'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Giảm liều 50% (tối đa 8mg/ngày)', 'severe':
        'Giảm liều 50% (tối đa 8mg/ngày). Ondansetron chuyển hóa ở gan qua CYP1A2, CYP2D6, CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ QT kéo dài.'
        , 'notes':
        'Ondansetron chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ, tăng nguy cơ QT kéo dài. Giảm liều ở suy gan trung bình và nặng.'
        }, 'overdose_management': {'symptoms': [
        'QT kéo dài, torsades de pointes, loạn nhịp tim (triệu chứng chính, có thể tử vong)'
        , 'Nhức đầu, chóng mặt', 'Buồn nôn, nôn', 'Mệt mỏi'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Theo dõi ECG liên tục (QT interval)',
        'Điều trị torsades de pointes nếu có: magnesium sulfate 2g IV, pacing nếu cần'
        , 'Bổ sung kali, magie nếu thiếu', 'Hỗ trợ triệu chứng',
        'Theo dõi dấu hiệu sinh tồn chặt chẽ'], 'monitoring':
        'Theo dõi ECG liên tục (QT interval), dấu hiệu sinh tồn, điện giải'},
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food': 'Có thể uống với hoặc không với thức ăn', 'timing':
        'Uống 30 phút trước hóa trị/xạ trị/phẫu thuật (dự phòng) hoặc ngay khi có buồn nôn. Có thể lặp lại mỗi 8 giờ. Tối đa 32mg/ngày.'
        }, 'iv': {'reconstitution':
        'Ondansetron IV: 4-8mg pha với 50ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate': 'Truyền trong 15 phút', 'compatibility': ['NaCl 0.9%',
        'Dextrose 5%'], 'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'Có thể tiêm IV trực tiếp chậm (2-5 phút) hoặc truyền. Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'
        }}, 'references': {'primary_sources': ['FDA Drug Label - Ondansetron',
        'UpToDate - Ondansetron: Drug information', 'Micromedex - Ondansetron',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'FDA Safety Communication - Ondansetron QT prolongation (2012)'],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs, safety warnings (QT prolongation)'}         "reversal_agents": {
             "available": False,
             "agents": []
         },
}}

__all__ = ['ANTIEMETIC_5_HT3_ANTAGONISTS_DRUGS']
