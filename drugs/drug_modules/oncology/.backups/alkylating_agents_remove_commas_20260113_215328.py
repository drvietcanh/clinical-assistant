"""Oncology Medications
Active module - contains all oncology drug data"""

# Alkylating Agents

ALKYLATING_AGENTS_DRUGS = {
    "Cyclophosphamide": {'group': 'Oncology - Alkylating Agent', 'vietnamese_name':
        'Cyclophosphamide, Endoxan, Cytoxan', 'administration': ['PO', 'IV'],
        'indications': ['U lympho (lymphoma)', 'Bệnh bạch cầu', 'Ung thư vú',
        'Ung thư buồng trứng', 'Bệnh tự miễn (lupus, vasculitis, liều thấp)'],
        'contraindications': ['Dị ứng cyclophosphamide',
        'Giảm bạch cầu/tiểu cầu nặng', 'Suy thận nặng', 'Suy gan nặng',
        'Viêm bàng quang chảy máu', 'Có thai', 'Đang cho con bú'], 'dosage': {
        'adult_cancer_high': '500-1000mg/m² IV mỗi 3-4 tuần',
        'adult_cancer_moderate': '50-200mg/m² PO/IV mỗi ngày',
        'adult_autoimmune':
        '1-2mg/kg PO mỗi ngày hoặc 500-750mg/m² IV mỗi tháng', 'notes':
        'Uống nhiều nước (2-3L/ngày) để phòng viêm bàng quang. Có thể dùng mesna để bảo vệ'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều 25-50%', 'under_30': 'Thận trọng, giảm liều đáng kể'},
        'side_effects': [
        'Viêm bàng quang chảy máu (hemorrhagic cystitis - phổ biến, nguy hiểm)',
        'Giảm bạch cầu, tiểu cầu (myelosuppression)', 'Buồn nôn, nôn',
        'Rụng tóc', 'Vô sinh (nam và nữ)', 'Ung thư thứ phát (hiếm)',
        'Độc tim (với liều cao)', 'Hội chứng lysis khối u'], 'interactions': [
        'Allopurinol: tăng độc tính', 'Phenobarbital: tăng chuyển hóa',
        'Succinylcholine: kéo dài tác dụng',
        'Mesna: bảo vệ chống viêm bàng quang'], 'pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Cyclophosphamide là prodrug alkylating agent, được chuyển hóa ở gan thành các chất hoạt động (phosphoramide mustard và acrolein). Phosphoramide mustard gây liên kết chéo DNA (cross-linking), ngăn chặn quá trình sao chép DNA và dẫn đến tổn thương DNA, chết tế bào. Acrolein gây độc cho bàng quang (hemorrhagic cystitis). Tác dụng: điều trị ung thư (lymphoma, leukemia, ung thư vú, buồng trứng) và bệnh tự miễn (lupus, vasculitis) ở liều thấp hơn. Có tác dụng ức chế miễn dịch mạnh'
        , 'monitoring': [
        'Công thức máu (CBC) trước và sau mỗi chu kỳ - myelosuppression (giảm bạch cầu, tiểu cầu)'
        ,
        'Dấu hiệu viêm bàng quang chảy máu: tiểu máu, đau khi tiểu, tiểu nhiều lần (RẤT QUAN TRỌNG)'
        , 'Lượng nước tiểu (đảm bảo >2-3L/ngày để phòng viêm bàng quang)',
        'Chức năng thận (creatinine, BUN) - điều chỉnh liều khi suy thận',
        'Chức năng gan (ALT, AST) - cần gan hoạt động để chuyển hóa thành chất hoạt động'
        , 'Dấu hiệu nhiễm trùng (do giảm bạch cầu)',
        'Dấu hiệu chảy máu (do giảm tiểu cầu)',
        'Dấu hiệu hội chứng lysis khối u: tăng uric acid, kali, phosphate (với liều cao)'
        , 'Dấu hiệu độc tim: nhịp tim nhanh, suy tim (với liều cao)',
        'Uric acid (tăng nguy cơ gout, hội chứng lysis khối u)'], 'precautions':
        [
        'UỐNG NHIỀU NƯỚC (2-3L/ngày) để phòng viêm bàng quang chảy máu - đây là độc tính phổ biến và nguy hiểm'
        , 'NGỪNG NGAY nếu có tiểu máu hoặc dấu hiệu viêm bàng quang',
        'Có thể dùng mesna (sodium 2-mercaptoethanesulfonate) để bảo vệ bàng quang khi dùng liều cao'
        ,
        'Mesna liều: 20% liều cyclophosphamide, dùng trước, 4 giờ, và 8 giờ sau cyclophosphamide'
        ,
        'Theo dõi chặt chẽ myelosuppression - có thể cần hỗ trợ G-CSF hoặc truyền máu'
        , 'Dùng allopurinol để phòng tăng uric acid (hội chứng lysis khối u)',
        'Thận trọng ở bệnh nhân suy gan (cần gan để chuyển hóa thành chất hoạt động)'
        , 'Thận trọng ở bệnh nhân suy thận (giảm liều)',
        'Có thể gây vô sinh (nam và nữ) - tư vấn trước khi điều trị',
        'Có thể gây ung thư thứ phát (hiếm, với liều cao)',
        'Theo dõi nhiễm trùng và chảy máu (do myelosuppression)',
        'Không dùng trong thai kỳ (dị tật thai nhi)'], 'pharmacokinetics': {
        'half_life': '3-12 giờ (phụ thuộc vào chuyển hóa)', 'onset':
        'Chậm (cần chuyển hóa thành chất hoạt động)', 'duration':
        'Dài (tác dụng kéo dài)', 'protein_binding': '10-20% (thấp)',
        'clearance':
        'Gan (chuyển hóa thành chất hoạt động qua CYP2B6, CYP3A4), thận (thải trừ)'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nang: bảo quản ở nhiệt độ phòng. Dung dịch IV: bảo quản ở nhiệt độ phòng, dùng trong 24 giờ. Không đông lạnh'
        , 'black_box_warnings':
        'Viêm bàng quang chảy máu có thể nghiêm trọng - cần uống nhiều nước (2-3L/ngày) và dùng mesna khi cần. Myelosuppression có thể nặng, dẫn đến nhiễm trùng và chảy máu. Có thể gây vô sinh vĩnh viễn. Có thể gây ung thư thứ phát. Chống chỉ định trong thai kỳ'
        , 'drug_interactions': {'major': [{'drug': 'Allopurinol', 'mechanism':
        'Tăng độc tính của cyclophosphamide', 'effect':
        'Tăng nguy cơ độc tính, đặc biệt myelosuppression', 'management':
        'Thận trọng. Giảm liều cyclophosphamide hoặc ngừng allopurinol nếu có thể.'
        }, {'drug': 'Phenobarbital, Rifampin', 'mechanism':
        'Cảm ứng CYP450, tăng chuyển hóa cyclophosphamide', 'effect':
        'Tăng chuyển hóa thành chất hoạt động, tăng độc tính', 'management':
        'Thận trọng. Theo dõi độc tính chặt chẽ. Có thể cần điều chỉnh liều.'}],
        'moderate': [{'drug': 'Succinylcholine', 'mechanism':
        'Cyclophosphamide ức chế cholinesterase', 'effect':
        'Kéo dài tác dụng succinylcholine', 'management':
        'Thận trọng khi gây mê. Giảm liều succinylcholine hoặc dùng thuốc khác.'
        }, {'drug': 'Warfarin', 'mechanism': 'Có thể tăng nguy cơ chảy máu',
        'effect': 'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}],
        'minor': [{'drug': 'Mesna', 'mechanism': 'Bảo vệ chống viêm bàng quang',
        'effect': 'Giảm nguy cơ viêm bàng quang chảy máu', 'management':
        'Dùng kèm khi dùng liều cao. Liều: 20% liều cyclophosphamide.'}]},
        'contraindications': {'tuyệt_đối': [
        'Viêm bàng quang chảy máu hoạt động', 'Có thai', 'Đang cho con bú',
        'Dị ứng cyclophosphamide', 'Giảm bạch cầu/tiểu cầu nặng'], 'tương_đối':
        ['Suy thận nặng (CrCl <30) - giảm liều đáng kể',
        'Suy gan nặng - thận trọng (cần gan để chuyển hóa thành chất hoạt động)',
        'Nhiễm trùng hoạt động - tăng nguy cơ',
        'Bệnh tim - tăng nguy cơ độc tim',
        'Người cao tuổi - tăng nguy cơ độc tính',
        'Đã dùng cyclophosphamide trước đây - tích lũy độc tính']},
        'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Cyclophosphamide gây dị tật thai nhi, chậm phát triển, tử vong thai nhi. Cần test thai trước khi điều trị. Sử dụng biện pháp tránh thai hiệu quả trong và sau điều trị (ít nhất 6-12 tháng). Có thể gây vô sinh vĩnh viễn (nam và nữ).'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Cyclophosphamide bài tiết vào sữa mẹ. Không an toàn cho trẻ bú mẹ. Có thể gây độc tính nghiêm trọng, myelosuppression ở trẻ.'
        , 'recommendation':
        'Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng điều trị.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể giảm liều nhẹ', 'severe':
        'Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ', 'notes':
        'Cyclophosphamide là prodrug, cần gan để chuyển hóa thành chất hoạt động (phosphoramide mustard). Suy gan làm giảm chuyển hóa, giảm hiệu quả. Tuy nhiên, suy gan nặng có thể làm giảm clearance, tăng độc tính.'
        }, 'overdose_management': {'symptoms': [
        'Viêm bàng quang chảy máu nặng (tiểu máu, đau bụng dưới)',
        'Myelosuppression nặng (giảm bạch cầu, tiểu cầu, thiếu máu)',
        'Nhiễm trùng nặng (do giảm bạch cầu)', 'Chảy máu (do giảm tiểu cầu)',
        'Hội chứng lysis khối u (tăng uric acid, kali, phosphate)',
        'Độc tim (rối loạn nhịp, suy tim)', 'Suy thận cấp', 'Suy hô hấp'],
        'antidote':
        'Không có antidote đặc hiệu. Mesna không phải antidote nhưng có thể giúp bảo vệ bàng quang'
        , 'treatment': ['Ngừng thuốc ngay lập tức',
        'UỐNG NHIỀU NƯỚC (3-4L/ngày) hoặc truyền dịch đầy đủ để phòng viêm bàng quang'
        ,
        'Mesna ngay lập tức (20% liều cyclophosphamide) nếu chưa dùng, sau đó mỗi 4 giờ'
        , 'Theo dõi sát nước tiểu (dấu hiệu viêm bàng quang chảy máu)',
        'Điều trị viêm bàng quang: Mesna, truyền dịch, có thể cần đặt catheter',
        'Theo dõi công thức máu chặt chẽ',
        'Điều trị myelosuppression: G-CSF, truyền máu/tiểu cầu nếu cần',
        'Điều trị nhiễm trùng: Kháng sinh phổ rộng',
        'Điều trị hội chứng lysis khối u: Allopurinol, hydration, rasburicase nếu cần'
        , 'Theo dõi chức năng thận, điện giải',
        'Điều trị hỗ trợ: Chống nôn, truyền dịch, theo dõi tim mạch'],
        'monitoring':
        'Nước tiểu (hematuria), công thức máu (CBC), chức năng thận, uric acid, kali, phosphate, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, ECG'
        }, 'reversal_agents': {'available': False, 'agents': [
        'Mesna (bảo vệ bàng quang, không phải antidote)']},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm kích ứng dạ dày'
        , 'timing':
        'Uống nhiều nước (2-3L/ngày) trước, trong và sau khi uống để phòng viêm bàng quang. Uống vào buổi sáng để tăng lượng nước tiểu ban ngày.'
        }, 'iv': {'reconstitution': 'Pha với D5W hoặc NS để nồng độ 1-20mg/mL',
        'infusion_rate': 'Truyền trong 30-60 phút. Tốc độ phụ thuộc liều',
        'compatibility': ['D5W', 'NS'], 'incompatibility': ['Các thuốc khác'],
        'notes':
        'UỐNG NHIỀU NƯỚC (2-3L/ngày) trước, trong và sau truyền để phòng viêm bàng quang. Dùng mesna khi dùng liều cao (20% liều cyclophosphamide, dùng trước, 4 giờ, và 8 giờ sau). Theo dõi lượng nước tiểu (đảm bảo >2L/ngày).'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Cytoxan (cyclophosphamide)',
        'UpToDate - Cyclophosphamide: Drug information',
        'NCCN Guidelines - Cancer treatment',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews'}},
    "Ifosfamide": {'group': 'Oncology - Alkylating Agent', 'vietnamese_name':
        'Ifosfamide, Ifex', 'administration': ['IV'], 'indications': [
        'Ung thư tinh hoàn', 'U lympho', 'Sarcoma mô mềm', 'Ung thư xương',
        'Ung thư phổi (một số loại)'], 'contraindications': [
        'Dị ứng ifosfamide', 'Suy thận nặng', 'Giảm bạch cầu/tiểu cầu nặng',
        'Viêm bàng quang chảy máu', 'Có thai', 'Đang cho con bú'], 'dosage': {
        'adult_standard': '1200-2000mg/m² IV x 3-5 ngày (mỗi 3-4 tuần)',
        'adult_high': '3000-5000mg/m² IV x 1-3 ngày (với mesna)', 'notes':
        'Luôn dùng kèm mesna để bảo vệ bàng quang. Uống nhiều nước'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, giảm liều 25-50%', 'under_30':
        'Thận trọng, giảm liều đáng kể'}, 'side_effects': [
        'Viêm bàng quang chảy máu (nguy hiểm - cần mesna)',
        'Độc thần kinh trung ương (lú lẫn, co giật - với liều cao)',
        'Giảm bạch cầu, tiểu cầu', 'Buồn nôn, nôn', 'Rụng tóc', 'Độc thận',
        'Vô sinh'], 'interactions': [
        'Mesna: bảo vệ chống viêm bàng quang (bắt buộc)',
        'Phenobarbital: tăng chuyển hóa', 'Cisplatin: tăng độc thận'],
        'pregnancy': 'D - Chống chỉ định', 'mechanism_of_action':
        'Ifosfamide là alkylating agent (nitrogen mustard), chuyển hóa trong gan thành các chất hoạt động (4-hydroxyifosfamide, aldophosphamide, isophosphoramide mustard). Các chất này gắn vào DNA, tạo ra cross-links DNA-DNA và DNA-protein, gây đứt gãy DNA và ngăn cản quá trình sao chép DNA. Thuốc tác động chủ yếu lên tế bào đang phân chia nhanh, gây độc tế bào và chết tế bào ung thư. Acrolein (sản phẩm chuyển hóa) gây độc bàng quang (hemorrhagic cystitis), cần dùng kèm mesna để bảo vệ'
        , 'monitoring': [
        'Công thức máu toàn phần (CBC) trước mỗi chu kỳ và giữa các chu kỳ',
        'Chức năng thận (creatinine, eGFR) trước mỗi chu kỳ',
        'Chức năng gan (ALT, AST, bilirubin) trước mỗi chu kỳ',
        'Nước tiểu (hematuria, proteinuria) - theo dõi viêm bàng quang chảy máu',
        'Dấu hiệu viêm bàng quang chảy máu (đái máu, đau bụng dưới) - nguy hiểm',
        'Dấu hiệu độc thần kinh trung ương (lú lẫn, co giật, hôn mê) - với liều cao'
        , 'Điện giải (Na, K) nếu có độc thần kinh trung ương',
        'Theo dõi lượng nước tiểu (đảm bảo >100ml/giờ)'], 'precautions': [
        'LUÔN dùng kèm mesna để bảo vệ bàng quang (bắt buộc)',
        'Uống nhiều nước và truyền dịch đầy đủ (đảm bảo >2L/ngày)',
        'Theo dõi sát nước tiểu (dấu hiệu viêm bàng quang chảy máu)',
        'Ngừng ngay nếu có viêm bàng quang chảy máu nặng',
        'Có thể gây độc thần kinh trung ương với liều cao (lú lẫn, co giật - cần điều trị)'
        , 'Giảm liều 25-50% nếu suy thận (CrCl 30-60)',
        'Tránh dùng với các thuốc độc thận (cisplatin)',
        'Có thể gây vô sinh (cần tư vấn trước điều trị)',
        'Mesna phải được dùng đúng liều và thời điểm (trước, trong, và sau ifosfamide)'
        ],
        'onset': '1-2 tuần (tác dụng lâm sàng)', 'duration':
        'Kéo dài (tích lũy)', 'protein_binding': '<20%', 'clearance':
        'Gan (chuyển hóa chủ yếu qua CYP2B6, CYP3A4), thận (thải trừ)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu'
        , 'black_box_warnings':
        'Có thể gây viêm bàng quang chảy máu nặng và nguy hiểm tính mạng. LUÔN phải dùng kèm mesna để bảo vệ bàng quang. Có thể gây độc thần kinh trung ương nặng (lú lẫn, co giật, hôn mê) với liều cao'
        , 'drug_interactions': {'major': [{'drug': 'Cisplatin', 'mechanism':
        'Cả hai đều có độc tính thận, tác dụng cộng dồn làm tăng nguy cơ suy thận cấp và độc thận nghiêm trọng.'
        , 'effect': 'Tăng nguy cơ suy thận cấp, độc thận nghiêm trọng',
        'management':
        'Thận trọng khi dùng đồng thời. Theo dõi chức năng thận chặt chẽ. Duy trì đủ dịch. Có thể cần giảm liều hoặc tránh dùng đồng thời.'
        }], 'moderate': [{'drug': 'Phenobarbital', 'mechanism':
        'Phenobarbital cảm ứng CYP450, làm tăng chuyển hóa ifosfamide, giảm nồng độ ifosfamide trong máu.'
        , 'effect': 'Giảm nồng độ ifosfamide, giảm hiệu quả điều trị',
        'management':
        'Theo dõi đáp ứng điều trị. Có thể cần tăng liều ifosfamide.'}],
        'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định',
        'Viêm bàng quang chảy máu nặng - chống chỉ định cho đến khi hồi phục'],
        'tương_đối': [
        'Suy thận nặng (CrCl <30) - giảm liều đáng kể, theo dõi chặt chẽ',
        'Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục',
        'Suy gan - thận trọng, có thể cần giảm liều',
        'Bệnh nhân có tiền sử độc thần kinh trung ương - tăng nguy cơ độc thần kinh nặng'
        ], 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Ifosfamide gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Ifosfamide bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng ifosfamide. Ngừng cho con bú hoặc ngừng thuốc.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        'Ifosfamide chuyển hóa chủ yếu qua gan (CYP2B6, CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ.'
        }, 'overdose_management': {'symptoms': [
        'Viêm bàng quang chảy máu nặng (đái máu, đau bụng dưới)',
        'Độc thần kinh trung ương nặng (lú lẫn, co giật, hôn mê)',
        'Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)', 'Suy thận cấp',
        'Nôn mửa nặng'], 'antidote':
        'Mesna (nếu chưa dùng) - bảo vệ bàng quang', 'treatment': [
        'Ngừng ngay ifosfamide',
        'Nếu chưa dùng mesna: dùng mesna ngay để bảo vệ bàng quang',
        'Truyền dịch đầy đủ (đảm bảo >2L/ngày, >100ml/giờ)',
        'Theo dõi nước tiểu (hematuria, proteinuria)',
        'Điều trị viêm bàng quang chảy máu nếu có (mesna, truyền dịch, có thể cần đặt ống thông)'
        ,
        'Điều trị độc thần kinh trung ương nếu có (methylene blue, thiamine, có thể cần điều trị co giật)'
        , 'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng thận, chức năng gan'], 'monitoring':
        'CBC, chức năng thận, chức năng gan, nước tiểu (hematuria), dấu hiệu độc thần kinh trung ương, lượng nước tiểu'
        }, 'reversal_agents': {'available': True, 'agents': [{'name': 'Mesna',
        'indication':
        'Bảo vệ bàng quang chống viêm bàng quang chảy máu do ifosfamide',
        'dose':
        '20% liều ifosfamide IV trước, trong, và sau ifosfamide (tổng 60% liều ifosfamide)'
        , 'notes':
        'Bắt buộc phải dùng kèm với ifosfamide. Mesna gắn với acrolein (sản phẩm chuyển hóa độc của ifosfamide) trong nước tiểu, bảo vệ bàng quang.'
        }]}, 'administration_instructions': {'oral': {'with_food':
        'Không áp dụng', 'timing': 'Không có dạng uống (chỉ có IV)'}, 'iv': {
        'reconstitution': 'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất',
        'infusion_rate': 'Truyền trong 1-4 giờ', 'compatibility': ['NS', 'D5W'],
        'incompatibility': [], 'notes':
        '1200-2000mg/m² IV x 3-5 ngày (mỗi 3-4 tuần). LUÔN dùng kèm mesna (20% liều ifosfamide IV trước, trong, và sau ifosfamide). Truyền dịch đầy đủ (đảm bảo >2L/ngày, >100ml/giờ). Truyền trong 1-4 giờ.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Ifosfamide (Ifex)',
        'UpToDate - Ifosfamide Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-15', "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    }


__all__ = ['ALKYLATING_AGENTS_DRUGS']
