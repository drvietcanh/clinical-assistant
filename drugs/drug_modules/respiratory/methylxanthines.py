"""
Methylxanthines - Theophylline and Aminophylline
Bronchodilators for asthma and COPD
"""

METHYLXANTHINES_DRUGS = {
    "Theophylline": {
        "group": "Respiratory - Methylxanthine (Bronchodilator)",
        "vietnamese_name": "Theophylline, Theolair, Uniphyl",
        "administration": ["PO", "IV"],
        "indications": [
            "Hen suyễn (asthma)",
            "COPD (chronic obstructive pulmonary disease)",
            "Bronchospasm",
            "Apnea of prematurity (trẻ sơ sinh)"
        ],
        "contraindications": [
            "Dị ứng theophylline hoặc methylxanthines",
            "Rối loạn nhịp tim nặng",
            "Động kinh không kiểm soát",
            "Loét dạ dày tá tràng hoạt động"
        ],
        "dosage": {
            "adult_loading": "5-6mg/kg IV (tối đa 500mg) trong 20-30 phút",
            "adult_maintenance_iv": "0.4-0.6mg/kg/giờ (truyền liên tục)",
            "adult_maintenance_po": "300-600mg/ngày chia 2-3 lần (tùy công thức)",
            "adult_extended_release": "400-800mg x 1-2 lần/ngày",
            "pediatric_loading": "5mg/kg IV",
            "pediatric_maintenance": "0.5-1mg/kg/giờ IV hoặc 10-16mg/kg/ngày PO chia 3-4 lần",
            "notes": "Therapeutic window hẹp (10-20 mcg/mL). Cần TDM (therapeutic drug monitoring). Nhiều yếu tố ảnh hưởng clearance (tuổi, hút thuốc, bệnh gan/thận, thuốc khác)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%",
            "hemodialysis": "Bổ sung liều sau lọc máu"
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến ở nồng độ cao)",
            "Nhức đầu",
            "Run, bồn chồn",
            "Tim đập nhanh, rối loạn nhịp tim",
            "Co giật (ở nồng độ rất cao >30 mcg/mL)",
            "Loét dạ dày",
            "Tăng đường huyết"
        ],
        "interactions": [
            "Ciprofloxacin, Erythromycin, Clarithromycin: tăng nồng độ theophylline",
            "Cimetidine: tăng nồng độ theophylline",
            "Rifampin, Phenytoin, Carbamazepine: giảm nồng độ theophylline",
            "Lithium: giảm nồng độ lithium",
            "Beta-2 agonists: tăng tác dụng phụ (run, tim đập nhanh)"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Theophylline là methylxanthine, ức chế phosphodiesterase (PDE), làm tăng cAMP và cGMP trong tế bào cơ trơn phế quản, gây giãn phế quản. Ngoài ra, theophylline đối kháng adenosine receptors (A1, A2), cũng góp phần giãn phế quản. Theophylline cũng có tác dụng chống viêm nhẹ và tăng cường cơ hô hấp. Cơ chế chính xác chưa hoàn toàn rõ ràng, nhưng tác dụng giãn phế quản rõ ràng. Theophylline có therapeutic window hẹp (10-20 mcg/mL), dưới 10 mcg/mL ít hiệu quả, trên 20 mcg/mL tăng nguy cơ độc tính, trên 30 mcg/mL có thể gây co giật và tử vong.",
        "monitoring": [
            "Nồng độ theophylline trong máu (TDM) - QUAN TRỌNG: Target 10-20 mcg/mL",
            "Dấu hiệu độc tính: buồn nôn, nôn, run, tim đập nhanh, co giật",
            "Nhịp tim, huyết áp",
            "Đường huyết (có thể tăng)",
            "Chức năng gan (theophylline chuyển hóa ở gan)",
            "Chức năng thận (một phần thải qua thận)",
            "Triệu chứng lâm sàng (cải thiện khó thở, giảm wheezing)"
        ],
        "precautions": [
            "CẦN TDM (therapeutic drug monitoring) - therapeutic window hẹp (10-20 mcg/mL)",
            "Nhiều yếu tố ảnh hưởng clearance: tuổi (trẻ em, người già), hút thuốc (tăng clearance), bệnh gan/thận (giảm clearance), sốt, suy tim, thuốc khác",
            "Hút thuốc: tăng clearance 50-100%, cần tăng liều",
            "Suy gan, suy tim: giảm clearance, cần giảm liều",
            "Nhiều tương tác thuốc - kiểm tra trước khi dùng",
            "Ngừng hút thuốc: clearance giảm, cần giảm liều",
            "Sốt, nhiễm trùng: có thể giảm clearance",
            "Theo dõi sát dấu hiệu độc tính (buồn nôn, nôn, run, tim đập nhanh, co giật)",
            "Dùng dạng extended-release để duy trì nồng độ ổn định",
            "Không dùng với thức ăn giàu chất béo (có thể tăng hấp thu)"
        ],
        "pharmacokinetics": {
            "half_life": "4-8 giờ (người lớn không hút thuốc), 3-5 giờ (người hút thuốc), 20-30 giờ (trẻ sơ sinh), 10-20 giờ (người già, suy gan/thận)",
            "onset": "30-60 phút (PO), 15-30 phút (IV)",
            "duration": "6-12 giờ (tùy công thức)",
            "protein_binding": "40%",
            "metabolism": "Gan: chuyển hóa qua CYP1A2 (chính), CYP2E1, CYP3A4. Nhiều yếu tố ảnh hưởng: hút thuốc (cảm ứng CYP1A2), bệnh gan, thuốc khác",
            "clearance": "Gan (chủ yếu, 90%), thận (10% bài tiết nguyên dạng). Clearance thay đổi nhiều tùy yếu tố."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất.",
        "black_box_warnings": "Therapeutic window hẹp (10-20 mcg/mL). Nồng độ >20 mcg/mL: tăng nguy cơ độc tính (buồn nôn, nôn, run, tim đập nhanh, rối loạn nhịp tim). Nồng độ >30 mcg/mL: nguy cơ co giật, rối loạn nhịp tim nặng, tử vong. CẦN TDM (therapeutic drug monitoring).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ciprofloxacin, Enoxacin",
                    "mechanism": "Ức chế CYP1A2, làm giảm chuyển hóa theophylline, tăng nồng độ theophylline.",
                    "effect": "Tăng nồng độ theophylline 2-3 lần, tăng nguy cơ độc tính (buồn nôn, nôn, co giật, rối loạn nhịp tim, tử vong)",
                    "management": "TRÁNH DÙNG CHUNG nếu có thể. Nếu bắt buộc: giảm liều theophylline 30-50%, theo dõi nồng độ theophylline chặt chẽ, theo dõi dấu hiệu độc tính. Cân nhắc dùng levofloxacin thay thế (ít ảnh hưởng hơn)."
                },
                {
                    "drug": "Erythromycin, Clarithromycin",
                    "mechanism": "Ức chế CYP3A4 và có thể ảnh hưởng đến chuyển hóa theophylline.",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính",
                    "management": "Giảm liều theophylline 25-50%. Theo dõi nồng độ theophylline. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế CYP1A2 và các enzyme CYP450 khác, làm giảm chuyển hóa theophylline.",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính",
                    "management": "Giảm liều theophylline 30-50%. Theo dõi nồng độ theophylline. Cân nhắc dùng ranitidine hoặc famotidine thay thế (ít ảnh hưởng hơn)."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng CYP1A2, làm tăng chuyển hóa theophylline, giảm nồng độ theophylline.",
                    "effect": "Giảm nồng độ theophylline, giảm hiệu quả",
                    "management": "Tăng liều theophylline 50-100% khi bắt đầu rifampin. Theo dõi nồng độ theophylline. Giảm liều theophylline khi ngừng rifampin."
                }
            ],
            "moderate": [
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Cảm ứng CYP450, có thể tăng chuyển hóa theophylline.",
                    "effect": "Giảm nồng độ theophylline, giảm hiệu quả",
                    "management": "Theo dõi nồng độ theophylline. Có thể cần tăng liều theophylline."
                },
                {
                    "drug": "Beta-2 agonists (Salbutamol, Salmeterol, Formoterol)",
                    "mechanism": "Tác dụng hiệp đồng giãn phế quản, nhưng cũng tăng tác dụng phụ.",
                    "effect": "Tăng tác dụng phụ (run, tim đập nhanh, loạn nhịp tim)",
                    "management": "Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều một trong hai thuốc nếu tác dụng phụ nặng."
                }
            ],
            "minor": [
                {
                    "drug": "Lithium",
                    "mechanism": "Theophylline làm tăng đào thải lithium qua thận, giảm nồng độ lithium.",
                    "effect": "Giảm nồng độ lithium, giảm hiệu quả",
                    "management": "Tăng liều lithium khi dùng theophylline. Theo dõi nồng độ lithium. Giảm liều lithium khi ngừng theophylline."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng theophylline hoặc methylxanthines (caffeine, theobromine)",
                "Rối loạn nhịp tim nặng (rung nhĩ, rung thất)",
                "Động kinh không kiểm soát",
                "Loét dạ dày tá tràng hoạt động"
            ],
            "tương_đối": [
                "Suy gan nặng - giảm clearance, tăng nguy cơ độc tính",
                "Suy thận nặng - giảm clearance nhẹ",
                "Suy tim - giảm clearance",
                "Sốt cao - có thể giảm clearance",
                "Trẻ sơ sinh - clearance chậm, half-life dài",
                "Người già - clearance giảm",
                "Hút thuốc - tăng clearance, cần tăng liều",
                "Dùng với ciprofloxacin, erythromycin, cimetidine - tăng nồng độ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Theophylline là FDA category C. Nghiên cứu trên động vật cho thấy có thể có nguy cơ cho thai nhi. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Theophylline được sử dụng trong thai kỳ để điều trị hen suyễn. Tuy nhiên, cần theo dõi nồng độ theophylline chặt chẽ vì clearance có thể thay đổi trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Theophylline bài tiết vào sữa mẹ. Nồng độ trong sữa mẹ có thể gây tác dụng phụ ở trẻ (bồn chồn, khó ngủ).",
                "recommendation": "Có thể dùng khi cho con bú nhưng thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh (bồn chồn, khó ngủ). Cân nhắc dùng thuốc khác nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Giảm liều 25%",
            "moderate": "Giảm liều 50%",
            "severe": "Giảm liều 75% hoặc tránh dùng",
            "notes": "Theophylline chuyển hóa chủ yếu ở gan (CYP1A2). Suy gan làm giảm clearance đáng kể, tăng nguy cơ độc tính. CẦN TDM và giảm liều."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn (thường gặp đầu tiên)",
                "Run, bồn chồn",
                "Tim đập nhanh, rối loạn nhịp tim",
                "Co giật (ở nồng độ >30 mcg/mL)",
                "Rối loạn nhịp tim nặng (rung thất, ngừng tim)",
                "Tử vong (ở nồng độ rất cao)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và thanh lọc.",
            "treatment": [
                "Ngừng ngay theophylline",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ",
                "Theo dõi nồng độ theophylline trong máu",
                "Điều trị co giật: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều trị rối loạn nhịp tim: Beta-blockers (propranolol, esmolol) - thận trọng ở bệnh nhân hen suyễn",
                "Thanh lọc máu (hemodialysis, hemoperfusion): Hiệu quả ở nồng độ cao (>40 mcg/mL) hoặc có triệu chứng nặng",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Nồng độ theophylline trong máu mỗi 2-4 giờ cho đến khi <20 mcg/mL. Dấu hiệu sinh tồn, nhịp tim, dấu hiệu thần kinh (co giật) trong ít nhất 24-48 giờ."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Tránh thức ăn giàu chất béo (có thể tăng hấp thu).",
                "timing": "Uống 2-3 lần/ngày (tùy công thức). Dạng extended-release: 1-2 lần/ngày. Uống đều đặn, cách đều nhau trong ngày. Không nghiền, không nhai viên extended-release."
            },
            "iv": {
                "reconstitution": "Pha theophylline với NaCl 0.9% hoặc D5W theo hướng dẫn nhà sản xuất.",
                "infusion_rate": "Loading dose: 5-6mg/kg trong 20-30 phút. Maintenance: 0.4-0.6mg/kg/giờ truyền liên tục. KHÔNG truyền nhanh (nguy cơ độc tính).",
                "compatibility": ["NaCl 0.9%", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "CẦN TDM khi dùng IV. Theo dõi nồng độ theophylline trong máu. Điều chỉnh tốc độ truyền theo nồng độ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Theophylline",
                "UpToDate - Theophylline: Drug information",
                "American Thoracic Society guidelines",
                "Global Initiative for Asthma (GINA) guidelines"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience, TDM guidelines"
        }
    },
    
    "Aminophylline": {
        "group": "Respiratory - Methylxanthine (Bronchodilator)",
        "vietnamese_name": "Aminophylline, Theophylline ethylenediamine",
        "administration": ["IV"],
        "indications": [
            "Hen suyễn cấp tính",
            "COPD cấp tính",
            "Bronchospasm cấp tính",
            "Apnea of prematurity (trẻ sơ sinh)"
        ],
        "contraindications": [
            "Dị ứng theophylline hoặc ethylenediamine",
            "Rối loạn nhịp tim nặng",
            "Động kinh không kiểm soát",
            "Loét dạ dày tá tràng hoạt động"
        ],
        "dosage": {
            "adult_loading": "5-6mg/kg IV (tính theo theophylline) trong 20-30 phút",
            "adult_maintenance": "0.4-0.6mg/kg/giờ (tính theo theophylline) truyền liên tục",
            "pediatric_loading": "5mg/kg IV (tính theo theophylline)",
            "pediatric_maintenance": "0.5-1mg/kg/giờ IV (tính theo theophylline)",
            "notes": "Aminophylline = theophylline + ethylenediamine (2:1). 1g aminophylline = 800mg theophylline. Cần tính liều theo theophylline. CẦN TDM."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến ở nồng độ cao)",
            "Nhức đầu",
            "Run, bồn chồn",
            "Tim đập nhanh, rối loạn nhịp tim",
            "Co giật (ở nồng độ rất cao)",
            "Phản ứng dị ứng với ethylenediamine (hiếm)"
        ],
        "interactions": [
            "Ciprofloxacin, Erythromycin, Clarithromycin: tăng nồng độ theophylline",
            "Cimetidine: tăng nồng độ theophylline",
            "Rifampin: giảm nồng độ theophylline",
            "Beta-2 agonists: tăng tác dụng phụ"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Aminophylline là phức hợp của theophylline và ethylenediamine (tỷ lệ 2:1), được chuyển hóa thành theophylline trong cơ thể. 1g aminophylline tương đương 800mg theophylline. Cơ chế tác dụng giống theophylline: ức chế phosphodiesterase (PDE), làm tăng cAMP và cGMP, gây giãn phế quản. Đối kháng adenosine receptors. Aminophylline chỉ có dạng IV, dùng trong cấp cứu. Cần tính liều theo theophylline (aminophylline = theophylline × 1.25).",
        "monitoring": [
            "Nồng độ theophylline trong máu (TDM) - Target 10-20 mcg/mL",
            "Dấu hiệu độc tính: buồn nôn, nôn, run, tim đập nhanh, co giật",
            "Nhịp tim, huyết áp",
            "Chức năng gan, thận",
            "Triệu chứng lâm sàng (cải thiện khó thở)"
        ],
        "precautions": [
            "CẦN TDM - therapeutic window hẹp (10-20 mcg/mL)",
            "Tính liều theo theophylline: aminophylline = theophylline × 1.25",
            "KHÔNG truyền nhanh (nguy cơ độc tính)",
            "Nhiều yếu tố ảnh hưởng clearance",
            "Nhiều tương tác thuốc",
            "Theo dõi sát dấu hiệu độc tính"
        ],
        "pharmacokinetics": {
            "half_life": "Giống theophylline (4-8 giờ người lớn, thay đổi tùy yếu tố)",
            "onset": "15-30 phút (IV)",
            "duration": "6-12 giờ",
            "protein_binding": "40%",
            "metabolism": "Chuyển hóa thành theophylline, sau đó chuyển hóa ở gan",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất.",
        "black_box_warnings": "Therapeutic window hẹp. Nồng độ >20 mcg/mL: tăng nguy cơ độc tính. Nồng độ >30 mcg/mL: nguy cơ co giật, tử vong. CẦN TDM.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ciprofloxacin, Enoxacin",
                    "mechanism": "Ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline 2-3 lần",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: giảm liều 30-50%, TDM chặt chẽ."
                },
                {
                    "drug": "Erythromycin, Clarithromycin, Cimetidine",
                    "mechanism": "Ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline",
                    "management": "Giảm liều 25-50%, TDM."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng theophylline hoặc ethylenediamine",
                "Rối loạn nhịp tim nặng",
                "Động kinh không kiểm soát"
            ],
            "tương_đối": [
                "Suy gan/thận nặng",
                "Suy tim",
                "Nhiều tương tác thuốc"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết vào sữa mẹ. Thận trọng.",
                "recommendation": "Có thể dùng khi cho con bú, thận trọng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Giảm liều 25%",
            "moderate": "Giảm liều 50%",
            "severe": "Giảm liều 75% hoặc tránh dùng",
            "notes": "Chuyển hóa ở gan. Suy gan làm giảm clearance."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Run, tim đập nhanh",
                "Co giật (ở nồng độ >30 mcg/mL)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay aminophylline",
                "TDM",
                "Điều trị co giật: Benzodiazepine",
                "Thanh lọc máu nếu nồng độ cao (>40 mcg/mL)"
            ],
            "monitoring": "Nồng độ theophylline, dấu hiệu sinh tồn, dấu hiệu thần kinh"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - Chỉ có dạng IV",
                "timing": "N/A"
            },
            "iv": {
                "reconstitution": "Pha với NaCl 0.9% hoặc D5W",
                "infusion_rate": "Loading: 5-6mg/kg (theophylline) trong 20-30 phút. Maintenance: 0.4-0.6mg/kg/giờ truyền liên tục. KHÔNG truyền nhanh.",
                "compatibility": ["NaCl 0.9%", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "CẦN TDM. Tính liều theo theophylline (aminophylline = theophylline × 1.25)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aminophylline",
                "UpToDate - Aminophylline: Drug information",
                "American Thoracic Society guidelines"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        }
    }
}

__all__ = ['METHYLXANTHINES_DRUGS']























