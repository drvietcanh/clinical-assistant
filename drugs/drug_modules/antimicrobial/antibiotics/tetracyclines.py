"""
Tetracycline Antibiotics (Classical)
Tetracycline, Doxycycline, Minocycline
"""

TETRACYCLINE_ANTIBIOTICS = {
    "Doxycycline": {
        # === 14 STANDARD FIELDS ===
        "group": "Antibiotic - Tetracycline",
        "vietnamese_name": "Doxycycline, Vibramycin, Doxy",
        "administration": ["PO", "IV"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu",
            "Bệnh Lyme",
            "Chlamydia",
            "Bệnh rickettsia",
            "Sốt rét (dự phòng và điều trị)",
            "Mụn trứng cá",
            "Vi khuẩn không điển hình (Mycoplasma, Chlamydia, Rickettsia)"
        ],
        "contraindications": [
            "Dị ứng doxycycline hoặc tetracycline",
            "Trẻ em <8 tuổi - CHỐNG CHỈ ĐỊNH (gây răng vàng, ức chế xương)",
            "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D, gây răng vàng và ức chế xương ở thai nhi)",
            "Phụ nữ đang cho con bú - thận trọng",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "100mg PO x 2 lần/ngày",
            "adult_severe": "100mg PO x 2 lần/ngày hoặc 200mg PO x 1 lần/ngày",
            "adult_iv": "100mg IV x 2 lần/ngày hoặc 200mg IV x 1 lần/ngày",
            "adult_lyme": "100mg PO x 2 lần/ngày x 14-21 ngày",
            "adult_chlamydia": "100mg PO x 2 lần/ngày x 7 ngày",
            "adult_malaria_prophylaxis": "100mg PO x 1 lần/ngày (bắt đầu 1-2 ngày trước đi, tiếp tục trong và sau khi về)",
            "adult_malaria_treatment": "100mg PO x 2 lần/ngày x 7 ngày (kết hợp với quinine)",
            "adult_acne": "50-100mg PO x 1-2 lần/ngày",
            "pediatric_8plus": "2-4mg/kg/ngày PO chia 1-2 lần (tối đa 200mg/ngày)",
            "notes": "Uống với nhiều nước (ít nhất 200ml) để giảm kích ứng thực quản và dạ dày. Có thể uống với thức ăn để giảm kích ứng dạ dày (nhưng giảm hấp thu nhẹ). Tránh nằm ngay sau khi uống (nguy cơ viêm thực quản)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải trừ chủ yếu qua gan/mật)",
            "under_30": "Không đổi (thải trừ chủ yếu qua gan/mật)"
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến)",
            "Tiêu chảy",
            "Đau bụng",
            "Viêm thực quản (nếu nằm ngay sau khi uống)",
            "Loét thực quản (nếu nằm ngay sau khi uống)",
            "Nhạy cảm với ánh sáng (photosensitivity) - phổ biến",
            "Răng vàng (ở trẻ em <8 tuổi, phụ nữ có thai) - không hồi phục",
            "Ức chế xương (ở trẻ em <8 tuổi, phụ nữ có thai)",
            "Tăng áp lực nội sọ (pseudotumor cerebri) - hiếm",
            "Viêm gan (hiếm, đặc biệt ở liều cao)",
            "Phát ban (hiếm)"
        ],
        "interactions": [
            "Antacid (aluminum, magnesium, calcium): giảm hấp thu - cách 2 giờ",
            "Sắt: giảm hấp thu - cách 2 giờ",
            "Canxi: giảm hấp thu - cách 2 giờ",
            "Magie: giảm hấp thu - cách 2 giờ",
            "Warfarin: có thể tăng INR",
            "Thuốc tránh thai đường uống: có thể giảm hiệu quả",
            "Penicillin: giảm hiệu quả penicillin (bacteriostatic vs bactericidal)",
            "Methotrexate: có thể tăng độc tính methotrexate"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Doxycycline là tetracycline kháng sinh bacteriostatic. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 30S của ribosome, ngăn chặn sự gắn aminoacyl-tRNA với ribosome. Phổ kháng khuẩn: Gram-dương (Staphylococcus, Streptococcus, một số Enterococcus), Gram-âm (Enterobacteriaceae - một số chủng, Haemophilus influenzae, Neisseria), và vi khuẩn không điển hình (Mycoplasma pneumoniae, Chlamydia trachomatis, Chlamydia pneumoniae, Rickettsia, Borrelia burgdorferi - bệnh Lyme). Không hiệu quả với Pseudomonas aeruginosa, Acinetobacter. Đặc điểm: dùng 1-2 lần/ngày, không cần điều chỉnh liều ở suy thận (thải trừ chủ yếu qua gan/mật), nhạy cảm ánh sáng phổ biến, CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi và phụ nữ có thai (gây răng vàng và ức chế xương).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có)",
            "Dấu hiệu viêm thực quản (đau ngực, khó nuốt) - nếu nằm ngay sau khi uống",
            "Dấu hiệu nhạy cảm ánh sáng (đỏ da, phát ban) - phổ biến",
            "Dấu hiệu tăng áp lực nội sọ (đau đầu, buồn nôn, phù gai thị) - hiếm",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "PT/INR (nếu dùng với warfarin)",
            "Răng (ở trẻ em <8 tuổi) - nguy cơ răng vàng"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi - gây răng vàng và ức chế xương",
            "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai - gây răng vàng và ức chế xương ở thai nhi",
            "Uống với nhiều nước (ít nhất 200ml) để giảm kích ứng thực quản",
            "Không nằm ngay sau khi uống (ít nhất 30 phút) - nguy cơ viêm thực quản",
            "Nhạy cảm ánh sáng phổ biến - tránh ánh nắng mặt trời, dùng kem chống nắng",
            "Tránh antacid, sắt, canxi, magie trong 2 giờ (giảm hấp thu)",
            "Có thể uống với thức ăn để giảm kích ứng dạ dày (nhưng giảm hấp thu nhẹ)",
            "Không cần điều chỉnh liều ở suy thận (ưu điểm)",
            "Theo dõi INR nếu dùng với warfarin",
            "Theo dõi dấu hiệu tăng áp lực nội sọ"
        ],
        "pharmacokinetics": {
            "half_life": "18-22 giờ (dài, cho phép dùng 1-2 lần/ngày)",
            "onset": "2-4 giờ sau khi uống",
            "duration": "q12-24h (dùng 1-2 lần/ngày)",
            "protein_binding": "80-90%",
            "metabolism": "Chuyển hóa một phần ở gan",
            "clearance": "Chủ yếu qua gan/mật (60-70%), một phần qua thận (30-40%), không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/viên nang: bảo quản trong bao bì kín.",
        
        # === 8 ENHANCED FIELDS ===
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi (gây răng vàng và ức chế xương). CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (gây răng vàng và ức chế xương ở thai nhi).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacid (Aluminum, Magnesium, Calcium), Sắt, Canxi, Magie",
                    "mechanism": "Các cation (Al3+, Mg2+, Ca2+, Fe2+) tạo phức hợp không hòa tan với doxycycline, giảm hấp thu",
                    "effect": "Giảm hấp thu doxycycline, giảm nồng độ trong máu, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống doxycycline. Không uống cùng lúc."
                },
                {
                    "drug": "Penicillin",
                    "mechanism": "Tác dụng kìm khuẩn của doxycycline có thể đối kháng tác dụng diệt khuẩn của penicillin",
                    "effect": "Giảm hiệu quả điều trị của penicillin trên một số vi khuẩn nhạy cảm",
                    "management": "Tránh phối hợp khi có thể; nếu buộc dùng, theo dõi đáp ứng lâm sàng."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Doxycycline có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Tetracycline có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng doxycycline và 7 ngày sau khi ngừng."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Doxycycline có thể làm tăng nồng độ hoặc độc tính methotrexate",
                    "effect": "Tăng nguy cơ độc tính (ức chế tủy, viêm miệng, độc gan)",
                    "management": "Theo dõi độc tính methotrexate; cân nhắc giảm liều hoặc chọn kháng sinh khác."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng doxycycline hoặc tetracycline",
                "Trẻ em <8 tuổi - CHỐNG CHỈ ĐỊNH (gây răng vàng và ức chế xương)",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D, gây răng vàng và ức chế xương ở thai nhi)"
            ],
            "tương_đối": [
                "Phụ nữ đang cho con bú - thận trọng (có thể gây răng vàng ở trẻ)",
                "Suy gan nặng - thận trọng",
                "Nhạy cảm với ánh sáng - tránh ánh nắng mặt trời",
                "Tiền sử tăng áp lực nội sọ - tăng nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Doxycycline là thuốc phân loại D. CHỐNG CHỈ ĐỊNH trong thai kỳ. Tetracycline gây răng vàng và ức chế xương ở thai nhi. Không dùng trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Doxycycline bài tiết vào sữa mẹ. Tetracycline có thể gây răng vàng và ức chế xương ở trẻ bú mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu bắt buộc, theo dõi trẻ về dấu hiệu răng vàng và ức chế xương."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa một phần ở gan)",
            "severe": "Thận trọng, cân nhắc giảm liều nếu dùng kéo dài",
            "notes": "Doxycycline chuyển hóa một phần ở gan và thải trừ chủ yếu qua gan/mật. Suy gan có thể giảm chuyển hóa và tích lũy; ưu tiên liều thấp và theo dõi lâm sàng/men gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "Viêm thực quản nặng",
                "Tăng áp lực nội sọ (đau đầu, buồn nôn, phù gai thị)",
                "Viêm gan (ở liều cao)",
                "Nhạy cảm ánh sáng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng doxycycline",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "Nếu viêm thực quản:",
                "  - Điều trị hỗ trợ",
                "  - Tránh thức ăn cứng",
                "Nếu tăng áp lực nội sọ:",
                "  - Ngừng ngay doxycycline",
                "  - Acetazolamide hoặc furosemide",
                "  - Theo dõi thần kinh",
                "Nếu viêm gan:",
                "  - Theo dõi ALT, AST",
                "  - Điều trị hỗ trợ gan",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng gan, thần kinh"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST), dấu hiệu thần kinh (tăng áp lực nội sọ) trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhưng giảm hấp thu nhẹ. Uống với nhiều nước (ít nhất 200ml) để giảm kích ứng thực quản.",
                "timing": "Uống 1-2 lần/ngày (q12-24h), thường 100mg mỗi lần. Uống đều đặn, cách đều nhau trong ngày. Không nằm ngay sau khi uống (ít nhất 30 phút). Cách antacid, sắt, canxi, magie ít nhất 2 giờ."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 0.1-1mg/ml. Pha 100mg trong 100ml = 1mg/ml. Pha 200mg trong 250ml = 0.8mg/ml.",
                "infusion_rate": "Truyền IV trong 1-4 giờ. Tốc độ: 100ml/1 giờ = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Antacid, sắt, canxi, magie - giảm hấp thu",
                    "Penicillin - giảm hiệu quả penicillin"
                ],
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi và phụ nữ có thai, 2) Nhạy cảm ánh sáng phổ biến, 3) Không cần điều chỉnh liều ở suy thận, 4) Uống với nhiều nước, không nằm ngay sau khi uống."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Doxycycline (Vibramycin)",
                "IDSA Guidelines - Community-Acquired Pneumonia, Lyme Disease",
                "UpToDate - Doxycycline: Drug Information",
                "Medscape - Doxycycline Drug Reference"
            ],
            "last_updated": "2026-01-07",
            "evidence_level": "A"
        },
        
        # === ADDITIONAL FIELDS ===
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"dental": "High (children <8, pregnancy)", "hepatic": "Moderate", "neurological": "Low (pseudotumor cerebri)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Lyme Disease",
            "IDSA Guidelines - Sexually Transmitted Diseases (Chlamydia)",
            "CDC Guidelines - Malaria Prevention",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Minocycline": {
        # === 14 STANDARD FIELDS ===
        "group": "Antibiotic - Tetracycline",
        "vietnamese_name": "Minocycline, Minocin",
        "administration": ["PO", "IV"],
        "indications": [
            "Mụn trứng cá (viêm)",
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn da và mô mềm",
            "Bệnh Lyme",
            "Chlamydia",
            "Vi khuẩn không điển hình (Mycoplasma, Chlamydia)"
        ],
        "contraindications": [
            "Dị ứng minocycline hoặc tetracycline",
            "Trẻ em <8 tuổi - CHỐNG CHỈ ĐỊNH",
            "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D)",
            "Phụ nữ đang cho con bú - thận trọng"
        ],
        "dosage": {
            "adult_standard": "100mg PO x 2 lần/ngày",
            "adult_severe": "100mg PO x 2 lần/ngày hoặc 200mg PO x 1 lần/ngày",
            "adult_iv": "100mg IV x 2 lần/ngày",
            "adult_acne": "50-100mg PO x 1-2 lần/ngày",
            "adult_lyme": "100mg PO x 2 lần/ngày x 14-21 ngày",
            "pediatric_8plus": "4mg/kg/ngày PO chia 1-2 lần (tối đa 200mg/ngày)",
            "notes": "Uống với nhiều nước. Có thể uống với thức ăn để giảm kích ứng dạ dày. Có thể gây chóng mặt, mất thăng bằng (vestibular toxicity) - đặc biệt ở phụ nữ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải trừ chủ yếu qua gan/mật)",
            "under_30": "Không đổi (thải trừ chủ yếu qua gan/mật)"
        },
        "side_effects": [
            "Chóng mặt, mất thăng bằng (vestibular toxicity) - phổ biến, đặc biệt ở phụ nữ",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Đau đầu",
            "Nhạy cảm với ánh sáng (ít hơn doxycycline)",
            "Răng vàng (ở trẻ em <8 tuổi, phụ nữ có thai)",
            "Ức chế xương (ở trẻ em <8 tuổi, phụ nữ có thai)",
            "Tăng áp lực nội sọ (hiếm)",
            "Viêm gan (hiếm)",
            "Phát ban (hiếm)",
            "Lupus-like syndrome (hiếm)"
        ],
        "interactions": [
            "Antacid (aluminum, magnesium, calcium): giảm hấp thu - cách 2 giờ",
            "Sắt: giảm hấp thu - cách 2 giờ",
            "Warfarin: có thể tăng INR",
            "Thuốc tránh thai đường uống: có thể giảm hiệu quả",
            "Penicillin: giảm hiệu quả penicillin"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Minocycline là tetracycline kháng sinh bacteriostatic. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 30S của ribosome. Phổ kháng khuẩn tương tự doxycycline. Đặc điểm: có thể gây chóng mặt và mất thăng bằng (vestibular toxicity) - phổ biến, đặc biệt ở phụ nữ, nhạy cảm ánh sáng ít hơn doxycycline, hiệu quả với mụn trứng cá, CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi và phụ nữ có thai.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, triệu chứng lâm sàng)",
            "Dấu hiệu chóng mặt, mất thăng bằng (vestibular toxicity) - phổ biến",
            "Dấu hiệu nhạy cảm ánh sáng",
            "Chức năng gan (ALT, AST) - hiếm",
            "PT/INR (nếu dùng với warfarin)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi và phụ nữ có thai",
            "Chóng mặt, mất thăng bằng phổ biến - đặc biệt ở phụ nữ, có thể cần ngừng thuốc",
            "Nhạy cảm ánh sáng ít hơn doxycycline",
            "Uống với nhiều nước",
            "Tránh antacid, sắt, canxi trong 2 giờ",
            "Không cần điều chỉnh liều ở suy thận",
            "Theo dõi INR nếu dùng với warfarin"
        ],
        "pharmacokinetics": {
            "half_life": "11-23 giờ",
            "onset": "2-4 giờ sau khi uống",
            "duration": "q12-24h",
            "protein_binding": "70-75%",
            "metabolism": "Chuyển hóa một phần ở gan",
            "clearance": "Chủ yếu qua gan/mật, một phần qua thận, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        
        # === 8 ENHANCED FIELDS ===
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi và phụ nữ có thai (gây răng vàng và ức chế xương).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacid (Aluminum, Magnesium, Calcium), Sắt, Canxi",
                    "mechanism": "Các cation tạo phức hợp không hòa tan với minocycline, giảm hấp thu",
                    "effect": "Giảm hấp thu minocycline",
                    "management": "Cách ít nhất 2 giờ trước hoặc sau khi uống minocycline."
                },
                {
                    "drug": "Penicillin",
                    "mechanism": "Tác dụng kìm khuẩn của minocycline có thể đối kháng tác dụng diệt khuẩn của penicillin",
                    "effect": "Giảm hiệu quả penicillin",
                    "management": "Tránh phối hợp nếu có thể; theo dõi đáp ứng lâm sàng."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Minocycline có thể ảnh hưởng đến hệ vi khuẩn đường ruột",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR thường xuyên."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Có thể tăng nồng độ/độc tính methotrexate",
                    "effect": "Tăng nguy cơ ức chế tủy/độc gan",
                    "management": "Theo dõi độc tính; cân nhắc kháng sinh khác."
                },
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Giảm tái hấp thu estrogen do thay đổi hệ vi khuẩn ruột",
                    "effect": "Giảm hiệu quả tránh thai (hiếm)",
                    "management": "Khuyên dùng biện pháp tránh thai bổ sung trong và 7 ngày sau điều trị."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng minocycline hoặc tetracycline",
                "Trẻ em <8 tuổi - CHỐNG CHỈ ĐỊNH",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D)"
            ],
            "tương_đối": [
                "Phụ nữ đang cho con bú - thận trọng",
                "Tiền sử chóng mặt, mất thăng bằng - tăng nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Minocycline là thuốc phân loại D. CHỐNG CHỈ ĐỊNH trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Minocycline bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng; cân nhắc giảm liều nếu dùng kéo dài",
            "severe": "Thận trọng cao; tránh liều cao/kéo dài",
            "notes": "Minocycline chuyển hóa một phần ở gan. Suy gan có thể tích lũy; dùng liều thấp và theo dõi men gan nếu kéo dài."
        },
        "overdose_management": {
            "symptoms": [
                "Chóng mặt, mất thăng bằng nặng",
                "Buồn nôn, nôn nặng",
                "Tăng áp lực nội sọ",
                "Viêm gan"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng minocycline",
                "Điều trị triệu chứng",
                "Nếu tăng áp lực nội sọ: acetazolamide hoặc furosemide",
                "Theo dõi chức năng gan, thần kinh"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan, thần kinh trong 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với nhiều nước.",
                "timing": "Uống 1-2 lần/ngày, thường 100mg mỗi lần. Cách antacid, sắt, canxi ít nhất 2 giờ."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 0.1-1mg/ml.",
                "infusion_rate": "Truyền IV trong 1-4 giờ",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Antacid, sắt, canxi - giảm hấp thu",
                    "Penicillin - giảm hiệu quả"
                ],
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi và phụ nữ có thai, 2) Chóng mặt, mất thăng bằng phổ biến, 3) Không cần điều chỉnh liều ở suy thận."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Minocycline (Minocin)",
                "UpToDate - Minocycline: Drug Information",
                "Medscape - Minocycline Drug Reference"
            ],
            "last_updated": "2026-01-07",
            "evidence_level": "A"
        },
        
        # === ADDITIONAL FIELDS ===
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"dental": "High (children <8, pregnancy)", "neurological": "Moderate (vestibular toxicity)", "hepatic": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Acne Treatment",
            "IDSA Guidelines - Lyme Disease",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Tetracycline": {
        # === 14 STANDARD FIELDS ===
        "group": "Antibiotic - Tetracycline",
        "vietnamese_name": "Tetracycline, Tetracyn",
        "administration": ["PO"],
        "indications": [
            "Mụn trứng cá",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn da và mô mềm",
            "Chlamydia",
            "Bệnh rickettsia",
            "Vi khuẩn không điển hình (Mycoplasma, Chlamydia, Rickettsia)"
        ],
        "contraindications": [
            "Dị ứng tetracycline",
            "Trẻ em <8 tuổi - CHỐNG CHỈ ĐỊNH",
            "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D)",
            "Phụ nữ đang cho con bú - thận trọng",
            "Suy thận nặng - CHỐNG CHỈ ĐỊNH (tích lũy, tăng độc tính)"
        ],
        "dosage": {
            "adult_standard": "250-500mg PO x 4 lần/ngày",
            "adult_severe": "500mg PO x 4 lần/ngày",
            "adult_acne": "250-500mg PO x 2-4 lần/ngày",
            "adult_chlamydia": "500mg PO x 4 lần/ngày x 7 ngày",
            "pediatric_8plus": "25-50mg/kg/ngày PO chia 4 lần (tối đa 2g/ngày)",
            "notes": "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu. Uống với nhiều nước. Dùng 4 lần/ngày. CHỐNG CHỈ ĐỊNH ở suy thận nặng (tích lũy, tăng độc tính)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Tránh dùng hoặc giảm liều đáng kể",
            "under_30": "CHỐNG CHỈ ĐỊNH (tích lũy, tăng độc tính)"
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến)",
            "Tiêu chảy",
            "Đau bụng",
            "Nhạy cảm với ánh sáng (photosensitivity) - phổ biến",
            "Răng vàng (ở trẻ em <8 tuổi, phụ nữ có thai) - không hồi phục",
            "Ức chế xương (ở trẻ em <8 tuổi, phụ nữ có thai)",
            "Tăng áp lực nội sọ (hiếm)",
            "Viêm gan (hiếm, đặc biệt ở suy thận)",
            "Độc thận (ở suy thận) - tích lũy",
            "Phát ban (hiếm)"
        ],
        "interactions": [
            "Antacid (aluminum, magnesium, calcium): giảm hấp thu - cách 2 giờ",
            "Sắt: giảm hấp thu - cách 2 giờ",
            "Warfarin: có thể tăng INR",
            "Thuốc tránh thai đường uống: có thể giảm hiệu quả",
            "Penicillin: giảm hiệu quả penicillin",
            "Methotrexate: có thể tăng độc tính methotrexate"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Tetracycline là tetracycline kháng sinh bacteriostatic đầu tiên. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 30S của ribosome. Phổ kháng khuẩn tương tự doxycycline. Đặc điểm: tetracycline cổ điển, dùng 4 lần/ngày, CHỐNG CHỈ ĐỊNH ở suy thận nặng (tích lũy, tăng độc tính), nhạy cảm ánh sáng phổ biến, ít được dùng hơn doxycycline do tác dụng phụ nhiều hơn và cần điều chỉnh liều ở suy thận.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, triệu chứng lâm sàng)",
            "Chức năng thận (creatinine, eGFR) - QUAN TRỌNG, CHỐNG CHỈ ĐỊNH ở suy thận nặng",
            "Dấu hiệu nhạy cảm ánh sáng",
            "Chức năng gan (ALT, AST) - đặc biệt ở suy thận",
            "PT/INR (nếu dùng với warfarin)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi và phụ nữ có thai",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30) - tích lũy, tăng độc tính",
            "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu",
            "Uống với nhiều nước",
            "Nhạy cảm ánh sáng phổ biến - tránh ánh nắng mặt trời",
            "Tránh antacid, sắt, canxi trong 2 giờ",
            "Theo dõi chức năng thận - quan trọng",
            "Theo dõi INR nếu dùng với warfarin"
        ],
        "pharmacokinetics": {
            "half_life": "6-12 giờ",
            "onset": "2-4 giờ sau khi uống",
            "duration": "q6h (dùng 4 lần/ngày)",
            "protein_binding": "20-65%",
            "metabolism": "Chuyển hóa một phần ở gan",
            "clearance": "Gan (60%) và thận (40%), tích lũy ở suy thận - CHỐNG CHỈ ĐỊNH ở suy thận nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        
        # === 8 ENHANCED FIELDS ===
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở trẻ em <8 tuổi và phụ nữ có thai (gây răng vàng và ức chế xương). CHỐNG CHỈ ĐỊNH ở suy thận nặng (tích lũy, tăng độc tính).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacid (Aluminum, Magnesium, Calcium), Sắt, Canxi",
                    "mechanism": "Các cation tạo phức hợp không hòa tan với tetracycline, giảm hấp thu",
                    "effect": "Giảm hấp thu tetracycline",
                    "management": "Cách ít nhất 2 giờ trước hoặc sau khi uống tetracycline."
                },
                {
                    "drug": "Penicillin",
                    "mechanism": "Tác dụng kìm khuẩn của tetracycline có thể đối kháng tác dụng diệt khuẩn của penicillin",
                    "effect": "Giảm hiệu quả penicillin",
                    "management": "Tránh phối hợp nếu có thể; theo dõi đáp ứng lâm sàng."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tetracycline có thể ảnh hưởng đến hệ vi khuẩn đường ruột",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR thường xuyên."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Có thể tăng nồng độ/độc tính methotrexate",
                    "effect": "Tăng nguy cơ ức chế tủy/độc gan",
                    "management": "Theo dõi độc tính; cân nhắc kháng sinh khác."
                },
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Giảm tái hấp thu estrogen do thay đổi hệ vi khuẩn ruột",
                    "effect": "Giảm hiệu quả tránh thai (hiếm)",
                    "management": "Khuyên dùng biện pháp tránh thai bổ sung trong và 7 ngày sau điều trị."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng tetracycline",
                "Trẻ em <8 tuổi - CHỐNG CHỈ ĐỊNH",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D)",
                "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH (tích lũy, tăng độc tính)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-60) - tránh dùng hoặc giảm liều đáng kể",
                "Phụ nữ đang cho con bú - thận trọng",
                "Nhạy cảm với ánh sáng - tránh ánh nắng mặt trời"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Tetracycline là thuốc phân loại D. CHỐNG CHỈ ĐỊNH trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Tetracycline bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng; cân nhắc giảm liều nếu dùng kéo dài",
            "severe": "Thận trọng cao; tránh liều cao/kéo dài",
            "notes": "Tetracycline chuyển hóa một phần ở gan. Suy gan có thể tích lũy; ưu tiên liều thấp và theo dõi men gan nếu phải dùng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "Tăng áp lực nội sọ",
                "Viêm gan",
                "Độc thận (ở suy thận)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng tetracycline",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ",
                "Điều trị triệu chứng",
                "Nếu tăng áp lực nội sọ: acetazolamide hoặc furosemide",
                "Nếu độc thận: bù dịch, lọc máu nếu cần",
                "Theo dõi chức năng gan, thận"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan, thận trong 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu. Uống với nhiều nước (ít nhất 200ml).",
                "timing": "Uống 4 lần/ngày (q6h), thường 250-500mg mỗi lần. Uống đều đặn, cách đều nhau trong ngày. Cách antacid, sắt, canxi ít nhất 2 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tetracycline",
                "UpToDate - Tetracycline: Drug Information",
                "Medscape - Tetracycline Drug Reference"
            ],
            "last_updated": "2026-01-07",
            "evidence_level": "A"
        },
        
        # === ADDITIONAL FIELDS ===
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"dental": "High (children <8, pregnancy)", "hepatic": "Moderate", "renal": "High (accumulation in renal impairment)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Acne Treatment",
            "IDSA Guidelines - Chlamydia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
}

__all__ = ['TETRACYCLINE_ANTIBIOTICS']
