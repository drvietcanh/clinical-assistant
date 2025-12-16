"""Neurological Medications - Alzheimer's Disease and Dementia
Active module - contains cholinesterase inhibitors and NMDA antagonists"""

# Cholinesterase Inhibitors and NMDA Antagonists

ALZHEIMER_DEMENTIA_DRUGS = {
    "Donepezil": {'group': 'Neurology - Cholinesterase Inhibitor',
        'vietnamese_name': 'Donepezil, Aricept', 'administration': ['PO'],
        'indications': [
        'Bệnh Alzheimer (mild to moderate dementia)',
        'Bệnh Alzheimer (moderate to severe dementia)'], 'contraindications': [
        'Dị ứng', 'Bệnh tim nặng (block nhĩ thất, rối loạn nhịp nặng)'],
        'dosage': {'adult_mild_moderate': '5mg/ngày, tăng đến 10mg/ngày sau 4-6 tuần',
        'adult_moderate_severe': '10mg/ngày, có thể tăng đến 23mg/ngày (extended release)',
        'adult_max': '23mg/ngày (extended release)', 'notes':
        'Uống buổi tối với thức ăn. Tăng liều chậm để giảm tác dụng phụ'}, 'side_effects': [
        'Buồn nôn, nôn', 'Tiêu chảy', 'Mất ngủ', 'Chóng mặt', 'Nhức đầu',
        'Chán ăn, giảm cân', 'Co thắt cơ (muscle cramps)', 'Mệt mỏi',
        'Chậm nhịp tim (bradycardia)', 'Ngất (syncope)'], 'interactions': [
        'Anticholinergics: đối kháng tác dụng donepezil',
        'Cholinergic drugs: tăng tác dụng, tăng tác dụng phụ',
        'Succinylcholine: tăng tác dụng, tăng nguy cơ kéo dài block thần kinh cơ',
        'Beta-blockers: tăng nguy cơ chậm nhịp tim'], 'pregnancy': 'C',
        'mechanism_of_action':
        'Donepezil là thuốc ức chế cholinesterase (acetylcholinesterase inhibitor) có tính chọn lọc, không thể đảo ngược. Ức chế enzyme acetylcholinesterase ở synap thần kinh, làm giảm phân hủy acetylcholine và tăng nồng độ acetylcholine trong synap. Acetylcholine là chất dẫn truyền thần kinh quan trọng cho trí nhớ và nhận thức. Trong bệnh Alzheimer, có sự suy giảm cholinergic (giảm acetylcholine). Donepezil làm tăng nồng độ acetylcholine, cải thiện chức năng nhận thức (trí nhớ, suy nghĩ, hành vi) ở bệnh nhân Alzheimer. Tác dụng: cải thiện nhận thức, hành vi, và hoạt động hàng ngày. Donepezil có half-life dài (70 giờ), cho phép dùng 1 lần/ngày.'
        , 'monitoring': [
        'Đáp ứng điều trị: cải thiện nhận thức, hành vi, hoạt động hàng ngày (đánh giá bằng MMSE, ADAS-Cog)'
        , 'Tác dụng phụ tiêu hóa: buồn nôn, nôn, tiêu chảy (phổ biến, thường tự khỏi sau vài tuần)'
        , 'Nhịp tim: chậm nhịp tim (bradycardia) - nguy hiểm, đặc biệt ở bệnh nhân có bệnh tim'
        , 'Ngất (syncope) - có thể xảy ra do chậm nhịp tim',
        'Cân nặng: chán ăn, giảm cân - theo dõi cân nặng',
        'Giấc ngủ: mất ngủ - có thể cần dùng buổi sáng thay vì buổi tối',
        'Tương tác với anticholinergics (đối kháng), cholinergic drugs (tăng tác dụng)'], 'precautions': [
        'Uống buổi tối với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất)',
        'Tăng liều chậm (5mg → 10mg sau 4-6 tuần) để giảm tác dụng phụ',
        'Buồn nôn, nôn, tiêu chảy - phổ biến, thường tự khỏi sau vài tuần, có thể giảm bằng cách uống với thức ăn'
        ,
        'CHẬM NHỊP TIM (bradycardia) - nguy hiểm, đặc biệt ở bệnh nhân có bệnh tim, block nhĩ thất, dùng beta-blockers'
        , 'Ngất (syncope) - có thể xảy ra do chậm nhịp tim, thận trọng',
        'Mất ngủ - có thể cần dùng buổi sáng thay vì buổi tối',
        'Chán ăn, giảm cân - theo dõi cân nặng',
        'CHỐNG CHỈ ĐỊNH trong bệnh tim nặng (block nhĩ thất, rối loạn nhịp nặng)',
        'Thận trọng khi dùng với beta-blockers (tăng nguy cơ chậm nhịp tim)',
        'Thận trọng khi dùng với anticholinergics (đối kháng tác dụng donepezil)',
        'Thận trọng khi dùng với cholinergic drugs (tăng tác dụng, tăng tác dụng phụ)',
        'Thận trọng với bệnh nhân có tiền sử loét dạ dày (tăng acid dạ dày)',
        'Không ngừng đột ngột (có thể làm tăng triệu chứng)'], 'pharmacokinetics': {
        'half_life': '70 giờ (rất dài, cho phép dùng 1 lần/ngày)', 'onset':
        'Vài tuần (tác dụng chậm)', 'duration': 'Dài (do half-life rất dài)',
        'protein_binding': '96% (rất cao)', 'metabolism':
        'Gan (chuyển hóa qua CYP2D6, CYP3A4), thận (thải trừ)', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ). Half-life rất dài (70 giờ) do gắn chặt với acetylcholinesterase.'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings':
        'Nguy cơ chậm nhịp tim (bradycardia) nghiêm trọng, có thể gây ngất, block nhĩ thất, rối loạn nhịp tim. Nguy cơ tăng ở bệnh nhân có bệnh tim, dùng beta-blockers, hoặc có block nhĩ thất. CHỐNG CHỈ ĐỊNH trong bệnh tim nặng. Theo dõi nhịp tim. Nguy cơ tăng acid dạ dày, có thể làm nặng loét dạ dày.'
        , 'drug_interactions': {'major': [{'drug': 'Beta-blockers (propranolol, metoprolol)',
        'mechanism': 'Cả hai đều có thể gây chậm nhịp tim', 'effect':
        'Tăng nguy cơ chậm nhịp tim nghiêm trọng, block nhĩ thất, ngất', 'management':
        'Thận trọng. Theo dõi nhịp tim. Có thể cần giảm liều beta-blocker hoặc donepezil.'
        }, {'drug': 'Succinylcholine', 'mechanism':
        'Donepezil ức chế cholinesterase, tăng tác dụng succinylcholine', 'effect':
        'Tăng tác dụng, tăng nguy cơ kéo dài block thần kinh cơ', 'management':
        'Ngừng donepezil ít nhất 2 tuần trước phẫu thuật nếu có thể. Nếu không thể, thông báo cho bác sĩ gây mê.'
        }], 'moderate': [{'drug': 'Anticholinergics (atropine, scopolamine)',
        'mechanism': 'Đối kháng tác dụng cholinergic của donepezil', 'effect':
        'Giảm hiệu quả donepezil', 'management':
        'Tránh dùng chung nếu có thể. Nếu phải dùng, theo dõi đáp ứng điều trị.'}, {
        'drug': 'Cholinergic drugs (bethanechol, pilocarpine)', 'mechanism':
        'Tăng tác dụng cholinergic', 'effect': 'Tăng tác dụng phụ (buồn nôn, nôn, tiêu chảy)',
        'management': 'Thận trọng. Có thể cần giảm liều một trong hai thuốc.'}], 'minor': [
        {'drug': 'CYP2D6, CYP3A4 inhibitors', 'mechanism':
        'Ức chế chuyển hóa donepezil', 'effect': 'Tăng nồng độ donepezil, tăng tác dụng phụ',
        'management': 'Thận trọng. Có thể cần giảm liều donepezil.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng donepezil hoặc các thành phần khác',
        'Bệnh tim nặng (block nhĩ thất độ II-III, rối loạn nhịp nặng)'], 'tương_đối': [
        'Bệnh tim mạch (suy tim, block nhĩ thất độ I) - tăng nguy cơ chậm nhịp tim',
        'Loét dạ dày - tăng acid dạ dày, có thể làm nặng loét',
        'Bệnh phổi (COPD, hen) - tăng co thắt phế quản',
        'Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy',
        'Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy',
        'Dùng với beta-blockers - tăng nguy cơ chậm nhịp tim',
        'Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Donepezil thường không được dùng trong thai kỳ vì bệnh Alzheimer chủ yếu ở người già. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không có dữ liệu về bài tiết donepezil vào sữa mẹ. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Tránh dùng khi cho con bú nếu có thể. Nếu phải dùng, theo dõi trẻ sát về dấu hiệu tác dụng phụ cholinergic.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ', 'notes':
        'Donepezil chuyển hóa ở gan qua CYP2D6, CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.'},
        'overdose_management': {'symptoms': [
        'Triệu chứng cholinergic quá mức: buồn nôn, nôn, tiêu chảy, tăng tiết nước bọt, đổ mồ hôi'
        , 'Chậm nhịp tim (bradycardia) nghiêm trọng, block nhĩ thất',
        'Co thắt phế quản, suy hô hấp',
        'Co giật (hiếm)',
        'Hôn mê (hiếm)'], 'antidote': 'Atropine (anticholinergic, đối kháng tác dụng cholinergic)',
        'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Atropine: 0.5-1mg IV (có thể lặp) để đối kháng tác dụng cholinergic',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch (nhịp tim)',
        'Xử trí chậm nhịp tim: atropine, pacemaker nếu cần',
        'Xử trí co thắt phế quản: albuterol, ipratropium',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp'], 'monitoring':
        'Theo dõi ý thức, hô hấp, tim mạch (nhịp tim), dấu hiệu cholinergic quá mức'},
        'reversal_agents': {'available': True, 'agents': [{'agent': 'Atropine',
        'mechanism': 'Anticholinergic, đối kháng tác dụng cholinergic', 'indication':
        'Quá liều gây triệu chứng cholinergic quá mức, chậm nhịp tim', 'caution':
        'Dùng thận trọng, theo dõi nhịp tim'}], 'notes':
        'Atropine là antidote cho quá liều donepezil. Dùng để đối kháng tác dụng cholinergic quá mức.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất)', 'timing':
        'Uống 1 lần/ngày vào buổi tối với thức ăn. Có thể chuyển sang buổi sáng nếu gây mất ngủ. Tăng liều chậm (5mg → 10mg sau 4-6 tuần).'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'}},
        'references': {'primary_sources': ['Lexicomp - Donepezil',
        'UpToDate - Donepezil: Drug information',
        'FDA - Aricept (donepezil) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'last_updated': '2024-12-19', 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        }},
    "Rivastigmine": {'group': 'Neurology - Cholinesterase Inhibitor',
        'vietnamese_name': 'Rivastigmine, Exelon', 'administration': ['PO',
        'Transdermal'], 'indications': [
        'Bệnh Alzheimer (mild to moderate dementia)',
        'Bệnh Alzheimer (moderate to severe dementia)',
        'Dementia do bệnh Parkinson'], 'contraindications': [
        'Dị ứng', 'Bệnh tim nặng (block nhĩ thất, rối loạn nhịp nặng)'],
        'dosage': {'adult_po': '1.5mg x 2 lần/ngày, tăng dần đến 6-12mg/ngày (chia 2 lần)',
        'adult_transdermal': '4.6mg/24h patch, tăng đến 9.5mg/24h patch', 'adult_max':
        '12mg/ngày (PO) hoặc 13.3mg/24h (transdermal)', 'notes':
        'Uống với thức ăn. Dạng transdermal: ít tác dụng phụ hơn'}, 'side_effects': [
        'Buồn nôn, nôn (phổ biến hơn donepezil)', 'Tiêu chảy', 'Chán ăn, giảm cân',
        'Chóng mặt', 'Nhức đầu', 'Mệt mỏi', 'Chậm nhịp tim (bradycardia)',
        'Kích ứng da (transdermal patch)'], 'interactions': [
        'Anticholinergics: đối kháng tác dụng rivastigmine',
        'Cholinergic drugs: tăng tác dụng, tăng tác dụng phụ',
        'Succinylcholine: tăng tác dụng, tăng nguy cơ kéo dài block thần kinh cơ',
        'Beta-blockers: tăng nguy cơ chậm nhịp tim'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Rivastigmine là thuốc ức chế cholinesterase (acetylcholinesterase và butyrylcholinesterase inhibitor) có tính chọn lọc, không thể đảo ngược. Ức chế cả acetylcholinesterase và butyrylcholinesterase ở synap thần kinh, làm giảm phân hủy acetylcholine và tăng nồng độ acetylcholine trong synap. Khác với donepezil, rivastigmine ức chế cả butyrylcholinesterase (có thể quan trọng trong bệnh Alzheimer). Rivastigmine có half-life ngắn (1.5 giờ), nhưng tác dụng kéo dài do gắn chặt với enzyme. Có dạng uống và dạng transdermal patch (ít tác dụng phụ tiêu hóa hơn). Tác dụng: cải thiện nhận thức, hành vi, và hoạt động hàng ngày ở bệnh nhân Alzheimer và dementia do bệnh Parkinson.'
        , 'monitoring': [
        'Đáp ứng điều trị: cải thiện nhận thức, hành vi, hoạt động hàng ngày',
        'Tác dụng phụ tiêu hóa: buồn nôn, nôn, tiêu chảy (phổ biến, đặc biệt với dạng uống)'
        , 'Nhịp tim: chậm nhịp tim (bradycardia) - nguy hiểm',
        'Cân nặng: chán ăn, giảm cân - theo dõi cân nặng',
        'Kích ứng da (nếu dùng transdermal patch) - thay vị trí dán patch',
        'Tương tác với anticholinergics (đối kháng), cholinergic drugs (tăng tác dụng)'], 'precautions': [
        'Uống với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất, đặc biệt với dạng uống)'
        , 'Dạng transdermal patch: ít tác dụng phụ tiêu hóa hơn dạng uống - nên dùng nếu có thể'
        , 'Tăng liều chậm để giảm tác dụng phụ',
        'Buồn nôn, nôn, tiêu chảy - phổ biến hơn donepezil, thường tự khỏi sau vài tuần',
        'CHẬM NHỊP TIM (bradycardia) - nguy hiểm, đặc biệt ở bệnh nhân có bệnh tim',
        'CHỐNG CHỈ ĐỊNH trong bệnh tim nặng (block nhĩ thất, rối loạn nhịp nặng)',
        'Thận trọng khi dùng với beta-blockers (tăng nguy cơ chậm nhịp tim)',
        'Thận trọng khi dùng với anticholinergics (đối kháng tác dụng)',
        'Thận trọng với bệnh nhân có tiền sử loét dạ dày',
        'Kích ứng da (transdermal patch) - thay vị trí dán patch mỗi ngày',
        'Không ngừng đột ngột (có thể làm tăng triệu chứng)'], 'pharmacokinetics': {
        'half_life': '1.5 giờ (ngắn), nhưng tác dụng kéo dài do gắn chặt với enzyme',
        'onset': 'Vài tuần (tác dụng chậm)', 'duration':
        'Dài (do gắn chặt với enzyme, mặc dù half-life ngắn)', 'protein_binding':
        '40%', 'metabolism':
        'Gan (chuyển hóa qua esterase, không phụ thuộc CYP450), thận (thải trừ)',
        'clearance':
        'Gan (chuyển hóa qua esterase, không phụ thuộc CYP450 - ít tương tác enzyme hơn), thận (thải trừ). Half-life ngắn nhưng tác dụng kéo dài do gắn chặt với enzyme.'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Transdermal patch: bảo quản trong bao bì kín, tránh nhiệt độ cao.'
        , 'black_box_warnings':
        'Nguy cơ chậm nhịp tim (bradycardia) nghiêm trọng, có thể gây ngất, block nhĩ thất, rối loạn nhịp tim. Nguy cơ tăng ở bệnh nhân có bệnh tim, dùng beta-blockers. CHỐNG CHỈ ĐỊNH trong bệnh tim nặng. Theo dõi nhịp tim. Nguy cơ tăng acid dạ dày, có thể làm nặng loét dạ dày.'
        , 'drug_interactions': {'major': [{'drug': 'Beta-blockers', 'mechanism':
        'Cả hai đều có thể gây chậm nhịp tim', 'effect':
        'Tăng nguy cơ chậm nhịp tim nghiêm trọng', 'management':
        'Thận trọng. Theo dõi nhịp tim. Có thể cần giảm liều.'}, {'drug':
        'Succinylcholine', 'mechanism':
        'Rivastigmine ức chế cholinesterase, tăng tác dụng succinylcholine', 'effect':
        'Tăng tác dụng, tăng nguy cơ kéo dài block thần kinh cơ', 'management':
        'Ngừng rivastigmine ít nhất 2 tuần trước phẫu thuật nếu có thể.'}], 'moderate': [
        {'drug': 'Anticholinergics', 'mechanism': 'Đối kháng tác dụng cholinergic',
        'effect': 'Giảm hiệu quả rivastigmine', 'management':
        'Tránh dùng chung nếu có thể.'}, {'drug': 'Cholinergic drugs', 'mechanism':
        'Tăng tác dụng cholinergic', 'effect': 'Tăng tác dụng phụ', 'management':
        'Thận trọng. Có thể cần giảm liều.'}], 'minor': []}, 'contraindications': {
        'tuyệt_đối': [
        'Dị ứng rivastigmine hoặc các thành phần khác',
        'Bệnh tim nặng (block nhĩ thất độ II-III, rối loạn nhịp nặng)'], 'tương_đối': [
        'Bệnh tim mạch - tăng nguy cơ chậm nhịp tim',
        'Loét dạ dày - tăng acid dạ dày',
        'Bệnh phổi (COPD, hen) - tăng co thắt phế quản',
        'Suy gan nặng - giảm chuyển hóa',
        'Suy thận nặng (CrCl <30) - giảm thải trừ',
        'Dùng với beta-blockers - tăng nguy cơ chậm nhịp tim']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Rivastigmine thường không được dùng trong thai kỳ vì bệnh Alzheimer chủ yếu ở người già. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không có dữ liệu về bài tiết rivastigmine vào sữa mẹ. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Tránh dùng khi cho con bú nếu có thể. Nếu phải dùng, theo dõi trẻ sát.'}},
        'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ', 'notes':
        'Rivastigmine chuyển hóa ở gan qua esterase (không phụ thuộc CYP450). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.'},
        'overdose_management': {'symptoms': [
        'Triệu chứng cholinergic quá mức: buồn nôn, nôn, tiêu chảy, tăng tiết nước bọt'
        , 'Chậm nhịp tim (bradycardia) nghiêm trọng',
        'Co thắt phế quản, suy hô hấp', 'Co giật (hiếm)'], 'antidote':
        'Atropine (anticholinergic)', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống',
        'Than hoạt tính nếu trong vòng 1-2 giờ',
        'Atropine: 0.5-1mg IV (có thể lặp)',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch',
        'Xử trí chậm nhịp tim: atropine, pacemaker nếu cần',
        'Hỗ trợ hô hấp nếu cần'], 'monitoring':
        'Theo dõi ý thức, hô hấp, tim mạch, dấu hiệu cholinergic quá mức'},
        'reversal_agents': {'available': True, 'agents': [{'agent': 'Atropine',
        'mechanism': 'Anticholinergic', 'indication': 'Quá liều gây triệu chứng cholinergic quá mức',
        'caution': 'Dùng thận trọng'}], 'notes': 'Atropine là antidote cho quá liều rivastigmine.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn để giảm buồn nôn', 'timing':
        'Chia 2 lần/ngày (sáng, tối) với thức ăn. Tăng liều chậm. Dạng transdermal patch: dán 1 lần/ngày, thay vị trí mỗi ngày.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống và transdermal'}},
        'references': {'primary_sources': ['Lexicomp - Rivastigmine',
        'UpToDate - Rivastigmine: Drug information',
        'FDA - Exelon (rivastigmine) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'last_updated': '2024-12-19', 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        }},
    "Memantine": {'group': 'Neurology - NMDA Receptor Antagonist',
        'vietnamese_name': 'Memantine, Namenda', 'administration': ['PO'],
        'indications': [
        'Bệnh Alzheimer (moderate to severe dementia)',
        'Bệnh Alzheimer (có thể dùng kết hợp với donepezil)'], 'contraindications': [
        'Dị ứng', 'Suy thận nặng (CrCl <30)'], 'dosage': {'adult_standard':
        '5mg/ngày, tăng dần đến 10mg x 2 lần/ngày (tối đa 20mg/ngày)', 'adult_max':
        '20mg/ngày', 'notes':
        'Tăng liều chậm (5mg → 10mg → 15mg → 20mg, mỗi tuần tăng 5mg)'}, 'side_effects': [
        'Chóng mặt', 'Nhức đầu', 'Táo bón', 'Buồn nôn', 'Mệt mỏi',
        'Lú lẫn (hiếm, thường khi tăng liều quá nhanh)'], 'interactions': [
        'Urine alkalinizers (sodium bicarbonate, carbonic anhydrase inhibitors): giảm thải trừ memantine, tăng nồng độ',
        'Acetazolamide: giảm thải trừ memantine',
        'Cimetidine, ranitidine: có thể tăng nồng độ memantine nhẹ'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Memantine là thuốc đối kháng thụ thể NMDA (N-methyl-D-aspartate receptor antagonist) không cạnh tranh, có ái lực thấp. Trong bệnh Alzheimer, có sự kích thích quá mức của thụ thể NMDA bởi glutamate (chất dẫn truyền thần kinh kích thích), dẫn đến độc tính thần kinh (excitotoxicity) và chết tế bào thần kinh. Memantine ức chế thụ thể NMDA, giảm kích thích quá mức và bảo vệ tế bào thần kinh. Khác với các thuốc đối kháng NMDA khác (như ketamine), memantine có ái lực thấp và không cạnh tranh, nên ít gây tác dụng phụ thần kinh (lú lẫn, ảo giác) hơn. Memantine được dùng trong bệnh Alzheimer moderate to severe, có thể dùng đơn độc hoặc kết hợp với donepezil. Tác dụng: cải thiện nhận thức, hành vi, và hoạt động hàng ngày.'
        , 'monitoring': [
        'Đáp ứng điều trị: cải thiện nhận thức, hành vi, hoạt động hàng ngày',
        'Tác dụng phụ thần kinh: chóng mặt, nhức đầu, lú lẫn (thường khi tăng liều quá nhanh)'
        , 'Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận (quan trọng)'
        , 'Tương tác với urine alkalinizers (giảm thải trừ, tăng nồng độ)'], 'precautions': [
        'Tăng liều chậm (5mg → 10mg → 15mg → 20mg, mỗi tuần tăng 5mg) để giảm tác dụng phụ'
        ,
        'Chóng mặt, nhức đầu - phổ biến, thường tự khỏi sau vài tuần, có thể giảm bằng cách tăng liều chậm'
        , 'Lú lẫn - hiếm, thường khi tăng liều quá nhanh, giảm liều nếu có',
        'Điều chỉnh liều ở suy thận QUAN TRỌNG: CrCl 30-60: giảm liều 50%; CrCl <30: chống chỉ định'
        , 'Thận trọng khi dùng với urine alkalinizers (sodium bicarbonate, acetazolamide) - giảm thải trừ, tăng nồng độ'
        , 'Thận trọng với bệnh nhân có tiền sử co giật (memantine có thể tăng nguy cơ co giật nhẹ)'
        , 'Có thể dùng kết hợp với donepezil (tác dụng bổ sung)',
        'Không ngừng đột ngột (có thể làm tăng triệu chứng)'], 'pharmacokinetics': {
        'half_life': '60-80 giờ (rất dài, cho phép dùng 1-2 lần/ngày)', 'onset':
        'Vài tuần (tác dụng chậm)', 'duration': 'Dài (do half-life rất dài)',
        'protein_binding': '45%', 'metabolism':
        'Thận (thải trừ chủ yếu nguyên dạng, ít chuyển hóa), gan (chuyển hóa một phần)',
        'clearance':
        'Thận: thải trừ chủ yếu nguyên dạng (80%), phụ thuộc pH nước tiểu (tăng thải trừ ở pH acid, giảm ở pH kiềm). Gan: chuyển hóa một phần. Half-life rất dài (60-80 giờ).'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, cần điều chỉnh liều ở suy thận (quan trọng). Nguy cơ lú lẫn khi tăng liều quá nhanh.'
        , 'drug_interactions': {'major': [{'drug':
        'Urine alkalinizers (sodium bicarbonate, acetazolamide, carbonic anhydrase inhibitors)',
        'mechanism':
        'Tăng pH nước tiểu, giảm thải trừ memantine (memantine thải trừ nhiều hơn ở pH acid)',
        'effect': 'Tăng nồng độ memantine, tăng tác dụng phụ', 'management':
        'Giảm liều memantine 50% khi dùng với urine alkalinizers. Theo dõi tác dụng phụ.'}],
        'moderate': [{'drug': 'Cimetidine, Ranitidine', 'mechanism':
        'Có thể giảm thải trừ memantine nhẹ', 'effect': 'Tăng nhẹ nồng độ memantine',
        'management': 'Thận trọng. Có thể cần giảm liều memantine nhẹ.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng memantine hoặc các thành phần khác',
        'Suy thận nặng (CrCl <30) - chống chỉ định do giảm thải trừ'], 'tương_đối': [
        'Suy thận (CrCl 30-60) - giảm liều 50%',
        'Suy gan nặng - giảm liều',
        'Tiền sử co giật - tăng nguy cơ co giật nhẹ',
        'Dùng với urine alkalinizers - giảm thải trừ, tăng nồng độ',
        'Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ']}, 'pregnancy_lactation': {
        'fda_category': 'B', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Memantine thường không được dùng trong thai kỳ vì bệnh Alzheimer chủ yếu ở người già. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không có dữ liệu về bài tiết memantine vào sữa mẹ. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Tránh dùng khi cho con bú nếu có thể. Nếu phải dùng, theo dõi trẻ sát.'}},
        'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ', 'notes':
        'Memantine chuyển hóa một phần ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, thải trừ chủ yếu qua thận, nên suy thận quan trọng hơn.'},
        'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: chóng mặt, nhức đầu, lú lẫn, mất điều hòa (ataxia)',
        'Rối loạn tiêu hóa: buồn nôn, nôn, táo bón',
        'Co giật (hiếm)',
        'Hôn mê (hiếm)'], 'antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ',
        'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống',
        'Than hoạt tính nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch',
        'Xử trí co giật: benzodiazepine nếu có',
        'Acid hóa nước tiểu (vitamin C, ammonium chloride) để tăng thải trừ memantine'
        , 'Hỗ trợ hô hấp nếu cần'], 'monitoring':
        'Theo dõi ý thức, hô hấp, tim mạch, dấu hiệu co giật'},
        'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn', 'timing':
        'Chia 2 lần/ngày (sáng, tối). Tăng liều chậm: 5mg/ngày x 1 tuần → 5mg x 2 lần/ngày x 1 tuần → 10mg buổi sáng + 5mg buổi tối x 1 tuần → 10mg x 2 lần/ngày. Có thể dùng kết hợp với donepezil.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'}},
        'references': {'primary_sources': ['Lexicomp - Memantine',
        'UpToDate - Memantine: Drug information',
        'FDA - Namenda (memantine) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'last_updated': '2024-12-19', 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        }}
}

__all__ = ['ALZHEIMER_DEMENTIA_DRUGS']





















