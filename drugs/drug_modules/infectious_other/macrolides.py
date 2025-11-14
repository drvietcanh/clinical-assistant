"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Macrolides

MACROLIDES_DRUGS = {
    "Azithromycin": {'group': 'Infectious Disease - Macrolide Antibiotic', 'vietnamese_name':
        'Azithromycin, Zithromax', 'administration': ['PO', 'IV'],
        'indications': ['Nhiễm trùng đường hô hấp trên (viêm họng, viêm xoang)',
        'Nhiễm trùng đường hô hấp dưới (viêm phổi, viêm phế quản)',
        'Nhiễm trùng da và mô mềm', 'Chlamydia',
        'Nhiễm trùng đường tiết niệu không biến chứng'], 'contraindications': [
        'Dị ứng azithromycin/macrolide', 'QT kéo dài', 'Rối loạn nhịp tim'],
        'dosage': {'adult_respiratory':
        '500mg x 1 lần/ngày x 3 ngày hoặc 500mg ngày đầu, sau đó 250mg x 1 lần/ngày x 4 ngày'
        , 'adult_chlamydia': '1g x 1 lần (đơn liều)', 'adult_iv':
        '500mg x 1 lần/ngày IV', 'notes':
        'Tác dụng kéo dài, uống ít lần hơn erythromycin'}, 'renal_adjustment':
        {'normal': 'Không đổi', '30_60': 'Không đổi', 'under_30': 'Thận trọng'},
        'side_effects': ['Buồn nôn, nôn, tiêu chảy', 'Đau bụng', 'QT kéo dài',
        'Loạn nhịp tim (torsades de pointes)', 'Rối loạn thính giác (hiếm)'],
        'interactions': ['Warfarin: tăng nguy cơ chảy máu',
        'Digoxin: tăng nồng độ digoxin',
        'Cyclosporine: tăng nồng độ cyclosporine',
        'Thuốc QT kéo dài: tăng nguy cơ loạn nhịp'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Macrolide antibiotic. Ức chế tổng hợp protein vi khuẩn bằng cách gắn vào 50S ribosomal subunit, ức chế peptide chain elongation. Phổ tác dụng: Gram-positive (Streptococcus, Staphylococcus), một số Gram-negative (Haemophilus influenzae), atypical pathogens (Mycoplasma, Chlamydia, Legionella). Có tác dụng kéo dài do thời gian bán hủy dài (68 giờ), cho phép phác đồ ngắn (3-5 ngày).'
        , 'monitoring': [
        'ECG: QT interval (có thể gây QT kéo dài, đặc biệt ở bệnh nhân có yếu tố nguy cơ)'
        ,
        'Triệu chứng rối loạn nhịp tim (torsades de pointes - hiếm nhưng nguy hiểm)'
        , 'Chức năng gan: ALT, AST (hiếm gây độc gan)',
        'Triệu chứng tiêu hóa: buồn nôn, nôn, tiêu chảy (phổ biến)',
        'Rối loạn thính giác (hiếm, thường ở liều cao hoặc dùng lâu dài)'],
        'precautions': [
        'Tránh dùng ở bệnh nhân QT kéo dài hoặc có yếu tố nguy cơ (suy tim, hạ kali máu, hạ magie máu, dùng thuốc QT kéo dài khác)'
        ,
        'Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu - theo dõi INR)',
        'Thận trọng khi dùng với digoxin (tăng nồng độ digoxin - theo dõi nồng độ)'
        , 'Thận trọng khi dùng với cyclosporine (tăng nồng độ cyclosporine)',
        'Có thể gây tiêu chảy (phổ biến) - có thể dẫn đến C. difficile colitis nếu nặng'
        , 'Thận trọng ở bệnh nhân suy gan nặng'], 'pharmacokinetics': {
        'half_life': '68 giờ (RẤT DÀI - cho phép phác đồ ngắn 3-5 ngày)',
        'onset': '2-3 giờ (PO), 1 giờ (IV)', 'duration':
        '5-7 ngày sau liều cuối (do half-life dài)', 'protein_binding':
        '7-50% (thay đổi theo nồng độ)', 'clearance':
        'Chủ yếu qua phân (không đổi), một phần qua gan. Không phụ thuộc vào chức năng thận (không cần điều chỉnh liều ở suy thận)'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Bảo quản suspension trong tủ lạnh sau khi pha'
        , 'black_box_warnings':
        'Có thể gây QT kéo dài và torsades de pointes, đặc biệt ở bệnh nhân có yếu tố nguy cơ (suy tim, hạ kali máu, hạ magie máu, nhịp tim chậm, dùng thuốc QT kéo dài khác). Tránh dùng ở bệnh nhân QT kéo dài'
        , 'drug_interactions': {'major': [{'drug': 'Warfarin', 'mechanism':
        'Azithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin. Cũng có thể ức chế nhẹ CYP450.'
        , 'effect': 'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu',
        'management':
        'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng azithromycin. Điều chỉnh liều warfarin nếu cần.'
        }, {'drug': 'Digoxin', 'mechanism':
        'Azithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm chuyển hóa digoxin, tăng hấp thu digoxin.'
        , 'effect':
        'Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)'
        , 'management':
        'Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin nếu cần. Theo dõi ECG.'
        }], 'moderate': [{'drug': 'Cyclosporine, Tacrolimus', 'mechanism':
        'Azithromycin có thể ức chế nhẹ CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus.'
        , 'effect':
        'Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, độc thần kinh)'
        , 'management':
        'Theo dõi nồng độ cyclosporine/tacrolimus, chức năng thận. Điều chỉnh liều nếu cần.'
        }, {'drug': 'Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics)',
        'mechanism': 'Cả hai đều kéo dài QT interval, tác dụng cộng dồn.',
        'effect':
        'Tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng'
        , 'management':
        'TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi ECG chặt chẽ. Đảm bảo kali, magie bình thường. Ngừng ngay nếu QT >500ms hoặc có triệu chứng.'
        }], 'minor': [{'drug': 'Antacids (Aluminum, Magnesium)', 'mechanism':
        'Antacids có thể giảm nhẹ hấp thu azithromycin.', 'effect':
        'Giảm nhẹ hấp thu azithromycin', 'management':
        'Cách 2 giờ nếu có thể. Không ảnh hưởng đáng kể ở liều điều trị thông thường.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng azithromycin hoặc các macrolide khác (erythromycin, clarithromycin)'
        ,
        'QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ torsades de pointes'
        ,
        'Dùng với pimozide, terfenadine, astemizole - tăng nguy cơ loạn nhịp tim nghiêm trọng'
        ], 'tương_đối': [
        'Suy tim - tăng nguy cơ QT kéo dài, torsades de pointes',
        'Hạ kali máu, hạ magie máu - tăng nguy cơ QT kéo dài, torsades de pointes',
        'Nhịp tim chậm - tăng nguy cơ QT kéo dài',
        'Dùng với thuốc kéo dài QT khác - tác dụng cộng dồn',
        'Suy gan nặng - thận trọng, có thể giảm chuyển hóa',
        'Suy thận nặng - thận trọng, mặc dù không cần điều chỉnh liều thường quy'
        ]}, 'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Azithromycin phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Macrolide là một trong những kháng sinh an toàn nhất trong thai kỳ (sau penicillin). Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng, đặc biệt Chlamydia. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Azithromycin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Macrolide là một trong những kháng sinh an toàn nhất khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban).'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Azithromycin chuyển hóa một phần qua gan nhưng không đáng kể.'
        , 'moderate':
        'Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua phân nên ít ảnh hưởng.'
        , 'severe':
        'Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua phân nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần theo dõi chặt chẽ.'
        , 'notes':
        'Azithromycin chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua phân (không đổi), một phần qua gan. Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể do thải trừ chủ yếu qua phân. Không cần điều chỉnh liều thường quy ở suy gan.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng',
        'Triệu chứng tim mạch: QT kéo dài, torsades de pointes, rối loạn nhịp tim (hiếm nhưng nguy hiểm)'
        , 'Triệu chứng thần kinh: Đau đầu, chóng mặt, mệt mỏi',
        'Triệu chứng thính giác: Giảm thính lực, ù tai (hiếm, thường ở liều cao hoặc dùng lâu dài)'
        ,
        'Triệu chứng nghiêm trọng: Torsades de pointes, rối loạn nhịp tim nghiêm trọng, mất thính lực'
        ], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay azithromycin',
        'Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)'
        , 'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG',
        'Điều trị triệu chứng tiêu hóa:', '  - Chống nôn nếu cần',
        '  - Truyền dịch nếu mất nước', '  - Theo dõi điện giải',
        'Điều trị QT kéo dài/torsades de pointes nếu có:',
        '  - Theo dõi ECG liên tục', '  - Đảm bảo kali, magie bình thường',
        '  - Điều trị torsades de pointes: Magnesium sulfate IV, pacing nếu cần',
        '  - Tránh các thuốc kéo dài QT khác',
        'Điều trị rối loạn thính giác nếu có:', '  - Ngừng ngay azithromycin',
        '  - Điều trị hỗ trợ', '  - Có thể không hồi phục',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG'],
        'monitoring':
        'Theo dõi dấu hiệu sinh tồn, ECG (QT interval), điện giải (kali, magie), dấu hiệu thính giác trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (QT kéo dài, torsades de pointes, rối loạn thính giác).'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày và buồn nôn. Có thể uống không thức ăn nếu cần.'
        , 'timing':
        'Uống 1 lần/ngày (phác đồ 3-5 ngày) hoặc theo chỉ định. Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều. Có thể uống trước hoặc sau bữa ăn.'
        }, 'iv': {'reconstitution':
        'Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.'
        , 'infusion_rate':
        'Truyền IV trong 60 phút (không truyền nhanh hơn). Có thể truyền trong 30 phút nếu cần nhưng không khuyến nghị.'
        , 'compatibility': ['NaCl 0.9%', 'D5W (Dextrose 5%)',
        'Nước cất vô trùng'], 'incompatibility': [
        'Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền',
        "Lactated Ringer's (LR) - không tương thích",
        'Các dung dịch có cation (Al3+, Mg2+) - có thể tạo phức hợp'], 'notes':
        'Truyền IV trong 60 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha.'
        }}, 'references': {'primary_sources': [
        'FDA Label: Zithromax (azithromycin)',
        'UpToDate: Azithromycin drug information',
        'Lexicomp: Azithromycin monograph',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Sanford Guide to Antimicrobial Therapy'], 'last_updated': '2025-02-03',
        'evidence_level':
        'Level 1 - FDA approved, multiple clinical trials, extensive clinical experience'
        }},
    "Clarithromycin": {'group': 'Infectious Disease - Macrolide Antibiotic', 'vietnamese_name':
        'Clarithromycin, Klacid', 'administration': ['PO', 'IV'], 'indications':
        ['Nhiễm trùng đường hô hấp (viêm phổi, viêm phế quản)',
        'Nhiễm trùng da và mô mềm', 'Tiệt trừ H. pylori (kết hợp)',
        'Mycobacterium avium complex (MAC)'], 'contraindications': [
        'Dị ứng clarithromycin/macrolide', 'QT kéo dài',
        'Dùng pimozide, terfenadine, astemizole'], 'dosage': {
        'adult_respiratory': '250-500mg x 2 lần/ngày x 7-14 ngày',
        'adult_h_pylori': '500mg x 2 lần/ngày (với amoxicillin + PPI)',
        'adult_mac': '500mg x 2 lần/ngày', 'notes':
        'Mạnh hơn azithromycin nhưng nhiều tương tác hơn'}, 'renal_adjustment':
        {'normal': 'Không đổi', '30_60': 'Giảm liều 50%', 'under_30':
        'Giảm liều 50-75%'}, 'side_effects': ['Buồn nôn, nôn', 'Tiêu chảy',
        'Vị kim loại trong miệng', 'QT kéo dài', 'Rối loạn thính giác (hiếm)'],
        'interactions': [
        'CYP3A4 substrates: tăng đáng kể nồng độ (simvastatin, lovastatin, midazolam)'
        , 'Warfarin: tăng tác dụng chống đông', 'Digoxin: tăng nồng độ digoxin',
        'Theophylline: tăng nồng độ theophylline'], 'pregnancy': 'C',
        'mechanism_of_action':
        'Clarithromycin là kháng sinh macrolide bán tổng hợp, thuộc nhóm azalide. Ức chế tổng hợp protein của vi khuẩn bằng cách gắn vào tiểu đơn vị 50S của ribosome vi khuẩn, ngăn chặn quá trình dịch mã (translocation) và kéo dài chuỗi peptide. Dẫn đến ngừng tổng hợp protein và ức chế sự phát triển của vi khuẩn. Clarithromycin có phổ kháng khuẩn rộng: Gram-dương (Streptococcus pneumoniae, Staphylococcus aureus - không phải MRSA), một số Gram-âm (H. influenzae, Moraxella catarrhalis), và vi khuẩn không điển hình (Mycoplasma pneumoniae, Chlamydia pneumoniae, Legionella pneumophila). Clarithromycin cũng có tác dụng với Helicobacter pylori và một số vi khuẩn không điển hình khác. Mạnh hơn azithromycin nhưng có nhiều tương tác thuốc hơn do ức chế CYP3A4.'
        , 'monitoring': [
        'Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị'
        ,
        'Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm'
        ,
        'ECG - QT kéo dài (đặc biệt ở bệnh nhân có nguy cơ, dùng với thuốc kéo dài QT khác)'
        ,
        'Rối loạn thính giác (giảm thính lực, ù tai) - hiếm nhưng có thể không hồi phục'
        , 'Chức năng gan (ALT, AST) nếu dùng lâu dài hoặc có triệu chứng',
        'Chức năng thận (creatinine) - điều chỉnh liều ở suy thận',
        'Tương tác với CYP3A4 substrates (simvastatin, lovastatin, midazolam, warfarin, digoxin, theophylline) - theo dõi tác dụng phụ và nồng độ nếu có'
        ], 'precautions': [
        'QT kéo dài - không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp'
        ,
        'Không dùng với pimozide, terfenadine, astemizole (tăng nguy cơ loạn nhịp nghiêm trọng)'
        ,
        'Nhiều tương tác thuốc do ức chế CYP3A4 - tăng nồng độ simvastatin, lovastatin (nguy cơ tiêu cơ vân), midazolam, warfarin (tăng INR), digoxin (tăng nồng độ), theophylline (tăng nồng độ)'
        , 'Giảm liều ở suy thận (CrCl <30: giảm 50-75%)',
        'Uống với thức ăn để giảm buồn nôn, nôn',
        'Rối loạn thính giác - ngừng ngay nếu có giảm thính lực, ù tai (có thể không hồi phục)'
        , 'Vị kim loại trong miệng - tác dụng phụ phổ biến, thường tự khỏi',
        'Thận trọng ở bệnh nhân có bệnh gan (metabolite qua gan)',
        'Dùng đủ liều và đủ thời gian để tránh kháng thuốc'],
        'pharmacokinetics': {'half_life': '3-7 giờ (tăng ở suy thận)', 'onset':
        '2-4 giờ', 'duration': 'q12h (dùng 2 lần/ngày)', 'protein_binding':
        '70%', 'clearance':
        'Gan: chuyển hóa qua CYP3A4 thành 14-hydroxyclarithromycin (metabolite hoạt động, mạnh hơn với H. influenzae). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều ở suy thận (CrCl <30).'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 14 ngày sau khi pha. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha.'
        , 'black_box_warnings':
        'Tăng nguy cơ tử vong do tim mạch ở bệnh nhân có bệnh tim mạch. Không dùng ở bệnh nhân có QT kéo dài, loạn nhịp tim, hoặc dùng với các thuốc kéo dài QT. Tăng nguy cơ tiêu cơ vân khi dùng với simvastatin, lovastatin.'
        , 'drug_interactions': {'major': [{'drug': 'Simvastatin, Lovastatin',
        'mechanism':
        'Clarithromycin ức chế mạnh CYP3A4, làm giảm chuyển hóa simvastatin và lovastatin.'
        , 'effect':
        'Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân (myopathy, rhabdomyolysis), suy thận cấp'
        , 'management':
        'TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều statin hoặc tạm ngừng. Dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4) nếu có thể. Theo dõi CK, dấu hiệu đau cơ.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Clarithromycin ức chế CYP2C9 và CYP3A4, làm giảm chuyển hóa warfarin.',
        'effect':
        'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng',
        'management':
        'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng clarithromycin. Giảm liều warfarin 25-50% khi bắt đầu clarithromycin. Điều chỉnh liều warfarin theo INR.'
        }, {'drug': 'Digoxin', 'mechanism':
        'Clarithromycin ức chế P-glycoprotein và ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu và giảm thải trừ digoxin.'
        , 'effect':
        'Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)'
        , 'management':
        'Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin 25-50% khi bắt đầu clarithromycin. Theo dõi ECG.'
        }, {'drug': 'Pimozide, Terfenadine, Astemizole', 'mechanism':
        'Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa pimozide, terfenadine, astemizole. Cả hai đều kéo dài QT interval.'
        , 'effect':
        'Tăng nồng độ thuốc, tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng, tử vong'
        , 'management': 'CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng đồng thời.'}],
        'moderate': [{'drug': 'Midazolam, Triazolam', 'mechanism':
        'Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa benzodiazepine.',
        'effect':
        'Tăng nồng độ benzodiazepine, tăng tác dụng an thần, kéo dài thời gian tác dụng'
        , 'management':
        'Giảm liều benzodiazepine 50-75%. Theo dõi dấu hiệu an thần quá mức, suy hô hấp.'
        }, {'drug': 'Theophylline', 'mechanism':
        'Clarithromycin có thể ảnh hưởng đến chuyển hóa theophylline.',
        'effect':
        'Tăng nồng độ theophylline, tăng độc tính (buồn nôn, nôn, co giật, rối loạn nhịp tim)'
        , 'management':
        'Theo dõi nồng độ theophylline. Giảm liều theophylline nếu cần. Theo dõi dấu hiệu độc tính.'
        }, {'drug': 'Cyclosporine, Tacrolimus', 'mechanism':
        'Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus.'
        , 'effect':
        'Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, độc thần kinh)'
        , 'management':
        'Giảm liều cyclosporine/tacrolimus 25-50% khi bắt đầu clarithromycin. Theo dõi nồng độ, chức năng thận. Điều chỉnh liều theo nồng độ.'
        }, {'drug': 'Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics)',
        'mechanism': 'Cả hai đều kéo dài QT interval, tác dụng cộng dồn.',
        'effect':
        'Tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng'
        , 'management':
        'TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi ECG chặt chẽ. Đảm bảo kali, magie bình thường. Ngừng ngay nếu QT >500ms hoặc có triệu chứng.'
        }], 'minor': [{'drug': 'Rifampin', 'mechanism':
        'Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa clarithromycin.',
        'effect': 'Giảm nồng độ clarithromycin, giảm hiệu quả điều trị',
        'management':
        'Tăng liều clarithromycin nếu cần. Theo dõi đáp ứng điều trị.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng clarithromycin hoặc các macrolide khác (erythromycin, azithromycin)'
        ,
        'QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ tử vong do tim mạch'
        ,
        'Dùng với pimozide, terfenadine, astemizole - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI, tăng nguy cơ loạn nhịp tim nghiêm trọng, tử vong'
        , 'Bệnh tim mạch nặng - tăng nguy cơ tử vong do tim mạch'], 'tương_đối':
        ['Suy tim - tăng nguy cơ QT kéo dài, tử vong do tim mạch',
        'Hạ kali máu, hạ magie máu - tăng nguy cơ QT kéo dài, torsades de pointes',
        'Dùng với thuốc kéo dài QT khác - tác dụng cộng dồn',
        'Dùng với simvastatin, lovastatin - tăng nguy cơ tiêu cơ vân',
        'Dùng với warfarin - tăng nguy cơ chảy máu',
        'Dùng với digoxin - tăng độc tính digoxin',
        'Suy thận nặng (CrCl <30) - cần giảm liều 50-75%',
        'Suy gan - thận trọng, có thể giảm chuyển hóa']}, 'pregnancy_lactation':
        {'fda_category': 'C', 'pregnancy_details':
        'Clarithromycin phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ (giảm cân, chậm phát triển xương). Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng, nhưng dữ liệu còn hạn chế. Macrolide nói chung an toàn hơn nhiều kháng sinh khác trong thai kỳ. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị H. pylori hoặc nhiễm trùng nặng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết. Azithromycin có thể là lựa chọn an toàn hơn trong thai kỳ (phân loại B).'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Clarithromycin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Macrolide là một trong những kháng sinh an toàn nhất khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban).'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Clarithromycin chuyển hóa qua gan nhưng không đáng kể ở suy gan nhẹ.'
        , 'moderate':
        'Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.'
        , 'severe':
        'Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng nồng độ clarithromycin và nguy cơ tác dụng phụ.'
        , 'notes':
        'Clarithromycin chuyển hóa qua CYP3A4 thành 14-hydroxyclarithromycin (metabolite hoạt động). Suy gan có thể giảm chuyển hóa, tăng nồng độ clarithromycin. Tuy nhiên, thải trừ một phần qua thận nên cần điều chỉnh liều theo cả chức năng gan và thận. Theo dõi chặt chẽ tác dụng phụ ở suy gan.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng, vị kim loại trong miệng'
        ,
        'Triệu chứng tim mạch: QT kéo dài, torsades de pointes, rối loạn nhịp tim, tử vong do tim mạch (hiếm nhưng nguy hiểm)'
        , 'Triệu chứng thần kinh: Đau đầu, chóng mặt, mệt mỏi',
        'Triệu chứng thính giác: Giảm thính lực, ù tai (hiếm, có thể không hồi phục)'
        ,
        'Triệu chứng nghiêm trọng: Torsades de pointes, rối loạn nhịp tim nghiêm trọng, tử vong do tim mạch, mất thính lực'
        ], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay clarithromycin',
        'Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)'
        , 'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG',
        'Điều trị triệu chứng tiêu hóa:', '  - Chống nôn nếu cần',
        '  - Truyền dịch nếu mất nước', '  - Theo dõi điện giải',
        'Điều trị QT kéo dài/torsades de pointes nếu có:',
        '  - Theo dõi ECG liên tục', '  - Đảm bảo kali, magie bình thường',
        '  - Điều trị torsades de pointes: Magnesium sulfate IV, pacing nếu cần',
        '  - Tránh các thuốc kéo dài QT khác',
        'Điều trị rối loạn thính giác nếu có:', '  - Ngừng ngay clarithromycin',
        '  - Điều trị hỗ trợ', '  - Có thể không hồi phục',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG'],
        'monitoring':
        'Theo dõi dấu hiệu sinh tồn, ECG (QT interval), điện giải (kali, magie), dấu hiệu thính giác trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (QT kéo dài, torsades de pointes, rối loạn thính giác).'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống với thức ăn để giảm kích ứng dạ dày, giảm buồn nôn, nôn. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.'
        , 'timing':
        'Uống 2 lần/ngày (q12h), thường 250-500mg x 2 lần/ngày. Uống đều đặn, cách đều nhau trong ngày (12 giờ). Không bỏ liều.'
        }, 'iv': {'reconstitution':
        'Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.'
        , 'infusion_rate':
        'Truyền IV trong 60 phút (không truyền nhanh hơn). Có thể truyền trong 30 phút nếu cần nhưng không khuyến nghị.'
        , 'compatibility': ['NaCl 0.9%', 'D5W (Dextrose 5%)',
        'Nước cất vô trùng'], 'incompatibility': [
        'Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền',
        "Lactated Ringer's (LR) - không tương thích",
        'Các dung dịch có cation (Al3+, Mg2+) - có thể tạo phức hợp'], 'notes':
        'Truyền IV trong 60 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha.'
        }}, 'references': {'primary_sources': [
        'FDA Label: Klacid (clarithromycin)',
        'UpToDate: Clarithromycin drug information',
        'Lexicomp: Clarithromycin monograph',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Sanford Guide to Antimicrobial Therapy'], 'last_updated': '2025-02-03',
        'evidence_level':
        'Level 1 - FDA approved, multiple clinical trials, extensive clinical experience'
        }}}

__all__ = ['MACROLIDES_DRUGS']
