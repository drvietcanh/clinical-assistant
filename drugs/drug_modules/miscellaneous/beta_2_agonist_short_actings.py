"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Beta-2 Agonist (Short-acting)s

BETA_2_AGONIST_SHORT_ACTING_DRUGS = {
    "Salbutamol": {'group': 'Respiratory - Beta-2 Agonist (Short-acting)',
        'vietnamese_name':
        'Salbutamol, Albuterol, Ventolin, Salbutamol', 'administration': ['INH',
        'IV', 'PO', 'NEB'],
        'indications': [
        'COPD',
        'Co thắt phế quản', 'Phòng co thắt phế quản do gắng sức',
        'Cấp cứu hen (nebulizer/IV)'],
        'contraindications': [
        'Dị ứng salbutamol', 'Nhịp tim nhanh nặng', 'Rối loạn nhịp tim nặng',
        'Cường giáp'],
        'dosage': {'adult_inh':
        '1-2 puff (100-200mcg) x 4 lần/ngày hoặc khi cần (tối đa 8-12 puff/ngày)',
        'adult_neb': '2.5-5mg nebulizer mỗi 4-6 giờ', 'adult_iv':
        '5mcg/kg IV bolus, sau đó 0.5-5mcg/kg/phút', 'pediatric_inh':
        '1-2 puff (100-200mcg) x 4 lần/ngày (trên 4 tuổi)', 'pediatric_neb':
        '0.15mg/kg (tối thiểu 1.25mg) nebulizer mỗi 4-6 giờ',
        'pediatric_po_syrup':
        '0.1-0.15mg/kg x 3 lần/ngày (tối đa 2-4mg x 3 lần/ngày)', 'notes':
        'Có dạng syrup và nebulizer cho trẻ em. Dùng khi cần cho cơn cấp'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': ['Run tay (phổ biến)',
        'Tim đập nhanh', 'Đánh trống ngực', 'Đau đầu', 'Chóng mặt',
        'Hạ kali máu (với liều cao)', 'Kích động'],
        'interactions': [
        'Beta-blockers: đối kháng tác dụng',
        'Digoxin: có thể tăng nguy cơ loạn nhịp',
        'Diuretics: tăng nguy cơ hạ kali máu', 'MAOIs: thận trọng'],
        'pregnancy': 'C - An toàn', 'mechanism_of_action':
        'Salbutamol (albuterol) là chất chủ vận beta-2 adrenergic receptors chọn lọc, kích thích beta-2 receptors ở cơ trơn phế quản. Khi gắn vào beta-2 receptor, kích hoạt adenylate cyclase → tăng cAMP trong tế bào → hoạt hóa protein kinase A → phosphoryl hóa các protein → giãn cơ trơn phế quản. Salbutamol chọn lọc beta-2 hơn beta-1 (tỷ lệ ~10:1), nhưng vẫn có tác dụng tim mạch ở liều cao do kích thích beta-1 receptors. Ngoài ra, salbutamol ức chế phóng thích các chất trung gian gây viêm từ mast cells và giảm phù nề niêm mạc phế quản. Tác dụng nhanh (5-15 phút với dạng hít), ngắn (4-6 giờ), phù hợp cho cắt cơn hen cấp tính.'
        , 'monitoring': [
        'Nhịp tim, huyết áp (đặc biệt khi dùng IV hoặc liều cao) - có thể gây nhịp tim nhanh, tăng huyết áp'
        'Kali máu nếu dùng liều cao hoặc kéo dài (hạ kali máu do kích thích beta-2 → tăng kali vào tế bào)'
        'Đáp ứng phế quản (peak flow, FEV1, triệu chứng lâm sàng) để đánh giá hiệu quả'
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp, đau ngực, khó thở nặng hơn'
        'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm - cần ngừng ngay)'
        'Đường huyết nếu dùng liều cao (có thể tăng đường huyết do kích thích beta-2)'
        'Tần suất sử dụng (nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS)'
        ],
        'precautions': [
        'Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên như thuốc duy trì'
        'Nếu cần dùng >4 lần/ngày hoặc >8-12 puff/ngày → cần đánh giá lại điều trị và tăng liều ICS (inhaled corticosteroid)'
        'Tránh dùng với beta-blocker không chọn lọc (propranolol) - đối kháng tác dụng, có thể gây co thắt phế quản nặng'
        'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)'
        'Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ (run, tim đập nhanh)',
        'Rửa miệng sau khi dùng dạng hít để giảm kích ứng và tránh nấm miệng (nếu dùng với ICS)'
        'Nếu không đáp ứng hoặc cần dùng thường xuyên → cần đánh giá lại chẩn đoán và điều trị'
        'Thận trọng với bệnh nhân cường giáp (tăng nhạy cảm với catecholamine)',
        'Thận trọng với bệnh nhân dùng digoxin (tăng nguy cơ loạn nhịp)',
        'Dùng liều cao có thể gây hạ kali máu - thận trọng với diuretics'],
        'pharmacokinetics': {'half_life':
        '2-7 giờ (dạng hít), 2-4 giờ (IV), 3.8 giờ (PO)', 'onset':
        '5-15 phút (dạng hít), 2-5 phút (IV), 30 phút (PO)', 'duration':
        '4-6 giờ (dạng hít), 4-6 giờ (IV), 4-6 giờ (PO)', 'protein_binding':
        'Không đáng kể', 'clearance':
        'Gan: chuyển hóa qua sulfation và glucuronidation. Thận: bài tiết một phần nguyên dạng và metabolites. Dạng hít: tác dụng tại chỗ, hấp thu toàn thân ít. PO: hấp thu tốt nhưng tác dụng chậm hơn và nhiều tác dụng phụ hơn.'
        },
        'storage':
        'Dạng hít (MDI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh đông lạnh. Kiểm tra xem có còn thuốc (lắc, nghe tiếng). Nebulizer solution: bảo quản ở nhiệt độ phòng, tránh ánh sáng, dùng trong vòng 1 tháng sau khi mở. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha. Syrup: bảo quản ở nhiệt độ phòng, đậy kín sau khi dùng.'
        , 'black_box_warnings': None, 'drug_interactions': {
            'major': [
                {'drug': 'Beta-blockers (không chọn lọc: Propranolol, Nadolol)',
                 'mechanism': 'Beta-blockers đối kháng tác dụng beta-2 của salbutamol, có thể gây co thắt phế quản nặng và làm giảm hiệu quả điều trị hen.',
                 'effect': 'Đối kháng tác dụng giãn phế quản, có thể gây co thắt phế quản nặng, suy hô hấp',
                 'management': 'TRÁNH DÙNG với beta-blocker không chọn lọc. Nếu bệnh nhân cần beta-blocker, dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng. Theo dõi chặt chẽ đáp ứng phế quản.'}
            ],
        'moderate': [
                {'drug': 'Digoxin',
                 'mechanism': 'Salbutamol có thể gây hạ kali máu và tăng nhịp tim, tăng nguy cơ độc tính digoxin và loạn nhịp tim.',
                 'effect': 'Tăng nguy cơ loạn nhịp tim, tăng độc tính digoxin (đặc biệt khi hạ kali máu)',
                 'management': 'Theo dõi nồng độ digoxin và kali máu. Theo dõi ECG nếu có triệu chứng. Có thể cần điều chỉnh liều digoxin.'},
                {'drug': 'Diuretics (Furosemide, Thiazide)',
                 'mechanism': 'Cả hai đều có thể gây hạ kali máu, tăng nguy cơ hạ kali máu nghiêm trọng.',
                 'effect': 'Tăng nguy cơ hạ kali máu nghiêm trọng, loạn nhịp tim, yếu cơ',
                 'management': 'Theo dõi kali máu thường xuyên, đặc biệt khi dùng liều cao salbutamol. Bổ sung kali nếu cần.'},
                {'drug': 'MAOIs (Phenelzine, Tranylcypromine)',
                 'mechanism': 'MAOIs ức chế chuyển hóa catecholamine, có thể tăng tác dụng và tác dụng phụ của salbutamol.',
                 'effect': 'Tăng tác dụng tim mạch, tăng huyết áp, tăng nguy cơ loạn nhịp',
                 'management': 'Thận trọng, dùng liều thấp salbutamol. Theo dõi huyết áp và nhịp tim chặt chẽ.'},
                {'drug': 'Theophylline',
                 'mechanism': 'Cả hai đều kích thích beta-adrenergic, có thể tăng tác dụng phụ và độc tính.',
                 'effect': 'Tăng tác dụng phụ (run, tim đập nhanh, loạn nhịp), tăng nguy cơ độc tính theophylline',
                 'management': 'Theo dõi nồng độ theophylline. Theo dõi nhịp tim và triệu chứng. Có thể cần giảm liều theophylline.'}
            ],
        'minor': [
                {'drug': 'Tricyclic Antidepressants (TCA)',
                 'mechanism': 'TCA tăng nhạy cảm với catecholamine, có thể tăng tác dụng tim mạch.',
                 'effect': 'Tăng nhịp tim, tăng huyết áp (nhẹ)',
                 'management': 'Theo dõi nhịp tim và huyết áp. Không cần điều chỉnh liều thường quy.'}
            ]
        },
        'contraindications': {'tuyệt_đối': [
        'Dị ứng salbutamol hoặc các thành phần trong chế phẩm',
        'Nhịp tim nhanh nặng không kiểm soát (>120 bpm ở người lớn, >150 bpm ở trẻ em)'
        , 'Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)',
        'Cường giáp không điều trị (tăng nhạy cảm với catecholamine)'],
        'tương_đối': [
        'Bệnh tim mạch (suy tim, bệnh mạch vành) - thận trọng, theo dõi chặt chẽ',
        'Tăng huyết áp không kiểm soát - có thể tăng huyết áp',
        'Loạn nhịp tim nhẹ - có thể làm nặng',
        'Đái tháo đường - có thể tăng đường huyết',
        'Hạ kali máu - có thể làm nặng',
        'Cường giáp đang điều trị - thận trọng',
        'Dùng với digoxin - tăng nguy cơ loạn nhịp',
        'Dùng với MAOIs - tăng tác dụng tim mạch']},
        'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Salbutamol là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Salbutamol được sử dụng rộng rãi trong thai kỳ để điều trị hen và có vẻ an toàn. Hen phế quản không kiểm soát có thể gây nguy hiểm cho cả mẹ và thai nhi (thiếu oxy, suy thai). Salbutamol có thể được dùng khi lợi ích vượt quá nguy cơ. Dạng hít được ưu tiên hơn dạng uống hoặc IV để giảm tác dụng toàn thân. Tránh dùng liều cao kéo dài trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Salbutamol bài tiết vào sữa mẹ ở nồng độ rất thấp. Dạng hít có hấp thu toàn thân tối thiểu, nồng độ trong sữa mẹ rất thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Dạng uống và IV có hấp thu toàn thân nhiều hơn nhưng vẫn an toàn.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dạng hít được ưu tiên. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài.'
        }},
        'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Salbutamol chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.'
        , 'moderate':
        'Không cần điều chỉnh liều. Theo dõi tác dụng phụ nếu có.', 'severe':
        'Thận trọng, có thể cần giảm liều. Theo dõi tác dụng phụ chặt chẽ. Chuyển hóa có thể giảm ở suy gan nặng.'
        , 'notes':
        'Salbutamol chuyển hóa chủ yếu qua gan (sulfation, glucuronidation). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, nhưng ít khi cần điều chỉnh liều vì dạng hít có tác dụng tại chỗ.'
        },
        'overdose_management': {'symptoms': [
        'Triệu chứng tim mạch: Nhịp tim nhanh (>120-150 bpm), đánh trống ngực, loạn nhịp tim, đau ngực, tăng huyết áp'
        'Triệu chứng thần kinh: Run cơ nặng, kích động, lo âu, mất ngủ, đau đầu, chóng mặt'
        'Triệu chứng chuyển hóa: Hạ kali máu (do kích thích beta-2 → tăng kali vào tế bào), tăng đường huyết, toan chuyển hóa (hiếm)'
        'Triệu chứng hô hấp: Co thắt phế quản nghịch lý (hiếm nhưng nguy hiểm - khó thở nặng hơn), suy hô hấp'
        'Triệu chứng nghiêm trọng: Rung nhĩ, rung thất, sốc, suy tim cấp (với liều rất cao)'
        ],
        'antidote':
        'Không có antidote đặc hiệu. Beta-blocker chọn lọc có thể đối kháng tác dụng nhưng thận trọng vì có thể gây co thắt phế quản.'
        , 'treatment': ['Ngừng ngay salbutamol',
        'Theo dõi dấu hiệu sinh tồn: Nhịp tim, huyết áp, nhịp thở, SpO2, ECG',
        'Điều trị hỗ trợ: Nghỉ ngơi, trấn an, hỗ trợ hô hấp nếu cần',
        'Điều chỉnh điện giải: Bổ sung kali nếu hạ kali máu (theo dõi kali máu)',
        'Điều trị loạn nhịp: Nếu có rối loạn nhịp tim nghiêm trọng, cân nhắc dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng (có thể gây co thắt phế quản)'
        'Điều trị hạ huyết áp nếu có: Truyền dịch, nếu cần dùng thuốc vận mạch (thận trọng với thuốc kích thích beta)'
        , 'Theo dõi đường huyết: Điều chỉnh nếu tăng đường huyết',
        'Điều trị co thắt phế quản nghịch lý: Ngừng salbutamol, dùng ipratropium hoặc corticosteroid'
        , 'Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học'],
        'monitoring':
        'Theo dõi dấu hiệu sinh tồn, ECG, kali máu, đường huyết trong ít nhất 4-6 giờ. Theo dõi lâu hơn nếu có biến chứng tim mạch hoặc loạn nhịp.'
        },
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ.', 'timing':
        'Uống 3-4 lần/ngày, cách đều. Có thể uống trước hoặc sau bữa ăn. Lưu ý: Dạng uống có nhiều tác dụng phụ hơn dạng hít, nên ưu tiên dạng hít khi có thể.'
        },
        'iv': {'reconstitution':
        'Pha với NS hoặc D5W. Nồng độ pha: 1-5mcg/ml. Pha 1mg (1ml) trong 100ml dịch = 10mcg/ml. Pha 5mg (5ml) trong 500ml dịch = 10mcg/ml.'
        , 'infusion_rate':
        'Bolus: 5mcg/kg IV trong 1-2 phút. Truyền liên tục: 0.5-5mcg/kg/phút. Bắt đầu với liều thấp, tăng dần theo đáp ứng. Tốc độ: Ví dụ 70kg, 1mcg/kg/phút = 70mcg/phút = 4.2mg/giờ. Pha 5mg trong 500ml = 10mcg/ml → 70mcg/phút = 7ml/phút = 420ml/giờ.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],
        'incompatibility': [
        'Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm.'
        ],
        'notes':
        'Chỉ dùng IV trong cấp cứu hen nặng. Theo dõi chặt chẽ nhịp tim, huyết áp, ECG. Dùng liều thấp nhất hiệu quả. Có thể gây hạ kali máu với liều cao - theo dõi kali máu.'
        }, 'inhalation': {'technique':
        'MDI: Lắc kỹ, thở ra hết, đặt ống ngậm vào miệng, bắt đầu hít vào chậm và sâu, bấm thuốc, tiếp tục hít vào đến khi đầy phổi, giữ hơi 10 giây, thở ra chậm. Đợi 30-60 giây trước khi bấm lần thứ 2. Spacer: Dùng với MDI để tăng hiệu quả và giảm tác dụng phụ (đặc biệt ở trẻ em và người cao tuổi).'
        , 'nebulizer':
        'Pha 2.5-5mg trong 2-4ml NS hoặc nước cất. Thở bình thường qua mask hoặc ống ngậm. Thời gian: 5-15 phút. Rửa miệng sau khi dùng.'
        }},
        'references': {'primary_sources': [
        'FDA Drug Label - Albuterol (Salbutamol)',
        'GINA 2023 Guidelines - Global Initiative for Asthma',
        'UpToDate - Albuterol: Drug Information',
        'Medscape - Albuterol Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Albuterol Monograph',
        'Micromedex - Albuterol Drug Information'],
        'last_updated':
        '2024-12-19', 'evidence_level':
        'A - Dựa trên FDA drug labels, GINA guidelines, và dữ liệu lâm sàng từ nhiều nguồn',
        },
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': 'None',
            'organ_toxicity': {
                'cardiovascular': 'Moderate (tachycardia, arrhythmias, especially with high doses or IV)',
                'metabolic': 'Moderate (hypokalemia with high doses, hyperglycemia)',
                'respiratory': 'Rare (paradoxical bronchospasm - dangerous)'
            }, 'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': [
                'Heart rate, blood pressure (especially with IV or high doses) - can cause tachycardia, hypertension',
                'Serum potassium (if high doses or prolonged use) - hypokalemia due to beta-2 stimulation',
                'Bronchial response (peak flow, FEV1, clinical symptoms) to assess efficacy',
                'Signs of overdose: heart rate >120 bpm, severe muscle tremor, arrhythmias, chest pain, worsening dyspnea',
                'Signs of paradoxical bronchospasm: worsening dyspnea - CRITICAL (rare but dangerous, stop immediately)',
                'Blood glucose (if high doses - can increase blood glucose)',
                'Frequency of use (if need >4 times/day → need to reassess treatment and increase ICS)'
            ], 'look_alike_sound_alike': ['Salbutamol', 'Albuterol', 'Salmeterol', 'Formoterol']
        }, 'guideline_tags': [
            'GINA 2023 Guidelines - Global Initiative for Asthma',
            'NAEPP Guidelines - Asthma Management',
            'FDA Drug Information - Albuterol',
            'WHO Essential Medicines List'
        ]}}

__all__ = ['BETA_2_AGONIST_SHORT_ACTING_DRUGS']
