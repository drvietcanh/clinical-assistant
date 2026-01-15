"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Short-acting Beta-2 Agonist (SABA)s

SHORT_ACTING_BETA_2_AGONIST_SABA_DRUGS = {
    "Salbutamol": {
        'group': 'Respiratory - Short-acting Beta-2 Agonist (SABA)',
        'vietnamese_name': 'Salbutamol, Ventolin, Albuterol, Salbutamol Stada',
        'administration': ['Inhalation', 'IV', 'PO'],
        'indications': [
            'Hen phế quản (cắt cơn)',
            'COPD (cắt cơn)',
            'Co thắt phế quản cấp',
            'Dự phòng co thắt do vận động (exercise-induced bronchospasm)',
            'Đợt cấp hen phế quản nặng (dạng IV trong bệnh viện)'
        ],
        'contraindications': {
            'tuyệt_đối': [
                'Dị ứng với salbutamol hoặc bất kỳ thành phần nào của thuốc',
                'Nhịp tim nhanh nặng không kiểm soát',
                'Loạn nhịp tim nghiêm trọng'
            ],
            'tương_đối': [
                'Bệnh tim mạch (suy tim, thiếu máu cơ tim, loạn nhịp tim) - thận trọng, theo dõi chặt chẽ',
                'Tăng huyết áp không kiểm soát - thận trọng',
                'Đái tháo đường - có thể tăng đường huyết',
                'Cường giáp - tăng nguy cơ tác dụng phụ tim mạch',
                'Dùng với beta-blocker - đối kháng tác dụng, tránh dùng chung'
            ]
        },
        'dosage': {
            'adult_inhalation': '1-2 puffs (100-200mcg) mỗi 4-6 giờ khi cần',
            'adult_nebulizer': '2.5-5mg mỗi 4-6 giờ khi cần',
            'adult_iv': '0.5mg IV bolus, sau đó 5-20mcg/phút truyền liên tục (trong đợt cấp nặng)',
            'pediatric': {
                'inhalation_4_11_years': '1-2 puffs (100-200mcg) mỗi 4-6 giờ khi cần',
                'inhalation_under_4_years': '1 puff (100mcg) mỗi 4-6 giờ khi cần (với spacer)',
                'nebulizer': '0.15mg/kg (tối thiểu 2.5mg) mỗi 4-6 giờ',
                'notes': 'FDA-approved cho trẻ em ≥4 tuổi dạng hít. Dưới 4 tuổi cần dùng với spacer và theo dõi chặt chẽ.'
            },
            'geriatric': {
                'dosing': 'Liều tương tự người lớn',
                'notes': 'Không cần điều chỉnh liều, nhưng thận trọng ở bệnh nhân tim mạch'
            },
            'notes': 'Dùng khi cần (PRN) cho cắt cơn, không dùng thường xuyên. Nếu cần >4 lần/ngày → đánh giá lại điều trị.'
        },
        'side_effects': ['Tim đập nhanh', 'Run cơ', 'Đau đầu',
        'Hạ kali máu (liều cao)', 'Loạn nhịp tim (hiếm)'],
        'interactions': [
            'Beta-blocker: đối kháng tác dụng (tránh dùng)',
            'MAO inhibitors, Tricyclic antidepressants: tăng tác dụng tim mạch',
            'Diuretics: tăng nguy cơ hạ kali máu',
            'Digoxin: có thể tăng nguy cơ loạn nhịp tim'
        ],
        'mechanism_of_action':
        'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng nhanh, ngắn (4-6 giờ). Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch ở liều cao. Giảm phóng thích chất trung gian gây viêm từ mast cells.'
        , 'monitoring': [
        'Nhịp tim, huyết áp (đặc biệt khi dùng IV hoặc liều cao)',
        'Kali máu nếu dùng liều cao hoặc kéo dài',
        'Đáp ứng phế quản (peak flow, FEV1)',
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp',
        'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)'],
        'precautions': [
        'Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên',
        'Nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS',
        'Tránh dùng với beta-blocker (đối kháng tác dụng)',
        'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)'
        , 'Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ',
        'Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng',
        'Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị'],
        'pharmacokinetics': {
            'half_life': '2-7 giờ (hít), 2-4 giờ (IV)',
            'onset': '5-15 phút (hít), 2-5 phút (IV)',
            'duration': '4-6 giờ',
            'bioavailability': 'Không rõ (dạng hít tác dụng tại chỗ), ~50% (PO)',
            'protein_binding': '10%',
            'volume_of_distribution': '~2 L/kg',
            'metabolism': 'Gan (chuyển hóa qua sulfation bởi SULT1A3, một phần qua CYP450), chuyển hóa nhanh',
            'clearance': 'Gan (chuyển hóa), thận (thải trừ). Tổng clearance: ~6-8 L/h/kg',
            'absorption': 'Hấp thu nhanh sau khi hít. Thời gian đạt nồng độ đỉnh (Tmax): 2-3 giờ (PO)',
            'food_effect': 'Không ảnh hưởng đáng kể đến hấp thu dạng hít'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.',
        'black_box_warnings':
        'Không dùng đơn độc cho hen phế quản mạn tính - phải kết hợp với corticosteroid dạng hít. Dùng quá mức (>4 lần/ngày) có thể gây tăng nguy cơ tử vong do hen. Nếu cần dùng thường xuyên → cần đánh giá lại và tăng điều trị kiểm soát.',
        'pregnancy': 'C - Thận trọng trong thai kỳ. Có thể dùng khi lợi ích vượt trội nguy cơ.',
        'drug_interactions': {
            'major': [
                {
                    'drug': 'Beta-blockers (non-selective và selective)',
                    'mechanism': 'Beta-blockers đối kháng tác dụng của salbutamol tại beta-2 receptors',
                    'effect': 'Giảm hoặc mất hiệu quả giãn phế quản, có thể làm nặng thêm co thắt phế quản',
                    'management': 'TRÁNH DÙNG CHUNG. Nếu cần dùng beta-blocker, cân nhắc beta-1 selective nhưng vẫn thận trọng.'
                }
            ],
            'moderate': [
                {
                    'drug': 'MAO inhibitors, Tricyclic antidepressants',
                    'mechanism': 'Có thể tăng tác dụng tim mạch của salbutamol',
                    'effect': 'Tăng nguy cơ nhịp tim nhanh, loạn nhịp tim',
                    'management': 'Thận trọng khi dùng cùng. Theo dõi nhịp tim, huyết áp.'
                },
                {
                    'drug': 'Diuretics (thiazide, loop)',
                    'mechanism': 'Cả hai đều có thể gây hạ kali máu',
                    'effect': 'Tăng nguy cơ hạ kali máu nghiêm trọng',
                    'management': 'Theo dõi kali máu khi dùng cùng.'
                }
            ],
            'minor': []
        },
        'pregnancy_lactation': {
            'fda_category': 'C',
            'pregnancy_details': 'Salbutamol phân loại C - thận trọng trong thai kỳ. Có thể được dùng trong thai kỳ khi lợi ích vượt trội nguy cơ, đặc biệt trong điều trị hen phế quản không kiểm soát. Tránh dùng liều cao hoặc kéo dài.',
            'lactation': {
                'safety': 'Compatible',
                'details': 'Salbutamol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp khi mẹ dùng dạng hít.',
                'recommendation': 'Có thể dùng khi cho con bú, đặc biệt dạng hít.'
            }
        },
        'hepatic_adjustment': {
            'mild': 'Không cần điều chỉnh liều',
            'moderate': 'Không cần điều chỉnh liều',
            'severe': 'Thận trọng, theo dõi chặt chẽ',
            'notes': 'Salbutamol chuyển hóa ở gan. Suy gan có thể ảnh hưởng đến chuyển hóa nhưng thường không cần điều chỉnh liều ở dạng hít.'
        },
        'renal_adjustment': {
            'normal': 'Không cần điều chỉnh liều',
            '30_60': 'Không cần điều chỉnh liều',
            'under_30': 'Thận trọng, có thể cần giảm liều ở dạng PO hoặc IV'
        },
        'overdose_management': {
            'symptoms': [
                'Nhịp tim nhanh (>120 bpm), loạn nhịp tim',
                'Run cơ nặng, bồn chồn',
                'Hạ kali máu (có thể gây loạn nhịp tim)',
                'Co thắt phế quản nghịch lý (hiếm)',
                'Đau ngực, tăng huyết áp hoặc hạ huyết áp'
            ],
            'antidote': 'Beta-blocker (propranolol, metoprolol) - nhưng THẬN TRỌNG ở bệnh nhân hen/COPD.',
            'treatment': [
                'Ngừng salbutamol ngay lập tức',
                'Theo dõi dấu hiệu sinh tồn',
                'Hỗ trợ hô hấp nếu cần',
                'Điều trị loạn nhịp tim nếu có',
                'Bù kali nếu hạ kali máu',
                'Beta-blocker chỉ khi thực sự cần và bệnh nhân không có hen/COPD nặng'
            ],
            'monitoring': 'Nhịp tim, huyết áp, SpO2, ECG, kali máu, đáp ứng phế quản'
        },
        'reversal_agents': {
            'available': True,
            'agents': [
                {
                    'agent': 'Beta-blocker (propranolol, metoprolol)',
                    'indication': 'Quá liều nặng với nhịp tim nhanh',
                    'dose': 'Propranolol 1-3mg IV hoặc metoprolol 2.5-5mg IV',
                    'notes': 'THẬN TRỌNG: Chỉ dùng khi thực sự cần và bệnh nhân không có hen/COPD nặng.'
                }
            ],
            'notes': 'Beta-blocker có thể đối kháng tác dụng nhưng cần thận trọng ở bệnh nhân hen/COPD.'
        },
        'administration_instructions': {
            'inhalation': {
                'preparation': 'Lắc kỹ bình xịt trước khi dùng. Kiểm tra hạn sử dụng.',
                'administration': 'Hít sâu và chậm, giữ hơi thở 10 giây. Đợi 1-2 phút trước khi hít lần tiếp theo.',
                'timing': 'Dùng khi cần (PRN), không quá 4 lần/ngày.',
                'missed_dose': 'Dùng ngay khi nhớ ra nếu cần.',
                'monitoring': ['Nhịp tim, huyết áp', 'Đáp ứng phế quản']
            },
            'iv': {
                'preparation': 'Chuẩn bị dung dịch truyền tĩnh mạch',
                'administration': '0.5mg IV bolus, sau đó 5-20mcg/phút truyền liên tục',
                'monitoring': ['Nhịp tim, huyết áp liên tục', 'ECG', 'Đáp ứng phế quản']
            }
        },
        'contraindications_detail': {
            'tuyệt_đối': [
                'Dị ứng với salbutamol',
                'Nhịp tim nhanh nặng không kiểm soát',
                'Loạn nhịp tim nghiêm trọng'
            ],
            'tương_đối': [
                'Bệnh tim mạch - thận trọng',
                'Tăng huyết áp không kiểm soát - thận trọng',
                'Đái tháo đường - có thể tăng đường huyết',
                'Dùng với beta-blocker - tránh dùng chung'
            ]
        },
        'references': {
            'primary_sources': [
                'FDA Drug Label - Albuterol (Salbutamol)',
                'UpToDate - Albuterol: Drug information (updated 2024)',
                'GINA Guidelines - Global Strategy for Asthma Management and Prevention (2024)',
                'GOLD Guidelines - Global Strategy for the Diagnosis, Management and Prevention of COPD (2024)'
            ],
            'last_updated': '2025-02-18',
            'evidence_level': 'High - FDA-approved, widely used. Evidence from GINA and GOLD guidelines.'
        }
    },
    "Terbutaline":     {
        "group": "Respiratory - Short-acting Beta-2 Agonist (SABA)",
        "vietnamese_name": "Terbutaline, Bricanyl",
        "administration": [
            "Inhalation",
            "SC",
            "PO"
    ],
        "indications": [
            "Hen phế quản (cắt cơn)",
            "COPD (cắt cơn)",
            "Co thắt phế quản cấp",
            "Dự phòng co thắt do vận động"
    ],
        "contraindications": [
            "Dị ứng",
            "Nhịp tim nhanh nặng"
    ],
        "dosage": {
            "adult_inhalation": "250-500mcg (1-2 puffs) mỗi 4-6 giờ khi cần",
            "adult_nebulizer": "5mg mỗi 4-6 giờ",
            "adult_sc": "0.25-0.5mg SC (đợt cấp nặng, không có khí dung)",
            "adult_po": "2.5-5mg x 3 lần/ngày",
            "notes": "Dùng khi cần (PRN) cho cắt cơn. Dạng SC dùng trong cấp cứu khi không có khí dung.",
        },
        "side_effects": [
            "Tim đập nhanh",
            "Run cơ",
            "Đau đầu",
            "Hạ kali máu (liều cao)",
            "Loạn nhịp tim (hiếm)"
    ],
        "interactions": [
            "Beta-blocker: đối kháng tác dụng (tránh dùng)"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng nhanh, ngắn (4-6 giờ). Tương tự salbutamol nhưng có thể dùng dạng SC trong cấp cứu. Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch ở liều cao. Giảm phóng thích chất trung gian gây viêm từ mast cells.""",
        "monitoring": [
            "Nhịp tim, huyết áp (đặc biệt khi dùng SC hoặc liều cao)",
            "Kali máu nếu dùng liều cao hoặc kéo dài",
            "Đáp ứng phế quản (peak flow, FEV1)",
            "Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp",
            "Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)"
    ],
        "precautions": [
            "Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên",
            "Nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS",
            "Tránh dùng với beta-blocker (đối kháng tác dụng)",
            "Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)",
            "Dạng SC: dùng trong cấp cứu khi không có khí dung, theo dõi chặt chẽ nhịp tim",
            "Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ",
            "Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng",
            "Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị"
    ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (hít), 2-3 giờ (SC)",
            "onset": "5-15 phút (hít), 5-10 phút (SC)",
            "duration": "4-6 giờ",
            "protein_binding": "25%",
            "clearance": "Gan (chuyển hóa qua sulfation, một phần qua CYP450), thận (thải trừ)",
        },
        "storage": """Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.""",
        "black_box_warnings": """Không dùng đơn độc cho hen phế quản mạn tính - phải kết hợp với corticosteroid dạng hít. Dùng quá mức (>4 lần/ngày) có thể gây tăng nguy cơ tử vong do hen. Nếu cần dùng thường xuyên → cần đánh giá lại và tăng điều trị kiểm soát.""",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (non-selective và selective)",
                    "mechanism": "Beta-blockers đối kháng tác dụng của terbutaline tại beta-2 receptors, làm giảm hiệu quả giãn phế quản",
                    "effect": "Giảm hoặc mất hiệu quả giãn phế quản, có thể làm nặng thêm co thắt phế quản",
                    "management": "TRÁNH DÙNG CHUNG. Nếu cần dùng beta-blocker, cân nhắc beta-1 selective (metoprolol, atenolol) nhưng vẫn thận trọng. Theo dõi chặt chẽ đáp ứng phế quản."
                }
            ],
            "moderate": [
                {
                    "drug": "MAO inhibitors, Tricyclic antidepressants",
                    "mechanism": "Có thể tăng tác dụng tim mạch của terbutaline",
                    "effect": "Tăng nguy cơ nhịp tim nhanh, loạn nhịp tim, tăng huyết áp",
                    "management": "Thận trọng khi dùng cùng. Theo dõi nhịp tim, huyết áp chặt chẽ."
                },
                {
                    "drug": "Diuretics (thiazide, loop)",
                    "mechanism": "Cả hai đều có thể gây hạ kali máu",
                    "effect": "Tăng nguy cơ hạ kali máu nghiêm trọng, loạn nhịp tim",
                    "management": "Theo dõi kali máu khi dùng cùng, đặc biệt ở liều cao terbutaline."
                }
            ],
            "minor": [
                {
                    "drug": "Other beta-2 agonists",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tác dụng phụ tim mạch",
                    "management": "Thận trọng khi dùng cùng các beta-2 agonist khác. Theo dõi nhịp tim, huyết áp."
                }
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Terbutaline phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Terbutaline có thể được dùng trong thai kỳ khi lợi ích vượt trội nguy cơ, đặc biệt trong điều trị hen phế quản không kiểm soát. Tuy nhiên, tránh dùng liều cao hoặc kéo dài trong thai kỳ do nguy cơ tác dụng phụ tim mạch cho mẹ và thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Terbutaline bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ khi mẹ dùng terbutaline dạng hít ở liều điều trị.",
                "recommendation": "Có thể dùng khi cho con bú, đặc biệt dạng hít. Theo dõi trẻ nếu có dấu hiệu bất thường (nhịp tim nhanh, run cơ)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, theo dõi chặt chẽ",
            "notes": "Terbutaline chuyển hóa ở gan qua sulfation và một phần qua CYP450. Suy gan có thể ảnh hưởng đến chuyển hóa nhưng thường không cần điều chỉnh liều ở dạng hít. Thận trọng ở suy gan nặng."
        },
        "renal_adjustment": {
            "normal": "Không cần điều chỉnh liều",
            "30_60": "Không cần điều chỉnh liều",
            "under_30": "Thận trọng, có thể cần giảm liều ở dạng PO hoặc SC"
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim nhanh (>120 bpm), loạn nhịp tim (rung nhĩ, nhịp nhanh thất)",
                "Run cơ nặng, bồn chồn, lo âu",
                "Đau đầu, chóng mặt",
                "Hạ kali máu (có thể gây loạn nhịp tim)",
                "Tăng đường huyết (do kích thích beta-2)",
                "Co thắt phế quản nghịch lý (hiếm nhưng nguy hiểm)",
                "Tăng huyết áp hoặc hạ huyết áp",
                "Đau ngực"
            ],
            "antidote": "Beta-blocker (propranolol, metoprolol) - nhưng THẬN TRỌNG ở bệnh nhân hen/COPD vì có thể làm nặng co thắt phế quản. Chỉ dùng khi có chỉ định và theo dõi chặt chẽ.",
            "treatment": [
                "Ngừng terbutaline ngay lập tức",
                "Theo dõi dấu hiệu sinh tồn (nhịp tim, huyết áp, SpO2, ECG)",
                "Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)",
                "Điều trị loạn nhịp tim nếu có (theo protocol ACLS nếu cần)",
                "Bù kali nếu hạ kali máu",
                "Beta-blocker chỉ khi thực sự cần và bệnh nhân không có hen/COPD nặng",
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi trong ICU nếu quá liều nặng"
            ],
            "monitoring": "Nhịp tim, huyết áp, SpO2, ECG liên tục, kali máu, đường huyết, dấu hiệu sinh tồn, đáp ứng phế quản"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Beta-blocker (propranolol, metoprolol)",
                    "indication": "Quá liều nặng với nhịp tim nhanh, loạn nhịp tim",
                    "dose": "Propranolol 1-3mg IV hoặc metoprolol 2.5-5mg IV",
                    "notes": "THẬN TRỌNG: Chỉ dùng khi thực sự cần và bệnh nhân không có hen/COPD nặng. Beta-blocker có thể làm nặng co thắt phế quản. Theo dõi chặt chẽ đáp ứng phế quản."
                }
            ],
            "notes": "Beta-blocker có thể đối kháng tác dụng của terbutaline nhưng cần thận trọng ở bệnh nhân hen/COPD. Không có antidote đặc hiệu khác."
        },
        "administration_instructions": {
            "inhalation": {
                "preparation": "Lắc kỹ bình xịt trước khi dùng. Kiểm tra hạn sử dụng và số lần xịt còn lại.",
                "administration": "Hít sâu và chậm, giữ hơi thở 10 giây sau khi hít. Đợi 1-2 phút trước khi hít lần tiếp theo nếu cần.",
                "with_food": "Không liên quan",
                "timing": "Dùng khi cần (PRN) cho cắt cơn, không quá 4 lần/ngày. Nếu cần thường xuyên → đánh giá lại điều trị.",
                "missed_dose": "Dùng ngay khi nhớ ra nếu cần. Không dùng gấp đôi liều.",
                "special_populations": {
                    "elderly": "Không cần điều chỉnh liều, nhưng thận trọng ở bệnh nhân tim mạch",
                    "pediatric": "Liều tương tự người lớn theo cân nặng. FDA-approved cho trẻ em ≥4 tuổi.",
                    "renal_impairment": "Không cần điều chỉnh liều ở dạng hít",
                    "hepatic_impairment": "Không cần điều chỉnh liều ở dạng hít"
                },
                "monitoring": ["Nhịp tim, huyết áp", "Đáp ứng phế quản (peak flow, FEV1)", "Dấu hiệu quá liều"]
            },
            "sc": {
                "preparation": "Dùng trong cấp cứu khi không có khí dung. Chuẩn bị ống tiêm vô trùng.",
                "administration": "Tiêm dưới da 0.25-0.5mg. Có thể lặp lại sau 15-30 phút nếu cần.",
                "monitoring": ["Nhịp tim, huyết áp liên tục", "Đáp ứng phế quản", "Dấu hiệu quá liều"]
            },
            "po": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "2.5-5mg x 3 lần/ngày",
                "monitoring": ["Nhịp tim, huyết áp", "Đáp ứng phế quản"]
            }
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với terbutaline hoặc bất kỳ thành phần nào của thuốc",
                "Nhịp tim nhanh nặng không kiểm soát",
                "Loạn nhịp tim nghiêm trọng"
            ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, thiếu máu cơ tim, loạn nhịp tim) - thận trọng, theo dõi chặt chẽ",
                "Tăng huyết áp không kiểm soát - thận trọng",
                "Đái tháo đường - có thể tăng đường huyết",
                "Cường giáp - tăng nguy cơ tác dụng phụ tim mạch",
                "Dùng với beta-blocker - đối kháng tác dụng, tránh dùng chung"
            ]
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Terbutaline (Bricanyl)",
                "UpToDate - Terbutaline: Drug information (updated 2024)",
                "GINA Guidelines - Global Strategy for Asthma Management and Prevention (2024)",
                "GOLD Guidelines - Global Strategy for the Diagnosis, Management and Prevention of COPD (2024)",
                "British Thoracic Society Guidelines - Asthma Management (2019)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, widely used in clinical practice. Evidence from GINA and GOLD guidelines."
        }
    },
    "Levalbuterol": {
        "group": "Respiratory - Short-acting Beta-2 Agonist (SABA)",
        "vietnamese_name": "Levalbuterol, Xopenex, R-albuterol",
        "administration": ["Inhalation", "Nebulizer"],
        "indications": [
            "Hen phế quản (cắt cơn)",
            "COPD (cắt cơn)",
            "Co thắt phế quản cấp",
            "Dự phòng co thắt do vận động (exercise-induced bronchospasm)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với levalbuterol hoặc bất kỳ thành phần nào của thuốc",
                "Nhịp tim nhanh nặng không kiểm soát",
                "Loạn nhịp tim nghiêm trọng"
            ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, thiếu máu cơ tim, loạn nhịp tim) - thận trọng, theo dõi chặt chẽ",
                "Tăng huyết áp không kiểm soát - thận trọng",
                "Đái tháo đường - có thể tăng đường huyết",
                "Cường giáp - tăng nguy cơ tác dụng phụ tim mạch",
                "Dùng với beta-blocker - đối kháng tác dụng, tránh dùng chung"
            ]
        },
        "dosage": {
            "adult_inhalation": "45-90mcg (1-2 puffs) mỗi 4-6 giờ khi cần",
            "adult_nebulizer": "0.63mg hoặc 1.25mg mỗi 4-6 giờ khi cần",
            "pediatric": {
                "inhalation_4_11_years": "45mcg (1 puff) mỗi 4-6 giờ khi cần",
                "nebulizer_6_11_years": "0.31mg mỗi 4-6 giờ",
                "nebulizer_under_6_years": "0.31mg mỗi 4-6 giờ (theo dõi chặt chẽ)",
                "notes": "FDA-approved cho trẻ em ≥4 tuổi dạng hít. Dưới 4 tuổi cần dùng với spacer và theo dõi chặt chẽ."
            },
            "geriatric": {
                "dosing": "Liều tương tự người lớn",
                "notes": "Không cần điều chỉnh liều, nhưng thận trọng ở bệnh nhân tim mạch"
            },
            "notes": "Levalbuterol là R-enantiomer của albuterol (racemic mixture). Chọn lọc beta-2 hơn albuterol, ít tác dụng phụ tim mạch hơn. Dùng khi cần (PRN) cho cắt cơn, không dùng thường xuyên. Nếu cần >4 lần/ngày → đánh giá lại điều trị."
        },
        "side_effects": [
            "Tim đập nhanh (ít hơn albuterol)",
            "Run cơ (ít hơn albuterol)",
            "Đau đầu",
            "Hạ kali máu (liều cao, ít hơn albuterol)",
            "Loạn nhịp tim (hiếm, ít hơn albuterol)"
        ],
        "interactions": [
            "Beta-blocker: đối kháng tác dụng (tránh dùng)",
            "MAO inhibitors, Tricyclic antidepressants: tăng tác dụng tim mạch",
            "Diuretics: tăng nguy cơ hạ kali máu",
            "Digoxin: có thể tăng nguy cơ loạn nhịp tim"
        ],
        "mechanism_of_action": "Levalbuterol là R-enantiomer (levorotatory) của albuterol. Albuterol là racemic mixture (50% R-albuterol và 50% S-albuterol). R-albuterol (levalbuterol) là dạng hoạt động, chịu trách nhiệm cho tác dụng giãn phế quản. S-albuterol không có tác dụng giãn phế quản và có thể gây tác dụng phụ. Levalbuterol kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Levalbuterol chọn lọc beta-2 hơn albuterol racemic, ít tác dụng phụ tim mạch hơn (ít nhịp tim nhanh, ít run cơ). Tác dụng nhanh (5-15 phút), ngắn (4-6 giờ).",
        "monitoring": [
            "Nhịp tim, huyết áp (đặc biệt khi dùng liều cao)",
            "Kali máu nếu dùng liều cao hoặc kéo dài",
            "Đáp ứng phế quản (peak flow, FEV1)",
            "Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp",
            "Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)"
        ],
        "precautions": [
            "Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên",
            "Nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS",
            "Tránh dùng với beta-blocker (đối kháng tác dụng)",
            "Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)",
            "Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ",
            "Rửa miệng sau khi dùng dạng hít để giảm kích ứng",
            "Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị",
            "Ưu điểm: ít tác dụng phụ tim mạch hơn albuterol racemic"
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (hít)",
            "onset": "5-15 phút (hít), 5-10 phút (nebulizer)",
            "duration": "4-6 giờ",
            "bioavailability": "Không rõ (dạng hít tác dụng tại chỗ)",
            "protein_binding": "10%",
            "volume_of_distribution": "~2 L/kg",
            "metabolism": "Gan (chuyển hóa qua sulfation bởi SULT1A3, một phần qua CYP450), chuyển hóa nhanh",
            "clearance": "Gan (chuyển hóa), thận (thải trừ). Tổng clearance: ~6-8 L/h/kg",
            "absorption": "Hấp thu nhanh sau khi hít. Thời gian đạt nồng độ đỉnh (Tmax): 2-3 giờ",
            "food_effect": "Không ảnh hưởng đáng kể đến hấp thu dạng hít"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "Không dùng đơn độc cho hen phế quản mạn tính - phải kết hợp với corticosteroid dạng hít. Dùng quá mức (>4 lần/ngày) có thể gây tăng nguy cơ tử vong do hen. Nếu cần dùng thường xuyên → cần đánh giá lại và tăng điều trị kiểm soát.",
        "pregnancy": "C - Thận trọng trong thai kỳ. Có thể dùng khi lợi ích vượt trội nguy cơ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (non-selective và selective)",
                    "mechanism": "Beta-blockers đối kháng tác dụng của levalbuterol tại beta-2 receptors",
                    "effect": "Giảm hoặc mất hiệu quả giãn phế quản, có thể làm nặng thêm co thắt phế quản",
                    "management": "TRÁNH DÙNG CHUNG. Nếu cần dùng beta-blocker, cân nhắc beta-1 selective nhưng vẫn thận trọng."
                }
            ],
            "moderate": [
                {
                    "drug": "MAO inhibitors, Tricyclic antidepressants",
                    "mechanism": "Có thể tăng tác dụng tim mạch của levalbuterol",
                    "effect": "Tăng nguy cơ nhịp tim nhanh, loạn nhịp tim",
                    "management": "Thận trọng khi dùng cùng. Theo dõi nhịp tim, huyết áp."
                },
                {
                    "drug": "Diuretics (thiazide, loop)",
                    "mechanism": "Cả hai đều có thể gây hạ kali máu",
                    "effect": "Tăng nguy cơ hạ kali máu nghiêm trọng",
                    "management": "Theo dõi kali máu khi dùng cùng."
                }
            ],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Levalbuterol phân loại C - thận trọng trong thai kỳ. Có thể được dùng trong thai kỳ khi lợi ích vượt trội nguy cơ, đặc biệt trong điều trị hen phế quản không kiểm soát. Tránh dùng liều cao hoặc kéo dài.",
            "lactation": {
                "safety": "Compatible",
                "details": "Levalbuterol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp khi mẹ dùng dạng hít.",
                "recommendation": "Có thể dùng khi cho con bú, đặc biệt dạng hít."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, theo dõi chặt chẽ",
            "notes": "Levalbuterol chuyển hóa ở gan. Suy gan có thể ảnh hưởng đến chuyển hóa nhưng thường không cần điều chỉnh liều ở dạng hít."
        },
        "renal_adjustment": {
            "normal": "Không cần điều chỉnh liều",
            "30_60": "Không cần điều chỉnh liều",
            "under_30": "Thận trọng, có thể cần giảm liều ở dạng nebulizer"
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim nhanh (>120 bpm), loạn nhịp tim",
                "Run cơ nặng, bồn chồn",
                "Hạ kali máu (có thể gây loạn nhịp tim)",
                "Co thắt phế quản nghịch lý (hiếm)",
                "Đau ngực, tăng huyết áp hoặc hạ huyết áp"
            ],
            "antidote": "Beta-blocker (propranolol, metoprolol) - nhưng THẬN TRỌNG ở bệnh nhân hen/COPD.",
            "treatment": [
                "Ngừng levalbuterol ngay lập tức",
                "Theo dõi dấu hiệu sinh tồn",
                "Hỗ trợ hô hấp nếu cần",
                "Điều trị loạn nhịp tim nếu có",
                "Bù kali nếu hạ kali máu",
                "Beta-blocker chỉ khi thực sự cần và bệnh nhân không có hen/COPD nặng"
            ],
            "monitoring": "Nhịp tim, huyết áp, SpO2, ECG, kali máu, đáp ứng phế quản"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Beta-blocker (propranolol, metoprolol)",
                    "indication": "Quá liều nặng với nhịp tim nhanh",
                    "dose": "Propranolol 1-3mg IV hoặc metoprolol 2.5-5mg IV",
                    "notes": "THẬN TRỌNG: Chỉ dùng khi thực sự cần và bệnh nhân không có hen/COPD nặng."
                }
            ],
            "notes": "Beta-blocker có thể đối kháng tác dụng nhưng cần thận trọng ở bệnh nhân hen/COPD."
        },
        "administration_instructions": {
            "inhalation": {
                "preparation": "Lắc kỹ bình xịt trước khi dùng. Kiểm tra hạn sử dụng.",
                "administration": "Hít sâu và chậm, giữ hơi thở 10 giây. Đợi 1-2 phút trước khi hít lần tiếp theo.",
                "timing": "Dùng khi cần (PRN), không quá 4 lần/ngày.",
                "missed_dose": "Dùng ngay khi nhớ ra nếu cần.",
                "monitoring": ["Nhịp tim, huyết áp", "Đáp ứng phế quản"]
            },
            "nebulizer": {
                "preparation": "Pha levalbuterol với normal saline theo hướng dẫn",
                "administration": "Phun sương qua máy phun sương, hít sâu và chậm",
                "timing": "Dùng khi cần (PRN), không quá 4 lần/ngày",
                "monitoring": ["Nhịp tim, huyết áp", "Đáp ứng phế quản"]
            }
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với levalbuterol",
                "Nhịp tim nhanh nặng không kiểm soát",
                "Loạn nhịp tim nghiêm trọng"
            ],
            "tương_đối": [
                "Bệnh tim mạch - thận trọng",
                "Tăng huyết áp không kiểm soát - thận trọng",
                "Đái tháo đường - có thể tăng đường huyết",
                "Dùng với beta-blocker - tránh dùng chung"
            ]
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Xopenex (Levalbuterol)",
                "UpToDate - Levalbuterol: Drug information (updated 2024)",
                "GINA Guidelines - Global Strategy for Asthma Management and Prevention (2024)",
                "GOLD Guidelines - Global Strategy for the Diagnosis, Management and Prevention of COPD (2024)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, widely used. Evidence from GINA and GOLD guidelines."
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Heart rate", "Blood pressure", "Potassium"],
            "look_alike_sound_alike": ["Levalbuterol", "Albuterol", "Salmeterol", "Formoterol"]
        },
        "guideline_tags": [
            "GINA Guidelines - Global Strategy for Asthma Management and Prevention",
            "GOLD Guidelines - Global Strategy for the Diagnosis, Management and Prevention of COPD"
        ]
    }
}

__all__ = ['SHORT_ACTING_BETA_2_AGONIST_SABA_DRUGS']
