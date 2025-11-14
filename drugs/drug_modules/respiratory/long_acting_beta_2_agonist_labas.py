"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Long-acting Beta-2 Agonist (LABA)s

LONG_ACTING_BETA_2_AGONIST_LABAS_DRUGS = {
    "Salmeterol": {'group': 'Respiratory - Long-acting Beta-2 Agonist (LABA)',
        'vietnamese_name': 'Salmeterol, Serevent', 'administration': [
        'Inhalation'], 'indications': [
        'Hen phế quản (phòng ngừa, phải dùng với ICS)', 'COPD (phòng ngừa)',
        'Co thắt phế quản ban đêm', 'Dự phòng co thắt do vận động'],
        'contraindications': ['Dị ứng', 'Nhịp tim nhanh nặng',
        'Hen phế quản cấp (không dùng đơn độc)'], 'dosage': {'adult_inhalation':
        '50mcg x 2 lần/ngày (sáng và tối)', 'notes':
        'PHẢI dùng kết hợp với ICS. Không dùng đơn độc cho hen. Tác dụng kéo dài 12 giờ'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Tim đập nhanh', 'Run cơ',
        'Đau đầu', 'Co thắt phế quản nghịch lý (hiếm)', 'Loạn nhịp tim (hiếm)'],
        'interactions': ['Beta-blocker: đối kháng tác dụng',
        'Theophylline: tăng tác dụng phụ'], 'pregnancy': 'C',
        'mechanism_of_action':
        'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng dài (12 giờ) do liên kết chặt với receptor, giải phóng chậm. Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch. Giảm phóng thích chất trung gian gây viêm từ mast cells. Dùng để phòng ngừa, không dùng để cắt cơn (tác dụng chậm).'
        , 'monitoring': ['Nhịp tim, huyết áp (đặc biệt khi bắt đầu điều trị)',
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp',
        'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)',
        'Tần suất dùng SABA (nếu tăng → cần đánh giá lại điều trị)'],
        'precautions': [
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid) - không bao giờ dùng đơn độc cho hen phế quản'
        ,
        'Không dùng để cắt cơn (tác dụng chậm, không hiệu quả) - cần có SABA để cắt cơn'
        , 'Không dùng đơn độc cho hen phế quản cấp - nguy cơ tăng tử vong',
        'Tránh dùng với beta-blocker (đối kháng tác dụng)',
        'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)'
        , 'Dùng đều đặn 2 lần/ngày (sáng và tối) để phòng ngừa',
        'Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng',
        'Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị và tăng ICS',
        'Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị'],
        'pharmacokinetics': {'half_life': '5.5 giờ (dài hơn salbutamol)',
        'onset': '15-30 phút (chậm hơn SABA)', 'duration': '12 giờ (dài)',
        'protein_binding': '96%', 'clearance':
        'Gan (chuyển hóa qua CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen. Không dùng để cắt cơn hen cấp (tác dụng chậm). Chỉ dùng để phòng ngừa và phải luôn có SABA để cắt cơn.'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (không chọn lọc: Propranolol, Nadolol)', 'mechanism':
        'Đối kháng tác dụng beta-2, chặn tác dụng giãn phế quản của salmeterol',
        'effect':
        'Đối kháng tác dụng giãn phế quản, có thể gây co thắt phế quản nặng, suy hô hấp'
        , 'management':
        'TRÁNH DÙNG với beta-blocker không chọn lọc. Nếu bệnh nhân cần beta-blocker, dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng. Theo dõi chặt chẽ đáp ứng phế quản.'
        }], 'moderate': [{'drug': 'Theophylline', 'mechanism':
        'Cả hai đều kích thích beta-adrenergic, có thể tăng tác dụng phụ và độc tính'
        , 'effect':
        'Tăng tác dụng phụ (run, tim đập nhanh, loạn nhịp), tăng nguy cơ độc tính theophylline'
        , 'management':
        'Theo dõi nồng độ theophylline. Theo dõi nhịp tim và triệu chứng. Có thể cần giảm liều theophylline.'
        }, {'drug': 'Digoxin', 'mechanism':
        'Salmeterol có thể gây hạ kali máu và tăng nhịp tim, tăng nguy cơ độc tính digoxin'
        , 'effect':
        'Tăng nguy cơ loạn nhịp tim, tăng độc tính digoxin (đặc biệt khi hạ kali máu)'
        , 'management':
        'Theo dõi nồng độ digoxin và kali máu. Theo dõi ECG nếu có triệu chứng. Có thể cần điều chỉnh liều digoxin.'
        }, {'drug': 'Diuretics (Furosemide, Thiazide)', 'mechanism':
        'Cả hai đều có thể gây hạ kali máu, tăng nguy cơ hạ kali máu nghiêm trọng',
        'effect':
        'Tăng nguy cơ hạ kali máu nghiêm trọng, loạn nhịp tim, yếu cơ',
        'management':
        'Theo dõi kali máu thường xuyên. Bổ sung kali nếu cần. Có thể cần điều chỉnh liều diuretic.'
        }], 'minor': [{'drug': 'Tricyclic Antidepressants (TCA)', 'mechanism':
        'TCA tăng nhạy cảm với catecholamine, có thể tăng tác dụng tim mạch',
        'effect': 'Tăng nhịp tim, tăng huyết áp (nhẹ)', 'management':
        'Theo dõi nhịp tim và huyết áp. Không cần điều chỉnh liều thường quy.'}
        ]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng với salmeterol hoặc các thành phần khác',
        'Nhịp tim nhanh nặng không kiểm soát (>120 bpm)',
        'Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)',
        'Hen phế quản cấp (không dùng đơn độc, không dùng để cắt cơn)'],
        'tương_đối': [
        'Bệnh tim mạch (suy tim, bệnh mạch vành) - thận trọng, theo dõi chặt chẽ',
        'Tăng huyết áp không kiểm soát - có thể tăng huyết áp',
        'Loạn nhịp tim nhẹ - có thể làm nặng',
        'Đái tháo đường - có thể tăng đường huyết',
        'Hạ kali máu - có thể làm nặng',
        'Cường giáp - tăng nhạy cảm với catecholamine',
        'Dùng với digoxin - tăng nguy cơ loạn nhịp',
        'Dùng với theophylline - tăng tác dụng phụ']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Salmeterol là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Salmeterol được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hen phế quản không kiểm soát có thể gây nguy hiểm cho cả mẹ và thai nhi (thiếu oxy, suy thai). Salmeterol có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng PHẢI dùng kết hợp với ICS. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Salmeterol bài tiết ít vào sữa mẹ. Nồng độ trong sữa mẹ rất thấp do hấp thu toàn thân ít từ dạng hít. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe':
        'Thận trọng - salmeterol chuyển hóa qua gan (CYP3A4), có thể tích lũy ở suy gan nặng'
        , 'notes':
        'Salmeterol chuyển hóa qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ nhịp tim và tác dụng phụ. Có thể cần giảm liều hoặc tăng khoảng cách giữa các liều.'
        }, 'overdose_management': {'symptoms': [
        'Nhịp tim nhanh nghiêm trọng (>150 bpm)', 'Run cơ nặng',
        'Loạn nhịp tim (rung nhĩ, rung thất)', 'Đau ngực', 'Khó thở nặng',
        'Co thắt phế quản nghịch lý', 'Hạ kali máu nghiêm trọng',
        'Tăng đường huyết', 'Kích động, lo âu', 'Đau đầu nặng'], 'antidote':
        'Không có antidote đặc hiệu. Beta-blocker chọn lọc beta-1 (atenolol, metoprolol) có thể được dùng để đối kháng tác dụng tim mạch, nhưng thận trọng vì có thể làm nặng co thắt phế quản.'
        , 'treatment': ['Ngừng ngay salmeterol',
        'Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)',
        'Theo dõi nhịp tim, huyết áp, ECG liên tục',
        'Điều trị loạn nhịp tim nếu có (theo protocol)',
        'Bổ sung kali nếu hạ kali máu', 'Điều trị tăng đường huyết nếu cần',
        'Nếu có co thắt phế quản nghịch lý: dùng ipratropium hoặc corticosteroid, tránh dùng SABA'
        , 'Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'Theo dõi liên tục: nhịp tim, huyết áp, ECG, SpO2, kali máu, đường huyết, đáp ứng phế quản. Theo dõi ít nhất 12-24 giờ do thời gian bán thải dài (5.5 giờ).'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Beta-blocker chọn lọc beta-1 (Atenolol, Metoprolol)', 'mechanism':
        'Đối kháng tác dụng beta-adrenergic, giảm tác dụng tim mạch',
        'indication': 'Quá liều gây nhịp tim nhanh nghiêm trọng, loạn nhịp tim',
        'caution':
        'Thận trọng vì có thể làm nặng co thắt phế quản. Chỉ dùng khi tác dụng tim mạch nghiêm trọng và có hỗ trợ hô hấp sẵn sàng.'
        }], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Beta-blocker chọn lọc beta-1 có thể được dùng để đối kháng tác dụng tim mạch nhưng thận trọng.'
        }, 'administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dùng dạng hít (MDI hoặc DPI). Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).'
        , 'timing':
        'Dùng 2 lần/ngày (sáng và tối), cách nhau khoảng 12 giờ. Dùng đều đặn hàng ngày, không phải khi cần.'
        , 'with_ics':
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid). Có thể dùng riêng hoặc dùng dạng fixed-dose combination (Seretide/Advair: fluticasone + salmeterol).'
        , 'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và tránh nấm miệng (đặc biệt nếu dùng với ICS).'
        , 'notes':
        'Không dùng để cắt cơn (tác dụng chậm). Luôn có SABA (salbutamol) sẵn sàng để cắt cơn. Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị.'
        }}, 'references': {'primary_sources': [
        'FDA Label: Serevent (Salmeterol)',
        'UpToDate: Long-acting beta-2 agonists in asthma',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Salmeterol'], 'last_updated': '2025-02-03',
        'evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'}}}

__all__ = ['LONG_ACTING_BETA_2_AGONIST_LABAS_DRUGS']
