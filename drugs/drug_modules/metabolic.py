"""
Metabolic and Endocrine Medications
Generated from drug_database_data.py
"""

METABOLIC_DRUGS = {
"Levothyroxine": {
        "group": "Endocrinology - Thyroid Hormone",
        "vietnamese_name": "Levothyroxine, Synthroid, Euthyrox, Thyroxine",
        "administration": ["PO", "IV"],
        "indications": [
            "Suy giáp (hypothyroidism)",
            "Suy giáp bẩm sinh",
            "Bướu cổ (goiter)",
            "Myxedema coma (IV)",
            "Ức chế TSH sau điều trị ung thư tuyến giáp"
        ],
        "contraindications": [
            "Cường giáp không điều trị",
            "Nhồi máu cơ tim cấp",
            "Viêm cơ tim cấp",
            "Dị ứng levothyroxine"
        ],
        "dosage": {
            "adult_start": "25-50mcg x 1 lần/ngày (sáng đói, trước ăn 30-60 phút)",
            "adult_usual": "75-150mcg x 1 lần/ngày",
            "adult_elderly": "Bắt đầu 12.5-25mcg/ngày, tăng dần",
            "adult_cardiac": "Bắt đầu 12.5-25mcg/ngày",
            "adult_myxedema_coma": "200-500mcg IV x 1 lần, sau đó 50-100mcg/ngày",
            "notes": "Uống sáng đói, cách xa thức ăn, thuốc khác ít nhất 30-60 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Dấu hiệu cường giáp (quá liều): tim đập nhanh, lo âu, mất ngủ, đổ mồ hôi",
            "Đau ngực",
            "Nhức đầu",
            "Rối loạn kinh nguyệt",
            "Rụng tóc (tạm thời)",
            "Loạn nhịp tim (quá liều)"
        ],
        "interactions": [
            "Calcium/Sắt/Antacid: giảm hấp thu - cách 4 giờ",
            "Cholestyramine: giảm hấp thu - cách 4 giờ",
            "Warfarin: tăng tác dụng chống đông (điều chỉnh liều warfarin)",
            "Digoxin: có thể cần tăng liều digoxin",
            "Insulin/Oral hypoglycemics: có thể cần điều chỉnh liều",
            "Estrogen: có thể cần tăng liều levothyroxine"
        ],
        "pregnancy": "A - An toàn, cần thiết cho thai kỳ",
        "mechanism_of_action": "Hormone tuyến giáp tổng hợp (T4, thyroxine). Bổ sung hoặc thay thế hormone tuyến giáp thiếu hụt. Trong tế bào, T4 được chuyển đổi thành T3 (triiodothyronine) - dạng hoạt động. T3 gắn với thyroid hormone receptor trong nhân tế bào, điều hòa biểu hiện gen, tăng chuyển hóa cơ bản, tăng nhịp tim, tăng nhiệt độ cơ thể, tăng nhu động ruột, và tăng phát triển tế bào. Được dùng trong suy giáp (hypothyroidism), bướu cổ, và sau phẫu thuật cắt tuyến giáp.",
        "monitoring": [
            "TSH (thyroid stimulating hormone) - mục tiêu: bình thường hóa TSH, kiểm tra mỗi 6-8 tuần khi điều chỉnh liều",
            "Free T4 (FT4) - mục tiêu: trong khoảng bình thường",
            "T3 (nếu cần, trong một số trường hợp)",
            "Nhịp tim và huyết áp (tăng ở quá liều)",
            "Dấu hiệu cường giáp (run, đổ mồ hôi, mất ngủ, nhịp tim nhanh, sụt cân) - dấu hiệu quá liều",
            "Dấu hiệu suy giáp (mệt mỏi, tăng cân, nhịp tim chậm, táo bón, lạnh) - dấu hiệu thiếu liều",
            "Xương (loãng xương nếu quá liều kéo dài)",
            "Tim mạch (rối loạn nhịp tim, đau thắt ngực ở bệnh nhân bệnh mạch vành nếu quá liều)"
        ],
        "precautions": [
            "PHẢI uống vào buổi sáng, khi đói, 30-60 phút trước khi ăn (thức ăn giảm hấp thu 40-60%)",
            "KHÔNG uống cùng với: sắt, canxi, antacid, sucralfate, cholestyramine (cách ít nhất 4 giờ)",
            "Bắt đầu với liều thấp, tăng dần dựa trên TSH",
            "Ở bệnh nhân bệnh mạch vành hoặc người cao tuổi: bắt đầu với liều rất thấp, tăng chậm",
            "Không được ngừng đột ngột (trừ khi có chỉ định)",
            "Liều thay thế: 1.6-1.8 mcg/kg/ngày",
            "TSH mục tiêu: 0.5-2.5 mIU/L (tùy tuổi và tình trạng)",
            "Khi điều chỉnh liều: kiểm tra TSH sau 6-8 tuần (TSH thay đổi chậm)",
            "Quá liều có thể gây cường giáp, rối loạn nhịp tim, đau thắt ngực ở bệnh nhân bệnh mạch vành",
            "Thận trọng ở phụ nữ có thai (nhu cầu tăng 25-50%)",
            "Không dùng để giảm cân (nguy hiểm)"
        ],
        "pharmacokinetics": {
            "half_life": "7 ngày (rất dài)",
            "onset": "3-5 ngày",
            "duration": "Dài (nhiều ngày)",
            "protein_binding": "99.97% (rất cao, gắn với TBG, transthyretin, albumin)",
            "metabolism": "Gan và các mô ngoại vi (deiodination thành T3)",
            "clearance": "Chủ yếu qua gan, một phần qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không được dùng để giảm cân ở bệnh nhân bình giáp. Quá liều có thể gây cường giáp, rối loạn nhịp tim, và đau thắt ngực ở bệnh nhân bệnh mạch vành. Ở bệnh nhân bệnh mạch vành, phải bắt đầu với liều thấp và tăng chậm."
    },
    "Methimazole": {
        "group": "Endocrinology - Antithyroid (Thionamide)",
        "vietnamese_name": "Methimazole, Tapazole",
        "administration": ["PO"],
        "indications": [
            "Cường giáp (hyperthyroidism)",
            "Bệnh Graves",
            "Bướu cổ độc (toxic goiter)",
            "Chuẩn bị trước phẫu thuật tuyến giáp",
            "Điều trị cường giáp trước phóng xạ iod"
        ],
        "contraindications": [
            "Dị ứng methimazole",
            "Có thai (3 tháng đầu - dùng PTU)",
            "Đang cho con bú (ưu tiên PTU)",
            "Giảm bạch cầu nặng"
        ],
        "dosage": {
            "adult_mild": "15-30mg/ngày chia 1-3 lần",
            "adult_moderate": "30-45mg/ngày chia 2-3 lần",
            "adult_severe": "40-60mg/ngày chia 2-3 lần",
            "adult_maintenance": "5-15mg/ngày chia 1-2 lần",
            "notes": "Khởi đầu với liều cao, giảm dần khi đạt bình giáp. Điều trị 12-18 tháng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Giảm bạch cầu, giảm tiểu cầu (nguy hiểm - theo dõi công thức máu)",
            "Phát ban",
            "Ngứa",
            "Đau khớp",
            "Rối loạn vị giác",
            "Độc gan (hiếm nhưng nguy hiểm)",
            "Agranulocytosis (mất bạch cầu - hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "Warfarin: có thể cần giảm liều warfarin (khi đạt bình giáp)",
            "Digoxin: có thể cần giảm liều digoxin"
        ],
        "pregnancy": "D - Tránh trong 3 tháng đầu (dùng PTU). Thận trọng sau đó",
        "mechanism_of_action": "Ức chế enzyme thyroid peroxidase (TPO), ngăn cản quá trình iod hóa tyrosine và ghép nối các iodotyrosine để tạo thành T3 và T4. Methimazole ức chế cả quá trình tổng hợp và giải phóng hormone tuyến giáp, dẫn đến giảm nồng độ T3 và T4 trong máu, giảm triệu chứng cường giáp",
        "monitoring": [
            "Công thức máu toàn phần (CBC) mỗi tuần trong 3 tháng đầu, sau đó mỗi tháng (theo dõi agranulocytosis)",
            "Chức năng gan (ALT, AST, bilirubin) mỗi 1-2 tháng",
            "TSH, FT3, FT4 mỗi 4-6 tuần khi điều chỉnh liều, sau đó mỗi 3-6 tháng",
            "Dấu hiệu nhiễm trùng (sốt, viêm họng - có thể là dấu hiệu agranulocytosis)",
            "Dấu hiệu độc gan (vàng da, mệt mỏi, đau bụng)"
        ],
        "precautions": [
            "Khởi đầu với liều cao (30-60mg/ngày), giảm dần khi đạt bình giáp",
            "Ngừng ngay nếu có sốt, viêm họng (dấu hiệu agranulocytosis - cấp cứu)",
            "Ngừng ngay nếu có dấu hiệu độc gan (vàng da, tăng ALT/AST)",
            "Tránh dùng trong 3 tháng đầu thai kỳ (dùng PTU thay thế)",
            "Có thể dùng trong cho con bú nhưng ưu tiên PTU",
            "Theo dõi sát công thức máu, đặc biệt trong 3 tháng đầu",
            "Có thể gây dị tật thai nhi nếu dùng trong thai kỳ (teratogenic)"
        ],
        "pharmacokinetics": {
            "half_life": "4-6 giờ (ngắn)",
            "onset": "1-2 tuần (giảm T3/T4)",
            "duration": "12-24 giờ (tác dụng kéo dài do tích lũy trong tuyến giáp)",
            "protein_binding": "Minimal",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây agranulocytosis (mất bạch cầu) - nguy hiểm tính mạng. Bệnh nhân cần được hướng dẫn ngừng thuốc và đến bệnh viện ngay nếu có sốt, viêm họng. Có thể gây dị tật thai nhi nếu dùng trong thai kỳ"
    },
    "Propylthiouracil": {
        "group": "Endocrinology - Antithyroid (Thionamide)",
        "vietnamese_name": "Propylthiouracil, PTU",
        "administration": ["PO"],
        "indications": [
            "Cường giáp (hyperthyroidism)",
            "Bệnh Graves",
            "Bướu cổ độc",
            "Có thai (3 tháng đầu - ưu tiên hơn methimazole)",
            "Cường giáp cấp (thyroid storm)"
        ],
        "contraindications": [
            "Dị ứng propylthiouracil",
            "Giảm bạch cầu nặng",
            "Đang cho con bú (có thể dùng)"
        ],
        "dosage": {
            "adult_mild": "100-150mg x 3 lần/ngày",
            "adult_moderate": "150-200mg x 3 lần/ngày",
            "adult_severe": "200-300mg x 3-4 lần/ngày",
            "adult_storm": "200-300mg x 4 lần/ngày",
            "adult_maintenance": "50-150mg/ngày chia 1-3 lần",
            "notes": "Ưu tiên hơn methimazole trong 3 tháng đầu thai kỳ. Nhiều tác dụng phụ gan hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Độc gan (cao hơn methimazole, có thể suy gan cấp)",
            "Giảm bạch cầu, agranulocytosis",
            "Phát ban",
            "Ngứa",
            "Đau khớp",
            "Vasculitis (hiếm)",
            "Lupus-like syndrome (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể cần giảm liều warfarin",
            "Digoxin: có thể cần giảm liều digoxin"
        ],
        "pregnancy": "D - An toàn hơn methimazole trong 3 tháng đầu, nhưng vẫn thận trọng",
        "mechanism_of_action": "Ức chế enzyme thyroid peroxidase (TPO), ngăn cản quá trình iod hóa tyrosine và ghép nối các iodotyrosine để tạo thành T3 và T4. Propylthiouracil còn ức chế chuyển đổi T4 thành T3 ở mô ngoại vi (ức chế 5'-deiodinase), giảm nhanh T3 hơn so với methimazole. Dẫn đến giảm nồng độ T3 và T4, giảm triệu chứng cường giáp",
        "monitoring": [
            "Công thức máu toàn phần (CBC) mỗi tuần trong 3 tháng đầu, sau đó mỗi tháng (theo dõi agranulocytosis)",
            "Chức năng gan (ALT, AST, bilirubin) mỗi 1-2 tháng (nguy cơ độc gan cao hơn methimazole)",
            "TSH, FT3, FT4 mỗi 4-6 tuần khi điều chỉnh liều, sau đó mỗi 3-6 tháng",
            "Dấu hiệu nhiễm trùng (sốt, viêm họng - có thể là dấu hiệu agranulocytosis)",
            "Dấu hiệu độc gan (vàng da, mệt mỏi, đau bụng, suy gan cấp)",
            "Dấu hiệu vasculitis (phát ban, đau khớp, tổn thương da)"
        ],
        "precautions": [
            "Khởi đầu với liều cao (600-900mg/ngày chia 3-4 lần), giảm dần khi đạt bình giáp",
            "Ngừng ngay nếu có sốt, viêm họng (dấu hiệu agranulocytosis - cấp cứu)",
            "Ngừng ngay nếu có dấu hiệu độc gan (vàng da, tăng ALT/AST, suy gan cấp)",
            "Ưu tiên hơn methimazole trong 3 tháng đầu thai kỳ (ít nguy cơ dị tật hơn)",
            "Có thể dùng trong cho con bú (an toàn hơn methimazole)",
            "Theo dõi sát chức năng gan (nguy cơ độc gan cao hơn methimazole)",
            "Cần dùng nhiều lần/ngày (3-4 lần) do thời gian bán thải ngắn",
            "Có thể gây vasculitis và lupus-like syndrome (hiếm)"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (rất ngắn)",
            "onset": "1-2 tuần (giảm T3/T4)",
            "duration": "6-8 giờ (ngắn hơn methimazole)",
            "protein_binding": "Minimal",
            "clearance": "Gan (chuyển hóa chủ yếu), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây suy gan cấp nặng và tử vong. Theo dõi sát chức năng gan và ngừng ngay nếu có dấu hiệu độc gan. Có thể gây agranulocytosis (mất bạch cầu) - nguy hiểm tính mạng"
    },
    "Prednisone": {
        "group": "Endocrinology - Corticosteroid (Glucocorticoid)",
        "vietnamese_name": "Prednisone, Deltasone",
        "administration": ["PO"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản nặng",
            "COPD đợt cấp",
            "Lupus ban đỏ hệ thống",
            "Viêm mạch máu",
            "Bệnh viêm ruột",
            "Dị ứng nặng",
            "Ung thư (kết hợp hóa trị)",
            "Ức chế miễn dịch",
            "Suy thượng thận"
        ],
        "contraindications": [
            "Nhiễm trùng nặng chưa điều trị",
            "Nhiễm nấm hệ thống",
            "Loét dạ dày tá tràng đang hoạt động",
            "Suy tim nặng",
            "Tăng huyết áp không kiểm soát"
        ],
        "dosage": {
            "adult_antiinflammatory": "5-60mg/ngày chia 1-4 lần",
            "adult_immunosuppression": "1-2mg/kg/ngày",
            "adult_asthma_exacerbation": "40-60mg/ngày x 5-7 ngày",
            "adult_copd_exacerbation": "30-40mg/ngày x 10-14 ngày",
            "adult_rheumatoid": "5-10mg/ngày",
            "adult_adrenal_insufficiency": "5-7.5mg/ngày",
            "notes": "Giảm liều dần dần khi ngừng (tránh suy thượng thận). Uống với thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Hoại tử xương",
            "Loét dạ dày",
            "Tăng cân",
            "Giữ nước",
            "Yếu cơ",
            "Ức chế miễn dịch (tăng nguy cơ nhiễm trùng)",
            "Ức chế trục hạ đồi-tuyến yên-thượng thận",
            "Đục thủy tinh thể",
            "Tăng nhãn áp"
        ],
        "interactions": [
            "Warfarin: tăng/giảm tác dụng chống đông (thay đổi)",
            "Insulin/Oral hypoglycemics: tăng đường huyết - cần điều chỉnh",
            "Thuốc hạ huyết áp: giảm hiệu quả",
            "Diuretics: tăng mất kali",
            "NSAID: tăng nguy cơ loét dạ dày",
            "Vaccine sống: chống chỉ định",
            "Rifampin: giảm nồng độ prednisone"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Prednisone là corticosteroid tổng hợp, chuyển hóa thành prednisolone (hoạt chất) trong gan. Gắn với thụ thể glucocorticoid trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, TNF-α, prostaglandin), giảm di chuyển bạch cầu đến vị trí viêm, ức chế chức năng miễn dịch",
        "monitoring": [
            "Đường huyết (corticosteroid gây tăng đường huyết)",
            "Huyết áp (có thể tăng huyết áp)",
            "Điện giải: K+, Na+ (mất kali, giữ natri)",
            "Cân nặng (giữ nước, tăng cân)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Dấu hiệu loét dạ dày (đau bụng, phân đen)",
            "Mật độ xương nếu dùng lâu dài (loãng xương)",
            "Chức năng thượng thận nếu dùng lâu dài (ACTH, cortisol)",
            "Mắt: đục thủy tinh thể, tăng nhãn áp"
        ],
        "precautions": [
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "GIẢM LIỀU DẦN DẦN khi ngừng (tránh suy thượng thận cấp) - không được ngừng đột ngột",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Bổ sung canxi, vitamin D nếu dùng lâu dài (phòng loãng xương)",
            "Cân nhắc bổ sung kali nếu dùng lâu dài",
            "Tránh vaccine sống khi đang dùng corticosteroid",
            "Tăng liều trong stress (phẫu thuật, nhiễm trùng nặng)",
            "Giảm liều khi có nhiễm trùng (nếu có thể)",
            "Theo dõi đường huyết ở bệnh nhân đái tháo đường",
            "Dạy bệnh nhân không tự ý ngừng thuốc"
        ],
        "pharmacokinetics": {
            "half_life": "Prednisone: 3-4 giờ; Prednisolone (active): 2-3 giờ",
            "onset": "1-2 giờ",
            "duration": "18-36 giờ (tác dụng sinh học kéo dài hơn half-life)",
            "protein_binding": "70-90% (prednisolone)",
            "clearance": "Gan (chuyển hóa prednisone → prednisolone), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Không ngừng đột ngột sau khi dùng lâu dài - có thể gây suy thượng thận cấp đe dọa tính mạng. Corticosteroid có thể gây ức chế miễn dịch, tăng nguy cơ nhiễm trùng nặng, và che dấu triệu chứng nhiễm trùng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ketoconazole, Itraconazole (Azole antifungals)",
                    "mechanism": "Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa prednisone → prednisolone, tăng nồng độ và tác dụng.",
                    "effect": "Tăng nồng độ prednisolone (active metabolite), tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)",
                    "management": "Giảm liều prednisone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing."
                },
                {
                    "drug": "Rifampin, Rifabutin",
                    "mechanism": "Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa prednisone → prednisolone, nhưng có thể giảm hiệu quả.",
                    "effect": "Có thể giảm nồng độ prednisolone, giảm hiệu quả điều trị",
                    "management": "Tăng liều prednisone 25-50% khi dùng với rifampin. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.",
                    "effect": "Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng prednisone. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAID (Ibuprofen, Naproxen, Diclofenac)",
                    "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.",
                    "effect": "Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng",
                    "management": "Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày."
                },
                {
                    "drug": "Phenytoin, Phenobarbital, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa, tăng chuyển hóa prednisone → prednisolone.",
                    "effect": "Có thể giảm nồng độ prednisolone, giảm hiệu quả",
                    "management": "Tăng liều prednisone. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.",
                    "effect": "Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính",
                    "management": "Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng."
                }
            ],
            "minor": [
                {
                    "drug": "Diuretics (Thiazide, Furosemide)",
                    "mechanism": "Corticosteroid gây giữ natri, có thể đối kháng tác dụng lợi tiểu.",
                    "effect": "Giảm hiệu quả lợi tiểu, có thể gây giữ nước",
                    "management": "Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm",
                "Dị ứng prednisone hoặc các corticosteroid khác",
                "Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt"
            ],
            "relative": [
                "Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng",
                "Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh",
                "Tăng huyết áp - có thể tăng huyết áp, giữ nước",
                "Suy tim - giữ nước, có thể làm nặng",
                "Loãng xương - tăng nguy cơ gãy xương",
                "Loét dạ dày tá tràng - tăng nguy cơ loét",
                "Rối loạn tâm thần - có thể làm nặng",
                "Glaucoma - có thể tăng nhãn áp",
                "Có thai - có thể ảnh hưởng đến thai nhi",
                "Suy gan - prednisone cần chuyển hóa ở gan thành prednisolone, có thể giảm hiệu quả ở suy gan nặng",
                "Suy thận - không cần điều chỉnh liều nhưng thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Prednisone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, prednisone được sử dụng trong thai kỳ để điều trị một số bệnh tự miễn và hen phế quản. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Tránh dùng liều cao kéo dài trong thai kỳ nếu có thể.",
            "lactation": {
                "safety": "Compatible (với dùng ngắn hạn)",
                "details": "Prednisone và prednisolone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thường dùng. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Prednisone chuyển hóa qua gan thành prednisolone (dạng hoạt động).",
            "moderate": "Thận trọng, có thể cần tăng liều nhẹ hoặc dùng prednisolone thay thế. Chuyển hóa có thể giảm ở suy gan trung bình, giảm chuyển đổi prednisone → prednisolone.",
            "severe": "Thận trọng, nên dùng prednisolone thay vì prednisone. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, giảm chuyển đổi prednisone → prednisolone, giảm hiệu quả.",
            "notes": "Prednisone cần chuyển hóa ở gan thành prednisolone (dạng hoạt động). Suy gan có thể làm giảm chuyển hóa, giảm hiệu quả. Ở bệnh nhân suy gan nặng, nên dùng prednisolone (dạng hoạt động) thay vì prednisone."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp",
                "Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu",
                "Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày",
                "Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê",
                "Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng",
                "Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng",
                "Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài), sốc, tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay prednisone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần - phải giảm dần)",
                "Nếu ngừng đột ngột sau dùng lâu dài:",
                "  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)",
                "  - Giảm dần liều theo thời gian",
                "Điều trị tăng đường huyết:",
                "  - Theo dõi đường huyết thường xuyên",
                "  - Insulin nếu cần",
                "  - Điều chỉnh liều đái tháo đường",
                "Điều trị loét dạ dày/xuất huyết tiêu hóa:",
                "  - PPI (omeprazole, pantoprazole)",
                "  - Truyền máu nếu cần",
                "  - Nội soi dạ dày nếu nghi ngờ thủng",
                "Điều trị rối loạn tâm thần:",
                "  - An thần nếu kích động, loạn thần",
                "  - Antipsychotic nếu cần",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị nhiễm trùng:",
                "  - Kháng sinh nếu có nhiễm trùng",
                "  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)",
                "Điều chỉnh điện giải:",
                "  - Bổ sung kali nếu hạ kali máu",
                "  - Điều chỉnh natri nếu cần",
                "Hỗ trợ huyết động:",
                "  - Truyền dịch nếu cần",
                "  - Thuốc vận mạch nếu sốc",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết"
            ],
            "monitoring": "Theo dõi đường huyết, điện giải, dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.",
                "timing": "Uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày. Với liều cao, chia nhiều lần. Với liều thấp, có thể uống 1 lần buổi sáng."
            },
            "iv": {
                "reconstitution": "Prednisone chủ yếu dùng đường uống. Nếu cần IV, có thể dùng methylprednisolone hoặc hydrocortisone thay thế.",
                "infusion_rate": "N/A - chủ yếu dùng đường uống",
                "compatibility": ["N/A"],
                "incompatibility": ["N/A"],
                "notes": "Prednisone chủ yếu dùng đường uống. Nếu cần dùng IV, cân nhắc dùng methylprednisolone hoặc hydrocortisone thay thế."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Prednisone (Deltasone)",
                "UpToDate - Prednisone: Drug Information",
                "Medscape - Prednisone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Prednisone Monograph",
                "Micromedex - Prednisone Drug Information",
                "Endocrine Society Guidelines - Corticosteroid Use"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
}

__all__ = ['METABOLIC_DRUGS']
