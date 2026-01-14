"""Oncology Medications
Active module - contains all oncology drug data"""

# Platinum Compounds

PLATINUM_COMPOUNDS_DRUGS = {
    "Carboplatin": {'group': 'Oncology - Platinum Compound', 'vietnamese_name':
        'Carboplatin, Paraplatin', 'administration': ['IV'], 'indications': [
        'Ung thư buồng trứng', 'Ung thư phổi (NSCLC)', 'Ung thư đầu cổ',
        'Ung thư cổ tử cung', 'Ung thư tinh hoàn'], 'contraindications': [
        'Dị ứng carboplatin hoặc platinum compounds',
        'Giảm bạch cầu/tiểu cầu nặng', 'Có thai', 'Đang cho con bú'], 'dosage':
        {'adult_calvert': 'AUC 4-6 mg/mL x min IV (tính theo GFR)',
        'adult_fixed': '300-400mg/m² IV mỗi 4 tuần', 'adult_weekly':
        '100mg/m² IV mỗi tuần', 'notes':
        'Dùng công thức Calvert: Dose (mg) = AUC x (GFR + 25). Ít độc thận hơn cisplatin'
        }, 'renal_adjustment': {'normal':
        'Tính theo GFR trong công thức Calvert', '30_60':
        'Giảm AUC hoặc liều 25-50%', 'under_30':
        'Thận trọng, giảm liều đáng kể'}, 'side_effects': [
        'Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến hơn cisplatin)',
        'Nôn mửa (ít hơn cisplatin)',
        'Độc thận (ít hơn cisplatin nhưng vẫn có)', 'Rụng tóc (ít)',
        'Độc thần kinh (ít hơn cisplatin)', 'Phản ứng dị ứng (hiếm)',
        'Hạ magne máu'],
        'interactions': [
        'Thuốc độc thận: tránh dùng đồng thời',
        'Phenytoin: giảm nồng độ phenytoin'],
        'mechanism_of_action':
        'Carboplatin là hợp chất platinum tương tự cisplatin, gây liên kết chéo DNA và ngăn chặn quá trình sao chép DNA. Cơ chế tác dụng giống cisplatin nhưng có cấu trúc hóa học khác (thay nhóm amin bằng cyclobutanedicarboxylate). Tác dụng trên nhiều loại ung thư tương tự cisplatin. Ưu điểm: ít độc thận và độc thần kinh hơn cisplatin, nhưng gây myelosuppression nhiều hơn. Liều được tính theo AUC (Area Under Curve) dựa trên GFR để đảm bảo hiệu quả và giảm độc tính'
        , 'monitoring': [
        'Creatinine, BUN, GFR trước mỗi chu kỳ (để tính liều theo công thức Calvert)'
        ,
        'Công thức máu (CBC) trước và sau mỗi chu kỳ - myelosuppression là độc tính phổ biến nhất'
        , 'Chức năng thận (CrCl) - cần để tính liều chính xác',
        'Dấu hiệu nhiễm trùng (do giảm bạch cầu)',
        'Dấu hiệu chảy máu (do giảm tiểu cầu)',
        'Dấu hiệu nôn mửa (ít hơn cisplatin nhưng vẫn có)',
        'Chức năng thận (độc thận ít hơn cisplatin nhưng vẫn cần theo dõi)',
        'Magne máu (hạ magne phổ biến)'], 'precautions': [
        'Dùng công thức Calvert để tính liều: Dose (mg) = AUC x (GFR + 25) - đảm bảo hiệu quả và giảm độc tính'
        , 'AUC thường dùng: 4-6 mg/mL x min (tùy phác đồ)',
        'THEO DÕI CHẶT CHẼ myelosuppression (giảm bạch cầu, tiểu cầu) - là độc tính phổ biến nhất'
        , 'Có thể cần hỗ trợ G-CSF nếu giảm bạch cầu nặng',
        'Có thể cần truyền tiểu cầu nếu giảm tiểu cầu nặng',
        'Ít cần hydration như cisplatin (ít độc thận hơn) nhưng vẫn nên truyền dịch đầy đủ'
        , 'Dùng antiemetic trước và sau truyền (ít nôn hơn cisplatin)',
        'Bổ sung magne nếu hạ magne máu',
        'Thận trọng ở bệnh nhân suy thận (cần điều chỉnh liều theo GFR)',
        'Theo dõi nhiễm trùng và chảy máu (do myelosuppression)',
        'Không dùng trong thai kỳ (dị tật thai nhi)'], 'pharmacokinetics': {
        'half_life': '2-6 giờ (ngắn hơn cisplatin)', 'onset': 'Nhanh',
        'duration': 'Dài (tác dụng kéo dài)', 'protein_binding':
        'Thấp (khác với cisplatin)', 'clearance':
        'Thận (chủ yếu, thải trừ nhanh hơn cisplatin)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch pha: bảo quản ở nhiệt độ phòng, dùng trong 8 giờ. Không đông lạnh'
        , 'black_box_warnings':
        'Myelosuppression có thể nặng (giảm bạch cầu, tiểu cầu) - theo dõi chặt chẽ. Nhiễm trùng và chảy máu có thể xảy ra. Chống chỉ định trong thai kỳ'
        , 'drug_interactions': {'major': [{'drug': 'Aminoglycosides',
        'mechanism': 'Tăng độc thận', 'effect': 'Tăng nguy cơ suy thận cấp',
        'management':
        'Tránh dùng cùng. Nếu bắt buộc, giảm liều và theo dõi chức năng thận chặt chẽ.'
        }, {'drug': 'Thuốc độc thận khác', 'mechanism':
        'Tăng độc thận tích lũy', 'effect': 'Tăng nguy cơ suy thận cấp',
        'management':
        'Tránh dùng cùng. Nếu bắt buộc, giảm liều và theo dõi chức năng thận.'}
        ], 'moderate': [{'drug': 'Phenytoin', 'mechanism':
        'Carboplatin có thể giảm nồng độ phenytoin', 'effect':
        'Giảm nồng độ phenytoin, tăng nguy cơ co giật', 'management':
        'Theo dõi nồng độ phenytoin. Tăng liều phenytoin nếu cần.'}, {'drug':
        'Nephrotoxic drugs (NSAIDs, ACE inhibitors)', 'mechanism':
        'Tăng độc thận', 'effect': 'Tăng nguy cơ suy thận', 'management':
        'Thận trọng. Theo dõi chức năng thận.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': ['Có thai', 'Đang cho con bú',
        'Dị ứng carboplatin hoặc platinum compounds',
        'Giảm bạch cầu/tiểu cầu nặng'], 'tương_đối': [
        'Suy thận nặng (CrCl <30) - giảm liều đáng kể, điều chỉnh công thức Calvert'
        , 'Suy gan nặng - thận trọng',
        'Người cao tuổi - tăng nguy cơ myelosuppression',
        'Đã dùng platinum compounds trước đây - tăng nguy cơ phản ứng dị ứng']},
        'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Carboplatin gây dị tật thai nhi, chậm phát triển, tử vong thai nhi. Cần test thai trước khi điều trị. Sử dụng biện pháp tránh thai hiệu quả trong và sau điều trị (ít nhất 6 tháng).'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Carboplatin bài tiết vào sữa mẹ. Không an toàn cho trẻ bú mẹ. Có thể gây độc tính nghiêm trọng ở trẻ.'
        , 'recommendation':
        'Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng điều trị.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Không đổi hoặc giảm liều nhẹ', 'severe':
        'Thận trọng, có thể giảm liều', 'notes':
        'Carboplatin chủ yếu thải trừ qua thận, không phụ thuộc nhiều vào chức năng gan. Liều được tính theo GFR (công thức Calvert).'
        }, 'overdose_management': {'symptoms': [
        'Myelosuppression nặng (giảm bạch cầu, tiểu cầu, thiếu máu)',
        'Nhiễm trùng (do giảm bạch cầu)', 'Chảy máu (do giảm tiểu cầu)',
        'Suy thận cấp (ít hơn cisplatin nhưng vẫn có)', 'Nôn mửa',
        'Hạ magne máu'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment': [
        'Ngừng truyền ngay lập tức',
        'Theo dõi công thức máu chặt chẽ (myelosuppression là độc tính chính)',
        'Điều trị myelosuppression: G-CSF nếu giảm bạch cầu nặng, truyền tiểu cầu nếu giảm tiểu cầu nặng, truyền máu nếu thiếu máu'
        , 'Điều trị nhiễm trùng: Kháng sinh phổ rộng nếu có nhiễm trùng',
        'Điều trị chảy máu: Truyền tiểu cầu, hỗ trợ đông máu',
        'Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu)',
        'Bổ sung magne nếu hạ magne máu',
        'Điều trị nôn mửa: Antiemetics (ondansetron, aprepitant)',
        'Hydration đầy đủ để tăng thải trừ'], 'monitoring':
        'Công thức máu (CBC), chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, magne máu'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Hydration đầy đủ để tăng thải trừ. Điều trị độc thận, độc thần kinh hỗ trợ.'},
        'administration_instructions': {'oral': {'with_food': 'N/A', 'timing':
        'N/A'}, 'iv': {'reconstitution':
        'Pha với D5W hoặc NS để nồng độ 0.5-2mg/mL', 'infusion_rate':
        'Truyền trong 15-60 phút. Tốc độ phụ thuộc liều và phác đồ',
        'compatibility': ['D5W', 'NS'], 'incompatibility': ['Các thuốc khác'],
        'notes':
        'Dùng công thức Calvert để tính liều: Dose (mg) = AUC x (GFR + 25). Ít cần hydration như cisplatin nhưng vẫn nên truyền dịch đầy đủ. Theo dõi công thức máu chặt chẽ.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Paraplatin (carboplatin)',
        'UpToDate - Carboplatin: Drug information',
        'NCCN Guidelines - Cancer treatment',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews'}},
    "Cisplatin": {'group': 'Oncology - Platinum Compound', 'vietnamese_name':
        'Cisplatin, Platinol', 'administration': ['IV'], 'indications': [
        'Ung thư phổi (NSCLC, SCLC)', 'Ung thư đầu cổ', 'Ung thư tinh hoàn',
        'Ung thư buồng trứng', 'Ung thư bàng quang', 'Ung thư cổ tử cung'],
        'contraindications': ['Dị ứng cisplatin', 'Suy thận nặng (CrCl <60)',
        'Giảm thính lực', 'Giảm bạch cầu/tiểu cầu nặng', 'Có thai',
        'Đang cho con bú'], 'dosage': {'adult_standard':
        '50-100mg/m² IV mỗi 3-4 tuần', 'adult_weekly': '20-30mg/m² IV mỗi tuần',
        'adult_daily': '15-20mg/m² IV x 5 ngày (mỗi 3-4 tuần)', 'notes':
        'Truyền với nước muối sinh lý (NaCl 0.9%), cần pre-hydration và post-hydration'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều 25-50%', 'under_30': 'Không dùng hoặc giảm liều 50-75%'},
        'side_effects': ['Độc thận (phổ biến và nghiêm trọng - cần hydration)',
        'Nôn mửa nặng (thường xảy ra)', 'Giảm thính lực (có thể vĩnh viễn)',
        'Độc thần kinh ngoại biên (tê bì, dị cảm)',
        'Giảm bạch cầu, tiểu cầu (myelosuppression)', 'Rụng tóc',
        'Hạ magne máu (phổ biến)', 'Độc tim (hiếm)'], 'interactions': [
        'Aminoglycosides: tăng độc thận', 'Furosemide: tăng độc thận',
        'Phenytoin: giảm nồng độ phenytoin',
        'Thuốc độc thận khác: tránh dùng đồng thời'], 'pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Cisplatin là hợp chất platinum gây liên kết chéo (cross-linking) DNA, đặc biệt giữa các base guanine và adenine. Liên kết chéo này ngăn chặn quá trình sao chép và phiên mã DNA, dẫn đến tổn thương DNA và chết tế bào. Cisplatin tạo thành các adduct với DNA, kích hoạt các con đường tín hiệu dẫn đến apoptosis. Tác dụng trên nhiều loại ung thư, đặc biệt hiệu quả với ung thư tinh hoàn, buồng trứng, phổi, đầu cổ. Có độc tính cao, đặc biệt là độc thận và độc thần kinh'
        , 'monitoring': [
        'Creatinine, BUN, điện giải trước và sau mỗi chu kỳ (độc thận là độc tính phổ biến nhất và nghiêm trọng)'
        , 'Lượng nước tiểu trong và sau truyền (đảm bảo >100ml/giờ)',
        'Chức năng thận (CrCl) trước mỗi chu kỳ - giảm liều nếu CrCl <60',
        'Thính lực (audiometry) trước và định kỳ - giảm thính lực có thể vĩnh viễn'
        ,
        'Dấu hiệu độc thần kinh ngoại biên: tê bì, dị cảm, yếu cơ (có thể tiến triển)'
        , 'Công thức máu (CBC) trước mỗi chu kỳ - myelosuppression',
        'Magne máu (hạ magne phổ biến, cần bổ sung)',
        'Dấu hiệu nôn mửa (nặng, cần antiemetic mạnh)',
        'Chức năng tim (ECG) nếu có triệu chứng (độc tim hiếm)'], 'precautions':
        [
        'PHẢI có pre-hydration và post-hydration đầy đủ (1-2L NS trước và sau) để giảm độc thận'
        , 'Truyền với NaCl 0.9% (không dùng D5W) để tăng thải trừ',
        'THEO DÕI CHẶT CHẼ chức năng thận - giảm liều hoặc ngừng nếu creatinine tăng'
        , 'Không dùng nếu CrCl <60 (trừ khi không có lựa chọn khác)',
        'Tránh dùng cùng aminoglycosides, furosemide (tăng độc thận)',
        'Theo dõi thính lực - ngừng nếu giảm thính lực tiến triển',
        'Dùng antiemetic mạnh (ondansetron, aprepitant) trước và sau truyền',
        'Bổ sung magne nếu hạ magne máu',
        'Theo dõi độc thần kinh - có thể tiến triển sau khi ngừng thuốc',
        'Thận trọng ở bệnh nhân cao tuổi, suy thận, suy tim (tăng nguy cơ độc tính)'
        , 'Không dùng trong thai kỳ (dị tật thai nhi)'], 'pharmacokinetics': {
        'half_life': '30-100 giờ (rất dài, do gắn với protein và mô)', 'onset':
        'Nhanh (vài giờ)', 'duration': 'Dài (tác dụng kéo dài)',
        'protein_binding': '>90% (rất cao)', 'clearance':
        'Thận (chủ yếu, thải trừ qua nước tiểu), một phần gắn với mô (half-life dài)'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch pha: bảo quản ở nhiệt độ phòng, dùng trong 20 giờ. Không đông lạnh'
        , 'black_box_warnings':
        'Độc thận có thể nghiêm trọng và tích lũy - cần hydration đầy đủ và theo dõi chức năng thận. Giảm thính lực có thể vĩnh viễn. Độc thần kinh ngoại biên có thể tiến triển. Myelosuppression có thể nặng. Chống chỉ định trong thai kỳ'
        , 'drug_interactions': {'major': [{'drug':
        'Aminoglycosides (gentamicin, tobramycin, amikacin)', 'mechanism':
        'Tăng độc thận tích lũy', 'effect':
        'Tăng nguy cơ suy thận cấp, độc thận nặng', 'management':
        'Tránh dùng cùng. Nếu bắt buộc, giảm liều và theo dõi chức năng thận chặt chẽ.'
        }, {'drug': 'Furosemide, Thiazides', 'mechanism': 'Tăng độc thận',
        'effect': 'Tăng nguy cơ suy thận cấp', 'management':
        'Tránh dùng cùng. Nếu cần lợi tiểu, dùng mannitol hoặc theo dõi chặt chẽ.'
        }, {'drug': 'Thuốc độc thận khác (vancomycin, amphotericin B)',
        'mechanism': 'Tăng độc thận tích lũy', 'effect':
        'Tăng nguy cơ suy thận cấp', 'management':
        'Tránh dùng cùng. Nếu bắt buộc, giảm liều và theo dõi chức năng thận chặt chẽ.'
        }], 'moderate': [{'drug': 'Phenytoin', 'mechanism':
        'Cisplatin có thể giảm hấp thu phenytoin', 'effect':
        'Giảm nồng độ phenytoin, tăng nguy cơ co giật', 'management':
        'Theo dõi nồng độ phenytoin. Tăng liều phenytoin nếu cần.'}, {'drug':
        'Warfarin', 'mechanism': 'Có thể tăng nguy cơ chảy máu', 'effect':
        'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}],
        'minor': [{'drug': 'Nephrotoxic drugs (NSAIDs, ACE inhibitors)',
        'mechanism': 'Tăng độc thận', 'effect': 'Tăng nguy cơ suy thận',
        'management': 'Thận trọng. Theo dõi chức năng thận.'}]},
        'contraindications': {'tuyệt_đối': ['Suy thận nặng (CrCl <60)',
        'Giảm thính lực nặng', 'Có thai', 'Đang cho con bú',
        'Dị ứng cisplatin hoặc platinum compounds',
        'Giảm bạch cầu/tiểu cầu nặng'], 'tương_đối': [
        'Suy thận nhẹ đến trung bình (CrCl 30-60) - giảm liều 25-50%',
        'Giảm thính lực nhẹ - theo dõi sát', 'Suy gan nặng - thận trọng',
        'Bệnh tim - tăng nguy cơ độc tim',
        'Người cao tuổi - tăng nguy cơ độc tính',
        'Đã dùng cisplatin trước đây - tích lũy độc tính']},
        'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Cisplatin gây dị tật thai nhi, chậm phát triển, tử vong thai nhi. Cần test thai trước khi điều trị. Sử dụng biện pháp tránh thai hiệu quả trong và sau điều trị (ít nhất 6 tháng).'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Cisplatin bài tiết vào sữa mẹ. Không an toàn cho trẻ bú mẹ. Có thể gây độc tính nghiêm trọng ở trẻ.'
        , 'recommendation':
        'Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng điều trị.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Không đổi hoặc giảm liều nhẹ', 'severe':
        'Thận trọng, có thể giảm liều', 'notes':
        'Cisplatin chủ yếu thải trừ qua thận, không phụ thuộc nhiều vào chức năng gan. Tuy nhiên, suy gan có thể ảnh hưởng đến chuyển hóa và protein binding.'
        }, 'overdose_management': {'symptoms': [
        'Suy thận cấp nặng (tăng creatinine, BUN, giảm lượng nước tiểu)',
        'Giảm thính lực nặng, điếc',
        'Độc thần kinh ngoại biên nặng (tê bì, mất cảm giác)',
        'Myelosuppression nặng (giảm bạch cầu, tiểu cầu)', 'Nôn mửa nặng',
        'Hạ magne máu nặng', 'Độc tim (rối loạn nhịp, suy tim)', 'Suy hô hấp'],
        'antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment':
        ['Ngừng truyền ngay lập tức',
        'Hydration đầy đủ và mạnh (2-3L NS) để tăng thải trừ',
        'Theo dõi chức năng thận chặt chẽ (creatinine, BUN, lượng nước tiểu)',
        'Điều trị suy thận cấp: Truyền dịch, mannitol, furosemide (thận trọng)',
        'Lọc máu (hemodialysis) nếu suy thận nặng (hiệu quả hạn chế do gắn với protein)'
        , 'Bổ sung magne nếu hạ magne máu',
        'Điều trị myelosuppression: G-CSF, truyền máu/tiểu cầu nếu cần',
        'Điều trị nôn mửa: Antiemetics mạnh (ondansetron, aprepitant)',
        'Theo dõi thính lực (audiometry)',
        'Điều trị hỗ trợ: Chống nhiễm trùng, chống chảy máu'], 'monitoring':
        'Creatinine, BUN, lượng nước tiểu, công thức máu, thính lực, dấu hiệu độc thần kinh, magne máu, ECG, huyết áp'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Hydration đầy đủ để tăng thải trừ. Điều trị độc thận, độc thần kinh hỗ trợ.'},
        'administration_instructions': {'oral': {'with_food': 'N/A', 'timing':
        'N/A'}, 'iv': {'reconstitution':
        'Pha với NS 0.9% để nồng độ 0.5-1mg/mL. Không dùng D5W (không ổn định)',
        'infusion_rate':
        'Truyền 50-100mg/m² trong 1-2 giờ. Không quá 100mg/phút',
        'compatibility': ['NS 0.9%', 'Dung dịch chứa clorua', 'Các thuốc khác'], 'notes':
        'PHẢI có pre-hydration (1-2L NS trước) và post-hydration (1-2L NS sau) để giảm độc thận. Truyền với NS 0.9% để tăng thải trừ. Theo dõi lượng nước tiểu (đảm bảo >100ml/giờ).'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Platinol (cisplatin)',
        'UpToDate - Cisplatin: Drug information',
        'NCCN Guidelines - Cancer treatment',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews'}},
    "Oxaliplatin": {'group': 'Oncology - Platinum Compound', 'vietnamese_name':
        'Oxaliplatin, Eloxatin', 'administration': ['IV'], 'indications': [
        'Ung thư đại trực tràng (adjuvant và metastatic)', 'Ung thư dạ dày',
        'Ung thư tụy'], 'contraindications': [
        'Dị ứng oxaliplatin hoặc platinum compounds',
        'Giảm bạch cầu/tiểu cầu nặng', 'Suy thận nặng (CrCl <30)',
        'Suy gan nặng', 'Có thai', 'Đang cho con bú'], 'dosage': {
        'adult_folfox':
        '85mg/m² IV mỗi 2 tuần (phối hợp với 5-FU và leucovorin)',
        'adult_single': '85-130mg/m² IV mỗi 2-3 tuần', 'notes':
        'Truyền 2-6 giờ. Tránh lạnh (độc lạnh - cold-induced neuropathy)'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, có thể giảm liều', 'under_30':
        'Thận trọng, giảm liều 25-50%'}, 'side_effects': [
        'Độc lạnh (cold-induced neuropathy - tê, cảm giác như bị điện giật khi tiếp xúc lạnh)'
        , 'Độc thần kinh ngoại biên (tê bì, mất cảm giác)', 'Nôn mửa',
        'Tiêu chảy', 'Giảm bạch cầu, tiểu cầu', 'Phản ứng dị ứng (hiếm)',
        'Độc gan (tăng transaminase)'], 'interactions': [
        'Thuốc độc thận: thận trọng',
        'Phenytoin: có thể giảm nồng độ phenytoin'], 'pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Oxaliplatin là platinum compound, tạo ra các phức hợp platinum-DNA (cross-links), gây đứt gãy DNA và ngăn cản quá trình sao chép và phiên mã DNA. Thuốc tác động chủ yếu lên tế bào đang phân chia nhanh, gây độc tế bào và chết tế bào ung thư. Oxaliplatin có cơ chế tương tự cisplatin và carboplatin nhưng có độc tính khác biệt (độc lạnh, độc thần kinh ngoại biên). Thuốc hiệu quả với ung thư đại trực tràng, đặc biệt khi dùng kết hợp với 5-FU và leucovorin (FOLFOX protocol)'
        , 'monitoring': ['Công thức máu toàn phần (CBC) trước mỗi chu kỳ',
        'Chức năng thận (creatinine, eGFR) trước mỗi chu kỳ',
        'Chức năng gan (ALT, AST) trước mỗi chu kỳ',
        'Dấu hiệu độc lạnh (tê, cảm giác như bị điện giật khi tiếp xúc lạnh) - phổ biến'
        , 'Dấu hiệu độc thần kinh ngoại biên (tê bì, mất cảm giác) - tích lũy',
        'Dấu hiệu phản ứng dị ứng (phát ban, khó thở) - hiếm',
        'Theo dõi extravasation khi truyền'], 'precautions': [
        'Tránh tiếp xúc với lạnh trong 3-7 ngày sau truyền (tránh độc lạnh)',
        'Không uống nước lạnh, không chạm vào đồ vật lạnh',
        'Mặc ấm, đeo găng tay, tất để tránh lạnh',
        'Theo dõi độc thần kinh ngoại biên (có thể tích lũy và kéo dài)',
        'Giảm liều hoặc ngừng nếu độc thần kinh nặng',
        'Giảm liều 25-50% nếu suy thận (CrCl <30-60)', 'Truyền trong 2-6 giờ',
        'Có thể gây phản ứng dị ứng (hiếm - cần theo dõi)'], 'pharmacokinetics':
        {'half_life': '40 giờ (dài)', 'onset': '1-2 tuần (tác dụng lâm sàng)',
        'duration': 'Kéo dài (tích lũy)', 'protein_binding': '>90%',
        'clearance': 'Thận (thải trừ chủ yếu), không chuyển hóa'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu'
        , 'black_box_warnings':
        'Có thể gây độc lạnh nặng (cold-induced neuropathy) - tránh tiếp xúc với lạnh trong 3-7 ngày sau truyền. Có thể gây độc thần kinh ngoại biên tích lũy và kéo dài'
        , 'drug_interactions': {'major': [], 'moderate': [{'drug':
        'Thuốc độc thận (Aminoglycosides, Vancomycin, Amphotericin B)',
        'mechanism':
        'Cả hai đều có độc tính thận, tác dụng cộng dồn làm tăng nguy cơ suy thận cấp.'
        , 'effect': 'Tăng nguy cơ suy thận cấp, độc thận nghiêm trọng',
        'management':
        'Thận trọng khi dùng đồng thời. Theo dõi chức năng thận chặt chẽ. Duy trì đủ dịch.'
        }, {'drug': 'Phenytoin', 'mechanism':
        'Oxaliplatin có thể giảm nồng độ phenytoin trong máu.', 'effect':
        'Giảm nồng độ phenytoin, giảm hiệu quả chống co giật', 'management':
        'Theo dõi nồng độ phenytoin. Có thể cần tăng liều phenytoin.'}],
        'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng oxaliplatin hoặc platinum compounds',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'], 'tương_đối': [
        'Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục',
        'Suy thận nặng (CrCl <30) - giảm liều 25-50%, theo dõi chặt chẽ',
        'Suy gan nặng - thận trọng, có thể cần giảm liều',
        'Bệnh nhân có tiền sử độc thần kinh - tăng nguy cơ độc thần kinh nặng']
        }, 'contraindications_detail': {'tuyệt_đối': [
        'Dị ứng oxaliplatin hoặc platinum compounds',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'], 'tương_đối': [
        'Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục',
        'Suy thận nặng (CrCl <30) - giảm liều 25-50%, theo dõi chặt chẽ',
        'Suy gan nặng - thận trọng, có thể cần giảm liều',
        'Bệnh nhân có tiền sử độc thần kinh - tăng nguy cơ độc thần kinh nặng']
        }, 'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Oxaliplatin gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Oxaliplatin bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng oxaliplatin. Ngừng cho con bú hoặc ngừng thuốc.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        'Oxaliplatin không chuyển hóa qua gan, thải trừ chủ yếu qua thận. Tuy nhiên, suy gan có thể ảnh hưởng đến chức năng tổng thể và khả năng chịu đựng điều trị.'
        }, 'overdose_management': {'symptoms': [
        'Độc lạnh nặng (tê, cảm giác như bị điện giật khi tiếp xúc lạnh)',
        'Độc thần kinh ngoại biên nặng (tê bì, mất cảm giác)', 'Nôn mửa nặng',
        'Tiêu chảy nặng', 'Giảm bạch cầu, tiểu cầu nặng',
        'Phản ứng dị ứng nặng'],
        'treatment': ['Ngừng ngay oxaliplatin',
        'Tránh tiếp xúc với lạnh (quan trọng)',
        'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng thận, chức năng gan',
        'Điều trị nôn mửa (ondansetron, granisetron)',
        'Điều trị tiêu chảy (loperamide, bù dịch)',
        'Theo dõi và điều trị phản ứng dị ứng nếu có'], 'monitoring':
        'CBC, chức năng thận, chức năng gan, dấu hiệu độc lạnh, dấu hiệu độc thần kinh, dấu hiệu nhiễm trùng'
        }, 'reversal_agents': {'available': False, 'agents': [],
        'notes': 'Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Tránh tiếp xúc với lạnh (quan trọng).'}, 'administration_instructions': {'oral': {
        'with_food': 'Không áp dụng', 'timing':
        'Không có dạng uống (chỉ có IV)'}, 'iv': {'reconstitution':
        'Pha với D5W (không dùng NS - có thể làm tăng độc tính) theo hướng dẫn nhà sản xuất'
        , 'infusion_rate': 'Truyền trong 2-6 giờ', 'compatibility': ['D5W'],
        'incompatibility': ['NS', 'NaCl'], 'notes':
        'KHÔNG dùng NS hoặc NaCl để pha (có thể làm tăng độc tính). Chỉ dùng D5W. Truyền trong 2-6 giờ. Tránh lạnh khi truyền và sau truyền.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Oxaliplatin (Eloxatin)',
        'UpToDate - Oxaliplatin Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-15', "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    }
}

__all__ = ['PLATINUM_COMPOUNDS_DRUGS']
