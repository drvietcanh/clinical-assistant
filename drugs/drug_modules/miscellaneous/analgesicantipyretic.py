"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Analgesic/Antipyretic

ANALGESIC_ANTIPYRETIC_DRUGS = {
    "Paracetamol": {'group': 'Analgesic/Antipyretic',
        'vietnamese_name':
        'Paracetamol, Acetaminophen, Tylenol, Efferalgan', 'administration': [
        'PO', 'IV', 'PR'],
        'indications': [
        'Đau nhẹ đến trung bình',
        'Đau đầu', 'Đau cơ', 'Đau răng'],
        'contraindications': [
        'Dị ứng paracetamol', 'Suy gan nặng', 'Bệnh gan tiến triển'],
        'dosage':
        {'adult_po': '500-1000mg x 3-4 lần/ngày (tối đa 4g/ngày)', 'adult_iv':
        '1000mg IV mỗi 6 giờ (tối đa 4g/ngày)', 'pediatric_po':
        '10-15mg/kg x 3-4 lần/ngày (tối đa 60mg/kg/ngày)', 'pediatric_iv':
        '15mg/kg IV mỗi 6 giờ (tối đa 60mg/kg/ngày)', 'pediatric_pr':
        '15-20mg/kg PR mỗi 6 giờ (khi không uống được)', 'notes':
        'Liều tối đa: Người lớn 4g/ngày, Trẻ em 60mg/kg/ngày. Quá liều gây độc gan nghiêm trọng'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Khoảng cách 6-8 giờ'},
        'side_effects': [
        'Hiếm khi có tác dụng phụ ở liều điều trị',
        'Độc gan (với liều quá cao - >150mg/kg)', 'Phát ban (hiếm)',
        'Giảm bạch cầu (rất hiếm)'],
        'interactions': [
        'Warfarin: tăng nguy cơ chảy máu (với liều cao kéo dài)',
        'Isoniazid: tăng nguy cơ độc gan', 'Alcohol: tăng nguy cơ độc gan',
        'Phenytoin/Carbamazepine: tăng nguy cơ độc gan'],
        'pregnancy':
        'C - An toàn (dùng được trong thai kỳ)', 'mechanism_of_action':
        'Paracetamol ức chế cyclooxygenase (COX) chủ yếu ở hệ thần kinh trung ương, làm giảm tổng hợp prostaglandin E2 trong vùng dưới đồi, từ đó giảm đau và hạ sốt. Khác với NSAID, paracetamol ít tác dụng kháng viêm ở ngoại biên vì không ức chế COX hiệu quả ở mô ngoại biên. Cơ chế chính xác vẫn chưa hoàn toàn rõ ràng, nhưng có thể liên quan đến ức chế COX-2 ở hệ thần kinh trung ương hoặc tác dụng qua con đường cannabinoid. Quan trọng: Ở liều quá cao, chuyển hóa qua CYP2E1 tạo NAPQI (N-acetyl-p-benzoquinone imine) - chất độc gây tổn thương gan nặng.'
        , 'monitoring': [
        'ALT/AST nếu nghi ngờ quá liều hoặc bệnh nhân có nguy cơ (suy gan, uống rượu, dùng isoniazid)'
        , 'INR nếu dùng với warfarin liều cao kéo dài (tăng nguy cơ chảy máu)',
        'Dấu hiệu độc tính gan: buồn nôn, nôn, đau bụng, vàng da (xuất hiện sau 24-48h sau quá liều)'
        'Nồng độ paracetamol trong máu nếu quá liều (đồ thị Rumack-Matthew để quyết định điều trị N-acetylcysteine)'
        , 'Đường huyết (hạ đường huyết có thể xảy ra trong quá liều)'],
        'precautions': [
        'Không vượt quá 4g/ngày ở người lớn, 60mg/kg/ngày ở trẻ em để tránh độc tính gan'
        'Giảm liều ở bệnh nhân suy gan, suy thận nặng (khoảng cách liều 6-8 giờ)',
        'Tránh rượu khi dùng (rượu tăng CYP2E1 → tăng sản xuất NAPQI độc)',
        'Kiểm tra các thuốc kết hợp có chứa paracetamol (tránh quá liều không chủ ý)'
        'Thận trọng với bệnh nhân suy dinh dưỡng, nhịn ăn (giảm glutathione → tăng nguy cơ độc tính)'
        'Nếu quá liều, điều trị ngay với N-acetylcysteine (hiệu quả nhất trong vòng 8 giờ đầu)'
        'Thận trọng với bệnh nhân dùng isoniazid, phenytoin, carbamazepine (tăng nguy cơ độc gan)'
        ],
        'pharmacokinetics': {'half_life':
        '2-3 giờ (bình thường), 4-8 giờ (quá liều)', 'onset':
        '30-60 phút (PO), 15-30 phút (IV), 60 phút (PR)', 'duration': '4-6 giờ',
        'protein_binding': '10-25%', 'clearance':
        'Gan: chủ yếu qua glucuronidation (40-60%) và sulfation (20-40%), một phần nhỏ qua CYP2E1 tạo NAPQI (chất độc). Thận: <5% bài tiết nguyên dạng. Ở quá liều, con đường CYP2E1 tăng → tăng NAPQI → vượt quá glutathione → độc gan'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dung dịch: tránh đông lạnh. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi dùng.'
        , 'black_box_warnings':
        'Quá liều có thể gây độc tính gan nghiêm trọng, suy gan cấp, tử vong. Liều >150mg/kg ở trẻ em hoặc >10g ở người lớn có thể gây độc tính gan. Triệu chứng ban đầu có thể nhẹ (buồn nôn, nôn) nhưng tổn thương gan xảy ra sau 24-48 giờ. Điều trị ngay với N-acetylcysteine nếu quá liều (hiệu quả nhất trong vòng 8 giờ đầu). Không dùng quá 4g/ngày ở người lớn.'
        , 'drug_interactions': {'major': [{'drug': 'Warfarin', 'mechanism':
        'Paracetamol liều cao kéo dài có thể ức chế CYP2C9, tăng nồng độ warfarin',
        'effect': 'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên nếu dùng paracetamol liều cao (>2g/ngày) kéo dài. Điều chỉnh liều warfarin nếu cần.'
        }, {'drug': 'Rượu (Ethanol)', 'mechanism':
        'Rượu kích hoạt CYP2E1, tăng chuyển hóa paracetamol thành NAPQI (chất độc)'
        , 'effect':
        'Tăng nguy cơ độc tính gan nghiêm trọng, đặc biệt ở liều paracetamol >4g/ngày'
        , 'management':
        'Tránh rượu hoặc giảm liều paracetamol khi uống rượu. Thận trọng ở bệnh nhân nghiện rượu.'
        }],
        'moderate': [{'drug': 'Rượu (Ethanol)', 'mechanism':
        'Tăng chuyển hóa qua CYP2E1', 'effect': 'Tăng nguy cơ độc tính gan',
        'management': 'Thận trọng, giảm liều paracetamol, theo dõi ALT/AST'}, {
        'drug': 'Phenytoin, Carbamazepine', 'mechanism':
        'Cảm ứng enzyme chuyển hóa', 'effect': 'Tăng nguy cơ độc tính gan',
        'management': 'Thận trọng, giảm liều paracetamol'}],
        'minor': [{'drug':
        'Metoclopramide', 'mechanism': 'Tăng nhu động dạ dày', 'effect':
        'Tăng hấp thu paracetamol (nhẹ)', 'management':
        'Không cần điều chỉnh liều'}]},
        'contraindications': {'tuyệt_đối': [
        'Suy gan nặng (Child-Pugh C)', 'Dị ứng paracetamol',
        'Quá liều paracetamol (đang trong quá trình điều trị)'],
        'tương_đối': [
        'Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều',
        'Nghiện rượu - giảm liều tối đa 2g/ngày',
        'Suy thận nặng (CrCl <30) - giảm liều hoặc tăng khoảng cách',
        'Thiếu hụt G6PD (hiếm gây thiếu máu tan máu)']},
        'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'An toàn trong thai kỳ. Paracetamol là thuốc giảm đau/hạ sốt được lựa chọn đầu tiên trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng ở tất cả các tam cá nguyệt. Tuy nhiên, một số nghiên cứu quan sát gợi ý mối liên hệ có thể có với ADHD và tự kỷ ở trẻ khi dùng lâu dài trong thai kỳ, nhưng chứng cứ chưa rõ ràng.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Paracetamol bài tiết vào sữa mẹ ở nồng độ thấp (<1% liều mẹ). An toàn cho trẻ bú mẹ. Nồng độ trong sữa mẹ rất thấp, không có tác dụng phụ đáng kể ở trẻ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dùng liều thường dùng (500-1000mg mỗi 4-6 giờ).'
        }},
        'hepatic_adjustment': {'mild':
        'Giảm liều tối đa 2-3g/ngày, chia 3-4 lần', 'moderate':
        'Giảm liều tối đa 2g/ngày, chia 3-4 lần. Theo dõi ALT/AST', 'severe':
        'Tránh dùng hoặc dùng liều rất thấp (1-1.5g/ngày) dưới sự giám sát chặt chẽ. Theo dõi ALT/AST thường xuyên'
        , 'notes':
        'Paracetamol chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính. Đặc biệt thận trọng ở bệnh nhân nghiện rượu.'
        },
        'overdose_management': {'symptoms': [
        'Giai đoạn 1 (0-24h): Buồn nôn, nôn, đau bụng, chán ăn, mệt mỏi. Bệnh nhân có thể không có triệu chứng rõ ràng'
        "Giai đoạn 2 (24-48h): Giảm triệu chứng (giai đoạn 'yên lặng'), nhưng ALT/AST bắt đầu tăng"
        'Giai đoạn 3 (48-72h): Tăng ALT/AST đỉnh, vàng da, suy gan, rối loạn đông máu, bệnh não gan, có thể tử vong'
        , 'Giai đoạn 4 (4-14 ngày): Hồi phục (nếu sống sót) hoặc tử vong'],
        'antidote':
        'N-acetylcysteine (NAC) - hiệu quả nếu dùng trong vòng 8-10 giờ sau quá liều, tốt nhất trong 4-6 giờ'
        , 'treatment': [
        'Đánh giá nguy cơ: Liều >150mg/kg (Trẻ em) hoặc >10g (Người lớn) hoặc >200mg/kg (người lớn có nguy cơ) = nguy cơ cao'
        'Đo nồng độ paracetamol trong máu 4 giờ sau khi uống (hoặc ngay khi đến viện nếu >4 giờ)'
        "Sử dụng đồ thị Rumack-Matthew để quyết định điều trị: Nếu nồng độ trên đường 'điều trị' → dùng NAC"
        'NAC protocol: IV hoặc PO. IV: 150mg/kg trong 15 phút, sau đó 50mg/kg trong 4 giờ, sau đó 100mg/kg trong 16 giờ. PO: 140mg/kg, sau đó 70mg/kg mỗi 4 giờ x 17 liều'
        'Theo dõi ALT/AST, INR, bilirubin, glucose, lactate, creatinine thường xuyên'
        'Điều trị hỗ trợ: Truyền dịch, điều chỉnh đường huyết, điều chỉnh rối loạn đông máu, xem xét ghép gan nếu suy gan nặng'
        ],
        'monitoring':
        "Nồng độ paracetamol trong máu, ALT/AST mỗi 12-24 giờ, INR, bilirubin, glucose, lactate, creatinine, dấu hiệu bệnh não gan, tiên lượng (King's College Criteria cho ghép gan)"
        },
        'reversal_agents': {'available': True, 'agents': [{'name':
        'N-acetylcysteine (NAC)', 'indication': 'Quá liều paracetamol', 'dose':
        'IV: 150mg/kg trong 15 phút, sau đó 50mg/kg trong 4 giờ, sau đó 100mg/kg trong 16 giờ. PO: 140mg/kg, sau đó 70mg/kg mỗi 4 giờ x 17 liều'
        , 'mechanism':
        'Bổ sung glutathione, liên kết với NAPQI (chất độc), giải độc gan',
        'notes':
        'Hiệu quả nhất nếu dùng trong vòng 8-10 giờ sau quá liều, tốt nhất trong 4-6 giờ. Vẫn có thể có lợi sau 24 giờ nếu có suy gan.'
        }]},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ'
        , 'timing':
        'Mỗi 4-6 giờ khi cần. Không quá 4g/ngày (Người lớn) hoặc 60mg/kg/ngày (Trẻ em). Có thể dùng trước khi đi ngủ nếu cần giảm đau/giảm sốt ban đêm.'
        },
        'iv': {'reconstitution':
        'Pha trong D5W hoặc NS. Nồng độ cuối: 1mg/ml (tối đa 10mg/ml). Dùng ngay sau khi pha.'
        , 'infusion_rate': 'Truyền trong 15 phút', 'compatibility': ['D5W',
        'NS', 'LR'],
        'incompatibility': ['Không pha trộn với các thuốc khác'],
        'notes':
        'Dùng cho bệnh nhân không uống được hoặc cần tác dụng nhanh. Liều tương đương PO.'
        }},
        'references': {'primary_sources': ['FDA Drug Label - Acetaminophen',
        'UpToDate - Acetaminophen poisoning', 'Rumack-Matthew nomogram',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics",
        "King's College Criteria for liver transplantation in acute liver failure"
        ],
        'evidence_level': 'High - RCTs và guidelines dựa trên chứng cứ'},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': 'Low',
            'organ_toxicity': {
                'hepatic': 'CRITICAL (hepatotoxicity with overdose >150mg/kg or >10g - can be fatal, acute liver failure)',
                'metabolic': 'Moderate (hypoglycemia with overdose)'
            }, 'qt_prolongation': False,
            'hepatotoxicity': True,
            'nephrotoxicity': False,
            'requires_monitoring': [
                'ALT/AST - CRITICAL (if suspected overdose or at-risk patients: liver disease, alcohol use, isoniazid use)',
                'Serum acetaminophen level - CRITICAL (if overdose, use Rumack-Matthew nomogram to determine NAC treatment)',
                'INR (if co-administered with warfarin at high doses >2g/day)',
                'Signs of hepatotoxicity: nausea, vomiting, abdominal pain, jaundice (appears 24-48h after overdose) - CRITICAL',
                'Blood glucose (hypoglycemia can occur with overdose)',
                'King\'s College Criteria for liver transplantation (if acute liver failure)'
            ], 'look_alike_sound_alike': ['Paracetamol', 'Acetaminophen', 'Acetylcysteine', 'N-acetylcysteine']
        }, 'guideline_tags': [
            'FDA Black Box Warning - Acetaminophen and Hepatotoxicity',
            'Rumack-Matthew Nomogram - Acetaminophen Overdose Treatment',
            "King's College Criteria - Liver Transplantation in Acute Liver Failure",
            'ACMT Guidelines - Acetaminophen Poisoning',
            'WHO Essential Medicines List'
        ]}}

__all__ = ['ANALGESIC_ANTIPYRETIC_DRUGS']
