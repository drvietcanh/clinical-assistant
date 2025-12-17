"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# Antihistamine (H1 Antagonist, 1st generation)s

ANTIHISTAMINE_H1_ANTAGONIST_1ST_GENERATIONS_DRUGS = {
    "Diphenhydramine": {
        'group': 'Allergy - Antihistamine (H1 Antagonist, 1st generation)',
        'vietnamese_name': 'Diphenhydramine, Benadryl',
        'administration': ['PO', 'IV', 'IM'],
        'indications': [
            'Dị ứng (allergic rhinitis)',
            'Mề đay (urticaria)',
            'Dị ứng da',
            'Say tàu xe (motion sickness)',
            'Mất ngủ (insomnia)',
            'Ho do dị ứng',
            'Phản ứng dị ứng cấp tính (IV/IM)'
        ],
        'contraindications': [
            'Dị ứng diphenhydramine',
            'Glaucoma góc đóng',
            'Bí tiểu do tắc nghẽn',
            'Trẻ sơ sinh (<6 tháng)'
        ],
        'dosage': {
            'adult_standard': '25-50mg x 3-4 lần/ngày (PO)',
            'adult_max': '50mg x 4 lần/ngày',
            'adult_insomnia': '25-50mg trước khi ngủ',
            'adult_iv_im': '10-50mg IV/IM (phản ứng dị ứng cấp)',
            'pediatric': '5mg/kg/ngày chia 3-4 lần (tối đa 300mg/ngày)',
            'pediatric_6_12': '12.5-25mg x 3-4 lần/ngày',
            'notes': 'Sedating, gây buồn ngủ - thận trọng khi lái xe'
        },
        'side_effects': [
            'Buồn ngủ (rất phổ biến)',
            'Khô miệng',
            'Chóng mặt',
            'Nhìn mờ',
            'Bí tiểu',
            'Táo bón',
            'Tim đập nhanh (hiếm)',
            'Hạ huyết áp (IV)',
            'Kích động nghịch lý ở trẻ em'
        ],
        'interactions': [
            'Alcohol: tăng buồn ngủ, suy hô hấp',
            'Benzodiazepines: tăng ức chế hệ thần kinh trung ương',
            'Opioids: tăng ức chế hệ thần kinh trung ương',
            'MAOIs: tăng tác dụng anticholinergic',
            'Anticholinergics khác: tăng tác dụng phụ'
        ],
        'pregnancy': 'B',
        'mechanism_of_action': 'Diphenhydramine là antihistamine thế hệ thứ nhất, đối kháng không chọn lọc với thụ thể H1 ở cả ngoại biên và trung ương. Khác với antihistamine thế hệ thứ hai, diphenhydramine dễ dàng qua hàng rào máu-não nên gây buồn ngủ mạnh và có tác dụng anticholinergic (kháng muscarinic). Diphenhydramine ức chế phóng thích histamine từ mast cells và basophils, ngăn chặn tác dụng của histamine trên các thụ thể H1. Tác dụng anticholinergic làm giảm tiết dịch, giảm co thắt cơ trơn, nhưng cũng gây khô miệng, nhìn mờ, bí tiểu. Tác dụng ức chế hệ thần kinh trung ương gây buồn ngủ, được sử dụng để điều trị mất ngủ. Diphenhydramine cũng có tác dụng chống say tàu xe do ức chế trung tâm nôn ở hành não.',
        'monitoring': [
            'Dấu hiệu buồn ngủ quá mức (đặc biệt khi lái xe hoặc vận hành máy móc)',
            'Dấu hiệu anticholinergic: khô miệng, nhìn mờ, bí tiểu, táo bón',
            'Huyết áp (đặc biệt khi dùng IV)',
            'Nhịp tim (có thể tăng nhịp tim)',
            'Dấu hiệu kích động nghịch lý ở trẻ em',
            'Đáp ứng điều trị (giảm triệu chứng dị ứng)'
        ],
        'precautions': [
            'Gây buồn ngủ mạnh - KHÔNG lái xe hoặc vận hành máy móc sau khi dùng',
            'Tác dụng anticholinergic - thận trọng với bệnh nhân glaucoma góc đóng, bí tiểu, tăng nhãn áp',
            'Thận trọng với người cao tuổi - tăng nguy cơ té ngã, lú lẫn, bí tiểu',
            'Tránh dùng với alcohol, benzodiazepines, opioids (tăng ức chế hệ thần kinh trung ương)',
            'Có thể gây kích động nghịch lý ở trẻ em (thay vì buồn ngủ)',
            'Dùng IV/IM cho phản ứng dị ứng cấp tính - theo dõi huyết áp',
            'Không dùng cho trẻ sơ sinh <6 tháng tuổi',
            'Có thể dùng để điều trị mất ngủ (liều 25-50mg trước khi ngủ) nhưng không phải lựa chọn đầu tiên'
        ],
        'pharmacokinetics': {
            'half_life': '2-8 giờ',
            'onset': '15-30 phút (PO), 5-10 phút (IV/IM)',
            'duration': '4-6 giờ',
            'protein_binding': '98-99%',
            'clearance': 'Gan: chuyển hóa qua CYP2D6, CYP1A2, CYP2C9 thành các metabolites không hoạt động. Thận: bài tiết một phần nguyên dạng và metabolites.'
        },
        'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng syrup: bảo quản ở nhiệt độ phòng, đậy kín sau khi dùng. Dạng IV/IM: bảo quản ở nhiệt độ phòng, tránh đông lạnh.',
        'black_box_warnings': None,
        'drug_interactions': {
            'major': [
                {
                    'drug': 'Alcohol',
                    'mechanism': 'Cả hai đều ức chế hệ thần kinh trung ương, tác dụng cộng dồn',
                    'effect': 'Tăng buồn ngủ, suy hô hấp, nguy cơ tử vong',
                    'management': 'TRÁNH dùng với rượu. Cảnh báo bệnh nhân về nguy cơ nghiêm trọng.'
                },
                {
                    'drug': 'Benzodiazepines, Opioids',
                    'mechanism': 'Cả hai đều ức chế hệ thần kinh trung ương',
                    'effect': 'Tăng ức chế hệ thần kinh trung ương, suy hô hấp',
                    'management': 'Thận trọng. Giảm liều nếu cần. Theo dõi hô hấp.'
                }
            ],
            'moderate': [
                {
                    'drug': 'MAOIs',
                    'mechanism': 'Tăng tác dụng anticholinergic',
                    'effect': 'Tăng tác dụng phụ anticholinergic (khô miệng, bí tiểu, nhìn mờ)',
                    'management': 'Thận trọng. Theo dõi tác dụng phụ.'
                },
                {
                    'drug': 'Anticholinergics khác (atropine, scopolamine)',
                    'mechanism': 'Tác dụng cộng dồn anticholinergic',
                    'effect': 'Tăng tác dụng phụ anticholinergic',
                    'management': 'Thận trọng. Theo dõi tác dụng phụ.'
                }
            ],
            'minor': []
        },
        'contraindications': {
            'tuyệt_đối': [
                'Dị ứng diphenhydramine',
                'Glaucoma góc đóng',
                'Bí tiểu do tắc nghẽn',
                'Trẻ sơ sinh <6 tháng tuổi'
            ],
            'tương_đối': [
                'Người cao tuổi - tăng nguy cơ té ngã, lú lẫn, bí tiểu',
                'Bệnh nhân có tiền sử bí tiểu - tăng nguy cơ',
                'Bệnh nhân có tiền sử glaucoma - thận trọng',
                'Bệnh nhân có bệnh tim mạch - có thể tăng nhịp tim',
                'Phụ nữ có thai - category B, thận trọng',
                'Trẻ em - có thể gây kích động nghịch lý'
            ]
        },
        'pregnancy_lactation': {
            'fda_category': 'B',
            'pregnancy_details': 'An toàn trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng ở tất cả các tam cá nguyệt nếu cần thiết. Tuy nhiên, nên cân nhắc dùng antihistamine thế hệ thứ hai (loratadine, cetirizine) nếu có thể vì ít tác dụng phụ hơn.',
            'lactation': {
                'safety': 'Compatible',
                'details': 'Diphenhydramine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây buồn ngủ ở trẻ bú mẹ. Thận trọng khi dùng.',
                'recommendation': 'Có thể dùng khi cho con bú nhưng thận trọng. Theo dõi dấu hiệu buồn ngủ ở trẻ. Cân nhắc dùng antihistamine thế hệ thứ hai nếu có thể.'
            }
        },
        'hepatic_adjustment': {
            'mild': 'Không đổi',
            'moderate': 'Thận trọng, có thể giảm liều nhẹ',
            'severe': 'Thận trọng, giảm liều hoặc tránh dùng',
            'notes': 'Diphenhydramine chuyển hóa ở gan qua CYP2D6, CYP1A2, CYP2C9. Suy gan có thể làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.'
        },
        'overdose_management': {
            'symptoms': [
                'Buồn ngủ nặng, hôn mê',
                'Kích động, lú lẫn, ảo giác',
                'Co giật (hiếm)',
                'Tim đập nhanh, loạn nhịp tim',
                'Hạ huyết áp',
                'Suy hô hấp',
                'Tăng thân nhiệt',
                'Bí tiểu, nhìn mờ, khô miệng nặng'
            ],
            'antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ.',
            'treatment': [
                'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
                'Than hoạt tính nếu uống trong vòng 1-2 giờ',
                'Hỗ trợ hô hấp (intubation nếu cần)',
                'Theo dõi ý thức, huyết áp, nhịp tim, hô hấp',
                'Điều trị co giật nếu có (benzodiazepines)',
                'Điều trị loạn nhịp tim nếu có',
                'Truyền dịch nếu hạ huyết áp',
                'Theo dõi ít nhất 24 giờ (half-life 2-8 giờ)'
            ],
            'monitoring': 'Ý thức, huyết áp, nhịp tim, hô hấp, thân nhiệt, điện tâm đồ'
        },
        'reversal_agents': {
            'available': False,
            'agents': []
        },
        'administration_instructions': {
            'oral': {
                'with_food': 'Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.',
                'timing': 'Dùng 3-4 lần/ngày tùy chỉ định. Dùng trước khi ngủ nếu dùng để điều trị mất ngủ. KHÔNG lái xe sau khi dùng.'
            },
            'iv': {
                'reconstitution': 'Dùng trực tiếp từ lọ, không cần pha loãng',
                'infusion_rate': 'Tiêm tĩnh mạch chậm (10-50mg trong 1-2 phút)',
                'compatibility': ['NS', 'D5W'],
                'incompatibility': [],
                'notes': 'Dùng cho phản ứng dị ứng cấp tính. Theo dõi huyết áp trong khi tiêm.'
            },
            'im': {
                'reconstitution': 'Dùng trực tiếp từ lọ',
                'injection_site': 'Tiêm bắp sâu',
                'notes': 'Dùng cho phản ứng dị ứng cấp tính nếu không có đường IV.'
            }
        },
        'references': {
            'primary_sources': [
                'FDA Drug Label - Benadryl (diphenhydramine)',
                'UpToDate - Diphenhydramine: Drug information',
                'Allergy & Clinical Immunology guidelines'
            ],
            'last_updated': '2025-02-05',
            'evidence_level': 'High - Multiple RCTs and systematic reviews'
        }
    },
    "Chlorpheniramine": {
        'group': 'Allergy - Antihistamine (H1 Antagonist, 1st generation)',
        'vietnamese_name': 'Chlorpheniramine, Chlor-Trimeton',
        'administration': ['PO', 'IV', 'IM'],
        'indications': [
            'Dị ứng (allergic rhinitis)',
            'Mề đay (urticaria)',
            'Dị ứng da',
            'Dị ứng mắt',
            'Phản ứng dị ứng cấp tính (IV/IM)'
        ],
        'contraindications': [
            'Dị ứng chlorpheniramine',
            'Glaucoma góc đóng',
            'Bí tiểu do tắc nghẽn',
            'Trẻ sơ sinh (<1 tháng)'
        ],
        'dosage': {
            'adult_standard': '4mg x 3-4 lần/ngày (PO)',
            'adult_max': '24mg/ngày',
            'adult_iv_im': '10-20mg IV/IM (phản ứng dị ứng cấp)',
            'pediatric': '0.35mg/kg/ngày chia 3-4 lần',
            'pediatric_6_12': '2-4mg x 3-4 lần/ngày',
            'pediatric_2_6': '1-2mg x 3-4 lần/ngày',
            'notes': 'Sedating nhưng ít hơn diphenhydramine'
        },
        'side_effects': [
            'Buồn ngủ (phổ biến nhưng ít hơn diphenhydramine)',
            'Khô miệng',
            'Chóng mặt',
            'Nhìn mờ',
            'Bí tiểu',
            'Táo bón',
            'Tim đập nhanh (hiếm)',
            'Hạ huyết áp (IV)'
        ],
        'interactions': [
            'Alcohol: tăng buồn ngủ',
            'Benzodiazepines: tăng ức chế hệ thần kinh trung ương',
            'Opioids: tăng ức chế hệ thần kinh trung ương',
            'MAOIs: tăng tác dụng anticholinergic',
            'Anticholinergics khác: tăng tác dụng phụ'
        ],
        'pregnancy': 'B',
        'mechanism_of_action': 'Chlorpheniramine là antihistamine thế hệ thứ nhất, đối kháng không chọn lọc với thụ thể H1 ở cả ngoại biên và trung ương. Chlorpheniramine qua hàng rào máu-não nên gây buồn ngủ, nhưng ít hơn so với diphenhydramine. Chlorpheniramine có tác dụng anticholinergic (kháng muscarinic) nhưng ít hơn diphenhydramine. Chlorpheniramine ức chế phóng thích histamine từ mast cells và basophils, ngăn chặn tác dụng của histamine trên các thụ thể H1. Tác dụng anticholinergic làm giảm tiết dịch, giảm co thắt cơ trơn. Chlorpheniramine được sử dụng rộng rãi ở Việt Nam do giá rẻ và hiệu quả tốt cho các triệu chứng dị ứng.',
        'monitoring': [
            'Dấu hiệu buồn ngủ (đặc biệt khi lái xe hoặc vận hành máy móc)',
            'Dấu hiệu anticholinergic: khô miệng, nhìn mờ, bí tiểu, táo bón',
            'Huyết áp (đặc biệt khi dùng IV)',
            'Nhịp tim',
            'Đáp ứng điều trị (giảm triệu chứng dị ứng)'
        ],
        'precautions': [
            'Gây buồn ngủ - thận trọng khi lái xe hoặc vận hành máy móc',
            'Tác dụng anticholinergic - thận trọng với bệnh nhân glaucoma góc đóng, bí tiểu',
            'Thận trọng với người cao tuổi - tăng nguy cơ té ngã, lú lẫn',
            'Tránh dùng với alcohol, benzodiazepines, opioids',
            'Không dùng cho trẻ sơ sinh <1 tháng tuổi',
            'Dùng IV/IM cho phản ứng dị ứng cấp tính - theo dõi huyết áp',
            'Giá rẻ, hiệu quả tốt, phù hợp cho bệnh nhân không cần tỉnh táo hoàn toàn'
        ],
        'pharmacokinetics': {
            'half_life': '20-24 giờ',
            'onset': '15-30 phút (PO), 5-10 phút (IV/IM)',
            'duration': '4-6 giờ',
            'protein_binding': '72%',
            'clearance': 'Gan: chuyển hóa qua CYP2D6 thành desmethylchlorpheniramine (metabolite hoạt động). Thận: bài tiết một phần nguyên dạng và metabolites.'
        },
        'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng syrup: bảo quản ở nhiệt độ phòng, đậy kín sau khi dùng. Dạng IV/IM: bảo quản ở nhiệt độ phòng, tránh đông lạnh.',
        'black_box_warnings': None,
        'drug_interactions': {
            'major': [
                {
                    'drug': 'Alcohol, Benzodiazepines, Opioids',
                    'mechanism': 'Cả hai đều ức chế hệ thần kinh trung ương',
                    'effect': 'Tăng ức chế hệ thần kinh trung ương, suy hô hấp',
                    'management': 'Thận trọng. Tránh dùng với rượu. Giảm liều nếu cần.'
                }
            ],
            'moderate': [
                {
                    'drug': 'MAOIs, Anticholinergics khác',
                    'mechanism': 'Tăng tác dụng anticholinergic',
                    'effect': 'Tăng tác dụng phụ anticholinergic',
                    'management': 'Thận trọng. Theo dõi tác dụng phụ.'
                }
            ],
            'minor': []
        },
        'contraindications': {
            'tuyệt_đối': [
                'Dị ứng chlorpheniramine',
                'Glaucoma góc đóng',
                'Bí tiểu do tắc nghẽn',
                'Trẻ sơ sinh <1 tháng tuổi'
            ],
            'tương_đối': [
                'Người cao tuổi - tăng nguy cơ té ngã, lú lẫn',
                'Bệnh nhân có tiền sử bí tiểu - tăng nguy cơ',
                'Bệnh nhân có tiền sử glaucoma - thận trọng',
                'Phụ nữ có thai - category B, thận trọng'
            ]
        },
        'pregnancy_lactation': {
            'fda_category': 'B',
            'pregnancy_details': 'An toàn trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng ở tất cả các tam cá nguyệt nếu cần thiết.',
            'lactation': {
                'safety': 'Compatible',
                'details': 'Chlorpheniramine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây buồn ngủ nhẹ ở trẻ bú mẹ.',
                'recommendation': 'Có thể dùng khi cho con bú. Theo dõi dấu hiệu buồn ngủ ở trẻ.'
            }
        },
        'hepatic_adjustment': {
            'mild': 'Không đổi',
            'moderate': 'Thận trọng, có thể giảm liều nhẹ',
            'severe': 'Thận trọng, giảm liều hoặc tránh dùng',
            'notes': 'Chlorpheniramine chuyển hóa ở gan qua CYP2D6. Suy gan có thể làm giảm chuyển hóa, tăng nguy cơ tích lũy.'
        },
        'overdose_management': {
            'symptoms': [
                'Buồn ngủ nặng, hôn mê',
                'Kích động, lú lẫn',
                'Tim đập nhanh',
                'Hạ huyết áp',
                'Suy hô hấp',
                'Bí tiểu, nhìn mờ, khô miệng nặng'
            ],
            'antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ.',
            'treatment': [
                'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
                'Than hoạt tính nếu uống trong vòng 1-2 giờ',
                'Hỗ trợ hô hấp nếu cần',
                'Theo dõi ý thức, huyết áp, nhịp tim, hô hấp',
                'Truyền dịch nếu hạ huyết áp',
                'Theo dõi ít nhất 24-48 giờ (half-life 20-24 giờ)'
            ],
            'monitoring': 'Ý thức, huyết áp, nhịp tim, hô hấp'
        },
        'reversal_agents': {
            'available': False,
            'agents': []
        },
        'administration_instructions': {
            'oral': {
                'with_food': 'Có thể dùng với hoặc không có thức ăn.',
                'timing': 'Dùng 3-4 lần/ngày. Thận trọng khi lái xe sau khi dùng.'
            },
            'iv': {
                'reconstitution': 'Dùng trực tiếp từ lọ, không cần pha loãng',
                'infusion_rate': 'Tiêm tĩnh mạch chậm (10-20mg trong 1-2 phút)',
                'compatibility': ['NS', 'D5W'],
                'incompatibility': [],
                'notes': 'Dùng cho phản ứng dị ứng cấp tính. Theo dõi huyết áp.'
            },
            'im': {
                'reconstitution': 'Dùng trực tiếp từ lọ',
                'injection_site': 'Tiêm bắp sâu',
                'notes': 'Dùng cho phản ứng dị ứng cấp tính nếu không có đường IV.'
            }
        },
        'references': {
            'primary_sources': [
                'FDA Drug Label - Chlor-Trimeton (chlorpheniramine)',
                'UpToDate - Chlorpheniramine: Drug information',
                'Allergy & Clinical Immunology guidelines'
            ],
            'last_updated': '2025-02-05',
            'evidence_level': 'High - Multiple RCTs and systematic reviews'
        }
    }
}

__all__ = ['ANTIHISTAMINE_H1_ANTAGONIST_1ST_GENERATIONS_DRUGS']






















