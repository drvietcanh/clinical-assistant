"""
Fluoroquinolone Antibiotics
"""
FLUOROQUINOLONE_ANTIBIOTICS = {
    "Levofloxacin": {
    "group": "Antibiotic - Fluoroquinolone",
    "vietnamese_name": "Levofloxacin, Tavanic",
    "administration": ["PO", "IV"],
    "indications": [
        "Viêm phổi cộng đồng",
        "Nhiễm khuẩn đường tiết niệu phức tạp",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm xoang",
        "Viêm tuyến tiền liệt do vi khuẩn"
    ],
    "contraindications": [
        "Dị ứng fluoroquinolone",
        "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
        "Có thai"
    ],
    "dosage": {
        "adult_po": "500-750mg x 1 lần/ngày",
        "adult_iv": "500-750mg IV x 1 lần/ngày",
        "adult_pneumonia": "500-750mg x 1 lần/ngày x 7-14 ngày",
        "notes": "Uống với nhiều nước. Tránh antacid, sắt trong 2 giờ"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "250-500mg x 1 lần/ngày"
    },
    "side_effects": [
        "Rối loạn tiêu hóa",
        "Nhức đầu",
        "Rối loạn giấc ngủ",
        "Rối loạn gân (viêm gân, đứt gân)",
        "QT kéo dài",
        "Hạ đường huyết (hiếm)"
    ],
    "interactions": [
        "Antacid/Sắt: giảm hấp thu",
        "Warfarin: tăng nguy cơ chảy máu",
        "Corticosteroid: tăng nguy cơ đứt gân"
    ],
    "pregnancy": "C",
    "mechanism_of_action": "Levofloxacin là fluoroquinolone kháng sinh phổ rộng, là enantiomer L của ofloxacin. Ức chế DNA gyrase (ở vi khuẩn Gram-âm) và topoisomerase IV (ở vi khuẩn Gram-dương), enzyme cần thiết cho sao chép và sửa chữa DNA. Dẫn đến tổn thương DNA và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, H. influenzae, Neisseria), một số Gram-dương (Streptococcus pneumoniae - kể cả penicillin-resistant), và vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Ưu điểm: dùng 1 lần/ngày (half-life dài hơn ciprofloxacin), tác dụng tốt với viêm phổi",
    "monitoring": [
        "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
        "Cấy máu và cấy từ vị trí nhiễm trùng",
        "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào",
        "Thần kinh trung ương (mất ngủ, lo âu, kích động, co giật)",
        "Tim mạch (QT kéo dài, rối loạn nhịp tim) - ECG nếu có yếu tố nguy cơ",
        "Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)",
        "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
        "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
    ],
    "precautions": [
        "NGỪNG NGAY nếu có đau, sưng gân (nguy cơ đứt gân, đặc biệt gân Achilles)",
        "Nguy cơ đứt gân tăng ở: > 60 tuổi, dùng corticosteroid, ghép tạng, hoạt động thể lực",
        "QT kéo dài → không dùng với các thuốc kéo dài QT khác, bệnh nhân có tiền sử rối loạn nhịp",
        "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID",
        "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng",
        "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm (cách 2 giờ)",
        "Hạ đường huyết → thận trọng với sulfonylurea",
        "Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn",
        "Điều chỉnh liều khi suy thận (giảm liều khi CrCl <50)",
        "Uống nhiều nước để tránh kết tinh trong nước tiểu",
        "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn ciprofloxacin)"
    ],
    "pharmacokinetics": {
        "half_life": "6-8 giờ (dài hơn ciprofloxacin)",
        "onset": "1-2 giờ (PO), ngay lập tức (IV)",
        "duration": "q24h (1 lần/ngày)",
        "protein_binding": "24-38%",
        "clearance": "Thận (chủ yếu, 80-90% thải nguyên dạng qua nước tiểu), gan (chuyển hóa ít)"
    },
    "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất",
    "black_box_warnings": "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc. Ngừng ngay nếu có đau, sưng gân. Nguy cơ tăng ở > 60 tuổi, dùng corticosteroid, ghép tạng. QT kéo dài có thể gây rối loạn nhịp tim nghiêm trọng",
    "drug_interactions": {
        "major": [
            {
                "drug": "Antacids (Aluminum, Magnesium), Sucralfate, Sắt, Kẽm",
                "mechanism": "Cation (Al3+, Mg2+, Fe2+, Zn2+) tạo phức hợp không hòa tan với levofloxacin, giảm hấp thu.",
                "effect": "Giảm hấp thu levofloxacin, giảm nồng độ trong máu, giảm hiệu quả điều trị",
                "management": "Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống levofloxacin. Không uống cùng lúc."
            },
            {
                "drug": "Warfarin",
                "mechanism": "Levofloxacin có thể ảnh hưởng đến chuyển hóa warfarin.",
                "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng levofloxacin. Điều chỉnh liều warfarin nếu cần."
            }
        ],
        "moderate": [
            {
                "drug": "Corticosteroid",
                "mechanism": "Cả hai đều tăng nguy cơ đứt gân, tác dụng cộng dồn.",
                "effect": "Tăng nguy cơ viêm gân, đứt gân",
                "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu đau, sưng gân. Ngừng ngay nếu có đau gân."
            },
            {
                "drug": "NSAID",
                "mechanism": "Cả hai đều có thể gây co giật, tác dụng cộng dồn.",
                "effect": "Tăng nguy cơ co giật",
                "management": "Tránh dùng đồng thời nếu có thể. Thận trọng ở bệnh nhân có tiền sử co giật."
            },
            {
                "drug": "Sulfonylurea",
                "mechanism": "Levofloxacin có thể gây hạ đường huyết.",
                "effect": "Tăng nguy cơ hạ đường huyết",
                "management": "Theo dõi đường huyết. Điều chỉnh liều sulfonylurea nếu cần."
            }
        ],
        "minor": []
    },
    "contraindications": {
        "tuyệt_đối": [
            "Dị ứng levofloxacin hoặc các fluoroquinolone khác",
            "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
            "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn, viêm khớp",
            "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng"
        ],
        "tương_đối": [
            "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân",
            "Dùng corticosteroid - tăng nguy cơ đứt gân",
            "Ghép cơ quan - tăng nguy cơ đứt gân",
            "Tiền sử co giật - tăng nguy cơ co giật",
            "Suy thận nặng (CrCl <30) - giảm liều đáng kể",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
        ]
    },
    "pregnancy_lactation": {
        "fda_category": "C",
        "pregnancy_details": "Levofloxacin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể gây tổn thương sụn ở khớp ở thai nhi. Có báo cáo về tổn thương sụn ở trẻ em khi dùng trong thai kỳ. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng và không có lựa chọn khác. Nhiễm trùng nặng có thể gây nguy hiểm cho thai nhi, nhưng nên dùng kháng sinh khác nếu có thể.",
        "lactation": {
            "safety": "Compatible (với thận trọng)",
            "details": "Levofloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, fluoroquinolone có thể gây tổn thương sụn ở trẻ sơ sinh.",
            "recommendation": "Có thể dùng khi cho con bú với thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh. Tránh dùng nếu có lựa chọn khác."
        }
    },
    "hepatic_adjustment": {
        "mild": "Không cần điều chỉnh liều. Levofloxacin chuyển hóa ít qua gan, thải trừ chủ yếu qua thận.",
        "moderate": "Không cần điều chỉnh liều. Thận trọng nếu có suy thận kèm theo.",
        "severe": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
        "notes": "Levofloxacin chuyển hóa ít qua gan, thải trừ chủ yếu qua thận (80-90% nguyên dạng). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
    },
    "overdose_management": {
        "symptoms": [
            "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
            "Triệu chứng thần kinh: Co giật, kích động, lo âu, mất ngủ, trầm cảm, rối loạn tâm thần",
            "Triệu chứng gân: Đau gân, viêm gân, đứt gân (đặc biệt gân Achilles)",
            "Triệu chứng tim mạch: QT kéo dài, rối loạn nhịp tim, có thể gây tử vong",
            "Triệu chứng chuyển hóa: Hạ hoặc tăng đường huyết",
            "Triệu chứng nghiêm trọng: Rối loạn nhịp tim nghiêm trọng, đứt gân"
        ],
        "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
        "treatment": [
            "Ngừng ngay levofloxacin",
            "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
            "Điều trị co giật nếu có: Benzodiazepine, theo dõi thần kinh chặt chẽ",
            "Điều trị rối loạn nhịp tim nếu có: Theo dõi ECG liên tục, điều trị loạn nhịp nếu cần",
            "Điều trị đau gân nếu có: Ngừng ngay, nghỉ ngơi, chườm lạnh, thuốc giảm đau nếu cần",
            "Điều trị hạ đường huyết nếu có: Truyền glucose, theo dõi đường huyết",
            "Điều trị triệu chứng tiêu hóa: Chống nôn nếu cần, truyền dịch nếu mất nước"
        ],
        "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG, dấu hiệu thần kinh, dấu hiệu gân, đường huyết trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng."
    },
    "reversal_agents": None,
    "administration_instructions": {
        "oral": {
            "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để tránh kết tinh trong nước tiểu.",
            "timing": "Uống 1 lần/ngày (q24h), cùng một thời điểm mỗi ngày. Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống antacid, sucralfate, sắt, kẽm. Không uống cùng lúc với các cation này. Ưu điểm: dùng 1 lần/ngày, compliance tốt hơn ciprofloxacin."
        },
        "iv": {
            "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 5mg/ml (tối đa). Pha 500mg trong 100ml dịch = 5mg/ml. Pha 750mg trong 150ml dịch = 5mg/ml.",
            "infusion_rate": "Truyền trong 60 phút (ít nhất 60 phút). Không truyền quá nhanh. Tốc độ: 100ml/60 phút = ~1.7ml/phút. 150ml/60 phút = ~2.5ml/phút.",
            "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
            "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với cation (Al3+, Mg2+, Ca2+)."],
            "notes": "Theo dõi chức năng thận, dấu hiệu gân, thần kinh trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần. Liều: 500-750mg x 1 lần/ngày (q24h)."
        }
    },
    "references": {
        "primary_sources": [
            "FDA Drug Label - Levofloxacin (Tavanic)",
            "UpToDate - Levofloxacin: Drug Information",
            "Medscape - Levofloxacin Drug Reference",
            "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
            "Lexicomp Online - Levofloxacin Monograph",
            "Micromedex - Levofloxacin Drug Information",
            "IDSA Guidelines - Antimicrobial Therapy"
        ],
        "last_updated": "2024-12-19",
        "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
    }    }
}

__all__ = ['FLUOROQUINOLONE_ANTIBIOTICS']
