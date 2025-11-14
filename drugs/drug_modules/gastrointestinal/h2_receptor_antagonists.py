"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# H2 Receptor Antagonists

H2_RECEPTOR_ANTAGONISTS_DRUGS = {
    "Ranitidine": {'group': 'Gastrointestinal - H2 Receptor Antagonist', 'vietnamese_name':
        'Ranitidine, Zantac', 'administration': ['PO', 'IV'], 'indications': [
        'Loét dạ dày tá tràng', 'GERD', 'Phòng ngừa loét do stress'],
        'contraindications': ['Dị ứng'], 'dosage': {'adult_po':
        '150mg x 2 lần/ngày hoặc 300mg x 1 lần/ngày', 'adult_iv':
        '50mg x 3 lần/ngày hoặc 150mg truyền liên tục/24h', 'notes':
        'Yếu hơn PPI, nhưng rẻ hơn. Một số sản phẩm đã bị thu hồi do NDMA'},
        'side_effects': ['Nhức đầu', 'Rối loạn tiêu hóa', 'Tăng men gan (hiếm)'
        ], 'interactions': [
        'Warfarin: có thể tăng tác dụng (ít hơn cimetidine)'], 'pregnancy': 'B',
        'mechanism_of_action':
        'H2 (histamine-2) receptor antagonist. Ức chế histamine tại H2 receptors ở tế bào thành dạ dày, giảm tiết acid dạ dày (giảm acid kích thích và một phần acid cơ bản). Yếu hơn PPI (proton pump inhibitor) nhưng rẻ hơn. Tác dụng ngắn hơn PPI (cần dùng 2 lần/ngày). Ức chế nhẹ một số enzyme CYP450 (ít hơn cimetidine).'
        , 'monitoring': ['Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)',
        'Chức năng gan (transaminase) - có thể tăng men gan (hiếm)',
        'Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ nhẹ'
        , 'INR nếu dùng với warfarin (tăng nguy cơ chảy máu nhẹ)'],
        'precautions': ['Uống với thức ăn hoặc trước bữa ăn (tăng hiệu quả)',
        'Yếu hơn PPI - cân nhắc dùng PPI nếu không đáp ứng',
        'Thận trọng ở suy thận (giảm liều)', 'Thận trọng ở suy gan (giảm liều)',
        'Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)'
        ,
        'Một số sản phẩm đã bị thu hồi do NDMA (chất gây ung thư) - kiểm tra nguồn gốc sản phẩm'
        ,
        'Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts) - cách 2 giờ'
        ], 'pharmacokinetics': {'half_life': '2-3 giờ', 'onset': '1-3 giờ',
        'duration': '8-12 giờ', 'protein_binding': '15%', 'metabolism':
        'Gan (chuyển hóa qua CYP450, một phần), thận (thải trừ)', 'clearance':
        'Gan (chuyển hóa), thận (30-50% thải nguyên dạng)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Kiểm tra nguồn gốc sản phẩm (một số sản phẩm đã bị thu hồi do NDMA).'
        , 'black_box_warnings':
        'Một số sản phẩm ranitidine đã bị thu hồi do chứa NDMA (N-nitrosodimethylamine) - chất gây ung thư. NDMA có thể tích lũy trong sản phẩm theo thời gian, đặc biệt ở nhiệt độ cao. Kiểm tra nguồn gốc sản phẩm và cân nhắc dùng thuốc khác (PPI, famotidine) nếu có thể.'
        , 'drug_interactions': {'major': [], 'moderate': [{'drug': 'Warfarin',
        'mechanism': 'Ranitidine ức chế CYP450 nhẹ (ít hơn cimetidine)',
        'effect': 'Có thể tăng INR nhẹ, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên. Ranitidine ít ảnh hưởng hơn cimetidine.'},
        {'drug': 'Ketoconazole, Itraconazole', 'mechanism':
        'H2 blocker giảm acid dạ dày, giảm hấp thu azole antifungals', 'effect':
        'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ.'}, {'drug': 'Iron salts', 'mechanism':
        'H2 blocker giảm acid dạ dày, giảm hấp thu sắt', 'effect':
        'Giảm hấp thu sắt', 'management': 'Cách thời gian ít nhất 2 giờ.'}],
        'minor': [{'drug': 'Phenytoin, Theophylline', 'mechanism':
        'Ức chế CYP450 nhẹ', 'effect': 'Có thể tăng nồng độ nhẹ', 'management':
        'Thận trọng, theo dõi nồng độ nếu cần'}]}, 'contraindications': {
        'tuyệt_đối': ['Dị ứng ranitidine hoặc H2 blocker khác',
        'Một số sản phẩm ranitidine đã bị thu hồi do NDMA - tránh dùng các sản phẩm bị thu hồi'
        ], 'tương_đối': ['Suy thận nặng (CrCl <30) - giảm liều 50%',
        'Suy gan nặng (Child-Pugh C) - giảm liều 50%',
        'Người già - thận trọng, giảm liều nếu cần',
        'Nhiễm C. difficile - tăng nguy cơ nhẹ']}, 'pregnancy_lactation': {
        'fda_category': 'B', 'pregnancy_details':
        'Ranitidine là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu trên người không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Tuy nhiên, một số nghiên cứu gần đây gợi ý có thể có nguy cơ nhẹ, nên cân nhắc dùng PPI (pantoprazole, esomeprazole) nếu có thể.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ranitidine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.',
        'recommendation': 'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}
        }, 'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Giảm liều 50%', 'severe':
        'Giảm liều 50% (Child-Pugh C). Ranitidine chuyển hóa ở gan một phần, thải trừ qua thận. Suy gan nặng làm giảm chuyển hóa.'
        , 'notes':
        'Giảm liều ở suy gan trung bình và nặng. Thận trọng theo dõi.'},
        'overdose_management': {'symptoms': [
        'H2 blocker ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, chóng mặt',
        'Liều rất cao có thể gây: lú lẫn, co giật (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': ['Hỗ trợ triệu chứng',
        'Theo dõi dấu hiệu sinh tồn',
        'Nếu uống trong vòng 1-2 giờ: có thể cân nhắc activated charcoal',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, triệu chứng thần kinh'}, 'reversal_agents':
        None, 'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc trước bữa ăn (tăng hiệu quả)', 'timing':
        'Uống 2 lần/ngày (sáng và tối) hoặc 1 lần/ngày vào buổi tối. Có thể uống với hoặc không với thức ăn.'
        }, 'iv': {'reconstitution':
        'Ranitidine IV: 50mg pha với 20-50ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate':
        'Truyền trong 15-20 phút (bolus) hoặc 50mg truyền liên tục trong 24 giờ',
        'compatibility': ['NaCl 0.9%', 'Dextrose 5%'], 'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'}},
        'references': {'primary_sources': [
        'FDA Drug Label - Ranitidine (Note: Many products recalled due to NDMA)',
        'UpToDate - H2-receptor antagonists: Pharmacology and clinical use',
        'Micromedex - Ranitidine',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs (Note: Many products recalled due to NDMA contamination)'
        }}}

__all__ = ['H2_RECEPTOR_ANTAGONISTS_DRUGS']
