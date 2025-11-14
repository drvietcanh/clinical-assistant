"""Respiratory Medications
Short-acting Beta-2 Agonist (SABA) drugs"""

# Short-acting Beta-2 Agonist (SABA)s

SHORT_ACTING_BETA_2_AGONISTS_DRUGS = {
    "Salbutamol": {
        'group': 'Respiratory - Short-acting Beta-2 Agonist (SABA)',
        'vietnamese_name': 'Salbutamol, Albuterol, Ventolin',
        'administration': ['INH', 'IV', 'PO', 'NEB'],
        'indications': [
            'Hen phế quản (cắt cơn)',
            'COPD (cắt cơn)',
            'Co thắt phế quản cấp',
            'Dự phòng co thắt do vận động'
        ],
        'contraindications': [
            'Dị ứng',
            'Nhịp tim nhanh nặng'
        ],
        'dosage': {
            'adult_inhalation': '1-2 puffs (100-200mcg) mỗi 4-6 giờ khi cần',
            'adult_nebulizer': '2.5-5mg mỗi 4-6 giờ',
            'adult_iv': '0.5mg IV, sau đó 5-20mcg/phút truyền liên tục',
            'notes': 'Dùng khi cần (PRN) cho cắt cơn, không dùng thường xuyên'
        },
        'renal_adjustment': {
            'normal': 'Không đổi',
            '30_60': 'Không đổi',
            'under_30': 'Không đổi'
        },
        'side_effects': [
            'Tim đập nhanh',
            'Run cơ',
            'Đau đầu',
            'Hạ kali máu (liều cao)',
            'Loạn nhịp tim (hiếm)'
        ],
        'interactions': [
            'Beta-blocker: đối kháng tác dụng (tránh dùng)'
        ],
        'pregnancy': 'C',
        'enhanced_fields': {
            'mechanism_of_action': 'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng nhanh, ngắn (4-6 giờ). Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch ở liều cao. Giảm phóng thích chất trung gian gây viêm từ mast cells.',
            'monitoring': [
                'Nhịp tim, huyết áp (đặc biệt khi dùng IV hoặc liều cao)',
                'Kali máu nếu dùng liều cao hoặc kéo dài',
                'Đáp ứng phế quản (peak flow, FEV1)',
                'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp',
                'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)'
            ],
            'precautions': [
                'Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên',
                'Nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS',
                'Tránh dùng với beta-blocker (đối kháng tác dụng)',
                'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)',
                'Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ',
                'Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng',
                'Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị'
            ],
            'pharmacokinetics': 'Half-life: 2-7 giờ (hít), 2-4 giờ (IV). Onset: 5-15 phút (hít), 2-5 phút (IV). Duration: 4-6 giờ. Protein binding: 10%. Clearance: Gan (chuyển hóa qua sulfation, một phần qua CYP450), thận (thải trừ).',
            'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.',
            'black_box_warnings': 'Không dùng đơn độc cho hen phế quản mạn tính - phải kết hợp với corticosteroid dạng hít. Dùng quá mức (>4 lần/ngày) có thể gây tăng nguy cơ tử vong do hen. Nếu cần dùng thường xuyên → cần đánh giá lại và tăng điều trị kiểm soát.',
            'drug_interactions': {
                'major': [
                    {
                        'drug': 'Beta-blockers (không chọn lọc: Propranolol, Nadolol)',
                        'mechanism': 'Beta-blockers đối kháng tác dụng beta-2 của salbutamol, có thể gây co thắt phế quản nặng',
                        'effect': 'Đối kháng tác dụng giãn phế quản, có thể gây co thắt phế quản nặng, suy hô hấp',
                        'management': 'TRÁNH DÙNG với beta-blocker không chọn lọc. Nếu bệnh nhân cần beta-blocker, dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng.'
                    }
                ],
                'moderate': [
                    {
                        'drug': 'Digoxin',
                        'mechanism': 'Salbutamol có thể gây hạ kali máu và tăng nhịp tim, tăng nguy cơ độc tính digoxin',
                        'effect': 'Tăng nguy cơ loạn nhịp tim, tăng độc tính digoxin',
                        'management': 'Theo dõi nồng độ digoxin và kali máu. Theo dõi ECG nếu có triệu chứng.'
                    },
                    {
                        'drug': 'Diuretics (Furosemide, Thiazide)',
                        'mechanism': 'Cả hai đều có thể gây hạ kali máu',
                        'effect': 'Tăng nguy cơ hạ kali máu nghiêm trọng, loạn nhịp tim',
                        'management': 'Theo dõi kali máu thường xuyên, đặc biệt khi dùng liều cao salbutamol. Bổ sung kali nếu cần.'
                    }
                ]
            },
            'contraindications': {
                'tuyệt_đối': [
                    'Dị ứng salbutamol hoặc các thành phần trong chế phẩm',
                    'Nhịp tim nhanh nặng không kiểm soát (>120 bpm)',
                    'Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)'
                ],
                'tương_đối': [
                    'Bệnh tim mạch (suy tim, bệnh mạch vành) - thận trọng, theo dõi chặt chẽ',
                    'Tăng huyết áp không kiểm soát - có thể tăng huyết áp',
                    'Loạn nhịp tim nhẹ - có thể làm nặng',
                    'Đái tháo đường - có thể tăng đường huyết',
                    'Hạ kali máu - có thể làm nặng'
                ]
            },
            'pregnancy_lactation': {
                'fda_category': 'C',
                'pregnancy_details': 'Salbutamol là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Salbutamol được sử dụng rộng rãi trong thai kỳ để điều trị hen và có vẻ an toàn. Hen phế quản không kiểm soát có thể gây nguy hiểm cho cả mẹ và thai nhi (thiếu oxy, suy thai). Salbutamol có thể được dùng khi lợi ích vượt quá nguy cơ. Dạng hít được ưu tiên hơn dạng uống hoặc IV để giảm tác dụng toàn thân.',
                'lactation': {
                    'safety': 'Compatible',
                    'details': 'Salbutamol bài tiết vào sữa mẹ ở nồng độ rất thấp. Dạng hít có hấp thu toàn thân tối thiểu, nồng độ trong sữa mẹ rất thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.',
                    'recommendation': 'Có thể dùng khi cho con bú. Dạng hít được ưu tiên. Dùng liều thấp nhất hiệu quả.'
                }
            },
            'hepatic_adjustment': {
                'mild': 'Không cần điều chỉnh liều',
                'moderate': 'Không cần điều chỉnh liều. Theo dõi tác dụng phụ nếu có.',
                'severe': 'Thận trọng, có thể cần giảm liều. Theo dõi tác dụng phụ chặt chẽ.',
                'notes': 'Salbutamol chuyển hóa chủ yếu qua gan (sulfation, glucuronidation). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, nhưng ít khi cần điều chỉnh liều vì dạng hít có tác dụng tại chỗ.'
            },
            'overdose_management': {
                'symptoms': [
                    'Triệu chứng tim mạch: Nhịp tim nhanh (>120-150 bpm), đánh trống ngực, loạn nhịp tim, đau ngực, tăng huyết áp',
                    'Triệu chứng thần kinh: Run cơ nặng, kích động, lo âu, mất ngủ, đau đầu, chóng mặt',
                    'Triệu chứng chuyển hóa: Hạ kali máu, tăng đường huyết',
                    'Triệu chứng hô hấp: Co thắt phế quản nghịch lý (hiếm nhưng nguy hiểm - khó thở nặng hơn)'
                ],
                'antidote': 'Không có antidote đặc hiệu. Beta-blocker chọn lọc có thể đối kháng tác dụng nhưng thận trọng vì có thể gây co thắt phế quản.',
                'treatment': [
                    'Ngừng ngay salbutamol',
                    'Theo dõi dấu hiệu sinh tồn: Nhịp tim, huyết áp, nhịp thở, SpO2, ECG',
                    'Điều trị hỗ trợ: Nghỉ ngơi, trấn an, hỗ trợ hô hấp nếu cần',
                    'Điều chỉnh điện giải: Bổ sung kali nếu hạ kali máu',
                    'Điều trị loạn nhịp: Nếu có rối loạn nhịp tim nghiêm trọng, cân nhắc dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng',
                    'Điều trị co thắt phế quản nghịch lý: Ngừng salbutamol, dùng ipratropium hoặc corticosteroid'
                ],
                'monitoring': 'Theo dõi dấu hiệu sinh tồn, ECG, kali máu, đường huyết trong ít nhất 4-6 giờ.'
            },
            'reversal_agents': {
                'available': False,
                'agents': []
            },
            'administration_instructions': {
                'oral': {
                    'with_food': 'Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ.',
                    'timing': 'Uống 3-4 lần/ngày, cách đều. Lưu ý: Dạng uống có nhiều tác dụng phụ hơn dạng hít, nên ưu tiên dạng hít khi có thể.'
                },
                'iv': {
                    'reconstitution': 'Pha với NS hoặc D5W. Nồng độ pha: 1-5mcg/ml.',
                    'infusion_rate': 'Bolus: 5mcg/kg IV trong 1-2 phút. Truyền liên tục: 0.5-5mcg/kg/phút.',
                    'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],
                    'incompatibility': ['Không trộn với các thuốc khác trong cùng một ống truyền'],
                    'notes': 'Chỉ dùng IV trong cấp cứu hen nặng. Theo dõi chặt chẽ nhịp tim, huyết áp, ECG.'
                },
                'inhalation': {
                    'technique': 'MDI: Lắc kỹ, thở ra hết, đặt ống ngậm vào miệng, bắt đầu hít vào chậm và sâu, bấm thuốc, tiếp tục hít vào đến khi đầy phổi, giữ hơi 10 giây, thở ra chậm. Đợi 30-60 giây trước khi bấm lần thứ 2.',
                    'nebulizer': 'Pha 2.5-5mg trong 2-4ml NS hoặc nước cất. Thở bình thường qua mask hoặc ống ngậm. Thời gian: 5-15 phút. Rửa miệng sau khi dùng.'
                }
            },
            'references': {
                'primary_sources': [
                    'FDA Drug Label - Albuterol (Salbutamol)',
                    'GINA 2023 Guidelines - Global Initiative for Asthma',
                    'UpToDate - Albuterol: Drug Information',
                    'Medscape - Albuterol Drug Reference'
                ],
                'last_updated': '2024-12-19',
                'evidence_level': 'A - Dựa trên FDA drug labels, GINA guidelines'
            }
        }
    }
}

__all__ = ['SHORT_ACTING_BETA_2_AGONISTS_DRUGS']

