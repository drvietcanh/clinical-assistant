"""Oncology Medications
Active module - contains all oncology drug data"""

# Antimetabolite (Antifolate)s

ANTIMETABOLITE_ANTIFOLATES_DRUGS = {
    "Methotrexate": {'group': 'Oncology - Antimetabolite (Antifolate)', 'vietnamese_name':
        'Methotrexate, MTX, Amethopterin', 'administration': ['PO', 'IV', 'IM',
        'SC', 'IT'],
        'indications': [
        'U lympho (lymphoma)', 'U nguyên bào nuôi (choriocarcinoma)',
        'Ung thư đầu cổ', 'Ung thư phổi', 'Viêm khớp dạng thấp (liều thấp)',
        'Vẩy nến (liều thấp)'],
        'contraindications': [
        'Suy thận nặng', 'Suy gan nặng', 'Giảm bạch cầu/tiểu cầu nặng',
        'Loét dạ dày tá tràng hoạt động', 'Có thai', 'Đang cho con bú'],
        'dosage': {'adult_cancer_high':
        '50-250mg/m² IV (cần folinic acid rescue)', 'adult_cancer_moderate':
        '10-50mg/m² IV/IM/PO', 'adult_ra_psoriasis': '7.5-25mg PO x 1 lần/tuần',
        'adult_it': '12-15mg IT (theo dõi chặt chẽ)', 'notes':
        'Liều cao (>50mg/m²) cần folinic acid rescue sau 24 giờ. Uống nhiều nước'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều 25-50%', 'under_30':
        'Không dùng hoặc giảm liều đáng kể, theo dõi sát'}, 'side_effects': [
        'Giảm bạch cầu, tiểu cầu, thiếu máu (myelosuppression - nghiêm trọng)',
        'Loét miệng (stomatitis)', 'Tiêu chảy',
        'Độc gan (tăng transaminase, xơ gan)',
        'Độc phổi (viêm phổi kẽ - hiếm nhưng nguy hiểm)',
        'Độc thận (với liều cao)', 'Rụng tóc', 'Phát ban'], 'interactions': [
        'Probenecid: tăng độc tính methotrexate', 'NSAID: tăng độc tính',
        'Penicillin: tăng độc tính',
        'Trimethoprim-Sulfamethoxazole: tăng độc tính',
        'Folinic acid: giải độc (rescue therapy)'], 'pregnancy':
        'X - Chống chỉ định tuyệt đối', 'mechanism_of_action':
        'Antimetabolite, folic acid antagonist. Ức chế enzyme dihydrofolate reductase (DHFR), ngăn cản chuyển đổi dihydrofolate thành tetrahydrofolate (THF). THF cần thiết cho tổng hợp purine và thymidine (DNA, RNA). Ức chế tổng hợp DNA và RNA → ức chế sự phát triển và phân chia tế bào. Tác động mạnh lên tế bào phân chia nhanh (tế bào ung thư, tế bào miễn dịch, tế bào niêm mạc, tế bào tủy xương). Được dùng trong điều trị ung thư (liều cao), viêm khớp dạng thấp, vảy nến (liều thấp), và các bệnh tự miễn khác.'
        , 'monitoring': [
        'Công thức máu (WBC, platelet, hemoglobin) - giảm bạch cầu, giảm tiểu cầu, thiếu máu - QUAN TRỌNG'
        , 'Chức năng gan (ALT, AST, bilirubin, albumin) - độc tính gan, xơ gan',
        'Chức năng thận (creatinine, eGFR) - độc tính thận',
        'X-quang phổi (xơ phổi - hiếm nhưng nguy hiểm)',
        'Nồng độ methotrexate trong máu (nếu dùng liều cao)',
        'Dấu hiệu nhiễm trùng (do giảm bạch cầu)',
        'Dấu hiệu chảy máu (do giảm tiểu cầu)',
        'Dấu hiệu độc tính niêm mạc (loét miệng, tiêu chảy)'], 'precautions': [
        'Độc tính nghiêm trọng - phải theo dõi chặt chẽ',
        'PHẢI dùng folic acid để giảm độc tính (5-10mg/tuần, không dùng cùng ngày với methotrexate)'
        'Giảm bạch cầu, giảm tiểu cầu, thiếu máu - theo dõi công thức máu mỗi 1-4 tuần'
        , 'Độc tính gan - có thể gây xơ gan, kiểm tra chức năng gan định kỳ',
        'Độc tính thận - uống nhiều nước, kiểm tra chức năng thận',
        'Không dùng ở suy thận nặng', 'Không dùng ở suy gan',
        'Tương tác với NSAID, aspirin → tăng nồng độ methotrexate, tăng độc tính',
        'Tương tác với trimethoprim-sulfamethoxazole → tăng độc tính',
        'Không dùng ở phụ nữ có thai (gây dị tật thai nhi) - dùng biện pháp tránh thai'
        'Liều thấp (viêm khớp, vảy nến): 7.5-25mg/tuần, liều cao (ung thư): 100mg/m² trở lên'
        , 'Ngừng nếu có dấu hiệu độc tính nghiêm trọng'], 'pharmacokinetics': {
        'half_life': '3-10 giờ (liều thấp), 8-15 giờ (liều cao)', 'onset':
        'Vài giờ đến vài ngày', 'duration': 'Dài (nhiều ngày, tích lũy)',
        'protein_binding': '50-60%', 'metabolism':
        'Một phần trong gan, một phần bị polyglutamylation trong tế bào (tích lũy)'
        , 'clearance': 'Chủ yếu qua thận (80-90%), cần điều chỉnh thận'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Dung dịch tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.'
        , 'black_box_warnings':
        'Độc tính nghiêm trọng, có thể tử vong. Giảm bạch cầu, giảm tiểu cầu, và thiếu máu có thể nặng. Độc tính gan có thể gây xơ gan. Độc tính thận có thể gây suy thận cấp. Phải theo dõi công thức máu và chức năng gan, thận định kỳ. Không dùng ở phụ nữ có thai (gây dị tật thai nhi).'
        , 'drug_interactions': {'major': [{'drug': 'Probenecid', 'mechanism':
        'Probenecid ức chế bài tiết ống thận của methotrexate, làm giảm thải trừ và tăng nồng độ methotrexate trong máu.'
        , 'effect':
        'Tăng nồng độ methotrexate đáng kể, tăng độc tính (giảm bạch cầu, độc gan, độc thận)'
        , 'management':
        'TRÁNH DÙNG đồng thời. Nếu bắt buộc, giảm liều methotrexate 50-75% và theo dõi chặt chẽ công thức máu, chức năng gan, thận.'
        }, {'drug': 'NSAID (Ibuprofen, Naproxen, Diclofenac, Aspirin)',
        'mechanism':
        'NSAID ức chế bài tiết ống thận của methotrexate, làm giảm thải trừ và tăng nồng độ methotrexate.'
        , 'effect':
        'Tăng nồng độ methotrexate, tăng độc tính nghiêm trọng (giảm bạch cầu, độc gan, độc thận)'
        , 'management':
        'TRÁNH DÙNG đồng thời, đặc biệt với liều cao methotrexate. Nếu dùng liều thấp (RA, psoriasis), thận trọng và theo dõi chặt chẽ. Có thể dùng acetaminophen thay thế.'
        }, {'drug': 'Trimethoprim-Sulfamethoxazole', 'mechanism':
        'Cả hai đều là folic acid antagonists, tác dụng cộng dồn làm tăng độc tính.'
        , 'effect':
        'Tăng độc tính nghiêm trọng (giảm bạch cầu, thiếu máu megaloblastic)',
        'management':
        'TRÁNH DÙNG đồng thời. Nếu bắt buộc, theo dõi chặt chẽ công thức máu và bổ sung folic acid.'
        }], 'moderate': [{'drug': 'Penicillin', 'mechanism':
        'Penicillin có thể ức chế bài tiết ống thận của methotrexate.',
        'effect': 'Tăng nồng độ methotrexate, tăng độc tính', 'management':
        'Thận trọng khi dùng đồng thời. Theo dõi công thức máu và chức năng gan, thận.'
        }, {'drug': 'Folic acid (nếu dùng cùng ngày)', 'mechanism':
        'Folic acid đối kháng tác dụng của methotrexate, giảm hiệu quả điều trị.',
        'effect': 'Giảm hiệu quả điều trị methotrexate', 'management':
        'KHÔNG dùng folic acid cùng ngày với methotrexate. Dùng folic acid vào ngày khác (5-10mg/tuần) để giảm độc tính mà không giảm hiệu quả.'
        }], 'minor': [{'drug': 'Acetaminophen', 'mechanism':
        'Acetaminophen có thể tăng độc tính gan khi dùng với methotrexate.',
        'effect': 'Tăng nguy cơ độc gan', 'management':
        'Thận trọng, tránh dùng liều cao acetaminophen. Theo dõi chức năng gan.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Có thai (gây dị tật thai nhi, sảy thai)', 'Đang cho con bú',
        'Suy thận nặng (CrCl <30)', 'Suy gan nặng',
        'Giảm bạch cầu/tiểu cầu nặng', 'Loét dạ dày tá tràng hoạt động'],
        'tương_đối': ['Suy thận (CrCl 30-60: giảm liều 25-50%)',
        'Suy gan nhẹ-trung bình (theo dõi chức năng gan)',
        'Nhiễm trùng đang hoạt động (ức chế miễn dịch)',
        'Bệnh phổi mạn tính (nguy cơ xơ phổi)']}, 'pregnancy_lactation': {
        'fda_category': 'X', 'pregnancy_details':
        'Methotrexate chống chỉ định tuyệt đối trong thai kỳ. Gây dị tật thai nhi nghiêm trọng (dị tật hệ thần kinh, sọ mặt, chi), sảy thai, và tử vong thai nhi. Phụ nữ trong độ tuổi sinh đẻ PHẢI dùng biện pháp tránh thai hiệu quả trong và sau khi dùng methotrexate ít nhất 3 tháng (hoặc 1 chu kỳ ovulatory sau liều cuối). Nam giới cũng nên dùng biện pháp tránh thai trong và sau khi dùng ít nhất 3 tháng.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Methotrexate bài tiết vào sữa mẹ ở nồng độ đáng kể. Chống chỉ định khi cho con bú. Có thể gây độc tính nghiêm trọng cho trẻ bú mẹ (giảm bạch cầu, độc gan, độc thận).'
        , 'recommendation':
        'KHÔNG dùng khi cho con bú. Ngừng cho con bú hoặc ngừng methotrexate.'}
        }, 'hepatic_adjustment': {'mild':
        'Thận trọng, theo dõi chức năng gan. Có thể cần giảm liều nhẹ.',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan chặt chẽ.',
        'severe':
        'Chống chỉ định hoặc thận trọng tối đa. Nguy cơ độc gan cao, có thể gây suy gan.'
        , 'notes':
        'Methotrexate chuyển hóa một phần qua gan và tích lũy trong gan. Suy gan làm tăng nguy cơ độc tính gan, xơ gan. Theo dõi ALT, AST, bilirubin, albumin định kỳ. Ngừng nếu có dấu hiệu độc gan.'
        }, 'overdose_management': {'symptoms': [
        'Giảm bạch cầu, giảm tiểu cầu, thiếu máu nặng (myelosuppression)',
        'Loét miệng, tiêu chảy nặng (mucositis)',
        'Độc gan (tăng ALT/AST, vàng da, suy gan)',
        'Độc thận (tăng creatinine, suy thận cấp)',
        'Độc phổi (khó thở, xơ phổi)', 'Nhiễm trùng nặng (do giảm bạch cầu)',
        'Chảy máu (do giảm tiểu cầu)'], 'antidote':
        'Folinic acid (leucovorin) - giải độc methotrexate. Dùng càng sớm càng tốt, tốt nhất trong vòng 24 giờ.'
        , 'treatment': ['Ngừng methotrexate ngay lập tức',
        'Dùng folinic acid (leucovorin) ngay: 10-15mg/m² mỗi 6 giờ cho đến khi nồng độ methotrexate <0.05 micromol/L. Liều folinic acid = liều methotrexate hoặc cao hơn.'
        'Tăng cường thủy phân (uống nhiều nước, truyền dịch) để tăng thải trừ qua thận'
        'Kiềm hóa nước tiểu (sodium bicarbonate) để tăng thải trừ methotrexate',
        'Theo dõi công thức máu, chức năng gan, thận chặt chẽ',
        'Điều trị nhiễm trùng nếu có (kháng sinh phổ rộng)',
        'Truyền tiểu cầu, hồng cầu nếu cần',
        'Theo dõi nồng độ methotrexate trong máu',
        'Có thể cần lọc máu (hemodialysis) nếu suy thận nặng'], 'monitoring':
        'Công thức máu mỗi ngày, chức năng gan/thận, nồng độ methotrexate, dấu hiệu nhiễm trùng, chảy máu. Theo dõi ít nhất 1-2 tuần.'
        }, 'reversal_agents': {'available': True, 'agents': [{'name':
        'Folinic acid (Leucovorin)', 'mechanism':
        'Folinic acid là dạng hoạt động của folic acid, bỏ qua bước ức chế bởi methotrexate, cung cấp tetrahydrofolate cho tế bào bình thường.'
        , 'indication': 'Quá liều methotrexate, đặc biệt liều cao (>50mg/m²)',
        'dosage':
        '10-15mg/m² IV/PO mỗi 6 giờ cho đến khi nồng độ methotrexate <0.05 micromol/L. Liều folinic acid thường bằng hoặc cao hơn liều methotrexate.'
        , 'notes':
        'Dùng càng sớm càng tốt, tốt nhất trong vòng 24 giờ sau liều methotrexate. Tiếp tục cho đến khi nồng độ methotrexate về bình thường.'
        }]}, 'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.'
        , 'timing':
        'Liều thấp (RA, psoriasis): uống 1 lần/tuần vào cùng ngày mỗi tuần. Liều cao (ung thư): theo chỉ định. Uống nhiều nước (2-3L/ngày) để tăng thải trừ qua thận.'
        }, 'iv': {'reconstitution':
        'Pha với D5W hoặc Normal saline theo hướng dẫn. Liều cao cần pha loãng đúng cách.'
        , 'infusion_rate':
        'Truyền trong 30-60 phút (liều thấp) hoặc theo chỉ định (liều cao). Không truyền nhanh.'
        , 'compatibility': ['D5W', 'Normal saline'], 'incompatibility': [
        'Không trộn với các thuốc khác'], 'notes':
        'Liều cao (>50mg/m²) cần folinic acid rescue sau 24 giờ. Uống nhiều nước hoặc truyền dịch để tăng thải trừ. Kiềm hóa nước tiểu nếu cần.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Methotrexate (Trexall, Rheumatrex)',
        'American College of Rheumatology Guidelines - Methotrexate use',
        'UpToDate - Methotrexate drug information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Methotrexate Monograph'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'A - Dựa trên FDA drug labels, ACR guidelines, và dữ liệu lâm sàng từ nhiều nguồn',
        }}}

__all__ = ['ANTIMETABOLITE_ANTIFOLATES_DRUGS']
