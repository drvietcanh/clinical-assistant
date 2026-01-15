"""
Osteoporosis Drugs (Thuốc loãng xương)
"""

OSTEOPOROSIS_DRUGS = {
    "Alendronate":     {
        "group": "Rheumatology - Bisphosphonate (Oral)",
        "vietnamese_name": "Alendronate, Fosamax",
        "brand_names": {
            "common": [
                "Fosamax",
                "Binosto"
            ],
            "vietnam": [
                "Fosamax 10mg",
                "Fosamax 70mg",
                "Alendronate Stada",
                "SaVi Alendronate",
                "Alenta"
            ],
        },
        "manufacturer": {
            "primary": "Merck & Co., Inc. (Fosamax)",
            "vietnam": [
                "Merck & Co., Inc.",
                "Công ty Cổ phần Dược phẩm SaVi (SaVi Alendronate)",
                "Getz Pharma (Alenta)",
                "Stada (Alendronate Stada)",
                "Các công ty dược phẩm Việt Nam (generic)"
            ],
            "notes": "Merck & Co., Inc. là nhà sản xuất gốc của Fosamax (alendronate). Có nhiều sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Điều trị loãng xương ở phụ nữ sau mãn kinh",
            "Điều trị loãng xương ở nam giới",
            "Phòng ngừa loãng xương do sử dụng glucocorticoid",
            "Điều trị bệnh Paget xương"
        ],
        "contraindications": [
            "Dị ứng với alendronate hoặc bất kỳ thành phần nào của thuốc",
            "Bất thường thực quản (hẹp, không giãn, không đàn hồi)",
            "Không thể đứng hoặc ngồi thẳng trong ít nhất 30 phút",
            "Hạ calci máu (chưa được điều chỉnh)",
            "Suy thận nặng (CrCl < 35 ml/phút)",
            "Phụ nữ có thai và cho con bú",
            "Trẻ em"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với alendronate hoặc bất kỳ thành phần nào của thuốc",
                "Bất thường thực quản (hẹp, không giãn, không đàn hồi)",
                "Không thể đứng hoặc ngồi thẳng trong ít nhất 30 phút",
                "Hạ calci máu (chưa được điều chỉnh)",
                "Suy thận nặng (CrCl < 35 ml/phút)",
                "Phụ nữ có thai và cho con bú",
                "Trẻ em"
            ],
            "tương_đối": [
                "Bệnh đường tiêu hóa trên (khó nuốt, viêm dạ dày, viêm tá tràng, loét) - thận trọng",
                "Suy thận trung bình (CrCl 35-60 ml/phút) - không cần chỉnh liều nhưng thận trọng",
                "Thiếu vitamin D - phải bổ sung trước khi dùng alendronate"
            ]
        },
        "dosage": {
            "adult_osteoporosis_postmenopausal": "10mg uống mỗi ngày 1 lần HOẶC 70mg uống mỗi tuần 1 lần",
            "adult_osteoporosis_male": "10mg uống mỗi ngày 1 lần HOẶC 70mg uống mỗi tuần 1 lần",
            "adult_osteoporosis_prevention_glucocorticoid": "5mg uống mỗi ngày 1 lần (phụ nữ sau mãn kinh không dùng estrogen: 10mg/ngày)",
            "adult_paget_disease": "40mg uống mỗi ngày 1 lần trong 6 tháng",
            "renal_adjustment_crcl_35_60": "Không cần chỉnh liều (CrCl 35-60 ml/phút)",
            "renal_adjustment_crcl_under_35": "CHỐNG CHỈ ĐỊNH (CrCl < 35 ml/phút)",
            "notes": "PHẢI uống vào buổi sáng, bụng đói, ít nhất 30 phút trước khi ăn, uống hoặc dùng thuốc khác. Uống với 1 ly nước đầy (180-240ml nước lọc). Không uống với nước khoáng, nước cam, cà phê, trà, nước hoa quả (làm giảm hấp thu). Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống để tránh loét thực quản. Không nằm trong 30 phút sau uống và cho đến sau bữa ăn đầu tiên trong ngày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/phút)",
            "35_60": "Không cần chỉnh liều (CrCl 35-60 ml/phút)",
            "under_35": "CHỐNG CHỈ ĐỊNH - không dùng (CrCl < 35 ml/phút)",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Alendronate thải trừ qua thận. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl < 35 ml/phút)."
        },
        "side_effects": [
            "Đau bụng, loét dạ dày, đầy hơi, táo bón, tiêu chảy (thường gặp)",
            "Kích ứng thực quản, loét thực quản, viêm dạ dày (nghiêm trọng - Black Box Warning)",
            "Nhức đầu, hoa mắt, chóng mặt",
            "Phát ban, rối loạn vị giác",
            "Hạ calci máu",
            "Hoại tử xương hàm (Osteonecrosis of the jaw - ONJ) - hiếm gặp, thường ở liều cao hoặc ung thư (Black Box Warning)",
            "Gãy xương đùi không điển hình (dùng lâu dài) - Black Box Warning",
            "Rụng tóc (hiếm)",
            "Suy gan, suy thận (hiếm)"
        ],
        "mechanism_of_action": "Alendronate là bisphosphonate thế hệ 2, ức chế hủy xương bằng cách gắn vào hydroxyapatite trong xương và ức chế enzyme farnesyl pyrophosphate synthase (FPPS) trong tế bào hủy xương (osteoclast). Bằng cách ức chế FPPS, alendronate làm giảm hoạt động và gây apoptosis của tế bào hủy xương, dẫn đến giảm hủy xương và tăng mật độ xương. Alendronate có ái lực cao với xương, gắn mạnh vào hydroxyapatite, và có thời gian bán thải rất dài trong xương (hơn 10 năm).",
        "monitoring": [
            "Mật độ xương (DEXA scan) - trước điều trị và sau 1-2 năm",
            "Calci máu, Vitamin D - trước và trong điều trị (phải bổ sung nếu thiếu)",
            "Chức năng thận (CrCl) - trước và trong điều trị (CHỐNG CHỈ ĐỊNH nếu CrCl <35 ml/phút)",
            "Dấu hiệu kích ứng thực quản (đau ngực, khó nuốt, nuốt đau) - Black Box Warning",
            "Dấu hiệu hoại tử xương hàm (ONJ) - đau hàm, sưng, răng lung lay, lộ xương - Black Box Warning",
            "Dấu hiệu gãy xương đùi không điển hình - đau đùi, háng - Black Box Warning",
            "Triệu chứng tiêu hóa (đau bụng, loét dạ dày)"
        ],
        "interactions": [
            "Calcium, sắt, antacids, multivitamins có calcium/sắt: giảm hấp thu alendronate - dùng cách xa ít nhất 30 phút",
            "NSAIDs: tăng nguy cơ kích ứng dạ dày, loét dạ dày",
            "Aspirin: tăng nguy cơ kích ứng dạ dày",
            "Nước khoáng, nước cam, cà phê, trà: làm giảm hấp thu alendronate - không uống với các loại nước này"
        ],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "precautions": [
            "QUAN TRỌNG: Uống lúc đói, ít nhất 30 phút trước ăn hoặc uống thuốc khác",
            "Uống với nước lọc (≥200ml), không uống với nước khoáng, cà phê, trà, nước hoa quả",
            "Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống để tránh kích ứng thực quản",
            "Không nằm ngay sau khi uống",
            "Dùng cách xa calcium, sắt, antacids ít nhất 30 phút",
            "Nguy cơ hoại tử xương hàm: đánh giá răng miệng trước điều trị, tránh phẫu thuật răng trong khi dùng",
            "Nguy cơ gãy xương đùi không điển hình: theo dõi đau đùi, háng",
            "Không dùng nếu CrCl <35 ml/min"
        ],
        "pharmacokinetics": {
            "half_life": "Hơn 10 năm (trong xương), ~10 giờ (trong máu)",
            "onset": "Giảm markers hủy xương trong 1-3 tháng, tăng mật độ xương trong 6-12 tháng",
            "duration": "Tác dụng kéo dài nhiều năm sau khi ngừng (do gắn vào xương)",
            "protein_binding": "~78% (gắn với xương)",
            "clearance": "Gắn vào xương (50%), thải qua thận (50%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Hoại tử xương hàm (ONJ): có thể xảy ra, đặc biệt ở bệnh nhân phẫu thuật răng, ung thư, dùng corticosteroid. Đánh giá răng miệng trước điều trị. Gãy xương đùi không điển hình: tăng nguy cơ gãy xương đùi không điển hình.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium, Sắt, Antacids, Multivitamins có calcium/sắt",
                    "mechanism": "Tạo phức hợp không hòa tan với alendronate, giảm hấp thu",
                    "effect": "Giảm hấp thu alendronate, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 30 phút. Uống alendronate trước, sau đó mới uống calcium/sắt."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Cả hai đều có thể gây kích ứng dạ dày",
                    "effect": "Tăng nguy cơ kích ứng dạ dày, loét dạ dày",
                    "management": "Thận trọng. Có thể cần dùng PPI hoặc H2 blocker."
                }
            ],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Có thể ảnh hưởng đến phát triển xương thai nhi.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều (không chuyển hóa qua gan)",
            "notes": "Alendronate không chuyển hóa qua gan, thải qua thận"
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng thực quản nặng, đau ngực, khó nuốt",
                "Hạ calci máu",
                "Đau bụng, buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Uống sữa hoặc antacid để che phủ thực quản",
                "Không gây nôn (có thể làm tổn thương thực quản thêm)",
                "Điều trị hạ calci máu: calcium IV nếu cần",
                "Theo dõi tại bệnh viện"
            ],
            "monitoring": "Calci máu, dấu hiệu kích ứng thực quản, dấu hiệu sinh tồn"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống lúc đói, ít nhất 30 phút trước ăn hoặc uống thuốc khác",
                "timing": "Uống vào buổi sáng, lúc đói, với nước lọc (≥200ml). Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống",
                "notes": "QUAN TRỌNG: Uống với nước lọc, không uống với nước khoáng, cà phê, trà, nước hoa quả. Đứng hoặc ngồi thẳng ít nhất 30 phút sau khi uống."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fosamax (alendronate)",
                "FIT Study - Fracture Intervention Trial",
                "NOF Guidelines - Osteoporosis Treatment 2024",
                "UpToDate - Alendronate: Drug information",
                "ASBMR Guidelines - Bisphosphonate Use",
                "Nhà thuốc An Khang - Alendronate",
                "MIMS Vietnam - Alendronate",
                "Thuốc Biết Dược - Alendronate"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High – FDA-approved, large RCTs (FIT Study)"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["gastrointestinal", "skeletal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Esophageal symptoms (Black Box Warning - esophageal ulceration)", "Bone density (DEXA scan)", "Calcium, Vitamin D", "Renal function", "ONJ signs (osteonecrosis of jaw - rare)", "Atypical femur fractures (long-term use)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Esophageal Ulceration",
            "FDA Black Box Warning - Osteonecrosis of Jaw (ONJ)",
            "FDA Black Box Warning - Atypical Femur Fractures (long-term use)",
            "ACR Guidelines - Osteoporosis",
            "WHO Essential Medicines List"
        ],
    },
    "Zoledronic Acid":     {
        "group": "Rheumatology - Bisphosphonate (IV)",
        "vietnamese_name": "Zoledronic Acid, Aclasta, Zometa",
        "brand_names": {
            "common": [
                "Reclast",
                "Zometa",
                "Aclasta"
            ],
            "vietnam": [
                "Aclasta 5mg/100ml",
                "Zometa 4mg (cho ung thư)",
                "Reclast 5mg",
                "Natzold (Zoledronic Acid)",
                "Zoledronic Acid 4mg",
                "Zoledronic Acid 5mg"
            ],
        },
        "manufacturer": {
            "primary": "Novartis Pharmaceuticals Corporation",
            "vietnam": [
                "Novartis Pharma",
                "Các công ty dược phẩm Việt Nam (generic - Natzold, v.v.)"
            ],
            "notes": "Novartis là nhà sản xuất gốc của Aclasta, Reclast và Zometa. Có các sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "IV (Truyền tĩnh mạch)"
        ],
        "indications": [
            "Loãng xương ở phụ nữ mãn kinh (Aclasta/Reclast - 5mg mỗi năm)",
            "Loãng xương ở nam giới (Aclasta/Reclast - 5mg mỗi năm)",
            "Loãng xương do corticosteroid (Aclasta/Reclast - 5mg mỗi năm)",
            "Dự phòng loãng xương sau mãn kinh (Aclasta/Reclast - 5mg cách 2 năm/lần)",
            "Bệnh Paget xương (Aclasta/Reclast - 5mg x 1 lần)",
            "Tăng calci máu do ung thư (Zometa - 4mg)",
            "Ung thư di căn xương (Zometa - 4mg mỗi 3-4 tuần)",
            "Đa u tủy xương (Multiple Myeloma) (Zometa - 4mg mỗi 3-4 tuần)"
        ],
        "dosage": {
            "adult_osteoporosis_postmenopausal": "5mg IV truyền tĩnh mạch (ít nhất 15 phút) mỗi 1 năm/lần (Aclasta/Reclast)",
            "adult_osteoporosis_male": "5mg IV truyền tĩnh mạch (ít nhất 15 phút) mỗi 1 năm/lần (Aclasta/Reclast)",
            "adult_osteoporosis_corticosteroid": "5mg IV truyền tĩnh mạch (ít nhất 15 phút) mỗi 1 năm/lần (Aclasta/Reclast)",
            "adult_osteoporosis_prevention": "5mg IV truyền tĩnh mạch (ít nhất 15 phút) cách 2 năm/lần (Aclasta/Reclast)",
            "adult_paget_disease": "5mg IV truyền tĩnh mạch (ít nhất 15 phút) x 1 lần (Aclasta/Reclast). Bổ sung calci 1.5g/ngày (750mg x 2 lần hoặc 500mg x 3 lần) và vitamin D 800 IU/ngày, đặc biệt trong 2 tuần đầu",
            "adult_hypercalcemia_cancer": "4mg IV truyền tĩnh mạch (ít nhất 15 phút) x 1 lần (Zometa). Có thể lặp lại sau ít nhất 7 ngày nếu cần",
            "adult_cancer_bone_metastases": "4mg IV truyền tĩnh mạch (ít nhất 15 phút) mỗi 3-4 tuần (Zometa)",
            "adult_multiple_myeloma": "4mg IV truyền tĩnh mạch (ít nhất 15 phút) mỗi 3-4 tuần (Zometa)",
            "renal_adjustment_crcl_50_60": "3.5mg IV (nếu CrCl 50-60 ml/min) - giảm liều và kéo dài thời gian truyền",
            "renal_adjustment_crcl_40_49": "3.3mg IV (nếu CrCl 40-49 ml/min) - giảm liều và kéo dài thời gian truyền",
            "renal_adjustment_crcl_30_39": "3mg IV (nếu CrCl 30-39 ml/min) - giảm liều và kéo dài thời gian truyền",
            "renal_adjustment_crcl_under_30": "Không khuyến cáo sử dụng (CrCl <30 ml/min)",
            "notes": "Bệnh nhân phải được bù đủ nước trước khi truyền (uống ít nhất 1-2 ly nước trước truyền). Truyền CHẬM tối thiểu 15 phút, không được truyền nhanh hơn. Cần bổ sung calci (500mg/ngày) và vitamin D (400 IU/ngày) trong suốt quá trình điều trị, trừ khi có chống chỉ định. Hội chứng giả cúm (sốt, đau cơ, đau khớp) rất thường gặp sau liều đầu, thường tự hết trong 24-48 giờ, có thể dùng acetaminophen để giảm triệu chứng."
        },
        "side_effects": [
            "Sốt, ớn lạnh, đau cơ, đau khớp, đau lưng (Hội chứng giả cúm - rất thường gặp sau liều đầu, thường tự hết trong 24-48 giờ)",
            "Đau đầu, mệt mỏi",
            "Buồn nôn, nôn, tiêu chảy",
            "Hạ calci máu, hạ phospho máu, hạ magie máu (có thể nghiêm trọng)",
            "Suy thận cấp (đặc biệt nếu truyền nhanh, mất nước hoặc phối hợp thuốc độc thận)",
            "Hoại tử xương hàm (osteonecrosis of the jaw - ONJ) - đặc biệt ở bệnh nhân ung thư, phẫu thuật răng",
            "Gãy xương đùi không điển hình (dùng kéo dài) - hiếm",
            "Rối loạn nhịp tim (atrial fibrillation) - hiếm",
            "Phản ứng da nghiêm trọng (hiếm)"
        ],
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "50_60": "3.5mg IV (CrCl 50-60 ml/min) - giảm liều và kéo dài thời gian truyền",
            "40_49": "3.3mg IV (CrCl 40-49 ml/min) - giảm liều và kéo dài thời gian truyền",
            "30_39": "3mg IV (CrCl 30-39 ml/min) - giảm liều và kéo dài thời gian truyền",
            "under_30": "Không khuyến cáo sử dụng (CrCl <30 ml/min)",
            "under_35_reclast": "Chống chỉ định cho chỉ định loãng xương (CrCl <35 ml/min cho Reclast/Aclasta)",
            "under_30_zometa": "Chống chỉ định cho chỉ định ung thư (CrCl <30 ml/min cho Zometa)",
            "notes": "Nguy cơ suy thận tăng nếu mất nước, truyền nhanh hoặc phối hợp thuốc độc thận. Phải kiểm tra creatinine và eGFR trước mỗi lần truyền. Ngừng điều trị nếu CrCl giảm."
        },
        "monitoring": [
            "Creatinine trước mỗi lần truyền và sau 24-48 giờ nếu nguy cơ cao",
            "Calci, phospho, magnesium máu (nguy cơ hạ calci/phospho)",
            "Dấu hiệu hoại tử xương hàm (đau hàm, răng lung lay, lộ xương)",
            "Dấu hiệu gãy xương đùi không điển hình (đau đùi/háng)",
            "Triệu chứng hội chứng giả cúm sau truyền"
        ],
        "contraindications": [
            "Dị ứng với zoledronic acid hoặc các bisphosphonates khác",
            "Hạ calci máu chưa được điều chỉnh",
            "Suy thận nặng (CrCl <35 ml/min cho Reclast/Aclasta, CrCl <30 ml/min cho Zometa)",
            "Mất nước nặng",
            "Phụ nữ có thai (Category D)",
            "Trẻ em và thanh thiếu niên dưới 18 tuổi"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với zoledronic acid hoặc các bisphosphonates khác",
                "Hạ calci máu chưa được điều chỉnh",
                "Suy thận nặng (CrCl <35 ml/min cho Reclast/Aclasta chỉ định loãng xương, CrCl <30 ml/min cho Zometa chỉ định ung thư)",
                "Mất nước nặng",
                "Phụ nữ có thai (Category D)",
                "Trẻ em và thanh thiếu niên dưới 18 tuổi"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60 ml/min) - thận trọng, giảm liều và kéo dài thời gian truyền",
                "Phẫu thuật răng gần đây hoặc dự kiến - tăng nguy cơ ONJ, trì hoãn điều trị nếu có thể",
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp tim (atrial fibrillation)",
                "Bệnh nhân ung thư đang điều trị - tăng nguy cơ ONJ và suy thận"
            ]
        },
        "interactions": [
            "Aminoglycosides: tăng nguy cơ hạ calci máu",
            "Loop diuretics: tăng nguy cơ hạ calci máu",
            "NSAID/thuốc độc thận (vancomycin, platinum): tăng nguy cơ suy thận"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH trong thai kỳ",
        "mechanism_of_action": "Bisphosphonate thế hệ 3. Ức chế hủy xương bằng cách ức chế enzyme farnesyl pyrophosphate synthase trong tế bào hủy xương (osteoclast), gây apoptosis hủy cốt bào, giảm hủy xương → tăng mật độ xương, giảm calci máu.",
        "precautions": [
            "QUAN TRỌNG: Bù đủ nước trước và sau truyền (bệnh nhân nên uống ít nhất 1-2 ly nước trước truyền); kiểm tra creatinine và eGFR trước mỗi liều",
            "QUAN TRỌNG: BẮT BUỘC truyền ít nhất 15 phút, không được truyền nhanh hơn - nguy cơ suy thận cấp nếu truyền nhanh",
            "Bổ sung calci (500mg/ngày) và vitamin D (400 IU/ngày) trong suốt quá trình điều trị, trừ khi có chống chỉ định",
            "Đối với bệnh Paget xương: bổ sung calci 1.5g/ngày (750mg x 2 lần hoặc 500mg x 3 lần) và vitamin D 800 IU/ngày, đặc biệt trong 2 tuần đầu",
            "Khám nha khoa trước khi điều trị; trì hoãn điều trị nếu có nhiễm trùng răng/loét miệng hoặc phẫu thuật răng gần đây",
            "Hội chứng giả cúm (sốt, ớn lạnh, đau cơ) rất thường gặp sau liều đầu - có thể dùng acetaminophen để giảm triệu chứng, thường tự hết trong 24-48 giờ",
            "Thận trọng phối hợp thuốc độc thận (NSAID, vancomycin, platinum, IV contrast) hoặc thuốc gây hạ calci (aminoglycosides, loop diuretics)",
            "Ngừng điều trị nếu CrCl giảm hoặc có dấu hiệu suy thận cấp",
            "Tránh dùng cho phụ nữ mang thai hoặc có kế hoạch mang thai",
            "Không dùng cho trẻ em và thanh thiếu niên dưới 18 tuổi"
        ],
        "pharmacokinetics": {
            "absorption": "Dùng IV, phân bố nhanh vào xương (gắn mạnh vào hydroxyapatite).",
            "distribution": "Gắn protein ~22%; tích lũy chủ yếu ở xương.",
            "metabolism": "Không chuyển hóa đáng kể.",
            "excretion": "Khoảng 39% thải qua thận trong 24 giờ; phần còn lại gắn xương và thải rất chậm.",
            "half_life": "146 giờ (pha cuối, do giải phóng chậm từ xương).",
            "onset": "24-48 giờ (giảm calci máu trong tăng calci do ung thư).",
            "duration": "Hiệu lực chống hủy xương kéo dài tới 12 tháng (liều loãng xương).",
            "protein_binding": "Khoảng 22%.",
            "clearance": "Thanh thải chủ yếu qua thận; tránh dùng nếu CrCl <35 mL/phút cho chỉ định loãng xương.",
            "notes": "Nguy cơ độc thận tăng nếu truyền nhanh hoặc mất nước; đảm bảo đủ nước."
        },
        "storage": "Bảo quản ở 15-30°C, tránh ánh sáng. Sau khi pha trong 100ml NaCl 0,9% hoặc D5W, dùng ngay hoặc trong 24 giờ nếu bảo quản 2-8°C (không đông lạnh).",
        "black_box_warnings": "Suy thận cấp (nguy cơ tăng khi truyền <15 phút hoặc mất nước); hạ calci máu có thể nghiêm trọng; hoại tử xương hàm (ONJ); gãy xương đùi không điển hình khi dùng kéo dài.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Cộng gộp hạ calci máu",
                    "effect": "Tăng nguy cơ hạ calci máu nghiêm trọng",
                    "management": "Theo dõi calci sát, bổ sung calci/vitamin D; cân nhắc tránh phối hợp nếu có thể."
                },
                {
                    "drug": "Loop diuretics (furosemide, bumetanide)",
                    "mechanism": "Tăng bài tiết calci qua thận",
                    "effect": "Tăng nguy cơ hạ calci máu",
                    "management": "Theo dõi calci; bổ sung calci/vitamin D."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc độc thận (NSAID, vancomycin, platinum, IV contrast)",
                    "mechanism": "Cộng gộp độc tính trên thận",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Đảm bảo đủ nước, theo dõi creatinine trước và sau truyền."
                }
            ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Category D - CHỐNG CHỈ ĐỊNH trong thai kỳ; có thể gây bất thường phát triển xương thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú nếu lợi ích vượt trội và theo dõi calci/triệu chứng ở trẻ."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều (không chuyển hóa qua gan).",
            "notes": "Chủ yếu thải qua thận; điều chỉnh dựa trên chức năng thận thay vì gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ calci máu nặng (co giật, tetany, rối loạn nhịp)",
                "Hạ phospho máu",
                "Suy thận cấp",
                "Sốt, ớn lạnh nặng"
            ],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [
                "Bù calci IV (calcium gluconate hoặc calcium chloride) và vitamin D",
                "Bổ sung phosphate nếu hạ phospho máu",
                "Truyền dịch, theo dõi sát chức năng thận; lọc máu nếu cần",
                "Điều trị triệu chứng sốt/đau (acetaminophen/NSAID nếu phù hợp)"
            ],
            "monitoring": "Calci, phospho, magnesium, chức năng thận, ECG và triệu chứng lâm sàng."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 4-5mg trong 100ml NaCl 0,9% hoặc D5W.",
                "infusion_rate": "Truyền CHẬM tối thiểu 15 phút, dùng dây truyền riêng.",
                "compatibility": ["NaCl 0,9%", "D5W"],
                "incompatibility": [
                    "Dung dịch chứa calci (calcium gluconate, calcium chloride)",
                    "Trộn chung với thuốc/ion đa hóa trị khác"
                ],
                "notes": "Đảm bảo bù nước trước/sau truyền; không pha chung với dung dịch chứa calci."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zoledronic acid (Zometa, Reclast, Aclasta)",
                "UpToDate - Zoledronic acid: Drug information",
                "ASCO Guidelines - Hypercalcemia of malignancy",
                "ASCO Guidelines - Cancer Bone Metastases",
                "NOF Guidelines - Osteoporosis Treatment 2024",
                "HORIZON-PFT Study - Zoledronic acid for osteoporosis",
                "EMA - Zoledronic acid Product Information",
                "Nhà thuốc An Khang - Zoledronic Acid",
                "MIMS Vietnam - Zoledronic Acid"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - FDA-approved, large RCTs (HORIZON-PFT), ASCO guidelines",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal", "skeletal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": [
                "Renal function (creatinine - Black Box Warning - acute renal failure nếu truyền nhanh hoặc mất nước)",
                "Calcium/phosphorus (hypocalcemia risk - Black Box Warning)",
                "Flu-like syndrome (fever, myalgia - common)",
                "ONJ signs (osteonecrosis of jaw - Black Box Warning)",
                "Atypical femur fractures (long-term use - Black Box Warning)"
            ]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Renal Impairment (acute renal failure if rapid infusion or dehydration)",
            "FDA Black Box Warning - Hypocalcemia (can be severe)",
            "FDA Black Box Warning - Osteonecrosis of Jaw (ONJ)",
            "FDA Black Box Warning - Atypical Femur Fractures (long-term use)",
            "ACR Guidelines - Osteoporosis",
            "ASCO Guidelines - Hypercalcemia of malignancy",
            "NOF Guidelines - Osteoporosis Treatment",
            "UpToDate - Zoledronic acid: Drug information"
        ],
    },
}
