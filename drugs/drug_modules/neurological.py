"""
Neurological and Psychiatric Medications
Generated from drug_database_data.py
"""

NEUROLOGICAL_DRUGS = {
"Carbamazepine": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Carbamazepine, Tegretol",
        "administration": ["PO"],
        "indications": [
            "Động kinh",
            "Đau dây thần kinh sinh ba",
            "Rối loạn lưỡng cực",
            "Rối loạn nhân cách"
        ],
        "contraindications": [
            "Block nhĩ thất",
            "Bệnh gan nặng",
            "Porphyria",
            "Dùng MAO inhibitor",
            "Giảm bạch cầu/giảm tiểu cầu"
        ],
        "dosage": {
            "adult_epilepsy": "200-400mg x 2-3 lần/ngày, tăng dần đến 800-1600mg/ngày",
            "adult_neuralgia": "100-200mg x 2 lần/ngày, tăng đến 200-400mg x 3-4 lần/ngày",
            "notes": "Theo dõi nồng độ trong máu, công thức máu, chức năng gan"
        },
        "side_effects": [
            "Chóng mặt",
            "Buồn nôn",
            "Giảm bạch cầu",
            "Ban da (nặng có thể SJS/TEN)",
            "Rối loạn chức năng gan",
            "Hạ natri máu"
        ],
        "interactions": [
            "Nhiều thuốc: cảm ứng enzyme CYP450, giảm nồng độ nhiều thuốc",
            "Warfarin: giảm tác dụng warfarin",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Thuốc chống co giật và ổn định tâm trạng. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh, ngăn cản sự lan truyền của các xung động bất thường. Cũng có thể ức chế giải phóng glutamate và điều hòa dòng calci. Tự cảm ứng enzyme (auto-induction) - tăng chuyển hóa của chính nó và các thuốc khác. Được dùng trong điều trị co giật cục bộ, co giật toàn thể, đau dây thần kinh sinh ba (trigeminal neuralgia), và rối loạn lưỡng cực. Có nhiều tương tác thuốc do cảm ứng enzyme.",
        "monitoring": [
            "Nồng độ carbamazepine trong máu (therapeutic range: 4-12 mcg/ml) - QUAN TRỌNG",
            "Tần suất và mức độ co giật",
            "Dấu hiệu độc tính (chóng mặt, ataxia, lú lẫn, buồn nôn)",
            "Công thức máu (giảm bạch cầu, giảm tiểu cầu, thiếu máu bất sản - nguy hiểm)",
            "Dấu hiệu hội chứng Stevens-Johnson (phát ban nặng) - nguy hiểm",
            "Chức năng gan (ALT, AST) - có thể tăng men gan, hiếm viêm gan",
            "Nồng độ natri (hạ natri máu - thường gặp)",
            "Chức năng thận"
        ],
        "precautions": [
            "Tuân thủ chặt chẽ liều và lịch dùng",
            "KHÔNG được ngừng đột ngột (nguy cơ co giật)",
            "Nồng độ trong máu cần được theo dõi định kỳ",
            "Nguy cơ giảm bạch cầu, giảm tiểu cầu, thiếu máu bất sản (nguy hiểm) - theo dõi công thức máu",
            "Nguy cơ hội chứng Stevens-Johnson - ngừng ngay nếu có phát ban",
            "Hạ natri máu thường gặp - theo dõi natri",
            "Tự cảm ứng enzyme → liều cần tăng dần theo thời gian",
            "Tương tác với nhiều thuốc: giảm hiệu quả thuốc tránh thai, warfarin, và các thuốc khác (do cảm ứng enzyme)",
            "Tương tác với nhiều thuốc: tăng nồng độ với erythromycin, cimetidine (do ức chế enzyme)",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Thận trọng ở suy gan"
        ],
        "pharmacokinetics": {
            "half_life": "25-65 giờ (bình thường), giảm xuống 12-17 giờ sau khi tự cảm ứng enzyme",
            "onset": "Vài giờ đến vài ngày",
            "duration": "Dài (phụ thuộc liều)",
            "protein_binding": "75%",
            "metabolism": "Gan (CYP3A4) - tự cảm ứng enzyme, cũng cảm ứng các enzyme khác",
            "clearance": "Gan, bị ảnh hưởng bởi tự cảm ứng và các thuốc tương tác"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Nguy cơ hội chứng Stevens-Johnson và hoại tử thượng bì nhiễm độc (TEN), có thể tử vong. Nguy cơ thiếu máu bất sản và giảm bạch cầu nghiêm trọng. Ngừng ngay nếu có phát ban hoặc dấu hiệu giảm bạch cầu. Nguy cơ tự sát và hành vi tự sát. Ngừng đột ngột có thể gây co giật."
    },
    "Fluoxetine": {
        "group": "Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)",
        "vietnamese_name": "Fluoxetine, Prozac",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu",
            "Rối loạn ám ảnh cưỡng chế (OCD)",
            "Bulimia"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_depression": "20mg x 1 lần/ngày, tăng đến 20-80mg/ngày",
            "adult_ocd": "20-60mg/ngày",
            "notes": "Tác dụng kéo dài (half-life dài), ngừng 5 tuần trước MAO inhibitor"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ hoặc buồn ngủ",
            "Giảm ham muốn tình dục",
            "Nhức đầu",
            "Hội chứng serotonin (với thuốc khác)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định (nguy cơ hội chứng serotonin)",
            "Tramadol: tăng nguy cơ co giật và hội chứng serotonin",
            "Warfarin: tăng tác dụng chống đông",
            "Triptans: tăng nguy cơ hội chứng serotonin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Fluoxetine là SSRI (Selective Serotonin Reuptake Inhibitor) ức chế tái hấp thu serotonin ở synap thần kinh, tăng nồng độ serotonin trong khe synap. Tăng serotonin dẫn đến điều chỉnh thụ thể serotonin (desensitization) và tác dụng chống trầm cảm. Có tính chọn lọc cao với serotonin (ít ảnh hưởng đến norepinephrine, dopamine, hoặc các thụ thể khác). Ưu điểm: half-life dài (cả thuốc và chất chuyển hóa norfluoxetine), ít tác dụng phụ cholinergic và tim mạch hơn TCA. Tác dụng kéo dài sau khi ngừng thuốc",
        "monitoring": [
            "Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)",
            "Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)",
            "Dấu hiệu hội chứng serotonin: kích động, nhịp tim nhanh, tăng huyết áp, sốt, co giật (nếu dùng với thuốc khác)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Chức năng gan nếu có triệu chứng (hiếm)",
            "Dấu hiệu rút thuốc khi ngừng (chóng mặt, buồn nôn, kích động)"
        ],
        "precautions": [
            "KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối - nguy cơ hội chứng serotonin nghiêm trọng)",
            "Ngừng fluoxetine ít nhất 5 tuần trước khi bắt đầu MAO inhibitor (do half-life dài)",
            "Theo dõi sát dấu hiệu tự tử trong vài tuần đầu (tăng nguy cơ ở <24 tuổi)",
            "Giảm liều dần khi ngừng (tránh hội chứng rút thuốc)",
            "Thận trọng khi dùng với tramadol, triptans (tăng nguy cơ hội chứng serotonin)",
            "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
            "Có thể gây mất ngủ → dùng buổi sáng",
            "Có thể gây buồn ngủ → dùng buổi tối (tùy bệnh nhân)",
            "Tác dụng kéo dài do half-life dài (cả thuốc và norfluoxetine)"
        ],
        "pharmacokinetics": {
            "half_life": "1-4 ngày (rất dài, cả fluoxetine và norfluoxetine)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "Rất dài (do half-life dài)",
            "protein_binding": "94-95% (rất cao)",
            "clearance": "Gan (chuyển hóa qua CYP2D6, CYP2C9, CYP3A4 thành norfluoxetine - chất hoạt động với half-life dài hơn)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Chống chỉ định với MAO inhibitor - nguy cơ hội chứng serotonin nghiêm trọng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline, linezolid)",
                    "mechanism": "Ức chế chuyển hóa serotonin, tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng: kích động, nhịp tim nhanh, tăng huyết áp, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng fluoxetine ít nhất 5 tuần trước khi bắt đầu MAO inhibitor (do half-life dài)."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Tăng nồng độ serotonin, tăng nguy cơ co giật",
                    "effect": "Hội chứng serotonin, tăng nguy cơ co giật",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giảm liều tramadol và theo dõi sát."
                },
                {
                    "drug": "Triptans (sumatriptan, rizatriptan)",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin",
                    "management": "Thận trọng. Dùng cách xa ít nhất 24 giờ. Theo dõi dấu hiệu hội chứng serotonin."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Fluoxetine ức chế CYP2C9, tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Fluoxetine ức chế CYP2D6, CYP2C9, tăng nồng độ",
                    "effect": "Tăng nồng độ phenytoin/carbamazepine, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ. Giảm liều phenytoin/carbamazepine nếu cần."
                },
                {
                    "drug": "Tricyclic antidepressants (TCA)",
                    "mechanism": "Ức chế CYP2D6, tăng nồng độ TCA",
                    "effect": "Tăng nồng độ TCA, tăng nguy cơ độc tính (rối loạn nhịp, block nhĩ thất)",
                    "management": "Thận trọng. Giảm liều TCA 50%. Theo dõi ECG."
                }
            ],
            "minor": [
                {
                    "drug": "CYP2D6 substrates (codeine, metoprolol)",
                    "mechanism": "Ức chế CYP2D6",
                    "effect": "Tăng nồng độ các thuốc chuyển hóa qua CYP2D6",
                    "management": "Thận trọng. Điều chỉnh liều nếu cần."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Dị ứng fluoxetine",
                "Hội chứng serotonin đang diễn ra"
            ],
            "relative": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Có ý định tự tử - chỉ kê đơn số lượng ít",
                "Bệnh tim - thận trọng",
                "Rối loạn đông máu - tăng nguy cơ chảy máu",
                "Dùng với tramadol, triptans - tăng nguy cơ hội chứng serotonin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Một số nghiên cứu gợi ý tăng nguy cơ dị tật thai nhi (dị tật tim, dị tật chi) khi dùng trong 3 tháng đầu, nhưng chứng cứ không rõ ràng. Có thể gây tăng huyết áp phổi ở trẻ sơ sinh (PPHN) - nguy cơ thấp. Có thể gây hội chứng cai ở trẻ sơ sinh (kích động, khó thở, run) nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Fluoxetine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ bú mẹ thường <10% nồng độ mẹ. Có thể gây buồn ngủ, bú kém, quấy khóc ở trẻ. Ít báo cáo về tác dụng phụ nghiêm trọng.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, quấy khóc ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc chuyển sang SSRI khác (sertraline)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Fluoxetine chuyển hóa ở gan qua CYP2D6, CYP2C9, CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan trực tiếp."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Kích động, lú lẫn",
                "Nhịp tim nhanh",
                "Tăng huyết áp",
                "Sốt",
                "Co giật",
                "Hôn mê",
                "Hội chứng serotonin (nếu dùng với thuốc khác)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG, huyết áp, nhịp tim",
                "Điều trị hội chứng serotonin: Cyproheptadine (4-8mg PO/IV), benzodiazepines cho co giật",
                "Điều trị co giật: Benzodiazepines (lorazepam, diazepam)",
                "Điều trị tăng huyết áp: Esmolol, labetalol",
                "Hạ nhiệt nếu sốt",
                "Truyền dịch",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài)"
            ],
            "monitoring": "ECG, huyết áp, nhịp tim, nhiệt độ, ý thức, dấu hiệu co giật, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (buổi sáng hoặc tối tùy tác dụng phụ). Nếu gây mất ngủ → dùng buổi sáng. Nếu gây buồn ngủ → dùng buổi tối."
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
                "FDA Drug Label - Prozac (fluoxetine)",
                "UpToDate - Fluoxetine: Drug information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
"Phenytoin": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Phenytoin, Dilantin",
        "administration": ["PO", "IV"],
        "indications": [
            "Động kinh (tổng quát, cục bộ)",
            "Status epilepticus",
            "Đau dây thần kinh sinh ba",
            "Rối loạn nhịp tim (hiếm)"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy gan nặng",
            "Block nhĩ thất",
            "Hội chứng bệnh lympho"
        ],
        "dosage": {
            "adult_po": "100mg x 3 lần/ngày, tăng đến 200-400mg/ngày",
            "adult_iv_loading": "15-20mg/kg IV (tối đa 1.5g)",
            "adult_iv_maintenance": "100mg IV mỗi 6-8 giờ sau loading",
            "status_epilepticus": "15-20mg/kg IV x 1 lần",
            "notes": "Theo dõi nồng độ trong máu (mục tiêu 10-20 mcg/mL). Non-linear kinetics"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Nystagmus (liều cao)",
            "Ataxia (liều cao)",
            "Ban da (có thể nặng - SJS/TEN)",
            "Hạ bạch cầu",
            "Tăng men gan",
            "Loãng xương (dùng lâu dài)",
            "Tăng acid uric",
            "Rối loạn chức năng nhận thức"
        ],
        "interactions": [
            "Warfarin: giảm tác dụng warfarin (cảm ứng enzyme)",
            "Oral contraceptives: giảm hiệu quả",
            "Folic acid: giảm nồng độ phenytoin",
            "Many drugs: cảm ứng CYP450, giảm nồng độ nhiều thuốc"
        ],
        "pregnancy": "D - Nguy cơ dị tật thai nhi",
        "mechanism_of_action": "Thuốc chống co giật, ổn định màng tế bào. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh, ngăn cản sự lan truyền của các xung động bất thường. Chỉ tác động lên các tế bào đang hoạt động mạnh (như trong co giật), không ảnh hưởng đến hoạt động bình thường. Điều hòa dòng calci và có thể ức chế giải phóng glutamate. Được dùng trong điều trị co giật cục bộ, co giật toàn thể, và status epilepticus. Cũng được dùng trong rối loạn nhịp tim (nhưng ít dùng hơn).",
        "monitoring": [
            "Nồng độ phenytoin trong máu (therapeutic range: 10-20 mcg/ml, free: 1-2 mcg/ml) - QUAN TRỌNG",
            "Tần suất và mức độ co giật",
            "Dấu hiệu độc tính (nystagmus ở >20 mcg/ml, ataxia ở >30 mcg/ml, lú lẫn ở >40 mcg/ml)",
            "Chức năng gan (ALT, AST, bilirubin) - có thể tăng men gan, hiếm viêm gan nặng",
            "Công thức máu (giảm bạch cầu, giảm tiểu cầu, thiếu máu megaloblastic do thiếu folate)",
            "Nồng độ folate và vitamin D (phenytoin làm giảm)",
            "Chức năng thận (creatinine)",
            "Dấu hiệu hội chứng Stevens-Johnson (phát ban nặng) - nguy hiểm",
            "Răng và nướu (tăng sản nướu)",
            "Xương (loãng xương do giảm vitamin D)"
        ],
        "precautions": [
            "Tuân thủ chặt chẽ liều và lịch dùng - bỏ liều có thể gây co giật",
            "KHÔNG được ngừng đột ngột (nguy cơ status epilepticus)",
            "Nồng độ trong máu cần được theo dõi định kỳ - có mối quan hệ không tuyến tính (saturable kinetics)",
            "Liều tăng nhỏ có thể làm nồng độ tăng rất nhiều ở liều cao (Michaelis-Menten kinetics)",
            "Tương tác với nhiều thuốc: giảm hiệu quả thuốc tránh thai, warfarin (cả hai đều tăng hoặc giảm tùy thuốc)",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không nghiền viên nang hoặc viên nén (giảm hấp thu)",
            "Bổ sung folate và vitamin D khi dùng kéo dài",
            "Nguy cơ hội chứng Stevens-Johnson - ngừng ngay nếu có phát ban",
            "Thận trọng ở suy gan (giảm chuyển hóa)",
            "Liều IV: truyền chậm (không quá 50mg/phút) để tránh hạ huyết áp, rối loạn nhịp",
            "Không pha trong D5W (kết tủa), chỉ dùng NS"
        ],
        "pharmacokinetics": {
            "half_life": "22 giờ (bình thường), dài hơn ở liều cao (saturable kinetics)",
            "onset": "30-60 phút (PO), 15-30 phút (IV)",
            "duration": "Dài (phụ thuộc liều)",
            "protein_binding": "90% (rất cao), chỉ free phenytoin mới hoạt động",
            "metabolism": "Gan (CYP2C9, CYP2C19) - chuyển hóa mạnh",
            "clearance": "Gan, có thể bị ảnh hưởng bởi tình trạng dinh dưỡng, tuổi tác"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản ở nhiệt độ phòng, không đông lạnh, chỉ dùng NS để pha.",
        "black_box_warnings": "Nguy cơ hội chứng Stevens-Johnson và hoại tử thượng bì nhiễm độc (TEN), có thể tử vong. Ngừng ngay nếu có phát ban. Nguy cơ tự sát và hành vi tự sát. Giảm bạch cầu, giảm tiểu cầu có thể nặng. Ngừng đột ngột có thể gây status epilepticus."
    },
    "Valproate": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Valproate, Valproic Acid, Depakote",
        "administration": ["PO", "IV"],
        "indications": [
            "Động kinh (nhiều loại)",
            "Rối loạn lưỡng cực",
            "Migraine phòng ngừa",
            "Status epilepticus"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Rối loạn chuyển hóa chu trình urea",
            "Suy gan nặng",
            "Có thai (cho rối loạn lưỡng cực)"
        ],
        "dosage": {
            "adult_po": "250-500mg x 2-3 lần/ngày, tăng đến 1000-3000mg/ngày",
            "adult_iv": "15-20mg/kg IV x 1 lần, sau đó 5-10mg/kg mỗi 6 giờ",
            "adult_max": "60mg/kg/ngày (không quá 3000mg/ngày)",
            "notes": "Theo dõi nồng độ (mục tiêu 50-100 mcg/mL), chức năng gan, tiểu cầu"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tăng cân",
            "Rụng tóc",
            "Tăng men gan",
            "Viêm tụy (hiếm nhưng nguy hiểm)",
            "Thiếu tiểu cầu",
            "Dị tật thai nhi (neural tube defects)",
            "Loãng xương (dùng lâu dài)",
            "Tăng ammonia máu"
        ],
        "interactions": [
            "Phenytoin/Carbamazepine: giảm nồng độ valproate",
            "Lamotrigine: tăng nồng độ lamotrigine",
            "Aspirin: tăng nồng độ valproate",
            "Warfarin: có thể tăng tác dụng"
        ],
        "pregnancy": "D - Nguy cơ dị tật thai nhi cao (neural tube defects)",
        "mechanism_of_action": "Valproate (valproic acid) ức chế enzyme GABA transaminase, tăng nồng độ GABA (gamma-aminobutyric acid) - chất dẫn truyền thần kinh ức chế chính trong não. Cũng ức chế kênh natri voltage-gated và kênh calci T-type, làm giảm tính kích thích của tế bào thần kinh. Có thể ức chế histone deacetylase. Tác dụng: chống động kinh (nhiều loại), ổn định tâm trạng (bipolar), phòng ngừa migraine. Cơ chế phức tạp, tác dụng trên nhiều hệ thống",
        "monitoring": [
            "Nồng độ valproate trong máu (mục tiêu 50-100 mcg/mL, hoặc 350-700 μmol/L) - định kỳ",
            "Chức năng gan (ALT, AST, bilirubin) trước khi bắt đầu, sau 2 tuần, sau 1 tháng, sau đó mỗi 3-6 tháng",
            "Tiểu cầu (platelet count) - định kỳ (có thể gây giảm tiểu cầu)",
            "Ammonia máu nếu có triệu chứng lú lẫn, buồn nôn, nôn (dấu hiệu tăng ammonia)",
            "Lipase, amylase nếu có đau bụng (viêm tụy - hiếm nhưng nguy hiểm)",
            "Dấu hiệu viêm tụy: đau bụng nặng, buồn nôn, nôn (ngừng ngay)",
            "Dấu hiệu độc gan: vàng da, mệt mỏi, buồn nôn (ngừng ngay)",
            "Cân nặng (tăng cân là tác dụng phụ phổ biến)",
            "Mật độ xương nếu dùng lâu dài (tăng nguy cơ loãng xương)"
        ],
        "precautions": [
            "THEO DÕI CHẶT CHẼ chức năng gan, đặc biệt trong 6 tháng đầu (nguy cơ viêm gan nặng, có thể tử vong)",
            "NGỪNG NGAY nếu có dấu hiệu viêm tụy (đau bụng nặng) hoặc độc gan (vàng da)",
            "Theo dõi nồng độ trong máu để điều chỉnh liều (therapeutic drug monitoring)",
            "Bổ sung acid folic trước và trong thai kỳ (giảm nguy cơ neural tube defects)",
            "Tránh dùng trong thai kỳ nếu có thể (nguy cơ dị tật thai nhi cao - neural tube defects, dị tật tim, dị tật mặt)",
            "Điều chỉnh liều khi dùng với lamotrigine (tăng nồng độ lamotrigine → giảm liều lamotrigine 50%)",
            "Thận trọng ở bệnh nhân suy gan, suy thận (giảm liều)",
            "Có thể gây tăng cân (cần theo dõi và tư vấn chế độ ăn)",
            "Có thể gây rụng tóc (thường tạm thời, có thể bổ sung kẽm, selen)",
            "Tránh dùng với aspirin liều cao (tăng nguy cơ độc tính)"
        ],
        "pharmacokinetics": {
            "half_life": "9-16 giờ (ngắn, nhưng có thể kéo dài ở liều cao do bão hòa chuyển hóa)",
            "onset": "Vài giờ đến vài ngày",
            "duration": "Ngắn (cần dùng 2-3 lần/ngày)",
            "protein_binding": "80-95% (cao, tăng ở liều cao do bão hòa)",
            "clearance": "Gan (chuyển hóa qua glucuronidation, beta-oxidation, CYP450), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nang: không làm lạnh",
        "black_box_warnings": "Viêm gan nặng có thể gây tử vong - nguy cơ cao nhất ở trẻ em <2 tuổi, dùng nhiều thuốc chống động kinh, bệnh gan. Viêm tụy có thể gây tử vong. Dị tật thai nhi (neural tube defects) - chống chỉ định trong thai kỳ cho rối loạn lưỡng cực. Giảm tiểu cầu có thể gây chảy máu",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Lamotrigine",
                    "mechanism": "Valproate ức chế glucuronidation của lamotrigine, tăng nồng độ lamotrigine",
                    "effect": "Tăng nguy cơ ban da nghiêm trọng (SJS/TEN) với lamotrigine",
                    "management": "Giảm liều khởi đầu lamotrigine 50% khi dùng với valproate. Theo dõi sát dấu hiệu ban da."
                },
                {
                    "drug": "Aspirin (liều cao)",
                    "mechanism": "Aspirin ức chế chuyển hóa valproate và tăng protein binding",
                    "effect": "Tăng nồng độ valproate, tăng nguy cơ độc tính",
                    "management": "Tránh dùng aspirin liều cao. Thận trọng khi dùng cùng, theo dõi nồng độ valproate."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Valproate có thể ức chế CYP2C9, tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa valproate",
                    "effect": "Giảm nồng độ valproate",
                    "management": "Tăng liều valproate nếu cần. Theo dõi nồng độ valproate và điều chỉnh liều."
                },
                {
                    "drug": "Phenobarbital",
                    "mechanism": "Cảm ứng enzyme, tăng chuyển hóa valproate",
                    "effect": "Giảm nồng độ valproate",
                    "management": "Tăng liều valproate nếu cần. Theo dõi nồng độ."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng CYP450, tăng chuyển hóa valproate",
                    "effect": "Giảm nồng độ valproate đáng kể",
                    "management": "Tăng liều valproate. Theo dõi nồng độ và điều chỉnh liều."
                }
            ],
            "minor": [
                {
                    "drug": "Metronidazole",
                    "mechanism": "Có thể ức chế chuyển hóa valproate",
                    "effect": "Tăng nhẹ nồng độ valproate",
                    "management": "Theo dõi nồng độ nếu dùng lâu dài"
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Bệnh gan hoạt động (viêm gan cấp hoặc mạn)",
                "Rối loạn chuyển hóa chu trình urea (urea cycle disorders)",
                "Suy gan nặng (Child-Pugh C)",
                "Có thai (cho rối loạn lưỡng cực) - nguy cơ dị tật thai nhi cao",
                "Dị ứng valproate"
            ],
            "relative": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều, theo dõi chặt chẽ",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Thiếu hụt tiểu cầu - tăng nguy cơ chảy máu",
                "Rối loạn đông máu - thận trọng",
                "Có thai (cho động kinh) - chỉ dùng nếu lợi ích > nguy cơ, bổ sung acid folic",
                "Trẻ em <2 tuổi - tăng nguy cơ viêm gan nặng",
                "Dùng nhiều thuốc chống động kinh - tăng nguy cơ độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ cho rối loạn lưỡng cực do nguy cơ dị tật thai nhi cao (neural tube defects 1-2%, dị tật tim, dị tật mặt, dị tật chi). Với động kinh, chỉ dùng nếu lợi ích > nguy cơ. Bổ sung acid folic 4-5mg/ngày trước và trong thai kỳ (giảm nguy cơ neural tube defects). Theo dõi nồng độ valproate trong thai kỳ (giảm do tăng clearance). Nguy cơ rối loạn phát triển thần kinh ở trẻ (IQ thấp hơn, tự kỷ, ADHD).",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Valproate bài tiết vào sữa mẹ ở nồng độ thấp (1-10% liều mẹ). Nồng độ trong máu trẻ bú mẹ thường <5% nồng độ mẹ. Ít báo cáo về tác dụng phụ ở trẻ bú mẹ. Tuy nhiên, cần theo dõi trẻ về dấu hiệu buồn ngủ, tăng cân chậm, tăng men gan.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, tăng cân chậm, vàng da ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều."
            }
        },
        "hepatic_adjustment": {
            "mild": "Giảm liều 25-50%. Theo dõi chức năng gan mỗi 3 tháng",
            "moderate": "Giảm liều 50%. Theo dõi chức năng gan mỗi 1-2 tháng. Tránh dùng nếu có thể",
            "severe": "Không dùng (chống chỉ định). Nếu bắt buộc, dùng liều rất thấp dưới sự giám sát chặt chẽ, theo dõi chức năng gan hàng tuần",
            "notes": "Valproate chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính gan. Nguy cơ viêm gan nặng cao nhất ở trẻ em <2 tuổi và bệnh nhân dùng nhiều thuốc chống động kinh. Theo dõi ALT/AST, bilirubin định kỳ."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "An thần, lú lẫn, hôn mê",
                "Rối loạn nhịp tim, block nhĩ thất",
                "Tăng ammonia máu (lú lẫn, hôn mê)",
                "Hạ huyết áp",
                "Suy hô hấp",
                "Độc gan (tăng ALT/AST, vàng da)",
                "Giảm tiểu cầu, chảy máu"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ (không dùng sau khi đã hôn mê)",
                "Theo dõi nồng độ valproate trong máu",
                "Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần",
                "Điều trị tăng ammonia: L-carnitine (100mg/kg/ngày IV hoặc PO), có thể dùng L-arginine",
                "Lọc máu (hemodialysis) nếu nồng độ >850 mcg/mL hoặc có triệu chứng nặng (hiệu quả do protein binding thấp ở liều cao)",
                "Theo dõi chức năng gan, tiểu cầu, ammonia máu",
                "Điều trị hỗ trợ: chống nôn, truyền dịch, theo dõi điện giải"
            ],
            "monitoring": "Nồng độ valproate trong máu, ALT/AST, bilirubin, tiểu cầu, ammonia máu, điện giải, ECG, huyết áp, nhịp tim, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Chia 2-3 lần/ngày (do half-life ngắn). Có thể dùng cùng bữa ăn để giảm kích ứng dạ dày"
            },
            "iv": {
                "reconstitution": "Pha với D5W hoặc NS để nồng độ 1-4mg/mL. Không pha với các dung dịch khác",
                "infusion_rate": "Truyền 15-20mg/kg trong 60 phút (không quá 20mg/phút)",
                "compatibility": ["D5W", "NS", "Ringer's lactate"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng chai"],
                "notes": "Truyền chậm để tránh kích ứng. Theo dõi huyết áp, nhịp tim trong khi truyền. Có thể gây kích ứng tĩnh mạch."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Depakote (valproate sodium)",
                "UpToDate - Valproate: Drug information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Epilepsia - ILAE treatment guidelines",
                "American Academy of Neurology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Levetiracetam": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Levetiracetam, Keppra",
        "administration": ["PO", "IV"],
        "indications": [
            "Động kinh cục bộ",
            "Động kinh tổng quát",
            "Status epilepticus (IV)"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "500-1000mg x 2 lần/ngày, tăng đến 1000-3000mg/ngày",
            "adult_iv": "500-1000mg IV mỗi 12 giờ",
            "adult_max": "3000mg/ngày",
            "notes": "Ít tương tác thuốc, an toàn cho trẻ em và người già"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "50_80": "Giảm liều 25%",
            "30_50": "Giảm liều 50%",
            "under_30": "Giảm liều 75%"
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Kích động, hành vi bất thường",
            "Nhức đầu",
            "Mệt mỏi",
            "Ít tác dụng phụ hơn các anticonvulsants khác"
        ],
        "interactions": [
            "Ít tương tác - không cảm ứng hoặc ức chế CYP450"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Thuốc chống co giật thế hệ mới, cơ chế chưa hoàn toàn rõ ràng. Gắn với protein SV2A (synaptic vesicle protein 2A) trong tế bào thần kinh, ức chế giải phóng chất dẫn truyền thần kinh từ túi synap, giảm hoạt động bất thường của tế bào thần kinh. Không ức chế kênh natri hoặc calci như các thuốc chống co giật cổ điển. Có phổ rộng: hiệu quả với co giật cục bộ và co giật toàn thể. Được dùng như thuốc bổ trợ hoặc đơn trị liệu. Ít tương tác thuốc hơn phenytoin.",
        "monitoring": [
            "Tần suất và mức độ co giật",
            "Tâm thần (kích động, lo âu, trầm cảm, suy nghĩ tự sát) - tác dụng phụ thần kinh tâm thần quan trọng",
            "Dấu hiệu hành vi bất thường (thay đổi tâm trạng, kích động)",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận",
            "Công thức máu (hiếm giảm bạch cầu, giảm tiểu cầu)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Mệt mỏi, chóng mặt (thường gặp)",
            "Dấu hiệu nhiễm trùng (hiếm giảm bạch cầu)"
        ],
        "precautions": [
            "Tác dụng phụ thần kinh tâm thần: kích động, lo âu, trầm cảm, suy nghĩ tự sát - theo dõi sát, đặc biệt ở trẻ em và thanh thiếu niên",
            "Nguy cơ hành vi tự sát - cảnh báo bệnh nhân và gia đình",
            "KHÔNG được ngừng đột ngột (nguy cơ co giật)",
            "Phải điều chỉnh liều ở suy thận (giảm liều và tăng khoảng cách liều)",
            "Khởi đầu với liều thấp, tăng dần để giảm tác dụng phụ",
            "Có thể gây mệt mỏi, chóng mặt - thận trọng khi lái xe, vận hành máy móc",
            "Tương tác thuốc ít hơn các thuốc chống co giật cổ điển (không ức chế CYP450)",
            "Có thể dùng với hoặc không có thức ăn",
            "Thận trọng ở bệnh nhân có tiền sử bệnh tâm thần",
            "Giảm liều ở người cao tuổi (nếu có suy thận)"
        ],
        "pharmacokinetics": {
            "half_life": "6-8 giờ (bình thường), 10-11 giờ (suy thận nặng)",
            "onset": "Nhanh (vài giờ đến vài ngày)",
            "duration": "Dài (phụ thuộc liều)",
            "protein_binding": "< 10% (rất thấp)",
            "metabolism": "Enzyme huyết tương (không qua CYP450) - ít tương tác",
            "clearance": "Chủ yếu qua thận (66% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Viên nén: tránh ẩm.",
        "black_box_warnings": "Nguy cơ hành vi tự sát và ý tưởng tự sát. Cảnh báo bệnh nhân và gia đình về các dấu hiệu kích động, lo âu, trầm cảm, thay đổi tâm trạng, và hành vi bất thường. Ngừng đột ngột có thể gây co giật."
    },
    "Lamotrigine": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Lamotrigine, Lamictal",
        "administration": ["PO"],
        "indications": [
            "Động kinh cục bộ",
            "Động kinh tổng quát",
            "Rối loạn lưỡng cực (phòng ngừa tái phát trầm cảm)"
        ],
        "contraindications": [
            "Dị ứng",
            "Ban da nặng trước đây (SJS/TEN)"
        ],
        "dosage": {
            "adult_epilepsy": "25mg x 2 lần/ngày x 2 tuần, tăng đến 100-200mg x 2 lần/ngày",
            "adult_bipolar": "25mg/ngày, tăng chậm đến 100-200mg/ngày",
            "adult_max": "400mg/ngày",
            "notes": "Tăng liều rất chậm để tránh ban da. Nếu dùng với valproate: giảm liều 50%"
        },
        "side_effects": [
            "Ban da (có thể nặng - SJS/TEN, đặc biệt khi tăng liều nhanh)",
            "Nhức đầu",
            "Chóng mặt",
            "Buồn nôn",
            "Mất ngủ",
            "Rối loạn thị giác"
        ],
        "interactions": [
            "Valproate: tăng nồng độ lamotrigine (giảm liều lamotrigine 50%)",
            "Carbamazepine: giảm nồng độ lamotrigine",
            "Oral contraceptives: giảm nồng độ lamotrigine (tăng liều)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Lamotrigine ức chế kênh natri voltage-gated, làm giảm giải phóng glutamate (chất dẫn truyền thần kinh kích thích) và làm giảm tính kích thích của tế bào thần kinh. Cũng có thể ức chế kênh calci. Tác dụng: chống động kinh (cục bộ và tổng quát), ổn định tâm trạng trong rối loạn lưỡng cực (phòng ngừa tái phát trầm cảm). Cơ chế chính xác chưa rõ hoàn toàn nhưng có liên quan đến ức chế giải phóng glutamate",
        "monitoring": [
            "Dấu hiệu ban da (RẤT QUAN TRỌNG) - ngừng ngay nếu có ban da, đặc biệt khi kèm sốt, mệt mỏi, đau khớp",
            "Ban da có thể tiến triển thành Stevens-Johnson syndrome (SJS) hoặc toxic epidermal necrolysis (TEN) - nguy hiểm tính mạng",
            "Nguy cơ ban da cao nhất trong 8 tuần đầu, đặc biệt khi tăng liều nhanh hoặc dùng với valproate",
            "Triệu chứng lâm sàng: nhức đầu, chóng mặt, buồn nôn (thường nhẹ)",
            "Chức năng gan nếu có triệu chứng (hiếm gây độc gan)",
            "Đáp ứng điều trị (động kinh hoặc tâm trạng)"
        ],
        "precautions": [
            "TĂNG LIỀU RẤT CHẬM để tránh ban da nghiêm trọng (SJS/TEN) - đây là tác dụng phụ nguy hiểm nhất",
            "NGỪNG NGAY nếu có ban da, đặc biệt kèm sốt, mệt mỏi, đau khớp (dấu hiệu SJS/TEN)",
            "Nếu dùng với valproate: giảm liều khởi đầu và tăng liều lamotrigine 50% (valproate tăng nồng độ lamotrigine)",
            "Nếu dùng với carbamazepine: tăng liều lamotrigine (carbamazepine giảm nồng độ)",
            "Nếu dùng với oral contraceptives: tăng liều lamotrigine (OCP giảm nồng độ)",
            "Không ngừng đột ngột (tăng nguy cơ co giật)",
            "Giảm liều dần nếu cần ngừng",
            "Thận trọng ở bệnh nhân suy gan, suy thận (giảm liều)",
            "Giáo dục bệnh nhân về dấu hiệu ban da và cần báo ngay"
        ],
        "pharmacokinetics": {
            "half_life": "25-30 giờ (dài, cho phép dùng 1-2 lần/ngày)",
            "onset": "Vài tuần (tác dụng chậm)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "55%",
            "clearance": "Gan (chuyển hóa qua glucuronidation, không qua CYP450), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ ban da nghiêm trọng (Stevens-Johnson syndrome, toxic epidermal necrolysis) - có thể gây tử vong. Nguy cơ tăng khi tăng liều nhanh, dùng với valproate, hoặc vi phạm phác đồ tăng liều. Ngừng ngay nếu có ban da, đặc biệt kèm sốt, mệt mỏi, đau khớp",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Valproate",
                    "mechanism": "Valproate ức chế glucuronidation của lamotrigine, tăng nồng độ lamotrigine đáng kể",
                    "effect": "Tăng nguy cơ ban da nghiêm trọng (SJS/TEN) - nguy cơ cao nhất khi dùng cùng valproate",
                    "management": "Giảm liều khởi đầu lamotrigine 50% khi dùng với valproate. Tăng liều rất chậm. Theo dõi sát dấu hiệu ban da."
                },
                {
                    "drug": "Oral contraceptives (estrogen)",
                    "mechanism": "Estrogen cảm ứng glucuronidation, tăng chuyển hóa lamotrigine",
                    "effect": "Giảm nồng độ lamotrigine 40-50%, có thể gây mất kiểm soát động kinh",
                    "management": "Tăng liều lamotrigine khi dùng OCP. Giảm liều khi ngừng OCP. Theo dõi nồng độ và điều chỉnh liều."
                }
            ],
            "moderate": [
                {
                    "drug": "Carbamazepine, Phenytoin, Phenobarbital",
                    "mechanism": "Cảm ứng glucuronidation, tăng chuyển hóa lamotrigine",
                    "effect": "Giảm nồng độ lamotrigine",
                    "management": "Tăng liều lamotrigine nếu cần. Theo dõi nồng độ và điều chỉnh liều."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng glucuronidation mạnh",
                    "effect": "Giảm nồng độ lamotrigine đáng kể",
                    "management": "Tăng liều lamotrigine. Theo dõi nồng độ và điều chỉnh liều."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng lamotrigine",
                "Ban da nặng trước đây (SJS/TEN) với lamotrigine",
                "Tăng liều quá nhanh (vi phạm phác đồ tăng liều)"
            ],
            "relative": [
                "Dùng với valproate - giảm liều khởi đầu 50%",
                "Trẻ em <16 tuổi - tăng nguy cơ ban da",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Dùng với oral contraceptives - tăng liều lamotrigine"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ dị tật thai nhi thấp hơn valproate và carbamazepine. Tuy nhiên, vẫn có nguy cơ dị tật (cleft palate, dị tật tim). Nồng độ lamotrigine giảm trong thai kỳ (tăng clearance), có thể cần tăng liều. Theo dõi nồng độ lamotrigine trong thai kỳ. Nguy cơ rối loạn phát triển thần kinh thấp hơn valproate.",
            "lactation": {
                "safety": "Compatible",
                "details": "Lamotrigine bài tiết vào sữa mẹ ở nồng độ đáng kể (40-50% liều mẹ). Nồng độ trong máu trẻ bú mẹ có thể đạt 20-30% nồng độ mẹ. Có thể gây tác dụng phụ ở trẻ (ban da, buồn ngủ). Cần theo dõi trẻ sát.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu ban da, buồn ngủ, bú kém ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Giảm liều 50-75% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ",
            "notes": "Lamotrigine chuyển hóa ở gan qua glucuronidation. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan hơn valproate."
        },
        "overdose_management": {
            "symptoms": [
                "Ban da (có thể tiến triển thành SJS/TEN)",
                "Buồn nôn, nôn",
                "Chóng mặt, nhức đầu",
                "Lú lẫn, co giật",
                "Rung nhĩ",
                "Hôn mê (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi sát dấu hiệu ban da (SJS/TEN) - nguy hiểm nhất",
                "Điều trị hỗ trợ: chống nôn, truyền dịch, theo dõi điện giải",
                "Theo dõi ECG nếu có triệu chứng tim mạch",
                "Điều trị co giật nếu có",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần"
            ],
            "monitoring": "Dấu hiệu ban da (SJS/TEN), ECG, ý thức, dấu hiệu co giật, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn",
                "timing": "Chia 2 lần/ngày (do half-life dài). Có thể dùng cùng bữa ăn để giảm kích ứng dạ dày"
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
                "FDA Drug Label - Lamictal (lamotrigine)",
                "UpToDate - Lamotrigine: Drug information",
                "Epilepsia - ILAE treatment guidelines",
                "American Academy of Neurology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Gabapentin": {
        "group": "Neurology - Anticonvulsant (Alpha-2-delta ligand)",
        "vietnamese_name": "Gabapentin, Neurontin",
        "administration": ["PO"],
        "indications": [
            "Động kinh cục bộ",
            "Đau thần kinh (postherpetic neuralgia, diabetic neuropathy)",
            "Rối loạn lo âu",
            "Hội chứng chân không yên"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_epilepsy": "300mg x 3 lần/ngày, tăng đến 900-1800mg/ngày",
            "adult_neuropathic": "300mg x 3 lần/ngày, tăng đến 1800-3600mg/ngày",
            "adult_max": "3600mg/ngày (chia 3 lần)",
            "notes": "Hấp thu giảm khi tăng liều. Uống cách xa antacids 2 giờ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "300mg x 2 lần/ngày",
            "15_30": "300mg x 1 lần/ngày",
            "under_15": "300mg cách ngày"
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Mệt mỏi",
            "Phù ngoại biên",
            "Tăng cân",
            "Nhìn mờ",
            "Suy giảm trí nhớ"
        ],
        "interactions": [
            "Antacids: giảm hấp thu (cách xa 2 giờ)",
            "Morphine: tăng tác dụng an thần",
            "Ít tương tác khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Gabapentin là thuốc chống động kinh và giảm đau thần kinh, có cấu trúc tương tự như GABA (gamma-aminobutyric acid) nhưng không gắn trực tiếp vào GABA receptors. Cơ chế chính xác chưa hoàn toàn rõ ràng, nhưng gabapentin gắn vào tiểu đơn vị alpha-2-delta của kênh canxi phụ thuộc điện thế (voltage-gated calcium channels) ở các terminal thần kinh. Điều này làm giảm dòng canxi vào tế bào, giảm phóng thích các chất dẫn truyền thần kinh (glutamate, noradrenaline, substance P) từ các terminal thần kinh. Dẫn đến giảm kích thích quá mức và giảm đau thần kinh. Gabapentin không ảnh hưởng đến GABA receptors, GABA uptake, hoặc GABA transaminase. Gabapentin có tác dụng chống động kinh, giảm đau thần kinh (đặc biệt đau sau zona, đau thần kinh do tiểu đường), và có thể có tác dụng an thần, giảm lo âu. Hấp thu giảm khi tăng liều do cơ chế vận chuyển bão hòa.",
        "monitoring": [
            "Đáp ứng điều trị (giảm cơn động kinh, giảm đau thần kinh, giảm lo âu)",
            "Tác dụng phụ thần kinh (buồn ngủ, chóng mặt, mệt mỏi, nhìn mờ, suy giảm trí nhớ) - đặc biệt khi bắt đầu hoặc tăng liều",
            "Phù ngoại biên (tay, chân) - có thể nặng",
            "Tăng cân - theo dõi cân nặng",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận (quan trọng)",
            "Dấu hiệu lệ thuộc, nghiện (hiếm nhưng có thể xảy ra)",
            "Tương tác với antacids (giảm hấp thu), morphine (tăng tác dụng an thần)"
        ],
        "precautions": [
            "Điều chỉnh liều ở suy thận QUAN TRỌNG: CrCl 30-60: 300mg x 2 lần/ngày; CrCl 15-30: 300mg x 1 lần/ngày; CrCl <15: 300mg cách ngày",
            "Hấp thu giảm khi tăng liều do cơ chế vận chuyển bão hòa - không tăng liều quá nhanh",
            "Uống cách xa antacids ít nhất 2 giờ (giảm hấp thu)",
            "Tăng liều dần dần để giảm tác dụng phụ (bắt đầu với 300mg x 3 lần/ngày)",
            "Buồn ngủ, chóng mặt, mệt mỏi - phổ biến, thường tự khỏi sau vài tuần, tránh lái xe hoặc vận hành máy móc",
            "Phù ngoại biên - có thể nặng, cần theo dõi, có thể cần giảm liều hoặc ngừng",
            "Tăng cân - theo dõi, có thể cần điều chỉnh chế độ ăn",
            "Không ngừng đột ngột - giảm liều dần dần (tăng nguy cơ co giật, hội chứng cai)",
            "Thận trọng ở bệnh nhân có tiền sử lệ thuộc thuốc (có thể gây lệ thuộc, nghiện)",
            "Thận trọng với bệnh nhân suy giảm chức năng thận (giảm thải trừ)",
            "Tương tác với morphine - tăng tác dụng an thần, thận trọng khi dùng chung",
            "Có thể gây suy giảm trí nhớ, nhìn mờ - thận trọng ở người cao tuổi"
        ],
        "pharmacokinetics": {
            "half_life": "5-7 giờ (bình thường), tăng ở suy thận (tỷ lệ với eGFR)",
            "onset": "Vài giờ đến vài ngày",
            "duration": "8-12 giờ (dùng 3 lần/ngày)",
            "protein_binding": "<3% (không gắn protein)",
            "clearance": "Thận: bài tiết chủ yếu qua thận (100% nguyên dạng, không chuyển hóa). Không chuyển hóa ở gan. Hấp thu giảm khi tăng liều do cơ chế vận chuyển L-amino acid bão hòa ở ruột. Thời gian bán thải tăng ở suy thận (tỷ lệ với eGFR)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/capsule: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng.",
        "black_box_warnings": "Nguy cơ suy hô hấp nghiêm trọng, có thể gây tử vong, khi dùng với các thuốc ức chế hệ thần kinh trung ương (opioids, benzodiazepines). Nguy cơ tăng ở bệnh nhân có bệnh hô hấp, người cao tuổi. Theo dõi chặt chẽ dấu hiệu suy hô hấp. Nguy cơ tác dụng phụ thần kinh nghiêm trọng (buồn ngủ, chóng mặt, mệt mỏi) có thể ảnh hưởng đến khả năng lái xe và vận hành máy móc."
    },
    "Pregabalin": {
        "group": "Neurology - Anticonvulsant (Alpha-2-delta ligand)",
        "vietnamese_name": "Pregabalin, Lyrica",
        "administration": ["PO"],
        "indications": [
            "Đau thần kinh (postherpetic neuralgia, diabetic neuropathy)",
            "Đau cơ xơ hóa",
            "Động kinh cục bộ",
            "Rối loạn lo âu tổng quát"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_neuropathic": "75mg x 2 lần/ngày, tăng đến 150-300mg x 2 lần/ngày",
            "adult_epilepsy": "75mg x 2 lần/ngày, tăng đến 150-600mg/ngày",
            "adult_max": "600mg/ngày",
            "notes": "Mạnh hơn gabapentin, hấp thu tốt hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "Giảm liều 75%",
            "under_15": "Giảm liều 90%"
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Phù ngoại biên",
            "Tăng cân",
            "Nhìn mờ",
            "Suy giảm trí nhớ",
            "Nguy cơ lạm dụng (controlled substance)"
        ],
        "interactions": [
            "Morphine: tăng tác dụng an thần",
            "Alcohol: tăng tác dụng an thần",
            "Ít tương tác khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Pregabalin là thuốc chống động kinh và giảm đau thần kinh, là dẫn xuất của gabapentin nhưng có cấu trúc tối ưu hơn. Pregabalin gắn vào tiểu đơn vị alpha-2-delta của kênh canxi phụ thuộc điện thế (voltage-gated calcium channels) ở các terminal thần kinh, với ái lực cao hơn gabapentin. Điều này làm giảm dòng canxi vào tế bào, giảm phóng thích các chất dẫn truyền thần kinh (glutamate, noradrenaline, substance P, CGRP) từ các terminal thần kinh. Dẫn đến giảm kích thích quá mức và giảm đau thần kinh. Khác với gabapentin, pregabalin có hấp thu tuyến tính (không bão hòa), dược động học dự đoán được, và hiệu quả mạnh hơn. Pregabalin có tác dụng chống động kinh, giảm đau thần kinh (đặc biệt đau sau zona, đau thần kinh do tiểu đường), đau cơ xơ hóa, và rối loạn lo âu. Pregabalin là controlled substance (có nguy cơ lạm dụng, nghiện).",
        "monitoring": [
            "Đáp ứng điều trị (giảm cơn động kinh, giảm đau thần kinh, giảm lo âu)",
            "Tác dụng phụ thần kinh (buồn ngủ, chóng mặt, mệt mỏi, nhìn mờ, suy giảm trí nhớ) - đặc biệt khi bắt đầu hoặc tăng liều",
            "Phù ngoại biên (tay, chân) - có thể nặng",
            "Tăng cân - theo dõi cân nặng",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận (quan trọng)",
            "Dấu hiệu lạm dụng, nghiện - pregabalin là controlled substance (nguy cơ lệ thuộc, nghiện)",
            "Tương tác với morphine (tăng tác dụng an thần), alcohol (tăng tác dụng an thần)"
        ],
        "precautions": [
            "Điều chỉnh liều ở suy thận QUAN TRỌNG: CrCl 30-60: giảm liều 50%; CrCl 15-30: giảm liều 75%; CrCl <15: giảm liều 90%",
            "Nguy cơ lạm dụng, nghiện - pregabalin là controlled substance (Schedule V), có thể gây lệ thuộc, nghiện",
            "Không ngừng đột ngột - giảm liều dần dần trong ít nhất 1 tuần (tăng nguy cơ co giật, hội chứng cai, mất ngủ, lo âu)",
            "Tăng liều dần dần để giảm tác dụng phụ (bắt đầu với 75mg x 2 lần/ngày)",
            "Buồn ngủ, chóng mặt, mệt mỏi - phổ biến, thường tự khỏi sau vài tuần, tránh lái xe hoặc vận hành máy móc",
            "Phù ngoại biên - có thể nặng, cần theo dõi, có thể cần giảm liều hoặc ngừng",
            "Tăng cân - theo dõi, có thể cần điều chỉnh chế độ ăn",
            "Thận trọng ở bệnh nhân có tiền sử lạm dụng thuốc, nghiện (nguy cơ cao)",
            "Thận trọng với bệnh nhân suy giảm chức năng thận (giảm thải trừ)",
            "Tương tác với morphine - tăng tác dụng an thần, thận trọng khi dùng chung",
            "Tránh rượu - tăng tác dụng an thần, tăng nguy cơ suy hô hấp",
            "Có thể gây suy giảm trí nhớ, nhìn mờ - thận trọng ở người cao tuổi",
            "Hấp thu tốt hơn gabapentin (không bão hòa), hiệu quả mạnh hơn, dùng 2 lần/ngày"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ (bình thường), tăng ở suy thận (tỷ lệ với eGFR)",
            "onset": "Vài giờ đến vài ngày",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "<1% (không gắn protein)",
            "clearance": "Thận: bài tiết chủ yếu qua thận (90% nguyên dạng, không chuyển hóa). Không chuyển hóa ở gan. Hấp thu tuyến tính (không bão hòa như gabapentin), dự đoán được. Thời gian bán thải tăng ở suy thận (tỷ lệ với eGFR)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/capsule: bảo quản trong bao bì kín. Controlled substance - cần bảo quản an toàn, tránh tiếp cận không được phép.",
        "black_box_warnings": "Nguy cơ suy hô hấp nghiêm trọng, có thể gây tử vong, khi dùng với các thuốc ức chế hệ thần kinh trung ương (opioids, benzodiazepines). Nguy cơ tăng ở bệnh nhân có bệnh hô hấp, người cao tuổi. Theo dõi chặt chẽ dấu hiệu suy hô hấp. Nguy cơ lạm dụng, nghiện - pregabalin là controlled substance (Schedule V), có thể gây lệ thuộc, nghiện. Không ngừng đột ngột - tăng nguy cơ co giật, hội chứng cai. Nguy cơ tác dụng phụ thần kinh nghiêm trọng (buồn ngủ, chóng mặt, mệt mỏi) có thể ảnh hưởng đến khả năng lái xe và vận hành máy móc."
    },
}

__all__ = ['NEUROLOGICAL_DRUGS']
