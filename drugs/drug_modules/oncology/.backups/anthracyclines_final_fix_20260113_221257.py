"""Oncology Medications
Active module - contains all oncology drug data"""

# Anthracyclines

ANTHRACYCLINES_DRUGS = {
    "Doxorubicin": {'group': 'Oncology - Anthracycline',
        'vietnamese_name':
        'Doxorubicin, Adriamycin', 'administration': ['IV'],
        'indications': [
        'Ung thư vú', 'U lympho', 'Bệnh bạch cầu', 'Sarcoma mô mềm',
        'Ung thư buồng trứng', 'Ung thư phổi (SCLC)'],
        'contraindications': [
        'Dị ứng doxorubicin', 'Suy tim nặng', 'Bệnh tim tiềm ẩn',
        'Giảm bạch cầu/tiểu cầu nặng', 'Có thai', 'Đang cho con bú'],
        'dosage':
        {'adult_standard': '60-75mg/m² IV mỗi 3 tuần', 'adult_weekly':
        '20-30mg/m² IV mỗi tuần', 'adult_cardiac_risk':
        'Giảm liều hoặc dùng liposomal doxorubicin', 'notes':
        'Tổng liều tích lũy tối đa: 450-550mg/m² (nguy cơ độc tim). Dùng phác đồ 3 tuần'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, có thể giảm liều', 'under_30': 'Thận trọng, giảm liều'},
        'side_effects': [
        'Độc tim (suy tim, rối loạn nhịp - tích lũy, không hồi phục)',
        'Giảm bạch cầu, tiểu cầu (myelosuppression)', 'Rụng tóc (phổ biến)',
        'Buồn nôn, nôn', 'Loét miệng',
        'Da đỏ, đau khi truyền (extravasation - nguy hiểm)',
        'Nước tiểu đỏ (bình thường, không phải máu)', 'Vô sinh'],
        'interactions': ['Cyclophosphamide: tăng độc tim',
        'Trastuzumab: tăng độc tim', 'Paclitaxel: có thể tăng độc tính',
        'Các anthracyclines khác: tăng độc tim'],pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Doxorubicin là anthracycline, gắn vào DNA và ức chế enzyme topoisomerase II, ngăn cản quá trình sửa chữa DNA và gây đứt gãy DNA. Thuốc tạo ra các gốc tự do (free radicals) gây stress oxy hóa, tổn thương màng tế bào và DNA. Doxorubicin tích lũy trong ty thể, gây tổn thương ty thể và dẫn đến độc tim (cardiotoxicity). Thuốc tác động chủ yếu lên tế bào đang phân chia nhanh, gây độc tế bào và chết tế bào ung thư. Độc tim là do tích lũy liều (dose-dependent) và có thể không hồi phục'
        , 'monitoring': [
        'Chức năng tim trước mỗi chu kỳ (echo, MUGA scan - đo EF)',
        'Điện tâm đồ (ECG) trước và trong điều trị',
        'Tổng liều tích lũy (tối đa 450-550mg/m² để tránh độc tim)',
        'Công thức máu toàn phần (CBC) trước mỗi chu kỳ',
        'Chức năng gan (ALT, AST, bilirubin) trước mỗi chu kỳ',
        'Dấu hiệu suy tim (khó thở, phù, mệt mỏi) - có thể xảy ra muộn',
        'Theo dõi extravasation khi truyền (da đỏ, đau - nguy hiểm)',
        'Nước tiểu đỏ (bình thường, không phải máu)'],
        'precautions': [
        'Theo dõi chặt chẽ tổng liều tích lũy (tối đa 450-550mg/m²)',
        'Đo EF trước mỗi chu kỳ nếu có nguy cơ độc tim cao',
        'Ngừng nếu EF giảm >10-15% hoặc có dấu hiệu suy tim',
        'Tránh extravasation khi truyền (có thể gây hoại tử da)',
        'Có thể dùng liposomal doxorubicin để giảm độc tim',
        'Tránh dùng với các thuốc khác gây độc tim (cyclophosphamide, trastuzumab)'
        , 'Độc tim có thể xảy ra muộn (sau nhiều năm) - cần theo dõi lâu dài',
        'Có thể gây vô sinh (cần tư vấn trước điều trị)'],
        'pharmacokinetics':
        {'half_life': '20-48 giờ (dài)', 'onset':
        '1-2 tuần (tác dụng lâm sàng)', 'duration':
        'Kéo dài (tích lũy trong mô)', 'protein_binding': '>90%', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ - chậm)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Bảo vệ khỏi ánh sáng'
        , 'black_box_warnings':
        'Có thể gây độc tim nặng và suy tim không hồi phục. Tổng liều tích lũy tối đa: 450-550mg/m². Theo dõi chức năng tim trước mỗi chu kỳ. Độc tim có thể xảy ra muộn (sau nhiều năm)'
        , 'drug_interactions': {'major': [{'drug': 'Cyclophosphamide',
        'mechanism':
        'Cả hai đều gây độc tim, tác dụng cộng dồn làm tăng nguy cơ suy tim nghiêm trọng.'
        , 'effect': 'Tăng nguy cơ độc tim, suy tim không hồi phục',
        'management':
        'Thận trọng khi dùng đồng thời. Giảm tổng liều tích lũy của cả hai thuốc. Theo dõi chức năng tim chặt chẽ.'
        }, {'drug': 'Trastuzumab', 'mechanism':
        'Cả hai đều gây độc tim, tác dụng cộng dồn làm tăng nguy cơ suy tim nghiêm trọng.'
        , 'effect': 'Tăng nguy cơ độc tim, suy tim không hồi phục',
        'management':
        'Thận trọng khi dùng đồng thời. Theo dõi chức năng tim chặt chẽ. Có thể cần giảm liều hoặc tránh dùng đồng thời.'
        }],
        'moderate': [{'drug': 'Unknown', 'mechanism':
        'Có thể tăng độc tính của doxorubicin.', 'effect':
        'Tăng độc tính tổng thể', 'management':
        'Thận trọng khi dùng đồng thời. Theo dõi độc tính chặt chẽ.'}, {'drug':
        'Các anthracyclines khác (Daunorubicin, Epirubicin, Idarubicin)',
        'mechanism': 'Cả hai đều gây độc tim tích lũy, tác dụng cộng dồn.',
        'effect': 'Tăng nguy cơ độc tim, suy tim', 'management':
        'Tính tổng liều tích lũy của tất cả anthracyclines. Giảm tổng liều tích lũy tối đa.'
        }],
        'minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng doxorubicin', 'Suy tim nặng - chống chỉ định tuyệt đối',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'],tương_đối': [
        'Bệnh tim tiềm ẩn - thận trọng, theo dõi chức năng tim chặt chẽ',
        'Tổng liều tích lũy >450-550mg/m² - nguy cơ độc tim cao, nên ngừng',
        'Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục',
        'Suy gan - thận trọng, có thể cần giảm liều',
        'Suy thận - thận trọng, có thể cần giảm liều']},contraindications_detail': {
        'tuyệt_đối': [
        'Dị ứng doxorubicin', 'Suy tim nặng - chống chỉ định tuyệt đối',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'],tương_đối': [
        'Bệnh tim tiềm ẩn - thận trọng, theo dõi chức năng tim chặt chẽ',
        'Tổng liều tích lũy >450-550mg/m² - nguy cơ độc tim cao, nên ngừng',
        'Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục',
        'Suy gan - thận trọng, có thể cần giảm liều',
        'Suy thận - thận trọng, có thể cần giảm liều']},reversal_agents': {
        'available': False, 'agents': [],notes': 'Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Nếu có extravasation: ngừng truyền ngay, không rút kim, chườm lạnh, tham khảo phẫu thuật.'},pregnancy_lactation':
        {'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Doxorubicin gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Doxorubicin bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng doxorubicin. Ngừng cho con bú hoặc ngừng thuốc.'
        }},hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Thận trọng, giảm liều 50-75%', 'notes':
        'Doxorubicin chuyển hóa chủ yếu qua gan. Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ. Có thể cần giảm liều đáng kể ở suy gan.'
        },overdose_management': {'symptoms': [
        'Suy tim cấp (khó thở, phù, mệt mỏi)', 'Rối loạn nhịp tim',
        'Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)',
        'Loét miệng nặng', 'Nôn mửa nặng',
        'Extravasation (da đỏ, đau - nguy hiểm)'],antidote':
        'Không có antidote đặc hiệu', 'treatment': ['Ngừng ngay doxorubicin',
        'Nếu có extravasation: ngừng truyền ngay, không rút kim, chườm lạnh, tham khảo phẫu thuật'
        , 'Điều trị suy tim: furosemide, ACE inhibitor, beta-blocker nếu cần',
        'Theo dõi và điều trị rối loạn nhịp tim',
        'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng tim, chức năng gan',
        'Điều trị nôn mửa (ondansetron, granisetron)'],
        'monitoring':
        'Chức năng tim (echo, ECG), CBC, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu extravasation'
        },administration_instructions': {'oral': {
        'with_food': 'Không áp dụng', 'timing':
        'Không có dạng uống (chỉ có IV)'},iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất', 'infusion_rate':
        'Truyền trong 15-30 phút (bolus) hoặc 1-4 giờ (infusion)',
        'compatibility': ['NS', 'D5W'],incompatibility': [],notes':
        'Bolus: 60-75mg/m² truyền trong 15-30 phút. Infusion: có thể truyền trong 1-4 giờ để giảm độc tính. QUAN TRỌNG: Theo dõi extravasation chặt chẽ (có thể gây hoại tử da). Bảo vệ khỏi ánh sáng.'
        }},references': {'primary_sources': [
        'FDA Drug Label - Doxorubicin (Adriamycin)',
        'UpToDate - Doxorubicin Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],last_updated': '2025-01-15',        "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    }
}

__all__ = ['ANTHRACYCLINES_DRUGS']
