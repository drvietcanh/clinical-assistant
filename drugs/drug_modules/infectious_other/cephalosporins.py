"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Cephalosporins

CEPHALOSPORINS_DRUGS = {
    "Ceftriaxone": {'group': 'Antibiotic - Cephalosporin (3rd Generation)', 'vietnamese_name':
        'Ceftriaxone, Rocephin', 'administration': ['IV', 'IM'], 'indications':
        ['Nhiễm khuẩn nặng', 'Viêm màng não', 'Nhiễm khuẩn bệnh viện',
        'Nhiễm khuẩn đường tiết niệu', 'Viêm phổi'], 'contraindications': [
        'Dị ứng cephalosporin hoặc penicillin (thận trọng)',
        'Trẻ sơ sinh <28 ngày với Ca IV'], 'dosage': {'adult_standard':
        '1-2g IV/IM mỗi 24 giờ', 'adult_severe': '2-4g IV mỗi 24 giờ',
        'adult_meningitis': '2g IV mỗi 12 giờ', 'pediatric_standard':
        '50-75mg/kg IV/IM mỗi 24 giờ (tối đa 2g)', 'pediatric_meningitis':
        '80-100mg/kg IV mỗi 12-24 giờ (tối đa 4g/ngày)', 'notes':
        'Thời gian bán hủy dài, dùng 1 lần/ngày. Có thể gây kết tủa với Ca ở trẻ sơ sinh'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Không đổi (thải qua mật)', 'under_30':
        'Giảm liều nếu CrCl <10 và suy gan'}, 'side_effects': ['Tiêu chảy',
        'Phát ban', 'Tăng transaminase', 'Viêm túi mật (hiếm)',
        'Giảm bạch cầu (hiếm)', 'Sỏi mật (với liều cao dài ngày)'],
        'interactions': ['Warfarin: tăng INR',
        'Calcium IV: kết tủa (trẻ sơ sinh)',
        'Probenecid: tăng nồng độ ceftriaxone'], 'pregnancy': 'B - An toàn',
        'mechanism_of_action':
        'Cephalosporin thế hệ 3, phổ rộng. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (một số), Gram-âm mạnh (Enterobacteriaceae, Neisseria, H. influenzae), và một số kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Không hiệu quả với Pseudomonas aeruginosa, Enterococcus, hoặc MRSA. Thời gian bán thải dài (6-9 giờ) → chỉ cần tiêm 1 lần/ngày.'
        , 'monitoring': ['Dấu hiệu nhiễm trùng (sốt, WBC, CRP)',
        'Cấy máu và cấy từ vị trí nhiễm trùng',
        'Chức năng gan (ALT, AST, bilirubin) - có thể tăng, hiếm sỏi mật',
        'Sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao',
        'Chức năng thận (creatinine) - không cần điều chỉnh thận nhưng theo dõi',
        'Dấu hiệu nhiễm C. difficile',
        'Co giật (hiếm, nhưng có thể ở suy thận nặng)',
        'Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)'], 'precautions': [
        'KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV (nguy cơ kết tủa ceftriaxone-calcium trong phổi, thận) - có thể tử vong'
        ,
        'Nguy cơ sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao, dùng kéo dài'
        ,
        'Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~5-10%)'
        , 'Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy',
        'Có thể gây tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin)',
        'Pha trong NS, D5W, hoặc LR, tiêm IV hoặc IM',
        'Tiêm IM: pha với lidocaine 1% để giảm đau',
        'Không pha trộn với các thuốc khác (tương kỵ với nhiều thuốc, đặc biệt vancomycin, calcium)'
        ,
        'Thời gian bán thải dài → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h)'
        ], 'pharmacokinetics': {'half_life':
        '6-9 giờ (rất dài cho cephalosporin)', 'onset':
        'Ngay lập tức sau khi tiêm IV', 'duration':
        '24 giờ (liều 1-2g q24h), 12 giờ (viêm màng não: 2g q12h)',
        'protein_binding': '85-95% (rất cao)', 'metabolism':
        'Không chuyển hóa, bài tiết nguyên dạng', 'clearance':
        '40% qua thận, 60% qua mật (độc nhất trong cephalosporin) → không cần điều chỉnh thận'
        }, 'storage':
        'Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày. Không đông lạnh.'
        , 'black_box_warnings':
        'KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV - có thể gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh.'
        , 'drug_interactions': {'major': [{'drug':
        'Calcium IV (đặc biệt ở trẻ sơ sinh < 28 ngày)', 'mechanism':
        'Ceftriaxone tạo phức hợp không hòa tan với calci, gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong.'
        , 'effect':
        'Kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong (đặc biệt ở trẻ sơ sinh)'
        , 'management':
        'CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI: Không dùng ceftriaxone ở trẻ sơ sinh < 28 ngày nếu đang dùng calci IV. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh. Ở người lớn, tránh pha chung trong cùng một ống truyền, truyền riêng biệt.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Ceftriaxone có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể đẩy warfarin khỏi albumin (protein binding cao).'
        , 'effect': 'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng ceftriaxone). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày).'
        }], 'moderate': [{'drug': 'Probenecid', 'mechanism':
        'Probenecid ức chế bài tiết ống thận của ceftriaxone, làm giảm thải trừ và tăng nồng độ ceftriaxone.'
        , 'effect': 'Tăng nồng độ ceftriaxone, tăng thời gian bán thải',
        'management':
        'Có thể cần giảm liều ceftriaxone. Theo dõi chức năng thận. Thường không cần điều chỉnh liều thường quy do ceftriaxone thải trừ chủ yếu qua mật.'
        }, {'drug': 'Vancomycin', 'mechanism':
        'Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.'
        , 'effect': 'Kết tủa khi pha chung, tăng nguy cơ độc thận',
        'management':
        'Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ. Theo dõi nồng độ vancomycin nếu có thể.'
        }, {'drug': 'Aminoglycosides (Gentamicin, Tobramycin, Amikacin)',
        'mechanism':
        'Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.'
        , 'effect': 'Kết tủa khi pha chung, tăng nguy cơ độc thận',
        'management':
        'Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ.'
        }], 'minor': [{'drug': 'Thuốc tránh thai đường uống', 'mechanism':
        'Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.'
        , 'effect':
        'Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)',
        'management':
        'Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)'
        ,
        'Trẻ sơ sinh < 28 ngày tuổi đang dùng calci IV - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (nguy cơ kết tủa tử vong)'
        ], 'tương_đối': [
        'Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng, có thể dùng nếu phản ứng nhẹ'
        , 'Suy gan nặng kèm suy thận (CrCl <10) - cần giảm liều',
        'Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát',
        'Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin',
        'Sỏi mật - tăng nguy cơ sỏi mật (ceftriaxone-calcium complex), đặc biệt ở trẻ em, dùng liều cao'
        ]}, 'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Ceftriaxone là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Cephalosporins nói chung được coi là an toàn trong thai kỳ và được sử dụng rộng rãi. Ceftriaxone có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm khuẩn nặng như viêm màng não. Tuy nhiên, cần thận trọng với nguy cơ sỏi mật và tương tác với calci. Nên tránh dùng kéo dài nếu có thể.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ceftriaxone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Cephalosporins nói chung được coi là an toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Ceftriaxone thải trừ 40% qua thận, 60% qua mật, không chuyển hóa qua gan.'
        , 'moderate':
        'Không cần điều chỉnh liều. Tuy nhiên, cần thận trọng với nguy cơ tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin).'
        , 'severe':
        'Không cần điều chỉnh liều. Tuy nhiên, nếu kèm theo suy thận nặng (CrCl <10), có thể cần giảm liều. Theo dõi bilirubin và chức năng gan.'
        , 'notes':
        'Ceftriaxone không chuyển hóa qua gan, thải trừ 40% qua thận và 60% qua mật (độc nhất trong cephalosporin). Không cần điều chỉnh liều ở bệnh nhân suy gan. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận nếu CrCl <10. Ngoài ra, ceftriaxone có protein binding cao (85-95%), có thể đẩy bilirubin khỏi albumin, gây tăng bilirubin nhất thời.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao hoặc suy thận nặng)'
        , 'Triệu chứng gan: Tăng bilirubin, tăng transaminase (nhất thời)',
        'Triệu chứng sỏi mật: Đau bụng, buồn nôn, nôn (do kết tủa ceftriaxone-calcium)'
        , 'Triệu chứng thận: Suy thận cấp (hiếm với liều thông thường)',
        'Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn',
        'Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)',
        'Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)'
        ], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay ceftriaxone',
        'Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital'
        , 'Điều trị sỏi mật nếu có:', '  - Giảm đau: NSAID hoặc opioid',
        '  - Bù dịch đầy đủ', '  - Theo dõi siêu âm bụng',
        '  - Có thể cần can thiệp nếu tắc nghẽn', 'Điều trị chảy máu nếu có:',
        '  - Bổ sung vitamin K nếu giảm prothrombin',
        '  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng',
        '  - Điều chỉnh liều warfarin nếu đang dùng',
        'Điều trị suy thận cấp nếu có:', '  - Bù dịch đầy đủ',
        '  - Điều chỉnh điện giải',
        '  - Lọc máu nếu cần (hemodialysis có thể loại bỏ ceftriaxone một phần)',
        'Điều trị dị ứng nếu có:', '  - Epinephrine nếu sốc phản vệ',
        '  - Antihistamine, corticosteroid', '  - Hỗ trợ hô hấp nếu cần',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2',
        'Lọc máu: Hemodialysis có thể loại bỏ ceftriaxone một phần (40% thải qua thận), nhưng không hiệu quả bằng các cephalosporin khác do thải trừ chủ yếu qua mật.'
        ], 'monitoring':
        'Theo dõi dấu hiệu thần kinh (co giật, ý thức), chức năng gan (bilirubin, ALT, AST), dấu hiệu sỏi mật (đau bụng), chức năng thận (creatinine, BUN, lượng nước tiểu), PT/INR (nếu dùng với warfarin), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có suy thận cấp hoặc sỏi mật.'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food': 'Không áp dụng - chỉ có dạng IV và IM', 'timing':
        'Không áp dụng - chỉ có dạng IV và IM'}, 'iv': {'reconstitution':
        "Pha với NS (0.9% NaCl), D5W (5% Dextrose), hoặc Ringer's Lactate. Nồng độ pha: 10-40mg/ml. Pha 1g trong 10ml = 100mg/ml (quá đậm, không dùng). Pha 1g trong 50ml = 20mg/ml. Pha 2g trong 50ml = 40mg/ml. Lắc kỹ để hòa tan hoàn toàn. KHÔNG pha với calci IV."
        , 'infusion_rate':
        'Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút. Có thể truyền nhanh hơn (bolus) nếu cần, nhưng thường truyền trong 30 phút để giảm đau tại chỗ.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)',
        "Ringer's Lactate"], 'incompatibility': [
        'Calcium IV - KHÔNG pha chung, nguy cơ kết tủa tử vong (đặc biệt ở trẻ sơ sinh)'
        , 'Vancomycin - tạo kết tủa, không pha chung',
        'Aminoglycosides - có thể tạo kết tủa, truyền riêng biệt',
        'Amphotericin B - không tương thích',
        'Các thuốc có tính kiềm hoặc acid mạnh'], 'notes':
        'QUAN TRỌNG: 1) KHÔNG pha chung với calci IV (nguy cơ kết tủa tử vong ở trẻ sơ sinh), 2) Không pha chung với vancomycin hoặc aminoglycosides, 3) Thời gian bán thải dài (6-9 giờ) → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h), 4) Tiêm IM: pha với lidocaine 1% để giảm đau, 5) Theo dõi sỏi mật ở trẻ em, dùng liều cao, dùng kéo dài.'
        }, 'im': {'reconstitution':
        'Pha với lidocaine 1% (không có epinephrine) để giảm đau. Nồng độ pha: 250mg/ml (1g trong 3.5ml lidocaine 1%). Pha 1g trong 3.5ml lidocaine 1% = 250mg/ml. Lắc kỹ để hòa tan hoàn toàn.'
        , 'injection_site':
        'Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis). Tránh tiêm vào mạch máu.'
        , 'notes':
        'Pha với lidocaine 1% để giảm đau tại chỗ. Tiêm sâu vào cơ. Có thể gây đau tại chỗ, nhưng thường nhẹ khi pha với lidocaine.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Ceftriaxone (Rocephin)',
        'UpToDate - Ceftriaxone: Drug Information',
        'Medscape - Ceftriaxone Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Ceftriaxone Monograph',
        'Micromedex - Ceftriaxone Drug Information',
        'IDSA Guidelines - Community-Acquired Pneumonia, Meningitis'],
        'last_updated': '2025-02-03', 'evidence_level':
        'A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }}}

__all__ = ['CEPHALOSPORINS_DRUGS']
