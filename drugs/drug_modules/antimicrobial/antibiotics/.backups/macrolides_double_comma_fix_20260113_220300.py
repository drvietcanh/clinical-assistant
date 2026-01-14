"""
Macrolide Antibiotics
Azithromycin, Clarithromycin, Erythromycin
"""

MACROLIDE_ANTIBIOTICS = {
    "Azithromycin": {
        "group": "Antibiotic - Macrolide (Azalide)",
        "vietnamese_name": "Azithromycin, Zithromax",
        "administration": ["PO", "IV"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm phế quản cấp",
            "Nhiễm khuẩn đường hô hấp trên",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu không biến chứng",
            "Bệnh lậu (kết hợp với ceftriaxone)",
            "Chlamydia",
            "Vi khuẩn không điển hình (Mycoplasma, Legionella)"
        ],
        "contraindications": [
            "Dị ứng azithromycin",
            "Dị ứng macrolide",
            "QT kéo dài",
            "Rối loạn nhịp tim nặng",
            "Dùng với thuốc kéo dài QT"
        ],
        "dosage": {
            "adult_po_standard": "500mg PO x 1 lần/ngày x 3 ngày",
            "adult_po_5day": "500mg PO ngày đầu, sau đó 250mg PO x 1 lần/ngày x 4 ngày",
            "adult_po_single": "1g PO x 1 liều duy nhất (chlamydia, gonorrhea)",
            "adult_iv": "500mg IV x 1 lần/ngày",
            "adult_pneumonia": "500mg PO/IV x 1 lần/ngày x 5 ngày",
            "adult_chlamydia": "1g PO x 1 liều duy nhất",
            "pediatric": "10mg/kg PO x 1 lần/ngày x 3 ngày (tối đa 500mg/ngày)",
            "notes": "Ưu điểm: dùng 1 lần/ngày, liều ngắn (3-5 ngày), half-life dài (68 giờ). Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu. Có thể kéo dài QT interval."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (thải trừ chủ yếu qua gan/mật)"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn, nôn",
            "Đau bụng",
            "QT kéo dài (có thể gây rối loạn nhịp tim)",
            "Rối loạn nhịp tim (torsades de pointes) - hiếm nhưng nguy hiểm",
            "Đau đầu",
            "Chóng mặt",
            "Phát ban (hiếm)"
        ],
        "interactions": [
            "Thuốc kéo dài QT (amiodarone, sotalol, antipsychotics): tăng nguy cơ rối loạn nhịp tim",
            "Warfarin: có thể tăng INR",
            "Digoxin: có thể tăng nồng độ digoxin",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Theophylline: có thể tăng nồng độ theophylline"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Azithromycin là macrolide (azalide), kháng sinh bacteriostatic. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 50S của ribosome, ngăn chặn quá trình dịch mã. Phổ kháng khuẩn: Gram-dương (Streptococcus pneumoniae, Streptococcus pyogenes, Staphylococcus aureus - MSSA), Gram-âm (Haemophilus influenzae, Moraxella catarrhalis, Neisseria gonorrhoeae), và vi khuẩn không điển hình (Mycoplasma pneumoniae, Chlamydia trachomatis, Chlamydia pneumoniae, Legionella pneumophila). Không hiệu quả với Enterococcus, Enterobacteriaceae, Pseudomonas. Đặc điểm: half-life rất dài (68 giờ), dùng 1 lần/ngày, liều ngắn (3-5 ngày), có thể kéo dài QT interval, ít tương tác thuốc hơn erythromycin.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có)",
            "ECG - QT interval (nếu có yếu tố nguy cơ hoặc dùng với thuốc kéo dài QT)",
            "Dấu hiệu rối loạn nhịp tim (palpitations, chóng mặt, ngất)",
            "Dấu hiệu tiêu chảy - phổ biến",
            "PT/INR (nếu dùng với warfarin)",
            "Nồng độ digoxin (nếu đang dùng)"
        ],
        "precautions": [
            "QT kéo dài - không dùng với các thuốc kéo dài QT khác, bệnh nhân có tiền sử rối loạn nhịp",
            "Theo dõi ECG nếu có yếu tố nguy cơ hoặc dùng với thuốc kéo dài QT",
            "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu",
            "Ưu điểm: dùng 1 lần/ngày, liều ngắn (3-5 ngày), compliance tốt",
            "Theo dõi INR nếu dùng với warfarin",
            "Theo dõi nồng độ digoxin nếu đang dùng",
            "Tiêu chảy phổ biến - có thể cần điều trị hỗ trợ"
        ],
        "pharmacokinetics": {
            "half_life": "68 giờ (rất dài, cho phép dùng 1 lần/ngày và liều ngắn)",
            "onset": "2-3 giờ sau khi uống",
            "duration": "24 giờ (dùng 1 lần/ngày), tác dụng kéo dài sau khi ngừng (do half-life dài)",
            "protein_binding": "7-50%",
            "metabolism": "Chuyển hóa một phần ở gan",
            "clearance": "Chủ yếu qua gan/mật (50-60%), một phần qua thận (12%), không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Viên nén/viên nang: bảo quản trong bao bì kín. Suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng.",
        "black_box_warnings": "Có thể kéo dài QT interval và gây rối loạn nhịp tim nghiêm trọng (torsades de pointes). Không dùng với các thuốc kéo dài QT khác. Theo dõi ECG nếu có yếu tố nguy cơ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics, Fluoroquinolones)",
                    "mechanism": "Cả hai đều kéo dài QT interval, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ kéo dài QT nặng, rối loạn nhịp tim (torsades de pointes), có thể tử vong",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi ECG chặt chẽ. Theo dõi QT interval."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Azithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm sản xuất vitamin K",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng azithromycin). Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Azithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim)",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Có thể cần giảm liều digoxin."
                }
            ],
            "minor": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Azithromycin có thể ức chế chuyển hóa cyclosporine",
                    "effect": "Tăng nồng độ cyclosporine",
                    "management": "Theo dõi nồng độ cyclosporine. Có thể cần giảm liều cyclosporine."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng azithromycin hoặc macrolide",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy tim - tăng nguy cơ QT kéo dài",
                "Bệnh nhân >60 tuổi - tăng nguy cơ QT kéo dài",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với digoxin - tăng độc tính digoxin"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng azithromycin hoặc macrolide",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy tim - tăng nguy cơ QT kéo dài",
                "Bệnh nhân >60 tuổi - tăng nguy cơ QT kéo dài",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với digoxin - tăng độc tính digoxin"
            ]
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có QT kéo dài hoặc phản ứng dị ứng nghiêm trọng."},
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Azithromycin là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Được sử dụng trong thai kỳ để điều trị chlamydia và các nhiễm trùng khác.",
            "lactation": {
                "safety": "Compatible",
                "details": "Azithromycin bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa một phần ở gan)",
            "severe": "Thận trọng, có thể tích lũy (chuyển hóa giảm)",
            "notes": "Azithromycin chuyển hóa một phần ở gan và thải trừ chủ yếu qua gan/mật. Suy gan có thể giảm chuyển hóa và tích lũy. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "QT kéo dài nặng",
                "Rối loạn nhịp tim (torsades de pointes) - NGUY HIỂM"
            ],
            "antidote": "Magnesium sulfate cho torsades de pointes. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng azithromycin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV",
                "  - Điều chỉnh điện giải (K+, Mg2+)",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "Theo dõi: ECG, dấu hiệu sinh tồn, điện giải"
            ],
            "monitoring": "Theo dõi ECG (QT interval), dấu hiệu sinh tồn, điện giải (K+, Mg2+) trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có QT kéo dài hoặc phản ứng dị ứng nghiêm trọng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu. Có thể uống với thức ăn nếu kích ứng dạ dày nhưng giảm hấp thu.",
                "timing": "Standard: 500mg PO x 1 lần/ngày x 3 ngày. Hoặc 500mg PO ngày đầu, sau đó 250mg PO x 1 lần/ngày x 4 ngày. Single dose: 1g PO x 1 liều duy nhất (chlamydia, gonorrhea). Uống đều đặn, cùng một thời điểm mỗi ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-2mg/ml. Pha 500mg trong 250ml = 2mg/ml. Pha 500mg trong 500ml = 1mg/ml.",
                "infusion_rate": "Truyền IV trong 60 phút. Tốc độ: 250ml/60 phút = ~4.2ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Thuốc kéo dài QT - tăng nguy cơ rối loạn nhịp tim",
                    "Không trộn với các thuốc khác"
                ],
                "notes": "QUAN TRỌNG: 1) Dùng 1 lần/ngày, liều ngắn (3-5 ngày), 2) Có thể kéo dài QT interval - theo dõi ECG, 3) Uống khi đói (PO), 4) Không dùng với thuốc kéo dài QT."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Azithromycin (Zithromax)",
                "IDSA Guidelines - Community-Acquired Pneumonia",
                "UpToDate - Azithromycin: Drug Information",
                "Medscape - Azithromycin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"cardiac": "High (QT prolongation, torsades de pointes)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "CDC Guidelines - Sexually Transmitted Diseases (Chlamydia, Gonorrhea)",
            "IDSA Guidelines - Traveler's Diarrhea",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Clarithromycin": {
        "group": "Antibiotic - Macrolide",
        "vietnamese_name": "Clarithromycin, Klacid, Biaxin",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm phế quản cấp",
            "Nhiễm khuẩn đường hô hấp trên",
            "Nhiễm khuẩn da và mô mềm",
            "Helicobacter pylori (kết hợp với PPI và amoxicillin/metronidazole)",
            "Vi khuẩn không điển hình (Mycoplasma, Legionella)"
        ],
        "contraindications": [
            "Dị ứng clarithromycin",
            "Dị ứng macrolide",
            "QT kéo dài",
            "Rối loạn nhịp tim nặng",
            "Dùng với thuốc kéo dài QT",
            "Dùng với cisapride, pimozide, terfenadine - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_standard": "250-500mg PO x 2 lần/ngày",
            "adult_severe": "500mg PO x 2 lần/ngày",
            "adult_pneumonia": "500mg PO x 2 lần/ngày x 7-14 ngày",
            "adult_hpylori": "500mg PO x 2 lần/ngày (kết hợp với PPI và amoxicillin/metronidazole)",
            "pediatric": "7.5mg/kg PO x 2 lần/ngày (tối đa 500mg mỗi liều)",
            "notes": "Uống với hoặc không thức ăn. Dùng 2 lần/ngày. Có thể kéo dài QT interval. Nhiều tương tác thuốc (ức chế CYP3A4)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "250mg PO x 2 lần/ngày hoặc 500mg PO x 1 lần/ngày",
            "under_30": "250mg PO x 1 lần/ngày",
            "hemodialysis": "250mg PO x 1 lần/ngày"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Vị kim loại (metallic taste) - phổ biến",
            "QT kéo dài (có thể gây rối loạn nhịp tim)",
            "Rối loạn nhịp tim (torsades de pointes) - hiếm nhưng nguy hiểm",
            "Đau đầu",
            "Phát ban (hiếm)"
        ],
        "interactions": [
            "Thuốc kéo dài QT (amiodarone, sotalol, antipsychotics): tăng nguy cơ rối loạn nhịp tim",
            "Cisapride, pimozide, terfenadine: CHỐNG CHỈ ĐỊNH (tăng nguy cơ tử vong)",
            "Warfarin: tăng INR",
            "Digoxin: tăng nồng độ digoxin",
            "Theophylline: tăng nồng độ theophylline",
            "Carbamazepine: tăng nồng độ carbamazepine",
            "Statins (atorvastatin, simvastatin): tăng nguy cơ tiêu cơ vân",
            "CYP3A4 substrates: tăng nồng độ (ức chế CYP3A4)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Clarithromycin là macrolide kháng sinh bacteriostatic. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 50S của ribosome, ngăn chặn quá trình dịch mã. Phổ kháng khuẩn: Gram-dương (Streptococcus pneumoniae, Streptococcus pyogenes, Staphylococcus aureus - MSSA), Gram-âm (Haemophilus influenzae, Moraxella catarrhalis), và vi khuẩn không điển hình (Mycoplasma pneumoniae, Chlamydia pneumoniae, Legionella pneumophila, Helicobacter pylori). Không hiệu quả với Enterococcus, Enterobacteriaceae, Pseudomonas. Đặc điểm: dùng 2 lần/ngày, có thể kéo dài QT interval, ức chế CYP3A4 mạnh (nhiều tương tác thuốc), vị kim loại phổ biến.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có)",
            "ECG - QT interval (nếu có yếu tố nguy cơ hoặc dùng với thuốc kéo dài QT)",
            "Dấu hiệu rối loạn nhịp tim",
            "PT/INR (nếu dùng với warfarin)",
            "Nồng độ digoxin, theophylline, carbamazepine (nếu đang dùng)",
            "CPK (nếu dùng với statins)"
        ],
        "precautions": [
            "QT kéo dài - không dùng với các thuốc kéo dài QT khác",
            "CHỐNG CHỈ ĐỊNH với cisapride, pimozide, terfenadine - tăng nguy cơ tử vong",
            "Ức chế CYP3A4 mạnh - nhiều tương tác thuốc",
            "Theo dõi ECG nếu có yếu tố nguy cơ",
            "Vị kim loại phổ biến - có thể ảnh hưởng chất lượng cuộc sống",
            "Điều chỉnh liều theo chức năng thận",
            "Theo dõi INR nếu dùng với warfarin",
            "Theo dõi nồng độ các thuốc chuyển hóa qua CYP3A4"
        ],
        "pharmacokinetics": {
            "half_life": "3-7 giờ",
            "onset": "2-3 giờ sau khi uống",
            "duration": "q12h (dùng 2 lần/ngày)",
            "protein_binding": "42-70%",
            "metabolism": "Chuyển hóa ở gan (CYP3A4) - ức chế CYP3A4 mạnh",
            "clearance": "Gan (chuyển hóa) và thận (20-30% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Viên nén/viên nang: bảo quản trong bao bì kín.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với cisapride, pimozide, terfenadine - tăng nguy cơ tử vong do rối loạn nhịp tim. Có thể kéo dài QT interval và gây rối loạn nhịp tim nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cisapride, Pimozide, Terfenadine",
                    "mechanism": "Clarithromycin ức chế CYP3A4, làm tăng nồng độ các thuốc này, gây kéo dài QT nặng",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim nghiêm trọng, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng đồng thời."
                },
                {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics)",
                    "mechanism": "Cả hai đều kéo dài QT interval, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim nghiêm trọng",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi ECG chặt chẽ."
                },
                {
                    "drug": "Statins (Atorvastatin, Simvastatin)",
                    "mechanism": "Clarithromycin ức chế CYP3A4, làm tăng nồng độ statins",
                    "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis), suy thận",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, ngừng statin hoặc dùng statin không chuyển hóa qua CYP3A4 (pravastatin, rosuvastatin). Theo dõi CPK."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Clarithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột và chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Clarithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng độc tính",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Clarithromycin có thể ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính",
                    "management": "Theo dõi nồng độ theophylline và dấu hiệu độc tính. Có thể cần giảm liều theophylline."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng clarithromycin hoặc macrolide",
                "Dùng với cisapride, pimozide, terfenadine - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy thận nặng - giảm liều",
                "Suy gan nặng - thận trọng",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với statins - tăng nguy cơ tiêu cơ vân",
                "Dùng với các thuốc chuyển hóa qua CYP3A4 - tăng nồng độ"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng clarithromycin hoặc macrolide",
                "Dùng với cisapride, pimozide, terfenadine - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy thận nặng - giảm liều",
                "Suy gan nặng - thận trọng",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với statins - tăng nguy cơ tiêu cơ vân",
                "Dùng với các thuốc chuyển hóa qua CYP3A4 - tăng nồng độ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Clarithromycin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Clarithromycin bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa qua gan)",
            "severe": "Thận trọng, có thể tích lũy (chuyển hóa giảm)",
            "notes": "Clarithromycin chuyển hóa ở gan (CYP3A4). Suy gan có thể giảm chuyển hóa và tích lũy. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "QT kéo dài nặng",
                "Rối loạn nhịp tim (torsades de pointes) - NGUY HIỂM"
            ],
            "antidote": "Magnesium sulfate cho torsades de pointes. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng clarithromycin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV",
                "  - Điều chỉnh điện giải",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Điều trị triệu chứng tiêu hóa",
                "Theo dõi: ECG, dấu hiệu sinh tồn"
            ],
            "monitoring": "Theo dõi ECG (QT interval), dấu hiệu sinh tồn trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có QT kéo dài hoặc phản ứng dị ứng nghiêm trọng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 2 lần/ngày (q12h), thường 250-500mg mỗi lần. Uống đều đặn, cách đều nhau trong ngày (12 giờ)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Clarithromycin (Biaxin)",
                "IDSA Guidelines - Community-Acquired Pneumonia",
                "UpToDate - Clarithromycin: Drug Information",
                "Medscape - Clarithromycin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"cardiac": "High (QT prolongation, torsades de pointes)", "hepatic": "Moderate", "musculoskeletal": "Moderate (rhabdomyolysis with statins)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "ACG Guidelines - Helicobacter pylori Treatment",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Erythromycin": {
        "group": "Antibiotic - Macrolide",
        "vietnamese_name": "Erythromycin, Erythrocin",
        "administration": ["PO", "IV"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm phế quản cấp",
            "Nhiễm khuẩn đường hô hấp trên",
            "Nhiễm khuẩn da và mô mềm",
            "Chlamydia",
            "Bệnh lậu (kết hợp)",
            "Vi khuẩn không điển hình (Mycoplasma, Legionella)",
            "Dự phòng viêm nội tâm mạc (ở bệnh nhân dị ứng penicillin)"
        ],
        "contraindications": [
            "Dị ứng erythromycin",
            "Dị ứng macrolide",
            "QT kéo dài",
            "Rối loạn nhịp tim nặng",
            "Dùng với thuốc kéo dài QT",
            "Dùng với cisapride, pimozide, terfenadine - CHỐNG CHỈ ĐỊNH",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_po_standard": "250-500mg PO x 4 lần/ngày",
            "adult_po_eryc": "250-500mg PO x 2 lần/ngày (dạng enteric-coated)",
            "adult_iv": "500mg-1g IV mỗi 6 giờ",
            "adult_chlamydia": "500mg PO x 4 lần/ngày x 7 ngày",
            "adult_prophylaxis": "1g PO x 1 liều trước thủ thuật",
            "pediatric": "30-50mg/kg/ngày PO chia 3-4 lần (tối đa 2g/ngày)",
            "notes": "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu. Dạng enteric-coated (eryc) có thể uống với thức ăn. Dùng 3-4 lần/ngày. Nhiều tương tác thuốc (ức chế CYP3A4 mạnh)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (thải trừ chủ yếu qua gan/mật)"
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến, đặc biệt với dạng không enteric-coated)",
            "Tiêu chảy",
            "Đau bụng",
            "QT kéo dài (có thể gây rối loạn nhịp tim)",
            "Rối loạn nhịp tim (torsades de pointes) - hiếm nhưng nguy hiểm",
            "Viêm gan (hiếm, đặc biệt với dạng estolate)",
            "Điếc tạm thời (hiếm, ở liều cao)",
            "Phát ban (hiếm)"
        ],
        "interactions": [
            "Thuốc kéo dài QT (amiodarone, sotalol, antipsychotics): tăng nguy cơ rối loạn nhịp tim",
            "Cisapride, pimozide, terfenadine: CHỐNG CHỈ ĐỊNH (tăng nguy cơ tử vong)",
            "Warfarin: tăng INR",
            "Digoxin: tăng nồng độ digoxin",
            "Theophylline: tăng nồng độ theophylline",
            "Carbamazepine: tăng nồng độ carbamazepine",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Statins (atorvastatin, simvastatin): tăng nguy cơ tiêu cơ vân",
            "CYP3A4 substrates: tăng nồng độ (ức chế CYP3A4 mạnh)",
            "Clindamycin: đối kháng (không dùng cùng)"
        ],,
"pregnancy": "B",
        "mechanism_of_action": "Erythromycin là macrolide kháng sinh bacteriostatic đầu tiên. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 50S của ribosome, ngăn chặn quá trình dịch mã. Phổ kháng khuẩn: Gram-dương (Streptococcus pneumoniae, Streptococcus pyogenes, Staphylococcus aureus - MSSA), Gram-âm (Haemophilus influenzae, Moraxella catarrhalis, Neisseria gonorrhoeae), và vi khuẩn không điển hình (Mycoplasma pneumoniae, Chlamydia trachomatis, Chlamydia pneumoniae, Legionella pneumophila). Không hiệu quả với Enterococcus, Enterobacteriaceae, Pseudomonas. Đặc điểm: macrolide cổ điển, dùng 3-4 lần/ngày, nhiều tương tác thuốc (ức chế CYP3A4 mạnh), buồn nôn/nôn phổ biến, ít được dùng hơn azithromycin/clarithromycin do tác dụng phụ và tương tác thuốc nhiều hơn.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có)",
            "ECG - QT interval (nếu có yếu tố nguy cơ)",
            "Dấu hiệu rối loạn nhịp tim",
            "Dấu hiệu buồn nôn, nôn - phổ biến",
            "Chức năng gan (ALT, AST) - đặc biệt với dạng estolate",
            "PT/INR (nếu dùng với warfarin)",
            "Nồng độ digoxin, theophylline, carbamazepine (nếu đang dùng)"
        ],
        "precautions": [
            "Buồn nôn, nôn phổ biến - dùng dạng enteric-coated để giảm",
            "QT kéo dài - không dùng với các thuốc kéo dài QT khác",
            "CHỐNG CHỈ ĐỊNH với cisapride, pimozide, terfenadine",
            "Ức chế CYP3A4 mạnh - nhiều tương tác thuốc",
            "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu (trừ dạng enteric-coated)",
            "Viêm gan với dạng estolate - tránh dùng ở suy gan",
            "Điếc tạm thời ở liều cao - ngừng nếu có",
            "Đối kháng với clindamycin - không dùng cùng",
            "Theo dõi INR nếu dùng với warfarin",
            "Theo dõi nồng độ các thuốc chuyển hóa qua CYP3A4"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ",
            "onset": "1-2 giờ sau khi uống",
            "duration": "q6h (dùng 4 lần/ngày)",
            "protein_binding": "70-90%",
            "metabolism": "Chuyển hóa ở gan (CYP3A4) - ức chế CYP3A4 mạnh",
            "clearance": "Chủ yếu qua gan/mật (80-90%), một phần qua thận (5-15%), không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Viên nén/viên nang: bảo quản trong bao bì kín.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với cisapride, pimozide, terfenadine - tăng nguy cơ tử vong do rối loạn nhịp tim. Có thể kéo dài QT interval và gây rối loạn nhịp tim nghiêm trọng. Viêm gan với dạng estolate - tránh dùng ở suy gan.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cisapride, Pimozide, Terfenadine",
                    "mechanism": "Erythromycin ức chế CYP3A4, làm tăng nồng độ các thuốc này, gây kéo dài QT nặng",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim nghiêm trọng, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng đồng thời."
                },
                {
                    "drug": "Clindamycin",
                    "mechanism": "Cả hai đều gắn với tiểu phần 50S của ribosome, đối kháng cạnh tranh",
                    "effect": "Giảm hiệu quả kháng khuẩn của cả hai thuốc",
                    "management": "TRÁNH DÙNG đồng thời. Chọn một trong hai thuốc."
                },
                {
                    "drug": "Statins (Atorvastatin, Simvastatin)",
                    "mechanism": "Erythromycin ức chế CYP3A4, làm tăng nồng độ statins",
                    "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis)",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, ngừng statin hoặc dùng statin không chuyển hóa qua CYP3A4."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Erythromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột và chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Erythromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng độc tính",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Erythromycin có thể ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính",
                    "management": "Theo dõi nồng độ theophylline và dấu hiệu độc tính."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng erythromycin hoặc macrolide",
                "Dùng với cisapride, pimozide, terfenadine - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH",
                "Suy gan nặng (với dạng estolate)"
            ],
            "tương_đối": [
                "Suy gan - thận trọng, đặc biệt với dạng estolate",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với statins - tăng nguy cơ tiêu cơ vân",
                "Dùng với các thuốc chuyển hóa qua CYP3A4 - tăng nồng độ"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng erythromycin hoặc macrolide",
                "Dùng với cisapride, pimozide, terfenadine - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH",
                "Suy gan nặng (với dạng estolate)"
            ],
            "tương_đối": [
                "Suy gan - thận trọng, đặc biệt với dạng estolate",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với statins - tăng nguy cơ tiêu cơ vân",
                "Dùng với các thuốc chuyển hóa qua CYP3A4 - tăng nồng độ"
            ]
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có QT kéo dài hoặc phản ứng dị ứng nghiêm trọng."},
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Erythromycin là thuốc phân loại B. An toàn trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Erythromycin bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa qua gan)",
            "severe": "CHỐNG CHỈ ĐỊNH hoặc thận trọng tối đa (đặc biệt với dạng estolate - nguy cơ viêm gan)",
            "notes": "Erythromycin chuyển hóa ở gan (CYP3A4). Suy gan có thể giảm chuyển hóa và tích lũy. Dạng estolate có nguy cơ viêm gan cao hơn. CHỐNG CHỈ ĐỊNH ở suy gan nặng với dạng estolate."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "QT kéo dài nặng",
                "Rối loạn nhịp tim (torsades de pointes) - NGUY HIỂM",
                "Điếc tạm thời (ở liều cao)",
                "Viêm gan (với dạng estolate)"
            ],
            "antidote": "Magnesium sulfate cho torsades de pointes. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng erythromycin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV",
                "  - Điều chỉnh điện giải",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Điều trị triệu chứng tiêu hóa",
                "Nếu điếc: ngừng ngay, thường tự hồi phục",
                "Nếu viêm gan: điều trị hỗ trợ gan",
                "Theo dõi: ECG, dấu hiệu sinh tồn, chức năng gan"
            ],
            "monitoring": "Theo dõi ECG (QT interval), dấu hiệu sinh tồn, chức năng gan trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có QT kéo dài, độc tính gan, hoặc phản ứng dị ứng nghiêm trọng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu. Dạng enteric-coated (eryc) có thể uống với thức ăn.",
                "timing": "Uống 3-4 lần/ngày (q6-8h), thường 250-500mg mỗi lần. Uống đều đặn, cách đều nhau trong ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-5mg/ml.",
                "infusion_rate": "Truyền IV trong 20-60 phút. Tốc độ: 100ml/60 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Thuốc kéo dài QT - tăng nguy cơ rối loạn nhịp tim",
                    "Không trộn với các thuốc khác"
                ],
                "notes": "QUAN TRỌNG: 1) Dùng 4 lần/ngày, 2) Nhiều tương tác thuốc (ức chế CYP3A4), 3) Buồn nôn/nôn phổ biến, 4) CHỐNG CHỈ ĐỊNH với cisapride, pimozide, terfenadine."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Erythromycin",
                "UpToDate - Erythromycin: Drug Information",
                "Medscape - Erythromycin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"cardiac": "High (QT prolongation, torsades de pointes)", "hepatic": "Moderate", "gastrointestinal": "High (GI side effects)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "AHA Guidelines - Infective Endocarditis Prophylaxis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
}

__all__ = ['MACROLIDE_ANTIBIOTICS']

