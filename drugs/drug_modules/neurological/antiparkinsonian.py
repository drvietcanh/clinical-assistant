"""
Antiparkinsonian Drugs
Drugs for Parkinson's disease and movement disorders
"""

ANTIPARKINSONIAN_DRUGS = {
    "Levodopa/Carbidopa": {
        "group": "Neurology - Antiparkinsonian (Dopamine Precursor + DOPA Decarboxylase Inhibitor)",
        "vietnamese_name": "Levodopa/Carbidopa, Sinemet",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease",
            "Parkinsonism (secondary)",
            "Restless legs syndrome - off-label"
        ],
        "contraindications": [
            "Dị ứng",
            "Glaucoma góc đóng",
            "Melanoma ác tính (hoặc tiền sử)",
            "Dùng với MAO inhibitors không chọn lọc (trong 14 ngày)",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_parkinson": "Bắt đầu: 25/100mg (levodopa/carbidopa) x 3 lần/ngày, tăng dần đến 25/250mg hoặc 50/200mg x 3-4 lần/ngày",
            "adult_max": "200/2000mg/ngày (levodopa/carbidopa)",
            "notes": "Levodopa là tiền chất dopamine, carbidopa ức chế DOPA decarboxylase ngoại biên. Dùng với thức ăn để giảm buồn nôn. Tránh protein cao (giảm hấp thu)."
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến khi bắt đầu)",
            "Chóng mặt",
            "Rối loạn vận động (dyskinesia) - phổ biến với dùng dài ngày",
            "Tác dụng dao động (wearing-off, on-off) - phổ biến với dùng dài ngày",
            "Ảo giác (đặc biệt ở người cao tuổi)",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Hạ huyết áp tư thế",
            "Rối loạn giấc ngủ",
            "Rối loạn hành vi (impulse control disorders) - hiếm"
        ],
        "interactions": [
            "MAO inhibitors không chọn lọc: CHỐNG CHỈ ĐỊNH - tăng nguy cơ tăng huyết áp nặng",
            "Protein cao: giảm hấp thu levodopa",
            "Pyridoxine (vitamin B6): giảm hiệu quả (nếu không có carbidopa)",
            "Antipsychotics: giảm hiệu quả (đối kháng dopamine)",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "Iron supplements: giảm hấp thu levodopa"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Levodopa là tiền chất dopamine, được chuyển hóa thành dopamine trong não bởi DOPA decarboxylase. Dopamine không thể qua hàng rào máu-não (blood-brain barrier), nhưng levodopa có thể. Carbidopa là DOPA decarboxylase inhibitor ngoại biên, ức chế chuyển hóa levodopa thành dopamine ở ngoại biên (giảm tác dụng phụ ngoại biên như buồn nôn, nôn) và tăng lượng levodopa đến não (tăng hiệu quả). Tác dụng: điều trị Parkinson's disease và parkinsonism. Tác dụng phụ: buồn nôn, nôn (phổ biến khi bắt đầu), rối loạn vận động (dyskinesia) - phổ biến với dùng dài ngày, tác dụng dao động (wearing-off, on-off) - phổ biến với dùng dài ngày, ảo giác (đặc biệt ở người cao tuổi).",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng Parkinson (run, cứng, chậm vận động), cải thiện chức năng vận động",
            "Rối loạn vận động (dyskinesia) - phổ biến với dùng dài ngày, có thể cần giảm liều",
            "Tác dụng dao động (wearing-off, on-off) - phổ biến với dùng dài ngày, có thể cần điều chỉnh liều hoặc thêm thuốc khác",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục",
            "Tương tác với MAO inhibitors (CHỐNG CHỈ ĐỊNH), protein cao, antipsychotics"
        ],
        "precautions": [
            "Buồn nôn, nôn - phổ biến khi bắt đầu, dùng với thức ăn, có thể dùng domperidone nếu cần",
            "Rối loạn vận động (dyskinesia) - phổ biến với dùng dài ngày, có thể cần giảm liều",
            "Tác dụng dao động (wearing-off, on-off) - phổ biến với dùng dài ngày, có thể cần điều chỉnh liều, thêm thuốc khác (COMT inhibitors, MAO-B inhibitors), hoặc dùng dạng extended release",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều hoặc thêm quetiapine/clozapine (atypical antipsychotics)",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors không chọn lọc (trong 14 ngày) - tăng nguy cơ tăng huyết áp nặng",
            "Tránh protein cao - giảm hấp thu levodopa, dùng levodopa 30-60 phút trước hoặc sau bữa ăn",
            "Tránh antipsychotics - giảm hiệu quả (đối kháng dopamine)",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Thận trọng khi dùng với iron supplements - giảm hấp thu levodopa, dùng cách nhau 2 giờ",
            "Dạng extended release - dùng cho tác dụng dao động, uống 1-2 lần/ngày, hấp thu chậm hơn"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (levodopa)",
            "onset": "30-60 phút (PO)",
            "duration": "3-5 giờ (PO), 4-6 giờ (extended release)",
            "protein_binding": "Minimal",
            "clearance": "Gan: chuyển hóa levodopa qua DOPA decarboxylase (ngoại biên và trung ương), COMT, MAO. Carbidopa ức chế DOPA decarboxylase ngoại biên. Thận: bài tiết một phần nguyên dạng và metabolites."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release: bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ rối loạn vận động (dyskinesia) với dùng dài ngày. Nguy cơ ảo giác, lú lẫn, đặc biệt ở người cao tuổi. Nguy cơ rối loạn hành vi (impulse control disorders).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors không chọn lọc (Phenelzine, Tranylcypromine)",
                    "mechanism": "Ức chế chuyển hóa dopamine qua MAO, tăng nồng độ dopamine, tăng nguy cơ tăng huyết áp nặng",
                    "effect": "Tăng huyết áp nặng, đau đầu, đột quỵ (nguy hiểm)",
                    "management": "CHỐNG CHỈ ĐỊNH - không được dùng cùng. Ngừng MAO inhibitors ít nhất 14 ngày trước khi dùng levodopa/carbidopa."
                },
                {
                    "drug": "Antipsychotics (Haloperidol, Risperidone, Olanzapine)",
                    "mechanism": "Đối kháng thụ thể dopamine D2, giảm hiệu quả levodopa",
                    "effect": "Giảm hiệu quả levodopa, tăng triệu chứng Parkinson",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc (ảo giác), dùng quetiapine hoặc clozapine (atypical antipsychotics ít đối kháng D2 hơn)."
                }
            ],
            "moderate": [
                {
                    "drug": "Protein cao",
                    "mechanism": "Cạnh tranh hấp thu với levodopa ở ruột",
                    "effect": "Giảm hấp thu levodopa, giảm hiệu quả",
                    "management": "Dùng levodopa 30-60 phút trước hoặc sau bữa ăn. Tránh bữa ăn giàu protein."
                },
                {
                    "drug": "Iron supplements",
                    "mechanism": "Giảm hấp thu levodopa ở ruột",
                    "effect": "Giảm hấp thu levodopa, giảm hiệu quả",
                    "management": "Dùng cách nhau 2 giờ. Tránh dùng cùng lúc."
                },
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng levodopa, carbidopa hoặc các thành phần khác",
                "Glaucoma góc đóng - tăng nhãn áp",
                "Melanoma ác tính (hoặc tiền sử) - levodopa có thể kích thích tăng trưởng melanoma",
                "Dùng với MAO inhibitors không chọn lọc (trong 14 ngày) - tăng nguy cơ tăng huyết áp nặng",
                "Suy tim nặng - tăng nguy cơ rối loạn nhịp tim"
            ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh tâm thần (ảo giác, lú lẫn) - tăng nguy cơ ảo giác, lú lẫn",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, ảo giác, lú lẫn, giảm liều 25-50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với antipsychotics - giảm hiệu quả",
                "Dùng với protein cao - giảm hấp thu levodopa",
                "Dùng với iron supplements - giảm hấp thu levodopa"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Levodopa và carbidopa bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "Thận trọng, giảm liều 25-50%, theo dõi tác dụng phụ chặt chẽ",
            "notes": "Levodopa và carbidopa chuyển hóa ở gan. Suy gan có thể ảnh hưởng đến chuyển hóa, nhưng ít tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: rối loạn vận động nặng (dyskinesia), ảo giác, lú lẫn, kích động",
                "Rối loạn tim mạch: tăng huyết áp (nếu dùng với MAO inhibitors), hạ huyết áp, rối loạn nhịp tim",
                "Rối loạn tiêu hóa: buồn nôn, nôn nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Có thể dùng pyridoxine (vitamin B6) để tăng chuyển hóa levodopa ngoại biên (giảm nồng độ levodopa đến não).",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Pyridoxine (vitamin B6): 50-100mg PO/IV để tăng chuyển hóa levodopa ngoại biên (giảm nồng độ levodopa đến não)",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí tăng huyết áp: nếu dùng với MAO inhibitors, dùng phentolamine hoặc nitroprusside",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Xử trí rối loạn vận động: giảm liều hoặc ngừng levodopa tạm thời",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp, rối loạn vận động"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Dùng với thức ăn để giảm buồn nôn, nôn. Tránh bữa ăn giàu protein (giảm hấp thu levodopa). Dùng levodopa 30-60 phút trước hoặc sau bữa ăn.",
                "timing": "Chia 3-4 lần/ngày. Uống cùng thời điểm mỗi ngày. Dạng extended release: uống 1-2 lần/ngày, hấp thu chậm hơn. KHÔNG nghiền hoặc nhai viên extended release (phải uống nguyên viên)."
            },
            "im": {
                "reconstitution": "Không có dạng IM",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Levodopa/Carbidopa",
                "UpToDate - Levodopa/Carbidopa: Drug information",
                "FDA - Sinemet (levodopa/carbidopa) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    "Pramipexole": {
        "group": "Neurology - Antiparkinsonian (Dopamine Agonist)",
        "vietnamese_name": "Pramipexole, Mirapex",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease",
            "Restless legs syndrome (RLS)"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_parkinson": "0.125mg x 3 lần/ngày, tăng dần mỗi 5-7 ngày đến 1.5mg x 3 lần/ngày (tối đa 4.5mg/ngày)",
            "adult_rls": "0.125mg trước khi ngủ, tăng dần đến 0.5mg trước khi ngủ (tối đa 0.5mg/ngày)",
            "adult_max": "4.5mg/ngày (Parkinson), 0.5mg/ngày (RLS)",
            "notes": "Dopamine agonist (D2, D3). Tác dụng dài. Tăng liều chậm để giảm tác dụng phụ. Dạng extended release: uống 1 lần/ngày."
        },
        "side_effects": [
            "Buồn nôn (phổ biến khi bắt đầu)",
            "Chóng mặt",
            "Buồn ngủ (phổ biến)",
            "Hạ huyết áp tư thế",
            "Ảo giác (đặc biệt ở người cao tuổi)",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Rối loạn hành vi (impulse control disorders) - hiếm: cờ bạc, mua sắm, tình dục",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm",
            "Rối loạn vận động (dyskinesia) - ít hơn levodopa"
        ],
        "interactions": [
            "Antipsychotics: giảm hiệu quả (đối kháng dopamine)",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "Cimetidine: tăng nồng độ pramipexole",
            "Quinidine: tăng nồng độ pramipexole"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Pramipexole là dopamine agonist, kích thích trực tiếp thụ thể dopamine D2 và D3 trong não. Khác với levodopa (tiền chất dopamine), pramipexole không cần chuyển hóa và có tác dụng dài hơn. Pramipexole ưu tiên kích thích thụ thể D3 (nhiều hơn D2), có thể giải thích tác dụng tốt hơn với các triệu chứng không vận động (non-motor symptoms) như trầm cảm, lo âu. Tác dụng: điều trị Parkinson's disease và restless legs syndrome (RLS). Có dạng immediate release (IR) và extended release (XR). Tác dụng phụ: buồn nôn (phổ biến khi bắt đầu), buồn ngủ (phổ biến), ảo giác (đặc biệt ở người cao tuổi), rối loạn hành vi (impulse control disorders) - hiếm, buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm.",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng Parkinson (run, cứng, chậm vận động), cải thiện chức năng vận động",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm, cảnh báo bệnh nhân",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục",
            "Tương tác với antipsychotics (giảm hiệu quả), antihypertensives, cimetidine, quinidine"
        ],
        "precautions": [
            "Buồn nôn - phổ biến khi bắt đầu, dùng với thức ăn, có thể dùng domperidone nếu cần",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm, cảnh báo bệnh nhân, tránh lái xe nếu có tiền sử",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều hoặc thêm quetiapine/clozapine (atypical antipsychotics)",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục, giảm liều hoặc ngừng nếu có",
            "Tránh antipsychotics - giảm hiệu quả (đối kháng dopamine)",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Thận trọng khi dùng với cimetidine hoặc quinidine - tăng nồng độ pramipexole, giảm liều pramipexole 25-50%",
            "Tăng liều chậm (mỗi 5-7 ngày) để giảm tác dụng phụ",
            "Dạng extended release (XR) - uống 1 lần/ngày, thuận tiện hơn, không nghiền hoặc nhai (phải uống nguyên viên)"
        ],
        "pharmacokinetics": {
            "half_life": "8-12 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "8-12 giờ (PO), 24 giờ (XR)",
            "protein_binding": "15%",
            "clearance": "Thận: bài tiết chủ yếu nguyên dạng (90%). Gan: chuyển hóa một phần. Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release (XR): bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ buồn ngủ đột ngột (sleep attacks) - có thể xảy ra mà không có dấu hiệu cảnh báo, nguy hiểm khi lái xe hoặc vận hành máy móc. Nguy cơ ảo giác, lú lẫn, đặc biệt ở người cao tuổi. Nguy cơ rối loạn hành vi (impulse control disorders).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antipsychotics (Haloperidol, Risperidone, Olanzapine)",
                    "mechanism": "Đối kháng thụ thể dopamine D2, giảm hiệu quả pramipexole",
                    "effect": "Giảm hiệu quả pramipexole, tăng triệu chứng Parkinson",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc (ảo giác), dùng quetiapine hoặc clozapine (atypical antipsychotics ít đối kháng D2 hơn)."
                }
            ],
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế thải trừ pramipexole qua thận, tăng nồng độ pramipexole",
                    "effect": "Tăng nồng độ pramipexole, tăng tác dụng phụ",
                    "management": "Giảm liều pramipexole 25-50% khi dùng với cimetidine. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Quinidine",
                    "mechanism": "Ức chế thải trừ pramipexole qua thận, tăng nồng độ pramipexole",
                    "effect": "Tăng nồng độ pramipexole, tăng tác dụng phụ",
                    "management": "Giảm liều pramipexole 25-50% khi dùng với quinidine. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng pramipexole hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Bệnh thận (CrCl <60) - giảm thải trừ, tăng nguy cơ tích lũy, giảm liều",
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh tâm thần (ảo giác, lú lẫn) - tăng nguy cơ ảo giác, lú lẫn",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, ảo giác, lú lẫn, giảm liều 25-50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với antipsychotics - giảm hiệu quả",
                "Dùng với cimetidine hoặc quinidine - giảm liều pramipexole"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Pramipexole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, theo dõi tác dụng phụ",
            "notes": "Pramipexole chuyển hóa một phần ở gan. Suy gan ít ảnh hưởng đến nồng độ pramipexole."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "under_30": "Giảm liều 50-75%, theo dõi tác dụng phụ chặt chẽ",
            "notes": "Pramipexole bài tiết chủ yếu qua thận (90% nguyên dạng). Suy thận làm giảm thải trừ, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, ảo giác, lú lẫn, kích động",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Xử trí nhịp chậm: Atropine nếu cần",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Dạng immediate release (IR): chia 3 lần/ngày. Dạng extended release (XR): uống 1 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm (mỗi 5-7 ngày) để giảm tác dụng phụ. KHÔNG nghiền hoặc nhai viên XR (phải uống nguyên viên)."
            },
            "im": {
                "reconstitution": "Không có dạng IM",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Pramipexole",
                "UpToDate - Pramipexole: Drug information",
                "FDA - Mirapex (pramipexole) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    "Ropinirole": {
        "group": "Neurology - Antiparkinsonian (Dopamine Agonist)",
        "vietnamese_name": "Ropinirole, Requip",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease",
            "Restless legs syndrome (RLS)"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_parkinson": "0.25mg x 3 lần/ngày, tăng dần mỗi 7 ngày đến 1-3mg x 3 lần/ngày (tối đa 24mg/ngày)",
            "adult_rls": "0.25mg trước khi ngủ, tăng dần đến 4mg trước khi ngủ (tối đa 4mg/ngày)",
            "adult_max": "24mg/ngày (Parkinson), 4mg/ngày (RLS)",
            "notes": "Dopamine agonist (D2, D3). Tác dụng trung bình. Tăng liều chậm để giảm tác dụng phụ. Dạng extended release: uống 1 lần/ngày."
        },
        "side_effects": [
            "Buồn nôn (phổ biến khi bắt đầu)",
            "Chóng mặt",
            "Buồn ngủ (phổ biến)",
            "Hạ huyết áp tư thế",
            "Ảo giác (đặc biệt ở người cao tuổi)",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Rối loạn hành vi (impulse control disorders) - hiếm: cờ bạc, mua sắm, tình dục",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm",
            "Rối loạn vận động (dyskinesia) - ít hơn levodopa"
        ],
        "interactions": [
            "Antipsychotics: giảm hiệu quả (đối kháng dopamine)",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "CYP1A2 inhibitors: tăng nồng độ ropinirole",
            "CYP1A2 inducers: giảm nồng độ ropinirole",
            "Estrogens: tăng nồng độ ropinirole"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ropinirole là dopamine agonist, kích thích trực tiếp thụ thể dopamine D2 và D3 trong não. Khác với levodopa (tiền chất dopamine), ropinirole không cần chuyển hóa và có tác dụng trung bình. Ropinirole ưu tiên kích thích thụ thể D3 (nhiều hơn D2), có thể giải thích tác dụng tốt hơn với các triệu chứng không vận động (non-motor symptoms) như trầm cảm, lo âu. Tác dụng: điều trị Parkinson's disease và restless legs syndrome (RLS). Có dạng immediate release (IR) và extended release (XR). Tác dụng phụ: buồn nôn (phổ biến khi bắt đầu), buồn ngủ (phổ biến), ảo giác (đặc biệt ở người cao tuổi), rối loạn hành vi (impulse control disorders) - hiếm, buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm.",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng Parkinson (run, cứng, chậm vận động), cải thiện chức năng vận động",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm, cảnh báo bệnh nhân",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục",
            "Tương tác với antipsychotics (giảm hiệu quả), antihypertensives, CYP1A2 inhibitors/inducers, estrogens"
        ],
        "precautions": [
            "Buồn nôn - phổ biến khi bắt đầu, dùng với thức ăn, có thể dùng domperidone nếu cần",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm, cảnh báo bệnh nhân, tránh lái xe nếu có tiền sử",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều hoặc thêm quetiapine/clozapine (atypical antipsychotics)",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục, giảm liều hoặc ngừng nếu có",
            "Tránh antipsychotics - giảm hiệu quả (đối kháng dopamine)",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Thận trọng khi dùng với CYP1A2 inhibitors (fluvoxamine, ciprofloxacin) - tăng nồng độ ropinirole, giảm liều ropinirole 50%",
            "Thận trọng khi dùng với CYP1A2 inducers (carbamazepine, smoking) - giảm nồng độ ropinirole, có thể cần tăng liều",
            "Thận trọng khi dùng với estrogens - tăng nồng độ ropinirole, giảm liều ropinirole 25-50%",
            "Tăng liều chậm (mỗi 7 ngày) để giảm tác dụng phụ",
            "Dạng extended release (XR) - uống 1 lần/ngày, thuận tiện hơn, không nghiền hoặc nhai (phải uống nguyên viên)"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "6-8 giờ (PO), 24 giờ (XR)",
            "protein_binding": "40%",
            "clearance": "Gan: chuyển hóa qua CYP1A2 (chính). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều khi dùng với CYP1A2 inhibitors/inducers và estrogens."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release (XR): bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ buồn ngủ đột ngột (sleep attacks) - có thể xảy ra mà không có dấu hiệu cảnh báo, nguy hiểm khi lái xe hoặc vận hành máy móc. Nguy cơ ảo giác, lú lẫn, đặc biệt ở người cao tuổi. Nguy cơ rối loạn hành vi (impulse control disorders).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antipsychotics (Haloperidol, Risperidone, Olanzapine)",
                    "mechanism": "Đối kháng thụ thể dopamine D2, giảm hiệu quả ropinirole",
                    "effect": "Giảm hiệu quả ropinirole, tăng triệu chứng Parkinson",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc (ảo giác), dùng quetiapine hoặc clozapine (atypical antipsychotics ít đối kháng D2 hơn)."
                },
                {
                    "drug": "CYP1A2 inhibitors (Fluvoxamine, Ciprofloxacin)",
                    "mechanism": "Ức chế chuyển hóa ropinirole qua CYP1A2, tăng nồng độ ropinirole",
                    "effect": "Tăng nồng độ ropinirole, tăng tác dụng phụ (buồn ngủ, ảo giác)",
                    "management": "Giảm liều ropinirole 50% khi dùng với CYP1A2 inhibitors. Theo dõi tác dụng phụ chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP1A2 inducers (Carbamazepine, Smoking)",
                    "mechanism": "Cảm ứng chuyển hóa ropinirole qua CYP1A2, giảm nồng độ ropinirole",
                    "effect": "Giảm nồng độ ropinirole, giảm hiệu quả",
                    "management": "Tăng liều ropinirole 50-100% khi dùng với carbamazepine hoặc ở người hút thuốc. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Estrogens",
                    "mechanism": "Ức chế chuyển hóa ropinirole, tăng nồng độ ropinirole",
                    "effect": "Tăng nồng độ ropinirole, tăng tác dụng phụ",
                    "management": "Giảm liều ropinirole 25-50% khi dùng với estrogens. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ropinirole hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy",
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh tâm thần (ảo giác, lú lẫn) - tăng nguy cơ ảo giác, lú lẫn",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, ảo giác, lú lẫn, giảm liều 25-50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với antipsychotics - giảm hiệu quả",
                "Dùng với CYP1A2 inhibitors - giảm liều ropinirole",
                "Dùng với CYP1A2 inducers hoặc hút thuốc - tăng liều ropinirole",
                "Dùng với estrogens - giảm liều ropinirole"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Ropinirole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "Giảm liều 25-50%, theo dõi tác dụng phụ chặt chẽ",
            "notes": "Ropinirole chuyển hóa ở gan qua CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, ảo giác, lú lẫn, kích động",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Xử trí nhịp chậm: Atropine nếu cần",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Dạng immediate release (IR): chia 3 lần/ngày. Dạng extended release (XR): uống 1 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm (mỗi 7 ngày) để giảm tác dụng phụ. KHÔNG nghiền hoặc nhai viên XR (phải uống nguyên viên)."
            },
            "im": {
                "reconstitution": "Không có dạng IM",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Ropinirole",
                "UpToDate - Ropinirole: Drug information",
                "FDA - Requip (ropinirole) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    }
}

__all__ = ['ANTIPARKINSONIAN_DRUGS']











