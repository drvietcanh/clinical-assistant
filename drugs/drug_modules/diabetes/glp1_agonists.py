"""
GLP-1 Receptor Agonists (Thuốc chủ vận thụ thể GLP-1)
Nhóm thuốc tiêm cho đái tháo đường type 2, có lợi ích giảm cân và tim mạch.
"""

GLP1_AGONISTS_DRUGS = {
    "Liraglutide":     {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Liraglutide, Victoza, Saxenda",
        "brand_names": {
            "common": [
                "Victoza (ĐTĐ)",
                "Saxenda (Giảm cân)"
    ],
            "vietnam": [
                "Victoza 6mg/ml"
    ],
        },
        "administration": [
            "SC (Tiêm dưới da)"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm cân (Saxenda 3mg) - Chỉ định riêng",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch"
    ],
        "contraindications": [
            "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
            "Tiền sử viêm tụy cấp",
            "Đái tháo đường type 1",
            "Nhiễm toan ceton đái tháo đường"
    ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
                "Tiền sử viêm tụy cấp",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng với liraglutide hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, có thể cần giảm liều",
                "Suy gan - thận trọng, theo dõi chức năng gan",
                "Bệnh nhân cao tuổi - tăng nguy cơ buồn nôn, mất nước",
                "Bệnh nhân có bệnh dạ dày - tăng nguy cơ buồn nôn, nôn",
                "Phụ nữ có thai - không có dữ liệu đầy đủ về an toàn"
            ]
        },
        "dosage": {
            "adult_start": "0.6mg SC x 1 lần/ngày x 1 tuần (Victoza - đái tháo đường type 2)",
            "adult_usual": "1.2-1.8mg SC x 1 lần/ngày (Victoza - đái tháo đường type 2). Tối đa 1.8mg/ngày.",
            "adult_max": "1.8mg/ngày (Victoza - đái tháo đường type 2) hoặc 3mg/ngày (Saxenda - giảm cân)",
            "dm_t2": "Khởi đầu 0.6mg SC x 1 lần/ngày x 1 tuần, sau đó tăng lên 1.2mg x 1 lần/ngày. Có thể tăng lên 1.8mg nếu cần (sau ít nhất 1 tuần ở liều 1.2mg). Tối đa 1.8mg/ngày.",
            "weight_loss": "Saxenda (chỉ định giảm cân): Khởi đầu 0.6mg SC x 1 lần/ngày x 1 tuần, tăng dần mỗi tuần: Tuần 2: 1.2mg/ngày, Tuần 3: 1.8mg/ngày, Tuần 4: 2.4mg/ngày, Tuần 5: 3mg/ngày. Tối đa 3mg/ngày.",
            "cardiovascular_benefit": "1.8mg SC x 1 lần/ngày (Victoza) - dựa trên LEADER trial, giảm biến cố tim mạch lớn ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch.",
            "elderly": "Khởi đầu 0.6mg SC x 1 lần/ngày x 1 tuần, tăng dần chậm hơn (mỗi 2 tuần thay vì 1 tuần). Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn nôn, mất nước).",
            "renal_adjustment_dosage": {
                "normal": "1.2-1.8mg SC x 1 lần/ngày (CrCl ≥60)",
                "30_60": "Có thể dùng nhưng thận trọng. Khởi đầu 0.6mg/ngày, tăng dần chậm. Theo dõi chức năng thận (CrCl 30-60)",
                "under_30": "Thận trọng, có thể cần giảm liều. Khởi đầu 0.6mg/ngày, tăng dần rất chậm. Theo dõi chức năng thận chặt chẽ (CrCl <30)",
                "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu. Cân nhắc lợi ích/nguy cơ."
            },
            "hepatic_adjustment_dosage": {
                "mild": "1.2-1.8mg SC x 1 lần/ngày. Không cần điều chỉnh liều đặc biệt.",
                "moderate": "1.2-1.8mg SC x 1 lần/ngày. Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều. Khởi đầu 0.6mg/ngày, tăng dần chậm. Theo dõi chức năng gan chặt chẽ."
            },
            "administration_route": "SC (tiêm dưới da)",
            "frequency": "1 lần/ngày",
            "with_food": "Không phụ thuộc bữa ăn. Có thể tiêm bất kỳ lúc nào trong ngày, nhưng nên tiêm cùng giờ mỗi ngày.",
            "timing": "Tiêm 1 lần/ngày vào cùng một giờ mỗi ngày. Có thể tiêm bất kỳ lúc nào trong ngày (sáng, trưa, tối), không phụ thuộc bữa ăn. Tiêm cùng giờ mỗi ngày để duy trì nồng độ ổn định.",
            "titration": "Tăng liều từ từ để giảm buồn nôn: Tuần 1: 0.6mg/ngày. Tuần 2: 1.2mg/ngày (nếu dung nạp tốt). Tuần 3: 1.8mg/ngày (nếu cần và dung nạp tốt). Nếu buồn nôn nặng, giữ ở liều thấp hơn lâu hơn. Đánh giá hiệu quả sau mỗi 4-8 tuần.",
            "notes": "Tiêm dưới da (bụng, đùi, cánh tay) mỗi ngày, cùng giờ. Tăng liều từ từ để giảm buồn nôn (rất phổ biến ~40%, giảm dần sau vài tuần). Victoza: tối đa 1.8mg/ngày cho đái tháo đường type 2. Saxenda: tối đa 3mg/ngày cho giảm cân. Lợi ích tim mạch: 1.8mg/ngày giảm biến cố tim mạch lớn (LEADER trial)."
        },
        "side_effects": [
            "Buồn nôn, nôn (Rất phổ biến ~40%, giảm dần sau vài tuần)",
            "Tiêu chảy",
            "Táo bón",
            "Đau bụng",
            "Giảm cân (Tác dụng mong muốn, ~3-5kg)",
            "Viêm tụy cấp (Hiếm nhưng nghiêm trọng)",
            "Tăng nhịp tim nhẹ"
    ],
        "interactions": [
            "Insulin, Sulfonylurea: Tăng nguy cơ hạ đường huyết (cần giảm liều).",
            "Thuốc uống: Làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống."
    ],
        "mechanism_of_action": """Chủ vận thụ thể GLP-1 (Glucagon-Like Peptide-1): Tăng tiết insulin phụ thuộc glucose, giảm tiết glucagon, làm chậm làm rỗng dạ dày, tăng cảm giác no → Giảm đường huyết và giảm cân. Lợi ích tim mạch: Giảm biến cố tim mạch lớn (LEADER trial).""",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu)",
            "Cân nặng (giảm cân là tác dụng mong muốn)",
            "Dấu hiệu viêm tụy (đau bụng dữ dội, buồn nôn, nôn)",
            "Nhịp tim",
            "Dấu hiệu hạ đường huyết (nếu dùng với insulin/SU)"
    ],
        "precautions": [
            "Buồn nôn rất phổ biến - Tăng liều từ từ, uống thuốc chống nôn nếu cần",
            "Nguy cơ viêm tụy - Ngừng thuốc nếu nghi ngờ viêm tụy",
            "Nguy cơ ung thư tuyến giáp tủy (MTC) - Chống chỉ định nếu có tiền sử MTC hoặc MEN 2",
            "Giảm liều insulin/sulfonylurea khi bắt đầu dùng",
            "Lợi ích giảm cân và tim mạch lớn",
            "Tiêm mỗi ngày - Tuân thủ điều trị có thể khó"
    ],
        "black_box_warnings": """Nguy cơ ung thư tuyến giáp tủy (MTC) ở động vật thí nghiệm. Chống chỉ định ở bệnh nhân có tiền sử MTC hoặc MEN 2.""",
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "pharmacokinetics": {
            "half_life": "13 giờ",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": ">98%",
            "metabolism": "Chuyển hóa giống protein (proteolytic degradation)",
            "clearance": "Thận (6% nguyên dạng), chuyển hóa nội bào"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C (tủ lạnh) trước khi mở. Sau khi mở, có thể bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh trong tối đa 30 ngày. Tránh đông lạnh. Tránh ánh sáng trực tiếp.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Không khuyến nghị dùng trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Liraglutide bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Theo dõi trẻ bú mẹ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Liraglutide chuyển hóa giống protein (proteolytic degradation), không phụ thuộc vào chức năng gan. Suy gan nhẹ đến trung bình không cần điều chỉnh liều. Suy gan nặng có thể làm giảm chuyển hóa, tăng nồng độ thuốc."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "Liraglutide thải trừ một phần qua thận (6% nguyên dạng). Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nghiêm trọng",
                "Tiêu chảy",
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Đau bụng",
                "Viêm tụy cấp (hiếm nhưng nghiêm trọng)",
                "Mất nước do nôn nhiều"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng thuốc, điều chỉnh đường huyết, điều trị viêm tụy nếu có.",
            "treatment": [
                "Ngừng liraglutide ngay lập tức",
                "Điều trị hạ đường huyết nếu có: Glucose PO hoặc IV (dextrose 50% 50ml IV)",
                "Điều trị buồn nôn/nôn: Thuốc chống nôn (ondansetron, metoclopramide)",
                "Bù dịch nếu mất nước: Normal saline IV",
                "Điều trị viêm tụy cấp nếu có: Nhịn ăn, bù dịch, giảm đau, theo dõi sát",
                "Theo dõi đường huyết, điện giải, chức năng thận, amylase/lipase nếu nghi ngờ viêm tụy",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Đường huyết, điện giải (Na, K, Cl), chức năng thận (creatinine, eGFR), amylase/lipase (nếu nghi ngờ viêm tụy), dấu hiệu mất nước, dấu hiệu viêm tụy (đau bụng dữ dội, buồn nôn, nôn)"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },
        "administration_instructions": {
            "sc": {
                "injection_sites": "Bụng, đùi, hoặc cánh tay. Luân chuyển vị trí tiêm để tránh kích ứng da.",
                "timing": "Tiêm 1 lần/ngày vào cùng một giờ mỗi ngày. Có thể tiêm bất kỳ lúc nào trong ngày, không phụ thuộc bữa ăn.",
                "technique": "Tiêm dưới da (subcutaneous). Không tiêm vào tĩnh mạch hoặc cơ. Không tiêm vào vùng da bị kích ứng, đỏ, hoặc cứng.",
                "notes": "Khởi đầu với liều thấp (0.6mg) x 1 tuần để giảm buồn nôn, sau đó tăng dần. Bảo quản ở tủ lạnh (2-8°C) trước khi mở. Sau khi mở, có thể bảo quản ở nhiệt độ phòng hoặc tủ lạnh trong tối đa 30 ngày."
            },
            "oral": {
                "reconstitution": "Không có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng tiêm dưới da (SC)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Victoza (liraglutide), Saxenda (liraglutide)",
                "UpToDate - Liraglutide: Drug information",
                "LEADER Study - New England Journal of Medicine (2016) - Liraglutide trong đái tháo đường type 2 và bệnh tim mạch",
                "SCALE Study - New England Journal of Medicine (2015) - Liraglutide cho giảm cân",
                "American Diabetes Association guidelines - GLP-1 receptor agonists"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Multiple large RCTs (LEADER, SCALE) showing cardiovascular benefits and weight loss"
        },
    },
    "Semaglutide":     {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Semaglutide, Ozempic, Wegovy, Rybelsus",
        "brand_names": {
            "common": [
                "Ozempic (ĐTĐ - tiêm)",
                "Wegovy (Giảm cân - tiêm)",
                "Rybelsus (ĐTĐ - uống)"
    ],
            "vietnam": [
                "Ozempic 0.25/0.5/1mg",
                "Rybelsus 3/7/14mg"
    ],
        },
        "administration": [
            "SC (Tiêm dưới da - Ozempic, Wegovy)",
            "PO (Uống - Rybelsus)"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm cân (Wegovy 2.4mg) - Chỉ định riêng",
            "Giảm nguy cơ biến cố tim mạch"
    ],
        "dosage": {
            "adult_start": "0.25mg SC x 1 lần/tuần x 4 tuần (Ozempic - đái tháo đường type 2) hoặc 3mg PO x 1 lần/sáng x 30 ngày (Rybelsus - đái tháo đường type 2)",
            "adult_usual": "0.5-2mg SC x 1 lần/tuần (Ozempic) hoặc 7-14mg PO x 1 lần/sáng (Rybelsus). Tối đa 2mg/tuần (Ozempic) hoặc 14mg/ngày (Rybelsus).",
            "adult_max": "2mg/tuần (Ozempic - đái tháo đường type 2) hoặc 14mg/ngày (Rybelsus) hoặc 2.4mg/tuần (Wegovy - giảm cân)",
            "dm_t2_injection": "Ozempic: Khởi đầu 0.25mg SC x 1 lần/tuần x 4 tuần, sau đó 0.5mg x 1 lần/tuần. Có thể tăng lên 1mg sau ít nhất 4 tuần ở liều 0.5mg, hoặc 2mg sau ít nhất 4 tuần ở liều 1mg nếu cần. Tối đa 2mg/tuần.",
            "dm_t2_oral": "Rybelsus: Khởi đầu 3mg PO x 1 lần/sáng x 30 ngày (uống lúc đói, với ít nước, chờ 30 phút mới ăn), sau đó 7mg x 1 lần/sáng. Có thể tăng lên 14mg sau ít nhất 30 ngày ở liều 7mg nếu cần. Tối đa 14mg/ngày.",
            "weight_loss": "Wegovy (chỉ định giảm cân): Tăng dần từ 0.25mg SC x 1 lần/tuần x 4 tuần, sau đó 0.5mg/tuần x 4 tuần, 1mg/tuần x 4 tuần, 1.7mg/tuần x 4 tuần, cuối cùng 2.4mg/tuần. Tối đa 2.4mg/tuần.",
            "cardiovascular_benefit": "0.5-1mg SC x 1 lần/tuần (Ozempic) - dựa trên SUSTAIN-6 trial, giảm biến cố tim mạch lớn ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch.",
            "elderly": "Khởi đầu 0.25mg SC x 1 lần/tuần x 4 tuần (tiêm) hoặc 3mg PO x 1 lần/sáng x 30 ngày (uống), tăng dần chậm hơn. Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn nôn, mất nước).",
            "renal_adjustment_dosage": {
                "normal": "0.5-2mg SC x 1 lần/tuần (Ozempic) hoặc 7-14mg PO x 1 lần/sáng (Rybelsus) (CrCl ≥60)",
                "30_60": "Có thể dùng nhưng thận trọng. Khởi đầu 0.25mg/tuần (tiêm) hoặc 3mg/ngày (uống), tăng dần chậm. Theo dõi chức năng thận (CrCl 30-60)",
                "under_30": "Thận trọng, có thể cần giảm liều. Khởi đầu 0.25mg/tuần (tiêm) hoặc 3mg/ngày (uống), tăng dần rất chậm. Theo dõi chức năng thận chặt chẽ (CrCl <30)",
                "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu. Cân nhắc lợi ích/nguy cơ."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.5-2mg SC x 1 lần/tuần (Ozempic) hoặc 7-14mg PO x 1 lần/sáng (Rybelsus). Không cần điều chỉnh liều đặc biệt.",
                "moderate": "0.5-2mg SC x 1 lần/tuần (Ozempic) hoặc 7-14mg PO x 1 lần/sáng (Rybelsus). Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều. Khởi đầu 0.25mg/tuần (tiêm) hoặc 3mg/ngày (uống), tăng dần chậm. Theo dõi chức năng gan chặt chẽ."
            },
            "administration_route": "SC (tiêm dưới da) - Ozempic, Wegovy. PO (uống) - Rybelsus.",
            "frequency": "1 lần/tuần (tiêm - Ozempic, Wegovy) hoặc 1 lần/ngày (uống - Rybelsus)",
            "with_food": "Tiêm (Ozempic, Wegovy): Không phụ thuộc bữa ăn. Có thể tiêm bất kỳ lúc nào trong ngày, cùng ngày mỗi tuần. Uống (Rybelsus): Phải uống lúc đói, với ít nước (≤120ml), chờ 30 phút mới ăn hoặc uống thuốc khác.",
            "timing": "Tiêm (Ozempic, Wegovy): Tiêm 1 lần/tuần vào cùng một ngày mỗi tuần, bất kỳ giờ nào trong ngày, không phụ thuộc bữa ăn. Uống (Rybelsus): Uống 1 lần/ngày vào buổi sáng, lúc đói, với ít nước (≤120ml), chờ 30 phút mới ăn hoặc uống thuốc khác.",
            "titration": "Tiêm (Ozempic): Tuần 1-4: 0.25mg/tuần. Tuần 5-8: 0.5mg/tuần. Tuần 9-12: 1mg/tuần (nếu cần). Tuần 13+: 2mg/tuần (nếu cần). Uống (Rybelsus): Ngày 1-30: 3mg/ngày. Ngày 31-60: 7mg/ngày (nếu dung nạp tốt). Ngày 61+: 14mg/ngày (nếu cần và dung nạp tốt). Tăng dần để giảm buồn nôn.",
            "notes": "Tiêm 1 lần/tuần (tiện lợi hơn Liraglutide - 1 lần/ngày). Rybelsus (dạng uống): Uống lúc đói, với ít nước (≤120ml), chờ 30 phút mới ăn hoặc uống thuốc khác (hấp thu kém nếu không tuân thủ). Giảm cân mạnh hơn Liraglutide (~5-10kg vs ~3-5kg). Lợi ích tim mạch: 0.5-1mg/tuần giảm biến cố tim mạch lớn (SUSTAIN-6 trial)."
        },
        "side_effects": [
            "Buồn nôn, nôn (Phổ biến nhưng ít hơn Liraglutide)",
            "Tiêu chảy, táo bón",
            "Đau bụng",
            "Giảm cân (Mạnh hơn Liraglutide, ~5-10kg)",
            "Viêm tụy cấp (Hiếm)",
            "Tăng nhịp tim nhẹ"
    ],
        "mechanism_of_action": """Tương tự Liraglutide nhưng tác dụng kéo dài hơn (tiêm 1 lần/tuần). Lợi ích tim mạch: Giảm biến cố tim mạch lớn (SUSTAIN-6 trial). Giảm cân mạnh hơn Liraglutide.""",
        "monitoring": [
            "Đường huyết, cân nặng",
            "Dấu hiệu viêm tụy",
            "Nhịp tim"
    ],
        "precautions": [
            "Tương tự Liraglutide",
            "Rybelsus (dạng uống): Phải uống lúc đói, chờ 30 phút mới ăn (hấp thu kém)",
            "Giảm cân mạnh - Rất phổ biến hiện nay (Ozempic, Wegovy)"
    ],
        "black_box_warnings": "Nguy cơ ung thư tuyến giáp tủy (MTC). Chống chỉ định nếu có tiền sử MTC hoặc MEN 2.",
        "contraindications": [
            "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
            "Tiền sử viêm tụy cấp",
            "Đái tháo đường type 1",
            "Nhiễm toan ceton đái tháo đường"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
                "Tiền sử viêm tụy cấp",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng với semaglutide hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, có thể cần giảm liều",
                "Suy gan - thận trọng, theo dõi chức năng gan",
                "Bệnh nhân cao tuổi - tăng nguy cơ buồn nôn, mất nước",
                "Bệnh nhân có bệnh dạ dày - tăng nguy cơ buồn nôn, nôn",
                "Phụ nữ có thai - không có dữ liệu đầy đủ về an toàn"
            ]
        },
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "pharmacokinetics": {
            "half_life": "7 ngày (tiêm), 7 ngày (uống)",
            "onset": "1-2 giờ (tiêm), 30 phút (uống)",
            "duration": "7 ngày (tiêm 1 lần/tuần), 24 giờ (uống)",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa giống protein (proteolytic degradation)",
            "clearance": "Thận (3% nguyên dạng), chuyển hóa nội bào"
        },
        "storage": "Ozempic/Wegovy (tiêm): Bảo quản ở nhiệt độ 2-8°C (tủ lạnh) trước khi mở. Sau khi mở, có thể bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh trong tối đa 56 ngày. Tránh đông lạnh. Tránh ánh sáng trực tiếp. Rybelsus (uống): Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Không khuyến nghị dùng trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Semaglutide bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Theo dõi trẻ bú mẹ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Semaglutide chuyển hóa giống protein (proteolytic degradation), không phụ thuộc vào chức năng gan. Suy gan nhẹ đến trung bình không cần điều chỉnh liều. Suy gan nặng có thể làm giảm chuyển hóa, tăng nồng độ thuốc."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "Semaglutide thải trừ một phần qua thận (3% nguyên dạng). Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nghiêm trọng",
                "Tiêu chảy",
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Đau bụng",
                "Viêm tụy cấp (hiếm nhưng nghiêm trọng)",
                "Mất nước do nôn nhiều"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng thuốc, điều chỉnh đường huyết, điều trị viêm tụy nếu có.",
            "treatment": [
                "Ngừng semaglutide ngay lập tức",
                "Điều trị hạ đường huyết nếu có: Glucose PO hoặc IV (dextrose 50% 50ml IV)",
                "Điều trị buồn nôn/nôn: Thuốc chống nôn (ondansetron, metoclopramide)",
                "Bù dịch nếu mất nước: Normal saline IV",
                "Điều trị viêm tụy cấp nếu có: Nhịn ăn, bù dịch, giảm đau, theo dõi sát",
                "Theo dõi đường huyết, điện giải, chức năng thận, amylase/lipase nếu nghi ngờ viêm tụy",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài: 7 ngày)"
            ],
            "monitoring": "Đường huyết, điện giải (Na, K, Cl), chức năng thận (creatinine, eGFR), amylase/lipase (nếu nghi ngờ viêm tụy), dấu hiệu mất nước, dấu hiệu viêm tụy (đau bụng dữ dội, buồn nôn, nôn)"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },
        "administration_instructions": {
            "sc": {
                "injection_sites": "Bụng, đùi, hoặc cánh tay. Luân chuyển vị trí tiêm để tránh kích ứng da.",
                "timing": "Tiêm 1 lần/tuần vào cùng một ngày mỗi tuần. Có thể tiêm bất kỳ lúc nào trong ngày, không phụ thuộc bữa ăn.",
                "technique": "Tiêm dưới da (subcutaneous). Không tiêm vào tĩnh mạch hoặc cơ. Không tiêm vào vùng da bị kích ứng, đỏ, hoặc cứng.",
                "notes": "Khởi đầu với liều thấp (0.25mg) x 4 tuần để giảm buồn nôn, sau đó tăng dần. Bảo quản ở tủ lạnh (2-8°C) trước khi mở. Sau khi mở, có thể bảo quản ở nhiệt độ phòng hoặc tủ lạnh trong tối đa 56 ngày."
            },
            "oral": {
                "with_food": "QUAN TRỌNG: Phải uống lúc đói, với ít nước (không quá 120ml), chờ 30 phút mới ăn hoặc uống thuốc khác.",
                "timing": "Uống 1 lần/ngày vào buổi sáng, lúc đói. Uống với ít nước (không quá 120ml). Chờ 30 phút trước khi ăn, uống thuốc khác, hoặc uống nước khác.",
                "notes": "Rybelsus: Phải uống lúc đói để hấp thu tốt. Uống với ít nước (không quá 120ml). Chờ 30 phút trước khi ăn hoặc uống thuốc khác. Không nghiền, không nhai viên nén. Nuốt nguyên viên với nước."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ozempic (semaglutide injection), Wegovy (semaglutide injection), Rybelsus (semaglutide oral)",
                "UpToDate - Semaglutide: Drug information",
                "SUSTAIN-6 Study - New England Journal of Medicine (2016) - Semaglutide trong đái tháo đường type 2 và bệnh tim mạch",
                "STEP Studies - New England Journal of Medicine (2021) - Semaglutide cho giảm cân",
                "SELECT Study - New England Journal of Medicine (2023) - Semaglutide trong giảm biến cố tim mạch",
                "American Diabetes Association guidelines - GLP-1 receptor agonists"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Multiple large RCTs (SUSTAIN-6, STEP, SELECT) showing cardiovascular benefits and weight loss"
        },
    },
    "Dulaglutide":     {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Dulaglutide, Trulicity",
        "brand_names": {
            "common": [
                "Trulicity"
    ],
            "vietnam": [
                "Trulicity 0.75/1.5mg"
    ],
        },
        "administration": [
            "SC (Tiêm dưới da)"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm nguy cơ biến cố tim mạch"
    ],
        "dosage": {
            "adult_start": "0.75mg SC x 1 lần/tuần (Trulicity - đái tháo đường type 2)",
            "adult_usual": "0.75-4.5mg SC x 1 lần/tuần. Thường 0.75-1.5mg/tuần. Có thể tăng lên 3mg hoặc 4.5mg nếu cần. Tối đa 4.5mg/tuần.",
            "adult_max": "4.5mg/tuần (Trulicity - đái tháo đường type 2)",
            "dm_t2": "Khởi đầu 0.75mg SC x 1 lần/tuần. Có thể tăng lên 1.5mg sau ít nhất 4 tuần nếu cần. Có thể tăng lên 3mg hoặc 4.5mg sau ít nhất 4 tuần ở liều trước đó nếu cần. Tối đa 4.5mg/tuần.",
            "cardiovascular_benefit": "0.75-1.5mg SC x 1 lần/tuần (Trulicity) - dựa trên REWIND trial, giảm biến cố tim mạch lớn ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch hoặc yếu tố nguy cơ tim mạch.",
            "elderly": "Khởi đầu 0.75mg SC x 1 lần/tuần, tăng dần chậm hơn. Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn nôn, mất nước).",
            "renal_adjustment_dosage": {
                "normal": "0.75-4.5mg SC x 1 lần/tuần (CrCl ≥60)",
                "30_60": "Có thể dùng nhưng thận trọng. Khởi đầu 0.75mg/tuần, tăng dần chậm. Theo dõi chức năng thận (CrCl 30-60)",
                "under_30": "Thận trọng, có thể cần giảm liều. Khởi đầu 0.75mg/tuần, tăng dần rất chậm. Theo dõi chức năng thận chặt chẽ (CrCl <30)",
                "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu. Cân nhắc lợi ích/nguy cơ."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.75-4.5mg SC x 1 lần/tuần. Không cần điều chỉnh liều đặc biệt.",
                "moderate": "0.75-4.5mg SC x 1 lần/tuần. Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều. Khởi đầu 0.75mg/tuần, tăng dần chậm. Theo dõi chức năng gan chặt chẽ."
            },
            "administration_route": "SC (tiêm dưới da)",
            "frequency": "1 lần/tuần",
            "with_food": "Không phụ thuộc bữa ăn. Có thể tiêm bất kỳ lúc nào trong ngày, cùng ngày mỗi tuần.",
            "timing": "Tiêm 1 lần/tuần vào cùng một ngày mỗi tuần, bất kỳ giờ nào trong ngày, không phụ thuộc bữa ăn. Bút tiêm sẵn (pre-filled pen) - Tiện lợi.",
            "titration": "Tăng liều từ từ: Tuần 1-4: 0.75mg/tuần. Tuần 5-8: 1.5mg/tuần (nếu cần). Tuần 9-12: 3mg/tuần (nếu cần). Tuần 13+: 4.5mg/tuần (nếu cần). Tăng dần để giảm buồn nôn.",
            "notes": "Tiêm 1 lần/tuần. Bút tiêm sẵn (pre-filled pen) - Tiện lợi. Lợi ích tim mạch lớn (REWIND trial) - giảm biến cố tim mạch lớn ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch hoặc yếu tố nguy cơ tim mạch."
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Đau bụng",
            "Giảm cân",
            "Viêm tụy (Hiếm)"
    ],
        "mechanism_of_action": "Tương tự các GLP-1 RA khác. Lợi ích tim mạch (REWIND trial). Bút tiêm sẵn tiện lợi.",
        "monitoring": [
            "Đường huyết, cân nặng",
            "Dấu hiệu viêm tụy"
    ],
        "black_box_warnings": "Nguy cơ ung thư tuyến giáp tủy (MTC).",
        "contraindications": [],
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "precautions": [
            "Buồn nôn rất phổ biến - Tăng liều từ từ, uống thuốc chống nôn nếu cần",
            "Nguy cơ viêm tụy - Ngừng thuốc nếu nghi ngờ viêm tụy",
            "Nguy cơ ung thư tuyến giáp tủy (MTC) - Chống chỉ định nếu có tiền sử MTC hoặc MEN 2",
            "Giảm liều insulin/sulfonylurea khi bắt đầu dùng",
            "Lợi ích tim mạch lớn (REWIND trial)",
            "Tiêm 1 lần/tuần - Tiện lợi với bút tiêm sẵn"
        ],
        "pharmacokinetics": {
            "half_life": "5 ngày",
            "onset": "1-2 giờ",
            "duration": "7 ngày (tiêm 1 lần/tuần)",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa giống protein (proteolytic degradation)",
            "clearance": "Thận (chủ yếu), chuyển hóa nội bào"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C (tủ lạnh) trước khi mở. Sau khi mở, có thể bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh trong tối đa 14 ngày. Tránh đông lạnh. Tránh ánh sáng trực tiếp.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Không khuyến nghị dùng trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Dulaglutide bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Theo dõi trẻ bú mẹ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Dulaglutide chuyển hóa giống protein (proteolytic degradation), không phụ thuộc vào chức năng gan. Suy gan nhẹ đến trung bình không cần điều chỉnh liều. Suy gan nặng có thể làm giảm chuyển hóa, tăng nồng độ thuốc."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "Dulaglutide thải trừ chủ yếu qua thận. Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nghiêm trọng",
                "Tiêu chảy",
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Đau bụng",
                "Viêm tụy cấp (hiếm nhưng nghiêm trọng)",
                "Mất nước do nôn nhiều"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng thuốc, điều chỉnh đường huyết, điều trị viêm tụy nếu có.",
            "treatment": [
                "Ngừng dulaglutide ngay lập tức",
                "Điều trị hạ đường huyết nếu có: Glucose PO hoặc IV (dextrose 50% 50ml IV)",
                "Điều trị buồn nôn/nôn: Thuốc chống nôn (ondansetron, metoclopramide)",
                "Bù dịch nếu mất nước: Normal saline IV",
                "Điều trị viêm tụy cấp nếu có: Nhịn ăn, bù dịch, giảm đau, theo dõi sát",
                "Theo dõi đường huyết, điện giải, chức năng thận, amylase/lipase nếu nghi ngờ viêm tụy",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài: 5 ngày)"
            ],
            "monitoring": "Đường huyết, điện giải (Na, K, Cl), chức năng thận (creatinine, eGFR), amylase/lipase (nếu nghi ngờ viêm tụy), dấu hiệu mất nước, dấu hiệu viêm tụy (đau bụng dữ dội, buồn nôn, nôn)"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },
        "administration_instructions": {
            "sc": {
                "injection_sites": "Bụng, đùi, hoặc cánh tay. Luân chuyển vị trí tiêm để tránh kích ứng da.",
                "timing": "Tiêm 1 lần/tuần vào cùng một ngày mỗi tuần. Có thể tiêm bất kỳ lúc nào trong ngày, không phụ thuộc bữa ăn.",
                "technique": "Tiêm dưới da (subcutaneous) bằng bút tiêm sẵn (pre-filled pen). Không tiêm vào tĩnh mạch hoặc cơ. Không tiêm vào vùng da bị kích ứng, đỏ, hoặc cứng.",
                "notes": "Khởi đầu với liều thấp (0.75mg) để giảm buồn nôn, sau đó tăng dần. Bảo quản ở tủ lạnh (2-8°C) trước khi mở. Sau khi mở, có thể bảo quản ở nhiệt độ phòng hoặc tủ lạnh trong tối đa 14 ngày."
            },
            "oral": {
                "reconstitution": "Không có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng tiêm dưới da (SC)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Trulicity (dulaglutide)",
                "UpToDate - Dulaglutide: Drug information",
                "REWIND Study - The Lancet (2019) - Dulaglutide trong đái tháo đường type 2 và bệnh tim mạch",
                "American Diabetes Association guidelines - GLP-1 receptor agonists"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Large RCT (REWIND) showing cardiovascular benefits"
        },
    },
    "Exenatide":     {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Exenatide, Byetta, Bydureon",
        "brand_names": {
            "common": [
                "Byetta (2 lần/ngày)",
                "Bydureon (1 lần/tuần)"
    ],
            "vietnam": [
                "Byetta 5/10mcg"
    ],
        },
        "administration": [
            "SC"
    ],
        "indications": [
            "Đái tháo đường type 2"
    ],
        "dosage": {
            "adult_start": "5mcg SC x 2 lần/ngày (Byetta) hoặc 2mg SC x 1 lần/tuần (Bydureon)",
            "adult_usual": "5-10mcg SC x 2 lần/ngày (Byetta) hoặc 2mg SC x 1 lần/tuần (Bydureon). Tối đa 10mcg x 2 lần/ngày (Byetta) hoặc 2mg/tuần (Bydureon).",
            "adult_max": "10mcg x 2 lần/ngày (Byetta) hoặc 2mg/tuần (Bydureon)",
            "dm_t2_byetta": "Byetta: Khởi đầu 5mcg SC x 2 lần/ngày (trước bữa sáng và tối, trong vòng 60 phút trước bữa ăn), sau 1 tháng tăng lên 10mcg x 2 lần/ngày nếu dung nạp tốt. Tối đa 10mcg x 2 lần/ngày.",
            "dm_t2_bydureon": "Bydureon: 2mg SC x 1 lần/tuần. Không cần tăng liều. Tiêm cùng ngày mỗi tuần, bất kỳ giờ nào trong ngày, không phụ thuộc bữa ăn.",
            "elderly": "Khởi đầu 5mcg SC x 2 lần/ngày (Byetta) hoặc 2mg SC x 1 lần/tuần (Bydureon), tăng dần chậm hơn. Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn nôn, mất nước).",
            "renal_adjustment_dosage": {
                "normal": "5-10mcg SC x 2 lần/ngày (Byetta) hoặc 2mg SC x 1 lần/tuần (Bydureon) (CrCl ≥60)",
                "30_60": "Có thể dùng nhưng thận trọng. Byetta: Khởi đầu 5mcg x 2 lần/ngày, tăng dần chậm. Bydureon: 2mg/tuần. Theo dõi chức năng thận (CrCl 30-60)",
                "under_30": "Thận trọng, có thể cần giảm liều. Byetta: Khởi đầu 5mcg x 2 lần/ngày, tăng dần rất chậm. Bydureon: 2mg/tuần. Theo dõi chức năng thận chặt chẽ (CrCl <30)",
                "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu. Cân nhắc lợi ích/nguy cơ."
            },
            "hepatic_adjustment_dosage": {
                "mild": "5-10mcg SC x 2 lần/ngày (Byetta) hoặc 2mg SC x 1 lần/tuần (Bydureon). Không cần điều chỉnh liều đặc biệt.",
                "moderate": "5-10mcg SC x 2 lần/ngày (Byetta) hoặc 2mg SC x 1 lần/tuần (Bydureon). Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều. Khởi đầu 5mcg x 2 lần/ngày (Byetta) hoặc 2mg/tuần (Bydureon), tăng dần chậm. Theo dõi chức năng gan chặt chẽ."
            },
            "administration_route": "SC (tiêm dưới da)",
            "frequency": "2 lần/ngày (Byetta) hoặc 1 lần/tuần (Bydureon)",
            "with_food": "Byetta: Tiêm trong vòng 60 phút TRƯỚC bữa sáng và tối. Bydureon: Không phụ thuộc bữa ăn, có thể tiêm bất kỳ lúc nào trong ngày.",
            "timing": "Byetta: Tiêm 2 lần/ngày trong vòng 60 phút TRƯỚC bữa sáng và tối (ít tiện lợi hơn các GLP-1 RA khác). Bydureon: Tiêm 1 lần/tuần vào cùng một ngày mỗi tuần, bất kỳ giờ nào trong ngày, không phụ thuộc bữa ăn (tiện lợi hơn Byetta).",
            "titration": "Byetta: Tuần 1-4: 5mcg x 2 lần/ngày. Tuần 5+: 10mcg x 2 lần/ngày (nếu dung nạp tốt). Bydureon: 2mg/tuần, không cần tăng liều. Tăng dần để giảm buồn nôn.",
            "notes": "Byetta: Tiêm 2 lần/ngày (ít tiện lợi hơn các GLP-1 RA khác). Bydureon: 1 lần/tuần (tiện lợi hơn Byetta). GLP-1 RA đầu tiên, ít được dùng hơn do Byetta phải tiêm 2 lần/ngày. Bydureon tiện lợi hơn với liều 1 lần/tuần."
        },
        "side_effects": [
            "Buồn nôn, nôn (Rất phổ biến)",
            "Tiêu chảy",
            "Hạ đường huyết (nếu dùng với SU)",
            "Viêm tụy (Hiếm)"
    ],
        "mechanism_of_action": """GLP-1 RA đầu tiên. Tác dụng tương tự các GLP-1 RA khác nhưng ít được dùng hơn do phải tiêm 2 lần/ngày (Byetta).""",
        "monitoring": [
            "Đường huyết",
            "Dấu hiệu viêm tụy"
    ],
        "contraindications": [
            "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
            "Tiền sử viêm tụy cấp",
            "Đái tháo đường type 1",
            "Nhiễm toan ceton đái tháo đường"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
                "Tiền sử viêm tụy cấp",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng với exenatide hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, có thể cần giảm liều",
                "Suy gan - thận trọng, theo dõi chức năng gan",
                "Bệnh nhân cao tuổi - tăng nguy cơ buồn nôn, mất nước",
                "Bệnh nhân có bệnh dạ dày - tăng nguy cơ buồn nôn, nôn",
                "Phụ nữ có thai - không có dữ liệu đầy đủ về an toàn"
            ]
        },
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "precautions": [
            "Buồn nôn rất phổ biến - Tăng liều từ từ, uống thuốc chống nôn nếu cần",
            "Nguy cơ viêm tụy - Ngừng thuốc nếu nghi ngờ viêm tụy",
            "Nguy cơ ung thư tuyến giáp tủy (MTC) - Chống chỉ định nếu có tiền sử MTC hoặc MEN 2",
            "Giảm liều insulin/sulfonylurea khi bắt đầu dùng",
            "Byetta: Phải tiêm 2 lần/ngày (ít tiện lợi hơn các GLP-1 RA khác)",
            "Bydureon: Tiêm 1 lần/tuần (tiện lợi hơn)"
        ],
        "pharmacokinetics": {
            "half_life": "2.4 giờ (Byetta), 7 ngày (Bydureon)",
            "onset": "1-2 giờ",
            "duration": "6-8 giờ (Byetta - tiêm 2 lần/ngày), 7 ngày (Bydureon - tiêm 1 lần/tuần)",
            "protein_binding": "Không gắn protein đáng kể",
            "metabolism": "Chuyển hóa giống protein (proteolytic degradation)",
            "clearance": "Thận (chủ yếu), chuyển hóa nội bào"
        },
        "storage": "Byetta: Bảo quản ở nhiệt độ 2-8°C (tủ lạnh) trước khi mở. Sau khi mở, có thể bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh trong tối đa 30 ngày. Bydureon: Bảo quản ở nhiệt độ 2-8°C (tủ lạnh) trước khi mở. Sau khi mở, có thể bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh trong tối đa 4 tuần. Tránh đông lạnh. Tránh ánh sáng trực tiếp.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Không khuyến nghị dùng trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Exenatide bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Theo dõi trẻ bú mẹ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Exenatide chuyển hóa giống protein (proteolytic degradation), không phụ thuộc vào chức năng gan. Suy gan nhẹ đến trung bình không cần điều chỉnh liều. Suy gan nặng có thể làm giảm chuyển hóa, tăng nồng độ thuốc."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "Exenatide thải trừ chủ yếu qua thận. Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nghiêm trọng",
                "Tiêu chảy",
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Đau bụng",
                "Viêm tụy cấp (hiếm nhưng nghiêm trọng)",
                "Mất nước do nôn nhiều"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng thuốc, điều chỉnh đường huyết, điều trị viêm tụy nếu có.",
            "treatment": [
                "Ngừng exenatide ngay lập tức",
                "Điều trị hạ đường huyết nếu có: Glucose PO hoặc IV (dextrose 50% 50ml IV)",
                "Điều trị buồn nôn/nôn: Thuốc chống nôn (ondansetron, metoclopramide)",
                "Bù dịch nếu mất nước: Normal saline IV",
                "Điều trị viêm tụy cấp nếu có: Nhịn ăn, bù dịch, giảm đau, theo dõi sát",
                "Theo dõi đường huyết, điện giải, chức năng thận, amylase/lipase nếu nghi ngờ viêm tụy",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Đường huyết, điện giải (Na, K, Cl), chức năng thận (creatinine, eGFR), amylase/lipase (nếu nghi ngờ viêm tụy), dấu hiệu mất nước, dấu hiệu viêm tụy (đau bụng dữ dội, buồn nôn, nôn)"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },
        "administration_instructions": {
            "sc": {
                "injection_sites": "Bụng, đùi, hoặc cánh tay. Luân chuyển vị trí tiêm để tránh kích ứng da.",
                "timing": "Byetta: Tiêm 2 lần/ngày (trước bữa sáng và tối), cách nhau ít nhất 6 giờ. Bydureon: Tiêm 1 lần/tuần vào cùng một ngày mỗi tuần. Có thể tiêm bất kỳ lúc nào trong ngày, không phụ thuộc bữa ăn.",
                "technique": "Tiêm dưới da (subcutaneous). Không tiêm vào tĩnh mạch hoặc cơ. Không tiêm vào vùng da bị kích ứng, đỏ, hoặc cứng.",
                "notes": "Byetta: Khởi đầu với liều thấp (5mcg x 2 lần/ngày) x 1 tháng để giảm buồn nôn, sau đó tăng lên 10mcg x 2 lần/ngày. Bydureon: Tiêm 1 lần/tuần. Bảo quản ở tủ lạnh (2-8°C) trước khi mở."
            },
            "oral": {
                "reconstitution": "Không có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng tiêm dưới da (SC)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Byetta (exenatide), Bydureon (exenatide extended-release)",
                "UpToDate - Exenatide: Drug information",
                "EXSCEL Study - New England Journal of Medicine (2017) - Exenatide trong đái tháo đường type 2 và bệnh tim mạch",
                "American Diabetes Association guidelines - GLP-1 receptor agonists"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Large RCT (EXSCEL) showing cardiovascular benefits"
        },
    },
}
