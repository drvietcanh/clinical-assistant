"""
Other Osteoporosis Medications
Denosumab (RANKL inhibitor), Teriparatide/Abaloparatide (PTH analogs),
Romosozumab (Sclerostin inhibitor), Raloxifene (SERM)
"""

OSTEOPOROSIS_OTHER_DRUGS = {
    "Abaloparatide": {
        "group": "Endocrinology - PTHrP Analog (Osteoporosis - Anabolic)",
        "vietnamese_name": "Abaloparatide, Tymlos",
        "administration": ["SC"],
        "indications": [
            "Loãng xương sau mãn kinh ở phụ nữ có nguy cơ gãy xương cao.",
        ],
        "contraindications": [
            "Dị ứng với abaloparatide.",
            "Tăng calci máu.",
            "Ung thư xương hoặc di căn xương.",
            "Bệnh Paget xương.",
            "Tiền sử xạ trị xương.",
        ],
        "dosage": {
            "adult_sc": "80mcg SC mỗi ngày, tiêm dưới da bụng.",
            "notes": "Dùng tối đa 24 tháng trong đời. Luân phiên vị trí tiêm. Bổ sung calcium và vitamin D.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng.",
            "under_30": "Không khuyến cáo nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Chóng mặt, đau đầu.",
            "Buồn nôn, nôn.",
            "Đau cơ, đau xương.",
            "Tăng calci máu - theo dõi.",
            "Tăng nguy cơ ung thư xương ở động vật thí nghiệm (osteosarcoma) - chưa rõ ở người.",
        ],
        "interactions": [],
        "pregnancy": "C: tránh dùng trong thai kỳ.",
        "mechanism_of_action": (
            "Abaloparatide là peptide tổng hợp tương tự PTHrP (Parathyroid Hormone-related Protein), "
            "kích thích tạo xương tương tự teriparatide nhưng có cấu trúc khác. "
            "Kích thích tế bào tạo xương (osteoblasts) và tăng hình thành xương mới, "
            "dẫn đến tăng mật độ xương và giảm nguy cơ gãy xương. "
            "Chỉ được dùng tối đa 24 tháng trong đời do nguy cơ ung thư xương ở động vật thí nghiệm."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 12-24 tháng.",
            "Calci máu trước và trong điều trị.",
            "Creatinine, eGFR trước điều trị.",
            "Dấu hiệu tăng calci máu.",
        ],
        "precautions": [
            "Dùng tối đa 24 tháng trong đời.",
            "Bổ sung calcium và vitamin D.",
            "Nguy cơ tăng calci máu - theo dõi calci máu chặt chẽ.",
            "Không dùng ở bệnh nhân ung thư xương hoặc di căn xương.",
            "SC: tiêm dưới da bụng. Luân phiên vị trí tiêm.",
        ],
        "pharmacokinetics": {
            "half_life": "~1.7 giờ.",
            "onset": "Tăng mật độ xương trong 3-6 tháng.",
            "duration": "24 giờ (tiêm 1 lần/ngày).",
            "protein_binding": "N/A (peptide).",
            "clearance": "Chuyển hóa ở gan và thận.",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh. Sau khi mở, có thể bảo quản ở nhiệt độ phòng tối đa 30 ngày.",
        "black_box_warnings": (
            "Ung thư xương (osteosarcoma): tăng nguy cơ ở động vật thí nghiệm. "
            "Chưa rõ nguy cơ ở người. Không dùng ở bệnh nhân ung thư xương hoặc di căn xương. "
            "Dùng tối đa 24 tháng trong đời."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với abaloparatide.",
                "Tăng calci máu.",
                "Ung thư xương hoặc di căn xương.",
                "Bệnh Paget xương.",
                "Tiền sử xạ trị xương.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Không khuyến cáo.",
            "notes": "Abaloparatide chuyển hóa một phần qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Tăng calci máu nặng.", "Buồn nôn, nôn nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị tăng calci máu: bù dịch, calcitonin, bisphosphonate nếu cần.",
                "Ngừng abaloparatide.",
            ],
            "monitoring": "Calci máu, ECG, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Bút tiêm sẵn dùng.",
                "injection_site": "Tiêm dưới da bụng. Luân phiên vị trí tiêm.",
                "timing": "Tiêm 1 lần/ngày, cùng giờ mỗi ngày. Dùng tối đa 24 tháng trong đời.",
                "notes": "Bảo quản trong tủ lạnh (2-8°C). Sau khi mở, có thể bảo quản ở nhiệt độ phòng tối đa 30 ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tymlos (abaloparatide)",
                "NOF Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
              "reversal_agents": {
              "available": False,
              "agents": []
          },
},

    "Calcitonin": {
        "group": "Endocrinology - Calcitonin (Osteoporosis, Hypercalcemia)",
        "vietnamese_name": "Calcitonin, Calcitonin cá hồi (salmon calcitonin)",
        "administration": ["SC", "IM", "IN"],
        "indications": [
            "Tăng calci máu cấp do ác tính (hỗ trợ ngắn hạn)",
            "Loãng xương sau mãn kinh khi các lựa chọn khác không phù hợp (vai trò hạn chế hiện nay)",
            "Đau do gãy xương lún đốt sống cấp (giảm đau ngắn hạn)",
        ],
        "contraindications": [
            "Dị ứng với calcitonin, đặc biệt calcitonin cá hồi",
        ],
        "dosage": {
            "hypercalcemia_sc_im": "4 IU/kg SC/IM mỗi 12 giờ (có thể tăng đến 8 IU/kg mỗi 6 giờ nếu cần)",
            "osteoporosis_in": "200 IU xịt mũi 1 lần/ngày, luân phiên bên mũi",
            "notes": "Hiệu quả loãng xương yếu hơn nhiều so với bisphosphonate/denosumab/PTH analog; chủ yếu dùng giảm đau gãy lún đốt sống cấp.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều, nhưng dữ liệu hạn chế",
        },
        "side_effects": [
            "Buồn nôn, nôn (SC/IM)",
            "Đỏ bừng mặt, cảm giác nóng bừng",
            "Kích ứng, chảy máu, khô mũi (dạng xịt mũi)",
            "Dị ứng, phản vệ (hiếm)",
            "Có báo cáo tăng nhẹ nguy cơ ung thư với dùng kéo dài dạng xịt mũi",
        ],
        "interactions": [],
        "pregnancy": "C – tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Calcitonin là hormone do tế bào C tuyến giáp tiết, làm giảm calci máu bằng cách ức chế hoạt động tế bào hủy xương "
            "và tăng thải calci qua thận. Trong tăng calci máu cấp, calcitonin cho tác dụng nhanh nhưng dung nạp giảm sau vài ngày. "
            "Trong loãng xương, hiệu quả tăng mật độ xương yếu, nên hiện ít được khuyến cáo như lựa chọn hàng đầu."
        ),
        "monitoring": [
            "Calci máu (đặc biệt trong điều trị tăng calci máu)",
            "Triệu chứng dị ứng, phản vệ (mề đay, khó thở)",
            "Đau xương/gãy lún đốt sống (đánh giá giảm đau)",
        ],
        "precautions": [
            "Không dùng kéo dài dạng xịt mũi cho loãng xương nếu có lựa chọn tốt hơn do lo ngại tăng nhẹ nguy cơ ung thư.",
            "Có thể cân nhắc test dị ứng trước khi dùng SC/IM nếu nghi ngờ cơ địa dị ứng.",
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 1 giờ (SC/IM); dạng xịt mũi hấp thu biến thiên",
            "onset": "Vài giờ cho tác dụng hạ calci",
            "duration": "Hiệu quả hạ calci kéo dài khoảng 6–8 giờ; xuất hiện hiện tượng nhờn thuốc sau vài ngày",
            "protein_binding": "N/A (peptide)",
            "clearance": "Chuyển hóa nhanh tại thận và mô; thải qua thận",
        },
        "storage": "Bảo quản trong tủ lạnh (2–8°C) theo hướng dẫn; một số chế phẩm có thể để nhiệt độ phòng trong thời gian giới hạn.",
        "black_box_warnings": (
            "Một số nghiên cứu cho thấy tăng nhẹ nguy cơ ung thư khi dùng calcitonin đường mũi kéo dài; "
            "chỉ dùng khi lợi ích vượt trội nguy cơ và không có lựa chọn tốt hơn."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với calcitonin cá hồi hoặc thành phần chế phẩm",
            ],
            "tương_đối": [
                "Tiền sử ung thư – cân nhắc kỹ nếu dùng kéo dài dạng xịt mũi",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng khi thật cần thiết (tăng calci máu cấp) dưới giám sát chuyên khoa.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa; nguy cơ lý thuyết thấp do peptide bị phân hủy trong tiêu hóa.",
                "recommendation": "Cân nhắc lợi ích–nguy cơ, ưu tiên điều trị thay thế nếu có.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Không chuyển hóa qua gan đáng kể.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ calci máu (hiếm do thời gian bán thải ngắn)",
                "Buồn nôn, nôn nặng, hạ huyết áp",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng calcitonin",
                "Điều trị hạ calci máu nếu có (calcium IV/PO)",
                "Hỗ trợ tuần hoàn nếu tụt huyết áp",
            ],
            "monitoring": "Calci máu, huyết áp, triệu chứng dị ứng.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng hoặc tăng calci máu nặng."},
        "administration_instructions": {
            "sc": {
                "injection_site": "Tiêm dưới da vùng đùi, bụng hoặc cánh tay, luân phiên vị trí tiêm.",
                "timing": "Mỗi 12–24 giờ tùy chỉ định.",
            },
            "in": {
                "notes": "Xịt mũi, luân phiên bên mũi, không hít sâu khi xịt.",
            },
        },
        "references": {
            "primary_sources": [
                "Endocrine Society guideline on osteoporosis",
                "UpToDate – Calcitonin in hypercalcemia and osteoporosis",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "B – vai trò hạn chế, dùng chọn lọc",
        },
    },
    "Denosumab": {
        "group": "Endocrinology - RANKL Inhibitor (Osteoporosis)",
        "vietnamese_name": "Denosumab, Prolia, Xgeva",
        "administration": ["SC"],
        "indications": [
            "Loãng xương sau mãn kinh ở phụ nữ có nguy cơ gãy xương cao (Prolia - 60mg mỗi 6 tháng).",
            "Loãng xương ở nam giới có nguy cơ gãy xương cao (Prolia).",
            "Loãng xương do corticosteroid (Prolia).",
            "Ung thư di căn xương (Xgeva - 120mg mỗi 4 tuần).",
            "Ung thư xương khổng lồ (Xgeva).",
        ],
        "contraindications": [
            "Dị ứng với denosumab.",
            "Hạ calci máu.",
            "Đang mang thai.",
        ],
        "dosage": {
            "adult_osteoporosis": "Prolia: 60mg SC mỗi 6 tháng.",
            "adult_cancer_bone": "Xgeva: 120mg SC mỗi 4 tuần.",
            "notes": "Tiêm dưới da bụng, đùi hoặc cánh tay. Bổ sung calcium và vitamin D trước và trong điều trị.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; thận trọng vì tăng nguy cơ hạ calci máu.",
            "under_30": "Thận trọng, tăng nguy cơ hạ calci máu; đảm bảo bổ sung đủ calcium và vitamin D.",
        },
        "side_effects": [
            "Hạ calci máu - phổ biến và nghiêm trọng, đặc biệt ở suy thận.",
            "Nhiễm trùng da, eczema.",
            "Hoại tử xương hàm (ONJ) - đặc biệt ở bệnh nhân ung thư, phẫu thuật răng.",
            "Gãy xương đùi không điển hình - hiếm.",
            "Nhiễm trùng nghiêm trọng - tăng nguy cơ.",
            "Đau cơ, đau xương, đau lưng.",
        ],
        "interactions": [
            "Immunosuppressants: tăng nguy cơ nhiễm trùng.",
        ],
        "pregnancy": "X: chống chỉ định trong thai kỳ.",
        "mechanism_of_action": (
            "Denosumab là kháng thể đơn dòng kháng RANKL (Receptor Activator of Nuclear Factor κB Ligand). "
            "RANKL là cytokine quan trọng trong quá trình hủy xương, kích thích sự hình thành, hoạt động và sống sót "
            "của tế bào hủy xương (osteoclasts). Bằng cách ức chế RANKL, denosumab làm giảm hình thành và hoạt động "
            "của tế bào hủy xương, dẫn đến giảm hủy xương và tăng mật độ xương. Denosumab có tác dụng nhanh và mạnh, "
            "nhưng tác dụng không kéo dài sau khi ngừng (khác với bisphosphonates)."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 1-2 năm.",
            "Calci máu, phospho máu, magie máu trước và trong điều trị - QUAN TRỌNG.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Dấu hiệu hạ calci máu (co cứng cơ, tê, co giật, rối loạn nhịp tim).",
            "Dấu hiệu hoại tử xương hàm (đau hàm, sưng, răng lung lay).",
            "Dấu hiệu nhiễm trùng da tại chỗ tiêm.",
            "Dấu hiệu gãy xương đùi không điển hình.",
        ],
        "precautions": [
            "QUAN TRỌNG: Bổ sung calcium (1000-1200mg/ngày) và vitamin D (800-1000 IU/ngày) trước và trong điều trị.",
            "Nguy cơ hạ calci máu cao, đặc biệt ở suy thận - theo dõi calci máu chặt chẽ.",
            "Nguy cơ hoại tử xương hàm: đánh giá răng miệng trước điều trị, tránh phẫu thuật răng trong khi dùng.",
            "Nguy cơ nhiễm trùng: thận trọng ở bệnh nhân suy giảm miễn dịch.",
            "Tác dụng không kéo dài sau khi ngừng - có thể mất mật độ xương nhanh, cân nhắc chuyển sang bisphosphonate sau khi ngừng.",
            "SC: tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
        ],
        "pharmacokinetics": {
            "half_life": "~25 ngày.",
            "onset": "Giảm markers hủy xương trong vài ngày đến 1 tuần.",
            "duration": "6 tháng (Prolia) hoặc 4 tuần (Xgeva) - tác dụng không kéo dài sau khi ngừng.",
            "protein_binding": "N/A (monoclonal antibody).",
            "clearance": "Phân hủy bởi hệ thống reticuloendothelial.",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh. Có thể bảo quản ở nhiệt độ phòng (≤25°C) tối đa 30 ngày.",
        "black_box_warnings": (
            "Hạ calci máu: có thể xảy ra và nghiêm trọng, đặc biệt ở suy thận. "
            "Bổ sung calcium và vitamin D trước và trong điều trị. Hoại tử xương hàm (ONJ): "
            "có thể xảy ra, đặc biệt ở bệnh nhân ung thư, phẫu thuật răng. "
            "Gãy xương đùi không điển hình: tăng nguy cơ. "
            "Nhiễm trùng nghiêm trọng: tăng nguy cơ nhiễm trùng nghiêm trọng."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Immunosuppressants (corticosteroid, cyclosporine)",
                    "mechanism": "Cả hai đều làm suy giảm miễn dịch.",
                    "effect": "Tăng nguy cơ nhiễm trùng nghiêm trọng.",
                    "management": "Thận trọng. Theo dõi dấu hiệu nhiễm trùng.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với denosumab.",
                "Hạ calci máu.",
                "Đang mang thai.",
            ],
            "tương_đối": [
                "Suy thận - tăng nguy cơ hạ calci máu, đảm bảo bổ sung đủ calcium và vitamin D.",
                "Phẫu thuật răng gần đây hoặc dự kiến - tăng nguy cơ ONJ.",
                "Suy giảm miễn dịch - tăng nguy cơ nhiễm trùng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Có thể gây hại cho thai nhi.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Denosumab là monoclonal antibody, không chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ calci máu nặng (co cứng cơ, tê, co giật, rối loạn nhịp tim).",
                "Nhiễm trùng nghiêm trọng.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ calci máu: calcium IV ngay lập tức nếu có triệu chứng.",
                "Bổ sung calcium và vitamin D đường uống.",
                "Điều trị nhiễm trùng nếu có.",
            ],
            "monitoring": "Calci máu, phospho máu, magie máu, ECG, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dung dịch tiêm sẵn dùng.",
                "injection_site": "Tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
                "timing": "Prolia: tiêm mỗi 6 tháng. Xgeva: tiêm mỗi 4 tuần.",
                "notes": "Bảo quản trong tủ lạnh (2-8°C). Đảm bảo bổ sung đủ calcium và vitamin D trước và trong điều trị.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Prolia (denosumab), Xgeva (denosumab)",
                "FREEDOM Study - Denosumab for osteoporosis",
                "NOF Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCTs (FREEDOM)",
        },
             "reversal_agents": {
             "available": False,
             "agents": []
         },
},

    "Raloxifene": {
        "group": "Endocrinology - SERM (Selective Estrogen Receptor Modulator)",
        "vietnamese_name": "Raloxifene, Evista",
        "administration": ["PO"],
        "indications": [
            "Loãng xương sau mãn kinh ở phụ nữ.",
            "Dự phòng loãng xương sau mãn kinh.",
            "Giảm nguy cơ ung thư vú xâm lấn ở phụ nữ sau mãn kinh có nguy cơ cao.",
        ],
        "contraindications": [
            "Dị ứng với raloxifene.",
            "Đang mang thai hoặc có thể mang thai.",
            "Đang cho con bú.",
            "Tiền sử huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE).",
            "Suy gan nặng.",
        ],
        "dosage": {
            "adult_osteoporosis": "60mg PO mỗi ngày.",
            "adult_breast_cancer_prevention": "60mg PO mỗi ngày.",
            "notes": "Uống bất kỳ lúc nào, có thể uống với hoặc không thức ăn. Bổ sung calcium và vitamin D.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, dữ liệu hạn chế.",
        },
        "side_effects": [
            "Bốc hỏa, đổ mồ hôi đêm.",
            "Chuột rút chân.",
            "Tăng nguy cơ huyết khối tĩnh mạch sâu (DVT) và thuyên tắc phổi (PE) - nghiêm trọng.",
            "Tăng nguy cơ đột quỵ tử vong.",
            "Đau khớp.",
        ],
        "interactions": [
            "Warfarin: raloxifene có thể tăng tác dụng chống đông của warfarin - theo dõi INR.",
            "Cholestyramine: giảm hấp thu raloxifene - dùng cách xa.",
        ],
        "pregnancy": "X: chống chỉ định trong thai kỳ.",
        "mechanism_of_action": (
            "Raloxifene là SERM (Selective Estrogen Receptor Modulator), tác dụng chọn lọc trên các thụ thể estrogen khác nhau. "
            "Trên xương: raloxifene hoạt động như chất chủ vận estrogen, kích thích thụ thể estrogen trên tế bào xương, "
            "dẫn đến giảm hủy xương và tăng mật độ xương. Trên vú: raloxifene hoạt động như chất đối kháng estrogen, "
            "ức chế tác dụng của estrogen, giảm nguy cơ ung thư vú. Trên tử cung: raloxifene không kích thích tử cung "
            "(khác với estrogen), không tăng nguy cơ ung thư nội mạc tử cung. Trên hệ tim mạch: raloxifene không có "
            "lợi ích tim mạch như estrogen, thậm chí tăng nguy cơ huyết khối và đột quỵ."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 1-2 năm.",
            "Dấu hiệu huyết khối tĩnh mạch sâu (sưng chân, đau chân) và thuyên tắc phổi (khó thở, đau ngực).",
            "Dấu hiệu đột quỵ (yếu liệt, rối loạn ngôn ngữ).",
            "INR nếu dùng với warfarin.",
        ],
        "precautions": [
            "QUAN TRỌNG: Tăng nguy cơ huyết khối tĩnh mạch sâu (DVT) và thuyên tắc phổi (PE) - không dùng ở bệnh nhân có tiền sử DVT/PE.",
            "Tăng nguy cơ đột quỵ tử vong - thận trọng ở bệnh nhân có nguy cơ đột quỵ.",
            "Ngừng ít nhất 72 giờ trước phẫu thuật lớn hoặc bất động kéo dài để giảm nguy cơ huyết khối.",
            "Bổ sung calcium và vitamin D.",
            "Có thể gây bốc hỏa - thường giảm sau vài tháng.",
        ],
        "pharmacokinetics": {
            "half_life": "~27.7 giờ.",
            "onset": "Tăng mật độ xương trong 6-12 tháng.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": ">95%.",
            "clearance": "Chuyển hóa ở gan (glucuronidation), thải qua phân.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Tăng nguy cơ huyết khối tĩnh mạch sâu (DVT) và thuyên tắc phổi (PE): "
            "không dùng ở bệnh nhân có tiền sử DVT/PE. Ngừng ít nhất 72 giờ trước phẫu thuật lớn hoặc bất động kéo dài. "
            "Tăng nguy cơ đột quỵ tử vong."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Raloxifene có thể tăng tác dụng chống đông của warfarin.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu.",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu raloxifene. Điều chỉnh liều warfarin nếu cần.",
                },
            ],
            "moderate": [
                {
                    "drug": "Cholestyramine",
                    "mechanism": "Cholestyramine giảm hấp thu raloxifene.",
                    "effect": "Giảm hiệu quả raloxifene.",
                    "management": "Dùng cách xa ít nhất 2 giờ.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với raloxifene.",
                "Đang mang thai hoặc có thể mang thai.",
                "Đang cho con bú.",
                "Tiền sử huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE).",
                "Suy gan nặng.",
            ],
            "tương_đối": [
                "Nguy cơ đột quỵ cao - thận trọng.",
                "Phẫu thuật lớn hoặc bất động kéo dài - ngừng ít nhất 72 giờ trước.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Có thể gây hại cho thai nhi.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Chống chỉ định khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Chống chỉ định.",
            "notes": "Raloxifene chuyển hóa ở gan (glucuronidation).",
        },
        "overdose_management": {
            "symptoms": [
                "Bốc hỏa nặng.",
                "Chuột rút chân.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng raloxifene.",
                "Điều trị hỗ trợ.",
            ],
            "monitoring": "Triệu chứng lâm sàng, dấu hiệu huyết khối.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Evista (raloxifene)",
                "MORE Study - Raloxifene for osteoporosis",
                "NOF Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCTs (MORE)",
        },
              "reversal_agents": {
              "available": False,
              "agents": []
          },
},

    "Romosozumab": {
        "group": "Endocrinology - Sclerostin Inhibitor (Osteoporosis - Anabolic)",
        "vietnamese_name": "Romosozumab, Evenity",
        "administration": ["SC"],
        "indications": [
            "Loãng xương sau mãn kinh ở phụ nữ có nguy cơ gãy xương cao.",
        ],
        "contraindications": [
            "Dị ứng với romosozumab.",
            "Tăng calci máu.",
            "Đang mang thai.",
            "Tiền sử đột quỵ hoặc cơn thiếu máu não thoáng qua (TIA) trong 1 năm qua.",
            "Nhồi máu cơ tim trong 1 năm qua.",
        ],
        "dosage": {
            "adult_sc": "210mg SC mỗi tháng (2 mũi tiêm 105mg mỗi mũi), dùng trong 12 tháng.",
            "notes": "Tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm. Bổ sung calcium và vitamin D.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, dữ liệu hạn chế.",
        },
        "side_effects": [
            "Đau cơ, đau khớp, đau lưng.",
            "Đau đầu.",
            "Tăng nguy cơ đột quỵ, nhồi máu cơ tim, tử vong tim mạch.",
            "Hoại tử xương hàm (ONJ) - hiếm.",
            "Gãy xương đùi không điển hình - hiếm.",
        ],
        "interactions": [],
        "pregnancy": "X: chống chỉ định trong thai kỳ.",
        "mechanism_of_action": (
            "Romosozumab là kháng thể đơn dòng kháng sclerostin. Sclerostin là protein được sản xuất bởi tế bào xương, "
            "ức chế con đường Wnt/β-catenin, làm giảm hoạt động của tế bào tạo xương (osteoblasts). "
            "Bằng cách ức chế sclerostin, romosozumab kích thích con đường Wnt/β-catenin, "
            "tăng hoạt động của tế bào tạo xương và giảm hoạt động của tế bào hủy xương, "
            "dẫn đến tăng mật độ xương nhanh và mạnh. Romosozumab có tác dụng kép: vừa kích thích tạo xương "
            "(anabolic) vừa ức chế hủy xương (anti-resorptive)."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 12 tháng.",
            "Calci máu, phospho máu trước và trong điều trị.",
            "Dấu hiệu đột quỵ, nhồi máu cơ tim (đau ngực, khó thở, yếu liệt, rối loạn ngôn ngữ).",
            "Dấu hiệu hoại tử xương hàm.",
            "Dấu hiệu gãy xương đùi không điển hình.",
        ],
        "precautions": [
            "QUAN TRỌNG: Tăng nguy cơ đột quỵ, nhồi máu cơ tim, tử vong tim mạch - không dùng ở bệnh nhân có tiền sử đột quỵ/TIA hoặc nhồi máu cơ tim trong 1 năm qua.",
            "Dùng trong 12 tháng, sau đó chuyển sang bisphosphonate hoặc denosumab để duy trì.",
            "Bổ sung calcium và vitamin D.",
            "Nguy cơ hoại tử xương hàm: đánh giá răng miệng trước điều trị.",
            "SC: tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
        ],
        "pharmacokinetics": {
            "half_life": "~5-6 ngày.",
            "onset": "Tăng mật độ xương nhanh trong 3-6 tháng.",
            "duration": "1 tháng (tiêm mỗi tháng), dùng trong 12 tháng.",
            "protein_binding": "N/A (monoclonal antibody).",
            "clearance": "Phân hủy bởi hệ thống reticuloendothelial.",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh. Có thể bảo quản ở nhiệt độ phòng (≤25°C) tối đa 30 ngày.",
        "black_box_warnings": (
            "Tăng nguy cơ đột quỵ, nhồi máu cơ tim, tử vong tim mạch: "
            "không dùng ở bệnh nhân có tiền sử đột quỵ hoặc cơn thiếu máu não thoáng qua (TIA) trong 1 năm qua, "
            "hoặc nhồi máu cơ tim trong 1 năm qua. Hoại tử xương hàm (ONJ): có thể xảy ra. "
            "Gãy xương đùi không điển hình: tăng nguy cơ."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với romosozumab.",
                "Tăng calci máu.",
                "Đang mang thai.",
                "Tiền sử đột quỵ hoặc TIA trong 1 năm qua.",
                "Nhồi máu cơ tim trong 1 năm qua.",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ biến cố tim mạch.",
                "Suy thận nặng (CrCl <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Có thể gây hại cho thai nhi.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Romosozumab là monoclonal antibody, không chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu.",
                "Đau cơ, đau xương nặng.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị tăng calci máu nếu cần.",
                "Ngừng romosozumab.",
                "Theo dõi tại bệnh viện.",
            ],
            "monitoring": "Calci máu, ECG, dấu hiệu sinh tồn, dấu hiệu biến cố tim mạch.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dung dịch tiêm sẵn dùng (2 mũi tiêm 105mg mỗi mũi).",
                "injection_site": "Tiêm dưới da bụng, đùi hoặc cánh tay. Luân phiên vị trí tiêm.",
                "timing": "Tiêm mỗi tháng, dùng trong 12 tháng. Sau đó chuyển sang bisphosphonate hoặc denosumab.",
                "notes": "Bảo quản trong tủ lạnh (2-8°C). Đảm bảo bổ sung đủ calcium và vitamin D.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Evenity (romosozumab)",
                "FRAME Study - Romosozumab for osteoporosis",
                "NOF Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCTs (FRAME)",
        },
              "reversal_agents": {
              "available": False,
              "agents": []
          },
},

    "Teriparatide": {
        "group": "Endocrinology - PTH Analog (Osteoporosis - Anabolic)",
        "vietnamese_name": "Teriparatide, Forteo",
        "administration": ["SC"],
        "indications": [
            "Loãng xương sau mãn kinh ở phụ nữ có nguy cơ gãy xương cao.",
            "Loãng xương ở nam giới có nguy cơ gãy xương cao.",
            "Loãng xương do corticosteroid.",
        ],
        "contraindications": [
            "Dị ứng với teriparatide.",
            "Tăng calci máu.",
            "Ung thư xương hoặc di căn xương.",
            "Bệnh Paget xương.",
            "Trẻ em và thanh thiếu niên (chưa đóng sụn tăng trưởng).",
            "Tiền sử xạ trị xương.",
        ],
        "dosage": {
            "adult_sc": "20mcg SC mỗi ngày, tiêm dưới da đùi hoặc bụng.",
            "notes": "Dùng tối đa 24 tháng trong đời. Luân phiên vị trí tiêm. Bổ sung calcium và vitamin D.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không khuyến cáo nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Đau cơ, đau xương, đau khớp.",
            "Chóng mặt, đau đầu.",
            "Tăng calci máu - theo dõi.",
            "Tăng acid uric máu, bệnh gút.",
            "Buồn nôn.",
            "Tăng nguy cơ ung thư xương ở động vật thí nghiệm (osteosarcoma) - chưa rõ ở người.",
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ tăng calci máu.",
        ],
        "pregnancy": "C: tránh dùng trong thai kỳ.",
        "mechanism_of_action": (
            "Teriparatide là peptide tổng hợp chứa 34 amino acid đầu tiên của hormone tuyến cận giáp (PTH 1-34). "
            "Khác với bisphosphonates và denosumab (ức chế hủy xương), teriparatide là thuốc đồng hóa (anabolic), "
            "kích thích tạo xương. Teriparatide kích thích tế bào tạo xương (osteoblasts) và tăng hình thành xương mới, "
            "dẫn đến tăng mật độ xương và giảm nguy cơ gãy xương. Teriparatide có tác dụng mạnh hơn bisphosphonates "
            "trong việc tăng mật độ xương, đặc biệt ở cột sống, nhưng chỉ được dùng tối đa 24 tháng trong đời "
            "do nguy cơ ung thư xương ở động vật thí nghiệm."
        ),
        "monitoring": [
            "Mật độ xương (DEXA scan) trước điều trị và sau 12-24 tháng.",
            "Calci máu trước và trong điều trị (sau 1 tháng, sau đó mỗi 3-6 tháng).",
            "Acid uric máu nếu có triệu chứng gút.",
            "Creatinine, eGFR trước điều trị.",
            "Dấu hiệu tăng calci máu (buồn nôn, nôn, yếu cơ, rối loạn nhịp tim).",
        ],
        "precautions": [
            "Dùng tối đa 24 tháng trong đời (do nguy cơ ung thư xương ở động vật thí nghiệm).",
            "Bổ sung calcium (1000-1200mg/ngày) và vitamin D (800-1000 IU/ngày).",
            "Nguy cơ tăng calci máu - theo dõi calci máu chặt chẽ.",
            "Nguy cơ tăng acid uric máu, bệnh gút - theo dõi nếu có triệu chứng.",
            "Không dùng ở bệnh nhân ung thư xương hoặc di căn xương.",
            "SC: tiêm dưới da đùi hoặc bụng. Luân phiên vị trí tiêm.",
        ],
        "pharmacokinetics": {
            "half_life": "~1 giờ.",
            "onset": "Tăng markers tạo xương trong vài tuần, tăng mật độ xương trong 3-6 tháng.",
            "duration": "24 giờ (tiêm 1 lần/ngày), nhưng tác dụng kéo dài sau khi ngừng.",
            "protein_binding": "N/A (peptide).",
            "clearance": "Chuyển hóa ở gan và thận.",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh. Sau khi mở, có thể bảo quản ở nhiệt độ phòng tối đa 28 ngày.",
        "black_box_warnings": (
            "Ung thư xương (osteosarcoma): tăng nguy cơ ở động vật thí nghiệm. "
            "Chưa rõ nguy cơ ở người. Không dùng ở bệnh nhân ung thư xương hoặc di căn xương. "
            "Dùng tối đa 24 tháng trong đời."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Teriparatide tăng calci máu, digoxin nhạy cảm với calci.",
                    "effect": "Tăng nguy cơ độc tính digoxin.",
                    "management": "Thận trọng. Theo dõi calci máu và nồng độ digoxin.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với teriparatide.",
                "Tăng calci máu.",
                "Ung thư xương hoặc di căn xương.",
                "Bệnh Paget xương.",
                "Trẻ em và thanh thiếu niên.",
                "Tiền sử xạ trị xương.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Tiền sử bệnh gút - tăng nguy cơ tái phát.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Có thể ảnh hưởng đến phát triển xương thai nhi.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Không khuyến cáo.",
            "notes": "Teriparatide chuyển hóa một phần qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu nặng (buồn nôn, nôn, yếu cơ, rối loạn nhịp tim).",
                "Đau cơ, đau xương nặng.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị tăng calci máu: bù dịch, calcitonin, bisphosphonate nếu cần.",
                "Ngừng teriparatide.",
                "Theo dõi tại bệnh viện.",
            ],
            "monitoring": "Calci máu, ECG, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "sc": {
                "reconstitution": "Bút tiêm sẵn dùng.",
                "injection_site": "Tiêm dưới da đùi hoặc bụng. Luân phiên vị trí tiêm.",
                "timing": "Tiêm 1 lần/ngày, cùng giờ mỗi ngày. Dùng tối đa 24 tháng trong đời.",
                "notes": "Bảo quản trong tủ lạnh (2-8°C). Sau khi mở, có thể bảo quản ở nhiệt độ phòng tối đa 28 ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Forteo (teriparatide)",
                "NOF Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
              "reversal_agents": {
              "available": False,
              "agents": []
          },
},

}

__all__ = ["OSTEOPOROSIS_OTHER_DRUGS"]

