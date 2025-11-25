"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Analgesic/Antipyretic/NSAID

ANALGESIC/ANTIPYRETIC/NSAID_DRUGS = {
    "Ibuprofen": {'group': 'Analgesic/Antipyretic/NSAID', 'vietnamese_name':
        'Ibuprofen, Brufen, Advil', 'administration': ['PO', 'IV'],
        'indications': ['Sốt', 'Đau nhẹ đến trung bình', 'Viêm khớp',
        'Đau bụng kinh', 'Đau đầu'], 'contraindications': ['Dị ứng NSAID',
        'Loét dạ dày tá tràng hoạt động', 'Suy thận nặng', 'Suy tim nặng',
        'Có thai (3 tháng cuối)', 'Trẻ em <6 tháng'], 'dosage': {'adult_po':
        '200-400mg x 3-4 lần/ngày (tối đa 2.4g/ngày)', 'adult_iv':
        '400-800mg IV mỗi 6 giờ', 'pediatric_po':
        '5-10mg/kg x 3-4 lần/ngày (tối đa 40mg/kg/ngày)',
        'pediatric_suspension': 'Có dạng suspension 100mg/5ml cho trẻ em',
        'notes':
        'Uống với thức ăn để giảm kích ứng dạ dày. Không dùng quá 10 ngày không có chỉ định'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, có thể cần giảm liều', 'under_30':
        'Không dùng hoặc giảm liều đáng kể'}, 'side_effects': [
        'Kích ứng dạ dày', 'Đau đầu', 'Chóng mặt',
        'Tăng nguy cơ tim mạch (với dùng lâu dài)', 'Suy thận cấp (hiếm)',
        'Phát ban'], 'interactions': ['Aspirin: có thể giảm hiệu quả aspirin',
        'Warfarin: tăng nguy cơ chảy máu', 'Lithium: tăng nồng độ lithium',
        'Methotrexate: tăng độc tính', 'ACE inhibitors: giảm hiệu quả'],
        'pregnancy': 'C - Tránh dùng trong 3 tháng cuối (D)',
        'mechanism_of_action':
        'Ibuprofen ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), làm giảm tổng hợp prostaglandin, thromboxane A2, và prostacyclin từ acid arachidonic. Prostaglandin tham gia vào quá trình viêm, đau, sốt, và điều hòa thận. Thromboxane A2 gây kết tập tiểu cầu và co mạch. Ức chế COX-1 làm giảm prostaglandin bảo vệ niêm mạc dạ dày và ảnh hưởng đến chức năng thận. Ức chế COX-2 chủ yếu giảm viêm và đau. Ibuprofen là NSAID không chọn lọc, có tác dụng kháng viêm, giảm đau, và hạ sốt. Tác dụng kháng viêm mạnh hơn paracetamol nhưng có nhiều tác dụng phụ hơn, đặc biệt là kích ứng dạ dày và ảnh hưởng đến thận.'
        , 'monitoring': [
        'Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng, thiếu máu)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ suy thận (tuổi cao, tiểu đường, tăng huyết áp)'
        ,
        'Huyết áp (NSAID có thể tăng huyết áp, đặc biệt ở bệnh nhân tăng huyết áp đang điều trị)'
        , 'Chức năng gan (ALT, AST) nếu dùng lâu dài hoặc có triệu chứng',
        'Dấu hiệu suy tim (giữ nước, phù, khó thở) - NSAID có thể làm nặng suy tim'
        , 'INR nếu dùng với warfarin (tăng nguy cơ chảy máu)',
        'Triệu chứng tim mạch (đau ngực, khó thở) - tăng nguy cơ tim mạch với dùng lâu dài'
        ], 'precautions': ['Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Cân nhắc dùng PPI (omeprazole, pantoprazole) hoặc misoprostol nếu có nguy cơ loét dạ dày (tuổi >65, tiền sử loét, dùng corticosteroid, dùng aspirin)'
        ,
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp (làm nặng bệnh)'
        ,
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp)'
        ,
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm, tăng nguy cơ chảy máu ở mẹ và con)'
        , 'Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể',
        'Thận trọng ở bệnh nhân >65 tuổi (tăng nguy cơ tác dụng phụ)',
        'Tránh dùng với aspirin liều thấp (có thể giảm hiệu quả bảo vệ tim mạch của aspirin)'
        , 'Thận trọng với bệnh nhân hen suyễn (có thể gây co thắt phế quản)',
        'Không dùng quá 10 ngày cho đau hoặc sốt mà không có chỉ định rõ ràng'],
        'pharmacokinetics': {'half_life': '2-4 giờ', 'onset':
        '30-60 phút (PO), 15-30 phút (IV)', 'duration': '4-6 giờ',
        'protein_binding': '>99% (gắn chặt với albumin)', 'clearance':
        'Gan: chuyển hóa qua CYP2C9 và CYP2C8 thành hydroxy và carboxy metabolites (không hoạt động). Thận: bài tiết <1% nguyên dạng, chủ yếu là metabolites. Thời gian bán thải tăng ở suy thận và suy gan.'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha.'
        , 'black_box_warnings':
        'Tăng nguy cơ biến cố tim mạch nghiêm trọng (nhồi máu cơ tim, đột quỵ) có thể xảy ra sớm và tăng nguy cơ tử vong. Nguy cơ tăng ở bệnh nhân có bệnh tim mạch hoặc các yếu tố nguy cơ tim mạch. NSAID tăng nguy cơ xuất huyết tiêu hóa, loét, thủng dạ dày có thể gây tử vong. Nguy cơ tăng ở người cao tuổi, tiền sử loét, dùng corticosteroid, aspirin, rượu, hút thuốc. Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm).'
        , 'drug_interactions': {'major': [{'drug': 'Warfarin', 'mechanism':
        'Ibuprofen ức chế kết tập tiểu cầu và có thể tăng nguy cơ chảy máu. Có thể ảnh hưởng đến chuyển hóa warfarin.'
        , 'effect': 'Tăng nguy cơ chảy máu nghiêm trọng, tăng INR',
        'management':
        'Theo dõi INR chặt chẽ. Tránh dùng đồng thời nếu có thể. Nếu cần dùng, giảm liều ibuprofen và theo dõi dấu hiệu chảy máu.'
        }, {'drug': 'ACE Inhibitors, ARB', 'mechanism':
        'NSAID giảm tổng hợp prostaglandin, làm giảm tác dụng giãn mạch của ACE inhibitor/ARB. Có thể gây giữ natri và nước.'
        , 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp, tăng kali máu',
        'management':
        'Tránh dùng đồng thời nếu có thể. Nếu cần, theo dõi creatinine, BUN, kali máu. Cân nhắc dùng liều thấp NSAID và thời gian ngắn.'
        }, {'drug': 'Aspirin (liều thấp tim mạch)', 'mechanism':
        'Ibuprofen có thể cạnh tranh với aspirin tại vị trí gắn COX-1, làm giảm tác dụng ức chế kết tập tiểu cầu của aspirin.'
        , 'effect': 'Giảm hiệu quả bảo vệ tim mạch của aspirin', 'management':
        'Nếu dùng aspirin liều thấp để bảo vệ tim mạch, dùng ibuprofen ít nhất 30 phút sau aspirin hoặc 8 giờ trước aspirin. Hoặc cân nhắc dùng NSAID khác không ức chế COX-1.'
        }], 'moderate': [{'drug': 'Methotrexate', 'mechanism':
        'NSAID giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate trong máu.'
        , 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy xương, độc gan)',
        'management':
        'Tránh dùng với liều cao methotrexate. Nếu dùng liều thấp, theo dõi công thức máu, chức năng gan. Có thể cần giảm liều methotrexate.'
        }, {'drug': 'Lithium', 'mechanism':
        'NSAID giảm thải trừ lithium qua thận, tăng nồng độ lithium.', 'effect':
        'Tăng nồng độ lithium, tăng nguy cơ độc tính lithium', 'management':
        'Theo dõi nồng độ lithium trong máu. Có thể cần giảm liều lithium khi bắt đầu dùng ibuprofen.'
        }, {'drug': 'Corticosteroid', 'mechanism':
        'Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.', 'effect':
        'Tăng nguy cơ xuất huyết tiêu hóa, loét dạ dày', 'management':
        'Cân nhắc dùng PPI hoặc misoprostol. Theo dõi dấu hiệu chảy máu dạ dày.'
        }], 'minor': [{'drug': 'Furosemide, Thiazide', 'mechanism':
        'NSAID giảm tác dụng lợi tiểu, có thể gây giữ natri và nước.', 'effect':
        'Giảm hiệu quả lợi tiểu, có thể gây phù', 'management':
        'Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng NSAID hoặc aspirin (quá mẫn cảm, phản ứng dị ứng nghiêm trọng)',
        'Loét dạ dày tá tràng hoạt động', 'Xuất huyết tiêu hóa đang hoạt động',
        'Suy thận nặng (CrCl <30 ml/min) hoặc đang lọc máu',
        'Suy gan nặng (Child-Pugh C)', 'Suy tim nặng (NYHA class IV)',
        'Có thai (3 tháng cuối) - đóng ống động mạch sớm',
        'Trẻ em <6 tháng tuổi'], 'tương_đối': [
        'Suy thận nhẹ đến trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, giảm liều',
        'Suy tim nhẹ đến trung bình (NYHA class II-III) - có thể làm nặng',
        'Tăng huyết áp không kiểm soát - có thể tăng huyết áp',
        'Tiền sử loét dạ dày - tăng nguy cơ loét',
        'Bệnh tim mạch hoặc yếu tố nguy cơ tim mạch - tăng nguy cơ biến cố tim mạch'
        ,
        'Hen suyễn - có thể gây co thắt phế quản (đặc biệt ở bệnh nhân nhạy cảm với aspirin)'
        , 'Người cao tuổi (>65) - tăng nguy cơ tác dụng phụ',
        'Có thai (1-2 tam cá nguyệt đầu) - thận trọng, chỉ dùng khi thực sự cần thiết'
        ]}, 'pregnancy_lactation': {'fda_category':
        'C (1-2 tam cá nguyệt), D (3 tam cá nguyệt cuối)', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Thuốc phân loại C. Có thể dùng khi lợi ích vượt quá nguy cơ, nhưng nên tránh nếu không cần thiết. Một số nghiên cứu gợi ý tăng nguy cơ dị tật tim và thành bụng khi dùng trong tam cá nguyệt đầu. Tam cá nguyệt 3: Thuốc phân loại D - CHỐNG CHỈ ĐỊNH. NSAID ức chế tổng hợp prostaglandin, có thể gây đóng ống động mạch sớm ở thai nhi, thiểu ối, suy thận thai nhi, tăng nguy cơ chảy máu ở mẹ và con. Không dùng từ tuần 30 trở đi.'
        , 'lactation': {'safety': 'Compatible (với dùng ngắn hạn)', 'details':
        'Ibuprofen bài tiết vào sữa mẹ ở nồng độ rất thấp (<0.6% liều mẹ). Nồng độ trong sữa mẹ thấp và thời gian bán thải ngắn (2-4 giờ). Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng lâu dài.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Theo dõi chức năng gan nếu dùng lâu dài.',
        'moderate':
        'Thận trọng, giảm liều 25-50%. Tối đa 1.2g/ngày. Theo dõi ALT, AST thường xuyên.'
        , 'severe':
        'Tránh dùng hoặc dùng liều rất thấp (600-800mg/ngày) dưới sự giám sát chặt chẽ. Theo dõi ALT, AST, bilirubin thường xuyên. Chuyển hóa qua gan có thể giảm ở suy gan nặng.'
        , 'notes':
        'Ibuprofen chuyển hóa chủ yếu qua gan (CYP2C9, CYP2C8). Suy gan có thể làm giảm chuyển hóa, tăng thời gian bán thải. Thận trọng ở bệnh nhân nghiện rượu hoặc viêm gan.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng sớm (1-4 giờ): Buồn nôn, nôn, đau bụng, chóng mặt, buồn ngủ, đau đầu'
        ,
        'Triệu chứng muộn (4-24 giờ): Chảy máu dạ dày, suy thận cấp, rối loạn điện giải, toan chuyển hóa'
        ,
        'Triệu chứng nghiêm trọng: Hạ huyết áp, sốc, suy hô hấp, co giật, hôn mê (hiếm)'
        ,
        'Triệu chứng tim mạch: Rối loạn nhịp tim, suy tim cấp (với liều rất cao)'
        ], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': [
        'Đánh giá nguy cơ: Liều >100mg/kg (Trẻ Em) hoặc >7.5g (Người Lớn) = nguy cơ cao'
        ,
        'Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)'
        , 'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2',
        'Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải, điều trị toan chuyển hóa nếu có'
        , 'Theo dõi chức năng thận: Creatinine, BUN, nước tiểu',
        'Theo dõi chức năng gan: ALT, AST, bilirubin',
        'Theo dõi dấu hiệu chảy máu: Công thức máu, INR, PTT nếu có',
        'Điều trị xuất huyết tiêu hóa nếu có: PPI, truyền máu nếu cần',
        'Điều trị suy thận cấp nếu có: Điều chỉnh dịch, lọc máu nếu cần',
        'Hỗ trợ hô hấp nếu có suy hô hấp',
        'Điều trị co giật nếu có: Benzodiazepine'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, chức năng thận, chức năng gan, công thức máu, dấu hiệu chảy máu trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng.'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.'
        , 'timing':
        'Uống 3-4 lần/ngày, cách đều. Có thể uống với hoặc sau bữa ăn. Không uống khi đói.'
        }, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W. Nồng độ pha: 4mg/ml (tối đa). Pha 800mg trong 200ml dịch = 4mg/ml. Pha 400mg trong 100ml dịch = 4mg/ml.'
        , 'infusion_rate':
        'Truyền trong 30 phút. Không truyền quá nhanh. Tốc độ: 400mg/100ml = 200ml/30 phút = ~6.7ml/phút. 800mg/200ml = 200ml/30 phút = ~6.7ml/phút.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)',
        'Lactated Ringer'], 'incompatibility': [
        'Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha.'
        ], 'notes':
        'Không dùng cho trẻ em <12 tuổi qua đường IV. Theo dõi dấu hiệu phản ứng dị ứng và tác dụng phụ trong quá trình truyền.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Ibuprofen (Advil, Motrin)',
        'UpToDate - Ibuprofen: Drug Information',
        'Medscape - Ibuprofen Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Ibuprofen Monograph',
        'Micromedex - Ibuprofen Drug Information'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }}}

__all__ = ['ANALGESIC/ANTIPYRETIC/NSAID_DRUGS']
