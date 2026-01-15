"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# NSAIDs

NSAIDS_DRUGS = {
    "Aspirin":     {
        "group": "Analgesic - NSAID/Antiplatelet",
        "vietnamese_name": "Aspirin, Acetylsalicylic acid, ASA",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Sốt",
            "Viêm khớp",
            "Phòng ngừa nhồi máu cơ tim",
            "Phòng ngừa đột quỵ",
            "Dự phòng tim mạch thứ phát",
            "Gout"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng aspirin/NSAID (phản vệ, hen phế quản do aspirin)",
                "Trẻ em <12 tuổi - CHỐNG CHỈ ĐỊNH (hội chứng Reye)",
                "Loét dạ dày tá tràng đang hoạt động",
                "Chảy máu đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)"
    ],
            "tương_đối": [
                "Suy thận nặng - thận trọng",
                "Suy gan nặng - thận trọng",
                "Dùng với warfarin - tăng nguy cơ chảy máu"
    ],
        },
        "dosage": {
            "adult_pain_fever": "325-650mg mỗi 4 giờ (tối đa 4g/ngày)",
            "adult_arthritis": "2.4-5.4g/ngày chia nhiều lần",
            "adult_cardiac_protection": "75-100mg x 1 lần/ngày",
            "adult_stroke_prevention": "75-100mg x 1 lần/ngày",
            "notes": """Liều thấp (75-100mg/ngày) cho dự phòng tim mạch. Liều cao cho đau/viêm. Không dùng cho trẻ <12 tuổi (hội chứng Reye)""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều",
        },
        "side_effects": [
            "Chảy máu dạ dày (phổ biến)",
            "Chảy máu nói chung (liều thấp)",
            "Tinnitus (ù tai) ở liều cao",
            "Suy thận",
            "Tăng huyết áp",
            "Hội chứng Reye ở trẻ em (nguy hiểm tính mạng)",
            "Phản ứng dị ứng (hen phế quản do aspirin)"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "Các thuốc chống đông khác: tăng nguy cơ chảy máu",
            "NSAID khác: tăng nguy cơ chảy máu dạ dày",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate",
            "Đái tháo đường: có thể tăng/giảm đường huyết"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Aspirin ức chế không hồi phục enzyme cyclooxygenase (COX-1 và COX-2) bằng cách acetyl hóa serine residue, khác với các NSAID khác (ức chế hồi phục). Giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Ở liều thấp (75-100mg/ngày): ức chế COX-1 trong tiểu cầu → giảm tổng hợp thromboxane A2 → chống kết tập tiểu cầu → dự phòng nhồi máu cơ tim và đột quỵ. Ở liều cao (>1g/ngày): giảm đau, kháng viêm, hạ sốt giống các NSAID khác. Đặc điểm: tác dụng chống kết tập tiểu cầu kéo dài (7-10 ngày) do tiểu cầu không có nhân, không thể tạo COX-1 mới.""",
        "monitoring": [
            "Dấu hiệu chảy máu (dạ dày, niêm mạc, chảy máu nói chung) - đặc biệt với liều thấp (dự phòng tim mạch)",
            "Tinnitus (ù tai) ở liều cao - dấu hiệu ngộ độc aspirin",
            "Creatinine, BUN nếu dùng lâu dài",
            "Huyết áp",
            "Chức năng gan (transaminase) nếu dùng lâu dài",
            "INR nếu dùng với warfarin"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi (hội chứng Reye - nguy hiểm tính mạng)",
            "Chảy máu - nguy cơ cao, đặc biệt với liều thấp (dự phòng tim mạch)",
            "Tinnitus ở liều cao - dấu hiệu ngộ độc, cần giảm liều",
            "Tránh dùng với warfarin (tăng nguy cơ chảy máu nặng)",
            "Tránh dùng với NSAID khác (tăng nguy cơ chảy máu dạ dày)",
            "Liều thấp (75-100mg/ngày) cho dự phòng tim mạch - không dùng liều cao",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Ngừng trước phẫu thuật 5-7 ngày (do tác dụng chống kết tập tiểu cầu kéo dài)",
            "Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)"
    ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (liều thấp), 15-30 giờ (liều cao)",
            "onset": "30-60 phút",
            "duration": "4-6 giờ (đau), 7-10 ngày (chống kết tập tiểu cầu)",
            "protein_binding": "50-80%",
            "clearance": "Gan (chuyển hóa thành salicylic acid), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": """CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi - có thể gây hội chứng Reye (nguy hiểm tính mạng, tổn thương gan và não). Aspirin có thể gây chảy máu nghiêm trọng, đặc biệt ở liều thấp (dự phòng tim mạch). Không dùng trong 3 tháng cuối thai kỳ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": """Aspirin ức chế COX-1, giảm tổng hợp thromboxane, chống kết tập tiểu cầu. Tác dụng hiệp đồng với warfarin.""",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": """Thận trọng. Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin. Hoặc cân nhắc dùng clopidogrel thay vì aspirin cho dự phòng tim mạch.""",
                }
                ],
            "moderate": [
    {
                    "drug": "NSAID khác (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Tác dụng hiệp đồng ức chế COX-1, tăng nguy cơ chảy máu dạ dày",
                    "effect": "Tăng nguy cơ chảy máu dạ dày",
                    "management": "Tránh dùng đồng thời. Nếu cần, cân nhắc dùng PPI để bảo vệ dạ dày.",
                },
    {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": """Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi.""",
            "lactation": {
                "safety": "Compatible with caution",
                "details": """Aspirin bài tiết vào sữa mẹ. Nồng độ trong sữa mẹ thấp. Tuy nhiên, liều cao có thể gây hội chứng Reye ở trẻ. Liều thấp (75-100mg/ngày) an toàn hơn.""",
                "recommendation": "Có thể dùng khi cho con bú với liều thấp (75-100mg/ngày). Tránh liều cao.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Aspirin chuyển hóa ở gan. Suy gan có thể ảnh hưởng đến chuyển hóa.",
        },
        # Sample data for new features
        "image_url": "https://www.drugs.com/images/pills/fio/ASA01.JPG",  # Sample image URL
        "image_source": "Drugs.com",
        "evidence_levels": {
            "mechanism_of_action": "A",  # Strong evidence
            "indications": "A",  # Strong evidence for cardiovascular protection
            "dosing": "A",  # Strong evidence
            "safety": "B",  # Moderate evidence (bleeding risk)
        },
        "toxicity_management": {
            "symptoms": [
                "Tinnitus (ù tai) - dấu hiệu sớm",
                "Buồn nôn, nôn",
                "Chóng mặt, nhức đầu",
                "Tăng thông khí (tăng nhịp thở)",
                "Toan chuyển hóa",
                "Sốt",
                "Hạ đường huyết",
                "Co giật (liều rất cao)",
                "Suy hô hấp, tử vong"
            ],
            "antidote": {
                "name": "Không có antidote đặc hiệu",
                "dose": "Sodium bicarbonate để kiềm hóa nước tiểu (tăng thải trừ salicylate)"
            },
            "treatment": [
                "Ngừng aspirin ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Sodium bicarbonate để kiềm hóa nước tiểu (pH >7.5) - tăng thải trừ aspirin",
                "Theo dõi nồng độ salicylate trong máu",
                "Điều trị toan chuyển hóa: sodium bicarbonate IV",
                "Điều trị hạ đường huyết: glucose IV",
                "Điều trị sốt: làm mát, paracetamol",
                "Hỗ trợ hô hấp nếu suy hô hấp",
                "Lọc máu (hemodialysis) nếu nồng độ salicylate rất cao (>100mg/dL)"
            ],
            "monitoring": [
                "Nồng độ salicylate trong máu (nếu có thể)",
                "pH máu, HCO3",
                "Điện giải (Na, K, Cl)",
                "Glucose máu",
                "Dấu hiệu sống (BP, HR, RR, SpO2)",
                "Dấu hiệu chảy máu",
                "Chức năng thận (creatinine, BUN)"
            ],
            "lethal_dose": "LD50: 175mg/kg (chuột). Ở người: >150mg/kg có thể gây tử vong. Liều gây chết thường >10g ở người lớn."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (quan trọng)",
                "timing": """Đau/sốt: 325-650mg mỗi 4 giờ. Dự phòng tim mạch: 75-100mg x 1 lần/ngày. Viêm khớp: 2.4-5.4g/ngày chia nhiều lần.""",
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aspirin",
                "UpToDate - Aspirin: Drug information",
                "ACC/AHA Guidelines - Aspirin for Cardiovascular Prevention"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, multiple RCTs for cardiovascular prevention",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {
                "hepatic": "unknown",
                "renal": "unknown",
                "cardiac": "unknown",
                "hematologic": "unknown",
            },
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Celecoxib": {'group': 'Analgesic - NSAID (COX-2 Selective)',
        'vietnamese_name':
        'Celecoxib, Celebrex', 'administration': ['PO'],
        'indications': [
        'Đau nhẹ đến trung bình', 'Viêm khớp dạng thấp', 'Viêm khớp xương khớp',
        'Đau bụng kinh', 'Đau cấp tính'],
        'contraindications': [
        'Dị ứng celecoxib, sulfonamides', 'Loét dạ dày tá tràng đang hoạt động',
        'Suy thận nặng', 'Suy gan nặng', 'Có thai (3 tháng cuối)',
        'Bệnh tim mạch nặng'],
        'dosage': {'adult_po':
        '100-200mg x 1-2 lần/ngày (tối đa 400mg/ngày)', 'notes':
        'COX-2 selective, ít tác dụng phụ dạ dày nhất. Tăng nguy cơ tim mạch'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, giảm liều', 'under_30': 'Tránh dùng'},
        'side_effects': [
        'Tăng nguy cơ nhồi máu cơ tim, đột quỵ (cao hơn NSAID khác)',
        'Chảy máu dạ dày (ít hơn NSAID không chọn lọc)', 'Suy thận', 'Tăng huyết áp',
        'Phù', 'Đau đầu', 'Ban da'],
        'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Fluconazole: tăng nồng độ celecoxib (ức chế CYP2C9)',
        'Methotrexate: tăng độc tính methotrexate'],
        'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế chọn lọc mạnh enzyme cyclooxygenase-2 (COX-2), ít ảnh hưởng đến COX-1. Giảm tổng hợp prostaglandin gây viêm (từ COX-2) nhưng ít ảnh hưởng đến prostaglandin bảo vệ dạ dày và chống kết tập tiểu cầu (từ COX-1). Do đó, celecoxib có ít tác dụng phụ dạ dày nhất trong các NSAID, nhưng tăng nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ) do giảm prostacyclin (bảo vệ tim mạch) từ COX-2. Tác dụng kháng viêm và giảm đau.',
        'monitoring': [
        'Dấu hiệu biến cố tim mạch (đau ngực, khó thở, đột quỵ) - nguy cơ cao hơn NSAID khác',
        'Dấu hiệu chảy máu dạ dày (ít hơn NSAID không chọn lọc nhưng vẫn có)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)'],
        'precautions': [
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'COX-2 selective → ít tác dụng phụ dạ dày nhất, nhưng TĂNG NGUY CƠ TIM MẠCH',
        'CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh tim mạch nặng, tiền sử nhồi máu cơ tim, đột quỵ',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Tương tác với fluconazole (tăng nồng độ celecoxib)'],
        'pharmacokinetics': {
        'half_life': '11 giờ', 'onset': '30-60 phút', 'duration': '12-24 giờ',
        'protein_binding': '97%', 'metabolism':
        'Gan (chuyển hóa qua CYP2C9 thành các chất chuyển hóa không hoạt động). Chuyển hóa chủ yếu qua CYP2C9, một phần qua CYP3A4. Tương tác với fluconazole (ức chế CYP2C9) làm tăng nồng độ celecoxib.',
        'clearance': 'Thận (thải trừ các chất chuyển hóa, <3% bài tiết dưới dạng không đổi)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Tăng nguy cơ nhồi máu cơ tim và đột quỵ nghiêm trọng, có thể tử vong. Nguy cơ tăng khi dùng lâu dài hoặc liều cao. CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh tim mạch nặng, tiền sử nhồi máu cơ tim, đột quỵ. Không dùng trong 3 tháng cuối thai kỳ.',
        'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Celecoxib ức chế COX-2, có thể tăng nguy cơ chảy máu', 'effect':
        'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }, {'drug': 'Fluconazole, các thuốc ức chế CYP2C9', 'mechanism':
        'Ức chế chuyển hóa celecoxib qua CYP2C9', 'effect':
        'Tăng nồng độ celecoxib, tăng nguy cơ tác dụng phụ', 'management':
        'Giảm liều celecoxib 50% khi dùng với fluconazole. Theo dõi tác dụng phụ.'}],
        'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Methotrexate', 'mechanism': 'Giảm thải trừ methotrexate qua thận',
        'effect': 'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }],
        'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng celecoxib, sulfonamides (celecoxib chứa nhóm sulfonamide)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Bệnh tim mạch nặng, tiền sử nhồi máu cơ tim, đột quỵ - CHỐNG CHỈ ĐỊNH do tăng nguy cơ biến cố tim mạch'
        , 'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'],
        'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ, đặc biệt biến cố tim mạch']},
        'pregnancy_lactation': {'fda_category': 'C - D trong tam cá nguyệt 3',
        'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.',
        'lactation': {'safety': 'Compatible', 'details':
        'Celecoxib bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ. An toàn cho trẻ bú mẹ.',
        'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm).'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Celecoxib chuyển hóa ở gan qua CYP2C9. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tương tác với fluconazole (ức chế CYP2C9) làm tăng nồng độ celecoxib.'},
        'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ', 'Hạ huyết áp', 'Suy thận cấp',
        'Chảy máu dạ dày', 'Biến cố tim mạch (đau ngực, khó thở)', 'Co giật (hiếm)'],
        'antidote': 'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim, ECG (nguy cơ biến cố tim mạch)',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ECG, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu, dấu hiệu biến cố tim mạch. Theo dõi ít nhất 24 giờ do half-life (11 giờ)'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị chảy máu dạ dày và biến cố tim mạch nếu có. Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        '1-2 lần/ngày. Có thể dùng vào buổi sáng và tối. Dùng với bữa ăn để giảm tác dụng phụ dạ dày. Liều tối đa: 400mg/ngày.'
        },
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': []}},
        'references': {'primary_sources': [
        'FDA Drug Label - Celebrex (celecoxib)',
        'UpToDate - Celecoxib: Drug information',
        'Lexicomp - Celecoxib monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05',
        'evidence_level': 'High - FDA-approved'
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": True,
            "organ_toxicity": ["GI", "renal", "cardiac"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["LFT", "RFT", "GI symptoms", "Blood pressure", "Cardiovascular symptoms"]
        },
        "guideline_tags": [
            "ACR 2021 Osteoarthritis Guidelines",
            "FDA Black Box Warning - Cardiovascular and GI risks",
            "ISMP High Alert Medications - NSAIDs"
        ],
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <2 tuổi",
            "infants": "Không khuyến cáo cho trẻ <2 tuổi",
            "children_2_12": "Chưa được FDA phê duyệt cho trẻ em <18 tuổi. Không khuyến cáo sử dụng.",
            "adolescents_12_18": "Chưa được FDA phê duyệt cho trẻ em <18 tuổi. Không khuyến cáo sử dụng.",
            "notes": "Celecoxib chưa được FDA phê duyệt cho trẻ em dưới 18 tuổi. Không nên sử dụng ở trẻ em do thiếu dữ liệu an toàn và hiệu quả."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ, đặc biệt là biến cố tim mạch (nhồi máu cơ tim, đột quỵ), suy thận, và chảy máu dạ dày. Suy thận và suy tim phổ biến hơn ở người cao tuổi.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (100mg x 1 lần/ngày). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài. Đặc biệt thận trọng ở bệnh nhân có bệnh tim mạch.",
            "monitoring": "Theo dõi dấu hiệu biến cố tim mạch sát hơn (đau ngực, khó thở, đột quỵ). Theo dõi chức năng thận (creatinine, BUN) thường xuyên. Theo dõi dấu hiệu chảy máu dạ dày. Theo dõi huyết áp."
        },
        "brand_names": {
            "vietnam": ["Celebrex", "Celecoxib", "Celecoxib Stada", "Celecoxib Teva"],
            "common": ["Celebrex", "Celecoxib"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "15,000 - 50,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Celecoxib generic thường rẻ hơn (15,000-30,000 VND/viên 200mg). Celebrex (brand) đắt hơn (30,000-50,000 VND/viên 200mg)."
        }
    },
    "Diclofenac": {'group': 'Analgesic - NSAID',
        'vietnamese_name': 'Diclofenac, Voltaren',
        'administration': ['PO', 'IM', 'Topical'],
        'indications': [
        'Đau nhẹ đến trung bình', 'Viêm khớp dạng thấp', 'Viêm khớp xương khớp',
        'Đau sau phẫu thuật', 'Đau do chấn thương', 'Viêm gân (topical)'],
        'contraindications': ['Loét dạ dày tá tràng đang hoạt động',
        'Suy thận nặng', 'Suy gan nặng', 'Có thai (3 tháng cuối)',
        'Dị ứng NSAID/aspirin', 'Suy tim nặng'],
        'dosage': {'adult_po':
        '50mg x 2-3 lần/ngày hoặc 75-100mg x 1 lần/ngày (extended release)',
        'adult_im': '75mg IM x 1-2 lần/ngày (tối đa 3 ngày)', 'adult_topical':
        'Bôi 2-4g x 3-4 lần/ngày', 'notes':
        'Hiệu quả cao nhưng nguy cơ tác dụng phụ cao'},
        'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Thận trọng, giảm liều', 'under_30':
        'Tránh dùng'},
        'side_effects': [
        'Chảy máu dạ dày (cao hơn các NSAID khác)', 'Suy thận', 'Tăng huyết áp',
        'Phù', 'Tăng men gan', 'Đau đầu', 'Ban da'],
        'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Digoxin: tăng nồng độ digoxin',
        'Methotrexate: tăng độc tính methotrexate'],
        'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), ưu tiên COX-2 hơn một số NSAID khác. Giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận. Tác dụng kháng viêm và giảm đau mạnh. Có nhiều dạng: uống, tiêm bắp, bôi tại chỗ. Dạng bôi tại chỗ có ít tác dụng phụ hệ thống hơn.'
        , 'monitoring': [
        'Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng) - nguy cơ cao hơn các NSAID khác'
        , 'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (ALT, AST) - diclofenac có nguy cơ tăng men gan cao hơn',
        'Dấu hiệu suy tim (giữ nước, phù)', 'Lithium máu nếu dùng với lithium',
        'Cyclosporine levels nếu dùng với cyclosporine'],
        'precautions': [
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày (nguy cơ cao)'
        , 'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Dạng bôi tại chỗ: ít tác dụng phụ hệ thống, phù hợp cho đau cục bộ',
        'IM: chỉ dùng tối đa 3 ngày, không dùng lâu dài',
        'Theo dõi chức năng gan chặt chẽ (nguy cơ tăng men gan)'],
        'pharmacokinetics': {'half_life':
        '1-2 giờ (ngắn), nhưng tác dụng kéo dài do tích lũy trong dịch khớp',
        'onset': '30-60 phút (PO), 10-15 phút (IM)', 'duration': '8-12 giờ',
        'protein_binding': '99.7%', 'metabolism':
        'Gan (chuyển hóa qua CYP2C9 và CYP3A4 thành các chất chuyển hóa hydroxyl hóa và glucuronide). Chuyển hóa chủ yếu qua CYP2C9, một phần qua CYP3A4. Có nguy cơ tăng men gan cao hơn các NSAID khác do chuyển hóa qua gan.',
        'clearance': 'Thận (thải trừ các chất chuyển hóa, <1% bài tiết dưới dạng không đổi)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng bôi: bảo quản ở nhiệt độ phòng, không làm lạnh.'
        , 'black_box_warnings':
        'Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao. Diclofenac có nguy cơ tăng men gan và chảy máu dạ dày cao hơn một số NSAID khác.'
        , 'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu',
        'effect': 'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }, {'drug': 'ACE inhibitors, ARBs', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Digoxin', 'mechanism': 'Giảm thải trừ digoxin qua thận',
        'effect':
        'Tăng nồng độ digoxin, tăng nguy cơ độc tính (nhịp tim chậm, block nhĩ thất)'
        , 'management':
        'Theo dõi digoxin máu thường xuyên. Có thể cần giảm liều digoxin'}, {
        'drug': 'Methotrexate', 'mechanism':
        'Giảm thải trừ methotrexate qua thận', 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }, {'drug': 'Cyclosporine', 'mechanism': 'Tăng nguy cơ độc tính thận',
        'effect': 'Tăng nguy cơ suy thận cấp', 'management':
        'Theo dõi creatinine, BUN chặt chẽ. Cân nhắc NSAID khác hoặc giảm liều cyclosporine'
        }],
        'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng diclofenac hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy gan nặng (do nguy cơ tăng men gan cao)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'],
        'tương_đối':
        ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan trung bình - thận trọng, theo dõi men gan chặt chẽ',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ, đặc biệt chảy máu dạ dày']
        },
        'pregnancy_lactation': {'fda_category':
        'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Diclofenac bài tiết vào sữa mẹ ở nồng độ rất thấp (<0.1% liều mẹ). An toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dạng bôi tại chỗ: ít ảnh hưởng hệ thống, an toàn hơn.'
        }},
        'hepatic_adjustment': {'mild': 'Không đổi nhưng theo dõi men gan',
        'moderate': 'Thận trọng, giảm liều 25-50%, theo dõi men gan chặt chẽ',
        'severe': 'TRÁNH DÙNG (chống chỉ định)', 'notes':
        'Diclofenac chuyển hóa ở gan qua CYP2C9 và CYP3A4. Có nguy cơ tăng men gan cao hơn các NSAID khác. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính gan.'
        },
        'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ', 'Hạ huyết áp',
        'Suy thận cấp', 'Chảy máu dạ dày', 'Tăng men gan (ALT, AST)',
        'Co giật (hiếm)'],
        'treatment': ['Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi chức năng gan (ALT, AST) - diclofenac có nguy cơ cao',
        'Theo dõi huyết áp, nhịp tim', 'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, ALT/AST, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 12-24 giờ'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị chảy máu dạ dày và độc tính gan nếu có. Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (quan trọng với diclofenac do nguy cơ cao)'
        , 'timing':
        'Mỗi 8-12 giờ. Dùng với bữa ăn để giảm tác dụng phụ dạ dày.'},
        'im': {
        'notes':
        'Tiêm bắp sâu. Chỉ dùng tối đa 3 ngày, không dùng lâu dài. Có thể gây đau tại chỗ tiêm.'
        }, 'topical': {'notes':
        'Dạng bôi tại chỗ: Bôi 2-4g x 3-4 lần/ngày lên vùng đau. Ít tác dụng phụ hệ thống hơn dạng uống. Không bôi trên vùng da bị tổn thương hoặc niêm mạc.'
        }},
        'references': {'primary_sources': [
        'FDA Drug Label - Voltaren (diclofenac)',
        'UpToDate - Diclofenac: Drug information',
        'Lexicomp - Diclofenac monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-06', 'evidence_level':
        'High - FDA-approved, extensive clinical data'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': True,
            'organ_toxicity': ['GI bleeding/ulceration (less than non-selective NSAIDs)', 'Renal toxicity', 'Cardiovascular events (MI, stroke)'],
        'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': True,
            'requires_monitoring': ['Signs of GI bleeding', 'Renal function (CrCl, BUN)', 'Blood pressure']
        },         'guideline_tags': [
            'FDA Drug Safety Communication - NSAIDs and Cardiovascular Risk',
            'ACR Guidelines - NSAID Use in Arthritis',
            'FDA Black Box Warning - NSAIDs and Pregnancy (3rd trimester)'
        ],
        'pediatric_dosing': {
            'neonates': 'Không khuyến cáo cho trẻ <6 tháng tuổi',
            'infants_6m_2y': '0.5-2mg/kg PO x 2-3 lần/ngày (tối đa 150mg/ngày). Dùng cho sốt và đau.',
            'children_2_12': '1-3mg/kg PO x 2-3 lần/ngày (tối đa 150mg/ngày). Dùng cho sốt, đau, viêm khớp.',
            'adolescents_12_18': 'Liều người lớn: 50mg x 2-3 lần/ngày hoặc 75-100mg x 1 lần/ngày (extended release)',
            'notes': 'Dùng cho sốt, đau, viêm khớp ở trẻ em. Uống với thức ăn để giảm kích ứng dạ dày. Theo dõi dấu hiệu chảy máu dạ dày, suy thận, tăng men gan. Dạng bôi tại chỗ: an toàn hơn cho trẻ em.'
        },
        'geriatric_dosing': {
            'considerations': 'Người cao tuổi nhạy cảm hơn với tác dụng phụ (chảy máu dạ dày, suy thận, tăng men gan). Suy thận, suy tim phổ biến hơn. Nguy cơ tăng men gan cao hơn.',
            'dose_adjustment': 'Khởi đầu với liều thấp hơn (25-50mg x 2 lần/ngày). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài. Theo dõi chức năng gan chặt chẽ.',
            'monitoring': 'Theo dõi dấu hiệu chảy máu dạ dày sát hơn. Theo dõi chức năng thận (creatinine, BUN) thường xuyên. Theo dõi chức năng gan (ALT, AST) - QUAN TRỌNG với diclofenac. Theo dõi huyết áp.'
        },
        'brand_names': {
            'vietnam': ['Voltaren', 'Diclofenac', 'Diclofenac Stada', 'Diclofenac Teva', 'Diclofenac Mylan', 'Voltaren Emulgel (topical)'],
            'common': ['Voltaren', 'Diclofenac', 'Cataflam', 'Voltaren Gel']
        },
        'cost_estimate': {
            'unit': 'VND',
            'range': '3,000 - 25,000 VND/viên (tùy hàm lượng và thương hiệu). Dạng bôi: 50,000 - 150,000 VND/tuýp.',
            'note': 'Giá thay đổi theo thương hiệu và nhà thuốc. Diclofenac generic thường rẻ hơn (3,000-8,000 VND/viên 50mg). Voltaren (brand) đắt hơn (10,000-25,000 VND/viên 50mg). Dạng bôi tại chỗ: 50,000-150,000 VND/tuýp.'
        }},
    "Etoricoxib": {'group': 'Analgesic - NSAID (COX-2 Selective)',
        'vietnamese_name': 'Etoricoxib, Arcoxia', 'administration': ['PO'],
        'indications': ['Đau nhẹ đến trung bình', 'Viêm khớp', 'Đau bụng kinh',
        'Gout cấp'],
        'contraindications': [
        'Loét dạ dày tá tràng đang hoạt động', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai (3 tháng cuối)', 'Dị ứng NSAID/aspirin',
        'Bệnh tim mạch nặng'],
        'dosage': {
        'adult_pain': '60-90mg x 1 lần/ngày',
        'adult_arthritis': '60-90mg x 1 lần/ngày',
        'adult_gout': '120mg x 1 lần/ngày (tối đa 5 ngày)',
        'adult_max': '120mg/ngày', 'notes':
        'COX-2 selective, ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. Dùng 1 lần/ngày.'
        },
        'side_effects': [
        'Tăng nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ)',
        'Tăng huyết áp', 'Phù', 'Suy thận', 'Chóng mặt', 'Đau đầu',
        'Ít tác dụng phụ dạ dày hơn NSAID không chọn lọc'],
        'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Lithium: tăng nồng độ lithium',
        'Methotrexate: tăng độc tính methotrexate'],
        'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế chọn lọc enzyme cyclooxygenase-2 (COX-2), giảm tổng hợp prostaglandin gây viêm và đau. Ít ức chế COX-1 (enzyme bảo vệ niêm mạc dạ dày) nên ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. Tuy nhiên, vẫn có nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ) tương tự các COX-2 selective khác. Dùng 1 lần/ngày, tiện lợi.'
        , 'monitoring': [
        'Dấu hiệu biến cố tim mạch (đau ngực, khó thở, yếu một bên)',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Dấu hiệu suy tim (giữ nước, phù)',
        'INR nếu dùng với warfarin'],
        'precautions': [
        'Tăng nguy cơ biến cố tim mạch - không dùng ở bệnh nhân có bệnh tim mạch nặng',
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ',
        'Theo dõi INR nếu dùng với warfarin',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể'],
        'pharmacokinetics': {
        'half_life': '22 giờ (dài)', 'onset': '30-60 phút', 'duration':
        '24 giờ (dài, dùng 1 lần/ngày)', 'protein_binding': '92%', 'metabolism':
        'Gan (chuyển hóa qua CYP3A4, CYP2C9, CYP2D6 thành các chất chuyển hóa hydroxyl hóa và glucuronide). Chuyển hóa chủ yếu qua CYP3A4, một phần qua CYP2C9 và CYP2D6.',
        'clearance': 'Thận (thải trừ các chất chuyển hóa, <1% bài tiết dưới dạng không đổi)'},
        'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Thận trọng, giảm liều 25-50%', 'under_30':
        'Tránh dùng hoặc giảm liều mạnh. Theo dõi chức năng thận chặt chẽ'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Tăng nguy cơ biến cố tim mạch nghiêm trọng (nhồi máu cơ tim, đột quỵ) - có thể tử vong. Nguy cơ tăng ở bệnh nhân có bệnh tim mạch. Không dùng trong 3 tháng cuối thai kỳ.'
        , 'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-2, tăng nguy cơ chảy máu', 'effect':
        'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }, {'drug': 'ACE inhibitors, ARBs', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng etoricoxib nếu có dấu hiệu suy thận'
        }, {'drug': 'Lithium', 'mechanism': 'Giảm thải trừ lithium qua thận',
        'effect': 'Tăng nồng độ lithium, tăng độc tính', 'management':
        'Theo dõi nồng độ lithium. Có thể cần giảm liều lithium.'}],
        'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng etoricoxib hoặc NSAID/aspirin',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Bệnh tim mạch nặng (nhồi máu cơ tim gần đây, suy tim nặng)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'],
        'tương_đối':
        ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu']},
        'pregnancy_lactation': {'fda_category': 'C - D trong tam cá nguyệt 3',
        'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Etoricoxib bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn.'}},
        'hepatic_adjustment': {
        'mild': 'Không đổi', 'moderate': 'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Etoricoxib chuyển hóa ở gan qua CYP3A4, CYP2C9, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.'
        },
        'overdose_management': {'symptoms': [
        'Buồn nôn, nôn, đau bụng', 'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ',
        'Hạ huyết áp', 'Suy thận cấp', 'Chảy máu dạ dày'],
        'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 24 giờ do half-life dài (22 giờ).'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị chảy máu dạ dày nếu có. Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        'Dùng 1 lần/ngày (tiện lợi). Liều tối đa: 120mg/ngày.'},
        'iv': None},
        'references': {'primary_sources': [
        'FDA Drug Label - Arcoxia (Etoricoxib)',
        'UpToDate - Etoricoxib: Drug information'],
            "evidence_level": "High - FDA approved"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": True,
            "organ_toxicity": ["GI", "renal", "cardiac"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["LFT", "RFT", "GI symptoms", "Blood pressure", "Cardiovascular symptoms"]
        },
        "guideline_tags": [
            "ACR 2021 Osteoarthritis Guidelines",
            "FDA Black Box Warning - Cardiovascular and GI risks",
            "ISMP High Alert Medications - NSAIDs"
        ],
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <12 tuổi",
            "infants": "Không khuyến cáo cho trẻ <12 tuổi",
            "children_12_18": "Chưa được FDA phê duyệt cho trẻ em <18 tuổi. Không khuyến cáo sử dụng.",
            "notes": "Etoricoxib chưa được FDA phê duyệt cho trẻ em dưới 18 tuổi. Không nên sử dụng ở trẻ em do thiếu dữ liệu an toàn và hiệu quả."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ, đặc biệt là biến cố tim mạch (nhồi máu cơ tim, đột quỵ), suy thận. Suy thận và suy tim phổ biến hơn ở người cao tuổi.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (60mg x 1 lần/ngày). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài. Đặc biệt thận trọng ở bệnh nhân có bệnh tim mạch.",
            "monitoring": "Theo dõi dấu hiệu biến cố tim mạch sát hơn (đau ngực, khó thở, đột quỵ). Theo dõi chức năng thận (creatinine, BUN) thường xuyên. Theo dõi dấu hiệu chảy máu dạ dày. Theo dõi huyết áp."
        },
        "brand_names": {
            "vietnam": ["Arcoxia", "Etoricoxib"],
            "common": ["Arcoxia", "Etoricoxib"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "20,000 - 60,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Etoricoxib generic thường rẻ hơn (20,000-40,000 VND/viên 90mg). Arcoxia (brand) đắt hơn (40,000-60,000 VND/viên 90mg)."
        }
    },
    "Ibuprofen": {'group': 'Analgesic - NSAID',
        'vietnamese_name': 'Ibuprofen, Brufen',
        'administration': ['PO'],
        'indications': [
        'Đau nhẹ đến trung bình', 'Viêm khớp', 'Sốt', 'Đau bụng kinh'],
        'contraindications': [
        'Loét dạ dày tá tràng đang hoạt động', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai (3 tháng cuối)', 'Dị ứng NSAID/aspirin'],
        'dosage': {
        'adult_pain': '200-400mg mỗi 4-6 giờ (tối đa 2.4g/ngày)',
        'adult_arthritis': '400-800mg x 3-4 lần/ngày (tối đa 3.2g/ngày)',
        'notes': 'Uống với thức ăn để giảm kích ứng dạ dày'},
        'side_effects': [
        'Chảy máu dạ dày', 'Suy thận', 'Tăng huyết áp', 'Phù', 'Đau đầu',
        'Ban da'],
        'interactions': [
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Aspirin: tăng nguy cơ chảy máu dạ dày',
        'Methotrexate: tăng độc tính methotrexate'],
        'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận'
        , 'monitoring': [
        'Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)'],
        'precautions': [
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể'],
        'pharmacokinetics': {'half_life': '2-4 giờ', 'onset': '30-60 phút',
        'duration': '4-6 giờ', 'protein_binding': '99%', 'metabolism':
        'Gan (chuyển hóa qua CYP2C9 và CYP2C8 thành các chất chuyển hóa hydroxyl hóa và carboxyl hóa). Chuyển hóa chủ yếu qua CYP2C9, một phần qua CYP2C8. Ibuprofen ít gây độc gan trực tiếp hơn một số NSAID khác.',
        'clearance': 'Thận (thải trừ các chất chuyển hóa, <1% bài tiết dưới dạng không đổi)'},
        'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Thận trọng, giảm liều 25-50%', 'under_30':
        'Tránh dùng hoặc giảm liều mạnh. Theo dõi chức năng thận chặt chẽ'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ'
        , 'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu',
        'effect': 'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }, {'drug': 'ACE inhibitors, ARBs', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Aspirin (liều thấp)', 'mechanism':
        'Ibuprofen có thể ức chế tác dụng chống kết tập tiểu cầu của aspirin',
        'effect': 'Giảm hiệu quả phòng ngừa nhồi máu cơ tim của aspirin',
        'management':
        'Dùng aspirin ít nhất 2 giờ trước ibuprofen, hoặc cân nhắc NSAID khác'}, {
        'drug': 'Methotrexate', 'mechanism':
        'Giảm thải trừ methotrexate qua thận', 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }],
        'moderate': [{'drug': 'Corticosteroids', 'mechanism':
        'Tăng nguy cơ loét dạ dày', 'effect': 'Tăng nguy cơ chảy máu dạ dày',
        'management': 'Cân nhắc dùng PPI hoặc misoprostol để bảo vệ dạ dày'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng ibuprofen hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'],
        'tương_đối':
        ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ']},
        'pregnancy_lactation':
        {'fda_category': 'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ibuprofen bài tiết vào sữa mẹ ở nồng độ rất thấp (<0.6% liều mẹ). Half-life ngắn (2-4 giờ) nên ít tích lũy. An toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm).'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Ibuprofen chuyển hóa ở gan qua CYP2C9 và CYP2C8. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ibuprofen ít gây độc gan trực tiếp hơn một số NSAID khác (như diclofenac).'
        },
        'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ',
        'Ức chế hô hấp (hiếm, ở liều rất cao)', 'Hạ huyết áp', 'Suy thận cấp',
        'Chảy máu dạ dày', 'Co giật (hiếm)'],
        'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim',
        'Hỗ trợ hô hấp nếu có ức chế hô hấp (hiếm)',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 4-6 giờ do half-life ngắn (2-4 giờ)'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị chảy máu dạ dày nếu có. Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        'Mỗi 4-6 giờ (do half-life ngắn). Dùng với bữa ăn để giảm tác dụng phụ dạ dày. Liều tối đa: 2.4g/ngày (đau) hoặc 3.2g/ngày (viêm khớp).'
        },
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': [],
        }},
        'pediatric_dosing': {
        'neonates': 'Không khuyến cáo cho trẻ <6 tháng tuổi',
        'infants': '10mg/kg mỗi 6-8 giờ (tối đa 40mg/kg/ngày). Dùng cho sốt và đau',
        'children': '10mg/kg mỗi 6-8 giờ (tối đa 40mg/kg/ngày). Dùng cho sốt, đau, viêm khớp. Liều tối đa: 2.4g/ngày',
        'adolescents': '200-400mg mỗi 4-6 giờ (tối đa 2.4g/ngày). Liều người lớn',
        'notes': 'Dùng cho sốt, đau, viêm khớp ở trẻ em. Uống với thức ăn để giảm kích ứng dạ dày. Theo dõi dấu hiệu chảy máu dạ dày, suy thận'
    },
        'geriatric_dosing': {
        'considerations': 'Người cao tuổi nhạy cảm hơn với tác dụng phụ (chảy máu dạ dày, suy thận). Suy thận, suy tim phổ biến hơn',
        'dose_adjustment': 'Khởi đầu với liều thấp hơn (200mg mỗi 6-8 giờ). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài',
        'monitoring': 'Theo dõi dấu hiệu chảy máu dạ dày sát hơn. Theo dõi chức năng thận (creatinine, BUN) thường xuyên. Theo dõi huyết áp'
    },
        'brand_names': {
        'vietnam': ['Brufen', 'Ibuprofen Stada', 'Ibuprofen', 'Advil', 'Nurofen'],
        'common': ['Advil', 'Motrin', 'Ibuprofen', 'Brufen', 'Nurofen']
    },
        'cost_estimate': {
        'unit': 'VND',
        'range': '3,000 - 15,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note': 'Giá thay đổi theo thương hiệu và nhà thuốc. Ibuprofen generic thường rẻ hơn (3,000-8,000 VND/viên 400mg).'
    },
        'references': {'primary_sources': [
        'FDA Drug Label - Advil, Motrin (ibuprofen)',
        'UpToDate - Ibuprofen: Drug information',
        'Lexicomp - Ibuprofen monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - FDA-approved, extensive clinical data'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': True,
            'organ_toxicity': ['GI bleeding/ulceration', 'Renal toxicity (especially with ACE inhibitors)', 'Hepatotoxicity (rare)', 'Cardiovascular events (MI, stroke)'],
        'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': True,
            'requires_monitoring': ['Signs of GI bleeding', 'Renal function (CrCl, BUN) if long-term use', 'Blood pressure', 'Signs of heart failure']
        }, 'guideline_tags': [
            'FDA Drug Safety Communication - NSAIDs and Cardiovascular Risk',
            'ACR Guidelines - NSAID Use in Arthritis',
            'FDA Black Box Warning - NSAIDs and Pregnancy (3rd trimester)',
            'ISMP High Alert Medications - NSAIDs in Elderly'
        ]},
    "Indomethacin":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Indomethacin, Indocin",
        "administration": [
            "PO",
            "IV",
            "Suppository"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Viêm cột sống dính khớp",
            "Gout cấp",
            "Đau đầu do căng thẳng",
            "Đóng ống động mạch (trẻ sơ sinh)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng indomethacin hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan trung bình - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "25-50mg x 2-3 lần/ngày (tối đa 200mg/ngày)",
            "adult_iv": "1mg/kg IV (đóng ống động mạch ở trẻ sơ sinh)",
            "adult_suppository": "50-100mg x 1-2 lần/ngày",
            "notes": "NSAID mạnh, nhiều tác dụng phụ. Dạng suppository giảm kích ứng dạ dày",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày (cao hơn các NSAID khác)",
            "Suy thận",
            "Tăng huyết áp",
            "Đau đầu (rất phổ biến)",
            "Chóng mặt",
            "Ban da",
            "Rối loạn tiêu hóa"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Digoxin: tăng nồng độ digoxin",
            "Lithium: tăng nồng độ lithium",
            "Methotrexate: tăng độc tính methotrexate"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. NSAID mạnh, hiệu quả cao nhưng nhiều tác dụng phụ. Đau đầu là tác dụng phụ rất phổ biến. Dạng suppository giảm kích ứng dạ dày.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày (nguy cơ cao)",
            "Creatinine, BUN",
            "Huyết áp",
            "Chức năng gan",
            "Dấu hiệu đau đầu (rất phổ biến)"
    ],
        "precautions": [
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Đau đầu rất phổ biến - có thể cần giảm liều hoặc ngừng",
            "Nguy cơ chảy máu dạ dày cao - cân nhắc dùng PPI",
            "Dạng suppository: giảm kích ứng dạ dày nhưng vẫn có tác dụng phụ hệ thống",
            "Tránh dùng lâu dài",
            "Không dùng trong 3 tháng cuối thai kỳ"
    ],
        "pharmacokinetics": {
            "half_life": "4-6 giờ",
            "onset": "30-60 phút (PO)",
            "duration": "4-6 giờ",
            "protein_binding": "99%",
            "metabolism": "Gan (chuyển hóa qua glucuronidation và demethylation thành các chất chuyển hóa không hoạt động). Chuyển hóa chủ yếu qua glucuronidation.",
            "clearance": "Thận (thải trừ các chất chuyển hóa, <20% bài tiết dưới dạng không đổi)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. Nguy cơ chảy máu dạ dày cao.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin",
                    "mechanism": "Ức chế COX-1",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời.",
                }
                ],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Compatible",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Tránh dùng",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau đầu nặng",
                "Chóng mặt",
                "Suy thận cấp",
                "Chảy máu dạ dày"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng indomethacin",
                "Rửa dạ dày",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Huyết áp, nhịp tim, creatinine, BUN",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (quan trọng với indomethacin do nguy cơ cao)",
                "timing": "25-50mg x 2-3 lần/ngày. Dùng với bữa ăn để giảm tác dụng phụ dạ dày và đau đầu.",
            },
            "iv": {
                "reconstitution": "Indomethacin IV: pha với NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 20-30 phút",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "Chỉ dùng cho đóng ống động mạch ở trẻ sơ sinh. Liều: 0.1-0.2mg/kg IV x 3 lần, cách nhau 12-24 giờ."
            },
            "suppository": {
                "notes": "Dạng suppository: 50-100mg x 1-2 lần/ngày. Giảm kích ứng dạ dày nhưng vẫn có tác dụng phụ hệ thống. Để trong tủ lạnh trước khi dùng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Indomethacin (Indocin)",
                "UpToDate - Indomethacin: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với indomethacin hoặc NSAID",
                "Loét dạ dày tá tràng tiến triển",
                "Suy thận nặng",
                "Suy tim nặng"
    ],
            "tương_đối": [
                "Suy thận vừa",
                "Suy gan vừa",
                "Tăng huyết áp",
                "Bệnh mạch vành"
    ],
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": ["LFT", "RFT", "GI symptoms"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ],
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. Tránh dùng trong 3 tháng cuối.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Indomethacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với liều ngắn hạn, nhưng thận trọng. Theo dõi trẻ về dấu hiệu bất thường."
            }
        },
        "pediatric_dosing": {
            "neonates": "Chỉ dùng IV cho đóng ống động mạch: 0.1-0.2mg/kg IV x 3 lần, cách nhau 12-24 giờ",
            "infants": "Không khuyến cáo cho trẻ <14 tuổi (ngoài chỉ định đóng ống động mạch)",
            "children_14_18": "25mg x 2-3 lần/ngày (tối đa 150mg/ngày). Thận trọng, theo dõi chặt chẽ",
            "notes": "Indomethacin có nhiều tác dụng phụ, đặc biệt đau đầu rất phổ biến. Chỉ dùng khi các NSAID khác không hiệu quả. Dạng suppository có thể giảm kích ứng dạ dày."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (chảy máu dạ dày, suy thận, đau đầu). Suy thận, suy tim phổ biến hơn. Đau đầu rất phổ biến với indomethacin.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (25mg x 2 lần/ngày). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài. Cân nhắc dùng dạng suppository để giảm kích ứng dạ dày.",
            "monitoring": "Theo dõi dấu hiệu chảy máu dạ dày sát hơn. Theo dõi chức năng thận (creatinine, BUN) thường xuyên. Theo dõi dấu hiệu đau đầu - rất phổ biến, có thể cần giảm liều hoặc ngừng. Theo dõi huyết áp."
        },
        "brand_names": {
            "vietnam": ["Indocin", "Indomethacin", "Indomethacin Stada"],
            "common": ["Indocin", "Indomethacin"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "5,000 - 20,000 VND/viên (tùy hàm lượng và thương hiệu). Dạng suppository: 8,000 - 25,000 VND/viên.",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Indomethacin generic thường rẻ hơn (5,000-12,000 VND/viên 25mg). Indocin (brand) đắt hơn (12,000-20,000 VND/viên 25mg)."
        }
    },
    "Ketoprofen":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Ketoprofen, Profenid",
        "administration": [
            "PO",
            "IV",
            "IM",
            "Topical"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau sau phẫu thuật",
            "Đau bụng kinh"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ketoprofen hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan trung bình - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "50-100mg x 2-3 lần/ngày (tối đa 300mg/ngày)",
            "adult_iv_im": "50-100mg IV/IM mỗi 6-8 giờ (tối đa 200mg/ngày)",
            "adult_topical": "Bôi 2-4g x 2-3 lần/ngày",
            "notes": "Có nhiều dạng: uống, tiêm, bôi tại chỗ. Dạng bôi ít tác dụng phụ hệ thống",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Ban da",
            "Nhạy cảm với ánh sáng"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Tác dụng kháng viêm và giảm đau. Có nhiều dạng: uống, tiêm, bôi tại chỗ. Dạng bôi tại chỗ có ít tác dụng phụ hệ thống hơn.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN nếu dùng lâu dài",
            "Huyết áp",
            "Chức năng gan (transaminase) nếu dùng lâu dài",
            "Dấu hiệu suy tim (giữ nước, phù)"
    ],
        "precautions": [
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Dạng bôi tại chỗ: ít tác dụng phụ hệ thống, phù hợp cho đau cục bộ",
            "Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp",
            "Không dùng trong 3 tháng cuối thai kỳ"
    ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "30-60 phút (PO), 10-15 phút (IV/IM)",
            "duration": "6-8 giờ",
            "protein_binding": "99%",
            "metabolism": "Gan (chuyển hóa qua glucuronidation và hydroxylation thành các chất chuyển hóa không hoạt động). Chuyển hóa chủ yếu qua glucuronidation.",
            "clearance": "Thận (thải trừ các chất chuyển hóa, <1% bài tiết dưới dạng không đổi)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin",
                    "mechanism": "Ức chế COX-1, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời. Theo dõi INR.",
                }
                ],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. Tránh dùng trong 3 tháng cuối.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ketoprofen bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với liều ngắn hạn. Dạng bôi tại chỗ: ít ảnh hưởng hệ thống, an toàn hơn."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Tránh dùng",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Chóng mặt",
                "Suy thận cấp",
                "Chảy máu dạ dày"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ketoprofen",
                "Rửa dạ dày",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Huyết áp, nhịp tim, creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
                "timing": "50-100mg x 2-3 lần/ngày. Dùng với bữa ăn để giảm tác dụng phụ dạ dày.",
            },
            "iv": {
                "reconstitution": "Ketoprofen IV: pha với NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 15-30 phút",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "Chỉ dùng cho đau cấp tính. Liều: 50-100mg IV mỗi 6-8 giờ (tối đa 200mg/ngày)."
            },
            "im": {
                "notes": "Tiêm bắp sâu. Liều: 50-100mg IM mỗi 6-8 giờ (tối đa 200mg/ngày). Có thể gây đau tại chỗ tiêm."
            },
            "topical": {
                "notes": "Dạng bôi tại chỗ: Bôi 2-4g x 2-3 lần/ngày lên vùng đau. Ít tác dụng phụ hệ thống hơn dạng uống. Không bôi trên vùng da bị tổn thương hoặc niêm mạc. Tránh tiếp xúc ánh nắng (nhạy cảm với ánh sáng)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ketoprofen",
                "UpToDate - Ketoprofen: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ketoprofen hoặc NSAID",
                "Loét dạ dày tá tràng tiến triển",
                "Suy thận nặng",
                "Suy tim nặng"
    ],
            "tương_đối": [
                "Suy thận vừa",
                "Suy gan vừa",
                "Tăng huyết áp",
                "Bệnh mạch vành"
    ],
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": ["LFT", "RFT", "GI symptoms"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ],
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <6 tháng tuổi",
            "infants": "Không khuyến cáo cho trẻ <6 tháng tuổi",
            "children_6m_12y": "1-2mg/kg PO x 2-3 lần/ngày (tối đa 150mg/ngày). Dùng cho sốt, đau, viêm khớp.",
            "adolescents_12_18": "50-100mg x 2-3 lần/ngày (tối đa 300mg/ngày). Liều người lớn",
            "notes": "Dùng cho sốt, đau, viêm khớp ở trẻ em. Uống với thức ăn để giảm kích ứng dạ dày. Theo dõi dấu hiệu chảy máu dạ dày, suy thận. Dạng bôi tại chỗ: an toàn hơn cho trẻ em. Tránh tiếp xúc ánh nắng (nhạy cảm với ánh sáng)."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (chảy máu dạ dày, suy thận). Suy thận, suy tim phổ biến hơn.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (50mg x 2 lần/ngày). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài. Cân nhắc dùng dạng bôi tại chỗ để giảm tác dụng phụ hệ thống.",
            "monitoring": "Theo dõi dấu hiệu chảy máu dạ dày sát hơn. Theo dõi chức năng thận (creatinine, BUN) thường xuyên. Theo dõi huyết áp. Tránh tiếp xúc ánh nắng (nhạy cảm với ánh sáng)."
        },
        "brand_names": {
            "vietnam": ["Profenid", "Ketoprofen", "Ketoprofen Stada", "Ketoprofen gel (topical)"],
            "common": ["Profenid", "Ketoprofen", "Orudis", "Oruvail"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "4,000 - 20,000 VND/viên (tùy hàm lượng và thương hiệu). Dạng bôi: 60,000 - 150,000 VND/tuýp.",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Ketoprofen generic thường rẻ hơn (4,000-10,000 VND/viên 50mg). Profenid (brand) đắt hơn (10,000-20,000 VND/viên 50mg). Dạng bôi tại chỗ: 60,000-150,000 VND/tuýp."
        }
    },
    "Ketorolac": {'group': 'Analgesic - NSAID',
        'vietnamese_name':
        'Ketorolac, Toradol', 'administration': ['PO', 'IV', 'IM'],
        'indications': [
        'Đau cấp tính vừa đến nặng (ngắn hạn)', 'Đau sau phẫu thuật',
        'Đau do chấn thương', 'Đau bụng kinh nặng'],
        'contraindications': [
        'Loét dạ dày tá tràng đang hoạt động', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai (3 tháng cuối)', 'Dị ứng NSAID/aspirin', 'Suy tim nặng',
        'Chảy máu đang hoạt động', 'Dùng lâu dài (>5 ngày)'],
        'dosage': {
        'adult_iv_im': '30mg IV/IM mỗi 6 giờ (tối đa 120mg/ngày, tối đa 5 ngày)',
        'adult_po': '10mg PO mỗi 4-6 giờ (tối đa 40mg/ngày, tối đa 5 ngày)',
        'adult_loading': '60mg IM x 1, sau đó 30mg mỗi 6 giờ', 'notes':
        'CHỈ dùng ngắn hạn (≤5 ngày). Tác dụng giảm đau mạnh, tương đương opioid nhẹ. Nguy cơ chảy máu cao hơn NSAID khác.'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều 50%', 'under_30': 'CHỐNG CHỈ ĐỊNH'},
        'side_effects': [
        'Chảy máu dạ dày (nguy cơ cao, đặc biệt khi dùng >5 ngày)',
        'Chảy máu nói chung (tăng nguy cơ)', 'Suy thận cấp (nguy cơ cao)',
        'Tăng huyết áp', 'Phù', 'Đau đầu', 'Ban da', 'Buồn nôn, nôn'],
        'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng (đặc biệt nguy hiểm)',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Methotrexate: tăng độc tính methotrexate',
        'Probenecid: tăng nồng độ ketorolac'],
        'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Ketorolac có tác dụng giảm đau mạnh, tương đương opioid nhẹ (như morphine 10mg), nhưng không gây nghiện và không ức chế hô hấp. Tuy nhiên, ketorolac có nguy cơ chảy máu và suy thận cao hơn các NSAID khác, đặc biệt khi dùng >5 ngày. CHỈ dùng ngắn hạn (≤5 ngày) cho đau cấp tính.',
        'monitoring': [
        'Dấu hiệu chảy máu (dạ dày, niêm mạc, chảy máu nói chung) - nguy cơ cao, đặc biệt khi dùng >5 ngày'
        , 'Creatinine, BUN mỗi ngày nếu dùng >2 ngày (nguy cơ suy thận cấp cao)',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)',
        'Công thức máu (CBC) nếu có dấu hiệu chảy máu'],
        'precautions': [
        'CHỈ dùng ngắn hạn (≤5 ngày) - CHỐNG CHỈ ĐỊNH dùng lâu dài',
        'Nguy cơ chảy máu cao hơn NSAID khác - tránh dùng ở bệnh nhân có nguy cơ chảy máu',
        'Nguy cơ suy thận cấp cao - tránh dùng ở bệnh nhân suy thận, mất nước',
        'Tránh dùng với warfarin (tăng nguy cơ chảy máu nặng)',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Theo dõi chức năng thận mỗi ngày nếu dùng >2 ngày',
        'IV/IM: chuyển sang PO sớm nhất có thể'],
        'pharmacokinetics': {
        'half_life': '2.5-8 giờ', 'onset': '10-30 phút (IV/IM), 30-60 phút (PO)',
        'duration': '4-6 giờ', 'protein_binding': '99%', 'metabolism':
        'Gan (chuyển hóa qua CYP2C9 và glucuronidation thành các chất chuyển hóa không hoạt động). Chuyển hóa chủ yếu qua CYP2C9, một phần qua glucuronidation.',
        'clearance': 'Thận (thải trừ các chất chuyển hóa, <10% bài tiết dưới dạng không đổi)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng IV/IM: bảo quản ở nhiệt độ phòng, không đông lạnh.',
        'black_box_warnings':
        'CHỈ dùng ngắn hạn (≤5 ngày). CHỐNG CHỈ ĐỊNH dùng lâu dài. Tăng nguy cơ chảy máu nghiêm trọng (dạ dày, niêm mạc, chảy máu nói chung), đặc biệt khi dùng >5 ngày. Tăng nguy cơ suy thận cấp, đặc biệt ở bệnh nhân suy thận, mất nước, dùng ACE inhibitor/ARB. Không dùng trong 3 tháng cuối thai kỳ.',
        'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu', 'effect':
        'Tăng nguy cơ chảy máu nặng, tăng INR (đặc biệt nguy hiểm với ketorolac)',
        'management':
        'CHỐNG CHỈ ĐỊNH dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần. Cân nhắc dùng thuốc giảm đau khác.'
        }, {'drug': 'Probenecid', 'mechanism': 'Giảm thải trừ ketorolac qua thận',
        'effect': 'Tăng nồng độ ketorolac, tăng nguy cơ tác dụng phụ', 'management':
        'Giảm liều ketorolac 50% khi dùng với probenecid. Theo dõi tác dụng phụ.'}],
        'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp (đặc biệt cao với ketorolac)',
        'management':
        'Thận trọng. Tránh dùng nếu có thể. Theo dõi creatinine, BUN mỗi ngày. Cân nhắc ngừng ketorolac nếu có dấu hiệu suy thận'
        }, {'drug': 'Methotrexate', 'mechanism': 'Giảm thải trừ methotrexate qua thận',
        'effect': 'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }],
        'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng ketorolac hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH',
        'Chảy máu đang hoạt động - CHỐNG CHỈ ĐỊNH',
        'Dùng lâu dài (>5 ngày) - CHỐNG CHỈ ĐỊNH',
        'Dùng với warfarin hoặc thuốc chống đông - CHỐNG CHỈ ĐỊNH (nguy cơ chảy máu nặng)'
        ],
        'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều 50%, theo dõi chặt chẽ',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Mất nước - tăng nguy cơ suy thận cấp',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ, đặc biệt chảy máu và suy thận',
        'Dùng >2 ngày - tăng nguy cơ chảy máu và suy thận']},
        'pregnancy_lactation': {
        'fda_category': 'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ, nhưng chỉ dùng ngắn hạn (≤5 ngày). Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.',
        'lactation': {'safety': 'Compatible with caution', 'details':
        'Ketorolac bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <0.4% liều mẹ. Tuy nhiên, do nguy cơ chảy máu và suy thận cao, nên thận trọng khi dùng khi cho con bú.',
        'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn (≤5 ngày), nhưng thận trọng. Theo dõi trẻ về dấu hiệu bất thường.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Ketorolac chuyển hóa ở gan qua CYP2C9 và glucuronidation. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ketorolac ít gây độc gan trực tiếp hơn một số NSAID khác.'},
        'overdose_management': {'symptoms': ['Chảy máu dạ dày nặng (triệu chứng chính)',
        'Chảy máu nói chung (niêm mạc, chảy máu nội tạng)', 'Suy thận cấp nặng',
        'Buồn nôn, nôn, đau bụng', 'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ',
        'Hạ huyết áp', 'Co giật (hiếm)'],
        'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Ngừng ngay ketorolac',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN) mỗi ngày - nguy cơ suy thận cấp cao',
        'Theo dõi dấu hiệu chảy máu chặt chẽ (dạ dày, niêm mạc, chảy máu nói chung)',
        'Theo dõi huyết áp, nhịp tim',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Điều trị chảy máu nếu có (truyền máu, điều trị hỗ trợ)',
        'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN (mỗi ngày), công thức máu, dấu hiệu chảy máu (dạ dày, niêm mạc, chảy máu nói chung). Theo dõi ít nhất 24-48 giờ do nguy cơ chảy máu và suy thận cao.'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị chảy máu nghiêm trọng nếu có (truyền máu, điều trị hỗ trợ). Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        'Mỗi 4-6 giờ. CHỈ dùng tối đa 5 ngày. Dùng với bữa ăn để giảm tác dụng phụ dạ dày. Liều tối đa: 40mg/ngày (PO).'
        },
        'iv': {'reconstitution':
        'Ketorolac IV: 30mg pha với 50-100ml NaCl 0.9% hoặc dextrose 5%', 'infusion_rate':
        'Truyền trong 15-30 phút', 'compatibility': ['NaCl 0.9%', 'Dextrose 5%'],
        'incompatibility': ['Không pha với các thuốc khác trong cùng đường truyền'],
        'notes':
        'CHỈ dùng tối đa 5 ngày. Chuyển sang PO sớm nhất có thể. Theo dõi chức năng thận mỗi ngày. Liều tối đa: 120mg/ngày (IV/IM).'
        },
        'im': {'notes':
        'Tiêm bắp sâu. CHỈ dùng tối đa 5 ngày. Chuyển sang PO sớm nhất có thể. Theo dõi chức năng thận mỗi ngày. Liều tối đa: 120mg/ngày (IV/IM).'
        }},
        'references': {'primary_sources': [
        'FDA Drug Label - Toradol (ketorolac)',
        'UpToDate - Ketorolac: Drug information',
        'Lexicomp - Ketorolac monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05',         'evidence_level':
        'High - FDA-approved, extensive clinical data'},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'bleeding_risk': True,
            'organ_toxicity': ['GI bleeding/ulceration', 'Renal toxicity (especially with long-term use)', 'Acute kidney injury (higher risk than other NSAIDs)'],
        'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': True,
            'requires_monitoring': ['Renal function (CrCl, BUN) - CRITICAL (max 5 days use)', 'Signs of GI bleeding', 'Blood pressure', 'Signs of acute kidney injury']
        },         'guideline_tags': [
            'FDA Drug Safety Communication - NSAIDs and Renal Risk',
            'ISMP High Alert Medications - Ketorolac',
            'FDA Black Box Warning - Ketorolac and Renal/GI Toxicity',
            'ACR Guidelines - NSAID Use in Arthritis'
        ],
        'pediatric_dosing': {
            'neonates': 'Không khuyến cáo cho trẻ <17 tuổi',
            'infants': 'Không khuyến cáo cho trẻ <17 tuổi',
            'children_17_18': 'Chưa được FDA phê duyệt cho trẻ em <17 tuổi. Không khuyến cáo sử dụng.',
            'notes': 'Ketorolac chưa được FDA phê duyệt cho trẻ em dưới 17 tuổi. CHỈ dùng ngắn hạn (≤5 ngày) cho đau cấp tính ở người lớn. Nguy cơ chảy máu và suy thận cao.'
        },
        'geriatric_dosing': {
            'considerations': 'Người cao tuổi nhạy cảm hơn với tác dụng phụ, đặc biệt là chảy máu và suy thận cấp. Suy thận, suy tim phổ biến hơn. Nguy cơ chảy máu và suy thận cao hơn với ketorolac.',
            'dose_adjustment': 'Khởi đầu với liều thấp hơn (15mg IV/IM mỗi 6 giờ hoặc 10mg PO mỗi 6 giờ). Giảm liều 50% nếu có suy thận (CrCl 30-60). CHỐNG CHỈ ĐỊNH ở CrCl <30. CHỈ dùng tối đa 5 ngày.',
            'monitoring': 'Theo dõi dấu hiệu chảy máu sát hơn (dạ dày, niêm mạc, chảy máu nói chung) - CRITICAL. Theo dõi chức năng thận (creatinine, BUN) mỗi ngày nếu dùng >2 ngày - CRITICAL. Theo dõi huyết áp.'
        },
        'brand_names': {
            'vietnam': ['Toradol', 'Ketorolac', 'Ketorolac Stada'],
            'common': ['Toradol', 'Ketorolac', 'Acular (eye drops)']
        },
        'cost_estimate': {
            'unit': 'VND',
            'range': '8,000 - 30,000 VND/viên PO (tùy hàm lượng và thương hiệu). Dạng IV/IM: 15,000 - 50,000 VND/ống.',
            'note': 'Giá thay đổi theo thương hiệu và nhà thuốc. Ketorolac generic thường rẻ hơn (8,000-15,000 VND/viên 10mg PO). Toradol (brand) đắt hơn (15,000-30,000 VND/viên 10mg PO). Dạng IV/IM: 15,000-50,000 VND/ống.'
        }},
    "Meloxicam": {'group': 'Analgesic - NSAID',
        'vietnamese_name': 'Meloxicam, Mobic',
        'administration': ['PO'],
        'indications': [
        'Đau nhẹ đến trung bình', 'Viêm khớp dạng thấp', 'Viêm khớp xương khớp', 'Đau bụng kinh'],
        'contraindications': ['Loét dạ dày tá tràng đang hoạt động',
        'Suy thận nặng', 'Suy gan nặng', 'Có thai (3 tháng cuối)',
        'Dị ứng NSAID/aspirin'],
        'dosage': {'adult_po':
        '7.5-15mg x 1 lần/ngày', 'notes':
        'COX-2 selective, ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. Uống với thức ăn'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, giảm liều', 'under_30': 'Tránh dùng'},
        'side_effects': [
        'Chảy máu dạ dày (ít hơn NSAID không chọn lọc)', 'Suy thận', 'Tăng huyết áp',
        'Phù', 'Đau đầu', 'Ban da', 'Nhạy cảm với ánh sáng'],
        'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Methotrexate: tăng độc tính methotrexate'],
        'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế chọn lọc enzyme cyclooxygenase-2 (COX-2) hơn COX-1, giảm tổng hợp prostaglandin gây viêm (từ COX-2) nhưng ít ảnh hưởng đến prostaglandin bảo vệ dạ dày (từ COX-1). Do đó, meloxicam có ít tác dụng phụ dạ dày hơn NSAID không chọn lọc (như ibuprofen, naproxen). Tác dụng kháng viêm và giảm đau. Thời gian bán thải dài (15-20 giờ) → có thể dùng 1 lần/ngày.',
        'monitoring': [
        'Dấu hiệu chảy máu dạ dày (ít hơn NSAID không chọn lọc nhưng vẫn có)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)'],
        'precautions': [
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'COX-2 selective → ít tác dụng phụ dạ dày hơn NSAID không chọn lọc, nhưng vẫn có nguy cơ',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Thời gian bán thải dài → tích lũy ở bệnh nhân suy thận, suy gan'],
        'pharmacokinetics': {
        'half_life': '15-20 giờ (dài)', 'onset': '30-60 phút', 'duration': '24 giờ',
        'protein_binding': '99%', 'metabolism':
        'Gan (chuyển hóa qua CYP2C9 và CYP3A4 thành các chất chuyển hóa hydroxyl hóa và glucuronide). Chuyển hóa chủ yếu qua CYP2C9, một phần qua CYP3A4. Thời gian bán thải dài do tích lũy.',
        'clearance': 'Thận (thải trừ các chất chuyển hóa, <0.5% bài tiết dưới dạng không đổi)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao.',
        'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu', 'effect':
        'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }, {'drug': 'ACE inhibitors, ARBs', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Methotrexate', 'mechanism': 'Giảm thải trừ methotrexate qua thận',
        'effect': 'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }],
        'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng meloxicam hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'],
        'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ']},
        'pregnancy_lactation': {
        'fda_category': 'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.',
        'lactation': {'safety': 'Compatible', 'details':
        'Meloxicam bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ. An toàn cho trẻ bú mẹ.',
        'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm).'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Meloxicam chuyển hóa ở gan qua CYP2C9 và CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, meloxicam ít gây độc gan hơn một số NSAID khác.'},
        'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ', 'Hạ huyết áp', 'Suy thận cấp',
        'Chảy máu dạ dày', 'Co giật (hiếm)'],
        'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 24-48 giờ do half-life dài (15-20 giờ)'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị chảy máu dạ dày nếu có. Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        '1 lần/ngày (do half-life dài). Có thể dùng vào buổi sáng hoặc tối. Dùng với bữa ăn để giảm tác dụng phụ dạ dày.'
        },
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': []}},
        'references': {'primary_sources': [
        'FDA Drug Label - Mobic (meloxicam)',
        'UpToDate - Meloxicam: Drug information',
        'Lexicomp - Meloxicam monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05', 'evidence_level':
        'High - FDA-approved, extensive clinical data'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['GI bleeding/ulceration (lower risk than non-selective NSAIDs)', 'Renal toxicity', 'Cardiovascular events (MI, stroke - similar to non-selective NSAIDs)', 'Sulfonamide allergy (contraindicated)'],
        'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': True,
            'requires_monitoring': ['Signs of GI bleeding', 'Renal function (CrCl, BUN)', 'Blood pressure', 'Signs of cardiovascular events']
        },         'guideline_tags': [
            'FDA Drug Safety Communication - NSAIDs and Cardiovascular Risk',
            'FDA Drug Safety Communication - COX-2 Inhibitors and Cardiovascular Risk',
            'ACR Guidelines - NSAID Use in Arthritis',
            'FDA Black Box Warning - NSAIDs and Pregnancy (3rd trimester)'
        ],
        'pediatric_dosing': {
            'neonates': 'Không khuyến cáo cho trẻ <2 tuổi',
            'infants': 'Không khuyến cáo cho trẻ <2 tuổi',
            'children_2_12': '0.125mg/kg PO x 1 lần/ngày (tối đa 7.5mg/ngày). Dùng cho viêm khớp dạng thấp thiếu niên.',
            'adolescents_12_18': '7.5-15mg x 1 lần/ngày. Liều người lớn',
            'notes': 'Dùng cho viêm khớp dạng thấp thiếu niên ở trẻ em ≥2 tuổi. Uống với thức ăn để giảm kích ứng dạ dày. Theo dõi dấu hiệu chảy máu dạ dày, suy thận. Thời gian bán thải dài → tích lũy ở trẻ em.'
        },
        'geriatric_dosing': {
            'considerations': 'Người cao tuổi nhạy cảm hơn với tác dụng phụ (chảy máu dạ dày, suy thận). Suy thận, suy tim phổ biến hơn. Thời gian bán thải dài → tích lũy ở người cao tuổi.',
            'dose_adjustment': 'Khởi đầu với liều thấp hơn (7.5mg x 1 lần/ngày). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài. Thời gian bán thải dài → tích lũy.',
            'monitoring': 'Theo dõi dấu hiệu chảy máu dạ dày sát hơn. Theo dõi chức năng thận (creatinine, BUN) thường xuyên do tích lũy. Theo dõi huyết áp.'
        },
        'brand_names': {
            'vietnam': ['Mobic', 'Meloxicam', 'Meloxicam Stada', 'Meloxicam Teva'],
            'common': ['Mobic', 'Meloxicam', 'Vivlodex']
        },
        'cost_estimate': {
            'unit': 'VND',
            'range': '5,000 - 25,000 VND/viên (tùy hàm lượng và thương hiệu)',
            'note': 'Giá thay đổi theo thương hiệu và nhà thuốc. Meloxicam generic thường rẻ hơn (5,000-12,000 VND/viên 7.5mg). Mobic (brand) đắt hơn (12,000-25,000 VND/viên 7.5mg).'
        }},
    "Naproxen": {'group': 'Analgesic - NSAID',
        'vietnamese_name': 'Naproxen, Naprosyn',
        'administration': ['PO'],
        'indications': [
        'Đau nhẹ đến trung bình', 'Viêm khớp dạng thấp', 'Viêm khớp xương khớp',
        'Viêm cột sống dính khớp', 'Đau bụng kinh', 'Đau đầu do căng thẳng',
        'Gout cấp'],
        'contraindications': [
        'Loét dạ dày tá tràng đang hoạt động', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai (3 tháng cuối)', 'Dị ứng NSAID/aspirin', 'Suy tim nặng'],
        'dosage': {'adult_pain': '250-500mg x 2 lần/ngày (tối đa 1.25g/ngày)',
        'adult_arthritis': '250-500mg x 2 lần/ngày (tối đa 1.5g/ngày)',
        'adult_dysmenorrhea':
        '500mg ngay khi có triệu chứng, sau đó 250mg mỗi 6-8 giờ', 'adult_gout':
        '750mg ngay, sau đó 250mg mỗi 8 giờ', 'notes':
        'Tác dụng kéo dài hơn ibuprofen. Uống với thức ăn'},
        'renal_adjustment':
        {'normal': 'Không đổi', '30_60': 'Thận trọng, giảm liều', 'under_30':
        'Tránh dùng'},
        'side_effects': ['Chảy máu dạ dày', 'Suy thận',
        'Tăng huyết áp', 'Phù', 'Đau đầu', 'Ban da', 'Nhạy cảm với ánh sáng'],
        'interactions': ['Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Aspirin: giảm hiệu quả naproxen', 'Lithium: tăng nồng độ lithium',
        'Methotrexate: tăng độc tính methotrexate'],
        'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận. Tác dụng kháng viêm và giảm đau mạnh hơn ibuprofen. Thời gian bán thải dài hơn ibuprofen (12-17 giờ) → tác dụng kéo dài hơn, có thể dùng 2 lần/ngày.'
        , 'monitoring': [
        'Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)', 'Lithium máu nếu dùng với lithium',
        'Nhạy cảm với ánh sáng (ban da khi tiếp xúc ánh nắng)'],
        'precautions':
        ['Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Tránh tiếp xúc ánh nắng quá nhiều (nhạy cảm với ánh sáng)',
        'Thời gian bán thải dài → tích lũy ở bệnh nhân suy thận, suy gan'],
        'pharmacokinetics': {'half_life': '12-17 giờ (dài hơn ibuprofen)',
        'onset': '30-60 phút', 'duration': '8-12 giờ', 'protein_binding': '99%',
        'metabolism': 'Gan (chuyển hóa qua CYP2C9 và CYP1A2 thành các chất chuyển hóa hydroxyl hóa và glucuronide). Chuyển hóa chủ yếu qua CYP2C9, một phần qua CYP1A2. Thời gian bán thải dài do tích lũy.',
        'clearance': 'Thận (thải trừ các chất chuyển hóa, <5% bài tiết dưới dạng không đổi)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp',
        'black_box_warnings':
        'Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao.'
        , 'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu',
        'effect': 'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }, {'drug': 'ACE inhibitors, ARBs', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Aspirin (liều thấp)', 'mechanism':
        'Naproxen có thể ức chế tác dụng chống kết tập tiểu cầu của aspirin',
        'effect': 'Giảm hiệu quả phòng ngừa nhồi máu cơ tim của aspirin',
        'management':
        'Dùng aspirin ít nhất 2 giờ trước naproxen, hoặc cân nhắc NSAID khác'},
        {'drug': 'Lithium', 'mechanism': 'Giảm thải trừ lithium qua thận',
        'effect': 'Tăng nồng độ lithium, tăng nguy cơ độc tính', 'management':
        'Theo dõi lithium máu thường xuyên. Có thể cần giảm liều lithium'}, {
        'drug': 'Methotrexate', 'mechanism':
        'Giảm thải trừ methotrexate qua thận', 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }],
        'moderate': [{'drug': 'Corticosteroids', 'mechanism':
        'Tăng nguy cơ loét dạ dày', 'effect': 'Tăng nguy cơ chảy máu dạ dày',
        'management': 'Cân nhắc dùng PPI hoặc misoprostol để bảo vệ dạ dày'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng naproxen hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'],
        'tương_đối':
        ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ']},
        'pregnancy_lactation':
        {'fda_category': 'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Naproxen bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ. Half-life dài (12-17 giờ) nhưng nồng độ trong sữa mẹ thấp nên ít ảnh hưởng đến trẻ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm).'
        }},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Naproxen chuyển hóa ở gan qua CYP2C9 và CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, naproxen ít gây độc gan hơn một số NSAID khác (như diclofenac).'
        },
        'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ',
        'Ức chế hô hấp (hiếm, ở liều rất cao)', 'Hạ huyết áp', 'Suy thận cấp',
        'Chảy máu dạ dày', 'Co giật (hiếm)'],
        'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim',
        'Hỗ trợ hô hấp nếu có ức chế hô hấp (hiếm)',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 12-24 giờ do half-life dài (12-17 giờ)'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị chảy máu dạ dày nếu có. Bù nước và điện giải nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        'Mỗi 8-12 giờ (do half-life dài). Có thể dùng 2 lần/ngày. Dùng với bữa ăn để giảm tác dụng phụ dạ dày.'
        },
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': [],
        }},
        'references': {'primary_sources': [
        'FDA Drug Label - Naprosyn (naproxen)',
        'UpToDate - Naproxen: Drug information',
        'Lexicomp - Naproxen monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-06', 'evidence_level':
        'High - FDA-approved, extensive clinical data'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': True,
            'organ_toxicity': ['GI bleeding/ulceration', 'Renal toxicity', 'Hepatotoxicity (higher risk than other NSAIDs)', 'Cardiovascular events (MI, stroke)'],
        'qt_prolongation': False,
            'hepatotoxicity': True,
            'nephrotoxicity': True,
            'requires_monitoring': ['Signs of GI bleeding', 'Hepatic function (ALT, AST) - CRITICAL', 'Renal function (CrCl, BUN)', 'Blood pressure']
        },         'guideline_tags': [
            'FDA Drug Safety Communication - NSAIDs and Cardiovascular Risk',
            'FDA Drug Safety Communication - Diclofenac and Hepatotoxicity',
            'ACR Guidelines - NSAID Use in Arthritis',
            'FDA Black Box Warning - NSAIDs and Pregnancy (3rd trimester)'
        ],
        'pediatric_dosing': {
            'neonates': 'Không khuyến cáo cho trẻ <2 tuổi',
            'infants': 'Không khuyến cáo cho trẻ <2 tuổi',
            'children_2_12': '5-7mg/kg PO x 2 lần/ngày (tối đa 1g/ngày). Dùng cho sốt, đau, viêm khớp dạng thấp thiếu niên.',
            'adolescents_12_18': '250-500mg x 2 lần/ngày (tối đa 1.25-1.5g/ngày). Liều người lớn',
            'notes': 'Dùng cho sốt, đau, viêm khớp dạng thấp thiếu niên ở trẻ em ≥2 tuổi. Uống với thức ăn để giảm kích ứng dạ dày. Theo dõi dấu hiệu chảy máu dạ dày, suy thận. Thời gian bán thải dài → tích lũy ở trẻ em. Tránh tiếp xúc ánh nắng (nhạy cảm với ánh sáng).'
        },
        'geriatric_dosing': {
            'considerations': 'Người cao tuổi nhạy cảm hơn với tác dụng phụ (chảy máu dạ dày, suy thận). Suy thận, suy tim phổ biến hơn. Thời gian bán thải dài → tích lũy ở người cao tuổi.',
            'dose_adjustment': 'Khởi đầu với liều thấp hơn (250mg x 2 lần/ngày). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài. Thời gian bán thải dài → tích lũy.',
            'monitoring': 'Theo dõi dấu hiệu chảy máu dạ dày sát hơn. Theo dõi chức năng thận (creatinine, BUN) thường xuyên do tích lũy. Theo dõi chức năng gan (ALT, AST) - QUAN TRỌNG với naproxen. Theo dõi huyết áp. Tránh tiếp xúc ánh nắng (nhạy cảm với ánh sáng).'
        },
        'brand_names': {
            'vietnam': ['Naprosyn', 'Naproxen', 'Naproxen Stada', 'Naproxen Teva', 'Aleve'],
            'common': ['Naprosyn', 'Aleve', 'Naproxen', 'Anaprox']
        },
        'cost_estimate': {
            'unit': 'VND',
            'range': '4,000 - 20,000 VND/viên (tùy hàm lượng và thương hiệu)',
            'note': 'Giá thay đổi theo thương hiệu và nhà thuốc. Naproxen generic thường rẻ hơn (4,000-10,000 VND/viên 250mg). Naprosyn (brand) đắt hơn (10,000-20,000 VND/viên 250mg).'
        }},
    "Nimesulide":     {
        "group": "Analgesic - NSAID (COX-2 Preferential)",
        "vietnamese_name": "Nimesulide, Nise, Aulin",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp",
            "Đau bụng kinh",
            "Gout cấp"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nimesulide hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Trẻ em <12 tuổi"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng, theo dõi chặt chẽ"
    ],
        },
        "dosage": {
            "adult_po": "100mg x 2 lần/ngày (tối đa 200mg/ngày)",
            "notes": """COX-2 preferential, ít tác dụng phụ dạ dày. Nguy cơ độc gan. Không phải tất cả quốc gia đều phê duyệt.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Độc gan (nguy cơ cao, có thể nặng)",
            "Chảy máu dạ dày (ít hơn NSAID không chọn lọc)",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Ban da"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế ưu tiên enzyme cyclooxygenase-2 (COX-2) hơn COX-1, giảm tổng hợp prostaglandin gây viêm. Ít tác dụng phụ dạ dày hơn NSAID không chọn lọc nhưng có nguy cơ độc gan cao. Không phải tất cả quốc gia đều phê duyệt (một số quốc gia đã rút khỏi thị trường do nguy cơ độc gan).""",
        "monitoring": [
            "Chức năng gan (ALT, AST) thường xuyên - QUAN TRỌNG (nguy cơ độc gan)",
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp"
    ],
        "precautions": [
            "NGUY CƠ ĐỘC GAN CAO - theo dõi ALT/AST thường xuyên, ngừng ngay nếu tăng",
            "Không phải tất cả quốc gia đều phê duyệt",
            "COX-2 preferential → ít tác dụng phụ dạ dày nhưng vẫn có nguy cơ",
            "Uống với thức ăn",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi"
    ],
        "pharmacokinetics": {
            "half_life": "2-5 giờ",
            "onset": "30-60 phút",
            "duration": "6-8 giờ",
            "protein_binding": "99%",
            "metabolism": "Gan (chuyển hóa qua CYP2C9 và CYP1A2 thành các chất chuyển hóa hydroxyl hóa và nitro-reduction). Chuyển hóa chủ yếu qua CYP2C9. NGUY CƠ ĐỘC GAN CAO do chuyển hóa qua gan.",
            "clearance": "Thận (thải trừ các chất chuyển hóa, <1% bài tiết dưới dạng không đổi)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """NGUY CƠ ĐỘC GAN CAO, có thể nặng. Theo dõi ALT/AST thường xuyên. Ngừng ngay nếu có dấu hiệu độc gan. Một số quốc gia đã rút khỏi thị trường do nguy cơ độc gan. Không dùng trong 3 tháng cuối thai kỳ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin",
                    "mechanism": "Ức chế COX",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời.",
                }
                ],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ, nhưng thận trọng do nguy cơ độc gan. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. Tránh dùng trong 3 tháng cuối.",
            "lactation": {
                "safety": "Caution",
                "details": "Nimesulide bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, do nguy cơ độc gan cao, nên thận trọng khi dùng khi cho con bú.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Theo dõi trẻ về dấu hiệu bất thường. Cân nhắc NSAID khác an toàn hơn."
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi ALT/AST",
            "moderate": "CHỐNG CHỈ ĐỊNH",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "NGUY CƠ ĐỘC GAN CAO. CHỐNG CHỈ ĐỊNH ở suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Độc gan (vàng da, tăng ALT/AST)",
                "Buồn nôn, nôn",
                "Suy thận cấp",
                "Chảy máu dạ dày"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng nimesulide ngay",
                "Theo dõi chức năng gan chặt chẽ",
                "Điều trị độc gan nếu có",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "ALT/AST, bilirubin, creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
                "timing": "100mg x 2 lần/ngày. Dùng với bữa ăn để giảm tác dụng phụ dạ dày. Liều tối đa: 200mg/ngày.",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nimesulide",
                "UpToDate - Nimesulide: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate - Not FDA-approved in US, approved in some countries",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": ["LFT", "RFT", "GI symptoms"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
                "Hepatotoxicity Warning - Some countries have withdrawn from market"
            ],
        "pediatric_dosing": {
            "neonates": "CHỐNG CHỈ ĐỊNH cho trẻ <12 tuổi",
            "infants": "CHỐNG CHỈ ĐỊNH cho trẻ <12 tuổi",
            "children_12_18": "100mg x 2 lần/ngày (tối đa 200mg/ngày). Liều người lớn. Thận trọng, theo dõi chức năng gan chặt chẽ.",
            "notes": "CHỐNG CHỈ ĐỊNH ở trẻ em <12 tuổi. Chỉ dùng cho trẻ ≥12 tuổi với liều người lớn. Theo dõi chức năng gan chặt chẽ do nguy cơ độc gan cao."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ, đặc biệt là độc gan. Suy thận, suy gan phổ biến hơn. NGUY CƠ ĐỘC GAN CAO.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (100mg x 1 lần/ngày). Giảm liều nếu có suy thận (CrCl <60). CHỐNG CHỈ ĐỊNH ở suy gan. Theo dõi chức năng gan chặt chẽ.",
            "monitoring": "Theo dõi chức năng gan (ALT, AST) thường xuyên - CRITICAL do nguy cơ độc gan cao. Theo dõi dấu hiệu chảy máu dạ dày. Theo dõi chức năng thận (creatinine, BUN) thường xuyên. Theo dõi huyết áp."
        },
        "brand_names": {
            "vietnam": ["Nise", "Nimesulide", "Nimesulide Stada", "Aulin"],
            "common": ["Nise", "Aulin", "Nimesulide", "Mesulid"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "5,000 - 25,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Nimesulide generic thường rẻ hơn (5,000-12,000 VND/viên 100mg). Nise (brand) đắt hơn (12,000-25,000 VND/viên 100mg). Lưu ý: Một số quốc gia đã rút khỏi thị trường do nguy cơ độc gan."
        }
    },
    "Piroxicam":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Piroxicam, Feldene",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau cơ xương",
            "Gout cấp"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng piroxicam hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ"
    ],
        },
        "dosage": {
            "adult_po": "20mg x 1 lần/ngày (tối đa 20mg/ngày)",
            "notes": """NSAID tác dụng kéo dài, dùng 1 lần/ngày. T1/2 dài (30-50 giờ) nên tích lũy có thể xảy ra. Nguy cơ chảy máu dạ dày cao hơn một số NSAID khác.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày (nguy cơ cao)",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da",
            "Tích lũy do T1/2 dài"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate",
            "Lithium: tăng nồng độ lithium",
            "Diuretics: giảm hiệu quả lợi tiểu"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Piroxicam có thời gian bán hủy dài (30-50 giờ) nên dùng 1 lần/ngày, nhưng có nguy cơ tích lũy và tác dụng phụ kéo dài. Tác dụng kháng viêm và giảm đau.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng) - nguy cơ cao",
            "Creatinine, BUN (đặc biệt ở người cao tuổi và suy thận)",
            "Huyết áp (NSAID có thể tăng huyết áp)",
            "Dấu hiệu tích lũy do T1/2 dài"
    ],
        "precautions": [
            "T1/2 dài (30-50 giờ) → nguy cơ tích lũy, đặc biệt ở người cao tuổi và suy thận",
            "Nguy cơ chảy máu dạ dày cao hơn một số NSAID khác",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Thận trọng ở người cao tuổi (tăng nguy cơ tác dụng phụ)",
            "Theo dõi chức năng thận thường xuyên"
    ],
        "pharmacokinetics": {
            "half_life": "30-50 giờ (rất dài)",
            "onset": "30-60 phút",
            "duration": "24 giờ (do T1/2 dài)",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ. Nguy cơ chảy máu dạ dày cao. T1/2 dài → nguy cơ tích lũy.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Giảm thải trừ methotrexate qua thận",
                    "effect": "Tăng độc tính methotrexate",
                    "management": "Tránh dùng đồng thời.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Giảm thải trừ lithium",
                    "effect": "Tăng nồng độ lithium",
                    "management": "Theo dõi nồng độ lithium, điều chỉnh liều.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp",
                "Co giật (hiếm)"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng piroxicam ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận",
                "Điều trị chảy máu dạ dày nếu có"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu, điện giải",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "20mg x 1 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Piroxicam",
                "UpToDate - Piroxicam: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Mefenamic acid":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Mefenamic acid, Ponstan",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Đau bụng kinh",
            "Đau đầu",
            "Đau răng",
            "Đau cơ xương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng mefenamic acid hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng",
                "Viêm ruột (Crohn, viêm loét đại tràng)"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng",
                "Hen phế quản - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "500mg x 3 lần/ngày (tối đa 1500mg/ngày)",
            "notes": """NSAID anthranilic acid derivative. Hiệu quả tốt cho đau bụng kinh. Không dùng quá 7 ngày liên tiếp. Nguy cơ chảy máu dạ dày và độc tính thần kinh trung ương.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Đau đầu",
            "Chóng mặt",
            "Co giật (hiếm nhưng nghiêm trọng)",
            "Suy thận",
            "Ban da"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate",
            "Probenecid: tăng nồng độ mefenamic acid"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Mefenamic acid là anthranilic acid derivative, có hiệu quả tốt trong điều trị đau bụng kinh. Có nguy cơ độc tính thần kinh trung ương (co giật) khi dùng liều cao hoặc kéo dài.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Dấu hiệu độc tính thần kinh trung ương (co giật, lú lẫn)",
            "Creatinine, BUN",
            "Triệu chứng tiêu hóa"
    ],
        "precautions": [
            "KHÔNG dùng quá 7 ngày liên tiếp",
            "Nguy cơ co giật khi dùng liều cao hoặc kéo dài",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Thận trọng ở bệnh nhân có tiền sử co giật",
            "Ngừng ngay nếu có dấu hiệu độc tính thần kinh trung ương"
    ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "30-60 phút",
            "duration": "4-6 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ. Nguy cơ co giật khi dùng liều cao hoặc kéo dài. Không dùng quá 7 ngày liên tiếp. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Giảm thải trừ mefenamic acid",
                    "effect": "Tăng nồng độ mefenamic acid",
                    "management": "Giảm liều mefenamic acid.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Co giật",
                "Lú lẫn",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng mefenamic acid ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị co giật nếu có",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu, dấu hiệu thần kinh",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "500mg x 3 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mefenamic acid",
                "UpToDate - Mefenamic acid: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "CNS symptoms"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Aceclofenac":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Aceclofenac, Airtal",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau cơ xương",
            "Đau lưng"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng aceclofenac hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng",
                "Bệnh tim mạch - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "100mg x 2 lần/ngày (tối đa 200mg/ngày)",
            "notes": """NSAID acetic acid derivative, tương tự diclofenac. Ít tác dụng phụ dạ dày hơn diclofenac. Hiệu quả tốt trong viêm khớp.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày (ít hơn diclofenac)",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da",
            "Tăng men gan"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate",
            "Lithium: tăng nồng độ lithium"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Aceclofenac là acetic acid derivative, tương tự diclofenac nhưng có ít tác dụng phụ dạ dày hơn. Chuyển hóa thành diclofenac và các chất chuyển hóa khác. Tác dụng kháng viêm và giảm đau.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp",
            "Chức năng gan (ALT, AST)"
    ],
        "precautions": [
            "Ít tác dụng phụ dạ dày hơn diclofenac nhưng vẫn có nguy cơ",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi chức năng gan và thận"
    ],
        "pharmacokinetics": {
            "half_life": "4 giờ",
            "onset": "30-60 phút",
            "duration": "8-12 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa thành diclofenac), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng aceclofenac ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "100mg x 2 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aceclofenac",
                "UpToDate - Aceclofenac: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP", "LFT"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Flurbiprofen":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Flurbiprofen, Ansaid",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau cơ xương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng flurbiprofen hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "100mg x 2-3 lần/ngày (tối đa 300mg/ngày)",
            "notes": """NSAID propionic acid derivative, tương tự ibuprofen. Hiệu quả tốt trong viêm khớp.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate",
            "Lithium: tăng nồng độ lithium"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Flurbiprofen là propionic acid derivative, tương tự ibuprofen. Tác dụng kháng viêm và giảm đau.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp"
    ],
        "precautions": [
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi chức năng thận"
    ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ",
            "onset": "30-60 phút",
            "duration": "6-8 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng flurbiprofen ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "100mg x 2-3 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Flurbiprofen",
                "UpToDate - Flurbiprofen: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Sulindac":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Sulindac, Clinoril",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau cơ xương",
            "Gout cấp"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng sulindac hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "150-200mg x 2 lần/ngày (tối đa 400mg/ngày)",
            "notes": """NSAID indole acetic acid derivative. Sulindac là prodrug, chuyển hóa thành sulfide hoạt tính. Ít ảnh hưởng đến chức năng thận hơn một số NSAID khác.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận (ít hơn một số NSAID khác)",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da",
            "Tăng men gan"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate",
            "Cyclosporine: tăng độc tính thận"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Sulindac là prodrug, chuyển hóa thành sulfide hoạt tính. Sulfide ức chế enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Sulindac ít ảnh hưởng đến chức năng thận hơn một số NSAID khác do cơ chế chuyển hóa đặc biệt. Tác dụng kháng viêm và giảm đau.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp",
            "Chức năng gan"
    ],
        "precautions": [
            "Ít ảnh hưởng đến thận hơn một số NSAID khác nhưng vẫn có nguy cơ",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi chức năng thận và gan"
    ],
        "pharmacokinetics": {
            "half_life": "7-8 giờ (sulfide hoạt tính)",
            "onset": "30-60 phút",
            "duration": "12 giờ",
            "protein_binding": "93-98%",
            "clearance": "Gan (chuyển hóa thành sulfide), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                },
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Tăng độc tính thận",
                    "effect": "Tăng nguy cơ suy thận",
                    "management": "Tránh dùng đồng thời hoặc theo dõi chức năng thận chặt chẽ.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng sulindac ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "150-200mg x 2 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sulindac",
                "UpToDate - Sulindac: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP", "LFT"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Nabumetone":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Nabumetone, Relafen",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau cơ xương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nabumetone hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "1000-2000mg/ngày (một liều hoặc chia liều: 500-1000mg x 2 lần/ngày)",
            "notes": """NSAID naphthylalkanone derivative. Nabumetone là prodrug, chuyển hóa thành 6-MNA hoạt tính. Ít tác dụng phụ dạ dày hơn một số NSAID khác. Có thể dùng một liều hoặc chia liều.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày (ít hơn một số NSAID khác)",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Nabumetone là prodrug, chuyển hóa thành 6-MNA (6-methoxy-2-naphthylacetic acid) hoạt tính. 6-MNA ức chế enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Nabumetone có ít tác dụng phụ dạ dày hơn một số NSAID khác do cơ chế chuyển hóa đặc biệt. Tác dụng kháng viêm và giảm đau.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp"
    ],
        "precautions": [
            "Ít tác dụng phụ dạ dày hơn một số NSAID khác nhưng vẫn có nguy cơ",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi chức năng thận"
    ],
        "pharmacokinetics": {
            "half_life": "22-30 giờ (6-MNA hoạt tính)",
            "onset": "30-60 phút",
            "duration": "24 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa thành 6-MNA), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng nabumetone ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "1000-2000mg/ngày (một liều hoặc chia liều)",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nabumetone",
                "UpToDate - Nabumetone: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Oxaprozin":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Oxaprozin, Daypro",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau cơ xương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng oxaprozin hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "1200mg x 1 lần/ngày (tối đa 1800mg/ngày)",
            "notes": """NSAID propionic acid derivative. T1/2 dài nên dùng 1 lần/ngày. Hiệu quả tốt trong viêm khớp.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate",
            "Lithium: tăng nồng độ lithium"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Oxaprozin là propionic acid derivative, có thời gian bán hủy dài nên dùng 1 lần/ngày. Tác dụng kháng viêm và giảm đau.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp"
    ],
        "precautions": [
            "T1/2 dài → nguy cơ tích lũy ở người cao tuổi và suy thận",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi chức năng thận"
    ],
        "pharmacokinetics": {
            "half_life": "40-60 giờ (rất dài)",
            "onset": "30-60 phút",
            "duration": "24 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ. T1/2 dài → nguy cơ tích lũy.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng oxaprozin ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "1200mg x 1 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Oxaprozin",
                "UpToDate - Oxaprozin: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Tolmetin":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Tolmetin, Tolectin",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau cơ xương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tolmetin hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "400mg x 3 lần/ngày (tối đa 1800mg/ngày)",
            "notes": """NSAID acetic acid derivative. Hiệu quả tốt trong viêm khớp dạng thấp.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Tolmetin là acetic acid derivative. Tác dụng kháng viêm và giảm đau. Hiệu quả tốt trong viêm khớp dạng thấp.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp"
    ],
        "precautions": [
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi chức năng thận"
    ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ",
            "onset": "30-60 phút",
            "duration": "6-8 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng tolmetin ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "400mg x 3 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tolmetin",
                "UpToDate - Tolmetin: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Dexketoprofen":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Dexketoprofen, Enantyum",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Đau cấp tính",
            "Đau sau phẫu thuật",
            "Đau bụng kinh",
            "Đau răng"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dexketoprofen hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "12.5-25mg x 2-3 lần/ngày (tối đa 75mg/ngày)",
            "notes": """Dexketoprofen là enantiomer hoạt tính của ketoprofen. Tác dụng nhanh, hiệu quả tốt cho đau cấp tính. Liều thấp hơn ketoprofen do hoạt tính cao hơn.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Dexketoprofen là enantiomer hoạt tính (S-enantiomer) của ketoprofen. Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Do chỉ chứa enantiomer hoạt tính nên liều thấp hơn ketoprofen nhưng hiệu quả tương đương. Tác dụng nhanh, hiệu quả tốt cho đau cấp tính. Tác dụng kháng viêm và giảm đau.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp"
    ],
        "precautions": [
            "Tác dụng nhanh, phù hợp cho đau cấp tính",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi chức năng thận"
    ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ",
            "onset": "15-30 phút (nhanh)",
            "duration": "4-6 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng dexketoprofen ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "12.5-25mg x 2-3 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dexketoprofen",
                "UpToDate - Dexketoprofen: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Tenoxicam":     {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Tenoxicam, Mobiflex",
        "administration": [
            "PO",
            "IM"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau cơ xương",
            "Gout cấp"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tenoxicam hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan nhẹ - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "20mg x 1 lần/ngày (tối đa 20mg/ngày)",
            "adult_im": "20mg x 1 lần/ngày",
            "notes": """NSAID oxicam derivative, tương tự piroxicam. T1/2 dài nên dùng 1 lần/ngày. Có dạng tiêm bắp.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Chóng mặt",
            "Ban da"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Methotrexate: tăng độc tính methotrexate"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Tenoxicam là oxicam derivative, tương tự piroxicam, có thời gian bán hủy dài nên dùng 1 lần/ngày. Có dạng tiêm bắp. Tác dụng kháng viêm và giảm đau.""",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày",
            "Creatinine, BUN",
            "Huyết áp"
    ],
        "precautions": [
            "T1/2 dài → nguy cơ tích lũy",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi chức năng thận"
    ],
        "pharmacokinetics": {
            "half_life": "60-75 giờ (rất dài)",
            "onset": "30-60 phút",
            "duration": "24 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ. T1/2 rất dài → nguy cơ tích lũy.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX, chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chảy máu dạ dày",
                "Suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng tenoxicam ngay",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Creatinine, BUN, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn",
                "timing": "20mg x 1 lần/ngày",
            },
            "iv": {"reconstitution": "Không có dạng IV", "infusion_rate": "N/A",
            "compatibility": [],
            "incompatibility": []}
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tenoxicam",
                "UpToDate - Tenoxicam: Drug information",
                "MSD Manual - NSAIDs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["RFT", "GI symptoms", "BP"],
            },
            "guideline_tags": [
                "ACR 2021 Osteoarthritis Guidelines",
                "FDA Black Box Warning - Cardiovascular and GI risks",
            ]
    },
    "Parecoxib": {
        "group": "Analgesic - NSAID (COX-2 Selective, Injectable)",
        "vietnamese_name": "Parecoxib, Dynastat",
        "administration": ["IV", "IM"],
        "indications": [
            "Giảm đau sau phẫu thuật (postoperative pain)",
            "Đau cấp tính (acute pain)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng parecoxib hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy thận nặng (CrCl <30)",
                "Suy gan nặng",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Bệnh tim mạch nặng"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng",
                "Suy gan trung bình - thận trọng",
                "Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch"
            ]
        },
        "dosage": {
            "adult_postop": "40mg IV/IM, sau đó 20-40mg mỗi 6-12 giờ (tối đa 80mg/ngày)",
            "adult_max": "80mg/ngày",
            "adult_duration": "Tối đa 3 ngày",
            "notes": "COX-2 selective, dạng tiêm. Dùng trong phẫu thuật để giảm đau sau mổ. Không dùng quá 3 ngày. Chuyển sang thuốc uống nếu cần điều trị lâu hơn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 50%",
            "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30)"
        },
        "side_effects": [
            "Tăng nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ)",
            "Tăng huyết áp",
            "Phù",
            "Suy thận",
            "Chóng mặt",
            "Đau đầu",
            "Buồn nôn",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng)",
            "Ít tác dụng phụ dạ dày hơn NSAID không chọn lọc"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium",
            "Methotrexate: tăng độc tính methotrexate"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Parecoxib là prodrug của valdecoxib (COX-2 selective inhibitor). Parecoxib được chuyển hóa nhanh thành valdecoxib trong cơ thể. Valdecoxib ức chế chọn lọc enzyme cyclooxygenase-2 (COX-2), giảm tổng hợp prostaglandin gây viêm và đau. Ít ức chế COX-1 (enzyme bảo vệ niêm mạc dạ dày) nên ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. Tuy nhiên, vẫn có nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ) tương tự các COX-2 selective khác. Dạng tiêm, dùng trong phẫu thuật để giảm đau sau mổ.",
        "monitoring": [
            "Dấu hiệu biến cố tim mạch (đau ngực, khó thở, yếu một bên)",
            "Huyết áp (NSAID có thể tăng huyết áp)",
            "Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ",
            "Dấu hiệu suy tim (giữ nước, phù)",
            "INR nếu dùng với warfarin",
            "Phản ứng tại chỗ tiêm"
        ],
        "precautions": [
            "Tăng nguy cơ biến cố tim mạch - không dùng ở bệnh nhân có bệnh tim mạch nặng",
            "Không dùng quá 3 ngày - chuyển sang thuốc uống nếu cần điều trị lâu hơn",
            "Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp",
            "Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi INR nếu dùng với warfarin",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể"
        ],
        "pharmacokinetics": {
            "half_life": "8-11 giờ (valdecoxib sau chuyển hóa)",
            "onset": "7-13 phút (nhanh)",
            "duration": "6-12 giờ",
            "protein_binding": "98%",
            "metabolism": "Parecoxib được chuyển hóa nhanh thành valdecoxib (active metabolite) qua enzyme hydrolase. Valdecoxib chuyển hóa qua gan (CYP3A4, CYP2C9) thành các chất chuyển hóa hydroxyl hóa và glucuronide.",
            "clearance": "Thận (thải trừ các chất chuyển hóa, <5% bài tiết dưới dạng không đổi)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C), dùng trong 24 giờ.",
        "black_box_warnings": "Tăng nguy cơ biến cố tim mạch nghiêm trọng (nhồi máu cơ tim, đột quỵ) - có thể tử vong. Nguy cơ tăng ở bệnh nhân có bệnh tim mạch. Không dùng trong 3 tháng cuối thai kỳ. Không dùng quá 3 ngày.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX-2, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần"
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng parecoxib nếu có dấu hiệu suy thận"
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "Giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng độc tính",
                    "management": "Theo dõi nồng độ lithium. Có thể cần giảm liều lithium."
                }
            ],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "CHỐNG CHỈ ĐỊNH (bệnh gan nặng)",
            "notes": "Parecoxib chuyển hóa thành valdecoxib, sau đó chuyển hóa ở gan qua CYP3A4, CYP2C9. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Chóng mặt, nhức đầu",
                "Lú lẫn, buồn ngủ",
                "Hạ huyết áp",
                "Suy thận cấp",
                "Tăng nguy cơ biến cố tim mạch"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng parecoxib ngay",
                "Theo dõi chức năng thận (creatinine, BUN), điện giải",
                "Theo dõi huyết áp, nhịp tim",
                "Truyền dịch nếu hạ huyết áp, suy thận",
                "Theo dõi dấu hiệu biến cố tim mạch",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu biến cố tim mạch. Theo dõi ít nhất 24 giờ do half-life dài (8-11 giờ)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay."
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong 2ml NaCl 0.9% hoặc nước cất",
                "injection_rate": "Tiêm tĩnh mạch chậm (trong ít nhất 15 giây)",
                "notes": "Tiêm tĩnh mạch chậm. Có thể tiêm bắp nếu cần. Không dùng quá 3 ngày."
            },
            "im": {
                "injection_site": "Vùng cơ lớn (mông, đùi)",
                "notes": "Tiêm bắp sâu. Có thể tiêm tĩnh mạch nếu cần. Không dùng quá 3 ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Parecoxib (Dynastat)",
                "UpToDate - Parecoxib: Drug information"
            ],
            "evidence_level": "High - FDA approved"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": True,
            "organ_toxicity": ["GI", "renal", "cardiac"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["LFT", "RFT", "GI symptoms", "Blood pressure", "Cardiovascular symptoms"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cardiovascular and GI risks",
            "ISMP High Alert Medications - NSAIDs"
        ]
    },
    "Valdecoxib": {
        "group": "Analgesic - NSAID (COX-2 Selective)",
        "vietnamese_name": "Valdecoxib, Bextra",
        "administration": ["PO"],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp",
            "Đau bụng kinh"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng valdecoxib hoặc NSAID/aspirin",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy thận nặng",
                "Suy gan nặng",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Bệnh tim mạch nặng"
            ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan trung bình - thận trọng",
                "Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch"
            ]
        },
        "dosage": {
            "adult_pain": "10-20mg x 1-2 lần/ngày",
            "adult_arthritis": "10mg x 1-2 lần/ngày",
            "adult_max": "40mg/ngày",
            "notes": "COX-2 selective, ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. LƯU Ý: Đã ngưng dùng ở nhiều nơi (bao gồm Mỹ) do lo ngại về an toàn tim mạch và phản ứng da nghiêm trọng (Stevens-Johnson syndrome, toxic epidermal necrolysis)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 25-50%",
            "under_30": "Tránh dùng hoặc giảm liều mạnh. Theo dõi chức năng thận chặt chẽ"
        },
        "side_effects": [
            "Tăng nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ) - NGUY HIỂM",
            "Phản ứng da nghiêm trọng (Stevens-Johnson syndrome, toxic epidermal necrolysis) - NGUY HIỂM, có thể tử vong",
            "Tăng huyết áp",
            "Phù",
            "Suy thận",
            "Chóng mặt",
            "Đau đầu",
            "Buồn nôn",
            "Ít tác dụng phụ dạ dày hơn NSAID không chọn lọc"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium",
            "Methotrexate: tăng độc tính methotrexate"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Valdecoxib ức chế chọn lọc enzyme cyclooxygenase-2 (COX-2), giảm tổng hợp prostaglandin gây viêm và đau. Ít ức chế COX-1 (enzyme bảo vệ niêm mạc dạ dày) nên ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. Tuy nhiên, có nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ) và phản ứng da nghiêm trọng (Stevens-Johnson syndrome, toxic epidermal necrolysis) cao hơn các COX-2 selective khác. LƯU Ý: Đã ngưng dùng ở nhiều nơi (bao gồm Mỹ) do lo ngại về an toàn.",
        "monitoring": [
            "Dấu hiệu biến cố tim mạch (đau ngực, khó thở, yếu một bên) - QUAN TRỌNG",
            "Phản ứng da nghiêm trọng (ban da, mụn nước, bong da) - QUAN TRỌNG, ngừng ngay nếu có",
            "Huyết áp (NSAID có thể tăng huyết áp)",
            "Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ",
            "Dấu hiệu suy tim (giữ nước, phù)",
            "INR nếu dùng với warfarin"
        ],
        "precautions": [
            "NGUY CƠ BIẾN CỐ TIM MẠCH NGHIÊM TRỌNG - không dùng ở bệnh nhân có bệnh tim mạch nặng",
            "NGUY CƠ PHẢN ỨNG DA NGHIÊM TRỌNG - ngừng ngay nếu có ban da, mụn nước, bong da",
            "ĐÃ NGƯNG DÙNG Ở NHIỀU NƠI - cân nhắc thuốc thay thế an toàn hơn",
            "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
            "Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp",
            "Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Theo dõi INR nếu dùng với warfarin",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể"
        ],
        "pharmacokinetics": {
            "half_life": "8-11 giờ",
            "onset": "30-60 phút",
            "duration": "12-24 giờ",
            "protein_binding": "98%",
            "metabolism": "Gan (chuyển hóa qua CYP3A4, CYP2C9 thành các chất chuyển hóa hydroxyl hóa và glucuronide)",
            "clearance": "Thận (thải trừ các chất chuyển hóa, <5% bài tiết dưới dạng không đổi)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ biến cố tim mạch nghiêm trọng (nhồi máu cơ tim, đột quỵ) - có thể tử vong. Phản ứng da nghiêm trọng (Stevens-Johnson syndrome, toxic epidermal necrolysis) - có thể tử vong. Ngừng ngay nếu có phản ứng da. Không dùng trong 3 tháng cuối thai kỳ. LƯU Ý: Đã ngưng dùng ở nhiều nơi (bao gồm Mỹ) do lo ngại về an toàn.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX-2, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần"
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng valdecoxib nếu có dấu hiệu suy thận"
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "Giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng độc tính",
                    "management": "Theo dõi nồng độ lithium. Có thể cần giảm liều lithium."
                }
            ],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "CHỐNG CHỈ ĐỊNH (bệnh gan nặng)",
            "notes": "Valdecoxib chuyển hóa ở gan qua CYP3A4, CYP2C9. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Chóng mặt, nhức đầu",
                "Lú lẫn, buồn ngủ",
                "Hạ huyết áp",
                "Suy thận cấp",
                "Tăng nguy cơ biến cố tim mạch",
                "Phản ứng da nghiêm trọng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng valdecoxib ngay",
                "Theo dõi chức năng thận (creatinine, BUN), điện giải",
                "Theo dõi huyết áp, nhịp tim",
                "Truyền dịch nếu hạ huyết áp, suy thận",
                "Theo dõi dấu hiệu biến cố tim mạch",
                "Điều trị phản ứng da nếu có (corticosteroid, hỗ trợ)",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu biến cố tim mạch, phản ứng da. Theo dõi ít nhất 24 giờ do half-life dài (8-11 giờ)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
                "timing": "Dùng 1-2 lần/ngày. Liều tối đa: 40mg/ngày.",
                "notes": "LƯU Ý: Đã ngưng dùng ở nhiều nơi (bao gồm Mỹ) do lo ngại về an toàn tim mạch và phản ứng da nghiêm trọng. Cân nhắc thuốc thay thế an toàn hơn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Valdecoxib (Bextra) - WITHDRAWN",
                "UpToDate - Valdecoxib: Drug information"
            ],
            "evidence_level": "High - FDA approved (withdrawn in US due to safety concerns)"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": True,
            "organ_toxicity": ["GI", "renal", "cardiac", "dermatologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["LFT", "RFT", "GI symptoms", "Blood pressure", "Cardiovascular symptoms", "Skin reactions"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cardiovascular and GI risks",
            "FDA Black Box Warning - Serious skin reactions",
            "WITHDRAWN in US due to safety concerns",
            "ISMP High Alert Medications - NSAIDs"
        ]
    }
}
