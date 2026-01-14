"""
Ophthalmology Drugs - Anti Inflammatory
"""
from typing import Dict, Any


ANTI_INFLAMMATORY_DRUGS: Dict[str, Dict[str, Any]] = {
        "Dexamethasone eye drops": {
            "group": "Ophthalmology - Corticosteroid (Anti-inflammatory)",
            "vietnamese_name": "Dexamethasone nhỏ mắt, Maxidex",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc dị ứng (allergic conjunctivitis)",
                "Viêm màng bồ đào (uveitis)",
                "Viêm giác mạc (keratitis)",
                "Viêm sau phẫu thuật mắt (postoperative inflammation)",
                "Viêm màng bồ đào do miễn dịch (immune-mediated uveitis)"
            ],
            "contraindications": [
                "Dị ứng dexamethasone hoặc corticosteroid",
                "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH",
                "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH",
                "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH",
                "Tăng nhãn áp (glaucoma) - thận trọng",
                "Đục thủy tinh thể (cataract) - thận trọng"
            ],
            "dosage": {
                "adult_conjunctivitis": "1-2 giọt vào mắt bị ảnh hưởng 4-6 lần/ngày, giảm dần khi cải thiện",
                "adult_uveitis": "1-2 giọt vào mắt bị ảnh hưởng mỗi giờ trong 24-48 giờ đầu, sau đó giảm dần",
                "adult_postoperative": "1-2 giọt vào mắt bị ảnh hưởng 4-6 lần/ngày trong 1-2 tuần",
                "notes": "Dexamethasone là corticosteroid mạnh, chống viêm hiệu quả. Dùng thường xuyên trong giai đoạn đầu, sau đó giảm dần. Điều trị thường 1-4 tuần. Nguy cơ tăng nhãn áp và đục thủy tinh thể nếu dùng kéo dài."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Tăng nhãn áp (glaucoma) - phổ biến nếu dùng kéo dài",
                "Đục thủy tinh thể (cataract) - phổ biến nếu dùng kéo dài",
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ",
                "Nhiễm trùng mắt (nếu dùng kéo dài, ức chế miễn dịch) - nguy hiểm",
                "Chậm lành vết thương",
                "Phản ứng dị ứng - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Dexamethasone là corticosteroid tổng hợp mạnh. Gắn với thụ thể glucocorticoid trong tế bào, ức chế quá trình viêm bằng cách: (1) Ức chế giải phóng các chất trung gian viêm (prostaglandin, leukotriene, cytokine), (2) Ức chế di chuyển và hoạt động của bạch cầu, (3) Ức chế sản xuất kháng thể, (4) Ổn định màng tế bào. Dẫn đến: giảm viêm, giảm đỏ, giảm sưng, giảm đau. ĐẶC ĐIỂM: (1) Corticosteroid mạnh, chống viêm hiệu quả, (2) Dùng thường xuyên trong giai đoạn đầu, sau đó giảm dần, (3) Nguy cơ tăng nhãn áp và đục thủy tinh thể nếu dùng kéo dài, (4) CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm, (5) Ức chế miễn dịch, tăng nguy cơ nhiễm trùng nếu dùng kéo dài.",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG: theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu đục thủy tinh thể (giảm thị lực, nhìn mờ) - nếu dùng kéo dài",
                "Dấu hiệu nhiễm trùng mắt (đỏ, chảy mủ, đau) - nguy hiểm nếu dùng kéo dài",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Dấu hiệu viêm (đỏ, sưng) - cải thiện sau vài ngày"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus (herpes simplex, varicella) - có thể làm nặng",
                "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do nấm - có thể làm nặng",
                "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do vi khuẩn chưa điều trị - có thể làm nặng",
                "NGUY CƠ TĂNG NHÃN ÁP - theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
                "NGUY CƠ ĐỤC THỦY TINH THỂ - theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
                "Nguy cơ nhiễm trùng mắt nếu dùng kéo dài (ức chế miễn dịch)",
                "Chậm lành vết thương",
                "Dùng đủ liều và đủ thời gian, nhưng tránh dùng kéo dài không cần thiết",
                "Giảm dần liều khi cải thiện để tránh tái phát",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "3-4 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
                "onset": "Vài giờ",
                "duration": "4-6 giờ (dùng 4-6 lần/ngày)",
                "protein_binding": "77%",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "NGUY CƠ TĂNG NHÃN ÁP VÀ ĐỤC THỦY TINH THỂ nếu dùng kéo dài. CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm. Ức chế miễn dịch, tăng nguy cơ nhiễm trùng nếu dùng kéo dài. Phải theo dõi nhãn áp định kỳ.",
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng dexamethasone hoặc corticosteroid",
                    "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                    "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                    "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH (có thể làm nặng)"
                ],
                "tương_đối": [
                    "Tăng nhãn áp (glaucoma) - thận trọng, theo dõi nhãn áp định kỳ",
                    "Đục thủy tinh thể (cataract) - thận trọng, có thể làm nặng",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng dexamethasone hoặc corticosteroid",
                    "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                    "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                    "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH (có thể làm nặng)"
                ],
                "tương_đối": [
                    "Tăng nhãn áp (glaucoma) - thận trọng, theo dõi nhãn áp định kỳ",
                    "Đục thủy tinh thể (cataract) - thận trọng, có thể làm nặng",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Dexamethasone là thuốc phân loại C. Dexamethasone có thể hấp thu toàn thân và qua nhau thai. Corticosteroid có thể gây dị tật bẩm sinh ở động vật. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Dexamethasone có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Dexamethasone dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Tăng nhãn áp nặng (nếu dùng kéo dài)",
                    "Đục thủy tinh thể (nếu dùng kéo dài)",
                    "Nhiễm trùng mắt (nếu dùng kéo dài)"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ. Giảm liều hoặc ngừng nếu có tác dụng phụ nặng.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Nếu tăng nhãn áp nặng:",
                    "  - Ngừng dexamethasone",
                    "  - Điều trị tăng nhãn áp (thuốc giảm nhãn áp)",
                    "Nếu nhiễm trùng mắt:",
                    "  - Ngừng dexamethasone",
                    "  - Điều trị nhiễm trùng (kháng sinh, kháng virus, kháng nấm)",
                    "Theo dõi: Thị lực, nhãn áp, dấu hiệu viêm, dấu hiệu nhiễm trùng"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu viêm, dấu hiệu nhiễm trùng cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng nhãn áp, đục thủy tinh thể, nhiễm trùng)."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là rửa mắt và điều trị hỗ trợ. Nếu tăng nhãn áp nặng: ngừng thuốc và điều trị tăng nhãn áp. Nếu nhiễm trùng mắt: ngừng thuốc và điều trị nhiễm trùng."
            },
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.1% (1 mg/ml).",
                    "application": "1-2 giọt vào mắt bị ảnh hưởng theo lịch trình (xem dosage). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "Tùy theo chỉ định: 4-6 lần/ngày (conjunctivitis, postoperative) hoặc mỗi giờ (uveitis).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm, 2) NGUY CƠ TĂNG NHÃN ÁP VÀ ĐỤC THỦY TINH THỂ nếu dùng kéo dài, 3) Theo dõi nhãn áp định kỳ, 4) Giảm dần liều khi cải thiện, 5) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Dexamethasone (Maxidex)",
                    "UpToDate - Dexamethasone: Drug Information",
                    "Medscape - Dexamethasone Drug Reference",
                    "AAO Guidelines - Uveitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Increased IOP (glaucoma) - CRITICAL", "Cataract formation (with prolonged use) - CRITICAL", "Corneal thinning/perforation (with prolonged use) - CRITICAL", "Infection (herpes, fungal) - increased risk"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["IOP (target <21 mmHg) - CRITICAL", "Vision and periodic eye exams", "Signs of eye irritation (redness, burning)", "Signs of increased IOP (headache, eye pain, blurred vision) - CRITICAL", "Signs of infection (pus, increased redness/swelling, herpes) - CRITICAL"]
            },
            "guideline_tags": [
                "AAO Guidelines - Uveitis",
                "AAO Guidelines - Postoperative Inflammation",
                "FDA Drug Information - Dexamethasone Eye Drops",
                "FDA Black Box Warning - Dexamethasone and Increased IOP",
                "UpToDate - Uveitis Treatment"
            ]
        },

        "Diclofenac eye drops": {
            "group": "Ophthalmology - NSAID (Anti-inflammatory)",
            "vietnamese_name": "Diclofenac, Voltaren Ophtha",
            "administration": ["Ophthalmic"],
            "indications": [
                "Điều trị viêm sau phẫu thuật mắt (postoperative inflammation)",
                "Giảm đau sau phẫu thuật mắt (postoperative pain)",
                "Điều trị viêm kết mạc dị ứng (allergic conjunctivitis)",
                "Giảm đau và viêm trong viêm màng bồ đào (uveitis)",
                "Dự phòng và điều trị phù hoàng điểm dạng nang (cystoid macular edema - CME) sau phẫu thuật mắt"
            ],
            "contraindications": [
                "Dị ứng diclofenac hoặc NSAID",
                "Loét dạ dày tá tràng hoạt động",
                "Xuất huyết tiêu hóa gần đây",
                "Suy thận nặng",
                "Suy gan nặng",
                "Rối loạn đông máu nặng",
                "Trẻ em <3 tuổi (thận trọng)"
            ],
            "dosage": {
                "adult_postop_inflammation": "1 giọt vào mắt phẫu thuật x 4 lần/ngày bắt đầu 24 giờ sau phẫu thuật, trong 2 tuần",
                "adult_allergic_conjunctivitis": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày",
                "adult_cme_prophylaxis": "1 giọt vào mắt phẫu thuật x 4 lần/ngày bắt đầu 24 giờ sau phẫu thuật, trong 4 tuần",
                "notes": "Diclofenac là NSAID tại chỗ, ức chế cyclooxygenase (COX), giảm viêm và đau. Tương tự ketorolac nhưng có thể ít kích ứng mắt hơn. Dùng 4 lần/ngày. Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (loét dạ dày, suy thận)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, theo dõi chức năng thận",
                "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
            },
            "side_effects": [
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa, châm chích) - phổ biến",
                "Nhìn mờ tạm thời",
                "Khô mắt",
                "Đau mắt",
                "Hấp thu toàn thân: loét dạ dày tá tràng - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: suy thận cấp - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: xuất huyết tiêu hóa - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: rối loạn đông máu - hiếm",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm"
            ],
            "interactions": [
                "NSAID đường uống (aspirin, ibuprofen, naproxen): tăng nguy cơ loét dạ dày, suy thận",
                "Warfarin, thuốc chống đông: tăng nguy cơ xuất huyết",
                "ACE inhibitors, ARBs: tăng nguy cơ suy thận",
                "Corticosteroid: tăng nguy cơ loét dạ dày",
                "Lithium: tăng nồng độ lithium"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Diclofenac là NSAID (nonsteroidal anti-inflammatory drug). Ức chế enzyme cyclooxygenase (COX-1 và COX-2), ngăn chặn sự tổng hợp prostaglandin từ arachidonic acid. Prostaglandin là chất trung gian gây viêm, đau, và sốt. Giảm prostaglandin dẫn đến: (1) Giảm viêm (giảm đỏ, sưng), (2) Giảm đau, (3) Giảm phù hoàng điểm dạng nang (CME) sau phẫu thuật mắt. Diclofenac tương tự ketorolac nhưng có thể ít kích ứng mắt hơn. ĐẶC ĐIỂM: (1) NSAID tại chỗ, ức chế COX, (2) Dùng 4 lần/ngày, (3) Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (loét dạ dày, suy thận), (4) CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, (5) Kích ứng mắt phổ biến nhưng có thể ít hơn ketorolac, (6) Hiệu quả cho viêm và đau sau phẫu thuật mắt, CME.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, đau) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa, châm chích tăng)",
                "Dấu hiệu hấp thu toàn thân: đau bụng, xuất huyết tiêu hóa (phân đen, nôn ra máu) - NGUY HIỂM",
                "Dấu hiệu hấp thu toàn thân: suy thận (giảm lượng nước tiểu, phù) - NGUY HIỂM",
                "Chức năng thận (creatinine, eGFR) - nếu dùng kéo dài hoặc có nguy cơ",
                "Thị lực (nhìn mờ tạm thời)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, xuất huyết tiêu hóa gần đây",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Hấp thu toàn thân - có thể gây loét dạ dày, suy thận, xuất huyết tiêu hóa",
                "TRÁNH DÙNG với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                "Thận trọng ở bệnh nhân dùng warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                "Thận trọng ở bệnh nhân dùng ACE inhibitors, ARBs - tăng nguy cơ suy thận",
                "Thận trọng ở bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Nhìn mờ tạm thời - bệnh nhân không nên lái xe ngay sau khi nhỏ"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Vài giờ",
                "duration": "4-6 giờ (dùng 4 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân, CYP2C9)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "Nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa, suy thận cấp nếu hấp thu toàn thân. CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, xuất huyết tiêu hóa gần đây. TRÁNH DÙNG với NSAID đường uống.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "NSAID đường uống (Aspirin, Ibuprofen, Naproxen, Ketorolac)",
                        "mechanism": "Cả hai đều ức chế COX, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa, suy thận cấp",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi dấu hiệu loét dạ dày, suy thận sát."
                    },
                    {
                        "drug": "Warfarin, Thuốc chống đông (Heparin, Enoxaparin, Dabigatran, Rivaroxaban)",
                        "mechanism": "NSAID ức chế COX-1, giảm sản xuất thromboxane, tăng nguy cơ xuất huyết",
                        "effect": "Tăng nguy cơ xuất huyết (đặc biệt xuất huyết tiêu hóa)",
                        "management": "Thận trọng. Theo dõi INR, dấu hiệu xuất huyết sát."
                    }
                ],
                "moderate": [
                    {
                        "drug": "ACE Inhibitors, ARBs (Lisinopril, Losartan, Valsartan)",
                        "mechanism": "NSAID giảm sản xuất prostaglandin, giảm lưu lượng máu thận, tác dụng cộng dồn với ACE inhibitors/ARBs",
                        "effect": "Tăng nguy cơ suy thận cấp",
                        "management": "Thận trọng. Theo dõi chức năng thận sát."
                    },
                    {
                        "drug": "Corticosteroid (Prednisone, Dexamethasone)",
                        "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày",
                        "effect": "Tăng nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa",
                        "management": "Thận trọng. Có thể cần dùng PPI (proton pump inhibitor) để bảo vệ dạ dày."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng diclofenac hoặc NSAID",
                    "Loét dạ dày tá tràng hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Xuất huyết tiêu hóa gần đây - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Rối loạn đông máu nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, theo dõi chức năng thận",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Dùng với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                    "Dùng với warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                    "Dùng với ACE inhibitors, ARBs - tăng nguy cơ suy thận",
                    "Trẻ em <3 tuổi - thận trọng"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng diclofenac hoặc NSAID",
                    "Loét dạ dày tá tràng hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Xuất huyết tiêu hóa gần đây - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Rối loạn đông máu nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, theo dõi chức năng thận",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Dùng với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                    "Dùng với warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                    "Dùng với ACE inhibitors, ARBs - tăng nguy cơ suy thận",
                    "Trẻ em <3 tuổi - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Diclofenac là thuốc phân loại C. NSAID có thể qua nhau thai và gây tác dụng phụ ở thai nhi (đóng sớm ống động mạch, suy thận). Tránh dùng trong tam cá nguyệt thứ ba. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong tam cá nguyệt thứ nhất và thứ hai.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Diclofenac có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ diclofenac và nguy cơ tác dụng phụ.",
                "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
                "notes": "Diclofenac chuyển hóa qua gan (CYP2C9). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: đau bụng nặng, xuất huyết tiêu hóa (phân đen, nôn ra máu) - NGUY HIỂM",
                    "Hấp thu toàn thân: suy thận cấp (giảm lượng nước tiểu, phù) - NGUY HIỂM",
                    "Hấp thu toàn thân: rối loạn đông máu (xuất huyết) - NGUY HIỂM"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Ngừng ngay diclofenac",
                    "  - Nếu xuất huyết tiêu hóa:",
                    "    - Hỗ trợ huyết động (truyền dịch, máu nếu cần)",
                    "    - Nội soi dạ dày nếu cần",
                    "    - PPI (omeprazole, pantoprazole) để giảm acid dạ dày",
                    "  - Nếu suy thận cấp:",
                    "    - Hỗ trợ huyết động",
                    "    - Lọc máu nếu cần",
                    "  - Theo dõi dấu hiệu sinh tồn, chức năng thận, đông máu",
                    "Theo dõi: Dấu hiệu sinh tồn, lượng nước tiểu, chức năng thận, dấu hiệu xuất huyết"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng nước tiểu, chức năng thận, dấu hiệu xuất huyết cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (xuất huyết tiêu hóa, suy thận cấp)."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là rửa mắt và điều trị hỗ trợ. Nếu hấp thu toàn thân nặng: ngừng thuốc, điều trị xuất huyết tiêu hóa (PPI, hỗ trợ huyết động), suy thận cấp (hỗ trợ huyết động, lọc máu nếu cần)."
            },
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.1%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "4 lần/ngày. Bắt đầu 24 giờ sau phẫu thuật mắt cho điều trị viêm sau phẫu thuật.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, 2) TRÁNH DÙNG với NSAID đường uống, 3) Kích ứng mắt phổ biến, 4) Hấp thu toàn thân có thể gây loét dạ dày, suy thận, 5) Nhìn mờ tạm thời - không lái xe ngay."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Diclofenac (Voltaren Ophtha)",
                    "UpToDate - Diclofenac: Drug Information",
                    "Medscape - Diclofenac Drug Reference",
                    "AAO Guidelines - Postoperative Inflammation, CME"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["GI toxicity (rare, if systemic absorption occurs)", "Renal toxicity (rare, if systemic absorption occurs)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in inflammation, pain)", "Signs of eye irritation (redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Signs of systemic side effects (rare): GI pain"]
            },
            "guideline_tags": [
                "AAO Guidelines - Postoperative Inflammation",
                "AAO Guidelines - Cystoid Macular Edema",
                "FDA Drug Information - Diclofenac Eye Drops",
                "UpToDate - Postoperative Eye Inflammation"
            ]
        },

        "Ketorolac eye drops": {
            "group": "Ophthalmology - NSAID (Anti-inflammatory)",
            "vietnamese_name": "Ketorolac, Acular",
            "administration": ["Ophthalmic"],
            "indications": [
                "Điều trị viêm sau phẫu thuật mắt (postoperative inflammation)",
                "Giảm đau sau phẫu thuật mắt (postoperative pain)",
                "Điều trị viêm kết mạc dị ứng (allergic conjunctivitis)",
                "Giảm đau và viêm trong viêm màng bồ đào (uveitis)",
                "Dự phòng và điều trị phù hoàng điểm dạng nang (cystoid macular edema - CME) sau phẫu thuật mắt"
            ],
            "contraindications": [
                "Dị ứng ketorolac hoặc NSAID",
                "Loét dạ dày tá tràng hoạt động",
                "Xuất huyết tiêu hóa gần đây",
                "Suy thận nặng",
                "Suy gan nặng",
                "Rối loạn đông máu nặng",
                "Trẻ em <3 tuổi (thận trọng)"
            ],
            "dosage": {
                "adult_postop_inflammation": "1 giọt vào mắt phẫu thuật x 4 lần/ngày bắt đầu 24 giờ sau phẫu thuật, trong 2 tuần",
                "adult_allergic_conjunctivitis": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày",
                "adult_cme_prophylaxis": "1 giọt vào mắt phẫu thuật x 4 lần/ngày bắt đầu 24 giờ sau phẫu thuật, trong 4 tuần",
                "notes": "Ketorolac là NSAID tại chỗ, ức chế cyclooxygenase (COX), giảm viêm và đau. Dùng 4 lần/ngày. Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (loét dạ dày, suy thận)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, theo dõi chức năng thận",
                "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
            },
            "side_effects": [
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa, châm chích) - phổ biến",
                "Nhìn mờ tạm thời",
                "Khô mắt",
                "Đau mắt",
                "Hấp thu toàn thân: loét dạ dày tá tràng - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: suy thận cấp - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: xuất huyết tiêu hóa - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: rối loạn đông máu - hiếm",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm"
            ],
            "interactions": [
                "NSAID đường uống (aspirin, ibuprofen, naproxen): tăng nguy cơ loét dạ dày, suy thận",
                "Warfarin, thuốc chống đông: tăng nguy cơ xuất huyết",
                "ACE inhibitors, ARBs: tăng nguy cơ suy thận",
                "Corticosteroid: tăng nguy cơ loét dạ dày",
                "Lithium: tăng nồng độ lithium"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Ketorolac là NSAID (nonsteroidal anti-inflammatory drug). Ức chế enzyme cyclooxygenase (COX-1 và COX-2), ngăn chặn sự tổng hợp prostaglandin từ arachidonic acid. Prostaglandin là chất trung gian gây viêm, đau, và sốt. Giảm prostaglandin dẫn đến: (1) Giảm viêm (giảm đỏ, sưng), (2) Giảm đau, (3) Giảm phù hoàng điểm dạng nang (CME) sau phẫu thuật mắt. ĐẶC ĐIỂM: (1) NSAID tại chỗ, ức chế COX, (2) Dùng 4 lần/ngày, (3) Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (loét dạ dày, suy thận), (4) CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, (5) Kích ứng mắt phổ biến, (6) Hiệu quả cho viêm và đau sau phẫu thuật mắt, CME.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, đau) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa, châm chích tăng)",
                "Dấu hiệu hấp thu toàn thân: đau bụng, xuất huyết tiêu hóa (phân đen, nôn ra máu) - NGUY HIỂM",
                "Dấu hiệu hấp thu toàn thân: suy thận (giảm lượng nước tiểu, phù) - NGUY HIỂM",
                "Chức năng thận (creatinine, eGFR) - nếu dùng kéo dài hoặc có nguy cơ",
                "Thị lực (nhìn mờ tạm thời)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, xuất huyết tiêu hóa gần đây",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Hấp thu toàn thân - có thể gây loét dạ dày, suy thận, xuất huyết tiêu hóa",
                "TRÁNH DÙNG với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                "Thận trọng ở bệnh nhân dùng warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                "Thận trọng ở bệnh nhân dùng ACE inhibitors, ARBs - tăng nguy cơ suy thận",
                "Thận trọng ở bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Nhìn mờ tạm thời - bệnh nhân không nên lái xe ngay sau khi nhỏ"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Vài giờ",
                "duration": "4-6 giờ (dùng 4 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân, CYP2C9, CYP3A4)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "Nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa, suy thận cấp nếu hấp thu toàn thân. CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, xuất huyết tiêu hóa gần đây. TRÁNH DÙNG với NSAID đường uống.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "NSAID đường uống (Aspirin, Ibuprofen, Naproxen, Diclofenac)",
                        "mechanism": "Cả hai đều ức chế COX, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa, suy thận cấp",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi dấu hiệu loét dạ dày, suy thận sát."
                    },
                    {
                        "drug": "Warfarin, Thuốc chống đông (Heparin, Enoxaparin, Dabigatran, Rivaroxaban)",
                        "mechanism": "NSAID ức chế COX-1, giảm sản xuất thromboxane, tăng nguy cơ xuất huyết",
                        "effect": "Tăng nguy cơ xuất huyết (đặc biệt xuất huyết tiêu hóa)",
                        "management": "Thận trọng. Theo dõi INR, dấu hiệu xuất huyết sát."
                    }
                ],
                "moderate": [
                    {
                        "drug": "ACE Inhibitors, ARBs (Lisinopril, Losartan, Valsartan)",
                        "mechanism": "NSAID giảm sản xuất prostaglandin, giảm lưu lượng máu thận, tác dụng cộng dồn với ACE inhibitors/ARBs",
                        "effect": "Tăng nguy cơ suy thận cấp",
                        "management": "Thận trọng. Theo dõi chức năng thận sát."
                    },
                    {
                        "drug": "Corticosteroid (Prednisone, Dexamethasone)",
                        "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày",
                        "effect": "Tăng nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa",
                        "management": "Thận trọng. Có thể cần dùng PPI (proton pump inhibitor) để bảo vệ dạ dày."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng ketorolac hoặc NSAID",
                    "Loét dạ dày tá tràng hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Xuất huyết tiêu hóa gần đây - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Rối loạn đông máu nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, theo dõi chức năng thận",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Dùng với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                    "Dùng với warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                    "Dùng với ACE inhibitors, ARBs - tăng nguy cơ suy thận",
                    "Trẻ em <3 tuổi - thận trọng"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng ketorolac hoặc NSAID",
                    "Loét dạ dày tá tràng hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Xuất huyết tiêu hóa gần đây - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Rối loạn đông máu nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, theo dõi chức năng thận",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Dùng với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                    "Dùng với warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                    "Dùng với ACE inhibitors, ARBs - tăng nguy cơ suy thận",
                    "Trẻ em <3 tuổi - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Ketorolac là thuốc phân loại C. NSAID có thể qua nhau thai và gây tác dụng phụ ở thai nhi (đóng sớm ống động mạch, suy thận). Tránh dùng trong tam cá nguyệt thứ ba. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong tam cá nguyệt thứ nhất và thứ hai.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Ketorolac có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ ketorolac và nguy cơ tác dụng phụ.",
                "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
                "notes": "Ketorolac chuyển hóa qua gan (CYP2C9, CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: đau bụng nặng, xuất huyết tiêu hóa (phân đen, nôn ra máu) - NGUY HIỂM",
                    "Hấp thu toàn thân: suy thận cấp (giảm lượng nước tiểu, phù) - NGUY HIỂM",
                    "Hấp thu toàn thân: rối loạn đông máu (xuất huyết) - NGUY HIỂM"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Ngừng ngay ketorolac",
                    "  - Nếu xuất huyết tiêu hóa:",
                    "    - Hỗ trợ huyết động (truyền dịch, máu nếu cần)",
                    "    - Nội soi dạ dày nếu cần",
                    "    - PPI (omeprazole, pantoprazole) để giảm acid dạ dày",
                    "  - Nếu suy thận cấp:",
                    "    - Hỗ trợ huyết động",
                    "    - Lọc máu nếu cần",
                    "  - Theo dõi dấu hiệu sinh tồn, chức năng thận, đông máu",
                    "Theo dõi: Dấu hiệu sinh tồn, lượng nước tiểu, chức năng thận, dấu hiệu xuất huyết"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng nước tiểu, chức năng thận, dấu hiệu xuất huyết cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (xuất huyết tiêu hóa, suy thận cấp)."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là rửa mắt và điều trị hỗ trợ. Nếu hấp thu toàn thân nặng: ngừng thuốc, điều trị xuất huyết tiêu hóa (PPI, hỗ trợ huyết động), suy thận cấp (hỗ trợ huyết động, lọc máu nếu cần)."
            },
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.4% hoặc 0.5%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "4 lần/ngày. Bắt đầu 24 giờ sau phẫu thuật mắt cho điều trị viêm sau phẫu thuật.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, 2) TRÁNH DÙNG với NSAID đường uống, 3) Kích ứng mắt phổ biến, 4) Hấp thu toàn thân có thể gây loét dạ dày, suy thận, 5) Nhìn mờ tạm thời - không lái xe ngay."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Ketorolac (Acular)",
                    "UpToDate - Ketorolac: Drug Information",
                    "Medscape - Ketorolac Drug Reference",
                    "AAO Guidelines - Postoperative Inflammation, CME"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI toxicity (if systemic absorption occurs) - CRITICAL", "Renal toxicity (if systemic absorption occurs) - CRITICAL", "Bleeding risk (if systemic absorption occurs) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in inflammation, pain)", "Signs of eye irritation (redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Signs of systemic side effects (rare): GI pain, bleeding, renal impairment - CRITICAL"]
            },
            "guideline_tags": [
                "AAO Guidelines - Postoperative Inflammation",
                "AAO Guidelines - Cystoid Macular Edema",
                "FDA Drug Information - Ketorolac Eye Drops",
                "FDA Black Box Warning - Ketorolac and GI/Renal Toxicity",
                "UpToDate - Postoperative Eye Inflammation"
            ]
        },

        "Nepafenac eye drops": {
            "group": "Ophthalmology - NSAID Prodrug (Anti-inflammatory)",
            "vietnamese_name": "Nepafenac, Nevanac",
            "administration": ["Ophthalmic"],
            "indications": [
                "Điều trị viêm sau phẫu thuật mắt (postoperative inflammation)",
                "Giảm đau sau phẫu thuật mắt (postoperative pain)",
                "Dự phòng và điều trị phù hoàng điểm dạng nang (cystoid macular edema - CME) sau phẫu thuật mắt",
                "Điều trị viêm màng bồ đào (uveitis)"
            ],
            "contraindications": [
                "Dị ứng nepafenac hoặc NSAID",
                "Loét dạ dày tá tràng hoạt động",
                "Xuất huyết tiêu hóa gần đây",
                "Suy thận nặng",
                "Suy gan nặng",
                "Rối loạn đông máu nặng"
            ],
            "dosage": {
                "adult_postop_inflammation": "1 giọt vào mắt phẫu thuật x 3 lần/ngày bắt đầu 24 giờ sau phẫu thuật, trong 2 tuần",
                "adult_cme_prophylaxis": "1 giọt vào mắt phẫu thuật x 3 lần/ngày bắt đầu 24 giờ sau phẫu thuật, trong 4 tuần",
                "notes": "Nepafenac là NSAID prodrug, chuyển hóa thành amfenac (active metabolite) trong mắt. Tác dụng tương tự ketorolac và diclofenac nhưng có thể ít kích ứng mắt hơn do là prodrug. Dùng 3 lần/ngày. Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (loét dạ dày, suy thận)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, theo dõi chức năng thận",
                "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
            },
            "side_effects": [
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa, châm chích) - phổ biến",
                "Nhìn mờ tạm thời",
                "Khô mắt",
                "Đau mắt",
                "Hấp thu toàn thân: loét dạ dày tá tràng - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: suy thận cấp - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: xuất huyết tiêu hóa - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: rối loạn đông máu - hiếm",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm"
            ],
            "interactions": [
                "NSAID đường uống (aspirin, ibuprofen, naproxen): tăng nguy cơ loét dạ dày, suy thận",
                "Warfarin, thuốc chống đông: tăng nguy cơ xuất huyết",
                "ACE inhibitors, ARBs: tăng nguy cơ suy thận",
                "Corticosteroid: tăng nguy cơ loét dạ dày",
                "Lithium: tăng nồng độ lithium"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Nepafenac là NSAID prodrug. Chuyển hóa thành amfenac (active metabolite) trong mắt bởi hydrolase. Amfenac ức chế enzyme cyclooxygenase (COX-1 và COX-2), ngăn chặn sự tổng hợp prostaglandin từ arachidonic acid. Prostaglandin là chất trung gian gây viêm, đau, và sốt. Giảm prostaglandin dẫn đến: (1) Giảm viêm (giảm đỏ, sưng), (2) Giảm đau, (3) Giảm phù hoàng điểm dạng nang (CME) sau phẫu thuật mắt. Nepafenac là prodrug, có thể ít kích ứng mắt hơn ketorolac và diclofenac do chuyển hóa tại mắt. ĐẶC ĐIỂM: (1) NSAID prodrug, chuyển hóa thành amfenac trong mắt, (2) Dùng 3 lần/ngày, (3) Có thể ít kích ứng mắt hơn ketorolac và diclofenac, (4) Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (loét dạ dày, suy thận), (5) CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, (6) Hiệu quả cho viêm và đau sau phẫu thuật mắt, CME.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, đau) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa, châm chích tăng)",
                "Dấu hiệu hấp thu toàn thân: đau bụng, xuất huyết tiêu hóa (phân đen, nôn ra máu) - NGUY HIỂM",
                "Dấu hiệu hấp thu toàn thân: suy thận (giảm lượng nước tiểu, phù) - NGUY HIỂM",
                "Chức năng thận (creatinine, eGFR) - nếu dùng kéo dài hoặc có nguy cơ",
                "Thị lực (nhìn mờ tạm thời)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, xuất huyết tiêu hóa gần đây",
                "Kích ứng mắt - phổ biến nhưng có thể ít hơn ketorolac và diclofenac",
                "Hấp thu toàn thân - có thể gây loét dạ dày, suy thận, xuất huyết tiêu hóa",
                "TRÁNH DÙNG với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                "Thận trọng ở bệnh nhân dùng warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                "Thận trọng ở bệnh nhân dùng ACE inhibitors, ARBs - tăng nguy cơ suy thận",
                "Thận trọng ở bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Nhìn mờ tạm thời - bệnh nhân không nên lái xe ngay sau khi nhỏ"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Vài giờ",
                "duration": "6-8 giờ (dùng 3 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt (nepafenac → amfenac bởi hydrolase), sau đó gan (nếu hấp thu toàn thân, CYP2C9)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "Nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa, suy thận cấp nếu hấp thu toàn thân. CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, xuất huyết tiêu hóa gần đây. TRÁNH DÙNG với NSAID đường uống.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "NSAID đường uống (Aspirin, Ibuprofen, Naproxen, Ketorolac, Diclofenac)",
                        "mechanism": "Cả hai đều ức chế COX, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa, suy thận cấp",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi dấu hiệu loét dạ dày, suy thận sát."
                    },
                    {
                        "drug": "Warfarin, Thuốc chống đông (Heparin, Enoxaparin, Dabigatran, Rivaroxaban)",
                        "mechanism": "NSAID ức chế COX-1, giảm sản xuất thromboxane, tăng nguy cơ xuất huyết",
                        "effect": "Tăng nguy cơ xuất huyết (đặc biệt xuất huyết tiêu hóa)",
                        "management": "Thận trọng. Theo dõi INR, dấu hiệu xuất huyết sát."
                    }
                ],
                "moderate": [
                    {
                        "drug": "ACE Inhibitors, ARBs (Lisinopril, Losartan, Valsartan)",
                        "mechanism": "NSAID giảm sản xuất prostaglandin, giảm lưu lượng máu thận, tác dụng cộng dồn với ACE inhibitors/ARBs",
                        "effect": "Tăng nguy cơ suy thận cấp",
                        "management": "Thận trọng. Theo dõi chức năng thận sát."
                    },
                    {
                        "drug": "Corticosteroid (Prednisone, Dexamethasone)",
                        "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày",
                        "effect": "Tăng nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa",
                        "management": "Thận trọng. Có thể cần dùng PPI (proton pump inhibitor) để bảo vệ dạ dày."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng nepafenac hoặc NSAID",
                    "Loét dạ dày tá tràng hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Xuất huyết tiêu hóa gần đây - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Rối loạn đông máu nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, theo dõi chức năng thận",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Dùng với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                    "Dùng với warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                    "Dùng với ACE inhibitors, ARBs - tăng nguy cơ suy thận"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng nepafenac hoặc NSAID",
                    "Loét dạ dày tá tràng hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Xuất huyết tiêu hóa gần đây - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Rối loạn đông máu nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, theo dõi chức năng thận",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Dùng với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                    "Dùng với warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                    "Dùng với ACE inhibitors, ARBs - tăng nguy cơ suy thận"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Nepafenac là thuốc phân loại C. NSAID có thể qua nhau thai và gây tác dụng phụ ở thai nhi (đóng sớm ống động mạch, suy thận). Tránh dùng trong tam cá nguyệt thứ ba. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong tam cá nguyệt thứ nhất và thứ hai.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Nepafenac có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ nepafenac/amfenac và nguy cơ tác dụng phụ.",
                "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
                "notes": "Nepafenac chuyển hóa tại mắt thành amfenac, sau đó gan (nếu hấp thu toàn thân, CYP2C9). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: đau bụng nặng, xuất huyết tiêu hóa (phân đen, nôn ra máu) - NGUY HIỂM",
                    "Hấp thu toàn thân: suy thận cấp (giảm lượng nước tiểu, phù) - NGUY HIỂM",
                    "Hấp thu toàn thân: rối loạn đông máu (xuất huyết) - NGUY HIỂM"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Ngừng ngay nepafenac",
                    "  - Nếu xuất huyết tiêu hóa:",
                    "    - Hỗ trợ huyết động (truyền dịch, máu nếu cần)",
                    "    - Nội soi dạ dày nếu cần",
                    "    - PPI (omeprazole, pantoprazole) để giảm acid dạ dày",
                    "  - Nếu suy thận cấp:",
                    "    - Hỗ trợ huyết động",
                    "    - Lọc máu nếu cần",
                    "  - Theo dõi dấu hiệu sinh tồn, chức năng thận, đông máu",
                    "Theo dõi: Dấu hiệu sinh tồn, lượng nước tiểu, chức năng thận, dấu hiệu xuất huyết"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng nước tiểu, chức năng thận, dấu hiệu xuất huyết cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (xuất huyết tiêu hóa, suy thận cấp)."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là rửa mắt và điều trị hỗ trợ. Nếu hấp thu toàn thân nặng: ngừng thuốc, điều trị xuất huyết tiêu hóa (PPI, hỗ trợ huyết động), suy thận cấp (hỗ trợ huyết động, lọc máu nếu cần)."
            },
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.1%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 3 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "3 lần/ngày. Bắt đầu 24 giờ sau phẫu thuật mắt cho điều trị viêm sau phẫu thuật.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, 2) TRÁNH DÙNG với NSAID đường uống, 3) Kích ứng mắt phổ biến nhưng có thể ít hơn ketorolac và diclofenac, 4) Hấp thu toàn thân có thể gây loét dạ dày, suy thận, 5) Nhìn mờ tạm thời - không lái xe ngay."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Nepafenac (Nevanac)",
                    "UpToDate - Nepafenac: Drug Information",
                    "Medscape - Nepafenac Drug Reference",
                    "AAO Guidelines - Postoperative Inflammation, CME"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["GI toxicity (rare, if systemic absorption occurs)", "Renal toxicity (rare, if systemic absorption occurs)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in inflammation, pain)", "Signs of eye irritation (redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Signs of systemic side effects (rare): GI pain"]
            },
            "guideline_tags": [
                "AAO Guidelines - Postoperative Inflammation",
                "AAO Guidelines - Cystoid Macular Edema",
                "FDA Drug Information - Nepafenac Eye Drops",
                "UpToDate - Postoperative Eye Inflammation"
            ]
        },

        "Prednisolone eye drops": {
            "group": "Ophthalmology - Corticosteroid (Anti-inflammatory)",
            "vietnamese_name": "Prednisolone nhỏ mắt, Pred Forte",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc dị ứng (allergic conjunctivitis)",
                "Viêm màng bồ đào (uveitis)",
                "Viêm giác mạc (keratitis)",
                "Viêm sau phẫu thuật mắt (postoperative inflammation)",
                "Viêm màng bồ đào do miễn dịch (immune-mediated uveitis)"
            ],
            "contraindications": [
                "Dị ứng prednisolone hoặc corticosteroid",
                "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH",
                "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH",
                "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH",
                "Tăng nhãn áp (glaucoma) - thận trọng",
                "Đục thủy tinh thể (cataract) - thận trọng"
            ],
            "dosage": {
                "adult_conjunctivitis": "1-2 giọt vào mắt bị ảnh hưởng 4-6 lần/ngày, giảm dần khi cải thiện",
                "adult_uveitis": "1-2 giọt vào mắt bị ảnh hưởng mỗi giờ trong 24-48 giờ đầu, sau đó giảm dần",
                "adult_postoperative": "1-2 giọt vào mắt bị ảnh hưởng 4-6 lần/ngày trong 1-2 tuần",
                "notes": "Prednisolone là corticosteroid mạnh, chống viêm hiệu quả. Dùng thường xuyên trong giai đoạn đầu, sau đó giảm dần. Điều trị thường 1-4 tuần. Nguy cơ tăng nhãn áp và đục thủy tinh thể nếu dùng kéo dài."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Tăng nhãn áp (glaucoma) - phổ biến nếu dùng kéo dài",
                "Đục thủy tinh thể (cataract) - phổ biến nếu dùng kéo dài",
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ",
                "Nhiễm trùng mắt (nếu dùng kéo dài, ức chế miễn dịch) - nguy hiểm",
                "Chậm lành vết thương",
                "Phản ứng dị ứng - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Prednisolone là corticosteroid tổng hợp mạnh. Gắn với thụ thể glucocorticoid trong tế bào, ức chế quá trình viêm bằng cách: (1) Ức chế giải phóng các chất trung gian viêm (prostaglandin, leukotriene, cytokine), (2) Ức chế di chuyển và hoạt động của bạch cầu, (3) Ức chế sản xuất kháng thể, (4) Ổn định màng tế bào. Dẫn đến: giảm viêm, giảm đỏ, giảm sưng, giảm đau. ĐẶC ĐIỂM: (1) Corticosteroid mạnh, chống viêm hiệu quả, (2) Dùng thường xuyên trong giai đoạn đầu, sau đó giảm dần, (3) Nguy cơ tăng nhãn áp và đục thủy tinh thể nếu dùng kéo dài, (4) CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm, (5) Ức chế miễn dịch, tăng nguy cơ nhiễm trùng nếu dùng kéo dài.",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG: theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu đục thủy tinh thể (giảm thị lực, nhìn mờ) - nếu dùng kéo dài",
                "Dấu hiệu nhiễm trùng mắt (đỏ, chảy mủ, đau) - nguy hiểm nếu dùng kéo dài",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Dấu hiệu viêm (đỏ, sưng) - cải thiện sau vài ngày"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus (herpes simplex, varicella) - có thể làm nặng",
                "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do nấm - có thể làm nặng",
                "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do vi khuẩn chưa điều trị - có thể làm nặng",
                "NGUY CƠ TĂNG NHÃN ÁP - theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
                "NGUY CƠ ĐỤC THỦY TINH THỂ - theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
                "Nguy cơ nhiễm trùng mắt nếu dùng kéo dài (ức chế miễn dịch)",
                "Chậm lành vết thương",
                "Dùng đủ liều và đủ thời gian, nhưng tránh dùng kéo dài không cần thiết",
                "Giảm dần liều khi cải thiện để tránh tái phát",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "2-3 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
                "onset": "Vài giờ",
                "duration": "4-6 giờ (dùng 4-6 lần/ngày)",
                "protein_binding": "90-95%",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "NGUY CƠ TĂNG NHÃN ÁP VÀ ĐỤC THỦY TINH THỂ nếu dùng kéo dài. CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm. Ức chế miễn dịch, tăng nguy cơ nhiễm trùng nếu dùng kéo dài. Phải theo dõi nhãn áp định kỳ.",
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng prednisolone hoặc corticosteroid",
                    "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                    "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                    "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH (có thể làm nặng)"
                ],
                "tương_đối": [
                    "Tăng nhãn áp (glaucoma) - thận trọng, theo dõi nhãn áp định kỳ",
                    "Đục thủy tinh thể (cataract) - thận trọng, có thể làm nặng",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng prednisolone hoặc corticosteroid",
                    "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                    "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                    "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH (có thể làm nặng)"
                ],
                "tương_đối": [
                    "Tăng nhãn áp (glaucoma) - thận trọng, theo dõi nhãn áp định kỳ",
                    "Đục thủy tinh thể (cataract) - thận trọng, có thể làm nặng",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Prednisolone là thuốc phân loại C. Prednisolone có thể hấp thu toàn thân và qua nhau thai. Corticosteroid có thể gây dị tật bẩm sinh ở động vật. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Prednisolone có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Prednisolone dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Tăng nhãn áp nặng (nếu dùng kéo dài)",
                    "Đục thủy tinh thể (nếu dùng kéo dài)",
                    "Nhiễm trùng mắt (nếu dùng kéo dài)"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ. Giảm liều hoặc ngừng nếu có tác dụng phụ nặng.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Nếu tăng nhãn áp nặng:",
                    "  - Ngừng prednisolone",
                    "  - Điều trị tăng nhãn áp (thuốc giảm nhãn áp)",
                    "Nếu nhiễm trùng mắt:",
                    "  - Ngừng prednisolone",
                    "  - Điều trị nhiễm trùng (kháng sinh, kháng virus, kháng nấm)",
                    "Theo dõi: Thị lực, nhãn áp, dấu hiệu viêm, dấu hiệu nhiễm trùng"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu viêm, dấu hiệu nhiễm trùng cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng nhãn áp, đục thủy tinh thể, nhiễm trùng)."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là rửa mắt và điều trị hỗ trợ. Nếu tăng nhãn áp nặng: ngừng thuốc và điều trị tăng nhãn áp. Nếu nhiễm trùng mắt: ngừng thuốc và điều trị nhiễm trùng."
            },
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.12%, 0.5%, hoặc 1%.",
                    "application": "1-2 giọt vào mắt bị ảnh hưởng theo lịch trình (xem dosage). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "Tùy theo chỉ định: 4-6 lần/ngày (conjunctivitis, postoperative) hoặc mỗi giờ (uveitis).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm, 2) NGUY CƠ TĂNG NHÃN ÁP VÀ ĐỤC THỦY TINH THỂ nếu dùng kéo dài, 3) Theo dõi nhãn áp định kỳ, 4) Giảm dần liều khi cải thiện, 5) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Prednisolone (Pred Forte)",
                    "UpToDate - Prednisolone: Drug Information",
                    "Medscape - Prednisolone Drug Reference",
                    "AAO Guidelines - Uveitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Increased intraocular pressure (glaucoma) - CRITICAL (common with prolonged use)", "Cataract formation - CRITICAL (common with prolonged use)", "Ocular infections (if used long-term, immunosuppression)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Intraocular pressure (IOP) - CRITICAL (periodic monitoring, especially with prolonged use)", "Vision and eye examination", "Signs of cataract (decreased vision, blurred vision) - if used long-term", "Signs of ocular infection (redness, discharge, pain) - dangerous if used long-term", "Signs of eye irritation"]
            },
            "guideline_tags": [
                "AAO Guidelines - Uveitis",
                "AAO Guidelines - Postoperative Inflammation",
                "FDA Black Box Warning - Prednisolone Eye Drops and Glaucoma/Cataract",
                "FDA Drug Information - Prednisolone Eye Drops"
            ]
        },

}

__all__ = ['ANTI_INFLAMMATORY_DRUGS']
