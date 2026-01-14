"""Neurological and Psychiatric Medications
Active module - contains all neurological and psychiatric drug data"""

# Anticonvulsants

ANTICONVULSANTS_DRUGS = {
    "Carbamazepine": {'group': 'Neurology - Anticonvulsant', 'vietnamese_name':
        'Carbamazepine, Tegretol', 'administration': ['PO'], 'indications': [
        'Động kinh', 'Đau dây thần kinh sinh ba', 'Rối loạn lưỡng cực',
        'Rối loạn nhân cách'],
        'contraindications': [
        'Bệnh gan nặng', 'Porphyria', 'Dùng MAO inhibitor',
        'Giảm bạch cầu/giảm tiểu cầu'], 'dosage': {'adult_epilepsy':
        '200-400mg x 2-3 lần/ngày, tăng dần đến 800-1600mg/ngày',
        'adult_neuralgia':
        '100-200mg x 2 lần/ngày, tăng đến 200-400mg x 3-4 lần/ngày', 'notes':
        'Theo dõi nồng độ trong máu, công thức máu, chức năng gan'},
        'side_effects': ['Chóng mặt', 'Buồn nôn', 'Giảm bạch cầu',
        'Ban da (nặng có thể SJS/TEN)', 'Rối loạn chức năng gan',
        'Hạ natri máu'], 'interactions': [
        'Nhiều thuốc: cảm ứng enzyme CYP450, giảm nồng độ nhiều thuốc',
        'Warfarin: giảm tác dụng warfarin',
        'Oral contraceptives: giảm hiệu quả'],
        'mechanism_of_action':
        'Thuốc chống co giật và ổn định tâm trạng. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh, ngăn cản sự lan truyền của các xung động bất thường. Cũng có thể ức chế giải phóng glutamate và điều hòa dòng calci. Tự cảm ứng enzyme (auto-induction) - tăng chuyển hóa của chính nó và các thuốc khác. Được dùng trong điều trị co giật cục bộ, co giật toàn thể, đau dây thần kinh sinh ba (trigeminal neuralgia), và rối loạn lưỡng cực. Có nhiều tương tác thuốc do cảm ứng enzyme.'
        , 'monitoring': [
        'Nồng độ carbamazepine trong máu (therapeutic range: 4-12 mcg/ml) - QUAN TRỌNG'
        , 'Tần suất và mức độ co giật',
        'Dấu hiệu độc tính (chóng mặt, ataxia, lú lẫn, buồn nôn)',
        'Công thức máu (giảm bạch cầu, giảm tiểu cầu, thiếu máu bất sản - nguy hiểm)'
        , 'Dấu hiệu hội chứng Stevens-Johnson (phát ban nặng) - nguy hiểm',
        'Chức năng gan (ALT, AST) - có thể tăng men gan, hiếm viêm gan',
        'Nồng độ natri (hạ natri máu - thường gặp)', 'Chức năng thận'],
        'precautions': ['Tuân thủ chặt chẽ liều và lịch dùng',
        'KHÔNG được ngừng đột ngột (nguy cơ co giật)',
        'Nồng độ trong máu cần được theo dõi định kỳ',
        'Nguy cơ giảm bạch cầu, giảm tiểu cầu, thiếu máu bất sản (nguy hiểm) - theo dõi công thức máu'
        , 'Nguy cơ hội chứng Stevens-Johnson - ngừng ngay nếu có phát ban',
        'Hạ natri máu thường gặp - theo dõi natri',
        'Tự cảm ứng enzyme → liều cần tăng dần theo thời gian',
        'Tương tác với nhiều thuốc: giảm hiệu quả thuốc tránh thai, warfarin, và các thuốc khác (do cảm ứng enzyme)'
        'Tương tác với nhiều thuốc: tăng nồng độ với erythromycin, cimetidine (do ức chế enzyme)'
        , 'Uống với thức ăn để giảm kích ứng dạ dày', 'Thận trọng ở suy gan'],
        'pharmacokinetics': {'half_life':
        '25-65 giờ (bình thường), giảm xuống 12-17 giờ sau khi tự cảm ứng enzyme',
        'onset': 'Vài giờ đến vài ngày', 'duration': 'Dài (phụ thuộc liều)',
        'protein_binding': '75%', 'metabolism':
        'Gan (CYP3A4) - tự cảm ứng enzyme, cũng cảm ứng các enzyme khác',
        'clearance': 'Gan, bị ảnh hưởng bởi tự cảm ứng và các thuốc tương tác'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.'
        , 'black_box_warnings':
        'Nguy cơ hội chứng Stevens-Johnson và hoại tử thượng bì nhiễm độc (TEN), có thể tử vong. Nguy cơ thiếu máu bất sản và giảm bạch cầu nghiêm trọng. Ngừng ngay nếu có phát ban hoặc dấu hiệu giảm bạch cầu. Nguy cơ tự sát và hành vi tự sát. Ngừng đột ngột có thể gây co giật.'
        , 'drug_interactions': {'major': [{'drug': 'Warfarin', 'mechanism':
        'Carbamazepine cảm ứng CYP2C9, tăng chuyển hóa warfarin', 'effect':
        'Giảm tác dụng chống đông, giảm INR', 'management':
        'Tăng liều warfarin, theo dõi INR thường xuyên. Có thể cần tăng liều warfarin 50-100% khi dùng carbamazepine.'
        }, {'drug': 'Oral contraceptives', 'mechanism':
        'Carbamazepine cảm ứng CYP3A4, tăng chuyển hóa estrogen và progestin',
        'effect': 'Giảm hiệu quả tránh thai, tăng nguy cơ mang thai',
        'management':
        'Sử dụng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang thuốc tránh thai liều cao hơn. Tư vấn bệnh nhân về nguy cơ.'
        }, {'drug': 'MAO inhibitors', 'mechanism':
        'Tăng nguy cơ hội chứng serotonin và tăng huyết áp', 'effect':
        'Nguy cơ hội chứng serotonin, tăng huyết áp nguy hiểm', 'management':
        'Chống chỉ định. Ngừng MAO inhibitor ít nhất 14 ngày trước khi dùng carbamazepine.'
        }, {'drug': 'Erythromycin, Clarithromycin', 'mechanism':
        'Ức chế CYP3A4, giảm chuyển hóa carbamazepine', 'effect':
        'Tăng nồng độ carbamazepine, tăng nguy cơ độc tính', 'management':
        'Giảm liều carbamazepine 25-50%, theo dõi nồng độ trong máu, dấu hiệu độc tính.'
        }, {'drug': 'Valproic acid', 'mechanism':
        'Cả hai đều ức chế chuyển hóa của nhau', 'effect':
        'Tăng nồng độ carbamazepine-10,11-epoxide (chất chuyển hóa độc)',
        'management':
        'Theo dõi nồng độ trong máu, giảm liều nếu cần. Theo dõi dấu hiệu độc tính.'
        }, {'drug': 'Phenytoin', 'mechanism': 'Cảm ứng enzyme lẫn nhau',
        'effect': 'Giảm nồng độ cả hai thuốc', 'management':
        'Theo dõi nồng độ trong máu, tăng liều nếu cần để đạt mức điều trị.'},
        {'drug': 'Cimetidine', 'mechanism': 'Ức chế CYP3A4', 'effect':
        'Tăng nồng độ carbamazepine', 'management':
        'Giảm liều carbamazepine, theo dõi nồng độ trong máu.'}], 'minor': [{
        'drug': 'Grapefruit juice', 'mechanism': 'Ức chế nhẹ CYP3A4', 'effect':
        'Tăng nhẹ nồng độ carbamazepine', 'management':
        'Tránh uống nhiều, hoặc tránh hoàn toàn nếu có thể.'}]},
        'contraindications': {'tuyệt_đối': [
        'Block nhĩ thất (AV block) độ II hoặc III',
        'Suy gan nặng (Child-Pugh C)', 'Porphyria',
        'Dùng MAO inhibitor (trong vòng 14 ngày)',
        'Tiền sử phản ứng quá mẫn với carbamazepine hoặc tricyclic antidepressants'
        , 'Giảm bạch cầu hoặc giảm tiểu cầu trước đó do carbamazepine'],
        'tương_đối': [
        'Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều, theo dõi chặt chẽ'
        , 'Suy thận (CrCl <30) - giảm liều, theo dõi nồng độ',
        'Bệnh tim mạch (rối loạn nhịp, block nhĩ thất độ I)',
        'Tiền sử bệnh tâm thần (nguy cơ tự sát)',
        'Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ',
        'Glaucoma góc đóng',
        'Bệnh nhân lớn tuổi (tăng nguy cơ hạ natri máu, độc tính)']},
        'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Carbamazepine có nguy cơ dị tật bẩm sinh (neural tube defects, dị tật tim, sứt môi/hà ếch). Nguy cơ dị tật bẩm sinh khoảng 5-6% (so với 2-3% ở dân số chung). Cần bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền, siêu âm chi tiết, và theo dõi chặt chẽ.'
        , 'lactation': {'safety': 'Compatible with monitoring', 'details':
        'Carbamazepine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình (nồng độ trong sữa mẹ khoảng 40-50% nồng độ trong huyết thanh mẹ). Nồng độ trong máu trẻ sơ sinh khoảng 5-10% nồng độ trong máu mẹ. Một số trẻ có thể có các tác dụng phụ nhẹ (buồn ngủ, bú kém).'
        , 'recommendation':
        'Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém, chậm tăng cân). Nếu trẻ có dấu hiệu ảnh hưởng, cân nhắc giảm liều hoặc ngừng cho con bú. Đo nồng độ carbamazepine trong máu trẻ nếu có triệu chứng.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan và nồng độ trong máu'
        , 'moderate':
        'Giảm liều 25-50%, theo dõi nồng độ trong máu thường xuyên, theo dõi ALT/AST'
        , 'severe':
        'Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ. Theo dõi nồng độ trong máu và ALT/AST thường xuyên. Nguy cơ tích lũy và độc tính cao.'
        , 'notes':
        'Carbamazepine chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính. Đặc biệt thận trọng vì carbamazepine có thể gây viêm gan.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: chóng mặt, ataxia, lú lẫn, buồn ngủ, hôn mê, co giật'
        'Rối loạn tim mạch: nhịp nhanh, hạ huyết áp, block nhĩ thất, rối loạn nhịp'
        , 'Rối loạn hô hấp: suy hô hấp, ngừng thở',
        'Rối loạn tiêu hóa: buồn nôn, nôn',
        'Triệu chứng khác: sốt, giảm bạch cầu, rối loạn điện giải'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ',
        'Đo nồng độ carbamazepine trong máu (nguy hiểm nếu >40 mcg/ml)',
        'Xử trí co giật: benzodiazepine (diazepam, lorazepam) hoặc phenobarbital',
        'Xử trí block nhĩ thất: atropine, pacemaker nếu cần',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp',
        'Lọc máu: không hiệu quả (gắn protein cao), nhưng có thể xem xét ở trường hợp nặng'
        , 'Theo dõi công thức máu (nguy cơ giảm bạch cầu)'], 'monitoring':
        'Theo dõi liên tục ý thức, hô hấp, tim mạch, điện tâm đồ, nồng độ carbamazepine trong máu, công thức máu, chức năng gan, điện giải'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống với thức ăn hoặc ngay sau bữa ăn để giảm kích ứng dạ dày và tăng hấp thu'
        , 'timing':
        'Chia liều 2-3 lần/ngày. Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. Không bỏ liều.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [],
        }}, 'pediatric_dosing': {'neonates':
        'Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế). Nếu cần: 5-10mg/kg/ngày PO chia 2-3 lần, tăng dần. Theo dõi nồng độ chặt chẽ.',
        'infants':
        '1 tháng - 2 tuổi: 10-20mg/kg/ngày PO chia 2-3 lần. Theo dõi nồng độ chặt chẽ. Tự cảm ứng enzyme → liều cần tăng dần theo thời gian.',
        'children':
        '2-12 tuổi: 10-20mg/kg/ngày PO chia 2-3 lần (tối đa 1000mg/ngày). Theo dõi nồng độ trong máu (mục tiêu 4-12 mcg/mL). Tự cảm ứng enzyme → liều cần tăng dần sau 2-4 tuần. Theo dõi công thức máu, chức năng gan.',
        'adolescents':
        '≥12 tuổi: Liều người lớn. 200-400mg x 2-3 lần/ngày, tăng dần đến 800-1600mg/ngày. Theo dõi nồng độ trong máu. Tự cảm ứng enzyme → liều cần tăng dần sau 2-4 tuần.',
        'notes':
        'Theo dõi nồng độ trong máu chặt chẽ (therapeutic range: 4-12 mcg/mL). Tự cảm ứng enzyme (auto-induction) → nồng độ có thể giảm sau 2-4 tuần, cần tăng liều. Theo dõi công thức máu (giảm bạch cầu, giảm tiểu cầu, thiếu máu bất sản). Theo dõi dấu hiệu hội chứng Stevens-Johnson (phát ban nặng).'}, 'geriatric_dosing': {'considerations':
        'Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (chóng mặt, ataxia, lú lẫn). Tăng nguy cơ hạ natri máu. Suy gan, suy thận phổ biến hơn. Tự cảm ứng enzyme có thể chậm hơn.',
        'dose_adjustment':
        'Khởi đầu với liều thấp hơn (100-200mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng gan, thận: CrCl <30 → giảm liều, theo dõi nồng độ. Theo dõi natri máu (hạ natri máu thường gặp).',
        'monitoring':
        'Theo dõi nồng độ trong máu thường xuyên (đặc biệt sau 2-4 tuần khi tự cảm ứng enzyme). Theo dõi công thức máu (giảm bạch cầu, giảm tiểu cầu). Theo dõi natri máu (hạ natri máu thường gặp). Theo dõi chức năng gan (ALT, AST). Theo dõi dấu hiệu hội chứng Stevens-Johnson (phát ban nặng).'}, 'brand_names': {'vietnam': [
        'Carbamazepine', 'Tegretol', 'Carbamazepine Stada', 'Carba'], 'common': [
        'Tegretol', 'Carbamazepine'],
        'range': '8,000 - 30,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Carbamazepine generic thường rẻ hơn (8,000-20,000 VND/viên 200mg). Tegretol (brand) thường đắt hơn (20,000-30,000 VND/viên 200mg).'}, 'references': {'primary_sources': ['Lexicomp - Carbamazepine',
        'UpToDate - Carbamazepine: Drug information',
        'FDA - Tegretol (carbamazepine) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        },
        "reversal_agents": {
             "available": False,
             "agents": []
         },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "dermatologic", "hematologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood levels", "CBC", "LFT", "Sodium levels"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Stevens-Johnson Syndrome/TEN",
            "FDA Black Box Warning - Aplastic Anemia/Agranulocytosis",
            "AAN 2018 Epilepsy Guidelines",
            "ISMP High Alert Medications - Anticonvulsants"
        ]
},
    "Ethosuximide": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Ethosuximide, Zarontin",
        "administration": ["PO"],
        "indications": [
            "Absence seizures (petit mal)",
            "Động kinh vắng ý thức",
            "Động kinh ở trẻ em"
        ],
        "contraindications": [
            "Dị ứng ethosuximide",
            "Suy gan nặng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult": "500-1500mg/ngày PO chia 2-3 lần/ngày",
            "pediatric_3_6": "250mg/ngày PO, tăng dần 250mg mỗi 4-7 ngày đến 20mg/kg/ngày",
            "pediatric_6_12": "250mg x 2 lần/ngày PO, tăng dần đến 20mg/kg/ngày",
            "pediatric_max": "1500mg/ngày",
            "notes": "Theo dõi nồng độ trong máu (mục tiêu 40-100 mcg/mL). Bắt đầu liều thấp, tăng dần."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Buồn ngủ",
            "Đau đầu",
            "Ban da (hiếm, có thể nặng)",
            "Rối loạn tâm thần (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Suy tủy xương (rất hiếm)"
        ],
        "interactions": [
            "Valproate: tăng nồng độ ethosuximide",
            "Carbamazepine, Phenytoin: giảm nồng độ ethosuximide",
            "Isoniazid: tăng nồng độ ethosuximide"
        ],
        ',
        "pregnancy": "C - Thận trọng",
        ',
        "mechanism_of_action": "Ethosuximide là thuốc chống động kinh chuyên biệt cho absence seizures (petit mal). Cơ chế tác dụng: ức chế kênh calci T-type (low-voltage activated calcium channels) ở đồi thị (thalamus), ngăn cản sự phóng điện bất thường đặc trưng của absence seizures. Kênh calci T-type đóng vai trò quan trọng trong việc tạo ra các sóng phóng điện 3Hz đặc trưng của absence seizures. Ethosuximide không có tác dụng với các loại động kinh khác (tonic-clonic, partial seizures). Đây là thuốc lựa chọn hàng đầu cho absence seizures ở trẻ em và người lớn.",
        "monitoring": [
            "Nồng độ ethosuximide trong máu (therapeutic range: 40-100 mcg/mL) - QUAN TRỌNG",
            "Tần suất và mức độ absence seizures",
            "Dấu hiệu độc tính (buồn nôn, nôn, chóng mặt, buồn ngủ quá mức)",
            "Công thức máu (giảm bạch cầu, suy tủy xương - rất hiếm nhưng nguy hiểm)",
            "Dấu hiệu ban da (có thể nặng, cần ngừng ngay)",
            "Dấu hiệu rối loạn tâm thần (hiếm)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Chức năng thận (creatinine)"
        ],
        "precautions": [
            "THEO DÕI NỒNG ĐỘ TRONG MÁU định kỳ (therapeutic range: 40-100 mcg/mL)",
            "KHÔNG được ngừng đột ngột (nguy cơ tăng co giật) - giảm liều dần dần",
            "Nguy cơ suy tủy xương (rất hiếm nhưng nguy hiểm) - theo dõi công thức máu",
            "Nguy cơ ban da nặng - ngừng ngay nếu có phát ban",
            "Tương tác với valproate (tăng nồng độ ethosuximide) - có thể cần giảm liều",
            "Tương tác với carbamazepine, phenytoin (giảm nồng độ ethosuximide) - có thể cần tăng liều",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Thận trọng ở suy gan, suy thận (giảm liều)"
        ],
        "pharmacokinetics": {
            "half_life": "30-60 giờ (dài)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "0% (không gắn protein)",
            "metabolism": "Gan (CYP3A4, CYP2E1) - chuyển hóa thành chất không hoạt động",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Half-life dài cho phép dùng 2-3 lần/ngày."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ suy tủy xương (rất hiếm nhưng có thể gây tử vong). Nguy cơ ban da nặng (Stevens-Johnson syndrome, toxic epidermal necrolysis). Theo dõi công thức máu và dấu hiệu ban da.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Valproate",
                    "mechanism": "Valproate ức chế chuyển hóa ethosuximide, tăng nồng độ ethosuximide",
                    "effect": "Tăng nồng độ ethosuximide, tăng độc tính",
                    "management": "Giảm liều ethosuximide 25-50%. Theo dõi nồng độ ethosuximide. Theo dõi dấu hiệu độc tính."
                }
            ],
            "moderate": [
                {
                    "drug": "Carbamazepine, Phenytoin",
                    "mechanism": "Cảm ứng enzyme CYP450, tăng chuyển hóa ethosuximide",
                    "effect": "Giảm nồng độ ethosuximide, giảm hiệu quả",
                    "management": "Tăng liều ethosuximide nếu cần. Theo dõi nồng độ ethosuximide và đáp ứng điều trị."
                },
                {
                    "drug": "Isoniazid",
                    "mechanism": "Isoniazid ức chế chuyển hóa ethosuximide",
                    "effect": "Tăng nồng độ ethosuximide, tăng độc tính",
                    "management": "Thận trọng. Theo dõi nồng độ ethosuximide. Có thể cần giảm liều ethosuximide."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ethosuximide",
                "Suy gan nặng (Child-Pugh C)",
                "Suy thận nặng (CrCl <15)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều, theo dõi chặt chẽ",
                "Suy thận (CrCl 15-30) - giảm liều 50%, theo dõi nồng độ",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ethosuximide là category C. Có nguy cơ dị tật bẩm sinh (thấp hơn một số thuốc chống động kinh khác). Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Cần bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Ethosuximide bài tiết vào sữa mẹ ở nồng độ đáng kể. Nồng độ trong sữa mẹ khoảng 80-90% nồng độ trong huyết thanh mẹ. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan và nồng độ trong máu",
            "moderate": "Giảm liều 25-50%, theo dõi nồng độ trong máu thường xuyên, theo dõi ALT/AST",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ. Theo dõi nồng độ trong máu và ALT/AST thường xuyên.",
            "notes": "Ethosuximide chuyển hóa ở gan qua CYP3A4 và CYP2E1. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ sâu, hôn mê, mất phản xạ",
                "Rối loạn tiêu hóa: buồn nôn, nôn",
                "Rối loạn tim mạch: nhịp chậm, hạ huyết áp",
                "Rối loạn hô hấp: suy hô hấp (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần",
                "Lọc máu (hemodialysis): có thể hiệu quả (protein binding 0%, bài tiết qua thận một phần)"
            ],
            "monitoring": "Theo dõi liên tục ý thức, hô hấp, tim mạch, nồng độ ethosuximide trong máu, chức năng gan, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày và buồn nôn",
                "timing": "Chia 2-3 lần/ngày. Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. KHÔNG ngừng đột ngột - giảm liều dần dần."
            }
        },
        "pediatric_dosing": {
            "children_3_6": "250mg/ngày PO, tăng dần 250mg mỗi 4-7 ngày đến 20mg/kg/ngày (tối đa 1000mg/ngày)",
            "children_6_12": "250mg x 2 lần/ngày PO, tăng dần đến 20mg/kg/ngày (tối đa 1500mg/ngày)",
            "adolescents": "500mg/ngày PO, tăng dần đến 20mg/kg/ngày (tối đa 1500mg/ngày)",
            "notes": "Theo dõi nồng độ trong máu chặt chẽ (therapeutic range: 40-100 mcg/mL). Bắt đầu liều thấp, tăng dần chậm. KHÔNG ngừng đột ngột - giảm liều dần dần."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt). Suy gan, suy thận phổ biến hơn. Tăng nguy cơ ngã (do buồn ngủ, chóng mặt).",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (250mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng gan, thận: CrCl 30-60 → giảm liều 25%, CrCl <30 → giảm liều 50%. Theo dõi nồng độ chặt chẽ.",
            "monitoring": "Theo dõi nồng độ trong máu thường xuyên hơn. Theo dõi dấu hiệu độc tính (buồn ngủ quá mức, chóng mặt). Theo dõi nguy cơ ngã. Theo dõi chức năng gan (ALT, AST). Theo dõi chức năng thận (creatinine, CrCl)."
        },
        "brand_names": {
            "vietnam": ["Ethosuximide", "Zarontin"],
            "common": ["Zarontin", "Ethosuximide"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "10,000 - 30,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Ethosuximide generic thường rẻ (10,000-20,000 VND/viên 250mg). Zarontin (brand) thường đắt hơn (20,000-30,000 VND/viên 250mg)."
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Ethosuximide",
                "UpToDate - Ethosuximide: Drug information",
                "FDA - Zarontin (ethosuximide) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood levels", "CBC"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "AAN 2018 Epilepsy Guidelines"
        ]
    },
    
    "Fosphenytoin": {
        "group": "Neurology - Anticonvulsant (Phenytoin Prodrug)",
        "vietnamese_name": "Fosphenytoin, Cerebyx",
        "administration": ["IV", "IM"],
        "indications": [
            "Status epilepticus (thay thế phenytoin IV khi không thể dùng phenytoin)",
            "Động kinh (khi không thể dùng phenytoin PO)",
            "Dự phòng co giật trong phẫu thuật thần kinh",
            "Điều trị co giật khi không có đường uống"
        ],
        "contraindications": [
            "Dị ứng fosphenytoin hoặc phenytoin",
            "Suy gan nặng",
            "Block nhĩ thất độ II hoặc III",
            "Hội chứng bệnh lympho",
            "Porphyria"
        ],
        "dosage": {
            "adult_status_epilepticus_iv": "15-20 mg PE/kg IV (PE = phenytoin equivalents, tối đa 1.5g PE)",
            "adult_status_epilepticus_im": "15-20 mg PE/kg IM (khi không có đường IV)",
            "adult_maintenance_iv": "4-6 mg PE/kg/ngày IV chia 2-3 lần",
            "adult_maintenance_im": "4-6 mg PE/kg/ngày IM chia 2-3 lần",
            "pediatric_status_epilepticus": "15-20 mg PE/kg IV hoặc IM",
            "notes": "Fosphenytoin được chuyển đổi thành phenytoin trong cơ thể. Liều tính theo PE (phenytoin equivalents): 1.5mg fosphenytoin = 1mg phenytoin. Tốc độ truyền: tối đa 150 mg PE/phút IV (nhanh hơn phenytoin)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Tương tự phenytoin nhưng ít hơn:",
            "Hạ huyết áp (ít hơn phenytoin IV)",
            "Rối loạn nhịp tim (ít hơn phenytoin IV)",
            "Đau, kích ứng tại chỗ tiêm (ít hơn phenytoin IV)",
            "Ngứa, cảm giác nóng rát (đặc biệt ở vùng háng, bẹn) - do phosphate",
            "Chóng mặt, buồn nôn",
            "Nystagmus, ataxia (liều cao)",
            "Ban da (có thể nặng - SJS/TEN)",
            "Hạ bạch cầu, tăng men gan"
        ],
        "interactions": [
            "Tương tự phenytoin:",
            "Warfarin: giảm tác dụng warfarin",
            "Oral contraceptives: giảm hiệu quả",
            "Folic acid: giảm nồng độ phenytoin",
            "Many drugs: cảm ứng CYP450"
        ],
        "pregnancy": "D - Nguy cơ dị tật thai nhi (tương tự phenytoin)",
        "mechanism_of_action": "Fosphenytoin là prodrug (tiền chất) của phenytoin. Fosphenytoin được chuyển đổi thành phenytoin trong cơ thể bởi enzyme phosphatase (chuyển đổi nhanh, thời gian bán thải chuyển đổi 8-15 phút). Sau khi chuyển đổi, fosphenytoin có tác dụng giống hệt phenytoin: ức chế kênh natri voltage-gated trong màng tế bào thần kinh, ngăn cản sự lan truyền của các xung động bất thường. ƯU ĐIỂM so với phenytoin IV: (1) Có thể truyền nhanh hơn (tối đa 150 mg PE/phút so với 50 mg/phút của phenytoin), (2) Ít gây kích ứng mạch máu (pH trung tính so với pH kiềm của phenytoin), (3) Có thể dùng IM (phenytoin không dùng được IM), (4) Ít gây hạ huyết áp và rối loạn nhịp tim hơn.",
        "monitoring": [
            "Nồng độ phenytoin trong máu (therapeutic range: 10-20 mcg/ml, free: 1-2 mcg/ml) - QUAN TRỌNG",
            "Tần suất và mức độ co giật",
            "Dấu hiệu độc tính (nystagmus, ataxia, lú lẫn)",
            "Huyết áp và nhịp tim (ít hơn phenytoin IV nhưng vẫn cần theo dõi)",
            "Chức năng gan (ALT, AST, bilirubin)",
            "Công thức máu (giảm bạch cầu, giảm tiểu cầu)",
            "Dấu hiệu hội chứng Stevens-Johnson (phát ban nặng)",
            "Ngứa, cảm giác nóng rát (đặc biệt ở vùng háng, bẹn) - do phosphate"
        ],
        "precautions": [
            "Liều tính theo PE (phenytoin equivalents): 1.5mg fosphenytoin = 1mg phenytoin",
            "Tốc độ truyền: tối đa 150 mg PE/phút IV (nhanh hơn phenytoin)",
            "Có thể dùng IM (ưu điểm so với phenytoin)",
            "Ít gây kích ứng mạch máu hơn phenytoin IV (pH trung tính)",
            "Ít gây hạ huyết áp và rối loạn nhịp tim hơn phenytoin IV",
            "Ngứa, cảm giác nóng rát (đặc biệt ở vùng háng, bẹn) - do phosphate, thường tự hết",
            "Theo dõi nồng độ phenytoin trong máu (sau khi chuyển đổi)",
            "Tương tác thuốc tương tự phenytoin"
        ],
        "pharmacokinetics": {
            "half_life": "Chuyển đổi: 8-15 phút (fosphenytoin → phenytoin). Phenytoin: 22 giờ (sau chuyển đổi)",
            "onset": "15-30 phút (sau khi chuyển đổi thành phenytoin)",
            "duration": "Dài (phụ thuộc liều, tương tự phenytoin)",
            "protein_binding": "Fosphenytoin: 95-99% (tạm thời), Phenytoin: 90% (sau chuyển đổi)",
            "clearance": "Chuyển đổi nhanh thành phenytoin bởi phosphatase, sau đó chuyển hóa ở gan (CYP2C9, CYP2C19)"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Dung dịch đã pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "Nguy cơ hội chứng Stevens-Johnson và hoại tử thượng bì nhiễm độc (TEN), có thể tử vong. Ngừng ngay nếu có phát ban. Nguy cơ tự sát và hành vi tự sát. Giảm bạch cầu, giảm tiểu cầu có thể nặng. Ngừng đột ngột có thể gây status epilepticus. (Tương tự phenytoin)",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Phenytoin (sau chuyển đổi) cảm ứng CYP2C9, tăng chuyển hóa warfarin",
                    "effect": "Giảm tác dụng chống đông, giảm INR",
                    "management": "Tăng liều warfarin, theo dõi INR thường xuyên."
                },
                {
                    "drug": "Oral contraceptives",
                    "mechanism": "Phenytoin cảm ứng CYP3A4, tăng chuyển hóa estrogen và progestin",
                    "effect": "Giảm hiệu quả tránh thai, tăng nguy cơ mang thai",
                    "management": "Sử dụng biện pháp tránh thai bổ sung hoặc chuyển sang thuốc tránh thai liều cao hơn."
                }
            ],
            "moderate": [
                {
                    "drug": "Valproate",
                    "mechanism": "Ức chế chuyển hóa phenytoin, tăng nồng độ free phenytoin",
                    "effect": "Tăng nồng độ free phenytoin, tăng nguy cơ độc tính",
                    "management": "Giảm liều fosphenytoin 25-50%, theo dõi nồng độ free phenytoin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fosphenytoin hoặc phenytoin",
                "Suy gan nặng (Child-Pugh C)",
                "Block nhĩ thất độ II hoặc III",
                "Hội chứng bệnh lympho",
                "Porphyria",
                "Tiền sử hội chứng Stevens-Johnson do phenytoin"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình - giảm liều, theo dõi chặt chẽ",
                "Suy thận nặng - giảm liều 50%",
                "Bệnh nhân cao tuổi - tăng nhạy cảm, giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Fosphenytoin là thuốc phân loại D (tương tự phenytoin). Có bằng chứng về nguy cơ dị tật thai nhi (hội chứng fetal hydantoin). Tuy nhiên, trong status epilepticus, lợi ích cứu sống mẹ vượt quá nguy cơ cho thai nhi. Status epilepticus có thể gây tử vong cho cả mẹ và thai nhi nếu không điều trị.",
            "lactation": {
                "safety": "Compatible",
                "details": "Phenytoin (sau chuyển đổi) bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ bú mẹ về dấu hiệu an thần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa ở gan sau chuyển đổi)",
            "severe": "Thận trọng, giảm liều (giảm chuyển hóa phenytoin)",
            "notes": "Fosphenytoin chuyển đổi thành phenytoin, sau đó chuyển hóa ở gan. Suy gan làm giảm chuyển hóa phenytoin, tăng nồng độ và tác dụng. Giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Tương tự phenytoin:",
                "Nystagmus (>20 mcg/ml)",
                "Ataxia (>30 mcg/ml)",
                "Lú lẫn (>40 mcg/ml)",
                "Hạ huyết áp (ít hơn phenytoin IV)",
                "Rối loạn nhịp tim (ít hơn phenytoin IV)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng fosphenytoin",
                "Theo dõi nồng độ phenytoin trong máu",
                "Nếu hạ huyết áp:",
                "  - Bù dịch (NS, LR)",
                "  - Vasopressor nếu cần",
                "Nếu rối loạn nhịp tim:",
                "  - Điều trị theo protocol rối loạn nhịp",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi: Nồng độ phenytoin, huyết áp, nhịp tim, ECG"
            ],
            "monitoring": "Theo dõi nồng độ phenytoin, huyết áp, nhịp tim, ECG liên tục cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Điều trị hỗ trợ. Fosphenytoin tự chuyển đổi thành phenytoin và được chuyển hóa."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp dung dịch đã pha sẵn (50 mg PE/ml).",
                "infusion_rate": "Status epilepticus: 15-20 mg PE/kg IV, tốc độ tối đa 150 mg PE/phút (nhanh hơn phenytoin). Maintenance: 4-6 mg PE/kg/ngày IV chia 2-3 lần.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."
                ],
                "notes": "QUAN TRỌNG: 1) Liều tính theo PE (phenytoin equivalents): 1.5mg fosphenytoin = 1mg phenytoin, 2) Tốc độ truyền: tối đa 150 mg PE/phút IV (nhanh hơn phenytoin 50 mg/phút), 3) Ít gây kích ứng mạch máu hơn phenytoin IV (pH trung tính), 4) Ít gây hạ huyết áp và rối loạn nhịp tim hơn phenytoin IV, 5) Ngứa, cảm giác nóng rát (đặc biệt ở vùng háng, bẹn) - do phosphate, thường tự hết, 6) Theo dõi nồng độ phenytoin trong máu (sau khi chuyển đổi)."
            },
            "im": {
                "reconstitution": "Dùng trực tiếp dung dịch đã pha sẵn (50 mg PE/ml).",
                "injection_site": "Cơ lớn (đùi, cánh tay).",
                "notes": "IM: 15-20 mg PE/kg (status epilepticus), 4-6 mg PE/kg/ngày chia 2-3 lần (maintenance). Tác dụng chậm hơn IV (30-45 phút). Ưu điểm: có thể dùng khi không có đường IV (phenytoin không dùng được IM)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fosphenytoin (Cerebyx)",
                "ACLS Guidelines 2020 - American Heart Association",
                "Status Epilepticus Guidelines",
                "UpToDate - Fosphenytoin: Drug Information",
                "Medscape - Fosphenytoin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, status epilepticus guidelines"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "dermatologic", "hematologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum phenytoin levels", "Liver function", "CBC", "Skin rash"]
        },
        "guideline_tags": [
            "AAN 2018 Epilepsy Guidelines",
            "FDA Black Box Warning - Stevens-Johnson Syndrome",
            "FDA Black Box Warning - Suicidal Behavior",
            "ISMP High Alert Medications - Anticonvulsants"
        ]
    },
    "Lacosamide": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Lacosamide, Vimpat",
        "administration": ["PO", "IV"],
        "indications": [
            "Động kinh cục bộ",
            "Động kinh tổng quát",
            "Status epilepticus (IV)"
        ],
        "contraindications": [
            "Dị ứng lacosamide",
            "Suy gan nặng",
            "Suy thận nặng (CrCl <30)"
        ],
        "dosage": {
            "adult_po_initial": "50mg x 2 lần/ngày, tăng dần mỗi tuần",
            "adult_po_maintenance": "100-200mg x 2 lần/ngày (tối đa 400mg/ngày)",
            "adult_iv": "200-400mg IV mỗi 12 giờ",
            "pediatric_po": "2-6mg/kg/ngày chia 2 lần (tối đa 12mg/kg/ngày)",
            "notes": "Thuốc mới, cơ chế độc đáo. Có dạng uống và IV. Ít tương tác thuốc hơn các anticonvulsants cổ điển."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Giảm liều 50%",
            "hemodialysis": "Bổ sung liều sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Chóng mặt (phổ biến)",
            "Nhức đầu",
            "Buồn nôn",
            "Mệt mỏi",
            "Nhìn đôi (diplopia)",
            "Rối loạn nhịp tim (hiếm, nhưng quan trọng - PR kéo dài, block AV)",
            "Rối loạn tâm thần (hiếm)"
        ],
        "interactions": [
            "Ít tương tác - không cảm ứng hoặc ức chế CYP450 mạnh",
            "Carbamazepine, Phenytoin: có thể giảm nhẹ nồng độ lacosamide",
            "Thuốc ức chế dẫn truyền nhĩ thất: tăng nguy cơ block AV"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Thuốc chống co giật thế hệ mới, cơ chế độc đáo: 1) Gắn với protein collapsin response mediator protein 2 (CRMP-2), làm chậm quá trình phosphoryl hóa CRMP-2, ức chế sự phát triển và tái tạo của sợi trục thần kinh, giảm tính kích thích của tế bào thần kinh. 2) Tăng hoạt động kênh natri voltage-gated chậm (slow inactivation), làm giảm tính kích thích của tế bào thần kinh. Không ảnh hưởng đến kênh natri nhanh như các thuốc chống co giật cổ điển. Đặc điểm: cơ chế độc đáo, ít tương tác thuốc, có dạng IV cho status epilepticus.",
        "monitoring": [
            "Tần suất và mức độ co giật",
            "ECG - quan trọng (nguy cơ PR kéo dài, block AV)",
            "Nhịp tim, huyết áp",
            "Dấu hiệu độc tính: chóng mặt, nhức đầu, mệt mỏi, nhìn đôi",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều ở suy thận",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu rối loạn tâm thần (hiếm)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột (nguy cơ co giật) - giảm liều dần dần trong vài tuần",
            "Nguy cơ rối loạn nhịp tim (PR kéo dài, block AV) - theo dõi ECG, đặc biệt ở bệnh nhân có bệnh tim",
            "Thận trọng ở bệnh nhân có bệnh tim, block AV độ 1, hoặc dùng thuốc ức chế dẫn truyền nhĩ thất",
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Có thể gây chóng mặt, nhức đầu - thận trọng khi lái xe, vận hành máy móc",
            "Ít tương tác thuốc hơn các anticonvulsants cổ điển (không cảm ứng CYP450 mạnh)",
            "Khởi đầu với liều thấp, tăng dần chậm để giảm tác dụng phụ",
            "Dạng IV: truyền trong 30-60 phút, không truyền nhanh hơn"
        ],
        "pharmacokinetics": {
            "half_life": "13 giờ",
            "onset": "Nhanh (vài giờ đến vài ngày)",
            "duration": "Dài (do half-life 13 giờ)",
            "protein_binding": "<15% (rất thấp)",
            "metabolism": "Gan (chuyển hóa một phần qua CYP2C19, CYP3A4, CYP2C9 - nhưng không cảm ứng mạnh)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ 40% nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng IV: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
        "black_box_warnings": "Nguy cơ rối loạn nhịp tim (PR kéo dài, block nhĩ thất độ 1, 2, hoặc 3). Theo dõi ECG trước và sau khi bắt đầu điều trị, đặc biệt ở bệnh nhân có bệnh tim hoặc dùng thuốc ức chế dẫn truyền nhĩ thất.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc ức chế dẫn truyền nhĩ thất (verapamil, diltiazem, beta-blockers)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng",
                    "management": "Thận trọng. Theo dõi ECG sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Carbamazepine, Phenytoin",
                    "mechanism": "Có thể cảm ứng nhẹ chuyển hóa lacosamide",
                    "effect": "Giảm nhẹ nồng độ lacosamide",
                    "management": "Có thể cần tăng liều lacosamide nếu không đạt hiệu quả."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng lacosamide",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Suy gan nặng (Child-Pugh C)",
                "Suy thận nặng (CrCl <15)"
            ],
            "tương_đối": [
                "Bệnh tim, block AV độ 1 - tăng nguy cơ block AV nặng hơn",
                "Suy thận (CrCl 15-30) - giảm liều 50%",
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng",
                "Dùng với thuốc ức chế dẫn truyền nhĩ thất - tăng nguy cơ block AV",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Lacosamide là category C. Chứng cứ về an toàn trong thai kỳ còn hạn chế. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Lacosamide bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa một phần qua gan)",
            "notes": "Lacosamide chuyển hóa một phần qua gan (CYP2C19, CYP3A4, CYP2C9). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: chóng mặt nặng, nhức đầu, mệt mỏi, nhìn đôi",
                "Rối loạn nhịp tim: PR kéo dài, block AV, nhịp tim chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Theo dõi ECG liên tục (quan trọng - nguy cơ block AV)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Điều trị block AV nếu có: Atropine, nếu cần: máy tạo nhịp tạm thời",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, ECG",
                "Lọc máu (hemodialysis): có thể hiệu quả (protein binding <15%, bài tiết qua thận một phần)"
            ],
            "monitoring": "Theo dõi liên tục ECG, nhịp tim, huyết áp, ý thức, hô hấp trong ít nhất 24 giờ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Chia 2 lần/ngày (sáng và tối). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. KHÔNG ngừng đột ngột - giảm liều dần dần trong vài tuần."
            },
            "iv": {
                "reconstitution": "Pha trong 0.9% NaCl hoặc D5W. Nồng độ pha: 10mg/ml. Pha 200mg trong 20ml = 10mg/ml.",
                "infusion_rate": "Truyền trong 30-60 phút. Tốc độ: 20ml/30 phút = ~0.67ml/phút. KHÔNG truyền nhanh hơn.",
                "compatibility": ["0.9% NaCl", "D5W"],
                "incompatibility": [],
                "notes": "QUAN TRỌNG: 1) Truyền trong 30-60 phút, không truyền nhanh hơn, 2) Theo dõi ECG (nguy cơ block AV), 3) Theo dõi nhịp tim, huyết áp."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vimpat (lacosamide)",
                "UpToDate - Lacosamide: Drug information",
                "Lexicomp - Lacosamide"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "dermatologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["LFT", "CBC", "Drug levels"]
        },
        "guideline_tags": [
            "AAN 2018 Epilepsy Guidelines",
            "FDA - Antiepileptic drug safety"
        ]
    },
    
    "Lamotrigine": {'group': 'Neurology - Anticonvulsant', 'vietnamese_name':
        'Lamotrigine, Lamictal', 'administration': ['PO'], 'indications': [
        'Động kinh cục bộ', 'Động kinh tổng quát',
        'Rối loạn lưỡng cực (phòng ngừa tái phát trầm cảm)'],
        'contraindications': ['Dị ứng', 'Ban da nặng trước đây (SJS/TEN)'],
        'dosage': {'adult_epilepsy':
        '25mg x 2 lần/ngày x 2 tuần, tăng đến 100-200mg x 2 lần/ngày',
        'adult_bipolar': '25mg/ngày, tăng chậm đến 100-200mg/ngày', 'adult_max':
        '400mg/ngày', 'notes':
        'Tăng liều rất chậm để tránh ban da. Nếu dùng với valproate: giảm liều 50%'
        }, 'side_effects': [
        'Ban da (có thể nặng - SJS/TEN, đặc biệt khi tăng liều nhanh)',
        'Nhức đầu', 'Chóng mặt', 'Buồn nôn', 'Mất ngủ', 'Rối loạn thị giác'],
        'interactions': [
        'Valproate: tăng nồng độ lamotrigine (giảm liều lamotrigine 50%)',
        'Carbamazepine: giảm nồng độ lamotrigine',
        'Oral contraceptives: giảm nồng độ lamotrigine (tăng liều)'],
        'pregnancy': 'C', 'mechanism_of_action':
        'Lamotrigine ức chế kênh natri voltage-gated, làm giảm giải phóng glutamate (chất dẫn truyền thần kinh kích thích) và làm giảm tính kích thích của tế bào thần kinh. Cũng có thể ức chế kênh calci. Tác dụng: chống động kinh (cục bộ và tổng quát), ổn định tâm trạng trong rối loạn lưỡng cực (phòng ngừa tái phát trầm cảm). Cơ chế chính xác chưa rõ hoàn toàn nhưng có liên quan đến ức chế giải phóng glutamate'
        , 'monitoring': [
        'Dấu hiệu ban da (RẤT QUAN TRỌNG) - ngừng ngay nếu có ban da, đặc biệt khi kèm sốt, mệt mỏi, đau khớp'
        'Ban da có thể tiến triển thành Stevens-Johnson syndrome (SJS) hoặc toxic epidermal necrolysis (TEN) - nguy hiểm tính mạng'
        'Nguy cơ ban da cao nhất trong 8 tuần đầu, đặc biệt khi tăng liều nhanh hoặc dùng với valproate'
        , 'Triệu chứng lâm sàng: nhức đầu, chóng mặt, buồn nôn (thường nhẹ)',
        'Chức năng gan nếu có triệu chứng (hiếm gây độc gan)',
        'Đáp ứng điều trị (động kinh hoặc tâm trạng)'], 'precautions': [
        'TĂNG LIỀU RẤT CHẬM để tránh ban da nghiêm trọng (SJS/TEN) - đây là tác dụng phụ nguy hiểm nhất'
        'NGỪNG NGAY nếu có ban da, đặc biệt kèm sốt, mệt mỏi, đau khớp (dấu hiệu SJS/TEN)'
        'Nếu dùng với valproate: giảm liều khởi đầu và tăng liều lamotrigine 50% (valproate tăng nồng độ lamotrigine)'
        'Nếu dùng với carbamazepine: tăng liều lamotrigine (carbamazepine giảm nồng độ)'
        'Nếu dùng với oral contraceptives: tăng liều lamotrigine (OCP giảm nồng độ)'
        , 'Không ngừng đột ngột (tăng nguy cơ co giật)',
        'Giảm liều dần nếu cần ngừng',
        'Thận trọng ở bệnh nhân suy gan, suy thận (giảm liều)',
        'Giáo dục bệnh nhân về dấu hiệu ban da và cần báo ngay'],
        'pharmacokinetics': {'half_life':
        '25-30 giờ (dài, cho phép dùng 1-2 lần/ngày)', 'onset':
        'Vài tuần (tác dụng chậm)', 'duration': 'Dài (do half-life dài)',
        'protein_binding': '55%', 'clearance':
        'Gan (chuyển hóa qua glucuronidation, không qua CYP450), thận (thải trừ)'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Nguy cơ ban da nghiêm trọng (Stevens-Johnson syndrome, toxic epidermal necrolysis) - có thể gây tử vong. Nguy cơ tăng khi tăng liều nhanh, dùng với valproate, hoặc vi phạm phác đồ tăng liều. Ngừng ngay nếu có ban da, đặc biệt kèm sốt, mệt mỏi, đau khớp'
        , 'drug_interactions': {'major': [{'drug': 'Valproate', 'mechanism':
        'Valproate ức chế glucuronidation của lamotrigine, tăng nồng độ lamotrigine đáng kể'
        , 'effect':
        'Tăng nguy cơ ban da nghiêm trọng (SJS/TEN) - nguy cơ cao nhất khi dùng cùng valproate'
        , 'management':
        'Giảm liều khởi đầu lamotrigine 50% khi dùng với valproate. Tăng liều rất chậm. Theo dõi sát dấu hiệu ban da.'
        }, {'drug': 'Oral contraceptives (estrogen)', 'mechanism':
        'Estrogen cảm ứng glucuronidation, tăng chuyển hóa lamotrigine',
        'effect':
        'Giảm nồng độ lamotrigine 40-50%, có thể gây mất kiểm soát động kinh',
        'management':
        'Tăng liều lamotrigine khi dùng OCP. Giảm liều khi ngừng OCP. Theo dõi nồng độ và điều chỉnh liều.'
        }, {'drug': 'Phenobarbital, Primidone', 'mechanism': 'Cảm ứng glucuronidation, tăng chuyển hóa lamotrigine',
        'effect': 'Giảm nồng độ lamotrigine', 'management':
        'Tăng liều lamotrigine nếu cần. Theo dõi nồng độ và điều chỉnh liều.'},
        {'drug': 'Rifampin', 'mechanism': 'Cảm ứng glucuronidation mạnh',
        'effect': 'Giảm nồng độ lamotrigine đáng kể', 'management':
        'Tăng liều lamotrigine. Theo dõi nồng độ và điều chỉnh liều.'}],
        'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng lamotrigine hoặc các thành phần khác',
        'Ban da nặng trước đây (SJS/TEN) với lamotrigine',
        'Tăng liều quá nhanh (vi phạm phác đồ tăng liều)'], 'tương_đối': [
        'Dùng với valproate - giảm liều khởi đầu 50%',
        'Trẻ em <16 tuổi - tăng nguy cơ ban da', 'Suy gan nặng - giảm liều',
        'Suy thận nặng (CrCl <30) - giảm liều',
        'Dùng với oral contraceptives - tăng liều lamotrigine']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ dị tật thai nhi thấp hơn valproate và carbamazepine. Tuy nhiên, vẫn có nguy cơ dị tật (cleft palate, dị tật tim). Nồng độ lamotrigine giảm trong thai kỳ (tăng clearance), có thể cần tăng liều. Theo dõi nồng độ lamotrigine trong thai kỳ. Nguy cơ rối loạn phát triển thần kinh thấp hơn valproate.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Lamotrigine bài tiết vào sữa mẹ ở nồng độ đáng kể (40-50% liều mẹ). Nồng độ trong máu trẻ bú mẹ có thể đạt 20-30% nồng độ mẹ. Có thể gây tác dụng phụ ở trẻ (ban da, buồn ngủ). Cần theo dõi trẻ sát.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu ban da, buồn ngủ, bú kém ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Giảm liều 50-75% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ',
        'notes':
        'Lamotrigine chuyển hóa ở gan qua glucuronidation. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan hơn valproate.'
        }, 'overdose_management': {'symptoms': [
        'Ban da (có thể tiến triển thành SJS/TEN)', 'Buồn nôn, nôn',
        'Chóng mặt, nhức đầu', 'Lú lẫn, co giật', 'Rung nhĩ', 'Hôn mê (hiếm)'],
        'antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment':
        ['Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi sát dấu hiệu ban da (SJS/TEN) - nguy hiểm nhất',
        'Điều trị hỗ trợ: chống nôn, truyền dịch, theo dõi điện giải',
        'Theo dõi ECG nếu có triệu chứng tim mạch', 'Điều trị co giật nếu có',
        'Hỗ trợ hô hấp và tuần hoàn nếu cần'], 'monitoring':
        'Dấu hiệu ban da (SJS/TEN), ECG, ý thức, dấu hiệu co giật, điện giải'},
        'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có SJS/TEN. Điều trị SJS/TEN tại ICU nếu có.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn', 'timing':
        'Chia 2 lần/ngày (do half-life dài). Có thể dùng cùng bữa ăn để giảm kích ứng dạ dày'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [],
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Lamictal (lamotrigine)',
        'UpToDate - Lamotrigine: Drug information',
        'Epilepsia - ILAE treatment guidelines',
        'American Academy of Neurology guidelines'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews'
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "dermatologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["LFT", "CBC", "Drug levels"]
        },
        "guideline_tags": [
            "AAN 2018 Epilepsy Guidelines",
            "FDA - Antiepileptic drug safety"
        ]
    },
    "Levetiracetam": {'group': 'Neurology - Anticonvulsant', 'vietnamese_name':
        'Levetiracetam, Keppra', 'administration': ['PO', 'IV'], 'indications':
        ['Động kinh cục bộ', 'Động kinh tổng quát', 'Status epilepticus (IV)'],
        'contraindications': ['Dị ứng'], 'dosage': {'adult_po':
        '500-1000mg x 2 lần/ngày, tăng đến 1000-3000mg/ngày', 'adult_iv':
        '500-1000mg IV mỗi 12 giờ', 'adult_max': '3000mg/ngày', 'notes':
        'Ít tương tác thuốc, an toàn cho trẻ em và người già'},
        'renal_adjustment': {'normal': 'Không đổi', '50_80': 'Giảm liều 25%',
        '30_50': 'Giảm liều 50%', 'under_30': 'Giảm liều 75%'}, 'side_effects':
        ['Buồn ngủ', 'Chóng mặt', 'Kích động, hành vi bất thường', 'Nhức đầu',
        'Mệt mỏi', 'Ít tác dụng phụ hơn các anticonvulsants khác'],
        'interactions': ['Ít tương tác - không cảm ứng hoặc ức chế CYP450'],
        'pregnancy': 'C', 'mechanism_of_action':
        'Thuốc chống co giật thế hệ mới, cơ chế chưa hoàn toàn rõ ràng. Gắn với protein SV2A (synaptic vesicle protein 2A) trong tế bào thần kinh, ức chế giải phóng chất dẫn truyền thần kinh từ túi synap, giảm hoạt động bất thường của tế bào thần kinh. Không ức chế kênh natri hoặc calci như các thuốc chống co giật cổ điển. Có phổ rộng: hiệu quả với co giật cục bộ và co giật toàn thể. Được dùng như thuốc bổ trợ hoặc đơn trị liệu. Ít tương tác thuốc hơn phenytoin.'
        , 'monitoring': ['Tần suất và mức độ co giật',
        'Tâm thần (kích động, lo âu, trầm cảm, suy nghĩ tự sát) - tác dụng phụ thần kinh tâm thần quan trọng'
        , 'Dấu hiệu hành vi bất thường (thay đổi tâm trạng, kích động)',
        'Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận',
        'Công thức máu (hiếm giảm bạch cầu, giảm tiểu cầu)',
        'Chức năng gan (ALT, AST) - hiếm viêm gan',
        'Mệt mỏi, chóng mặt (thường gặp)',
        'Dấu hiệu nhiễm trùng (hiếm giảm bạch cầu)'], 'precautions': [
        'Tác dụng phụ thần kinh tâm thần: kích động, lo âu, trầm cảm, suy nghĩ tự sát - theo dõi sát, đặc biệt ở trẻ em và thanh thiếu niên'
        , 'Nguy cơ hành vi tự sát - cảnh báo bệnh nhân và gia đình',
        'KHÔNG được ngừng đột ngột (nguy cơ co giật)',
        'Phải điều chỉnh liều ở suy thận (giảm liều và tăng khoảng cách liều)',
        'Khởi đầu với liều thấp, tăng dần để giảm tác dụng phụ',
        'Có thể gây mệt mỏi, chóng mặt - thận trọng khi lái xe, vận hành máy móc',
        'Tương tác thuốc ít hơn các thuốc chống co giật cổ điển (không ức chế CYP450)'
        , 'Có thể dùng với hoặc không có thức ăn',
        'Thận trọng ở bệnh nhân có tiền sử bệnh tâm thần',
        'Giảm liều ở người cao tuổi (nếu có suy thận)'], 'pharmacokinetics': {
        'half_life': '6-8 giờ (bình thường), 10-11 giờ (suy thận nặng)',
        'onset': 'Nhanh (vài giờ đến vài ngày)', 'duration':
        'Dài (phụ thuộc liều)', 'protein_binding': '< 10% (rất thấp)',
        'metabolism': 'Enzyme huyết tương (không qua CYP450) - ít tương tác',
        'clearance':
        'Chủ yếu qua thận (66% bài tiết nguyên dạng), cần điều chỉnh thận'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Viên nén: tránh ẩm.',
        'black_box_warnings':
        'Nguy cơ hành vi tự sát và ý tưởng tự sát. Cảnh báo bệnh nhân và gia đình về các dấu hiệu kích động, lo âu, trầm cảm, thay đổi tâm trạng, và hành vi bất thường. Ngừng đột ngột có thể gây co giật.'
        , 'drug_interactions': {'major': [], 'moderate': [{'drug':
        'Carbamazepine, Phenytoin, Phenobarbital', 'mechanism':
        'Cảm ứng enzyme, tăng chuyển hóa levetiracetam', 'effect':
        'Giảm nhẹ nồng độ levetiracetam', 'management':
        'Có thể cần tăng liều levetiracetam nếu không đạt hiệu quả.'}], 'minor':
        [{'drug': 'Probenecid', 'mechanism': 'Ức chế bài tiết qua thận',
        'effect': 'Tăng nhẹ nồng độ levetiracetam', 'management':
        'Giảm liều levetiracetam 50% nếu dùng chung.'}]}, 'contraindications':
        {'tuyệt_đối': ['Dị ứng levetiracetam hoặc các thành phần khác'],
        'tương_đối': [
        'Suy thận (CrCl <30) - giảm liều 75%, tăng khoảng cách liều',
        'Tiền sử bệnh tâm thần (tăng nguy cơ kích động, lo âu, trầm cảm)',
        'Bệnh nhân lớn tuổi có suy thận - giảm liều thêm',
        'Mang thai (chứng cứ hạn chế) - chỉ dùng nếu lợi ích > nguy cơ']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh (khoảng 2.5-3% so với 2% ở dân số chung), nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Levetiracetam bài tiết vào sữa mẹ ở nồng độ thấp (nồng độ trong sữa mẹ khoảng 50-100% nồng độ trong huyết thanh mẹ). Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm.'
        , 'recommendation':
        'Có thể cho con bú. Theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém).'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều (levetiracetam không chuyển hóa ở gan)',
        'moderate':
        'Không cần điều chỉnh liều (levetiracetam không chuyển hóa ở gan)',
        'severe':
        'Không cần điều chỉnh liều (levetiracetam không chuyển hóa ở gan). Tuy nhiên, thận trọng ở bệnh nhân suy gan kèm suy thận.'
        , 'notes':
        'Levetiracetam không chuyển hóa ở gan, bài tiết chủ yếu qua thận. Không cần điều chỉnh liều ở suy gan. Chỉ cần điều chỉnh liều ở suy thận.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, mất điều hòa (ataxia)'
        , 'Rối loạn hô hấp: suy hô hấp (hiếm)',
        'Rối loạn tiêu hóa: buồn nôn, nôn',
        'Triệu chứng khác: mệt mỏi, kích động'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp',
        'Lọc máu: có thể hiệu quả (không gắn protein, bài tiết qua thận), xem xét ở trường hợp nặng'
        ], 'monitoring':
        'Theo dõi ý thức, hô hấp, dấu hiệu thần kinh. Có thể đo nồng độ levetiracetam trong máu nếu có sẵn.'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.',
        'timing':
        'Chia liều 2 lần/ngày (sáng và tối). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. Không bỏ liều.'
        }, 'iv': {'reconstitution':
        'Dùng trực tiếp từ lọ, không cần pha. Có thể pha loãng trong 0.9% NaCl hoặc D5W đến nồng độ 15mg/ml.'
        , 'infusion_rate':
        'Truyền trong 15 phút (tốc độ tiêu chuẩn). Không truyền nhanh hơn.',
        'compatibility': ['0.9% NaCl', 'D5W'], 'incompatibility': [], 'notes':
        'Có thể truyền trực tiếp hoặc pha loãng. Theo dõi dấu hiệu phản ứng tại chỗ tiêm.'
        }},         'references': {'primary_sources': ['Lexicomp - Levetiracetam',
        'UpToDate - Levetiracetam: Drug information',
        'FDA - Keppra (levetiracetam) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        },
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['neurological', 'psychiatric'],
            'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Seizure frequency', 'Psychiatric symptoms', 'Renal function', 'CBC']
        },
        'guideline_tags': [
            'AAN 2018 Epilepsy Guidelines',
            'FDA Black Box Warning - Suicidal Behavior',
            'ISMP High Alert Medications - Anticonvulsants'
        ]
    },
    "Oxcarbazepine": {'group': 'Neurology - Anticonvulsant', 'vietnamese_name':
        'Oxcarbazepine, Trileptal', 'administration': ['PO'], 'indications': [
        'Động kinh cục bộ', 'Động kinh tổng quát',
        'Đau dây thần kinh sinh ba'],
        'contraindications': [
        'Dị ứng carbamazepine (cross-reactivity)'], 'dosage': {'adult_epilepsy':
        '300mg x 2 lần/ngày, tăng đến 600-1200mg x 2 lần/ngày',
        'adult_max': '2400mg/ngày', 'notes':
        'Tương tự carbamazepine nhưng ít tương tác thuốc hơn, ít tác dụng phụ hơn'
        }, 'side_effects': ['Chóng mặt', 'Buồn nôn', 'Buồn ngủ', 'Ataxia',
        'Hạ natri máu (thường gặp)', 'Ban da (ít hơn carbamazepine)',
        'Rối loạn thị giác'], 'interactions': [
        'Oral contraceptives: có thể giảm hiệu quả',
        'Ít tương tác hơn carbamazepine (không cảm ứng CYP450 mạnh)'], 'pregnancy':
        'C', 'mechanism_of_action':
        'Oxcarbazepine là dẫn xuất của carbamazepine, được chuyển hóa thành chất hoạt động 10-monohydroxy derivative (MHD). Cơ chế tương tự carbamazepine: ức chế kênh natri voltage-gated, ngăn cản sự lan truyền của các xung động bất thường. Khác với carbamazepine, oxcarbazepine không cảm ứng enzyme CYP450 mạnh, ít tương tác thuốc hơn. Cũng có thể ức chế kênh calci. Tác dụng: chống động kinh (cục bộ và tổng quát), điều trị đau dây thần kinh sinh ba. Ít tác dụng phụ hơn carbamazepine, đặc biệt ít ban da nghiêm trọng (SJS/TEN).'
        , 'monitoring': [
        'Tần suất và mức độ co giật',
        'Dấu hiệu độc tính (chóng mặt, ataxia, lú lẫn, buồn nôn)',
        'Nồng độ natri (hạ natri máu - thường gặp, có thể nặng)',
        'Chức năng thận (creatinine)',
        'Dấu hiệu ban da (ít hơn carbamazepine nhưng vẫn có thể xảy ra)',
        'Rối loạn thị giác'], 'precautions': [
        'Hạ natri máu thường gặp - theo dõi natri định kỳ, đặc biệt ở người cao tuổi và phụ nữ'
        , 'Ít tương tác thuốc hơn carbamazepine (không cảm ứng CYP450 mạnh)',
        'Vẫn có thể giảm hiệu quả thuốc tránh thai - sử dụng biện pháp bổ sung',
        'KHÔNG được ngừng đột ngột (nguy cơ co giật)',
        'Giảm liều dần dần nếu cần ngừng',
        'Thận trọng ở bệnh nhân suy thận (giảm thải trừ MHD)',
        'Thận trọng ở bệnh nhân có tiền sử dị ứng carbamazepine (cross-reactivity)'
        , 'Uống với thức ăn để giảm kích ứng dạ dày'], 'pharmacokinetics': {
        'half_life': '2 giờ (oxcarbazepine), 9 giờ (MHD - chất hoạt động)',
        'onset': 'Vài giờ đến vài ngày', 'duration': 'Dài (phụ thuộc liều)',
        'protein_binding': '40% (MHD)', 'metabolism':
        'Gan (chuyển hóa thành MHD, không qua CYP450 chính) - ít tương tác enzyme'
        , 'clearance':
        'Gan (chuyển hóa), thận (thải trừ MHD). Không cảm ứng CYP450 mạnh như carbamazepine.'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.'
        , 'black_box_warnings':
        'Nguy cơ hạ natri máu nghiêm trọng (có thể <125 mEq/L), đặc biệt ở người cao tuổi và phụ nữ. Nguy cơ ban da nghiêm trọng (SJS/TEN) - ít hơn carbamazepine nhưng vẫn có thể xảy ra. Ngừng đột ngột có thể gây co giật.'
        , 'drug_interactions': {'major': [{'drug': 'Oral contraceptives',
        'mechanism':
        'Oxcarbazepine có thể cảm ứng enzyme nhẹ, giảm nồng độ estrogen', 'effect':
        'Giảm hiệu quả tránh thai, tăng nguy cơ mang thai', 'management':
        'Sử dụng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang thuốc tránh thai liều cao hơn. Tư vấn bệnh nhân về nguy cơ.'
        }, {'drug': 'Phenobarbital, Phenytoin, Carbamazepine', 'mechanism':
        'Cảm ứng enzyme, tăng chuyển hóa MHD', 'effect':
        'Giảm nồng độ MHD, giảm hiệu quả', 'management':
        'Tăng liều oxcarbazepine nếu cần. Theo dõi nồng độ và điều chỉnh liều.'},
        {'drug': 'Felodipine, Verapamil', 'mechanism':
        'Có thể giảm nồng độ MHD', 'effect': 'Giảm hiệu quả oxcarbazepine',
        'management':
        'Theo dõi nồng độ và điều chỉnh liều nếu cần.'}], 'minor': [{'drug':
        'Cimetidine', 'mechanism': 'Có thể tăng nhẹ nồng độ MHD', 'effect':
        'Tăng nhẹ nồng độ MHD', 'management':
        'Theo dõi tác dụng phụ. Có thể cần giảm liều.'}]}, 'contraindications': {
        'tuyệt_đối': ['Dị ứng oxcarbazepine hoặc carbamazepine',
        'Ban da nặng trước đây (SJS/TEN) với oxcarbazepine hoặc carbamazepine'],
        'tương_đối': [
        'Suy thận nặng (CrCl <30) - giảm liều, tăng khoảng cách liều',
        'Suy gan nặng - giảm liều',
        'Mang thai (chứng cứ hạn chế) - chỉ dùng nếu lợi ích > nguy cơ',
        'Người cao tuổi - tăng nguy cơ hạ natri máu',
        'Phụ nữ - tăng nguy cơ hạ natri máu']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.'
        , 'lactation': {'safety': 'Compatible with monitoring', 'details':
        'Oxcarbazepine và MHD bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ bú mẹ có thể đạt 10-20% nồng độ mẹ. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém). Cần theo dõi trẻ sát.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, chậm tăng cân ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan'
        , 'moderate':
        'Giảm liều 25-50%, theo dõi chức năng gan thường xuyên', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ', 'notes':
        'Oxcarbazepine chuyển hóa ở gan thành MHD. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan hơn carbamazepine.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: chóng mặt, ataxia, lú lẫn, buồn ngủ, hôn mê, co giật'
        , 'Hạ natri máu: lú lẫn, co giật, hôn mê (có thể nặng)',
        'Rối loạn tiêu hóa: buồn nôn, nôn',
        'Rối loạn tim mạch: nhịp tim chậm, hạ huyết áp (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ',
        'Điều trị hạ natri máu: truyền NaCl 3% nếu natri <125 mEq/L và có triệu chứng'
        , 'Xử trí co giật: benzodiazepine (diazepam, lorazepam) nếu có',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp',
        'Lọc máu: có thể hiệu quả (gắn protein 40%), xem xét ở trường hợp nặng'
        ], 'monitoring':
        'Theo dõi liên tục ý thức, hô hấp, tim mạch, điện tâm đồ, nồng độ natri (quan trọng), chức năng thận'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống với thức ăn hoặc ngay sau bữa ăn để giảm kích ứng dạ dày và tăng hấp thu'
        , 'timing':
        'Chia liều 2 lần/ngày (sáng và tối). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. Không bỏ liều.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [],
        }}, 'pediatric_dosing': {'neonates':
        'Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế). Nếu cần: 8-10mg/kg/ngày PO chia 2 lần, tăng dần. Theo dõi chặt chẽ.'
        , 'infants':
        '1 tháng - 2 tuổi: 8-10mg/kg/ngày PO chia 2 lần, tăng đến 20-30mg/kg/ngày nếu cần. Theo dõi chặt chẽ.'
        , 'children':
        '2-12 tuổi: 8-10mg/kg/ngày PO chia 2 lần, tăng đến 20-30mg/kg/ngày nếu cần (tối đa 2400mg/ngày). Theo dõi nồng độ natri định kỳ.'
        , 'adolescents':
        '≥12 tuổi: Liều người lớn. 300mg x 2 lần/ngày, tăng đến 600-1200mg x 2 lần/ngày. Theo dõi nồng độ natri định kỳ.'
        , 'notes':
        'Theo dõi nồng độ natri định kỳ (hạ natri máu thường gặp). Theo dõi dấu hiệu độc tính (chóng mặt, ataxia, lú lẫn). KHÔNG ngừng đột ngột - giảm liều dần dần.'}, 'geriatric_dosing': {'considerations':
        'Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (chóng mặt, ataxia, lú lẫn). Tăng nguy cơ hạ natri máu. Suy gan, suy thận phổ biến hơn.'
        , 'dose_adjustment':
        'Khởi đầu với liều thấp hơn (150mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng gan, thận: CrCl <30 → giảm liều. Theo dõi natri máu thường xuyên.'
        , 'monitoring':
        'Theo dõi nồng độ natri thường xuyên (hạ natri máu thường gặp, có thể nặng). Theo dõi dấu hiệu độc tính (chóng mặt, ataxia, lú lẫn). Theo dõi chức năng gan, thận.'}, 'brand_names': {'vietnam': [
        'Oxcarbazepine', 'Trileptal', 'Oxcarbazepine Stada'], 'common': [
        'Trileptal', 'Oxcarbazepine'],
        'range': '15,000 - 50,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Oxcarbazepine generic thường rẻ hơn (15,000-30,000 VND/viên 300mg). Trileptal (brand) thường đắt hơn (30,000-50,000 VND/viên 300mg).'}, 'references': {'primary_sources': ['Lexicomp - Oxcarbazepine',
        'UpToDate - Oxcarbazepine: Drug information',
        'FDA - Trileptal (oxcarbazepine) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        },
        "reversal_agents": {
             "available": False,
             "agents": []
         },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
},
    "Perampanel": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Perampanel, Fycompa",
        "administration": ["PO"],
        "indications": [
            "Động kinh cục bộ",
            "Động kinh tổng quát",
            "Động kinh tonic-clonic",
            "Động kinh myoclonic"
        ],
        "contraindications": [
            "Dị ứng perampanel",
            "Suy gan nặng",
            "Suy thận nặng (CrCl <30)"
        ],
        "dosage": {
            "adult_initial": "2mg x 1 lần/ngày trước khi ngủ, tăng dần mỗi tuần",
            "adult_maintenance": "4-12mg x 1 lần/ngày (tối đa 12mg/ngày)",
            "pediatric_initial": "2mg/ngày, tăng dần",
            "pediatric_maintenance": "4-12mg/ngày (tối đa 12mg/ngày)",
            "notes": "Thuốc mới, cơ chế độc đáo (AMPA receptor antagonist). Uống trước khi ngủ để giảm tác dụng phụ. Tăng liều chậm để giảm tác dụng phụ thần kinh tâm thần."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Giảm liều 50%",
            "hemodialysis": "Bổ sung liều sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Chóng mặt (phổ biến)",
            "Buồn ngủ",
            "Mệt mỏi",
            "Kích động, hành vi bất thường (quan trọng)",
            "Lo âu, trầm cảm",
            "Suy nghĩ tự sát (quan trọng)",
            "Rối loạn tâm thần (hiếm)",
            "Ngã (do chóng mặt, buồn ngủ)",
            "Nhức đầu",
            "Buồn nôn"
        ],
        "interactions": [
            "Carbamazepine, Phenytoin: cảm ứng enzyme, giảm nồng độ perampanel",
            "Valproate: không ảnh hưởng đáng kể",
            "CYP3A4 inducers: giảm nồng độ perampanel",
            "CYP3A4 inhibitors: tăng nồng độ perampanel",
            "Ethanol: tăng tác dụng an thần, tăng nguy cơ kích động"
        ],
        ',
        "pregnancy": "C",
        ',
        "mechanism_of_action": "Thuốc chống co giật thế hệ mới, cơ chế độc đáo: đối vận không cạnh tranh thụ thể AMPA (alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid), một loại thụ thể glutamate. Glutamate là chất dẫn truyền thần kinh kích thích chính trong não. Perampanel ức chế hoạt động của AMPA receptor, làm giảm tính kích thích của tế bào thần kinh và giảm hoạt động bất thường gây co giật. Đặc điểm: cơ chế độc đáo (AMPA antagonist), hiệu quả với cả co giật cục bộ và co giật toàn thể, nhưng có nguy cơ tác dụng phụ thần kinh tâm thần (kích động, lo âu, suy nghĩ tự sát).",
        "monitoring": [
            "Tần suất và mức độ co giật",
            "Tâm thần (RẤT QUAN TRỌNG): kích động, lo âu, trầm cảm, suy nghĩ tự sát, hành vi bất thường",
            "Dấu hiệu hành vi tự sát - cảnh báo bệnh nhân và gia đình",
            "Ngã (do chóng mặt, buồn ngủ)",
            "Dấu hiệu độc tính: chóng mặt quá mức, buồn ngủ, mệt mỏi",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều ở suy thận",
            "Chức năng gan (ALT, AST) - hiếm viêm gan"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột (nguy cơ co giật) - giảm liều dần dần trong vài tuần",
            "Nguy cơ tác dụng phụ thần kinh tâm thần: kích động, lo âu, trầm cảm, suy nghĩ tự sát - theo dõi sát, đặc biệt ở trẻ em và thanh thiếu niên",
            "Nguy cơ hành vi tự sát - cảnh báo bệnh nhân và gia đình về các dấu hiệu",
            "Uống trước khi ngủ để giảm tác dụng phụ ban ngày (chóng mặt, buồn ngủ)",
            "Tăng liều chậm (mỗi tuần) để giảm tác dụng phụ",
            "Nguy cơ ngã (do chóng mặt, buồn ngủ) - thận trọng ở người cao tuổi",
            "Tránh ethanol (rượu) - tăng tác dụng an thần, tăng nguy cơ kích động",
            "Thận trọng ở bệnh nhân có tiền sử bệnh tâm thần - tăng nguy cơ tác dụng phụ",
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Tương tác với carbamazepine, phenytoin (giảm nồng độ perampanel) - có thể cần tăng liều"
        ],
        "pharmacokinetics": {
            "half_life": "105 giờ (rất dài)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "Rất dài (do half-life rất dài, dùng 1 lần/ngày)",
            "protein_binding": "95-96% (rất cao)",
            "metabolism": "Gan (chuyển hóa chủ yếu qua CYP3A4, một phần qua CYP1A2, CYP2B6)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ hành vi tự sát và ý tưởng tự sát. Cảnh báo bệnh nhân và gia đình về các dấu hiệu kích động, lo âu, trầm cảm, thay đổi tâm trạng, và hành vi bất thường. Nguy cơ tăng ở trẻ em và thanh thiếu niên. Ngừng đột ngột có thể gây co giật.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inducers (carbamazepine, phenytoin, phenobarbital, rifampin)",
                    "mechanism": "Cảm ứng enzyme CYP3A4, tăng chuyển hóa perampanel",
                    "effect": "Giảm nồng độ perampanel đáng kể, giảm hiệu quả",
                    "management": "Tăng liều perampanel nếu cần. Theo dõi đáp ứng điều trị. Khi ngừng inducer, giảm liều perampanel."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa perampanel qua CYP3A4",
                    "effect": "Tăng nồng độ perampanel, tăng độc tính (chóng mặt, buồn ngủ, kích động)",
                    "management": "Thận trọng. Giảm liều perampanel. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Ethanol",
                    "mechanism": "Tác dụng hiệp đồng ức chế thần kinh trung ương",
                    "effect": "Tăng tác dụng an thần, tăng nguy cơ kích động, hành vi bất thường",
                    "management": "Tránh ethanol khi dùng perampanel."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng perampanel",
                "Suy gan nặng (Child-Pugh C)",
                "Suy thận nặng (CrCl <15)"
            ],
            "tương_đối": [
                "Tiền sử bệnh tâm thần - tăng nguy cơ tác dụng phụ thần kinh tâm thần",
                "Tiền sử hành vi tự sát - tăng nguy cơ",
                "Suy thận (CrCl 15-30) - giảm liều 50%",
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng",
                "Dùng với CYP3A4 inducers - giảm nồng độ perampanel",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Perampanel là category C. Chứng cứ về an toàn trong thai kỳ còn hạn chế. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Perampanel bài tiết vào sữa mẹ ở nồng độ đáng kể. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém, kích động).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, kích động ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa chủ yếu qua gan)",
            "notes": "Perampanel chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: chóng mặt nặng, buồn ngủ sâu, hôn mê",
                "Triệu chứng tâm thần: kích động nặng, loạn thần, hành vi bất thường",
                "Rối loạn hô hấp: suy hô hấp (hiếm)",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch",
                "Điều trị kích động nếu có: Benzodiazepine (thận trọng - có thể tăng tác dụng an thần)",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Lọc máu (hemodialysis): ít hiệu quả (protein binding 95-96%, chuyển hóa chủ yếu qua gan)"
            ],
            "monitoring": "Theo dõi liên tục ý thức, hô hấp, tim mạch, dấu hiệu tâm thần (kích động, loạn thần) trong ít nhất 24-48 giờ (do half-life rất dài 105 giờ)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày, trước khi ngủ (do tác dụng an thần và để giảm tác dụng phụ ban ngày). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. KHÔNG ngừng đột ngột - giảm liều dần dần trong vài tuần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fycompa (perampanel)",
                "UpToDate - Perampanel: Drug information",
                "Lexicomp - Perampanel"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information"
        ]
    },
    
    "Phenobarbital": {'group': 'Neurology - Anticonvulsant', 'vietnamese_name':
        'Phenobarbital, Luminal', 'administration': ['PO', 'IV', 'IM'],
        'indications': ['Động kinh (nhiều loại)', 'Status epilepticus',
        'An thần', 'Cai nghiện rượu', 'Cai nghiện benzodiazepine'],
        'contraindications': ['Porphyria', 'Suy hô hấp nặng',
        'Suy gan nặng', 'Dị ứng barbiturates'], 'dosage': {'adult_epilepsy':
        '60-180mg/ngày PO chia 2-3 lần/ngày', 'adult_status_epilepticus':
        '15-20mg/kg IV x 1 lần (tối đa 1g), sau đó 1-3mg/kg mỗi 6-8 giờ',
        'adult_sedation': '30-120mg/ngày PO chia 2-3 lần/ngày', 'adult_max':
        '300mg/ngày', 'notes':
        'Theo dõi nồng độ trong máu (mục tiêu 15-40 mcg/mL). Half-life rất dài (80-120 giờ)'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Giảm liều 25%',
        'under_30': 'Giảm liều 50%'}, 'side_effects': ['Buồn ngủ, an thần',
        'Chóng mặt', 'Ataxia', 'Rối loạn nhận thức', 'Ức chế hô hấp (liều cao)',
        'Phụ thuộc, nghiện', 'Hội chứng cai (ngừng đột ngột)',
        'Rối loạn chức năng gan (hiếm)', 'Ban da (hiếm)',
        'Loãng xương (dùng lâu dài)'], 'interactions': [
        'Nhiều thuốc: cảm ứng enzyme CYP450 mạnh, giảm nồng độ nhiều thuốc',
        'Warfarin: giảm tác dụng warfarin (cảm ứng enzyme)',
        'Oral contraceptives: giảm hiệu quả',
        'Corticosteroids: giảm hiệu quả',
        'Valproate: cảm ứng enzyme, giảm nồng độ valproate',
        'Alcohol, benzodiazepines: tăng ức chế hô hấp'],
        'pregnancy': 'D - Nguy cơ dị tật thai nhi', 'mechanism_of_action':
        'Phenobarbital là barbiturate, thuốc chống động kinh cổ điển. Tăng hoạt động GABA (gamma-aminobutyric acid) - chất dẫn truyền thần kinh ức chế chính trong não - bằng cách gắn vào GABA-A receptor và tăng thời gian mở kênh chloride, làm tăng ức chế thần kinh. Cũng có thể ức chế kênh natri voltage-gated và kênh calci. Cảm ứng enzyme CYP450 mạnh (CYP2C9, CYP2C19, CYP3A4), tăng chuyển hóa của chính nó và nhiều thuốc khác. Tác dụng: chống động kinh (nhiều loại), an thần, gây ngủ, và điều trị status epilepticus. Half-life rất dài (80-120 giờ) cho phép dùng 1-2 lần/ngày. Có nguy cơ phụ thuộc và nghiện.'
        , 'monitoring': [
        'Nồng độ phenobarbital trong máu (therapeutic range: 15-40 mcg/mL) - QUAN TRỌNG'
        , 'Tần suất và mức độ co giật',
        'Dấu hiệu độc tính (buồn ngủ quá mức, ataxia, lú lẫn, ức chế hô hấp)',
        'Chức năng gan (ALT, AST, bilirubin) - hiếm viêm gan',
        'Chức năng thận (creatinine)',
        'Dấu hiệu phụ thuộc/nghiện (tăng liều, tìm kiếm thuốc)',
        'Dấu hiệu hội chứng cai (kích động, mất ngủ, co giật) nếu ngừng đột ngột',
        'Mật độ xương nếu dùng lâu dài (tăng nguy cơ loãng xương)'], 'precautions': [
        'THEO DÕI NỒNG ĐỘ TRONG MÁU định kỳ (therapeutic range: 15-40 mcg/mL)',
        'KHÔNG được ngừng đột ngột (nguy cơ hội chứng cai, co giật) - giảm liều dần dần',
        'Cảm ứng enzyme CYP450 mạnh → giảm nồng độ nhiều thuốc (warfarin, OCP, corticosteroids, valproate)',
        'Nguy cơ phụ thuộc và nghiện - thận trọng ở bệnh nhân có tiền sử nghiện',
        'Ức chế hô hấp ở liều cao - thận trọng ở bệnh nhân suy hô hấp, COPD',
        'Half-life rất dài (80-120 giờ) → tích lũy nếu dùng lâu dài, cần giảm liều ở người cao tuổi',
        'Thận trọng ở suy gan (giảm chuyển hóa, tăng nguy cơ tích lũy)',
        'Thận trọng ở suy thận (giảm thải trừ)',
        'CHỐNG CHỈ ĐỊNH trong porphyria (có thể gây cơn porphyria cấp)',
        'Tăng nguy cơ loãng xương khi dùng lâu dài - bổ sung vitamin D, canxi',
        'Tương tác với alcohol, benzodiazepines → tăng ức chế hô hấp nguy hiểm'], 'pharmacokinetics': {
        'half_life': '80-120 giờ (rất dài, cho phép dùng 1-2 lần/ngày)',
        'onset': '30-60 phút (PO), 5-15 phút (IV)', 'duration':
        'Rất dài (do half-life rất dài)', 'protein_binding': '20-45% (thấp)',
        'metabolism': 'Gan (CYP2C9, CYP2C19, CYP2C8, CYP2E1) - cảm ứng enzyme mạnh',
        'clearance':
        'Gan (chuyển hóa), thận (thải trừ một phần). Cảm ứng enzyme CYP450 mạnh, tăng chuyển hóa của chính nó và nhiều thuốc khác.'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản ở nhiệt độ phòng, không đông lạnh.'
        , 'black_box_warnings':
        'Nguy cơ phụ thuộc và nghiện. Ngừng đột ngột có thể gây hội chứng cai nghiêm trọng (kích động, mất ngủ, co giật, ảo giác). Ức chế hô hấp có thể gây tử vong, đặc biệt khi dùng với alcohol hoặc benzodiazepines. Nguy cơ dị tật bẩm sinh khi dùng trong thai kỳ. Cảm ứng enzyme CYP450 mạnh, giảm hiệu quả nhiều thuốc quan trọng.'
        , 'drug_interactions': {'major': [{'drug': 'Warfarin', 'mechanism':
        'Phenobarbital cảm ứng CYP2C9, tăng chuyển hóa warfarin', 'effect':
        'Giảm tác dụng chống đông, giảm INR', 'management':
        'Tăng liều warfarin, theo dõi INR thường xuyên. Có thể cần tăng liều warfarin 50-100% khi dùng phenobarbital.'
        }, {'drug': 'Oral contraceptives', 'mechanism':
        'Phenobarbital cảm ứng CYP3A4, tăng chuyển hóa estrogen và progestin',
        'effect': 'Giảm hiệu quả tránh thai, tăng nguy cơ mang thai', 'management':
        'Sử dụng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang thuốc tránh thai liều cao hơn. Tư vấn bệnh nhân về nguy cơ.'
        }, {'drug': 'Valproate', 'mechanism':
        'Phenobarbital cảm ứng enzyme, tăng chuyển hóa valproate', 'effect':
        'Giảm nồng độ valproate, giảm hiệu quả', 'management':
        'Tăng liều valproate nếu cần. Theo dõi nồng độ valproate và điều chỉnh liều.'
        }, {'drug': 'Corticosteroids', 'mechanism':
        'Phenobarbital cảm ứng enzyme, tăng chuyển hóa corticosteroids', 'effect':
        'Giảm hiệu quả corticosteroid', 'management':
        'Tăng liều corticosteroid nếu cần. Theo dõi đáp ứng điều trị.'}, {'drug':
        'Alcohol, Benzodiazepines', 'mechanism':
        'Cả hai đều ức chế hệ thần kinh trung ương, tác dụng cộng hợp', 'effect':
        'Tăng ức chế hô hấp nguy hiểm, có thể tử vong', 'management':
        'Tránh dùng cùng. Nếu cần, giảm liều cả hai thuốc và theo dõi hô hấp chặt chẽ.'}],
        'moderate': [{'drug': 'Phenytoin, Carbamazepine', 'mechanism':
        'Cảm ứng enzyme lẫn nhau', 'effect': 'Giảm nồng độ cả hai thuốc',
        'management':
        'Theo dõi nồng độ trong máu, tăng liều nếu cần để đạt mức điều trị.'},
        {'drug': 'Doxycycline, Tetracycline', 'mechanism':
        'Phenobarbital cảm ứng enzyme, tăng chuyển hóa', 'effect':
        'Giảm nồng độ kháng sinh, giảm hiệu quả', 'management':
        'Tăng liều kháng sinh nếu cần. Theo dõi đáp ứng điều trị.'}, {'drug':
        'Theophylline', 'mechanism': 'Phenobarbital cảm ứng enzyme, tăng chuyển hóa',
        'effect': 'Giảm nồng độ theophylline, giảm hiệu quả', 'management':
        'Tăng liều theophylline nếu cần. Theo dõi nồng độ và điều chỉnh liều.'}],
        'minor': [{'drug': 'Acetaminophen', 'mechanism':
        'Phenobarbital cảm ứng enzyme, tăng chuyển hóa thành chất độc', 'effect':
        'Tăng nguy cơ độc gan với acetaminophen', 'management':
        'Thận trọng khi dùng cùng, giảm liều acetaminophen nếu cần.'}]},
        'contraindications': {'tuyệt_đối': ['Porphyria (có thể gây cơn porphyria cấp)',
        'Suy hô hấp nặng (ức chế hô hấp)', 'Suy gan nặng (Child-Pugh C)',
        'Dị ứng phenobarbital hoặc barbiturates',
        'Tiền sử nghiện chất (tăng nguy cơ phụ thuộc)'], 'tương_đối': [
        'Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều, theo dõi chặt chẽ'
        , 'Suy thận (CrCl <30) - giảm liều 50%, theo dõi nồng độ',
        'COPD, suy hô hấp nhẹ - tăng nguy cơ ức chế hô hấp',
        'Mang thai (nguy cơ dị tật bẩm sinh) - phân loại D, chỉ dùng nếu lợi ích > nguy cơ'
        , 'Bệnh nhân lớn tuổi - tăng nguy cơ tích lũy, độc tính, ngã',
        'Tiền sử nghiện rượu, chất - tăng nguy cơ phụ thuộc',
        'Trầm cảm - có thể làm nặng thêm']}, 'pregnancy_lactation': {
        'fda_category': 'D', 'pregnancy_details':
        'Phenobarbital có nguy cơ dị tật bẩm sinh (dị tật tim, sứt môi/hà ếch, dị tật ngón tay, chậm phát triển). Nguy cơ dị tật bẩm sinh khoảng 5-10%. Nguy cơ rối loạn phát triển thần kinh ở trẻ (IQ thấp hơn, chậm phát triển). Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền, siêu âm chi tiết, và theo dõi chặt chẽ. Cần bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ. Theo dõi nồng độ phenobarbital trong thai kỳ (có thể thay đổi).'
        , 'lactation': {'safety': 'Compatible with monitoring', 'details':
        'Phenobarbital bài tiết vào sữa mẹ ở nồng độ đáng kể (nồng độ trong sữa mẹ khoảng 30-50% nồng độ trong huyết thanh mẹ). Nồng độ trong máu trẻ bú mẹ có thể đạt 20-40% nồng độ mẹ. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém, chậm tăng cân, an thần). Cần theo dõi trẻ sát.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, chậm tăng cân, an thần ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều. Đo nồng độ phenobarbital trong máu trẻ nếu có triệu chứng.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan và nồng độ trong máu'
        , 'moderate':
        'Giảm liều 25-50%, theo dõi nồng độ trong máu thường xuyên, theo dõi ALT/AST'
        , 'severe':
        'Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ. Theo dõi nồng độ trong máu và ALT/AST thường xuyên. Nguy cơ tích lũy và độc tính cao.'
        , 'notes':
        'Phenobarbital chuyển hóa ở gan qua nhiều enzyme CYP450. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính. Đặc biệt thận trọng vì phenobarbital có thể gây viêm gan (hiếm).'},
        'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: buồn ngủ sâu, hôn mê, mất phản xạ, co giật (paradoxical)'
        'Ức chế hô hấp: suy hô hấp, ngừng thở (nguy hiểm nhất)',
        'Rối loạn tim mạch: nhịp chậm, hạ huyết áp, shock',
        'Rối loạn tiêu hóa: buồn nôn, nôn',
        'Hạ thân nhiệt (do ức chế trung tâm điều nhiệt)',
        'Phù phổi (hiếm)'], 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp NGAY LẬP TỨC nếu cần (ưu tiên cao nhất)'
        , 'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ, có thể lặp lại mỗi 4-6 giờ (phenobarbital có enterohepatic circulation)'
        , 'Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp (quan trọng nhất)',
        'Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần',
        'Lọc máu (hemodialysis) hoặc lọc máu liên tục: có thể hiệu quả (protein binding thấp, bài tiết qua thận), xem xét ở trường hợp nặng'
        , 'Theo dõi nồng độ phenobarbital trong máu (nguy hiểm nếu >60-80 mcg/mL)',
        'Điều trị hỗ trợ: giữ ấm, theo dõi điện giải'], 'monitoring':
        'Theo dõi liên tục ý thức, hô hấp (quan trọng nhất), tim mạch, điện tâm đồ, nồng độ phenobarbital trong máu, chức năng gan, điện giải, thân nhiệt'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm kích ứng dạ dày'
        , 'timing':
        'Chia 1-2 lần/ngày (do half-life rất dài). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. KHÔNG ngừng đột ngột - giảm liều dần dần.'
        }, 'iv': {'reconstitution':
        'Pha trong 0.9% NaCl hoặc D5W. Nồng độ tối đa 130mg/ml. Không trộn với các thuốc khác.'
        , 'infusion_rate':
        'Truyền chậm: không quá 60mg/phút (tối đa 60mg/phút) để tránh ức chế hô hấp, hạ huyết áp. Theo dõi hô hấp, huyết áp, nhịp tim liên tục trong khi truyền.'
        , 'compatibility': ['0.9% NaCl', 'D5W'], 'incompatibility': [
        'Không trộn với các thuốc khác'], 'notes':
        'Truyền qua đường tĩnh mạch lớn. Theo dõi hô hấp, huyết áp, nhịp tim, điện tâm đồ trong khi truyền. Có thể gây kích ứng tĩnh mạch. Ức chế hô hấp là nguy cơ chính - sẵn sàng hỗ trợ hô hấp.'}},
        'pediatric_dosing': {'neonates':
        'Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế, tăng nguy cơ ức chế hô hấp). Nếu cần: 3-5mg/kg/ngày PO chia 1-2 lần/ngày, tăng dần. Theo dõi nồng độ chặt chẽ.'
        , 'infants':
        '1 tháng - 2 tuổi: 3-5mg/kg/ngày PO chia 1-2 lần/ngày, tăng đến 5-8mg/kg/ngày nếu cần. IV loading: 15-20mg/kg IV x 1 lần (tối đa 1g). Theo dõi nồng độ chặt chẽ (mục tiêu 15-40 mcg/mL). Theo dõi hô hấp chặt chẽ.'
        , 'children':
        '2-12 tuổi: 3-5mg/kg/ngày PO chia 1-2 lần/ngày, tăng đến 5-8mg/kg/ngày nếu cần (tối đa 180mg/ngày). IV loading: 15-20mg/kg IV x 1 lần (tối đa 1g). Theo dõi nồng độ trong máu (mục tiêu 15-40 mcg/mL). Theo dõi hô hấp, chức năng gan.'
        , 'adolescents':
        '≥12 tuổi: Liều người lớn. 60-180mg/ngày PO chia 1-2 lần/ngày. IV loading: 15-20mg/kg IV x 1 lần (tối đa 1g). Theo dõi nồng độ trong máu (mục tiêu 15-40 mcg/mL).'
        , 'notes':
        'Theo dõi nồng độ trong máu chặt chẽ (therapeutic range: 15-40 mcg/mL). Half-life rất dài (80-120 giờ) → tích lũy nếu dùng lâu dài. Theo dõi hô hấp chặt chẽ (đặc biệt ở trẻ nhỏ). KHÔNG ngừng đột ngột - giảm liều dần dần. Theo dõi dấu hiệu phụ thuộc/nghiện.'},
        'geriatric_dosing': {'considerations':
        'Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (buồn ngủ, ataxia, lú lẫn, ức chế hô hấp). Half-life rất dài → tăng nguy cơ tích lũy. Suy gan, suy thận phổ biến hơn. Tăng nguy cơ ngã (do ataxia, buồn ngủ). Tăng nguy cơ loãng xương.'
        , 'dose_adjustment':
        'Khởi đầu với liều thấp hơn (30-60mg/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng gan, thận: CrCl 30-60 → giảm liều 25%, CrCl <30 → giảm liều 50%. Theo dõi nồng độ chặt chẽ (tăng nguy cơ tích lũy).'
        , 'monitoring':
        'Theo dõi nồng độ trong máu thường xuyên hơn (tăng nguy cơ tích lũy do half-life dài). Theo dõi dấu hiệu độc tính (buồn ngủ quá mức, ataxia, lú lẫn, ức chế hô hấp). Theo dõi hô hấp (tăng nguy cơ ức chế hô hấp). Theo dõi chức năng gan (ALT, AST). Theo dõi chức năng thận (creatinine, CrCl). Theo dõi nguy cơ ngã. Theo dõi mật độ xương nếu dùng lâu dài.'},
        'brand_names': {'vietnam': ['Phenobarbital', 'Luminal',
        'Phenobarbital Stada']},
        'cost_estimate': {'unit': 'VND',
        'range': '3,000 - 15,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Phenobarbital generic thường rẻ (3,000-8,000 VND/viên 100mg). Luminal (brand) thường đắt hơn (8,000-15,000 VND/viên 100mg). Dạng IV: 50,000-150,000 VND/lọ 200mg.'},
        'references': {'primary_sources': ['Lexicomp - Phenobarbital',
        'UpToDate - Phenobarbital: Drug information',
        'FDA - Luminal (phenobarbital) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        },
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': True,
            'bleeding_risk': False,
            'organ_toxicity': ['hepatic', 'respiratory', 'bone'],
            'qt_prolongation': False,
            'hepatotoxicity': True,
            'nephrotoxicity': False,
            'requires_monitoring': ['Serum phenobarbital levels', 'Respiratory rate', 'Liver function', 'Bone density']
        },
        'guideline_tags': [
            'AAN 2018 Epilepsy Guidelines',
            'FDA Black Box Warning - Dependence and Addiction',
            'FDA Black Box Warning - Respiratory Depression',
            'ISMP High Alert Medications - Anticonvulsants'
        ]
    },
    "Phenytoin": {'group': 'Neurology - Anticonvulsant', 'vietnamese_name':
        'Phenytoin, Dilantin', 'administration': ['PO', 'IV'], 'indications': [
        'Động kinh (tổng quát, cục bộ)', 'Status epilepticus',
        'Đau dây thần kinh sinh ba', 'Rối loạn nhịp tim (hiếm)'],
        'contraindications': ['Dị ứng', 'Suy gan nặng', 'Block nhĩ thất',
        'Hội chứng bệnh lympho'], 'dosage': {'adult_po':
        '100mg x 3 lần/ngày, tăng đến 200-400mg/ngày', 'adult_iv_loading':
        '15-20mg/kg IV (tối đa 1.5g)', 'adult_iv_maintenance':
        '100mg IV mỗi 6-8 giờ sau loading', 'status_epilepticus':
        '15-20mg/kg IV x 1 lần', 'notes':
        'Theo dõi nồng độ trong máu (mục tiêu 10-20 mcg/mL). Non-linear kinetics'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Giảm liều 25%',
        'under_30': 'Giảm liều 50%'}, 'side_effects': ['Rối loạn tiêu hóa',
        'Nystagmus (liều cao)', 'Ataxia (liều cao)',
        'Ban da (có thể nặng - SJS/TEN)', 'Hạ bạch cầu', 'Tăng men gan',
        'Loãng xương (dùng lâu dài)', 'Tăng acid uric',
        'Rối loạn chức năng nhận thức'], 'interactions': [
        'Warfarin: giảm tác dụng warfarin (cảm ứng enzyme)',
        'Oral contraceptives: giảm hiệu quả',
        'Folic acid: giảm nồng độ phenytoin',
        'Many drugs: cảm ứng CYP450, giảm nồng độ nhiều thuốc'], 'pregnancy':
        'D - Nguy cơ dị tật thai nhi', 'mechanism_of_action':
        'Thuốc chống co giật, ổn định màng tế bào. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh, ngăn cản sự lan truyền của các xung động bất thường. Chỉ tác động lên các tế bào đang hoạt động mạnh (như trong co giật), không ảnh hưởng đến hoạt động bình thường. Điều hòa dòng calci và có thể ức chế giải phóng glutamate. Được dùng trong điều trị co giật cục bộ, co giật toàn thể, và status epilepticus. Cũng được dùng trong rối loạn nhịp tim (nhưng ít dùng hơn).'
        , 'monitoring': [
        'Nồng độ phenytoin trong máu (therapeutic range: 10-20 mcg/ml, free: 1-2 mcg/ml) - QUAN TRỌNG'
        , 'Tần suất và mức độ co giật',
        'Dấu hiệu độc tính (nystagmus ở >20 mcg/ml, ataxia ở >30 mcg/ml, lú lẫn ở >40 mcg/ml)'
        'Chức năng gan (ALT, AST, bilirubin) - có thể tăng men gan, hiếm viêm gan nặng'
        'Công thức máu (giảm bạch cầu, giảm tiểu cầu, thiếu máu megaloblastic do thiếu folate)'
        , 'Nồng độ folate và vitamin D (phenytoin làm giảm)',
        'Chức năng thận (creatinine)',
        'Dấu hiệu hội chứng Stevens-Johnson (phát ban nặng) - nguy hiểm',
        'Răng và nướu (tăng sản nướu)', 'Xương (loãng xương do giảm vitamin D)'
        ], 'precautions': [
        'Tuân thủ chặt chẽ liều và lịch dùng - bỏ liều có thể gây co giật',
        'KHÔNG được ngừng đột ngột (nguy cơ status epilepticus)',
        'Nồng độ trong máu cần được theo dõi định kỳ - có mối quan hệ không tuyến tính (saturable kinetics)'
        'Liều tăng nhỏ có thể làm nồng độ tăng rất nhiều ở liều cao (Michaelis-Menten kinetics)'
        'Tương tác với nhiều thuốc: giảm hiệu quả thuốc tránh thai, warfarin (cả hai đều tăng hoặc giảm tùy thuốc)'
        , 'Uống với thức ăn để giảm kích ứng dạ dày',
        'Không nghiền viên nang hoặc viên nén (giảm hấp thu)',
        'Bổ sung folate và vitamin D khi dùng kéo dài',
        'Nguy cơ hội chứng Stevens-Johnson - ngừng ngay nếu có phát ban',
        'Thận trọng ở suy gan (giảm chuyển hóa)',
        'Liều IV: truyền chậm (không quá 50mg/phút) để tránh hạ huyết áp, rối loạn nhịp'
        , 'Không pha trong D5W (kết tủa), chỉ dùng NS'], 'pharmacokinetics': {
        'half_life':
        '22 giờ (bình thường), dài hơn ở liều cao (saturable kinetics)',
        'onset': '30-60 phút (PO), 15-30 phút (IV)', 'duration':
        'Dài (phụ thuộc liều)', 'protein_binding':
        '90% (rất cao), chỉ free phenytoin mới hoạt động', 'metabolism':
        'Gan (CYP2C9, CYP2C19) - chuyển hóa mạnh', 'clearance':
        'Gan, có thể bị ảnh hưởng bởi tình trạng dinh dưỡng, tuổi tác'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản ở nhiệt độ phòng, không đông lạnh, chỉ dùng NS để pha.'
        , 'black_box_warnings':
        'Nguy cơ hội chứng Stevens-Johnson và hoại tử thượng bì nhiễm độc (TEN), có thể tử vong. Ngừng ngay nếu có phát ban. Nguy cơ tự sát và hành vi tự sát. Giảm bạch cầu, giảm tiểu cầu có thể nặng. Ngừng đột ngột có thể gây status epilepticus.'
        , 'drug_interactions': {'major': [{'drug': 'Warfarin', 'mechanism':
        'Phenytoin cảm ứng CYP2C9, tăng chuyển hóa warfarin', 'effect':
        'Giảm tác dụng chống đông, giảm INR', 'management':
        'Tăng liều warfarin, theo dõi INR thường xuyên. Có thể cần tăng liều warfarin 50-100% khi dùng phenytoin.'
        }, {'drug': 'Oral contraceptives', 'mechanism':
        'Phenytoin cảm ứng CYP3A4, tăng chuyển hóa estrogen và progestin',
        'effect': 'Giảm hiệu quả tránh thai, tăng nguy cơ mang thai',
        'management':
        'Sử dụng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang thuốc tránh thai liều cao hơn. Tư vấn bệnh nhân về nguy cơ.'
        }, {'drug': 'Folic acid', 'mechanism':
        'Folic acid có thể làm giảm nồng độ phenytoin', 'effect':
        'Giảm nồng độ phenytoin, có thể gây co giật', 'management':
        'Theo dõi nồng độ phenytoin khi bổ sung folic acid. Có thể cần tăng liều phenytoin.'
        }, {'drug': 'Chloramphenicol, Isoniazid, Sulfonamides', 'mechanism':
        'Ức chế CYP2C9, CYP2C19, giảm chuyển hóa phenytoin', 'effect':
        'Tăng nồng độ phenytoin, tăng nguy cơ độc tính', 'management':
        'Giảm liều phenytoin 25-50%, theo dõi nồng độ trong máu, dấu hiệu độc tính.'
        }, {'drug': 'Valproate', 'mechanism':
        'Ức chế chuyển hóa phenytoin, tăng nồng độ free phenytoin (do giảm protein binding)'
        , 'effect': 'Tăng nồng độ free phenytoin, tăng nguy cơ độc tính',
        'management':
        'Giảm liều phenytoin 25-50%, theo dõi nồng độ free phenytoin, dấu hiệu độc tính.'
        }, {'drug': 'Cimetidine', 'mechanism': 'Ức chế CYP2C9, CYP2C19',
        'effect': 'Tăng nồng độ phenytoin', 'management':
        'Giảm liều phenytoin, theo dõi nồng độ trong máu.'}, {'drug':
        'Corticosteroids', 'mechanism':
        'Phenytoin cảm ứng enzyme, tăng chuyển hóa', 'effect':
        'Giảm hiệu quả corticosteroid', 'management':
        'Tăng liều corticosteroid nếu cần.'}], 'minor': [{'drug': 'Antacids', 'mechanism': 'Giảm hấp thu phenytoin', 'effect':
        'Giảm nhẹ nồng độ phenytoin', 'management': 'Uống cách nhau 2-3 giờ.'}]},
        'contraindications': {'tuyệt_đối': [
        'Suy gan nặng (Child-Pugh C)', 'Block nhĩ thất độ II hoặc III',
        'Hội chứng bệnh lympho (lymphoma-like syndrome)',
        'Tiền sử hội chứng Stevens-Johnson do phenytoin'], 'tương_đối': [
        'Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều, theo dõi chặt chẽ'
        , 'Suy thận (CrCl <30) - giảm liều 50%, theo dõi nồng độ',
        'Bệnh tim mạch (rối loạn nhịp, block nhĩ thất độ I)',
        'Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ',
        'Bệnh nhân lớn tuổi (tăng nguy cơ độc tính, giảm chuyển hóa)',
        'Thiếu hụt folate (tăng nguy cơ thiếu máu megaloblastic)',
        'Loãng xương (tăng nguy cơ gãy xương)']}, 'pregnancy_lactation': {
        'fda_category': 'D', 'pregnancy_details':
        'Phenytoin có nguy cơ dị tật bẩm sinh (fetal hydantoin syndrome: dị tật tim, sứt môi/hà ếch, chậm phát triển, dị tật ngón tay). Nguy cơ dị tật bẩm sinh khoảng 5-10%. Cần bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền, siêu âm chi tiết, và theo dõi chặt chẽ. Theo dõi nồng độ phenytoin thường xuyên (thay đổi trong thai kỳ).'
        , 'lactation': {'safety': 'Compatible with monitoring', 'details':
        'Phenytoin bài tiết vào sữa mẹ ở nồng độ thấp (nồng độ trong sữa mẹ khoảng 10-20% nồng độ trong huyết thanh mẹ). Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.'
        , 'recommendation':
        'Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém). Đo nồng độ phenytoin trong máu trẻ nếu có triệu chứng.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan và nồng độ trong máu'
        , 'moderate':
        'Giảm liều 25-50%, theo dõi nồng độ trong máu thường xuyên, theo dõi ALT/AST'
        , 'severe':
        'Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ. Theo dõi nồng độ trong máu và ALT/AST thường xuyên. Nguy cơ tích lũy và độc tính cao.'
        , 'notes':
        'Phenytoin chuyển hóa ở gan qua CYP2C9 và CYP2C19. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính. Đặc biệt thận trọng vì phenytoin có thể gây viêm gan.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: nystagmus (dấu hiệu sớm nhất), ataxia, lú lẫn, buồn ngủ, hôn mê, co giật'
        'Rối loạn tim mạch: nhịp chậm, block nhĩ thất, hạ huyết áp, rối loạn nhịp',
        'Rối loạn hô hấp: suy hô hấp, ngừng thở',
        'Rối loạn tiêu hóa: buồn nôn, nôn',
        'Triệu chứng khác: sốt, giảm bạch cầu, rối loạn điện giải'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ',
        'Đo nồng độ phenytoin trong máu (nguy hiểm nếu >40 mcg/ml)',
        'Xử trí co giật: benzodiazepine (diazepam, lorazepam) hoặc phenobarbital',
        'Xử trí block nhĩ thất: atropine, pacemaker nếu cần',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp',
        'Lọc máu: không hiệu quả (gắn protein cao), nhưng có thể xem xét ở trường hợp nặng'
        , 'Theo dõi công thức máu (nguy cơ giảm bạch cầu)'], 'monitoring':
        'Theo dõi liên tục ý thức, hô hấp, tim mạch, điện tâm đồ, nồng độ phenytoin trong máu (total và free), công thức máu, chức năng gan, điện giải'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống với thức ăn hoặc ngay sau bữa ăn để giảm kích ứng dạ dày và tăng hấp thu'
        , 'timing':
        'Chia liều 2-3 lần/ngày. Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. Không bỏ liều. KHÔNG nghiền viên nang hoặc viên nén (giảm hấp thu).'
        }, 'iv': {'reconstitution':
        'Pha trong 0.9% NaCl (không dùng D5W - kết tủa). Nồng độ tối đa 10mg/ml. Không trộn với các thuốc khác.'
        , 'infusion_rate':
        'Truyền chậm: không quá 50mg/phút (tối đa 50mg/phút) để tránh hạ huyết áp, rối loạn nhịp, ngừng tim. Theo dõi huyết áp, nhịp tim liên tục trong khi truyền.'
        , 'compatibility': ['0.9% NaCl', 'Không trộn với các thuốc khác']}, 'notes':
        'Chỉ dùng NS để pha. Truyền qua đường tĩnh mạch lớn. Theo dõi huyết áp, nhịp tim, điện tâm đồ trong khi truyền. Không dùng filter trong dây truyền (có thể làm giảm nồng độ).'
        }, 'pediatric_dosing': {'neonates':
        'Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế). Nếu cần: 5mg/kg/ngày PO chia 2-3 lần, tăng dần. Theo dõi nồng độ chặt chẽ.',
        'infants':
        '1 tháng - 2 tuổi: 5-8mg/kg/ngày PO chia 2-3 lần. IV loading: 15-20mg/kg IV (tối đa 1.5g). Theo dõi nồng độ chặt chẽ. Non-linear kinetics - tăng liều nhỏ có thể làm nồng độ tăng rất nhiều.',
        'children':
        '2-12 tuổi: 5-8mg/kg/ngày PO chia 2-3 lần (tối đa 300mg/ngày). IV loading: 15-20mg/kg IV (tối đa 1.5g). Theo dõi nồng độ trong máu (mục tiêu 10-20 mcg/mL). Bổ sung folate và vitamin D.',
        'adolescents':
        '≥12 tuổi: Liều người lớn. 100mg x 3 lần/ngày, tăng đến 200-400mg/ngày. IV loading: 15-20mg/kg IV (tối đa 1.5g). Theo dõi nồng độ trong máu. Bổ sung folate và vitamin D.',
        'notes':
        'Theo dõi nồng độ trong máu chặt chẽ (therapeutic range: 10-20 mcg/mL). Non-linear kinetics - tăng liều nhỏ có thể làm nồng độ tăng rất nhiều ở liều cao. Bổ sung folate và vitamin D khi dùng kéo dài. Theo dõi dấu hiệu độc tính (nystagmus, ataxia, lú lẫn).'}, 'geriatric_dosing': {'considerations':
        'Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (nystagmus, ataxia, lú lẫn). Chuyển hóa có thể giảm, tăng nguy cơ tích lũy. Suy gan, suy thận phổ biến hơn. Tăng nguy cơ loãng xương.',
        'dose_adjustment':
        'Khởi đầu với liều thấp hơn (100mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng gan, thận: CrCl 30-60 → giảm liều 25%, CrCl <30 → giảm liều 50%. Theo dõi nồng độ chặt chẽ.',
        'monitoring':
        'Theo dõi nồng độ trong máu thường xuyên hơn (non-linear kinetics). Theo dõi dấu hiệu độc tính (nystagmus, ataxia, lú lẫn). Theo dõi chức năng gan (ALT, AST). Theo dõi chức năng thận (creatinine, CrCl). Bổ sung folate và vitamin D. Theo dõi mật độ xương nếu dùng lâu dài.'}, 'brand_names': {'vietnam': [
        'Phenytoin', 'Dilantin', 'Phenytoin Stada', 'Phenyto'], 'common': [
        'Dilantin', 'Phenytoin'],
        'range': '5,000 - 20,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Phenytoin generic thường rẻ hơn (5,000-12,000 VND/viên 100mg). Dilantin (brand) thường đắt hơn (12,000-20,000 VND/viên 100mg). Dạng IV: 50,000-100,000 VND/lọ 250mg.'},
        'references': {'primary_sources': ['Lexicomp - Phenytoin',
        'UpToDate - Phenytoin: Drug information',
        'FDA - Dilantin (phenytoin) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews',
        'last_updated': '2025-02-18'
        },
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': True,
            'bleeding_risk': False,
            'organ_toxicity': ['hepatic', 'hematologic', 'dermatologic', 'bone'],
            'qt_prolongation': False,
            'hepatotoxicity': True,
            'nephrotoxicity': False,
            'requires_monitoring': ['Serum phenytoin levels', 'Liver function', 'CBC', 'Skin rash', 'Bone density']
        },
        'guideline_tags': [
            'AAN 2018 Epilepsy Guidelines',
            'FDA Black Box Warning - Stevens-Johnson Syndrome',
            'FDA Black Box Warning - Suicidal Behavior',
            'ISMP High Alert Medications - Anticonvulsants'
        ]
    },
    "Primidone": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Primidone, Mysoline",
        "administration": ["PO"],
        "indications": [
            "Động kinh cục bộ",
            "Động kinh tổng quát",
            "Động kinh tonic-clonic",
            "Động kinh myoclonic"
        ],
        "contraindications": [
            "Dị ứng primidone hoặc phenobarbital",
            "Porphyria",
            "Suy gan nặng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_initial": "125mg x 1 lần/ngày, tăng dần mỗi 3-7 ngày",
            "adult_maintenance": "250-500mg x 3-4 lần/ngày (tối đa 2000mg/ngày)",
            "pediatric_initial": "50-125mg/ngày, tăng dần",
            "pediatric_maintenance": "10-25mg/kg/ngày chia 3-4 lần",
            "notes": "Chuyển hóa thành phenobarbital và phenylethylmalonamide (PEMA). Cả hai đều có hoạt tính chống co giật. Khởi đầu với liều thấp để tránh tác dụng phụ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Giảm liều 50%, theo dõi nồng độ phenobarbital"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến, đặc biệt khi bắt đầu)",
            "Chóng mặt",
            "Mất điều hòa (ataxia)",
            "Buồn nôn, nôn",
            "Rối loạn nhận thức",
            "Rối loạn hành vi",
            "Phát ban",
            "Giảm bạch cầu (hiếm)",
            "Thiếu máu megaloblastic (hiếm, do thiếu folate)"
        ],
        "interactions": [
            "Valproate: tăng nồng độ phenobarbital (từ primidone)",
            "Carbamazepine, Phenytoin: cảm ứng enzyme, giảm nồng độ primidone",
            "Warfarin: cảm ứng enzyme, giảm tác dụng warfarin",
            "Thuốc tránh thai: cảm ứng enzyme, giảm hiệu quả",
            "Ethanol: tăng tác dụng an thần"
        ],
        ',
        "pregnancy": "D",
        ',
        "mechanism_of_action": "Primidone là prodrug, chuyển hóa thành hai chất hoạt động: phenobarbital (chất chuyển hóa chính) và phenylethylmalonamide (PEMA). Phenobarbital ức chế kênh natri voltage-gated và tăng hoạt động GABA (gamma-aminobutyric acid), làm giảm hoạt động bất thường của tế bào thần kinh. PEMA cũng có hoạt tính chống co giật yếu hơn. Cảm ứng enzyme CYP450 mạnh, gây nhiều tương tác thuốc. Được dùng trong điều trị động kinh cục bộ và tổng quát.",
        "monitoring": [
            "Tần suất và mức độ co giật",
            "Nồng độ phenobarbital trong máu (therapeutic range: 15-40 mcg/mL)",
            "Dấu hiệu độc tính: buồn ngủ quá mức, chóng mặt, mất điều hòa, rối loạn nhận thức",
            "Công thức máu (CBC) - hiếm giảm bạch cầu, thiếu máu megaloblastic",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Chức năng thận (creatinine) - cần điều chỉnh liều ở suy thận",
            "Dấu hiệu thiếu folate (thiếu máu megaloblastic) - bổ sung folate nếu cần",
            "Dấu hiệu nhiễm trùng (giảm bạch cầu)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột (nguy cơ co giật, status epilepticus) - giảm liều dần dần trong vài tuần",
            "Khởi đầu với liều rất thấp (125mg/ngày) để tránh tác dụng phụ (buồn ngủ, chóng mặt)",
            "Tăng dần liều chậm (mỗi 3-7 ngày) để giảm tác dụng phụ",
            "Theo dõi nồng độ phenobarbital trong máu (therapeutic range: 15-40 mcg/mL)",
            "Cảm ứng enzyme CYP450 mạnh → nhiều tương tác thuốc (warfarin, thuốc tránh thai, và nhiều thuốc khác)",
            "Bổ sung folate (1-5mg/ngày) để phòng ngừa thiếu máu megaloblastic",
            "Thận trọng ở bệnh nhân suy gan, suy thận (giảm liều, theo dõi nồng độ)",
            "Có thể gây buồn ngủ, chóng mặt - thận trọng khi lái xe, vận hành máy móc",
            "Thận trọng ở bệnh nhân có tiền sử lạm dụng chất (có thể gây nghiện)",
            "Tương tác với valproate (tăng nồng độ phenobarbital) - có thể cần giảm liều primidone"
        ],
        "pharmacokinetics": {
            "half_life": "10-12 giờ (primidone), 80-120 giờ (phenobarbital - rất dài)",
            "onset": "Vài ngày đến vài tuần (do cần chuyển hóa thành phenobarbital)",
            "duration": "Dài (do half-life dài của phenobarbital)",
            "protein_binding": "20% (primidone), 50% (phenobarbital)",
            "metabolism": "Gan (chuyển hóa thành phenobarbital và PEMA qua CYP450)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ phenobarbital). Phenobarbital có half-life rất dài (80-120 giờ) → tích lũy."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ nghiện và lệ thuộc (do chuyển hóa thành phenobarbital). KHÔNG được ngừng đột ngột - có thể gây co giật, status epilepticus. Phải giảm liều dần dần trong vài tuần.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Valproate",
                    "mechanism": "Valproate ức chế chuyển hóa phenobarbital, tăng nồng độ phenobarbital từ primidone",
                    "effect": "Tăng nồng độ phenobarbital đáng kể, tăng độc tính (buồn ngủ, chóng mặt, mất điều hòa)",
                    "management": "Giảm liều primidone 25-50%. Theo dõi nồng độ phenobarbital. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Phenobarbital (từ primidone) cảm ứng enzyme CYP450, tăng chuyển hóa warfarin",
                    "effect": "Giảm tác dụng chống đông, giảm INR, tăng nguy cơ huyết khối",
                    "management": "Tăng liều warfarin. Theo dõi INR thường xuyên. Khi ngừng primidone, giảm liều warfarin."
                },
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Phenobarbital cảm ứng enzyme CYP450, tăng chuyển hóa estrogen và progestin",
                    "effect": "Giảm hiệu quả thuốc tránh thai, tăng nguy cơ mang thai",
                    "management": "Sử dụng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang thuốc tránh thai liều cao hơn. Tư vấn bệnh nhân về nguy cơ."
                }
            ],
            "moderate": [
                {
                    "drug": "Carbamazepine, Phenytoin",
                    "mechanism": "Cảm ứng enzyme CYP450 lẫn nhau, tăng chuyển hóa primidone",
                    "effect": "Giảm nồng độ primidone, giảm hiệu quả",
                    "management": "Tăng liều primidone nếu cần. Theo dõi nồng độ phenobarbital và đáp ứng điều trị."
                },
                {
                    "drug": "Ethanol",
                    "mechanism": "Tác dụng hiệp đồng ức chế thần kinh trung ương",
                    "effect": "Tăng tác dụng an thần, tăng nguy cơ suy hô hấp",
                    "management": "Tránh ethanol khi dùng primidone."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng primidone hoặc phenobarbital",
                "Porphyria (phenobarbital có thể gây cơn porphyria)",
                "Suy gan nặng (Child-Pugh C)",
                "Suy thận nặng (CrCl <15)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều, theo dõi chặt chẽ",
                "Suy thận (CrCl 15-30) - giảm liều 50%, theo dõi nồng độ phenobarbital",
                "Mang thai (category D) - nguy cơ dị tật bẩm sinh, chỉ dùng nếu lợi ích > nguy cơ rõ ràng",
                "Tiền sử lạm dụng chất - nguy cơ nghiện",
                "Dùng với valproate - tăng nồng độ phenobarbital"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Primidone là category D - có nguy cơ dị tật bẩm sinh (do phenobarbital). Tăng nguy cơ dị tật tim, sứt môi/hàm ếch, dị tật thần kinh. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ rõ ràng. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Cần bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Primidone và phenobarbital bài tiết vào sữa mẹ ở nồng độ đáng kể. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém, chậm phát triển).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, chậm phát triển ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan và nồng độ phenobarbital",
            "moderate": "Giảm liều 25-50%, theo dõi nồng độ phenobarbital thường xuyên, theo dõi ALT/AST",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ. Theo dõi nồng độ phenobarbital và ALT/AST thường xuyên.",
            "notes": "Primidone chuyển hóa ở gan thành phenobarbital. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ sâu, hôn mê, mất phản xạ, suy hô hấp",
                "Rối loạn hô hấp: suy hô hấp nặng (do phenobarbital)",
                "Rối loạn tim mạch: nhịp chậm, hạ huyết áp",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp ngay lập tức (quan trọng)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp (quan trọng)",
                "Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần",
                "Lọc máu (hemodialysis): có thể hiệu quả với phenobarbital (protein binding 50%, bài tiết qua thận một phần)",
                "Theo dõi nồng độ phenobarbital trong máu"
            ],
            "monitoring": "Theo dõi liên tục ý thức, hô hấp, tim mạch, nồng độ phenobarbital trong máu, chức năng gan, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày và buồn nôn",
                "timing": "Chia 3-4 lần/ngày. Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. KHÔNG ngừng đột ngột - giảm liều dần dần trong vài tuần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mysoline (primidone)",
                "UpToDate - Primidone: Drug information",
                "Lexicomp - Primidone",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information"
        ]
    },
    
    "Topiramate": {'group': 'Neurology - Anticonvulsant',
',
        "pregnancy": "D - Có bằng chứng về nguy cơ dị tật bẩm sinh",
        ', 'vietnamese_name':
        'Topiramate, Topamax', 'administration': ['PO'], 'indications': [
        'Động kinh cục bộ', 'Động kinh tổng quát', 'Migraine phòng ngừa',
        'Rối loạn lưỡng cực (off-label)'], 'contraindications': [
        'Dị ứng', 'Sỏi thận tái phát', 'Glaucoma góc hẹp'], 'dosage': {
        'adult_epilepsy':
        '25-50mg x 2 lần/ngày, tăng dần đến 200-400mg/ngày (chia 2 lần)',
        'adult_migraine': '25mg/ngày, tăng đến 100mg/ngày (chia 2 lần)',
        'adult_max': '400mg/ngày', 'notes':
        'Tăng liều chậm. Uống nhiều nước để tránh sỏi thận'}, 'side_effects': [
        'Sỏi thận (tăng nguy cơ)', 'Giảm cân', 'Chóng mặt', 'Buồn ngủ',
        'Rối loạn nhận thức (khó tập trung, chậm suy nghĩ)', 'Dị cảm (tê, ngứa)',
        'Mất vị giác (metallic taste)', 'Tăng nhãn áp (glaucoma góc hẹp)',
        'Toan chuyển hóa (metabolic acidosis)'], 'interactions': [
        'Phenytoin, Carbamazepine: giảm nồng độ topiramate',
        'Valproate: tăng nguy cơ tăng amoniac máu',
        'Oral contraceptives: có thể giảm hiệu quả (cần liều cao hơn)',
        'Digoxin: có thể giảm nồng độ digoxin'],
        'mechanism_of_action':
        'Topiramate là thuốc chống động kinh đa cơ chế. Ức chế kênh natri voltage-gated (giống phenytoin, carbamazepine), ức chế kênh calci (L-type), tăng hoạt động GABA (kích thích GABA-A receptors), và ức chế AMPA/kainate receptors (giảm glutamate). Cũng ức chế carbonic anhydrase (gây sỏi thận, toan chuyển hóa). Tác dụng: chống động kinh (cục bộ và tổng quát), phòng ngừa migraine, và có thể ổn định tâm trạng. Cơ chế đa dạng làm topiramate hiệu quả trong nhiều loại động kinh khác nhau.'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm cơn động kinh, giảm migraine)',
        'Dấu hiệu sỏi thận: đau lưng, đau bụng, tiểu máu (tăng nguy cơ do ức chế carbonic anhydrase)'
        , 'Chức năng thận (creatinine, eGFR) - theo dõi định kỳ',
        'Toan chuyển hóa: bicarbonate, pH (có thể gây toan chuyển hóa)',
        'Rối loạn nhận thức: khó tập trung, chậm suy nghĩ, suy giảm trí nhớ (phổ biến)'
        , 'Giảm cân - theo dõi cân nặng',
        'Nhãn áp (nếu có triệu chứng glaucoma)',
        'Dấu hiệu dị cảm (tê, ngứa) - phổ biến'], 'precautions': [
        'Uống nhiều nước (2-3L/ngày) để giảm nguy cơ sỏi thận - QUAN TRỌNG',
        'Tăng liều chậm để giảm tác dụng phụ nhận thức',
        'Rối loạn nhận thức (khó tập trung, chậm suy nghĩ) - phổ biến, có thể ảnh hưởng công việc, học tập'
        'Giảm cân - có thể là tác dụng phụ hoặc lợi ích tùy bệnh nhân, theo dõi cân nặng'
        , 'Dị cảm (tê, ngứa) - phổ biến, thường tự khỏi',
        'Mất vị giác (metallic taste) - có thể ảnh hưởng ăn uống',
        'Toan chuyển hóa - có thể xảy ra, theo dõi bicarbonate',
        'CHỐNG CHỈ ĐỊNH trong glaucoma góc hẹp (tăng nhãn áp)',
        'CHỐNG CHỈ ĐỊNH trong sỏi thận tái phát (tăng nguy cơ)',
        'Thận trọng khi dùng với phenytoin, carbamazepine (giảm nồng độ topiramate)',
        'Thận trọng khi dùng với valproate (tăng nguy cơ tăng amoniac máu)',
        'Thận trọng với oral contraceptives (có thể giảm hiệu quả)',
        'Không ngừng đột ngột (tăng nguy cơ co giật)'], 'pharmacokinetics': {
        'half_life': '19-25 giờ (dài, cho phép dùng 2 lần/ngày)', 'onset':
        'Vài ngày đến vài tuần', 'duration': 'Dài (do half-life dài)',
        'protein_binding': '15-41% (thấp)', 'metabolism':
        'Gan (một phần, không phụ thuộc CYP450 chính), thận (thải trừ 70% nguyên dạng)'
        , 'clearance':
        'Thận (70% nguyên dạng), gan (30% chuyển hóa). Không phụ thuộc CYP450 chính nên ít tương tác enzyme hơn.'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings':
        'Nguy cơ dị tật bẩm sinh (cleft lip/palate) khi dùng trong thai kỳ - phân loại D. Nguy cơ toan chuyển hóa có thể gây hậu quả nghiêm trọng. Nguy cơ tăng nhãn áp (glaucoma góc hẹp) - chống chỉ định. Nguy cơ sỏi thận - chống chỉ định trong sỏi thận tái phát.'
        , 'drug_interactions': {'major': [{'drug': 'Phenytoin, Carbamazepine',
        'mechanism': 'Cảm ứng enzyme, tăng chuyển hóa topiramate', 'effect':
        'Giảm nồng độ topiramate, giảm hiệu quả', 'management':
        'Tăng liều topiramate nếu cần. Theo dõi nồng độ và điều chỉnh liều.'}, {
        'drug': 'Valproate', 'mechanism':
        'Cả hai đều ức chế carbonic anhydrase, tăng nguy cơ tăng amoniac máu',
        'effect': 'Tăng nguy cơ tăng amoniac máu, toan chuyển hóa', 'management':
        'Theo dõi amoniac máu, bicarbonate. Có thể cần giảm liều một trong hai thuốc.'
        }, {'drug': 'Oral contraceptives', 'mechanism':
        'Topiramate có thể cảm ứng enzyme, giảm nồng độ estrogen', 'effect':
        'Giảm hiệu quả tránh thai, tăng nguy cơ mang thai', 'management':
        'Sử dụng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang thuốc tránh thai liều cao hơn.'
        }, {'drug': 'Digoxin', 'mechanism':
        'Topiramate có thể giảm nồng độ digoxin', 'effect':
        'Giảm tác dụng digoxin, có thể mất kiểm soát nhịp tim', 'management':
        'Theo dõi nồng độ digoxin, điều chỉnh liều nếu cần.'}], 'minor': [{
        'drug': 'Metformin', 'mechanism':
        'Cả hai đều có thể gây toan chuyển hóa', 'effect':
        'Tăng nguy cơ toan chuyển hóa', 'management':
        'Theo dõi bicarbonate, pH. Thận trọng khi dùng chung.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng topiramate hoặc các thành phần khác',
        'Glaucoma góc hẹp (tăng nhãn áp)',
        'Sỏi thận tái phát (tăng nguy cơ)'], 'tương_đối': [
        'Suy thận nặng (CrCl <30) - giảm liều, tăng khoảng cách liều',
        'Suy gan nặng - giảm liều',
        'Mang thai (nguy cơ dị tật bẩm sinh) - phân loại D, chỉ dùng nếu lợi ích > nguy cơ'
        , 'Tiền sử sỏi thận - tăng nguy cơ, uống nhiều nước',
        'Bệnh nhân lớn tuổi - tăng nguy cơ rối loạn nhận thức',
        'Dùng với valproate - tăng nguy cơ tăng amoniac máu']},
        'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Topiramate có nguy cơ dị tật bẩm sinh cao (cleft lip/palate, dị tật tim, dị tật hệ thần kinh). Nguy cơ dị tật bẩm sinh khoảng 4-5% (so với 2-3% ở dân số chung). Nguy cơ cleft lip/palate tăng 2-3 lần. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền, siêu âm chi tiết, và theo dõi chặt chẽ. Cần bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible with monitoring', 'details':
        'Topiramate bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ bú mẹ có thể đạt 10-20% nồng độ mẹ. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, chậm tăng cân). Cần theo dõi trẻ sát.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, chậm tăng cân, bú kém ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều.'}},
        'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ', 'notes':
        'Topiramate chuyển hóa một phần ở gan (không phụ thuộc CYP450 chính). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, 70% bài tiết qua thận nguyên dạng, nên suy thận quan trọng hơn.'},
        'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, mất điều hòa (ataxia), co giật'
        , 'Rối loạn tiêu hóa: buồn nôn, nôn',
        'Rối loạn thị giác: nhìn mờ, rối loạn thị giác',
        'Toan chuyển hóa: giảm bicarbonate, tăng anion gap',
        'Rối loạn tim mạch: nhịp tim chậm, hạ huyết áp (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch',
        'Xử trí toan chuyển hóa: bicarbonate nếu cần (nếu toan nặng)',
        'Xử trí co giật: benzodiazepine nếu có',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp',
        'Lọc máu: có thể hiệu quả (70% bài tiết qua thận nguyên dạng), xem xét ở trường hợp nặng'
        ], 'monitoring':
        'Theo dõi ý thức, hô hấp, tim mạch, điện giải (bicarbonate, anion gap), chức năng thận'},
        'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Lọc máu có thể hiệu quả (70% bài tiết qua thận nguyên dạng) ở trường hợp nặng.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn', 'timing':
        'Chia 2 lần/ngày (sáng, tối). Tăng liều chậm để giảm tác dụng phụ. Uống nhiều nước (2-3L/ngày) để giảm nguy cơ sỏi thận. KHÔNG ngừng đột ngột - giảm liều dần dần.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': []
        }
        },
        'references': {'primary_sources': ['Lexicomp - Topiramate',
        'UpToDate - Topiramate: Drug information',
        'FDA - Topamax (topiramate) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews',
        'last_updated': '2025-02-18'
        },
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': None,
            'organ_toxicity': {'renal': 'Kidney stones (contraindicated in recurrent stones)', 'ophthalmic': 'Glaucoma (narrow-angle - contraindicated)', 'metabolic': 'Metabolic acidosis', 'teratogenic': 'Black Box Warning (cleft lip/palate)'},
            'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': 'Kidney stones risk',
            'requires_monitoring': ['Renal function (kidney stones risk)', 'Bicarbonate (metabolic acidosis)', 'Cognitive function', 'Weight', 'Teratogenicity (pregnancy - Black Box Warning)'],
            'look_alike_sound_alike': ['Topiramate', 'Topotecan']
        },
        'guideline_tags': [
            'FDA Black Box Warning - Teratogenicity (Cleft Lip/Palate)',
            'AAN Guidelines - Epilepsy Treatment',
            'AAN Guidelines - Migraine Prevention',
            'ILAE Guidelines - Antiepileptic Drugs'
        ]
    },
    "Valproate": {'group': 'Neurology - Anticonvulsant', 'vietnamese_name':
        'Valproate, Valproic Acid, Depakote', 'administration': ['PO', 'IV'],
        'indications': ['Động kinh (nhiều loại)', 'Rối loạn lưỡng cực',
        'Migraine phòng ngừa', 'Status epilepticus'], 'contraindications': [
        'Bệnh gan hoạt động', 'Rối loạn chuyển hóa chu trình urea',
        'Suy gan nặng', 'Có thai (cho rối loạn lưỡng cực)'], 'dosage': {
        'adult_po': '250-500mg x 2-3 lần/ngày, tăng đến 1000-3000mg/ngày',
        'adult_iv': '15-20mg/kg IV x 1 lần, sau đó 5-10mg/kg mỗi 6 giờ',
        'adult_max': '60mg/kg/ngày (không quá 3000mg/ngày)', 'notes':
        'Theo dõi nồng độ (mục tiêu 50-100 mcg/mL), chức năng gan, tiểu cầu'},
        'side_effects': ['Buồn nôn, nôn', 'Tăng cân', 'Rụng tóc',
        'Tăng men gan', 'Viêm tụy (hiếm nhưng nguy hiểm)', 'Thiếu tiểu cầu',
        'Dị tật thai nhi (neural tube defects)', 'Loãng xương (dùng lâu dài)',
        'Tăng ammonia máu'], 'interactions': [
        'Phenytoin/Carbamazepine: giảm nồng độ valproate',
        'Lamotrigine: tăng nồng độ lamotrigine',
        'Aspirin: tăng nồng độ valproate', 'Warfarin: có thể tăng tác dụng'],
        'pregnancy': 'D - Nguy cơ dị tật thai nhi cao (neural tube defects)',
        'mechanism_of_action':
        'Valproate (valproic acid) ức chế enzyme GABA transaminase, tăng nồng độ GABA (gamma-aminobutyric acid) - chất dẫn truyền thần kinh ức chế chính trong não. Cũng ức chế kênh natri voltage-gated và kênh calci T-type, làm giảm tính kích thích của tế bào thần kinh. Có thể ức chế histone deacetylase. Tác dụng: chống động kinh (nhiều loại), ổn định tâm trạng (bipolar), phòng ngừa migraine. Cơ chế phức tạp, tác dụng trên nhiều hệ thống'
        , 'monitoring': [
        'Nồng độ valproate trong máu (mục tiêu 50-100 mcg/mL, hoặc 350-700 μmol/L) - định kỳ'
        'Chức năng gan (ALT, AST, bilirubin) trước khi bắt đầu, sau 2 tuần, sau 1 tháng, sau đó mỗi 3-6 tháng'
        , 'Tiểu cầu (platelet count) - định kỳ (có thể gây giảm tiểu cầu)',
        'Ammonia máu nếu có triệu chứng lú lẫn, buồn nôn, nôn (dấu hiệu tăng ammonia)'
        , 'Lipase, amylase nếu có đau bụng (viêm tụy - hiếm nhưng nguy hiểm)',
        'Dấu hiệu viêm tụy: đau bụng nặng, buồn nôn, nôn (ngừng ngay)',
        'Dấu hiệu độc gan: vàng da, mệt mỏi, buồn nôn (ngừng ngay)',
        'Cân nặng (tăng cân là tác dụng phụ phổ biến)',
        'Mật độ xương nếu dùng lâu dài (tăng nguy cơ loãng xương)'],
        'precautions': [
        'THEO DÕI CHẶT CHẼ chức năng gan, đặc biệt trong 6 tháng đầu (nguy cơ viêm gan nặng, có thể tử vong)'
        'NGỪNG NGAY nếu có dấu hiệu viêm tụy (đau bụng nặng) hoặc độc gan (vàng da)'
        'Theo dõi nồng độ trong máu để điều chỉnh liều (therapeutic drug monitoring)'
        'Bổ sung acid folic trước và trong thai kỳ (giảm nguy cơ neural tube defects)'
        'Tránh dùng trong thai kỳ nếu có thể (nguy cơ dị tật thai nhi cao - neural tube defects, dị tật tim, dị tật mặt)'
        'Điều chỉnh liều khi dùng với lamotrigine (tăng nồng độ lamotrigine → giảm liều lamotrigine 50%)'
        , 'Thận trọng ở bệnh nhân suy gan, suy thận (giảm liều)',
        'Có thể gây tăng cân (cần theo dõi và tư vấn chế độ ăn)',
        'Có thể gây rụng tóc (thường tạm thời, có thể bổ sung kẽm, selen)',
        'Tránh dùng với aspirin liều cao (tăng nguy cơ độc tính)'],
        'pharmacokinetics': {'half_life':
        '9-16 giờ (ngắn, nhưng có thể kéo dài ở liều cao do bão hòa chuyển hóa)',
        'onset': 'Vài giờ đến vài ngày', 'duration':
        'Ngắn (cần dùng 2-3 lần/ngày)', 'protein_binding':
        '80-95% (cao, tăng ở liều cao do bão hòa)', 'clearance':
        'Gan (chuyển hóa qua glucuronidation, beta-oxidation, CYP450), thận (thải trừ)'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nang: không làm lạnh'
        , 'black_box_warnings':
        'Viêm gan nặng có thể gây tử vong - nguy cơ cao nhất ở trẻ em <2 tuổi, dùng nhiều thuốc chống động kinh, bệnh gan. Viêm tụy có thể gây tử vong. Dị tật thai nhi (neural tube defects) - chống chỉ định trong thai kỳ cho rối loạn lưỡng cực. Giảm tiểu cầu có thể gây chảy máu'
        , 'drug_interactions': {'major': [{'drug': 'Lamotrigine', 'mechanism':
        'Valproate ức chế glucuronidation của lamotrigine, tăng nồng độ lamotrigine'
        , 'effect':
        'Tăng nguy cơ ban da nghiêm trọng (SJS/TEN) với lamotrigine',
        'management':
        'Giảm liều khởi đầu lamotrigine 50% khi dùng với valproate. Theo dõi sát dấu hiệu ban da.'
        }, {'drug': 'Aspirin (liều cao)', 'mechanism':
        'Aspirin ức chế chuyển hóa valproate và tăng protein binding', 'effect':
        'Tăng nồng độ valproate, tăng nguy cơ độc tính', 'management':
        'Tránh dùng aspirin liều cao. Thận trọng khi dùng cùng, theo dõi nồng độ valproate.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Valproate có thể ức chế CYP2C9, tăng nồng độ warfarin', 'effect':
        'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}],
        'moderate': [{'drug': 'Phenytoin, Carbamazepine', 'mechanism':
        'Cảm ứng enzyme chuyển hóa valproate', 'effect':
        'Giảm nồng độ valproate', 'management':
        'Tăng liều valproate nếu cần. Theo dõi nồng độ valproate và điều chỉnh liều.'
        }, {'drug': 'Phenobarbital', 'mechanism':
        'Cảm ứng enzyme, tăng chuyển hóa valproate', 'effect':
        'Giảm nồng độ valproate', 'management':
        'Tăng liều valproate nếu cần. Theo dõi nồng độ.'}, {'drug': 'Rifampin',
        'mechanism': 'Cảm ứng CYP450, tăng chuyển hóa valproate', 'effect':
        'Giảm nồng độ valproate đáng kể', 'management':
        'Tăng liều valproate. Theo dõi nồng độ và điều chỉnh liều.'}], 'minor':
        [{'drug': 'Metronidazole', 'mechanism':
        'Có thể ức chế chuyển hóa valproate', 'effect':
        'Tăng nhẹ nồng độ valproate', 'management':
        'Theo dõi nồng độ nếu dùng lâu dài'}]}, 'contraindications': {
        'tuyệt_đối': ['Bệnh gan hoạt động (viêm gan cấp hoặc mạn)',
        'Rối loạn chuyển hóa chu trình urea (urea cycle disorders)',
        'Suy gan nặng (Child-Pugh C)',
        'Có thai (cho rối loạn lưỡng cực) - nguy cơ dị tật thai nhi cao',
        'Dị ứng valproate'], 'tương_đối': [
        'Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều, theo dõi chặt chẽ'
        , 'Suy thận nặng (CrCl <30) - giảm liều',
        'Thiếu hụt tiểu cầu - tăng nguy cơ chảy máu',
        'Rối loạn đông máu - thận trọng',
        'Có thai (cho động kinh) - chỉ dùng nếu lợi ích > nguy cơ, bổ sung acid folic'
        , 'Trẻ em <2 tuổi - tăng nguy cơ viêm gan nặng',
        'Dùng nhiều thuốc chống động kinh - tăng nguy cơ độc tính']},
        'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ cho rối loạn lưỡng cực do nguy cơ dị tật thai nhi cao (neural tube defects 1-2%, dị tật tim, dị tật mặt, dị tật chi). Với động kinh, chỉ dùng nếu lợi ích > nguy cơ. Bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ (giảm nguy cơ neural tube defects). Theo dõi nồng độ valproate trong thai kỳ (giảm do tăng clearance). Nguy cơ rối loạn phát triển thần kinh ở trẻ (IQ thấp hơn, tự kỷ, ADHD).'
        , 'lactation': {'safety': 'Compatible with caution', 'details':
        'Valproate bài tiết vào sữa mẹ ở nồng độ thấp (1-10% liều mẹ). Nồng độ trong máu trẻ bú mẹ thường <5% nồng độ mẹ. Ít báo cáo về tác dụng phụ ở trẻ bú mẹ. Tuy nhiên, cần theo dõi trẻ về dấu hiệu buồn ngủ, tăng cân chậm, tăng men gan.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, tăng cân chậm, vàng da ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều.'
        }}, 'hepatic_adjustment': {'mild':
        'Giảm liều 25-50%. Theo dõi chức năng gan mỗi 3 tháng', 'moderate':
        'Giảm liều 50%. Theo dõi chức năng gan mỗi 1-2 tháng. Tránh dùng nếu có thể'
        , 'severe':
        'Không dùng (chống chỉ định). Nếu bắt buộc, dùng liều rất thấp dưới sự giám sát chặt chẽ, theo dõi chức năng gan hàng tuần'
        , 'notes':
        'Valproate chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính gan. Nguy cơ viêm gan nặng cao nhất ở trẻ em <2 tuổi và bệnh nhân dùng nhiều thuốc chống động kinh. Theo dõi ALT/AST, bilirubin định kỳ.'
        }, 'overdose_management': {'symptoms': ['Buồn nôn, nôn, tiêu chảy',
        'An thần, lú lẫn, hôn mê', 'Rối loạn nhịp tim, block nhĩ thất',
        'Tăng ammonia máu (lú lẫn, hôn mê)', 'Hạ huyết áp', 'Suy hô hấp',
        'Độc gan (tăng ALT/AST, vàng da)', 'Giảm tiểu cầu, chảy máu'],
        'antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment':
        ['Hỗ trợ hô hấp và tuần hoàn nếu cần',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ (không dùng sau khi đã hôn mê)'
        , 'Theo dõi nồng độ valproate trong máu',
        'Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần',
        'Điều trị tăng ammonia: L-carnitine (100mg/kg/ngày IV hoặc PO), có thể dùng L-arginine'
        'Lọc máu (hemodialysis) nếu nồng độ >850 mcg/mL hoặc có triệu chứng nặng (hiệu quả do protein binding thấp ở liều cao)'
        , 'Theo dõi chức năng gan, tiểu cầu, ammonia máu',
        'Điều trị hỗ trợ: chống nôn, truyền dịch, theo dõi điện giải'],
        'monitoring':
        'Nồng độ valproate trong máu, ALT/AST, bilirubin, tiểu cầu, ammonia máu, điện giải, ECG, huyết áp, nhịp tim, ý thức'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị độc tính gan và hạ tiểu cầu nếu có. Có thể cần lọc máu để loại bỏ thuốc.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn'
        , 'timing':
        'Chia 2-3 lần/ngày (do half-life ngắn). Có thể dùng cùng bữa ăn để giảm kích ứng dạ dày'
        }, 'iv': {'reconstitution':
        'Pha với D5W hoặc NS để nồng độ 1-4mg/mL. Không pha với các dung dịch khác'
        , 'infusion_rate':
        'Truyền 15-20mg/kg trong 60 phút (không quá 20mg/phút)',
        'compatibility': ['D5W', 'NS', "Ringer's lactate"], 'incompatibility':
        ['Không pha với các thuốc khác trong cùng chai'], 'notes':
        'Truyền chậm để tránh kích ứng. Theo dõi huyết áp, nhịp tim trong khi truyền. Có thể gây kích ứng tĩnh mạch.'
        }}, 'pediatric_dosing': {'neonates':
        'Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế, tăng nguy cơ viêm gan). Nếu cần: 10-15mg/kg/ngày PO chia 2-3 lần, tăng dần. Theo dõi chức năng gan chặt chẽ.',
        'infants':
        '1 tháng - 2 tuổi: 10-15mg/kg/ngày PO chia 2-3 lần, tăng đến 20-30mg/kg/ngày nếu cần. TĂNG NGUY CƠ VIÊM GAN NẶNG ở trẻ <2 tuổi - theo dõi chức năng gan chặt chẽ. Theo dõi nồng độ trong máu (mục tiêu 50-100 mcg/mL).',
        'children':
        '2-12 tuổi: 10-15mg/kg/ngày PO chia 2-3 lần, tăng đến 20-30mg/kg/ngày nếu cần (tối đa 60mg/kg/ngày, không quá 3000mg/ngày). Theo dõi nồng độ trong máu. Theo dõi chức năng gan, tiểu cầu. Bổ sung acid folic.',
        'adolescents':
        '≥12 tuổi: Liều người lớn. 250-500mg x 2-3 lần/ngày, tăng đến 1000-3000mg/ngày. Theo dõi nồng độ trong máu (mục tiêu 50-100 mcg/mL). Theo dõi chức năng gan, tiểu cầu.',
        'notes':
        'TĂNG NGUY CƠ VIÊM GAN NẶNG ở trẻ <2 tuổi, đặc biệt khi dùng nhiều thuốc chống động kinh. Theo dõi chức năng gan chặt chẽ trong 6 tháng đầu. Theo dõi nồng độ trong máu (therapeutic range: 50-100 mcg/mL). Theo dõi tiểu cầu. Bổ sung acid folic trước và trong thai kỳ. NGỪNG NGAY nếu có dấu hiệu viêm gan (vàng da) hoặc viêm tụy (đau bụng nặng).'}, 'geriatric_dosing': {'considerations':
        'Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (buồn nôn, an thần, lú lẫn). Suy gan, suy thận phổ biến hơn. Tăng nguy cơ tích lũy và độc tính gan. Tăng nguy cơ loãng xương.',
        'dose_adjustment':
        'Khởi đầu với liều thấp hơn (250mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng gan, thận: CrCl <30 → giảm liều. Theo dõi chức năng gan chặt chẽ.',
        'monitoring':
        'Theo dõi chức năng gan thường xuyên hơn (ALT, AST, bilirubin) - đặc biệt trong 6 tháng đầu. Theo dõi nồng độ trong máu (mục tiêu 50-100 mcg/mL). Theo dõi tiểu cầu. Theo dõi ammonia máu nếu có triệu chứng lú lẫn. Theo dõi dấu hiệu viêm tụy (đau bụng nặng). Theo dõi mật độ xương nếu dùng lâu dài.'}, 'brand_names': {'vietnam': [
        'Valproate', 'Valproic Acid', 'Depakote', 'Valproate Stada'], 'common': [
        'Depakote', 'Valproate', 'Valproic Acid'],
        'range': '10,000 - 40,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Valproate generic thường rẻ hơn (10,000-25,000 VND/viên 500mg). Depakote (brand) thường đắt hơn (25,000-40,000 VND/viên 500mg). Dạng IV: 100,000-200,000 VND/lọ 500mg.'},         'references': {'primary_sources': [
        'FDA Drug Label - Depakote (valproate sodium)',
        'UpToDate - Valproate: Drug information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Epilepsia - ILAE treatment guidelines',
        'American Academy of Neurology guidelines'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews'},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': 'Moderate (thrombocytopenia)',
            'organ_toxicity': {'hepatic': 'Black Box Warning (fatal hepatitis)', 'pancreatic': 'Black Box Warning (fatal pancreatitis)', 'hematologic': 'Thrombocytopenia', 'teratogenic': 'Black Box Warning (neural tube defects)'},
            'qt_prolongation': False,
            'hepatotoxicity': 'Black Box Warning (fatal)',
            'nephrotoxicity': False,
            'requires_monitoring': ['Liver function (Black Box Warning - first 6 months)', 'Platelet count', 'Serum valproate levels (50-100 mcg/mL)', 'Pancreatitis signs (Black Box Warning)', 'Ammonia levels', 'Teratogenicity (pregnancy - Black Box Warning)'],
            'look_alike_sound_alike': ['Valproate', 'Valproic acid', 'Divalproex']
        },
        'guideline_tags': [
            'FDA Black Box Warning - Fatal Hepatitis',
            'FDA Black Box Warning - Fatal Pancreatitis',
            'FDA Black Box Warning - Teratogenicity (Neural Tube Defects)',
            'AAN Guidelines - Epilepsy Treatment',
            'APA Guidelines - Bipolar Disorder',
            'ILAE Guidelines - Antiepileptic Drugs',
            'WHO Essential Medicines List'
        ]
    },
    "Zonisamide": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Zonisamide, Zonegran",
        "administration": ["PO"],
        "indications": [
            "Động kinh cục bộ",
            "Động kinh tổng quát",
            "Động kinh tonic-clonic",
            "Động kinh myoclonic"
        ],
        "contraindications": [
            "Dị ứng zonisamide hoặc sulfonamides",
            "Suy thận nặng (CrCl <30)",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_initial": "100mg x 1 lần/ngày, tăng dần mỗi 2 tuần",
            "adult_maintenance": "200-400mg x 1 lần/ngày (tối đa 600mg/ngày)",
            "pediatric_initial": "2-4mg/kg/ngày, tăng dần",
            "pediatric_maintenance": "4-8mg/kg/ngày (tối đa 12mg/kg/ngày)",
            "notes": "Đa cơ chế: ức chế kênh natri, calci T-type, tăng GABA. Half-life dài (63 giờ), dùng 1 lần/ngày. Thải qua thận, cần điều chỉnh liều ở suy thận."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "CHỐNG CHỈ ĐỊNH hoặc giảm liều 75%",
            "hemodialysis": "Bổ sung liều sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Mất điều hòa (ataxia)",
            "Nhức đầu",
            "Buồn nôn",
            "Sỏi thận (hiếm, do ức chế carbonic anhydrase)",
            "Giảm tiết mồ hôi (hiếm, nguy hiểm ở trẻ em - tăng thân nhiệt)",
            "Rối loạn nhận thức",
            "Phát ban (hiếm, nhưng có thể nặng)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Carbamazepine, Phenytoin: cảm ứng enzyme, giảm nồng độ zonisamide",
            "Valproate: không ảnh hưởng đáng kể",
            "CYP3A4 inhibitors: tăng nồng độ zonisamide",
            "Thuốc ức chế carbonic anhydrase (acetazolamide): tăng nguy cơ sỏi thận"
        ],
        ',
        "pregnancy": "C",
        ',
        "mechanism_of_action": "Thuốc chống co giật đa cơ chế: 1) Ức chế kênh natri voltage-gated trong màng tế bào thần kinh, ngăn cản sự lan truyền của các xung động bất thường. 2) Ức chế kênh calci T-type, giảm hoạt động bất thường của tế bào thần kinh. 3) Tăng hoạt động GABA (gamma-aminobutyric acid), tăng ức chế thần kinh. 4) Ức chế carbonic anhydrase (tác dụng phụ - tăng nguy cơ sỏi thận). Có phổ rộng: hiệu quả với co giật cục bộ và co giật toàn thể. Đặc điểm: thời gian bán thải dài (63 giờ), dùng 1 lần/ngày.",
        "monitoring": [
            "Tần suất và mức độ co giật",
            "Dấu hiệu độc tính: buồn ngủ quá mức, chóng mặt, mất điều hòa, rối loạn nhận thức",
            "Chức năng thận (creatinine, eGFR) - quan trọng (thải qua thận, nguy cơ sỏi thận)",
            "Dấu hiệu sỏi thận: đau lưng, đau bụng, tiểu máu (do ức chế carbonic anhydrase)",
            "Thân nhiệt (đặc biệt ở trẻ em - nguy cơ giảm tiết mồ hôi, tăng thân nhiệt)",
            "Công thức máu (CBC) - hiếm giảm bạch cầu",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu nhiễm trùng (giảm bạch cầu)",
            "Phát ban (hiếm, nhưng có thể nặng)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột (nguy cơ co giật) - giảm liều dần dần trong vài tuần",
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng (thải qua thận)",
            "Nguy cơ sỏi thận (do ức chế carbonic anhydrase) - tăng lượng nước uống, theo dõi dấu hiệu sỏi thận",
            "Nguy cơ giảm tiết mồ hôi (đặc biệt ở trẻ em) - nguy hiểm, có thể gây tăng thân nhiệt, sốc nhiệt",
            "Thận trọng ở trẻ em - tăng nguy cơ giảm tiết mồ hôi, tăng thân nhiệt",
            "Khởi đầu với liều thấp, tăng dần chậm để giảm tác dụng phụ",
            "Có thể gây buồn ngủ, chóng mặt - thận trọng khi lái xe, vận hành máy móc",
            "Tăng lượng nước uống để giảm nguy cơ sỏi thận (ít nhất 1.5-2L/ngày)",
            "Thận trọng ở bệnh nhân suy thận (CrCl <30) - chống chỉ định hoặc giảm liều 75%",
            "Tương tác với carbamazepine, phenytoin (giảm nồng độ zonisamide) - có thể cần tăng liều"
        ],
        "pharmacokinetics": {
            "half_life": "63 giờ (rất dài)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "Dài (do half-life dài, dùng 1 lần/ngày)",
            "protein_binding": "40%",
            "metabolism": "Gan (chuyển hóa một phần qua CYP3A4, N-acetylation, reduction)",
            "clearance": "Chủ yếu qua thận (35% bài tiết nguyên dạng, 65% dạng chuyển hóa), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ giảm tiết mồ hôi và tăng thân nhiệt (đặc biệt ở trẻ em) - có thể gây sốc nhiệt, tử vong. Nguy cơ sỏi thận. Nguy cơ phát ban nặng (Stevens-Johnson syndrome, toxic epidermal necrolysis).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Carbamazepine, Phenytoin",
                    "mechanism": "Cảm ứng enzyme CYP3A4, tăng chuyển hóa zonisamide",
                    "effect": "Giảm nồng độ zonisamide, giảm hiệu quả",
                    "management": "Tăng liều zonisamide nếu cần. Theo dõi đáp ứng điều trị."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa zonisamide qua CYP3A4",
                    "effect": "Tăng nồng độ zonisamide, tăng độc tính",
                    "management": "Thận trọng. Theo dõi dấu hiệu độc tính. Có thể cần giảm liều zonisamide."
                },
                {
                    "drug": "Thuốc ức chế carbonic anhydrase (acetazolamide, topiramate)",
                    "mechanism": "Tác dụng hiệp đồng ức chế carbonic anhydrase",
                    "effect": "Tăng nguy cơ sỏi thận, tăng nguy cơ giảm tiết mồ hôi",
                    "management": "Thận trọng. Tăng lượng nước uống. Theo dõi dấu hiệu sỏi thận và tăng thân nhiệt."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng zonisamide hoặc sulfonamides",
                "Suy thận nặng (CrCl <30) - tích lũy do thải qua thận",
                "Suy gan nặng (Child-Pugh C)"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - giảm liều 25-50%",
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng",
                "Tiền sử sỏi thận - tăng nguy cơ sỏi thận",
                "Trẻ em - tăng nguy cơ giảm tiết mồ hôi, tăng thân nhiệt",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với thuốc ức chế carbonic anhydrase - tăng nguy cơ sỏi thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Zonisamide là category C. Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Cần bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Zonisamide bài tiết vào sữa mẹ ở nồng độ đáng kể. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa một phần qua gan)",
            "notes": "Zonisamide chuyển hóa một phần qua gan (CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ sâu, hôn mê, mất điều hòa",
                "Rối loạn hô hấp: suy hô hấp (hiếm)",
                "Rối loạn tiêu hóa: buồn nôn, nôn",
                "Rối loạn thận: sỏi thận, suy thận cấp (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Lọc máu (hemodialysis): có thể hiệu quả (protein binding 40%, bài tiết qua thận một phần)"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, dấu hiệu thần kinh, chức năng thận, thân nhiệt (đặc biệt ở trẻ em)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày (do half-life dài 63 giờ). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. KHÔNG ngừng đột ngột - giảm liều dần dần trong vài tuần. Tăng lượng nước uống (ít nhất 1.5-2L/ngày) để giảm nguy cơ sỏi thận."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zonegran (zonisamide)",
                "UpToDate - Zonisamide: Drug information",
                "Lexicomp - Zonisamide",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["RFT"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "ILAE Guidelines - Antiepileptic Drugs"
        ]
    }
}

__all__ = ['ANTICONVULSANTS_DRUGS']
