"""
Oxazolidinone Antibiotics
Linezolid
"""

OXAZOLIDINONE_ANTIBIOTICS = {
    "Linezolid": {
        "group": "Antibiotic - Oxazolidinone",
        "vietnamese_name": "Linezolid, Zyvox",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn do VRE (Vancomycin-resistant Enterococcus)",
            "Nhiễm khuẩn do MRSA (Methicillin-resistant Staphylococcus aureus)",
            "Viêm phổi bệnh viện do MRSA",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "Nhiễm khuẩn huyết do Gram-dương kháng"
        ],
        "contraindications": [
            "Dị ứng linezolid",
            "Dùng với MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
            "Dùng với SSRI/SNRI (tăng nguy cơ hội chứng serotonin)",
            "Dùng với pimozide, buspirone (tăng nguy cơ hội chứng serotonin)"
        ],
        "dosage": {
            "adult_standard": "600mg PO/IV x 2 lần/ngày",
            "adult_po": "600mg PO x 2 lần/ngày",
            "adult_iv": "600mg IV x 2 lần/ngày",
            "pediatric_po": "10mg/kg PO x 3 lần/ngày (tối đa 600mg mỗi liều)",
            "pediatric_iv": "10mg/kg IV x 3 lần/ngày (tối đa 600mg mỗi liều)",
            "notes": "Dùng 2-3 lần/ngày. Có thể chuyển từ IV sang PO (100% bioavailability). Thời gian điều trị: thường 10-14 ngày, tối đa 28 ngày (nguy cơ độc tính tăng khi dùng >28 ngày)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (không cần điều chỉnh liều ở suy thận)",
            "hemodialysis": "Bổ sung 200mg sau mỗi lần lọc máu (do một phần bị loại bỏ qua lọc máu)"
        },
        "side_effects": [
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến, đặc biệt khi dùng >14 ngày",
            "Giảm bạch cầu (neutropenia) - hiếm",
            "Thiếu máu - hiếm",
            "Viêm dây thần kinh ngoại biên (peripheral neuropathy) - hiếm, thường khi dùng kéo dài",
            "Viêm dây thần kinh thị giác (optic neuropathy) - hiếm, có thể không hồi phục",
            "Hội chứng serotonin - khi dùng với SSRI/SNRI/MAO inhibitors",
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Đau đầu"
        ],
        "interactions": [
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (nguy hiểm)",
            "MAO inhibitors: tăng nguy cơ hội chứng serotonin (chống chỉ định)",
            "Tramadol: tăng nguy cơ hội chứng serotonin",
            "Warfarin: có thể tăng INR",
            "Phenytoin: có thể tăng nồng độ phenytoin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Linezolid là oxazolidinone kháng sinh, ức chế tổng hợp protein vi khuẩn bằng cách gắn với 50S ribosomal subunit, ngăn chặn sự hình thành phức hợp khởi đầu (initiation complex) 70S ribosome. Dẫn đến ngừng tổng hợp protein và ức chế sự phát triển của vi khuẩn. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - kể cả MRSA, Staphylococcus epidermidis, Streptococcus pneumoniae, Enterococcus - kể cả VRE), không có hoạt tính với Gram-âm. Đặc điểm: ức chế MAO (monoamine oxidase), dẫn đến nguy cơ hội chứng serotonin khi dùng với SSRI/SNRI/MAO inhibitors. 100% bioavailability khi uống (có thể chuyển từ IV sang PO).",
        "monitoring": [
            "Công thức máu (CBC) - HÀNG TUẦN khi dùng >14 ngày (giảm tiểu cầu, giảm bạch cầu, thiếu máu)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu viêm dây thần kinh ngoại biên (tê, ngứa ran, yếu cơ) - đặc biệt khi dùng kéo dài",
            "Dấu hiệu viêm dây thần kinh thị giác (giảm thị lực, mù màu, mất thị lực) - đặc biệt khi dùng kéo dài, có thể không hồi phục",
            "Dấu hiệu hội chứng serotonin (kích động, nhầm lẫn, tăng thân nhiệt, tăng phản xạ, run, co giật) - khi dùng với SSRI/SNRI/MAO inhibitors",
            "INR nếu dùng với warfarin",
            "Nồng độ phenytoin nếu đang dùng"
        ],
        "precautions": [
            "NGUY CƠ GIẢM TIỂU CẦU - phổ biến, đặc biệt khi dùng >14 ngày. Theo dõi CBC hàng tuần khi dùng >14 ngày. Ngừng nếu giảm tiểu cầu nặng.",
            "NGUY CƠ HỘI CHỨNG SEROTONIN - linezolid ức chế MAO, tăng nguy cơ hội chứng serotonin khi dùng với SSRI/SNRI/MAO inhibitors. CHỐNG CHỈ ĐỊNH với MAO inhibitors. TRÁNH DÙNG với SSRI/SNRI nếu có thể. Nếu bắt buộc, ngừng SSRI/SNRI 2 tuần trước khi dùng linezolid.",
            "NGUY CƠ VIÊM DÂY THẦN KINH - đặc biệt viêm dây thần kinh thị giác (có thể không hồi phục). Theo dõi dấu hiệu giảm thị lực, mù màu. Ngừng ngay nếu có dấu hiệu viêm dây thần kinh thị giác.",
            "Thời gian điều trị: thường 10-14 ngày, tối đa 28 ngày (nguy cơ độc tính tăng khi dùng >28 ngày)",
            "Có thể chuyển từ IV sang PO (100% bioavailability) - tiết kiệm chi phí",
            "Không cần điều chỉnh liều ở suy thận (khác với nhiều kháng sinh khác)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "5 giờ",
            "onset": "Ngay lập tức sau khi truyền IV, 1-2 giờ sau khi uống",
            "duration": "q12h (dùng 2 lần/ngày)",
            "protein_binding": "31%",
            "metabolism": "Chuyển hóa qua gan (50% chuyển hóa, 50% bài tiết nguyên dạng)",
            "clearance": "Chủ yếu qua gan (50% chuyển hóa), một phần qua thận (30% bài tiết nguyên dạng), không cần điều chỉnh liều ở suy thận"
        },
        "storage": "Bảo quản viên nén ở nhiệt độ phòng (20-25°C), tránh ẩm. Bảo quản suspension ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 21 ngày sau khi pha. Bảo quản bột khô IV ở nhiệt độ phòng. Sau khi pha IV: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 48 giờ.",
        "black_box_warnings": "NGUY CƠ HỘI CHỨNG SEROTONIN - linezolid ức chế MAO, tăng nguy cơ hội chứng serotonin khi dùng với SSRI/SNRI/MAO inhibitors. CHỐNG CHỈ ĐỊNH với MAO inhibitors. TRÁNH DÙNG với SSRI/SNRI. NGUY CƠ GIẢM TIỂU CẦU - phổ biến, đặc biệt khi dùng >14 ngày. NGUY CƠ VIÊM DÂY THẦN KINH THỊ GIÁC - có thể không hồi phục, đặc biệt khi dùng kéo dài.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "SSRI (Fluoxetine, Sertraline, Citalopram, Escitalopram, Paroxetine)",
                    "mechanism": "Linezolid ức chế MAO, tăng nguy cơ hội chứng serotonin khi dùng với SSRI.",
                    "effect": "Tăng nguy cơ hội chứng serotonin (kích động, nhầm lẫn, tăng thân nhiệt, tăng phản xạ, run, co giật, có thể tử vong)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, ngừng SSRI 2 tuần trước khi dùng linezolid. Theo dõi chặt chẽ dấu hiệu hội chứng serotonin. Ngừng ngay nếu có dấu hiệu hội chứng serotonin."
                },
                {
                    "drug": "SNRI (Venlafaxine, Duloxetine)",
                    "mechanism": "Linezolid ức chế MAO, tăng nguy cơ hội chứng serotonin khi dùng với SNRI.",
                    "effect": "Tăng nguy cơ hội chứng serotonin (kích động, nhầm lẫn, tăng thân nhiệt, tăng phản xạ, run, co giật, có thể tử vong)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, ngừng SNRI 2 tuần trước khi dùng linezolid. Theo dõi chặt chẽ dấu hiệu hội chứng serotonin. Ngừng ngay nếu có dấu hiệu hội chứng serotonin."
                },
                {
                    "drug": "MAO Inhibitors (Phenelzine, Tranylcypromine, Selegiline)",
                    "mechanism": "Linezolid ức chế MAO, tăng nguy cơ hội chứng serotonin khi dùng với MAO inhibitors.",
                    "effect": "Tăng nguy cơ hội chứng serotonin nghiêm trọng, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng đồng thời."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Linezolid ức chế MAO, tramadol ức chế tái hấp thu serotonin, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu hội chứng serotonin. Ngừng ngay nếu có dấu hiệu hội chứng serotonin."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Linezolid có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm sản xuất vitamin K, tăng tác dụng của warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng linezolid. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Linezolid có thể ức chế chuyển hóa phenytoin, làm tăng nồng độ phenytoin.",
                    "effect": "Tăng nồng độ phenytoin, tăng độc tính (chóng mặt, rối loạn thăng bằng, co giật)",
                    "management": "Theo dõi nồng độ phenytoin và dấu hiệu độc tính. Giảm liều phenytoin nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng linezolid",
                "Dùng với MAO inhibitors (phenelzine, tranylcypromine, selegiline) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI, tăng nguy cơ hội chứng serotonin nghiêm trọng, có thể tử vong",
                "Dùng với pimozide, buspirone - tăng nguy cơ hội chứng serotonin"
            ],
            "tương_đối": [
                "Dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin, TRÁNH DÙNG nếu có thể",
                "Dùng với tramadol - tăng nguy cơ hội chứng serotonin",
                "Dùng >28 ngày - tăng nguy cơ độc tính (giảm tiểu cầu, viêm dây thần kinh)",
                "Bệnh nhân có tiền sử giảm tiểu cầu - tăng nguy cơ",
                "Bệnh nhân có tiền sử viêm dây thần kinh - tăng nguy cơ",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Linezolid phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm trùng nặng do VRE hoặc MRSA. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.",
            "lactation": {
                "safety": "Compatible",
                "details": "Linezolid bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ. Nồng độ trong sữa mẹ thấp và không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú. Linezolid bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Linezolid chuyển hóa qua gan nhưng không đáng kể ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng nồng độ linezolid và nguy cơ tác dụng phụ.",
            "notes": "Linezolid chuyển hóa qua gan (50% chuyển hóa, 50% bài tiết nguyên dạng). Suy gan có thể giảm chuyển hóa, tăng nồng độ linezolid. Tuy nhiên, không có hướng dẫn điều chỉnh liều cụ thể ở suy gan. Theo dõi chặt chẽ tác dụng phụ ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy",
                "Triệu chứng huyết học: Giảm tiểu cầu, giảm bạch cầu, thiếu máu",
                "Triệu chứng thần kinh: Đau đầu, chóng mặt, viêm dây thần kinh ngoại biên, viêm dây thần kinh thị giác",
                "Triệu chứng hội chứng serotonin: Kích động, nhầm lẫn, tăng thân nhiệt, tăng phản xạ, run, co giật (nếu dùng với SSRI/SNRI/MAO inhibitors)",
                "Triệu chứng nghiêm trọng: Hội chứng serotonin, viêm dây thần kinh thị giác (có thể không hồi phục), giảm tiểu cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều linezolid. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay linezolid nếu đang dùng",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Điều trị hội chứng serotonin nếu có:",
                "  - Ngừng ngay linezolid và SSRI/SNRI/MAO inhibitors",
                "  - Hạ nhiệt (paracetamol, làm mát)",
                "  - Benzodiazepine cho kích động, co giật",
                "  - Cyproheptadine (antihistamine có tác dụng chẹn serotonin) nếu có",
                "  - Hỗ trợ hô hấp nếu cần",
                "Điều trị giảm tiểu cầu nếu có:",
                "  - Theo dõi CBC",
                "  - Truyền tiểu cầu nếu giảm tiểu cầu nặng và có chảy máu",
                "Điều trị viêm dây thần kinh thị giác nếu có:",
                "  - Ngừng ngay linezolid",
                "  - Điều trị hỗ trợ",
                "  - Có thể không hồi phục",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, CBC (tiểu cầu, bạch cầu, hồng cầu), dấu hiệu hội chứng serotonin, dấu hiệu viêm dây thần kinh (đặc biệt thị giác) trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (hội chứng serotonin, viêm dây thần kinh thị giác, giảm tiểu cầu nặng)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 2 lần/ngày (q12h), thường 600mg x 2 lần/ngày. Uống đều đặn, cách đều nhau trong ngày (12 giờ). Không bỏ liều. Có thể chuyển từ IV sang PO (100% bioavailability)."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Thể tích pha: 100-300ml cho liều 600mg. Nồng độ pha: 6mg/ml (600mg/100ml) đến 2mg/ml (600mg/300ml). Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30-120 phút. Tốc độ: 100ml/30 phút = ~3.3ml/phút (nhanh) hoặc 300ml/120 phút = ~2.5ml/phút (chậm).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "Truyền IV trong 30-120 phút. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha. Có thể chuyển từ IV sang PO (100% bioavailability)."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <3 tháng tuổi (dữ liệu hạn chế).",
            "infants": "3 tháng - 1 tuổi: 10mg/kg PO/IV x 3 lần/ngày (tối đa 600mg mỗi liều). Theo dõi CBC hàng tuần nếu dùng >14 ngày.",
            "children": "1-12 tuổi: 10mg/kg PO/IV x 3 lần/ngày (tối đa 600mg mỗi liều). Theo dõi CBC hàng tuần nếu dùng >14 ngày. Theo dõi dấu hiệu viêm dây thần kinh.",
            "adolescents": "≥12 tuổi: Liều người lớn. 600mg PO/IV x 2 lần/ngày.",
            "notes": "Tính liều theo cân nặng. Dùng 3 lần/ngày ở trẻ em (khác với người lớn 2 lần/ngày). Theo dõi CBC hàng tuần nếu dùng >14 ngày. Theo dõi dấu hiệu viêm dây thần kinh (đặc biệt thị giác)."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (giảm tiểu cầu, viêm dây thần kinh). Suy gan, suy thận phổ biến hơn.",
            "dose_adjustment": "Không cần điều chỉnh liều ở suy thận. Thận trọng ở suy gan nặng. Tránh dùng >28 ngày (tăng nguy cơ độc tính).",
            "monitoring": "Theo dõi CBC hàng tuần nếu dùng >14 ngày (giảm tiểu cầu phổ biến). Theo dõi dấu hiệu viêm dây thần kinh (đặc biệt thị giác). Theo dõi dấu hiệu hội chứng serotonin nếu dùng với SSRI/SNRI."
        },
        "brand_names": {
            "vietnam": ["Zyvox", "Linezolid", "Linezolid Stada"],
            "common": ["Zyvox", "Linezolid"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "200,000 - 500,000 VND/viên hoặc lọ (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Linezolid generic thường rẻ hơn (200,000-350,000 VND/viên 600mg hoặc lọ 600mg). Zyvox (brand) thường đắt hơn (350,000-500,000 VND/viên 600mg hoặc lọ 600mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zyvox (linezolid)",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Linezolid: Drug Information",
                "Medscape - Linezolid Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Linezolid Monograph",
                "Micromedex - Linezolid Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['OXAZOLIDINONE_ANTIBIOTICS']















