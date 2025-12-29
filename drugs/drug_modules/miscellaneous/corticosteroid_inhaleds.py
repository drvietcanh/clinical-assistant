"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Corticosteroid (Inhaled)s

CORTICOSTEROID_INHALED_DRUGS = {
    "Budesonide": {'group': 'Respiratory - Corticosteroid (Inhaled)', 'vietnamese_name':
        'Budesonide inhaled, Pulmicort', 'administration': ['INH', 'NEB'],
        'indications': ['Hen phế quản (duy trì)', 'COPD', 'Viêm mũi dị ứng',
        'Hen phế quản (Trẻ em)'], 'contraindications': ['Dị ứng budesonide',
        'Nhiễm trùng đường hô hấp không điều trị'], 'dosage': {'adult_inh':
        '200-800mcg x 2 lần/ngày', 'adult_neb':
        '0.5-1mg nebulizer x 2 lần/ngày', 'pediatric_inh':
        '100-400mcg x 2 lần/ngày (theo tuổi)', 'pediatric_neb':
        '0.25-0.5mg nebulizer x 2 lần/ngày', 'notes':
        'Súc miệng sau khi dùng để tránh nấm miệng. Có dạng nebulizer cho trẻ em'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': [
        'Nấm miệng (candida - phổ biến nếu không súc miệng)', 'Khàn tiếng',
        'Ho', 'Kích ứng họng', 'Tác dụng toàn thân (hiếm với liều thường)'],
        'interactions': ['Ketoconazole/Itraconazole: tăng nồng độ budesonide',
        'Ritonavir: tăng nồng độ budesonide'], 'pregnancy': 'C - An toàn',
        'mechanism_of_action':
        'Budesonide là corticosteroid hít (inhaled corticosteroid, ICS) có tác dụng kháng viêm mạnh tại chỗ. Budesonide gắn vào glucocorticoid receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào glucocorticoid response elements (GRE) trên DNA, kích hoạt hoặc ức chế biểu hiện gen. Dẫn đến: ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, IL-4, IL-5, TNF-α), giảm phóng thích các chất trung gian gây viêm từ mast cells và eosinophils, giảm thâm nhập tế bào viêm, giảm phù nề niêm mạc phế quản, và tăng số lượng beta-2 receptors. Budesonide có tác dụng chủ yếu tại chỗ (phế quản), ít hấp thu toàn thân nên ít tác dụng phụ toàn thân. Tuy nhiên, một phần nhỏ vẫn được hấp thu và có thể gây tác dụng toàn thân ở liều cao. Budesonide được chuyển hóa nhanh ở gan (first-pass metabolism cao) nên tác dụng toàn thân ít hơn so với corticosteroid uống.'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm triệu chứng hen, tần suất cơn cấp, nhu cầu dùng SABA)'
        ,
        'Nấm miệng (candidiasis) - kiểm tra lưỡi, miệng, đặc biệt nếu không súc miệng sau khi dùng'
        , 'Khàn tiếng, ho, kích ứng họng - tác dụng phụ tại chỗ phổ biến',
        'Tác dụng toàn thân (chỉ ở liều cao): ức chế trục HPA, chậm phát triển ở trẻ em, loãng xương, tăng huyết áp'
        , 'Chức năng gan nếu có triệu chứng (hiếm)',
        'Tương tác với ritonavir, ketoconazole, itraconazole (tăng nồng độ budesonide)'
        ], 'precautions': [
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG'
        ,
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, budesonide là thuốc duy trì'
        ,
        'Tác dụng phát huy sau vài ngày đến vài tuần - không mong đợi tác dụng tức thì'
        , 'Không ngừng đột ngột - giảm liều dần dần',
        'Tác dụng toàn thân hiếm với liều thường nhưng có thể xảy ra ở liều cao (>1600mcg/ngày)'
        ,
        'Thận trọng với bệnh nhân lao phổi, nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước'
        ,
        'Tránh dùng với ritonavir (tăng đáng kể nồng độ budesonide, tăng nguy cơ ức chế HPA)'
        , 'Thận trọng với ketoconazole, itraconazole (tăng nồng độ budesonide)',
        'Theo dõi chậm phát triển ở trẻ em nếu dùng liều cao',
        'Có thể dùng cho trẻ em (có dạng nebulizer)',
        'Dùng đều đặn hàng ngày, không phải khi cần'], 'pharmacokinetics': {
        'half_life': '2-3 giờ (trong phổi), 4-6 giờ (toàn thân sau hấp thu)',
        'onset': 'Vài giờ đến vài ngày (tác dụng kháng viêm)', 'duration':
        '12-24 giờ (dùng 2 lần/ngày)', 'protein_binding': '88-90%', 'clearance':
        'Gan: chuyển hóa nhanh qua CYP3A4 (first-pass metabolism cao, ~85-90% bị chuyển hóa). Thận: bài tiết một phần metabolites. Hấp thu toàn thân ít do chuyển hóa nhanh ở gan. Phần lớn tác dụng tại chỗ (phế quản).'
        }, 'storage':
        'Dạng hít (MDI/DPI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Không đông lạnh. Nebulizer suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 2 giờ sau khi mở gói. Bảo quản trong tủ lạnh nếu không dùng ngay (2-8°C), để nhiệt độ phòng trước khi dùng.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Ritonavir (HIV protease inhibitor)', 'mechanism':
        'Ritonavir ức chế CYP3A4 mạnh, làm giảm chuyển hóa budesonide, tăng nồng độ budesonide đáng kể.'
        , 'effect':
        'Tăng nồng độ budesonide đáng kể, tăng nguy cơ ức chế trục HPA, tác dụng phụ toàn thân (Cushing, tăng đường huyết, ức chế miễn dịch)'
        , 'management':
        'TRÁNH DÙNG cùng. Nếu bắt buộc, giảm liều budesonide đáng kể hoặc dùng corticosteroid hít khác (fluticasone ít bị ảnh hưởng hơn). Theo dõi dấu hiệu ức chế HPA.'
        }], 'moderate': [{'drug':
        'Ketoconazole, Itraconazole, Voriconazole (Azole antifungals)',
        'mechanism':
        'Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa budesonide.',
        'effect':
        'Tăng nồng độ budesonide, tăng nguy cơ tác dụng phụ toàn thân',
        'management':
        'Thận trọng. Có thể cần giảm liều budesonide. Theo dõi dấu hiệu ức chế HPA.'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng budesonide',
        'Nhiễm trùng đường hô hấp không điều trị (lao phổi, nhiễm nấm) - corticosteroid có thể làm nặng nhiễm trùng'
        ], 'tương_đối': ['Lao phổi - cần điều trị lao trước, thận trọng',
        'Nhiễm nấm đường hô hấp - cần điều trị trước',
        'Có thai - category C, thận trọng',
        'Đang dùng ritonavir - tăng nguy cơ ức chế HPA']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Budesonide là category C. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Corticosteroid hít có ít tác dụng toàn thân hơn corticosteroid uống, nhưng vẫn có thể ảnh hưởng đến thai nhi ở liều cao. Dùng liều thấp nhất hiệu quả.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Budesonide bài tiết vào sữa mẹ ở nồng độ rất thấp do chuyển hóa nhanh ở gan. An toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả.'}},
        'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Budesonide chuyển hóa ở gan nhưng suy gan nhẹ không ảnh hưởng đáng kể.'
        , 'moderate':
        'Thận trọng, có thể tăng nồng độ nhẹ. Theo dõi dấu hiệu tác dụng phụ toàn thân.'
        , 'severe':
        'Thận trọng, có thể tăng nồng độ. Giảm liều nếu có dấu hiệu tác dụng phụ toàn thân.'
        , 'notes':
        'Budesonide chuyển hóa nhanh ở gan qua CYP3A4 (first-pass metabolism cao). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ toàn thân.'
        }, 'overdose_management': {'symptoms': [
        'Tác dụng toàn thân: ức chế trục HPA, Cushing, tăng đường huyết, tăng huyết áp'
        , 'Nấm miệng nặng (nếu không súc miệng)', 'Khàn tiếng, ho nặng',
        'Ức chế miễn dịch (tăng nguy cơ nhiễm trùng)'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng budesonide hoặc giảm liều đáng kể',
        'Nếu ức chế HPA: điều trị hỗ trợ, có thể cần corticosteroid thay thế tạm thời'
        , 'Nếu nấm miệng: điều trị nấm (nystatin, fluconazole)',
        'Theo dõi đường huyết, huyết áp, dấu hiệu nhiễm trùng',
        'Theo dõi chức năng thượng thận nếu có dấu hiệu ức chế HPA'],
        'monitoring':
        'Đường huyết, huyết áp, dấu hiệu ức chế HPA, dấu hiệu nhiễm trùng, nấm miệng'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay hoặc giảm liều đáng kể. Có thể cần bổ sung corticosteroid nếu có suy thượng thận.'},
        'administration_instructions': {'oral': {'with_food': 'N/A - dạng hít',
        'timing': 'N/A - dạng hít'}, 'iv': {'reconstitution':
        'N/A - chỉ có dạng hít', 'infusion_rate': 'N/A', 'compatibility': [],
        'incompatibility': [], 'notes':
        'Chỉ có dạng hít (MDI/DPI) và nebulizer'}, 'inhaled': {'technique':
        'MDI: Lắc kỹ, thở ra hoàn toàn, đặt ống ngậm vào miệng, bấm và hít sâu chậm, giữ hơi 10 giây. DPI: Thở ra hoàn toàn, đặt ống ngậm vào miệng, hít mạnh và sâu, giữ hơi 10 giây.'
        , 'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng - QUAN TRỌNG',
        'frequency': '2 lần/ngày (sáng và tối), cách đều'}, 'nebulizer': {
        'preparation':
        'Lắc kỹ suspension trước khi dùng. Đổ vào buồng nebulizer. Dùng trong vòng 2 giờ sau khi mở gói.'
        , 'administration':
        'Thở bình thường qua ống ngậm hoặc mặt nạ cho đến khi hết thuốc (thường 5-15 phút).'
        , 'after_use':
        'Súc miệng và súc họng sau khi dùng. Rửa sạch thiết bị nebulizer.'}},
        'references': {'primary_sources': [
        'FDA Drug Label - Budesonide (Pulmicort)',
        'UpToDate - Budesonide: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ], 'last_updated': '2025-02-04', 'evidence_level':
        'A - Dựa trên FDA drug labels và dữ liệu lâm sàng'}}}

__all__ = ['CORTICOSTEROID_INHALED_DRUGS']
