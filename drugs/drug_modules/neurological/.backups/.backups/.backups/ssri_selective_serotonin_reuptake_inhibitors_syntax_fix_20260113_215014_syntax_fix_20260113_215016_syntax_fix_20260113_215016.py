"""Neurological and Psychiatric Medications
Active module - contains all neurological and psychiatric drug data"""

# SSRI (Selective Serotonin Reuptake Inhibitor)s

SSRI_SELECTIVE_SEROTONIN_REUPTAKE_INHIBITORS_DRUGS = {
    "Fluoxetine": {'group': 'Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)',
',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        ',
        'vietnamese_name': 'Fluoxetine, Prozac', 'administration': ['PO'],
        'indications': ['Trầm cảm', 'Rối loạn lo âu',
        'Rối loạn ám ảnh cưỡng chế (OCD)', 'Bulimia'], 'contraindications': [
        'Dùng MAO inhibitor', 'Dị ứng'], 'dosage': {'adult_depression':
        '20mg x 1 lần/ngày, tăng đến 20-80mg/ngày', 'adult_ocd': '20-60mg/ngày',
        'notes':
        'Tác dụng kéo dài (half-life dài), ngừng 5 tuần trước MAO inhibitor'},
        'side_effects': ['Buồn nôn', 'Mất ngủ hoặc buồn ngủ',
        'Giảm ham muốn tình dục', 'Nhức đầu',
        'Hội chứng serotonin (với thuốc khác)'], 'interactions': [
        'MAO inhibitor: chống chỉ định (nguy cơ hội chứng serotonin)',
        'Tramadol: tăng nguy cơ co giật và hội chứng serotonin',
        'Warfarin: tăng tác dụng chống đông',
        'Triptans: tăng nguy cơ hội chứng serotonin'],
        'mechanism_of_action':
        'Fluoxetine là SSRI (Selective Serotonin Reuptake Inhibitor) ức chế tái hấp thu serotonin ở synap thần kinh, tăng nồng độ serotonin trong khe synap. Tăng serotonin dẫn đến điều chỉnh thụ thể serotonin (desensitization) và tác dụng chống trầm cảm. Có tính chọn lọc cao với serotonin (ít ảnh hưởng đến norepinephrine, dopamine, hoặc các thụ thể khác). Ưu điểm: half-life dài (cả thuốc và chất chuyển hóa norfluoxetine), ít tác dụng phụ cholinergic và tim mạch hơn TCA. Tác dụng kéo dài sau khi ngừng thuốc'
        , 'monitoring': [
        'Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)',
        'Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)',
        'Dấu hiệu hội chứng serotonin: kích động, nhịp tim nhanh, tăng huyết áp, sốt, co giật (nếu dùng với thuốc khác)'
        , 'INR nếu dùng với warfarin (tăng nguy cơ chảy máu)',
        'Chức năng gan nếu có triệu chứng (hiếm)',
        'Dấu hiệu rút thuốc khi ngừng (chóng mặt, buồn nôn, kích động)'],
        'precautions': [
        'KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối - nguy cơ hội chứng serotonin nghiêm trọng)'
        ,
        'Ngừng fluoxetine ít nhất 5 tuần trước khi bắt đầu MAO inhibitor (do half-life dài)'
        ,
        'Theo dõi sát dấu hiệu tự tử trong vài tuần đầu (tăng nguy cơ ở <24 tuổi)',
        'Giảm liều dần khi ngừng (tránh hội chứng rút thuốc)',
        'Thận trọng khi dùng với tramadol, triptans (tăng nguy cơ hội chứng serotonin)'
        ,
        'Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu - theo dõi INR)',
        'Có thể gây mất ngủ → dùng buổi sáng',
        'Có thể gây buồn ngủ → dùng buổi tối (tùy bệnh nhân)',
        'Tác dụng kéo dài do half-life dài (cả thuốc và norfluoxetine)'],
        'pharmacokinetics': {'half_life':
        '1-4 ngày (rất dài, cả fluoxetine và norfluoxetine)', 'onset':
        '2-4 tuần (tác dụng chống trầm cảm)', 'duration':
        'Rất dài (do half-life dài)', 'protein_binding': '94-95% (rất cao)',
        'clearance':
        'Gan (chuyển hóa qua CYP2D6, CYP2C9, CYP3A4 thành norfluoxetine - chất hoạt động với half-life dài hơn)'
        }, 'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm',
        'black_box_warnings':
        'Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Chống chỉ định với MAO inhibitor - nguy cơ hội chứng serotonin nghiêm trọng'
        , 'drug_interactions': {
            'major': [
                {'drug': 'MAO inhibitors (phenelzine, tranylcypromine, selegiline, linezolid)',
                 'mechanism': 'Ức chế chuyển hóa serotonin, tăng nồng độ serotonin',
                 'effect': 'Hội chứng serotonin nghiêm trọng: kích động, nhịp tim nhanh, tăng huyết áp, sốt cao, co giật, tử vong',
                 'management': 'CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng fluoxetine ít nhất 5 tuần trước khi bắt đầu MAO inhibitor (do half-life dài).'},
                {'drug': 'Tramadol',
                 'mechanism': 'Tăng nồng độ serotonin, tăng nguy cơ co giật',
                 'effect': 'Hội chứng serotonin, tăng nguy cơ co giật',
                 'management': 'Tránh dùng cùng. Nếu bắt buộc, giảm liều tramadol và theo dõi sát.'},
                {'drug': 'Triptans (sumatriptan, rizatriptan)',
                 'mechanism': 'Tăng nồng độ serotonin',
                 'effect': 'Hội chứng serotonin',
                 'management': 'Thận trọng. Dùng cách xa ít nhất 24 giờ. Theo dõi dấu hiệu hội chứng serotonin.'}
            ],
            'moderate': [
                {'drug': 'Warfarin',
                 'mechanism': 'Fluoxetine ức chế CYP2C9, tăng nồng độ warfarin',
                 'effect': 'Tăng INR, tăng nguy cơ chảy máu',
                 'management': 'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'},
                {'drug': 'Phenytoin, Carbamazepine',
                 'mechanism': 'Fluoxetine ức chế CYP2D6, CYP2C9, tăng nồng độ',
                 'effect': 'Tăng nồng độ phenytoin/carbamazepine, tăng nguy cơ độc tính',
                 'management': 'Theo dõi nồng độ. Giảm liều phenytoin/carbamazepine nếu cần.'},
                {'drug': 'Tricyclic antidepressants (TCA)',
                 'mechanism': 'Ức chế CYP2D6, tăng nồng độ TCA',
                 'effect': 'Tăng nồng độ TCA, tăng nguy cơ độc tính (rối loạn nhịp, block nhĩ thất)',
                 'management': 'Thận trọng. Giảm liều TCA 50%. Theo dõi ECG.'}
            ],
            'minor': [
                {'drug': 'CYP2D6 substrates (codeine, metoprolol)',
                 'mechanism': 'Ức chế CYP2D6',
                 'effect': 'Tăng nồng độ các thuốc chuyển hóa qua CYP2D6',
                 'management': 'Thận trọng. Điều chỉnh liều nếu cần.'}
            ]
        }, 'contraindications': {
        'tuyệt_đối': ['Dùng MAO inhibitor (chống chỉ định tuyệt đối)',
        'Dị ứng fluoxetine', 'Hội chứng serotonin đang diễn ra'], 'tương_đối':
        ['Suy gan nặng - giảm liều', 'Suy thận nặng (CrCl <30) - giảm liều',
        'Trẻ em <18 tuổi - tăng nguy cơ tự tử',
        'Có ý định tự tử - chỉ kê đơn số lượng ít', 'Bệnh tim - thận trọng',
        'Rối loạn đông máu - tăng nguy cơ chảy máu',
        'Dùng với tramadol, triptans - tăng nguy cơ hội chứng serotonin']},
        'contraindications_detail': {
        'tuyệt_đối': ['Dùng MAO inhibitor (chống chỉ định tuyệt đối)',
        'Dị ứng fluoxetine', 'Hội chứng serotonin đang diễn ra'], 'tương_đối':
        ['Suy gan nặng - giảm liều', 'Suy thận nặng (CrCl <30) - giảm liều',
        'Trẻ em <18 tuổi - tăng nguy cơ tự tử',
        'Có ý định tự tử - chỉ kê đơn số lượng ít', 'Bệnh tim - thận trọng',
        'Rối loạn đông máu - tăng nguy cơ chảy máu',
        'Dùng với tramadol, triptans - tăng nguy cơ hội chứng serotonin']},
        'renal_adjustment': {'normal': 'Không cần chỉnh liều', '30_60': 'Thận trọng, có thể cần giảm liều',
        'under_30': 'Giảm liều 25-50%', 'dialysis': 'Thận trọng, giảm liều. Fluoxetine không được lọc sạch hiệu quả qua thẩm phân máu.',
        'notes': 'Fluoxetine chuyển hóa chủ yếu ở gan. Suy thận có thể ảnh hưởng nhẹ đến thải trừ. Giảm liều ở suy thận nặng.'},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Một số nghiên cứu gợi ý tăng nguy cơ dị tật thai nhi (dị tật tim, dị tật chi) khi dùng trong 3 tháng đầu, nhưng chứng cứ không rõ ràng. Có thể gây tăng huyết áp phổi ở trẻ sơ sinh (PPHN) - nguy cơ thấp. Có thể gây hội chứng cai ở trẻ sơ sinh (kích động, khó thở, run) nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Fluoxetine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ bú mẹ thường <10% nồng độ mẹ. Có thể gây buồn ngủ, bú kém, quấy khóc ở trẻ. Ít báo cáo về tác dụng phụ nghiêm trọng.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, quấy khóc ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc chuyển sang SSRI khác (sertraline).'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ', 'notes':
        'Fluoxetine chuyển hóa ở gan qua CYP2D6, CYP2C9, CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan trực tiếp.'
        }, 'overdose_management': {'symptoms': ['Buồn nôn, nôn',
        'Kích động, lú lẫn', 'Nhịp tim nhanh', 'Tăng huyết áp', 'Sốt',
        'Co giật', 'Hôn mê', 'Hội chứng serotonin (nếu dùng với thuốc khác)'],
        'antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment':
        ['Hỗ trợ hô hấp và tuần hoàn nếu cần',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi ECG, huyết áp, nhịp tim',
        'Điều trị hội chứng serotonin: Cyproheptadine (4-8mg PO/IV), benzodiazepines cho co giật'
        , 'Điều trị co giật: Benzodiazepines (lorazepam, diazepam)',
        'Điều trị tăng huyết áp: Esmolol, labetalol', 'Hạ nhiệt nếu sốt',
        'Truyền dịch', 'Theo dõi ít nhất 24-48 giờ (do half-life dài)'],
        'monitoring':
        'ECG, huyết áp, nhịp tim, nhiệt độ, ý thức, dấu hiệu co giật, điện giải'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Theo dõi ít nhất 24-48 giờ do half-life dài.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn'
        , 'timing':
        'Dùng 1 lần/ngày (buổi sáng hoặc tối tùy tác dụng phụ). Nếu gây mất ngủ → dùng buổi sáng. Nếu gây buồn ngủ → dùng buổi tối.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [],
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Prozac (fluoxetine)',
        'UpToDate - Fluoxetine: Drug information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'American Psychiatric Association guidelines'], 'last_updated':
        '2024-12-19', "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    }
}

__all__ = ['SSRI_SELECTIVE_SEROTONIN_REUPTAKE_INHIBITORS_DRUGS']
