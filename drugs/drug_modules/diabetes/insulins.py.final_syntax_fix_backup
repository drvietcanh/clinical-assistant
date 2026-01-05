"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Insulins

INSULINS_DRUGS = {
    "Insulin": {'group': 'Diabetes - Insulin', 'vietnamese_name': 'Insulin',
        'administration': ['SC', 'IV'], 'indications': ['Đái tháo đường type 1',
        'Đái tháo đường type 2 (khi không kiểm soát bằng thuốc uống)',
        'Nhiễm toan ceton do đái tháo đường',
        'Tăng đường huyết tăng áp lực thẩm thấu',
        'Tăng đường huyết trong bệnh viện'], 'contraindications': [
        'Hạ đường huyết', 'Dị ứng insulin'], 'dosage': {'type1_basal':
        '0.2-0.4 đơn vị/kg/ngày (NPH hoặc insulin dài)', 'type1_bolus':
        '0.5-1 đơn vị/kg/ngày chia trước bữa ăn', 'dka_iv':
        '0.1 đơn vị/kg/giờ IV truyền liên tục', 'hospital_hyperglycemia':
        '0.05-0.1 đơn vị/kg/giờ', 'notes':
        'Nhiều loại: rapid-acting, short-acting, intermediate, long-acting. Điều chỉnh theo đường huyết'
        }, 'side_effects': ['Hạ đường huyết (nguy hiểm)', 'Tăng cân',
        'Phản ứng tại chỗ tiêm', 'Kháng insulin (hiếm)'], 'interactions': [
        'Beta-blocker: che dấu triệu chứng hạ đường huyết',
        'Corticosteroid: tăng đường huyết', 'Rượu: tăng nguy cơ hạ đường huyết'
        ], 'pregnancy': 'B - An toàn, điều chỉnh liều theo thai kỳ',
        'mechanism_of_action':
        'Insulin là hormone tự nhiên được tiết ra từ tế bào beta tuyến tụy. Gắn với thụ thể insulin, kích hoạt các tín hiệu nội bào, tăng vận chuyển glucose vào tế bào, kích thích tổng hợp glycogen, protein, lipid, và ức chế sản xuất glucose ở gan. Giảm đường huyết bằng cách tăng sử dụng glucose và giảm sản xuất glucose'
        , 'monitoring': [
        'Đường huyết (glucose) thường xuyên: Trước bữa ăn, 2 giờ sau bữa ăn, trước khi ngủ'
        , 'HbA1c mỗi 3 tháng (mục tiêu <7% hoặc theo cá thể hóa)',
        'Dấu hiệu hạ đường huyết: Run rẩy, đổ mồ hôi, nhịp tim nhanh, đói, nhầm lẫn, co giật, hôn mê'
        , 'Dấu hiệu tăng đường huyết: Khát nhiều, tiểu nhiều, mệt mỏi, mờ mắt',
        'Cân nặng (insulin có thể gây tăng cân)',
        'Chức năng thận (giảm clearance insulin ở suy thận)',
        'Kiểm tra vị trí tiêm (tránh lipodystrophy)'], 'precautions': [
        'LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết',
        'Điều chỉnh liều theo đường huyết, bữa ăn, hoạt động thể chất',
        'Xoay vị trí tiêm (bụng, đùi, cánh tay, mông)',
        'Bảo quản đúng cách: Insulin đang dùng có thể để ở nhiệt độ phòng, chưa mở phải để tủ lạnh'
        , 'Không được làm đông lạnh insulin',
        'Giảm liều ở suy thận (giảm clearance)',
        'Tăng liều trong bệnh nặng, stress, nhiễm trùng',
        'Dạy bệnh nhân nhận biết và xử trí hạ đường huyết',
        'Trong thai kỳ: tăng nhu cầu insulin, điều chỉnh thường xuyên'],
        'pharmacokinetics': {'half_life':
        'Rapid-acting (lispro, aspart): 1 giờ; Short-acting (regular): 2-4 giờ; Intermediate (NPH): 8-12 giờ; Long-acting (glargine, detemir): 12-24 giờ; Ultra-long (degludec): 42 giờ'
        , 'onset':
        'Rapid: 15 phút; Short: 30-60 phút; Intermediate: 1-3 giờ; Long: 1-2 giờ',
        'duration':
        'Rapid: 3-5 giờ; Short: 6-8 giờ; Intermediate: 12-16 giờ; Long: 18-24 giờ; Ultra-long: >42 giờ'
        , 'protein_binding': 'Không (peptide hormone)', 'clearance':
        'Gan (50-60%), thận (30-40%), một phần bị phân hủy bởi insulinase'},
        'storage':
        'Chưa mở: Tủ lạnh (2-8°C), không đông lạnh. Đang dùng: Nhiệt độ phòng (<30°C), tránh ánh sáng, tránh nhiệt độ cao. Dùng trong vòng 28-30 ngày sau khi mở'
        , 'black_box_warnings':
        'Hạ đường huyết có thể đe dọa tính mạng. Cần theo dõi đường huyết thường xuyên và có sẵn glucose/glucagon để điều trị hạ đường huyết. Không được dùng chung ống tiêm insulin'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (atenolol, metoprolol, propranolol)', 'mechanism':
        'Beta-blockers che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run, đổ mồ hôi) và ức chế glycogenolysis'
        , 'effect':
        'Tăng nguy cơ hạ đường huyết nặng, khó nhận biết triệu chứng, khó điều trị'
        , 'management':
        'Theo dõi đường huyết thường xuyên. Bệnh nhân nên biết các triệu chứng hạ đường huyết khác (lú lẫn, đổ mồ hôi). Cân nhắc dùng beta-1 selective (atenolol, metoprolol) thay vì non-selective (propranolol).'
        }, {'drug': 'Rượu (ethanol)', 'mechanism':
        'Rượu ức chế gluconeogenesis ở gan, tăng nguy cơ hạ đường huyết, đặc biệt khi đói'
        , 'effect':
        'Tăng nguy cơ hạ đường huyết nặng, có thể hôn mê, đặc biệt khi uống rượu mà không ăn'
        , 'management':
        'Tránh uống rượu khi đói. Nếu uống rượu, nên ăn kèm. Theo dõi đường huyết sau khi uống rượu. Giáo dục bệnh nhân về nguy cơ.'
        }, {'drug':
        'Corticosteroids (prednisone, dexamethasone, hydrocortisone)',
        'mechanism':
        'Corticosteroids tăng sản xuất glucose ở gan, tăng insulin resistance, tăng đường huyết'
        , 'effect':
        'Giảm hiệu quả insulin, tăng nhu cầu insulin, tăng đường huyết',
        'management':
        'Tăng liều insulin khi dùng corticosteroid. Theo dõi đường huyết thường xuyên. Giảm liều insulin khi ngừng corticosteroid.'
        }], 'moderate': [{'drug':
        'Thiazide diuretics (hydrochlorothiazide, chlorthalidone)', 'mechanism':
        'Thiazide có thể gây hạ kali máu, tăng đường huyết nhẹ', 'effect':
        'Tăng nhẹ đường huyết, có thể cần tăng liều insulin', 'management':
        'Theo dõi đường huyết. Có thể cần tăng liều insulin nhẹ.'}, {'drug':
        'Sulfonylureas (glibenclamide, gliclazide)', 'mechanism':
        'Cả hai đều kích thích tiết insulin, tác dụng hiệp đồng', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thường không dùng cùng. Nếu cần, giảm liều cả hai. Theo dõi đường huyết chặt chẽ.'
        }, {'drug': 'ACE inhibitors, ARB (enalapril, losartan)', 'mechanism':
        'ACE inhibitors có thể tăng nhạy cảm với insulin, tăng nguy cơ hạ đường huyết'
        , 'effect': 'Tăng nguy cơ hạ đường huyết nhẹ', 'management':
        'Theo dõi đường huyết. Có thể cần giảm liều insulin nhẹ.'}, {'drug':
        'MAO inhibitors', 'mechanism':
        'MAO inhibitors có thể tăng tác dụng insulin', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Theo dõi đường huyết. Có thể cần giảm liều insulin.'}, {'drug':
        'Pentamidine (antiparasitic)', 'mechanism':
        'Pentamidine có thể gây hạ đường huyết (phá hủy tế bào beta) hoặc tăng đường huyết'
        , 'effect': 'Hạ đường huyết hoặc tăng đường huyết', 'management':
        'Theo dõi đường huyết chặt chẽ. Điều chỉnh liều insulin theo đường huyết.'
        }], 'minor': [{'drug': 'Aspirin liều thấp', 'mechanism':
        'Aspirin có thể tăng nhẹ tác dụng insulin', 'effect':
        'Tăng nhẹ nguy cơ hạ đường huyết', 'management':
        'Thường không cần điều chỉnh. Theo dõi đường huyết.'}, {'drug':
        'Thyroid hormones (levothyroxine)', 'mechanism':
        'Thyroid hormones tăng chuyển hóa, có thể tăng nhu cầu insulin',
        'effect': 'Tăng nhẹ nhu cầu insulin', 'management':
        'Theo dõi đường huyết. Có thể cần tăng liều insulin nhẹ khi bắt đầu levothyroxine.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Hạ đường huyết (hypoglycemia) - không được dùng khi đường huyết thấp',
        'Dị ứng insulin hoặc bất kỳ thành phần nào trong chế phẩm insulin',
        'Hôn mê do hạ đường huyết - không được dùng insulin cho đến khi hồi phục'
        ], 'tương_đối': ['Suy thận - giảm clearance insulin, giảm liều insulin',
        'Suy gan - giảm gluconeogenesis, tăng nguy cơ hạ đường huyết, giảm liều insulin'
        , 'Suy tim - thận trọng, có thể cần điều chỉnh liều',
        'Người cao tuổi - tăng nguy cơ hạ đường huyết, cần liều thấp hơn',
        'Bệnh nhân không có khả năng tự quản lý - cần người chăm sóc',
        'Bệnh nhân không có khả năng nhận biết hạ đường huyết - tăng nguy cơ',
        'Thai kỳ - điều chỉnh liều thường xuyên (tăng nhu cầu trong tam cá nguyệt 2-3)'
        ]}, 'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Insulin là thuốc được ưu tiên trong thai kỳ cho đái tháo đường. Insulin không qua nhau thai, an toàn cho thai nhi. Nhu cầu insulin tăng trong thai kỳ, đặc biệt ở tam cá nguyệt 2-3 (tăng 50-100%). Cần điều chỉnh liều thường xuyên. Hạ đường huyết mẹ có thể ảnh hưởng đến thai nhi. Tăng đường huyết mẹ có thể gây dị tật thai nhi, thai to, hạ đường huyết ở trẻ sơ sinh. Mục tiêu đường huyết: <95 mg/dL (trước ăn), <140 mg/dL (1 giờ sau ăn), <120 mg/dL (2 giờ sau ăn).'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Insulin không bài tiết vào sữa mẹ ở nồng độ đáng kể. Insulin là protein, bị tiêu hóa trong đường tiêu hóa của trẻ, không hấp thu. Insulin là thuốc được ưu tiên cho phụ nữ đái tháo đường cho con bú. Nhu cầu insulin có thể giảm nhẹ khi cho con bú (do tiêu thụ glucose).'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Insulin là thuốc được ưu tiên cho phụ nữ đái tháo đường cho con bú. Theo dõi đường huyết và điều chỉnh liều nếu cần.'
        }}, 'hepatic_adjustment': {'mild':
        'Thận trọng. Giảm liều insulin 10-20% do giảm gluconeogenesis, tăng nguy cơ hạ đường huyết.'
        , 'moderate':
        'Thận trọng. Giảm liều insulin 20-30%. Theo dõi đường huyết thường xuyên. Tăng nguy cơ hạ đường huyết.'
        , 'severe':
        'Thận trọng. Giảm liều insulin 30-50%. Theo dõi đường huyết rất thường xuyên. Tăng nguy cơ hạ đường huyết nặng. Cân nhắc dùng insulin tác dụng ngắn và điều chỉnh theo đường huyết.'
        , 'notes':
        'Insulin chuyển hóa chủ yếu ở gan (50-60%). Suy gan làm giảm gluconeogenesis và glycogenolysis, tăng nguy cơ hạ đường huyết. Cần giảm liều insulin và theo dõi đường huyết thường xuyên.'
        }, 'overdose_management': {'symptoms': [
        'Hạ đường huyết (hypoglycemia) - triệu chứng chính và nguy hiểm nhất',
        'Triệu chứng nhẹ đến trung bình: Run rẩy, đổ mồ hôi, nhịp tim nhanh, đói, lo lắng, nhức đầu, nhầm lẫn nhẹ'
        ,
        'Triệu chứng nặng: Co giật, hôn mê, mất ý thức, rối loạn hành vi, yếu cơ, nhìn đôi'
        , 'Hạ đường huyết nặng có thể gây tổn thương não vĩnh viễn, tử vong',
        'Tăng kali máu (hiếm, với insulin IV liều cao)',
        'Hạ kali máu (do điều trị hạ đường huyết với glucose)'], 'antidote':
        'Glucagon (đối kháng insulin, kích thích glycogenolysis), Glucose (điều trị trực tiếp hạ đường huyết)'
        , 'treatment': [
        'Đo đường huyết ngay (nếu có thể, nhưng không trì hoãn điều trị nếu nghi ngờ hạ đường huyết)'
        , 'Nếu bệnh nhân tỉnh và có thể nuốt:',
        '  - Glucose 15-20g đường miệng (4 viên glucose, 1/2 lon nước ngọt, 1/2 cốc nước trái cây, 1 thìa mật ong)'
        , '  - Lặp lại sau 15 phút nếu đường huyết vẫn <70 mg/dL',
        '  - Ăn bữa ăn hoặc snack sau khi đường huyết ổn định',
        'Nếu bệnh nhân không tỉnh hoặc không thể nuốt:',
        '  - Glucagon 1mg SC/IM (có thể lặp lại sau 15 phút nếu cần)',
        '  - HOẶC Dextrose 50% 50ml IV (có thể lặp lại)',
        '  - HOẶC Dextrose 10% truyền IV liên tục nếu cần',
        '  - Theo dõi đường huyết mỗi 15-30 phút cho đến khi ổn định',
        'Ngừng insulin tạm thời (nếu đang truyền liên tục)',
        'Theo dõi đường huyết thường xuyên (mỗi 15-30 phút) cho đến khi ổn định',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ý thức',
        'Theo dõi kali máu (có thể hạ kali sau khi điều trị hạ đường huyết)',
        'Hỗ trợ hô hấp nếu cần',
        'Theo dõi ít nhất 24 giờ (tùy loại insulin - rapid-acting 3-5 giờ, long-acting 18-24 giờ)'
        ], 'monitoring':
        'Đường huyết (mỗi 15-30 phút cho đến khi ổn định), dấu hiệu sinh tồn (huyết áp, nhịp tim, ý thức), kali máu (có thể hạ kali), dấu hiệu hạ đường huyết tái phát, dấu hiệu tổn thương não (nếu hạ đường huyết nặng kéo dài)'
        }, 'reversal_agents': {'available': True, 'agents': [{'name':
        'Glucagon', 'mechanism':
        'Kích thích glycogenolysis ở gan, tăng đường huyết, đối kháng tác dụng insulin'
        , 'dose': '1mg SC/IM, có thể lặp lại sau 15 phút nếu cần', 'indication':
        'Hạ đường huyết nặng, đặc biệt khi bệnh nhân không tỉnh hoặc không thể nuốt'
        }, {'name': 'Glucose (Dextrose)', 'mechanism':
        'Cung cấp glucose trực tiếp, tăng đường huyết', 'dose':
        'Dextrose 50% 50ml IV, hoặc Dextrose 10% truyền IV liên tục',
        'indication': 'Hạ đường huyết nặng, đặc biệt khi bệnh nhân không tỉnh'},
        {'name': 'Glucose đường miệng', 'mechanism':
        'Cung cấp glucose trực tiếp qua đường tiêu hóa', 'dose':
        '15-20g glucose (4 viên glucose, 1/2 lon nước ngọt, 1/2 cốc nước trái cây)'
        , 'indication':
        'Hạ đường huyết nhẹ đến trung bình, bệnh nhân tỉnh và có thể nuốt'}]},
        'administration_instructions': {'oral': {'with_food':
        'Không áp dụng - insulin không uống được', 'timing': 'Không áp dụng'},
        'iv': {'reconstitution':
        'Insulin regular (short-acting) có thể dùng IV. Pha trong normal saline hoặc dextrose. Nồng độ thường: 0.05-0.1 đơn vị/kg/giờ trong DKA hoặc tăng đường huyết trong bệnh viện.'
        , 'infusion_rate':
        'Truyền liên tục với tốc độ điều chỉnh theo đường huyết. Thường bắt đầu với 0.05-0.1 đơn vị/kg/giờ. Điều chỉnh theo protocol insulin sliding scale hoặc theo đường huyết.'
        , 'compatibility': ['Normal saline (0.9% NaCl)', 'Dextrose 5% (D5W)',
        'Dextrose 10% (D10W)', "Ringer's lactate"], 'incompatibility': [
        'Không trộn với các thuốc khác trong cùng ống truyền',
        'Một số thuốc có thể làm giảm hiệu quả insulin (cần kiểm tra cụ thể)'],
        'notes':
        'Insulin IV chỉ dùng trong bệnh viện, DKA, hoặc tăng đường huyết nặng. Phải có protocol rõ ràng và theo dõi đường huyết thường xuyên (mỗi 1-2 giờ).'
        }, 'sc': {'with_food':
        'Rapid-acting insulin: Tiêm 15 phút TRƯỚC bữa ăn. Short-acting insulin: Tiêm 30-60 phút TRƯỚC bữa ăn. Long-acting insulin: Tiêm 1 lần/ngày, không phụ thuộc bữa ăn.'
        , 'timing':
        'Rapid-acting (lispro, aspart): 15 phút trước bữa ăn. Short-acting (regular): 30-60 phút trước bữa ăn. Intermediate (NPH): 1-3 giờ trước bữa ăn. Long-acting (glargine, detemir): 1 lần/ngày, cùng một giờ mỗi ngày. Xoay vị trí tiêm (bụng, đùi, cánh tay, mông).'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Various insulin products',
        'UpToDate - Insulin therapy in type 1 and type 2 diabetes',
        'American Diabetes Association (ADA) Standards of Medical Care in Diabetes'
        , 'American Association of Clinical Endocrinologists (AACE) Guidelines',
        'DCCT Study - New England Journal of Medicine (1993) - Intensive insulin therapy in type 1 diabetes'
        ,
        'UKPDS Study - Lancet (1998) - Intensive glucose control in type 2 diabetes'
        ,
        "Goodman & Gilman's Pharmacological Basis of Therapeutics - Insulin and oral hypoglycemic agents"
        ], 'last_updated': '2025-02-18', 'evidence_level':
        'High - Multiple large RCTs (DCCT, UKPDS) showing benefit of intensive glucose control'
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "High (hypoglycemia)"}
        },
        "guideline_tags": [
            "ADA Standards of Medical Care in Diabetes",
            "AACE/ACE Diabetes Guidelines",
            "IDF Diabetes Guidelines",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
                 "renal_adjustment": {
             "normal": "Không đổi",
             "30_60": "Không đổi",
             "under_30": "Thận trọng, có thể giảm liều",
             "notes": "Insulin chủ yếu chuyển hóa ở gan, nhưng cần thận trọng ở suy thận nặng."
         },
}}

__all__ = ['INSULINS_DRUGS']
