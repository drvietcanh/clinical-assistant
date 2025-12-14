"""
Benzodiazepines
Anxiolytics, sedatives, anticonvulsants
"""

BENZODIAZEPINES_DRUGS = {
    "Diazepam": {
        "group": "Neurology - Benzodiazepine",
        "vietnamese_name": "Diazepam, Valium",
        "administration": ["PO", "IM", "IV", "Rectal"],
        "indications": [
            "Lo âu",
            "Co giật (status epilepticus)",
            "Giãn cơ (spasticity)",
            "An thần trước phẫu thuật",
            "Cai rượu (alcohol withdrawal)",
            "Cai benzodiazepine (tapering)"
        ],
        "contraindications": [
            "Dị ứng",
            "Myasthenia gravis nặng",
            "Glaucoma góc đóng",
            "Suy hô hấp nặng",
            "Ức chế hệ thần kinh trung ương nặng"
        ],
        "dosage": {
            "adult_anxiety_po": "2-10mg x 2-4 lần/ngày",
            "adult_seizure_iv": "5-10mg IV, lặp mỗi 10-15 phút nếu cần (tối đa 30mg)",
            "adult_seizure_rectal": "10-20mg rectal, lặp sau 4-12 giờ nếu cần",
            "adult_muscle_spasm": "2-10mg x 3-4 lần/ngày",
            "adult_alcohol_withdrawal": "10mg x 3-4 lần/ngày, giảm dần",
            "adult_max": "40mg/ngày PO",
            "notes": "Benzodiazepine tác dụng dài (half-life 20-50 giờ). Tích lũy ở người cao tuổi. Có thể gây phụ thuộc."
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Suy hô hấp (nguy hiểm, đặc biệt khi dùng IV)",
            "Phụ thuộc, nghiện (với dùng dài ngày)",
            "Tăng nguy cơ té ngã (đặc biệt ở người cao tuổi)",
            "Amnesia (mất trí nhớ)",
            "Paradoxical reactions (kích động, hung hăng) - hiếm"
        ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Opioids: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp (nguy hiểm)",
            "CYP3A4 inhibitors: tăng nồng độ diazepam",
            "CYP3A4 inducers: giảm nồng độ diazepam",
            "Cimetidine: tăng nồng độ diazepam"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Diazepam là benzodiazepine tác dụng dài, tăng cường tác dụng của GABA (gamma-aminobutyric acid) - chất dẫn truyền thần kinh ức chế chính trong não. Diazepam gắn với thụ thể benzodiazepine (BZ1, BZ2) trên phức hợp GABA-A receptor, làm tăng tần suất mở kênh chloride, tăng dòng chloride vào tế bào, gây siêu phân cực và ức chế tế bào thần kinh. Tác dụng: an thần, giảm lo âu, chống co giật, giãn cơ, và gây quên. Có dạng uống (PO), tiêm bắp (IM), tiêm tĩnh mạch (IV), và đặt hậu môn (rectal). Half-life dài (20-50 giờ), tích lũy ở người cao tuổi. Tác dụng phụ: buồn ngủ, chóng mặt, lú lẫn, suy hô hấp (nguy hiểm), phụ thuộc, nghiện.",
        "monitoring": [
            "Đáp ứng điều trị: giảm lo âu, giảm co giật, giảm co cứng cơ",
            "Dấu hiệu suy hô hấp: thở chậm, thở nông, giảm SpO2 (đặc biệt khi dùng IV)",
            "Dấu hiệu quá liều: buồn ngủ nặng, lú lẫn, hôn mê, suy hô hấp",
            "Dấu hiệu phụ thuộc: cần tăng liều, triệu chứng cai khi ngừng",
            "Dấu hiệu té ngã: đặc biệt ở người cao tuổi",
            "Tương tác với alcohol, opioids, CYP3A4 inhibitors/inducers"
        ],
        "precautions": [
            "Suy hô hấp - nguy hiểm, đặc biệt khi dùng IV, theo dõi hô hấp chặt chẽ",
            "Phụ thuộc, nghiện - với dùng dài ngày, cần giảm liều dần (tapering) khi ngừng",
            "Tăng nguy cơ té ngã - đặc biệt ở người cao tuổi, tránh lái xe hoặc vận hành máy móc",
            "Lú lẫn - đặc biệt ở người cao tuổi, giảm liều",
            "Paradoxical reactions - hiếm nhưng có thể xảy ra (kích động, hung hăng), ngừng ngay",
            "Tránh rượu - tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Tránh opioids - tăng nguy cơ suy hô hấp (nguy hiểm)",
            "Thận trọng khi dùng với CYP3A4 inhibitors - tăng nồng độ diazepam, giảm liều",
            "Thận trọng khi dùng với CYP3A4 inducers - giảm nồng độ diazepam, có thể cần tăng liều",
            "Dạng IV - tiêm tĩnh mạch chậm (không quá 5mg/phút), theo dõi hô hấp chặt chẽ",
            "Dạng rectal - dùng cho co giật ở trẻ em hoặc khi không thể dùng IV",
            "Không ngừng đột ngột (có thể gây co giật, lo âu, mất ngủ)"
        ],
        "pharmacokinetics": {
            "half_life": "20-50 giờ (PO), 20-100 giờ (active metabolite)",
            "onset": "15-30 phút (PO), 1-5 phút (IV)",
            "duration": "6-12 giờ (PO), 15-60 phút (IV)",
            "protein_binding": "98%",
            "clearance": "Gan: chuyển hóa qua CYP3A4, CYP2C19. Thận: bài tiết một phần nguyên dạng và metabolites. Active metabolite (desmethyldiazepam) có half-life dài (20-100 giờ), tích lũy ở người cao tuổi."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng. Dạng rectal: bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh.",
        "black_box_warnings": "Nguy cơ suy hô hấp, đặc biệt khi dùng với opioids hoặc alcohol. Nguy cơ phụ thuộc, nghiện với dùng dài ngày. Nguy cơ té ngã ở người cao tuổi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp (nguy hiểm)",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân về nguy cơ suy hô hấp."
                },
                {
                    "drug": "Opioids (Morphine, Fentanyl, Oxycodone)",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ suy hô hấp (nguy hiểm, có thể tử vong)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, giảm liều cả hai thuốc, theo dõi hô hấp chặt chẽ."
                },
                {
                    "drug": "CYP3A4 inhibitors (Ketoconazole, Itraconazole, Erythromycin, Clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa diazepam qua CYP3A4, tăng nồng độ diazepam",
                    "effect": "Tăng nồng độ diazepam, tăng tác dụng phụ (buồn ngủ, suy hô hấp)",
                    "management": "Giảm liều diazepam 50% khi dùng với CYP3A4 inhibitors. Theo dõi tác dụng phụ chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (Carbamazepine, Phenytoin, Rifampin)",
                    "mechanism": "Cảm ứng chuyển hóa diazepam qua CYP3A4, giảm nồng độ diazepam",
                    "effect": "Giảm nồng độ diazepam, giảm hiệu quả",
                    "management": "Tăng liều diazepam 50-100% khi dùng với CYP3A4 inducers. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế chuyển hóa diazepam, tăng nồng độ diazepam",
                    "effect": "Tăng nồng độ diazepam, tăng tác dụng phụ",
                    "management": "Giảm liều diazepam 25-50% khi dùng với cimetidine. Theo dõi tác dụng phụ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng diazepam hoặc các thành phần khác",
                "Myasthenia gravis nặng - làm yếu cơ",
                "Glaucoma góc đóng - tăng nhãn áp",
                "Suy hô hấp nặng - tăng nguy cơ suy hô hấp",
                "Ức chế hệ thần kinh trung ương nặng"
            ],
            "tương_đối": [
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, té ngã, lú lẫn, giảm liều 50%",
                "Mang thai (nguy cơ dị tật bẩm sinh, withdrawal ở trẻ sơ sinh) - tránh dùng nếu có thể",
                "Dùng với alcohol hoặc opioids - tăng nguy cơ suy hô hấp",
                "Dùng với CYP3A4 inhibitors - giảm liều diazepam",
                "Dùng với CYP3A4 inducers - tăng liều diazepam"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có nguy cơ dị tật bẩm sinh (cleft lip/palate, heart defects). Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng diazepam trong thai kỳ, đặc biệt gần cuối thai kỳ. Tránh dùng trong thai kỳ nếu có thể. Nếu dùng, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Diazepam bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh thấp nhưng có thể gây buồn ngủ, bú kém.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém). Tránh dùng liều cao hoặc dài ngày."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Diazepam chuyển hóa ở gan qua CYP3A4, CYP2C19. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, lú lẫn, hôn mê",
                "Rối loạn hô hấp: suy hô hấp (nguy hiểm, có thể tử vong)",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Flumazenil (benzodiazepine antagonist) - 0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg). Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc benzodiazepine.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng, có thể cần thở máy)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Flumazenil: 0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg). Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc.",
                "Theo dõi liên tục: ý thức, hô hấp (quan trọng), tim mạch, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài)"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp (quan trọng), tim mạch, huyết áp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Flumazenil",
                    "dose": "0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg)",
                    "notes": "Benzodiazepine antagonist. Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc benzodiazepine."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Chia 2-4 lần/ngày. Uống cùng thời điểm mỗi ngày. Không ngừng đột ngột (có thể gây co giật, lo âu, mất ngủ)."
            },
            "im": {
                "reconstitution": "Không cần pha loãng.",
                "infusion_rate": "Tiêm bắp sâu vào cơ lớn (gluteal, deltoid).",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Dạng IM: hấp thu chậm và không đều, ít dùng."
            },
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W. Nồng độ: 1-5mg/mL.",
                "infusion_rate": "Tiêm tĩnh mạch chậm (không quá 5mg/phút). Theo dõi hô hấp chặt chẽ.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Dạng IV: dùng cho co giật (status epilepticus), an thần. Theo dõi hô hấp chặt chẽ (nguy cơ suy hô hấp)."
            },
            "rectal": {
                "with_food": "N/A",
                "timing": "Đặt hậu môn khi có co giật. Lặp sau 4-12 giờ nếu cần.",
                "notes": "Dạng rectal: dùng cho co giật ở trẻ em hoặc khi không thể dùng IV."
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Diazepam",
                "UpToDate - Diazepam: Drug information",
                "FDA - Valium (diazepam) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    "Lorazepam": {
        "group": "Neurology - Benzodiazepine",
        "vietnamese_name": "Lorazepam, Ativan",
        "administration": ["PO", "IM", "IV"],
        "indications": [
            "Lo âu",
            "Co giật (status epilepticus)",
            "An thần trước phẫu thuật",
            "Delirium (ICU)",
            "Cai rượu (alcohol withdrawal)",
            "Buồn nôn do hóa trị (adjunct)"
        ],
        "contraindications": [
            "Dị ứng",
            "Myasthenia gravis nặng",
            "Glaucoma góc đóng",
            "Suy hô hấp nặng",
            "Ức chế hệ thần kinh trung ương nặng"
        ],
        "dosage": {
            "adult_anxiety_po": "1-2mg x 2-3 lần/ngày",
            "adult_seizure_iv": "4mg IV, lặp sau 10-15 phút nếu cần (tối đa 8mg)",
            "adult_delirium_iv": "0.5-2mg IV mỗi 4-6 giờ",
            "adult_alcohol_withdrawal": "2-4mg x 3-4 lần/ngày, giảm dần",
            "adult_max": "10mg/ngày PO",
            "notes": "Benzodiazepine tác dụng trung bình (half-life 10-20 giờ). Không có active metabolite, ít tích lũy hơn diazepam. Dùng tốt cho người cao tuổi và suy gan."
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Lú lẫn (ít hơn diazepam)",
            "Suy hô hấp (nguy hiểm, đặc biệt khi dùng IV)",
            "Phụ thuộc, nghiện (với dùng dài ngày)",
            "Tăng nguy cơ té ngã (đặc biệt ở người cao tuổi)",
            "Amnesia (mất trí nhớ)",
            "Paradoxical reactions (kích động, hung hăng) - hiếm"
        ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Opioids: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp (nguy hiểm)",
            "Probenecid: tăng nồng độ lorazepam",
            "Valproate: tăng nồng độ lorazepam"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Lorazepam là benzodiazepine tác dụng trung bình, tăng cường tác dụng của GABA (gamma-aminobutyric acid) - chất dẫn truyền thần kinh ức chế chính trong não. Lorazepam gắn với thụ thể benzodiazepine (BZ1, BZ2) trên phức hợp GABA-A receptor, làm tăng tần suất mở kênh chloride, tăng dòng chloride vào tế bào, gây siêu phân cực và ức chế tế bào thần kinh. Tác dụng: an thần, giảm lo âu, chống co giật, và gây quên. Có dạng uống (PO), tiêm bắp (IM), và tiêm tĩnh mạch (IV). Half-life trung bình (10-20 giờ), không có active metabolite, ít tích lũy hơn diazepam. Dùng tốt cho người cao tuổi và suy gan. Tác dụng phụ: buồn ngủ, chóng mặt, lú lẫn (ít hơn diazepam), suy hô hấp (nguy hiểm), phụ thuộc, nghiện.",
        "monitoring": [
            "Đáp ứng điều trị: giảm lo âu, giảm co giật, giảm delirium",
            "Dấu hiệu suy hô hấp: thở chậm, thở nông, giảm SpO2 (đặc biệt khi dùng IV)",
            "Dấu hiệu quá liều: buồn ngủ nặng, lú lẫn, hôn mê, suy hô hấp",
            "Dấu hiệu phụ thuộc: cần tăng liều, triệu chứng cai khi ngừng",
            "Dấu hiệu té ngã: đặc biệt ở người cao tuổi",
            "Tương tác với alcohol, opioids, probenecid, valproate"
        ],
        "precautions": [
            "Suy hô hấp - nguy hiểm, đặc biệt khi dùng IV, theo dõi hô hấp chặt chẽ",
            "Phụ thuộc, nghiện - với dùng dài ngày, cần giảm liều dần (tapering) khi ngừng",
            "Tăng nguy cơ té ngã - đặc biệt ở người cao tuổi, tránh lái xe hoặc vận hành máy móc",
            "Lú lẫn - ít hơn diazepam nhưng vẫn có, đặc biệt ở người cao tuổi",
            "Paradoxical reactions - hiếm nhưng có thể xảy ra (kích động, hung hăng), ngừng ngay",
            "Tránh rượu - tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Tránh opioids - tăng nguy cơ suy hô hấp (nguy hiểm)",
            "Thận trọng khi dùng với probenecid hoặc valproate - tăng nồng độ lorazepam, giảm liều",
            "Dạng IV - tiêm tĩnh mạch chậm (không quá 2mg/phút), theo dõi hô hấp chặt chẽ",
            "Dạng IM - hấp thu tốt hơn diazepam, có thể dùng",
            "Không ngừng đột ngột (có thể gây co giật, lo âu, mất ngủ)"
        ],
        "pharmacokinetics": {
            "half_life": "10-20 giờ",
            "onset": "30-60 phút (PO), 15-30 phút (IM), 1-5 phút (IV)",
            "duration": "6-12 giờ (PO), 4-8 giờ (IM), 15-60 phút (IV)",
            "protein_binding": "85%",
            "clearance": "Gan: chuyển hóa qua glucuronidation (không qua CYP450). Thận: bài tiết một phần nguyên dạng và metabolites. Không có active metabolite, ít tích lũy hơn diazepam. Dùng tốt cho người cao tuổi và suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ suy hô hấp, đặc biệt khi dùng với opioids hoặc alcohol. Nguy cơ phụ thuộc, nghiện với dùng dài ngày. Nguy cơ té ngã ở người cao tuổi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp (nguy hiểm)",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân về nguy cơ suy hô hấp."
                },
                {
                    "drug": "Opioids (Morphine, Fentanyl, Oxycodone)",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ suy hô hấp (nguy hiểm, có thể tử vong)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, giảm liều cả hai thuốc, theo dõi hô hấp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Ức chế glucuronidation, tăng nồng độ lorazepam",
                    "effect": "Tăng nồng độ lorazepam, tăng tác dụng phụ",
                    "management": "Giảm liều lorazepam 25-50% khi dùng với probenecid. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Valproate",
                    "mechanism": "Ức chế glucuronidation, tăng nồng độ lorazepam",
                    "effect": "Tăng nồng độ lorazepam, tăng tác dụng phụ",
                    "management": "Giảm liều lorazepam 25-50% khi dùng với valproate. Theo dõi tác dụng phụ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng lorazepam hoặc các thành phần khác",
                "Myasthenia gravis nặng - làm yếu cơ",
                "Glaucoma góc đóng - tăng nhãn áp",
                "Suy hô hấp nặng - tăng nguy cơ suy hô hấp",
                "Ức chế hệ thần kinh trung ương nặng"
            ],
            "tương_đối": [
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy (nhưng ít hơn diazepam)",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, té ngã, lú lẫn, giảm liều 50%",
                "Mang thai (nguy cơ dị tật bẩm sinh, withdrawal ở trẻ sơ sinh) - tránh dùng nếu có thể",
                "Dùng với alcohol hoặc opioids - tăng nguy cơ suy hô hấp",
                "Dùng với probenecid hoặc valproate - giảm liều lorazepam"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có nguy cơ dị tật bẩm sinh (cleft lip/palate, heart defects). Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng lorazepam trong thai kỳ, đặc biệt gần cuối thai kỳ. Tránh dùng trong thai kỳ nếu có thể. Nếu dùng, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Lorazepam bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh thấp nhưng có thể gây buồn ngủ, bú kém.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém). Tránh dùng liều cao hoặc dài ngày."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Lorazepam chuyển hóa ở gan qua glucuronidation (không qua CYP450), ít tích lũy hơn diazepam. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ, nhưng ít hơn diazepam."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, lú lẫn, hôn mê",
                "Rối loạn hô hấp: suy hô hấp (nguy hiểm, có thể tử vong)",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Flumazenil (benzodiazepine antagonist) - 0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg). Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc benzodiazepine.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng, có thể cần thở máy)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Flumazenil: 0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg). Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc.",
                "Theo dõi liên tục: ý thức, hô hấp (quan trọng), tim mạch, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp (quan trọng), tim mạch, huyết áp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Flumazenil",
                    "dose": "0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg)",
                    "notes": "Benzodiazepine antagonist. Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc benzodiazepine."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Chia 2-3 lần/ngày. Uống cùng thời điểm mỗi ngày. Không ngừng đột ngột (có thể gây co giật, lo âu, mất ngủ)."
            },
            "im": {
                "reconstitution": "Không cần pha loãng.",
                "infusion_rate": "Tiêm bắp sâu vào cơ lớn (gluteal, deltoid). Hấp thu tốt hơn diazepam.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Dạng IM: hấp thu tốt hơn diazepam, có thể dùng."
            },
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W. Nồng độ: 0.5-2mg/mL.",
                "infusion_rate": "Tiêm tĩnh mạch chậm (không quá 2mg/phút). Theo dõi hô hấp chặt chẽ.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Dạng IV: dùng cho co giật (status epilepticus), an thần, delirium. Theo dõi hô hấp chặt chẽ (nguy cơ suy hô hấp)."
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Lorazepam",
                "UpToDate - Lorazepam: Drug information",
                "FDA - Ativan (lorazepam) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    "Clonazepam": {
        "group": "Neurology - Benzodiazepine",
        "vietnamese_name": "Clonazepam, Klonopin",
        "administration": ["PO"],
        "indications": [
            "Động kinh (epilepsy) - phòng ngừa co giật",
            "Panic disorder",
            "Rối loạn lo âu tổng quát (GAD)",
            "Restless legs syndrome - off-label",
            "Tic disorders - off-label"
        ],
        "contraindications": [
            "Dị ứng",
            "Myasthenia gravis nặng",
            "Glaucoma góc đóng",
            "Suy hô hấp nặng",
            "Ức chế hệ thần kinh trung ương nặng"
        ],
        "dosage": {
            "adult_epilepsy_po": "0.5mg x 3 lần/ngày, tăng đến 1-4mg/ngày (chia 2-3 lần)",
            "adult_panic_disorder": "0.25mg x 2 lần/ngày, tăng đến 1-4mg/ngày",
            "adult_max": "20mg/ngày",
            "notes": "Benzodiazepine tác dụng dài (half-life 18-50 giờ). Dùng chủ yếu cho động kinh và panic disorder. Tăng liều chậm để giảm tác dụng phụ."
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Ataxia (mất phối hợp vận động)",
            "Phụ thuộc, nghiện (với dùng dài ngày)",
            "Tăng nguy cơ té ngã (đặc biệt ở người cao tuổi)",
            "Amnesia (mất trí nhớ)",
            "Paradoxical reactions (kích động, hung hăng) - hiếm",
            "Tăng tiết nước bọt (ở trẻ em)"
        ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Opioids: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp (nguy hiểm)",
            "CYP3A4 inhibitors: tăng nồng độ clonazepam",
            "CYP3A4 inducers: giảm nồng độ clonazepam",
            "Valproate: tăng nồng độ clonazepam"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Clonazepam là benzodiazepine tác dụng dài, tăng cường tác dụng của GABA (gamma-aminobutyric acid) - chất dẫn truyền thần kinh ức chế chính trong não. Clonazepam gắn với thụ thể benzodiazepine (BZ1, BZ2) trên phức hợp GABA-A receptor, làm tăng tần suất mở kênh chloride, tăng dòng chloride vào tế bào, gây siêu phân cực và ức chế tế bào thần kinh. Tác dụng: chống co giật (phòng ngừa), giảm lo âu, và an thần. Có dạng uống (PO). Half-life dài (18-50 giờ), tích lũy ở người cao tuổi. Dùng chủ yếu cho động kinh (phòng ngừa co giật) và panic disorder. Tác dụng phụ: buồn ngủ, chóng mặt, lú lẫn, ataxia (mất phối hợp vận động), phụ thuộc, nghiện.",
        "monitoring": [
            "Đáp ứng điều trị: giảm tần suất co giật, giảm panic attacks, giảm lo âu",
            "Dấu hiệu quá liều: buồn ngủ nặng, lú lẫn, ataxia, hôn mê",
            "Dấu hiệu phụ thuộc: cần tăng liều, triệu chứng cai khi ngừng",
            "Dấu hiệu té ngã: đặc biệt ở người cao tuổi",
            "Ataxia (mất phối hợp vận động) - đặc biệt khi bắt đầu hoặc tăng liều",
            "Tương tác với alcohol, opioids, CYP3A4 inhibitors/inducers, valproate"
        ],
        "precautions": [
            "Phụ thuộc, nghiện - với dùng dài ngày, cần giảm liều dần (tapering) khi ngừng",
            "Tăng nguy cơ té ngã - đặc biệt ở người cao tuổi, tránh lái xe hoặc vận hành máy móc",
            "Ataxia (mất phối hợp vận động) - đặc biệt khi bắt đầu hoặc tăng liều, tăng liều chậm",
            "Lú lẫn - đặc biệt ở người cao tuổi, giảm liều",
            "Paradoxical reactions - hiếm nhưng có thể xảy ra (kích động, hung hăng), ngừng ngay",
            "Tránh rượu - tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Tránh opioids - tăng nguy cơ suy hô hấp (nguy hiểm)",
            "Thận trọng khi dùng với CYP3A4 inhibitors - tăng nồng độ clonazepam, giảm liều",
            "Thận trọng khi dùng với CYP3A4 inducers - giảm nồng độ clonazepam, có thể cần tăng liều",
            "Thận trọng khi dùng với valproate - tăng nồng độ clonazepam, giảm liều",
            "Tăng liều chậm để giảm tác dụng phụ (đặc biệt ataxia, buồn ngủ)",
            "Không ngừng đột ngột (có thể gây co giật, lo âu, mất ngủ, status epilepticus)"
        ],
        "pharmacokinetics": {
            "half_life": "18-50 giờ",
            "onset": "30-60 phút (PO)",
            "duration": "6-12 giờ (PO)",
            "protein_binding": "85%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần nguyên dạng và metabolites. Half-life dài, tích lũy ở người cao tuổi."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ suy hô hấp, đặc biệt khi dùng với opioids hoặc alcohol. Nguy cơ phụ thuộc, nghiện với dùng dài ngày. Nguy cơ té ngã ở người cao tuổi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp (nguy hiểm)",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân về nguy cơ suy hô hấp."
                },
                {
                    "drug": "Opioids (Morphine, Fentanyl, Oxycodone)",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ suy hô hấp (nguy hiểm, có thể tử vong)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, giảm liều cả hai thuốc, theo dõi hô hấp chặt chẽ."
                },
                {
                    "drug": "CYP3A4 inhibitors (Ketoconazole, Itraconazole, Erythromycin, Clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa clonazepam qua CYP3A4, tăng nồng độ clonazepam",
                    "effect": "Tăng nồng độ clonazepam, tăng tác dụng phụ (buồn ngủ, ataxia)",
                    "management": "Giảm liều clonazepam 50% khi dùng với CYP3A4 inhibitors. Theo dõi tác dụng phụ chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (Carbamazepine, Phenytoin, Rifampin)",
                    "mechanism": "Cảm ứng chuyển hóa clonazepam qua CYP3A4, giảm nồng độ clonazepam",
                    "effect": "Giảm nồng độ clonazepam, giảm hiệu quả",
                    "management": "Tăng liều clonazepam 50-100% khi dùng với CYP3A4 inducers. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Valproate",
                    "mechanism": "Ức chế chuyển hóa clonazepam, tăng nồng độ clonazepam",
                    "effect": "Tăng nồng độ clonazepam, tăng tác dụng phụ",
                    "management": "Giảm liều clonazepam 25-50% khi dùng với valproate. Theo dõi tác dụng phụ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng clonazepam hoặc các thành phần khác",
                "Myasthenia gravis nặng - làm yếu cơ",
                "Glaucoma góc đóng - tăng nhãn áp",
                "Suy hô hấp nặng - tăng nguy cơ suy hô hấp",
                "Ức chế hệ thần kinh trung ương nặng"
            ],
            "tương_đối": [
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, té ngã, lú lẫn, ataxia, giảm liều 50%",
                "Mang thai (nguy cơ dị tật bẩm sinh, withdrawal ở trẻ sơ sinh) - tránh dùng nếu có thể",
                "Dùng với alcohol hoặc opioids - tăng nguy cơ suy hô hấp",
                "Dùng với CYP3A4 inhibitors - giảm liều clonazepam",
                "Dùng với CYP3A4 inducers - tăng liều clonazepam",
                "Dùng với valproate - giảm liều clonazepam"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có nguy cơ dị tật bẩm sinh (cleft lip/palate, heart defects). Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng clonazepam trong thai kỳ, đặc biệt gần cuối thai kỳ. Tránh dùng trong thai kỳ nếu có thể. Nếu dùng, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Clonazepam bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh thấp nhưng có thể gây buồn ngủ, bú kém.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém). Tránh dùng liều cao hoặc dài ngày."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Clonazepam chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, lú lẫn, ataxia, hôn mê",
                "Rối loạn hô hấp: suy hô hấp (nguy hiểm, có thể tử vong)",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Flumazenil (benzodiazepine antagonist) - 0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg). Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc benzodiazepine.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng, có thể cần thở máy)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Flumazenil: 0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg). Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc.",
                "Theo dõi liên tục: ý thức, hô hấp (quan trọng), tim mạch, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài)"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp (quan trọng), tim mạch, huyết áp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Flumazenil",
                    "dose": "0.2mg IV, lặp mỗi 1 phút nếu cần (tối đa 3mg)",
                    "notes": "Benzodiazepine antagonist. Cẩn thận: có thể gây co giật ở bệnh nhân phụ thuộc benzodiazepine."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Chia 2-3 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm để giảm tác dụng phụ (đặc biệt ataxia, buồn ngủ). Không ngừng đột ngột (có thể gây co giật, lo âu, mất ngủ, status epilepticus)."
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
                "Lexicomp - Clonazepam",
                "UpToDate - Clonazepam: Drug information",
                "FDA - Klonopin (clonazepam) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    }
}

__all__ = ['BENZODIAZEPINES_DRUGS']














