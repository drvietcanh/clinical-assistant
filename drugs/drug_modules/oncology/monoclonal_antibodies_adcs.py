"""Oncology Medications - Monoclonal Antibodies and Antibody-Drug Conjugates
Active module - contains targeted therapy mAbs and ADCs for cancer treatment"""

# Monoclonal Antibodies and Antibody-Drug Conjugates for Oncology

MONOCLONAL_ANTIBODIES_ADCS_DRUGS = {
    "Bevacizumab": {
        "group": "Oncology - Anti-VEGF Monoclonal Antibody",
        "vietnamese_name": "Bevacizumab, Avastin",
        "administration": ["IV"],
        "indications": [
            "Ung thư đại trực tràng (metastatic) - kết hợp với hóa trị",
            "Ung thư phổi không tế bào nhỏ (NSCLC - non-squamous) - kết hợp với hóa trị",
            "Ung thư thận (metastatic renal cell carcinoma)",
            "Ung thư buồng trứng (recurrent)",
            "Ung thư cổ tử cung (persistent, recurrent, or metastatic)",
            "Ung thư não (glioblastoma - recurrent)"
        ],
        "contraindications": [
            "Dị ứng bevacizumab hoặc bất kỳ thành phần nào",
            "Phẫu thuật gần đây (trong vòng 28 ngày)",
            "Vết thương hở chưa lành",
            "Xuất huyết nặng đang hoạt động"
        ],
        "dosage": {
            "adult_colorectal": "5mg/kg IV mỗi 2 tuần hoặc 7.5mg/kg IV mỗi 3 tuần (với FOLFOX)",
            "adult_nsclc": "15mg/kg IV mỗi 3 tuần (với hóa trị)",
            "adult_renal": "10mg/kg IV mỗi 2 tuần",
            "adult_ovarian": "15mg/kg IV mỗi 3 tuần (với hóa trị)",
            "notes": "Truyền tĩnh mạch trong 30-90 phút (liều đầu tiên 90 phút, liều sau 30-60 phút). Bevacizumab là anti-VEGF mAb, ức chế angiogenesis (tạo mạch máu mới)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Xuất huyết (chảy máu) - phổ biến, có thể nghiêm trọng",
            "Huyết khối động mạch (arterial thrombosis) - hiếm nhưng NGUY HIỂM",
            "Huyết khối tĩnh mạch (venous thrombosis) - phổ biến",
            "Tăng huyết áp - phổ biến",
            "Protein niệu (proteinuria) - phổ biến, có thể nặng",
            "Thủng đường tiêu hóa (GI perforation) - hiếm nhưng NGUY HIỂM, có thể tử vong",
            "Lỗ rò (fistula) - hiếm nhưng NGUY HIỂM",
            "Chậm lành vết thương (wound healing impairment) - phổ biến",
            "Phản ứng truyền (infusion-related reactions) - hiếm",
            "Mệt mỏi - phổ biến",
            "Buồn nôn, nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Độc tim (suy tim) - hiếm",
            "Hội chứng não sau (posterior reversible encephalopathy syndrome - PRES) - hiếm nhưng NGUY HIỂM"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể dùng cùng với các thuốc hóa trị khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Bevacizumab là kháng thể đơn dòng kháng VEGF (Vascular Endothelial Growth Factor, humanized monoclonal antibody IgG1). VEGF là cytokine quan trọng trong quá trình angiogenesis (tạo mạch máu mới), kích thích tăng sinh tế bào nội mô mạch máu và tạo mạch máu mới. Trong ung thư, khối u cần mạch máu mới để cung cấp oxy và chất dinh dưỡng cho sự phát triển. Bevacizumab gắn với VEGF (VEGF-A) → ngăn chặn VEGF gắn với thụ thể VEGFR trên tế bào nội mô → ức chế angiogenesis → giảm cung cấp máu cho khối u → khối u thiếu oxy và chất dinh dưỡng → chết tế bào ung thư và giảm kích thước khối u. Bevacizumab cũng làm bình thường hóa mạch máu khối u, tăng hiệu quả của hóa trị. ĐẶC ĐIỂM: (1) Anti-VEGF mAb, ức chế angiogenesis, (2) Xuất huyết - phổ biến, có thể nghiêm trọng, (3) Thủng đường tiêu hóa - hiếm nhưng NGUY HIỂM, có thể tử vong, (4) Chậm lành vết thương - phổ biến, CHỐNG CHỈ ĐỊNH phẫu thuật gần đây, (5) Tăng huyết áp và protein niệu - phổ biến, (6) Hiệu quả với nhiều loại ung thư khi dùng kết hợp với hóa trị.",
        "monitoring": [
            "Huyết áp - QUAN TRỌNG (tăng huyết áp phổ biến), theo dõi mỗi chu kỳ",
            "Protein niệu - QUAN TRỌNG (protein niệu phổ biến, có thể nặng), theo dõi mỗi chu kỳ",
            "Dấu hiệu xuất huyết (chảy máu) - phổ biến, có thể nghiêm trọng",
            "Dấu hiệu thủng đường tiêu hóa (đau bụng, nôn, sốt) - hiếm nhưng NGUY HIỂM",
            "Dấu hiệu lỗ rò (fistula) - hiếm nhưng NGUY HIỂM",
            "Dấu hiệu huyết khối (đau ngực, khó thở, sưng chân) - phổ biến",
            "Dấu hiệu độc tim (suy tim) - hiếm",
            "Dấu hiệu hội chứng não sau (PRES) - đau đầu, co giật, rối loạn thị giác - hiếm nhưng NGUY HIỂM",
            "Đáp ứng điều trị: CT scan mỗi 2-3 tháng"
        ],
        "precautions": [
            "XUẤT HUYẾT - phổ biến, có thể nghiêm trọng, ngừng ngay nếu có xuất huyết nặng",
            "THỦNG ĐƯỜNG TIÊU HÓA - hiếm nhưng NGUY HIỂM, có thể tử vong - NGỪNG NGAY nếu có đau bụng, nôn, sốt",
            "CHẬM LÀNH VẾT THƯƠNG - phổ biến, CHỐNG CHỈ ĐỊNH phẫu thuật gần đây (trong vòng 28 ngày) và vết thương hở chưa lành",
            "TĂNG HUYẾT ÁP - phổ biến, điều trị với thuốc hạ huyết áp nếu cần",
            "PROTEIN NIỆU - phổ biến, có thể nặng, ngừng nếu protein niệu nặng (>3.5g/24h)",
            "HUYẾT KHỐI - phổ biến (tĩnh mạch), hiếm nhưng NGUY HIỂM (động mạch), điều trị với thuốc chống đông nếu cần",
            "Độc tim (suy tim) - hiếm, ngừng nếu có",
            "Hội chứng não sau (PRES) - hiếm nhưng NGUY HIỂM, ngừng ngay nếu có",
            "Có thể dùng kết hợp với các thuốc hóa trị khác"
        ],
        "pharmacokinetics": {
            "half_life": "20 ngày",
            "onset": "Vài tuần (tác dụng lâm sàng)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 8 giờ ở 2-8°C hoặc 4 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "XUẤT HUYẾT (chảy máu) - phổ biến, có thể nghiêm trọng và đe dọa tính mạng. Ngừng ngay bevacizumab nếu có xuất huyết nặng. THỦNG ĐƯỜNG TIÊU HÓA (GI perforation) - hiếm nhưng NGUY HIỂM, có thể tử vong. Ngừng ngay bevacizumab nếu có đau bụng, nôn, sốt. CHẬM LÀNH VẾT THƯƠNG (wound healing impairment) - phổ biến. CHỐNG CHỈ ĐỊNH phẫu thuật gần đây (trong vòng 28 ngày) và vết thương hở chưa lành.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng bevacizumab hoặc bất kỳ thành phần nào",
                "Phẫu thuật gần đây (trong vòng 28 ngày) - CHỐNG CHỈ ĐỊNH",
                "Vết thương hở chưa lành - CHỐNG CHỈ ĐỊNH",
                "Xuất huyết nặng đang hoạt động - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Tăng huyết áp không kiểm soát - điều trị trước khi dùng",
                "Protein niệu nặng (>3.5g/24h) - ngừng bevacizumab",
                "Huyết khối động mạch gần đây - tăng nguy cơ",
                "Bệnh tim - tăng nguy cơ độc tim"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Bevacizumab phân loại C - thận trọng trong thai kỳ. Không có dữ liệu đầy đủ trên phụ nữ có thai. Bevacizumab ức chế angiogenesis, có thể gây hại cho thai nhi. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết bevacizumab có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Bevacizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Xuất huyết nặng (chảy máu)",
                "Thủng đường tiêu hóa nặng (đau bụng, nôn, sốt)",
                "Tăng huyết áp nặng",
                "Protein niệu nặng",
                "Huyết khối nặng",
                "Độc tim (suy tim)",
                "Hội chứng não sau (PRES)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay bevacizumab",
                "Nếu xuất huyết nặng: truyền máu, điều trị hỗ trợ",
                "Nếu thủng đường tiêu hóa: phẫu thuật khẩn cấp nếu cần",
                "Nếu tăng huyết áp nặng: thuốc hạ huyết áp",
                "Nếu huyết khối: thuốc chống đông",
                "Nếu độc tim: hỗ trợ tim mạch",
                "Nếu PRES: điều trị hỗ trợ, có thể cần điều trị co giật",
                "Supportive care: bù dịch, điều trị nhiễm trùng"
            ],
            "monitoring": "Dấu hiệu sinh tồn, huyết áp, protein niệu, dấu hiệu xuất huyết, dấu hiệu thủng đường tiêu hóa, dấu hiệu huyết khối, ECG, dấu hiệu độc tim, dấu hiệu PRES"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W. Nồng độ cuối: 1.4-16.5mg/ml. Không lọc.",
                "infusion_rate": "Liều đầu tiên: truyền trong 90 phút. Liều sau: truyền trong 30-60 phút nếu dung nạp tốt.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Theo dõi chặt chẽ trong và sau truyền (phản ứng truyền hiếm). Có thể phối hợp với FOLFIRI, FOLFOX, hoặc các phác đồ hóa trị khác."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Bevacizumab (Avastin)",
                "UpToDate - Bevacizumab: Drug Information",
                "NCCN Guidelines - Colorectal Cancer, Non-Small Cell Lung Cancer",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, effective for multiple cancer types when combined with chemotherapy"
        }
    },

    "Brentuximab vedotin": {
        "group": "Oncology - Antibody-Drug Conjugate (ADC)",
        "vietnamese_name": "Brentuximab vedotin, Adcetris",
        "administration": ["IV"],
        "indications": [
            "Hodgkin lymphoma - relapsed/refractory",
            "Hodgkin lymphoma - frontline (kết hợp với AVD)",
            "Anaplastic large cell lymphoma (ALCL) - relapsed/refractory",
            "Cutaneous T-cell lymphoma (CTCL) - relapsed/refractory",
            "Peripheral T-cell lymphoma (PTCL) - frontline"
        ],
        "contraindications": [
            "Dị ứng brentuximab vedotin hoặc bất kỳ thành phần nào",
            "Đang có nhiễm trùng nặng"
        ],
        "dosage": {
            "adult_standard": "1.8mg/kg IV mỗi 3 tuần (tối đa 180mg)",
            "adult_weekly": "1.2mg/kg IV mỗi tuần x 3 tuần, sau đó nghỉ 1 tuần (chu kỳ 4 tuần)",
            "notes": "Truyền tĩnh mạch trong 30 phút. Cần premedication để giảm phản ứng truyền. Dùng kết hợp với các thuốc khác trong một số phác đồ."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Giảm bạch cầu trung tính (neutropenia) - phổ biến, có thể nghiêm trọng",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Giảm hemoglobin (anemia) - phổ biến",
            "Bệnh lý thần kinh ngoại biên (peripheral neuropathy) - phổ biến, có thể nghiêm trọng",
            "Mệt mỏi",
            "Buồn nôn",
            "Tiêu chảy",
            "Sốt",
            "Nhiễm trùng (nhiễm trùng đường hô hấp trên, viêm phổi) - phổ biến",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Hội chứng giải phóng cytokine (cytokine release syndrome) - hiếm nhưng nghiêm trọng"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Thuốc gây độc thần kinh (vincristine, cisplatin): tăng nguy cơ bệnh lý thần kinh",
            "Strong CYP3A4 inhibitors: tăng nồng độ monomethyl auristatin E (MMAE), tăng độc tính",
            "Strong CYP3A4 inducers: giảm nồng độ MMAE, giảm hiệu quả"
        ],
        "pregnancy": "D",
        "mechanism_of_action": (
            "Brentuximab vedotin là antibody-drug conjugate (ADC) gồm: "
            "(1) kháng thể đơn dòng kháng CD30 (chimeric monoclonal antibody), "
            "(2) linker (valine-citrulline dipeptide), và "
            "(3) payload (monomethyl auristatin E - MMAE, một chất ức chế microtubule). "
            "CD30 là kháng nguyên bề mặt trên tế bào Reed-Sternberg trong Hodgkin lymphoma và tế bào T trong ALCL. "
            "Brentuximab vedotin gắn với CD30 trên tế bào ung thư → được nội bào hóa (internalization) vào tế bào → "
            "linker bị cắt bởi protease (cathepsin B) trong lysosome → giải phóng MMAE → "
            "MMAE ức chế microtubule polymerization → ngăn cản phân chia tế bào → gây chết tế bào ung thư. "
            "Dẫn đến: tiêu diệt tế bào ung thư biểu hiện CD30, cải thiện đáp ứng điều trị, và kéo dài thời gian sống. "
            "Brentuximab vedotin được dùng để điều trị Hodgkin lymphoma và T-cell lymphoma, "
            "đặc biệt hiệu quả ở bệnh nhân relapsed/refractory. "
            "MMAE cũng có thể được giải phóng vào máu và gây độc tính toàn thân (đặc biệt bệnh lý thần kinh ngoại biên)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng tiểu cầu - theo dõi thrombocytopenia",
            "Hemoglobin - theo dõi anemia",
            "Bệnh lý thần kinh ngoại biên - theo dõi triệu chứng (tê, ngứa ran, yếu, đau)",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Đáp ứng điều trị (CT scan, PET scan)"
        ],
        "precautions": [
            "BỆNH LÝ THẦN KINH NGOẠI BIÊN - phổ biến và có thể nghiêm trọng, cần theo dõi và điều chỉnh liều",
            "PHẢN ỨNG TRUYỀN - phổ biến, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm bạch cầu",
            "Giảm liều hoặc ngừng thuốc nếu bệnh lý thần kinh ngoại biên nặng (grade 3-4)",
            "Thận trọng khi dùng với thuốc gây độc thần kinh (vincristine, cisplatin)",
            "Thận trọng khi dùng với strong CYP3A4 inhibitors hoặc inducers",
            "Ngừng brentuximab vedotin nếu có nhiễm trùng nặng"
        ],
        "pharmacokinetics": {
            "half_life": "~4-6 ngày (ADC), ~3-4 ngày (MMAE)",
            "onset": "Giảm tế bào ung thư trong vòng vài tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "ADC: IgG1 monoclonal antibody, MMAE: ~70%",
            "metabolism": "ADC: chuyển hóa qua RES, MMAE: chuyển hóa qua CYP3A4",
            "clearance": "ADC: không phụ thuộc gan thận đáng kể, MMAE: phụ thuộc gan (CYP3A4)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 24 giờ ở 2-8°C hoặc 8 giờ ở nhiệt độ phòng.",
        "black_box_warnings": (
            "BỆNH LÝ THẦN KINH NGOẠI BIÊN - có thể nghiêm trọng và không hồi phục. "
            "Cần theo dõi triệu chứng và điều chỉnh liều hoặc ngừng thuốc nếu nặng. "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội. "
            "Ngừng brentuximab vedotin nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa MMAE, tăng nồng độ",
                    "effect": "Tăng độc tính (đặc biệt bệnh lý thần kinh ngoại biên)",
                    "management": "Thận trọng. Có thể cần giảm liều brentuximab vedotin."
                },
                {
                    "drug": "Thuốc gây độc thần kinh (vincristine, cisplatin, paclitaxel)",
                    "mechanism": "Tăng độc tính thần kinh",
                    "effect": "Tăng nguy cơ bệnh lý thần kinh ngoại biên nghiêm trọng",
                    "management": "Thận trọng. Theo dõi triệu chứng thần kinh chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa MMAE, giảm nồng độ",
                    "effect": "Giảm hiệu quả brentuximab vedotin",
                    "management": "Thận trọng. Có thể cần tăng liều brentuximab vedotin."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng brentuximab vedotin hoặc bất kỳ thành phần nào",
                "Đang có nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Tiền sử bệnh lý thần kinh ngoại biên nặng",
                "Tiền sử nhiễm trùng tái phát",
                "Suy gan nặng - giảm chuyển hóa MMAE, tăng độc tính",
                "Suy thận nặng - giảm thải trừ, tăng độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Tránh dùng trong thai kỳ. Nếu cần dùng, thông báo rõ ràng về nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Tránh dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "MMAE chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ MMAE, tăng độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ bệnh lý thần kinh ngoại biên nặng",
                "Tăng nguy cơ giảm bạch cầu/tiểu cầu nặng",
                "Tăng nguy cơ nhiễm trùng",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Theo dõi bệnh lý thần kinh ngoại biên chặt chẽ",
                "Hỗ trợ tế bào máu nếu cần (G-CSF, truyền tiểu cầu, truyền máu)",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chức năng gan"
            ],
            "monitoring": "Bệnh lý thần kinh ngoại biên, số lượng tế bào máu, chức năng gan, dấu hiệu nhiễm trùng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong 30 phút.",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Brentuximab vedotin (Adcetris)",
                "UpToDate - Brentuximab vedotin: Drug information",
                "Lexicomp - Brentuximab vedotin monograph",
                "NCCN Guidelines - Hodgkin Lymphoma"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in Hodgkin and T-cell lymphoma"
        }
    },

    "Cetuximab": {
        "group": "Oncology - Anti-EGFR Monoclonal Antibody",
        "vietnamese_name": "Cetuximab, Erbitux",
        "administration": ["IV"],
        "indications": [
            "Ung thư đại trực tràng (metastatic) - KRAS wild-type",
            "Ung thư đầu cổ (squamous cell carcinoma) - locally advanced hoặc recurrent/metastatic"
        ],
        "contraindications": [
            "Dị ứng cetuximab hoặc bất kỳ thành phần nào",
            "KRAS mutation positive (ung thư đại trực tràng) - không hiệu quả"
        ],
        "dosage": {
            "adult_initial": "400mg/m² IV (liều đầu tiên, truyền 120 phút)",
            "adult_maintenance": "250mg/m² IV mỗi tuần (truyền 60 phút)",
            "notes": "Cần premedication với diphenhydramine để giảm phản ứng truyền. Chỉ dùng cho KRAS wild-type (không có KRAS mutation) trong ung thư đại trực tràng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Phản ứng truyền (infusion-related reactions) - phổ biến, có thể nghiêm trọng",
            "Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash)",
            "Ngứa - phổ biến",
            "Khô da - phổ biến",
            "Viêm móng (paronychia) - phổ biến",
            "Mệt mỏi - phổ biến",
            "Buồn nôn, nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Hạ magne máu (hypomagnesemia) - phổ biến, có thể nặng",
            "Viêm phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng NGUY HIỂM",
            "Xuất huyết (chảy máu) - hiếm"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể dùng cùng với các thuốc hóa trị khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Cetuximab là kháng thể đơn dòng kháng EGFR (Epidermal Growth Factor Receptor, chimeric monoclonal antibody IgG1). EGFR là thụ thể trên bề mặt tế bào, khi được kích hoạt bởi EGF hoặc các ligands khác, kích hoạt tín hiệu tăng sinh tế bào (RAS-RAF-MEK-ERK pathway và PI3K-AKT pathway). Trong ung thư đại trực tràng và đầu cổ, EGFR thường được biểu hiện quá mức, dẫn đến tăng sinh tế bào ung thư. Cetuximab gắn với EGFR trên tế bào ung thư → ngăn chặn EGF gắn với EGFR → ức chế hoạt tính kinase của EGFR → ngăn chặn tín hiệu tăng sinh và gây chết tế bào ung thư. Cetuximab cũng kích hoạt antibody-dependent cell-mediated cytotoxicity (ADCC) và complement-dependent cytotoxicity (CDC). ĐẶC ĐIỂM: (1) Anti-EGFR mAb, hiệu quả với ung thư đại trực tràng KRAS wild-type và ung thư đầu cổ, (2) Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị, (3) Hạ magne máu - phổ biến, có thể nặng, cần bổ sung magne, (4) CHỐNG CHỈ ĐỊNH ở KRAS mutation positive (không hiệu quả), (5) Phản ứng truyền - phổ biến, cần premedication.",
        "monitoring": [
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị",
            "Magne máu - QUAN TRỌNG (hạ magne phổ biến, có thể nặng), theo dõi mỗi chu kỳ",
            "Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị",
            "Dấu hiệu viêm phổi kẽ (ILD) - hiếm nhưng NGUY HIỂM",
            "Dấu hiệu xuất huyết (chảy máu) - hiếm",
            "Đáp ứng điều trị: CT scan mỗi 2-3 tháng",
            "Test KRAS mutation trước điều trị (ung thư đại trực tràng)"
        ],
        "precautions": [
            "PHẢN ỨNG TRUYỀN - phổ biến, có thể nghiêm trọng, cần premedication với diphenhydramine",
            "PHÁT BAN (RASH) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị, điều trị với corticosteroid tại chỗ hoặc kháng sinh nếu nhiễm trùng",
            "HẠ MAGNE MÁU - phổ biến, có thể nặng, cần bổ sung magne định kỳ",
            "CHỐNG CHỈ ĐỊNH ở KRAS mutation positive (ung thư đại trực tràng) - không hiệu quả, cần test KRAS trước điều trị",
            "VIÊM PHỔI KẼ (ILD) - hiếm nhưng NGUY HIỂM - NGỪNG NGAY nếu có khó thở, ho, sốt",
            "Theo dõi chức năng gan chặt chẽ (tăng men gan phổ biến)",
            "Có thể dùng kết hợp với các thuốc hóa trị khác (FOLFIRI, FOLFOX)"
        ],
        "pharmacokinetics": {
            "half_life": "112 giờ (4.7 ngày)",
            "onset": "Vài tuần (tác dụng lâm sàng)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 12 giờ ở 2-8°C hoặc 8 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "PHẢN ỨNG TRUYỀN (infusion-related reactions) - có thể nghiêm trọng và đe dọa tính mạng. Cần premedication với diphenhydramine. Theo dõi chặt chẽ trong và sau truyền. VIÊM PHỔI KẼ (Interstitial Lung Disease - ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong. Ngừng ngay cetuximab nếu có khó thở, ho, sốt.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cetuximab hoặc bất kỳ thành phần nào",
                "KRAS mutation positive (ung thư đại trực tràng) - CHỐNG CHỈ ĐỊNH (không hiệu quả)"
            ],
            "tương_đối": [
                "Viêm phổi kẽ đang hoạt động - tăng nguy cơ ILD",
                "Bệnh phổi - tăng nguy cơ ILD"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Cetuximab phân loại C - thận trọng trong thai kỳ. Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết cetuximab có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Cetuximab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng (sốc phản vệ)",
                "Phát ban nặng",
                "Hạ magne máu nặng",
                "Viêm phổi kẽ nặng (khó thở, ho, sốt)",
                "Tăng men gan nặng",
                "Xuất huyết (chảy máu)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay cetuximab",
                "Xử trí phản ứng truyền: epinephrine, diphenhydramine, corticosteroid, H2 blocker, hỗ trợ hô hấp",
                "Nếu viêm phổi kẽ: ngừng ngay, chụp X-quang ngực, corticosteroid, hỗ trợ hô hấp nếu cần",
                "Bổ sung magne nếu hạ magne máu",
                "Điều trị phát ban: corticosteroid tại chỗ, kháng sinh nếu nhiễm trùng",
                "Supportive care: bù dịch, điều trị nhiễm trùng"
            ],
            "monitoring": "Dấu hiệu sinh tồn, chức năng gan, magne máu, X-quang ngực, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu viêm phổi kẽ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W. Nồng độ cuối: 0.4-2mg/ml. Không lọc.",
                "infusion_rate": "Liều đầu tiên: 400mg/m² IV truyền trong 120 phút. Liều duy trì: 250mg/m² IV truyền trong 60 phút mỗi tuần.",
                "premedication": "CẦN PREMEDICATION: Diphenhydramine 50mg IV trước truyền để giảm phản ứng truyền.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Theo dõi chặt chẽ trong và sau truyền (phản ứng truyền). Có thể phối hợp với FOLFIRI hoặc FOLFOX (ung thư đại trực tràng)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cetuximab (Erbitux)",
                "UpToDate - Cetuximab: Drug Information",
                "NCCN Guidelines - Colorectal Cancer, Head and Neck Cancer",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, effective for KRAS wild-type colorectal cancer and head and neck cancer"
        }
    },

    "Daratumumab": {
        "group": "Oncology - Anti-CD38 Monoclonal Antibody",
        "vietnamese_name": "Daratumumab, Darzalex",
        "administration": ["IV", "SC"],
        "indications": [
            "Multiple myeloma - newly diagnosed",
            "Multiple myeloma - relapsed/refractory",
            "AL amyloidosis - relapsed/refractory"
        ],
        "contraindications": [
            "Dị ứng daratumumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_iv": "16mg/kg IV mỗi tuần x 8 tuần, sau đó mỗi 2 tuần x 16 tuần, sau đó mỗi 4 tuần",
            "adult_sc": "1800mg SC mỗi tuần x 8 tuần, sau đó mỗi 2 tuần x 16 tuần, sau đó mỗi 4 tuần",
            "notes": "Truyền tĩnh mạch hoặc tiêm dưới da. Cần premedication để giảm phản ứng truyền. Dùng kết hợp với các thuốc khác (lenalidomide, bortezomib, pomalidomide)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion-related reactions) - phổ biến, có thể nghiêm trọng",
            "Giảm bạch cầu trung tính (neutropenia) - phổ biến",
            "Giảm bạch cầu lympho (lymphopenia) - phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Giảm hemoglobin (anemia) - phổ biến",
            "Nhiễm trùng (nhiễm trùng đường hô hấp trên, viêm phổi) - phổ biến",
            "Mệt mỏi",
            "Buồn nôn",
            "Tiêu chảy",
            "Tăng nguy cơ nhiễm trùng nặng (bao gồm nhiễm trùng cơ hội)"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Vaccine sống: chống chỉ định trong và sau điều trị"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Daratumumab là kháng thể đơn dòng kháng CD38 (human monoclonal antibody). "
            "CD38 là kháng nguyên bề mặt trên tế bào plasma (plasma cells) và tế bào myeloma, "
            "cũng có trên một số tế bào miễn dịch khác. "
            "Trong multiple myeloma, tế bào myeloma biểu hiện CD38 ở mức độ cao. "
            "Daratumumab gắn với CD38 trên tế bào myeloma → kích hoạt complement-dependent cytotoxicity (CDC), "
            "antibody-dependent cell-mediated cytotoxicity (ADCC), và antibody-dependent cellular phagocytosis (ADCP) → "
            "tiêu diệt tế bào myeloma. "
            "Daratumumab cũng có thể ức chế hoạt động của CD38 (một enzyme có vai trò trong chuyển hóa), "
            "gây ức chế tăng sinh tế bào myeloma. "
            "Dẫn đến: giảm số lượng tế bào myeloma, cải thiện đáp ứng điều trị, và kéo dài thời gian sống trong multiple myeloma. "
            "Daratumumab được dùng để điều trị multiple myeloma (newly diagnosed và relapsed/refractory), "
            "thường dùng kết hợp với các thuốc khác (lenalidomide, bortezomib, pomalidomide, dexamethasone)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng bạch cầu lympho - theo dõi lymphopenia",
            "Số lượng tiểu cầu - theo dõi thrombocytopenia",
            "Hemoglobin - theo dõi anemia",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Đáp ứng điều trị (M-protein, free light chains, bone marrow biopsy)"
        ],
        "precautions": [
            "PHẢN ỨNG TRUYỀN - phổ biến và có thể nghiêm trọng, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm tế bào miễn dịch",
            "Cần hoàn thành tất cả vaccine trước khi bắt đầu điều trị (ít nhất 4-6 tuần trước)",
            "CHỐNG CHỈ ĐỊNH vaccine sống trong và sau điều trị (ít nhất 3-6 tháng sau liều cuối)",
            "Ngừng daratumumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm trùng tái phát",
            "Dạng SC: ít phản ứng truyền hơn dạng IV"
        ],
        "pharmacokinetics": {
            "half_life": "~18 ngày (dài, cho phép dùng 1-4 tuần một lần)",
            "onset": "Giảm tế bào myeloma trong vòng vài tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "IgG1κ monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 24 giờ ở 2-8°C hoặc 15 giờ ở nhiệt độ phòng.",
        "black_box_warnings": (
            "NGUY CƠ PHẢN ỨNG TRUYỀN - có thể nghiêm trọng và đe dọa tính mạng. "
            "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. "
            "Theo dõi chặt chẽ trong và sau truyền. "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội. "
            "Ngừng daratumumab nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Vaccine sống (MMR, varicella, zoster, yellow fever, BCG)",
                    "mechanism": "Daratumumab làm giảm đáp ứng miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "CHỐNG CHỈ ĐỊNH dùng vaccine sống trong và sau điều trị. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao, lenalidomide, bortezomib)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng",
                    "management": "Thận trọng. Theo dõi chặt chẽ dấu hiệu nhiễm trùng."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng daratumumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tiền sử nhiễm trùng tái phát",
                "Tiền sử phản ứng truyền nặng với các mAbs khác",
                "Suy giảm miễn dịch nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Daratumumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ phản ứng truyền nặng",
                "Tăng nguy cơ nhiễm trùng",
                "Giảm bạch cầu/tiểu cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay nếu có phản ứng nặng",
                "Điều trị phản ứng truyền: corticosteroid, antihistamine, epinephrine nếu cần",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Hỗ trợ tế bào máu nếu cần (G-CSF, truyền tiểu cầu, truyền máu)"
            ],
            "monitoring": "Phản ứng truyền, dấu hiệu nhiễm trùng, số lượng tế bào máu, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch với tốc độ tăng dần (bắt đầu 50ml/h, tăng đến 200ml/h nếu dung nạp tốt).",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền."
            },
            "sc": {
                "reconstitution": "Dùng trực tiếp từ ống tiêm đã pha sẵn.",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                "notes": "Dạng SC: ít phản ứng truyền hơn dạng IV. Cần premedication trước mỗi liều."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Daratumumab (Darzalex)",
                "UpToDate - Daratumumab: Drug information",
                "Lexicomp - Daratumumab monograph",
                "NCCN Guidelines - Multiple Myeloma"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in multiple myeloma"
        }
    },

    "Sacituzumab govitecan": {
        "group": "Oncology - Antibody-Drug Conjugate (ADC)",
        "vietnamese_name": "Sacituzumab govitecan, Trodelvy",
        "administration": ["IV"],
        "indications": [
            "Ung thư vú triple-negative (TNBC) - unresectable hoặc metastatic",
            "Ung thư vú hormone receptor-positive (HR+) - unresectable hoặc metastatic",
            "Ung thư bàng quang (urothelial carcinoma) - unresectable hoặc metastatic"
        ],
        "contraindications": [
            "Dị ứng sacituzumab govitecan hoặc bất kỳ thành phần nào",
            "Đang có nhiễm trùng nặng"
        ],
        "dosage": {
            "adult_standard": "10mg/kg IV ngày 1 và 8 của chu kỳ 21 ngày",
            "notes": "Truyền tĩnh mạch trong 3 giờ. Cần premedication để giảm phản ứng truyền. Điều chỉnh liều theo độc tính."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Giảm bạch cầu trung tính (neutropenia) - phổ biến, có thể nghiêm trọng",
            "Giảm hemoglobin (anemia) - phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến, có thể nghiêm trọng",
            "Mệt mỏi - phổ biến",
            "Nôn - phổ biến",
            "Rụng tóc - phổ biến",
            "Táo bón - phổ biến",
            "Giảm cảm giác ngon miệng - phổ biến",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Bệnh lý phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng nghiêm trọng",
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Nhiễm trùng - phổ biến"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Strong CYP3A4 inhibitors: tăng nồng độ SN-38, tăng độc tính",
            "Strong CYP3A4 inducers: giảm nồng độ SN-38, giảm hiệu quả",
            "Strong UGT1A1 inhibitors: tăng nồng độ SN-38, tăng độc tính"
        ],
        "pregnancy": "D",
        "mechanism_of_action": (
            "Sacituzumab govitecan là antibody-drug conjugate (ADC) gồm: "
            "(1) sacituzumab (kháng thể đơn dòng kháng Trop-2, humanized monoclonal antibody), "
            "(2) linker (CL2A, cleavable), và "
            "(3) payload (govitecan - SN-38, một chất ức chế topoisomerase I, là chất chuyển hóa hoạt động của irinotecan). "
            "Trop-2 (trophoblast cell-surface antigen 2) là kháng nguyên bề mặt trên tế bào ung thư vú, bàng quang, và các ung thư khác. "
            "Sacituzumab govitecan gắn với Trop-2 trên tế bào ung thư → được nội bào hóa (internalization) vào tế bào → "
            "linker bị cắt bởi protease trong lysosome → giải phóng SN-38 → "
            "SN-38 ức chế topoisomerase I → gây đứt gãy DNA → gây chết tế bào ung thư. "
            "SN-38 cũng có thể khuếch tán vào các tế bào lân cận (bystander effect), "
            "tiêu diệt cả tế bào ung thư không biểu hiện Trop-2. "
            "Dẫn đến: tiêu diệt tế bào ung thư biểu hiện Trop-2, cải thiện đáp ứng điều trị, và kéo dài thời gian sống. "
            "Sacituzumab govitecan được dùng để điều trị ung thư vú triple-negative và HR+, "
            "và ung thư bàng quang, đặc biệt hiệu quả ở bệnh nhân đã điều trị trước đó. "
            "SN-38 cũng có thể được giải phóng vào máu và gây độc tính toàn thân (đặc biệt tiêu chảy và giảm bạch cầu)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng tiểu cầu - theo dõi thrombocytopenia",
            "Hemoglobin - theo dõi anemia",
            "TIÊU CHẢY - theo dõi triệu chứng và mức độ nghiêm trọng",
            "Bệnh lý phổi kẽ (ILD) - theo dõi triệu chứng (khó thở, ho, sốt, đau ngực)",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Đáp ứng điều trị (CT scan, PET scan)"
        ],
        "precautions": [
            "TIÊU CHẢY - phổ biến và có thể nghiêm trọng, cần điều trị sớm (loperamide, atropine/diphenoxylate)",
            "BỆNH LÝ PHỔI KẼ (ILD) - hiếm nhưng nghiêm trọng, cần theo dõi chặt chẽ",
            "PHẢN ỨNG TRUYỀN - phổ biến, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm bạch cầu",
            "Giảm liều hoặc ngừng thuốc nếu giảm bạch cầu/tiểu cầu nặng (grade 3-4)",
            "Giảm liều hoặc ngừng thuốc nếu tiêu chảy nặng (grade 3-4)",
            "Thận trọng khi dùng với strong CYP3A4 hoặc UGT1A1 inhibitors hoặc inducers",
            "Ngừng sacituzumab govitecan nếu có nhiễm trùng nặng"
        ],
        "pharmacokinetics": {
            "half_life": "~11.7 giờ (ADC), ~12.4 giờ (SN-38)",
            "onset": "Giảm tế bào ung thư trong vòng vài tuần",
            "duration": "Trung bình (do half-life trung bình)",
            "protein_binding": "ADC: IgG1 monoclonal antibody, SN-38: ~95%",
            "metabolism": "ADC: chuyển hóa qua RES, SN-38: chuyển hóa qua CYP3A4 và UGT1A1",
            "clearance": "ADC: không phụ thuộc gan thận đáng kể, SN-38: phụ thuộc gan (CYP3A4, UGT1A1)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 4 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
        "black_box_warnings": (
            "TIÊU CHẢY - có thể nghiêm trọng. Cần điều trị sớm (loperamide, atropine/diphenoxylate). "
            "Giảm liều hoặc ngừng thuốc nếu tiêu chảy nặng. "
            "BỆNH LÝ PHỔI KẼ (ILD) - có thể nghiêm trọng và đe dọa tính mạng. "
            "Cần theo dõi triệu chứng và chức năng phổi. "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội. "
            "Ngừng sacituzumab govitecan nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa SN-38, tăng nồng độ",
                    "effect": "Tăng độc tính (đặc biệt tiêu chảy và giảm bạch cầu)",
                    "management": "Thận trọng. Có thể cần giảm liều sacituzumab govitecan."
                },
                {
                    "drug": "Strong UGT1A1 inhibitors",
                    "mechanism": "Ức chế chuyển hóa SN-38, tăng nồng độ",
                    "effect": "Tăng độc tính (đặc biệt tiêu chảy và giảm bạch cầu)",
                    "management": "Thận trọng. Có thể cần giảm liều sacituzumab govitecan."
                }
            ],
            "moderate": [
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa SN-38, giảm nồng độ",
                    "effect": "Giảm hiệu quả sacituzumab govitecan",
                    "management": "Thận trọng. Có thể cần tăng liều sacituzumab govitecan."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng sacituzumab govitecan hoặc bất kỳ thành phần nào",
                "Đang có nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Tiền sử tiêu chảy nặng - tăng nguy cơ tiêu chảy",
                "Tiền sử bệnh lý phổi kẽ - tăng nguy cơ ILD",
                "Tiền sử nhiễm trùng tái phát",
                "Suy gan nặng - giảm chuyển hóa SN-38, tăng độc tính",
                "Suy thận nặng - giảm thải trừ, tăng độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Tránh dùng trong thai kỳ. Nếu cần dùng, thông báo rõ ràng về nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Tránh dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "SN-38 chuyển hóa ở gan qua CYP3A4 và UGT1A1. Suy gan làm giảm chuyển hóa, tăng nồng độ SN-38, tăng độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ tiêu chảy nặng",
                "Tăng nguy cơ bệnh lý phổi kẽ nặng",
                "Tăng nguy cơ giảm bạch cầu/tiểu cầu nặng",
                "Tăng nguy cơ nhiễm trùng",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị tiêu chảy: loperamide, atropine/diphenoxylate, bù nước và điện giải",
                "Đánh giá bệnh lý phổi kẽ (X-quang ngực, CT scan ngực) nếu có triệu chứng",
                "Điều trị ILD nếu có (corticosteroid, hỗ trợ hô hấp nếu cần)",
                "Hỗ trợ tế bào máu nếu cần (G-CSF, truyền tiểu cầu, truyền máu)",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chức năng gan"
            ],
            "monitoring": "Tiêu chảy, bệnh lý phổi kẽ, số lượng tế bào máu, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong 3 giờ.",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền, đặc biệt dấu hiệu tiêu chảy và bệnh lý phổi kẽ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sacituzumab govitecan (Trodelvy)",
                "UpToDate - Sacituzumab govitecan: Drug information",
                "Lexicomp - Sacituzumab govitecan monograph",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in triple-negative breast cancer"
        }
    },

    "Teprotumumab": {
        "group": "Oncology - Anti-IGF-1R Monoclonal Antibody",
        "vietnamese_name": "Teprotumumab, Tepezza",
        "administration": ["IV"],
        "indications": [
            "Bệnh mắt do tuyến giáp (thyroid eye disease - TED) - active, moderate to severe"
        ],
        "contraindications": [
            "Dị ứng teprotumumab hoặc bất kỳ thành phần nào",
            "Đang có nhiễm trùng nặng"
        ],
        "dosage": {
            "adult_standard": "10mg/kg IV liều đầu, sau đó 20mg/kg IV mỗi 3 tuần x 7 liều (tổng 8 liều)",
            "notes": "Truyền tĩnh mạch trong 90 phút. Cần premedication để giảm phản ứng truyền."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Co thắt cơ (muscle spasms) - phổ biến",
            "Rụng tóc - phổ biến",
            "Mệt mỏi - phổ biến",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Tăng đường huyết - phổ biến",
            "Giảm thính lực (hearing loss) - phổ biến, có thể không hồi phục",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Nhiễm trùng - phổ biến"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Insulin, thuốc hạ đường huyết: tăng đường huyết, có thể cần điều chỉnh liều"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Teprotumumab là kháng thể đơn dòng kháng IGF-1R (insulin-like growth factor-1 receptor, human monoclonal antibody). "
            "IGF-1R là thụ thể tyrosine kinase trên tế bào, có vai trò trong tăng sinh tế bào, biệt hóa, và chuyển hóa. "
            "Trong bệnh mắt do tuyến giáp (TED), có sự kích hoạt quá mức của IGF-1R trên tế bào fibroblast và tế bào mỡ trong hốc mắt, "
            "dẫn đến tăng sinh mô, viêm, và phù nề, gây lồi mắt (proptosis), nhìn đôi (diplopia), và các triệu chứng khác. "
            "Teprotumumab gắn với IGF-1R → ức chế tín hiệu IGF-1R → "
            "giảm tăng sinh tế bào fibroblast và tế bào mỡ → giảm viêm và phù nề trong hốc mắt. "
            "Dẫn đến: giảm lồi mắt, cải thiện nhìn đôi, và cải thiện các triệu chứng khác của TED. "
            "Teprotumumab được dùng để điều trị TED active, moderate to severe, "
            "là thuốc đầu tiên được FDA phê duyệt đặc biệt cho TED. "
            "Teprotumumab có thể gây tăng đường huyết do ức chế tín hiệu insulin/IGF-1."
        ),
        "monitoring": [
            "Đáp ứng điều trị: lồi mắt (proptosis), nhìn đôi (diplopia), các triệu chứng khác",
            "Đường huyết - theo dõi tăng đường huyết",
            "Thính lực - theo dõi giảm thính lực (có thể không hồi phục)",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)"
        ],
        "precautions": [
            "GIẢM THÍNH LỰC - phổ biến và có thể không hồi phục, cần theo dõi thính lực định kỳ",
            "TĂNG ĐƯỜNG HUYẾT - phổ biến, có thể cần điều chỉnh liều insulin hoặc thuốc hạ đường huyết",
            "PHẢN ỨNG TRUYỀN - phổ biến, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do ức chế miễn dịch",
            "Ngừng teprotumumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân đái tháo đường - tăng đường huyết",
            "Thận trọng ở bệnh nhân có tiền sử giảm thính lực"
        ],
        "pharmacokinetics": {
            "half_life": "~20 ngày (dài, cho phép dùng mỗi 3 tuần)",
            "onset": "Cải thiện triệu chứng trong vòng vài tuần đến vài tháng",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 4 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
        "black_box_warnings": (
            "GIẢM THÍNH LỰC - có thể không hồi phục. "
            "Cần theo dõi thính lực định kỳ. "
            "Ngừng teprotumumab nếu có giảm thính lực nghiêm trọng. "
            "TĂNG ĐƯỜNG HUYẾT - có thể nghiêm trọng. "
            "Cần theo dõi đường huyết và điều chỉnh liều insulin hoặc thuốc hạ đường huyết nếu cần."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, thuốc hạ đường huyết (metformin, sulfonylureas)",
                    "mechanism": "Teprotumumab gây tăng đường huyết",
                    "effect": "Có thể cần tăng liều insulin hoặc thuốc hạ đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Điều chỉnh liều insulin hoặc thuốc hạ đường huyết nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng",
                    "management": "Thận trọng. Theo dõi chặt chẽ dấu hiệu nhiễm trùng."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng teprotumumab hoặc bất kỳ thành phần nào",
                "Đang có nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Tiền sử giảm thính lực - tăng nguy cơ giảm thính lực",
                "Đái tháo đường - tăng nguy cơ tăng đường huyết",
                "Tiền sử nhiễm trùng tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Teprotumumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ giảm thính lực",
                "Tăng đường huyết nặng",
                "Tăng nguy cơ phản ứng truyền nặng",
                "Tăng nguy cơ nhiễm trùng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay nếu có phản ứng nặng",
                "Điều trị phản ứng truyền: corticosteroid, antihistamine, epinephrine nếu cần",
                "Theo dõi thính lực chặt chẽ",
                "Theo dõi đường huyết và điều chỉnh liều insulin nếu cần",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có"
            ],
            "monitoring": "Thính lực, đường huyết, phản ứng truyền, dấu hiệu nhiễm trùng, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong 90 phút.",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền, đặc biệt dấu hiệu giảm thính lực và tăng đường huyết."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Teprotumumab (Tepezza)",
                "UpToDate - Teprotumumab: Drug information",
                "Lexicomp - Teprotumumab monograph",
                "ATA Guidelines - Thyroid Eye Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in thyroid eye disease"
        }
    },

    "Trastuzumab": {
        "group": "Oncology - Anti-HER2 Monoclonal Antibody",
        "vietnamese_name": "Trastuzumab, Herceptin",
        "administration": ["IV", "SC"],
        "indications": [
            "Ung thư vú (HER2-positive) - adjuvant và metastatic",
            "Ung thư dạ dày (HER2-positive) - metastatic"
        ],
        "contraindications": [
            "Dị ứng trastuzumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_iv_initial": "4mg/kg IV (liều đầu tiên, truyền 90 phút)",
            "adult_iv_maintenance": "2mg/kg IV mỗi tuần (truyền 30 phút)",
            "adult_iv_3weekly": "8mg/kg IV mỗi 3 tuần (truyền 90 phút) sau liều đầu tiên 6mg/kg",
            "adult_sc": "600mg SC mỗi 3 tuần (tiêm dưới da)",
            "notes": "Cần test HER2 trước điều trị (IHC 3+ hoặc FISH positive). Trastuzumab là anti-HER2 mAb, hiệu quả với ung thư vú và dạ dày HER2-positive."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Độc tim (suy tim, rối loạn nhịp) - phổ biến, NGUY HIỂM",
            "Phản ứng truyền (infusion-related reactions) - phổ biến, có thể nghiêm trọng",
            "Mệt mỏi - phổ biến",
            "Buồn nôn, nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Đau đầu - phổ biến",
            "Phát ban - phổ biến",
            "Giảm bạch cầu, tiểu cầu (myelosuppression) - phổ biến (khi dùng với hóa trị)",
            "Viêm phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng NGUY HIỂM",
            "Phản ứng tại chỗ tiêm (với dạng SC) - phổ biến"
        ],
        "interactions": [
            "Anthracyclines (doxorubicin, epirubicin): tăng độc tim - TRÁNH DÙNG CHUNG",
            "Không có tương tác dược động học quan trọng khác"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Trastuzumab là kháng thể đơn dòng kháng HER2 (Human Epidermal Growth Factor Receptor 2, humanized monoclonal antibody IgG1). HER2 là thụ thể tyrosine kinase trên bề mặt tế bào, một thành viên của EGFR family. Trong ung thư vú và dạ dày, một số bệnh nhân có HER2 overexpression (20-30% ung thư vú), dẫn đến tăng sinh tế bào ung thư. Trastuzumab gắn với HER2 trên tế bào ung thư → ngăn chặn dimerization của HER2 với các thụ thể khác (EGFR, HER3, HER4) → ức chế hoạt tính kinase → ngăn chặn tín hiệu tăng sinh (RAS-RAF-MEK-ERK pathway và PI3K-AKT pathway) và gây chết tế bào ung thư. Trastuzumab cũng kích hoạt antibody-dependent cell-mediated cytotoxicity (ADCC) và complement-dependent cytotoxicity (CDC). ĐẶC ĐIỂM: (1) Anti-HER2 mAb, hiệu quả với ung thư vú và dạ dày HER2-positive, (2) Độc tim - phổ biến, NGUY HIỂM, cần theo dõi chức năng tim chặt chẽ, (3) TRÁNH DÙNG CHUNG với anthracyclines (tăng độc tim), (4) Cần test HER2 trước điều trị (IHC 3+ hoặc FISH positive), (5) Có cả dạng IV và SC (dạng SC tiện lợi hơn), (6) Hiệu quả cao với ung thư vú HER2-positive (tăng tỷ lệ sống).",
        "monitoring": [
            "Chức năng tim - QUAN TRỌNG (độc tim phổ biến, NGUY HIỂM), theo dõi trước điều trị, mỗi 3 tháng trong năm đầu, sau đó mỗi 6 tháng:",
            "  - LVEF (Left Ventricular Ejection Fraction) - echo hoặc MUGA scan",
            "  - Dấu hiệu suy tim (khó thở, phù, mệt mỏi)",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu viêm phổi kẽ (ILD) - hiếm nhưng NGUY HIỂM",
            "Công thức máu toàn phần (CBC) - khi dùng với hóa trị",
            "Đáp ứng điều trị: CT scan mỗi 2-3 tháng",
            "Test HER2 trước điều trị (IHC 3+ hoặc FISH positive)"
        ],
        "precautions": [
            "ĐỘC TIM - phổ biến, NGUY HIỂM - theo dõi chức năng tim chặt chẽ (LVEF trước điều trị, mỗi 3 tháng trong năm đầu, sau đó mỗi 6 tháng)",
            "Ngừng trastuzumab nếu LVEF giảm >10% từ baseline hoặc LVEF <50%",
            "TRÁNH DÙNG CHUNG với anthracyclines (doxorubicin, epirubicin) - tăng độc tim nghiêm trọng",
            "Cần test HER2 trước điều trị (IHC 3+ hoặc FISH positive) - chỉ hiệu quả với HER2-positive",
            "Phản ứng truyền - phổ biến, có thể nghiêm trọng, cần theo dõi chặt chẽ",
            "VIÊM PHỔI KẼ (ILD) - hiếm nhưng NGUY HIỂM - NGỪNG NGAY nếu có khó thở, ho, sốt",
            "Dạng SC: phản ứng tại chỗ tiêm - phổ biến",
            "Có thể dùng kết hợp với các thuốc hóa trị khác (paclitaxel, docetaxel, carboplatin)"
        ],
        "pharmacokinetics": {
            "half_life": "28 ngày",
            "onset": "Vài tuần (tác dụng lâm sàng)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 28 ngày ở 2-8°C hoặc 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "ĐỘC TIM (suy tim, rối loạn nhịp) - phổ biến và NGUY HIỂM. Theo dõi chức năng tim chặt chẽ (LVEF trước điều trị, mỗi 3 tháng trong năm đầu, sau đó mỗi 6 tháng). Ngừng trastuzumab nếu LVEF giảm >10% từ baseline hoặc LVEF <50%. TRÁNH DÙNG CHUNG với anthracyclines (doxorubicin, epirubicin) - tăng độc tim nghiêm trọng. VIÊM PHỔI KẼ (Interstitial Lung Disease - ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong. Ngừng ngay trastuzumab nếu có khó thở, ho, sốt.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Anthracyclines (Doxorubicin, Epirubicin)",
                    "mechanism": "Cả hai đều có độc tính tim, tác dụng cộng dồn",
                    "effect": "Tăng độc tim nghiêm trọng, tăng nguy cơ suy tim",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi chức năng tim chặt chẽ. Có thể dùng trastuzumab sau khi hoàn thành anthracyclines."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng trastuzumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy tim nặng (LVEF <50%) - ngừng trastuzumab",
                "Viêm phổi kẽ đang hoạt động - tăng nguy cơ ILD",
                "Bệnh tim - tăng nguy cơ độc tim",
                "HER2-negative - không hiệu quả, cần test HER2 trước điều trị"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Trastuzumab phân loại D - có thể gây hại cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Có thể gây dị tật thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Trastuzumab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Trastuzumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Độc tim nặng (suy tim, rối loạn nhịp)",
                "Phản ứng truyền nặng (sốc phản vệ)",
                "Viêm phổi kẽ nặng (khó thở, ho, sốt)",
                "Giảm bạch cầu, tiểu cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay trastuzumab",
                "Nếu độc tim: điều trị suy tim (ACE inhibitor, beta-blocker, diuretic), hỗ trợ tim mạch nếu cần",
                "Xử trí phản ứng truyền: epinephrine, diphenhydramine, corticosteroid, H2 blocker, hỗ trợ hô hấp",
                "Nếu viêm phổi kẽ: ngừng ngay, chụp X-quang ngực, corticosteroid, hỗ trợ hô hấp nếu cần",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần"
            ],
            "monitoring": "Dấu hiệu sinh tồn, chức năng tim (LVEF, ECG), X-quang ngực, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu viêm phổi kẽ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W. Nồng độ cuối: 0.4-2mg/ml. Không lọc.",
                "infusion_rate": "Liều đầu tiên: 4mg/kg IV truyền trong 90 phút. Liều duy trì hàng tuần: 2mg/kg IV truyền trong 30 phút. Liều 3 tuần: 8mg/kg IV truyền trong 90 phút sau liều đầu tiên 6mg/kg.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Theo dõi chặt chẽ trong và sau truyền (phản ứng truyền). Có thể phối hợp với paclitaxel, docetaxel, carboplatin, hoặc các thuốc hóa trị khác."
            },
            "sc": {
                "reconstitution": "Không cần pha loãng. Dung dịch tiêm sẵn.",
                "injection_site": "Tiêm dưới da (bụng, đùi). Thay đổi vị trí tiêm.",
                "notes": "600mg SC mỗi 3 tuần. Tiêm dưới da. Có thể gây phản ứng tại chỗ tiêm. Dạng SC tiện lợi hơn dạng IV."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Trastuzumab (Herceptin)",
                "UpToDate - Trastuzumab: Drug Information",
                "NCCN Guidelines - Breast Cancer, Gastric Cancer",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, revolutionized HER2-positive breast cancer treatment, extensive clinical data"
        }
    },
    "Trastuzumab deruxtecan": {
        "group": "Oncology - Antibody-Drug Conjugate (ADC)",
        "vietnamese_name": "Trastuzumab deruxtecan, Enhertu",
        "administration": ["IV"],
        "indications": [
            "Ung thư vú HER2+ - unresectable hoặc metastatic",
            "Ung thư vú HER2-low - unresectable hoặc metastatic",
            "Ung thư dạ dày HER2+ - unresectable hoặc metastatic",
            "Ung thư phổi không tế bào nhỏ (NSCLC) HER2-mutant - unresectable hoặc metastatic"
        ],
        "contraindications": [
            "Dị ứng trastuzumab deruxtecan hoặc bất kỳ thành phần nào",
            "Đang có nhiễm trùng nặng"
        ],
        "dosage": {
            "adult_standard": "5.4mg/kg IV mỗi 3 tuần",
            "adult_her2_low": "5.4mg/kg IV mỗi 3 tuần",
            "notes": "Truyền tĩnh mạch trong 30-90 phút. Cần premedication để giảm phản ứng truyền. Điều chỉnh liều theo độc tính."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Giảm bạch cầu trung tính (neutropenia) - phổ biến, có thể nghiêm trọng",
            "Giảm hemoglobin (anemia) - phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Buồn nôn - phổ biến",
            "Mệt mỏi - phổ biến",
            "Nôn - phổ biến",
            "Rụng tóc - phổ biến",
            "Táo bón - phổ biến",
            "Tiêu chảy - phổ biến",
            "Giảm cảm giác ngon miệng - phổ biến",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Bệnh lý phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng nghiêm trọng, có thể gây tử vong",
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Nhiễm trùng - phổ biến"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Strong CYP3A4 inhibitors: tăng nồng độ deruxtecan, tăng độc tính",
            "Strong CYP3A4 inducers: giảm nồng độ deruxtecan, giảm hiệu quả"
        ],
        "pregnancy": "D",
        "mechanism_of_action": (
            "Trastuzumab deruxtecan là antibody-drug conjugate (ADC) gồm: "
            "(1) trastuzumab (kháng thể đơn dòng kháng HER2, humanized monoclonal antibody), "
            "(2) linker (tetrapeptide-based, cleavable), và "
            "(3) payload (deruxtecan - DXd, một chất ức chế topoisomerase I). "
            "HER2 (human epidermal growth factor receptor 2) là thụ thể tyrosine kinase trên tế bào ung thư vú, dạ dày, và phổi. "
            "Trastuzumab deruxtecan gắn với HER2 trên tế bào ung thư → được nội bào hóa (internalization) vào tế bào → "
            "linker bị cắt bởi protease trong lysosome → giải phóng deruxtecan → "
            "deruxtecan ức chế topoisomerase I → gây đứt gãy DNA → gây chết tế bào ung thư. "
            "Deruxtecan cũng có thể khuếch tán vào các tế bào lân cận (bystander effect), "
            "tiêu diệt cả tế bào ung thư không biểu hiện HER2. "
            "Dẫn đến: tiêu diệt tế bào ung thư HER2+, cải thiện đáp ứng điều trị, và kéo dài thời gian sống. "
            "Trastuzumab deruxtecan được dùng để điều trị ung thư vú HER2+ và HER2-low, "
            "ung thư dạ dày HER2+, và ung thư phổi HER2-mutant, "
            "đặc biệt hiệu quả ở bệnh nhân đã điều trị trước đó với trastuzumab và các thuốc khác. "
            "Deruxtecan cũng có thể được giải phóng vào máu và gây độc tính toàn thân (đặc biệt bệnh lý phổi kẽ)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng tiểu cầu - theo dõi thrombocytopenia",
            "Hemoglobin - theo dõi anemia",
            "BỆNH LÝ PHỔI KẼ (ILD) - theo dõi triệu chứng (khó thở, ho, sốt, đau ngực)",
            "Chức năng phổi (X-quang ngực, CT scan ngực) - nếu có triệu chứng ILD",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Đáp ứng điều trị (CT scan, PET scan)"
        ],
        "precautions": [
            "BỆNH LÝ PHỔI KẼ (ILD) - hiếm nhưng nghiêm trọng, có thể gây tử vong, cần theo dõi chặt chẽ",
            "Ngừng trastuzumab deruxtecan ngay nếu nghi ngờ ILD và đánh giá",
            "PHẢN ỨNG TRUYỀN - phổ biến, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm bạch cầu",
            "Giảm liều hoặc ngừng thuốc nếu giảm bạch cầu/tiểu cầu nặng (grade 3-4)",
            "Thận trọng khi dùng với strong CYP3A4 inhibitors hoặc inducers",
            "Ngừng trastuzumab deruxtecan nếu có nhiễm trùng nặng"
        ],
        "pharmacokinetics": {
            "half_life": "~5.7 ngày (ADC), ~5.8 ngày (deruxtecan)",
            "onset": "Giảm tế bào ung thư trong vòng vài tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "ADC: IgG1 monoclonal antibody, deruxtecan: ~97%",
            "metabolism": "ADC: chuyển hóa qua RES, deruxtecan: chuyển hóa qua CYP3A4",
            "clearance": "ADC: không phụ thuộc gan thận đáng kể, deruxtecan: phụ thuộc gan (CYP3A4)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 24 giờ ở 2-8°C hoặc 4 giờ ở nhiệt độ phòng.",
        "black_box_warnings": (
            "BỆNH LÝ PHỔI KẼ (ILD) - có thể nghiêm trọng và đe dọa tính mạng. "
            "Có báo cáo tử vong do ILD. "
            "Cần theo dõi triệu chứng (khó thở, ho, sốt, đau ngực) và chức năng phổi. "
            "Ngừng trastuzumab deruxtecan ngay nếu nghi ngờ ILD và đánh giá. "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội. "
            "Ngừng trastuzumab deruxtecan nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa deruxtecan, tăng nồng độ",
                    "effect": "Tăng độc tính (đặc biệt bệnh lý phổi kẽ)",
                    "management": "Thận trọng. Có thể cần giảm liều trastuzumab deruxtecan."
                }
            ],
            "moderate": [
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa deruxtecan, giảm nồng độ",
                    "effect": "Giảm hiệu quả trastuzumab deruxtecan",
                    "management": "Thận trọng. Có thể cần tăng liều trastuzumab deruxtecan."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng trastuzumab deruxtecan hoặc bất kỳ thành phần nào",
                "Đang có nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Tiền sử bệnh lý phổi kẽ - tăng nguy cơ ILD",
                "Tiền sử nhiễm trùng tái phát",
                "Suy gan nặng - giảm chuyển hóa deruxtecan, tăng độc tính",
                "Suy thận nặng - giảm thải trừ, tăng độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Tránh dùng trong thai kỳ. Nếu cần dùng, thông báo rõ ràng về nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Tránh dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "Deruxtecan chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ deruxtecan, tăng độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ bệnh lý phổi kẽ nặng",
                "Tăng nguy cơ giảm bạch cầu/tiểu cầu nặng",
                "Tăng nguy cơ nhiễm trùng",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Đánh giá bệnh lý phổi kẽ (X-quang ngực, CT scan ngực)",
                "Điều trị ILD nếu có (corticosteroid, hỗ trợ hô hấp nếu cần)",
                "Hỗ trợ tế bào máu nếu cần (G-CSF, truyền tiểu cầu, truyền máu)",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chức năng gan"
            ],
            "monitoring": "Bệnh lý phổi kẽ, số lượng tế bào máu, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong 30-90 phút (tùy liều).",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền, đặc biệt dấu hiệu bệnh lý phổi kẽ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Trastuzumab deruxtecan (Enhertu)",
                "UpToDate - Trastuzumab deruxtecan: Drug information",
                "Lexicomp - Trastuzumab deruxtecan monograph",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in HER2+ and HER2-low breast cancer"
        }
    },

    "Tivdak": {
        "group": "FDA Approved 9/20/2021",
        "vietnamese_name": "Tisotumab vedotin, Tivdak",
        "administration": ["IV"],
        "indications": [
            "Ung thư cổ tử cung tái phát hoặc di căn đã tiến triển sau hóa trị",
            "Cervical cancer với disease progression on or after chemotherapy"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tisotumab vedotin hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Xuất huyết nặng - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Có thai - CHỐNG CHỈ ĐỊNH (category D)"
            ]
        },
        "dosage": {
            "adult_standard": "2mg/kg IV mỗi 3 tuần",
            "notes": "Truyền tĩnh mạch trong 30 phút. Tisotumab vedotin là ADC (antibody-drug conjugate) cho ung thư cổ tử cung. FDA phê duyệt 9/20/2021."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Xuất huyết - phổ biến, có thể nghiêm trọng",
            "Giảm bạch cầu (neutropenia) - phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Giảm hồng cầu (anemia) - phổ biến",
            "Mệt mỏi - phổ biến",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Phản ứng truyền (infusion-related reactions) - không phổ biến",
            "Bệnh lý thần kinh ngoại biên (peripheral neuropathy) - phổ biến",
            "Rụng tóc - phổ biến"
        ],
        "interactions": [
            "Thuốc chống đông (warfarin, heparin): tăng nguy cơ xuất huyết",
            "Thuốc ức chế CYP3A4: có thể tăng nồng độ monomethyl auristatin E (MMAE)"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Tisotumab vedotin là antibody-drug conjugate (ADC) gồm: (1) Tisotumab - kháng thể đơn dòng kháng tissue factor (TF), (2) Vedotin - liên kết với monomethyl auristatin E (MMAE), một chất ức chế microtubule. Tissue factor (TF) được biểu hiện cao trên tế bào ung thư cổ tử cung. Tisotumab vedotin gắn với TF trên tế bào ung thư → nội hóa vào tế bào → giải phóng MMAE → MMAE ức chế microtubule → ngăn chặn phân chia tế bào → gây chết tế bào ung thư. ĐẶC ĐIỂM: (1) ADC kháng TF cho ung thư cổ tử cung, (2) XUẤT HUYẾT - phổ biến, có thể nghiêm trọng, (3) Giảm tế bào máu (neutropenia, thrombocytopenia, anemia) - phổ biến, (4) Bệnh lý thần kinh ngoại biên - phổ biến, (5) Truyền tĩnh mạch trong 30 phút, (6) FDA phê duyệt 9/20/2021.",
        "monitoring": [
            "XUẤT HUYẾT - phổ biến, có thể nghiêm trọng - theo dõi dấu hiệu chảy máu - QUAN TRỌNG",
            "CBC: giảm bạch cầu, giảm tiểu cầu, giảm hồng cầu - phổ biến",
            "Chức năng gan: ALT, AST (tăng men gan phổ biến)",
            "Bệnh lý thần kinh ngoại biên - phổ biến, theo dõi triệu chứng",
            "Phản ứng truyền - theo dõi trong và sau truyền",
            "Đáp ứng điều trị: CT scan mỗi 6-9 tuần"
        ],
        "precautions": [
            "XUẤT HUYẾT - phổ biến, có thể nghiêm trọng. Theo dõi dấu hiệu chảy máu. Ngừng tạm thời nếu xuất huyết nặng.",
            "GIẢM TẾ BÀO MÁU - phổ biến. Theo dõi CBC định kỳ. Có thể cần hỗ trợ G-CSF, truyền máu.",
            "BỆNH LÝ THẦN KINH NGOẠI BIÊN - phổ biến. Theo dõi triệu chứng. Có thể cần giảm liều hoặc ngừng tạm thời.",
            "Tăng men gan - phổ biến. Theo dõi chức năng gan.",
            "Phản ứng truyền - theo dõi trong và sau truyền",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ (category D)",
            "Truyền tĩnh mạch trong 30 phút"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 4 ngày",
            "onset": "Vài tuần (tác dụng lâm sàng)",
            "duration": "3 tuần (chu kỳ)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, MMAE chuyển hóa qua CYP3A4",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Bảo vệ khỏi ánh sáng.",
        "black_box_warnings": "XUẤT HUYẾT - có thể gây xuất huyết nghiêm trọng, có thể tử vong. Theo dõi dấu hiệu chảy máu. Ngừng tạm thời nếu xuất huyết nặng. CHỐNG CHỈ ĐỊNH trong thai kỳ (category D).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc chống đông (Warfarin, Heparin, DOACs)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ xuất huyết",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ. Có thể cần ngừng tạm thời thuốc chống đông."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 Inhibitors (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ MMAE",
                    "effect": "Tăng nồng độ MMAE, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều tisotumab vedotin."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng tisotumab vedotin hoặc bất kỳ thành phần nào",
                "Có thai (category D) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Xuất huyết nặng đang hoạt động - tăng nguy cơ xuất huyết",
                "Suy gan nặng - thận trọng, có thể tăng độc tính",
                "Suy thận nặng - thận trọng, dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Tisotumab vedotin là FDA category D - có nguy cơ cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Tisotumab vedotin có thể bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Tisotumab vedotin chuyển hóa qua hệ thống RES, MMAE chuyển hóa qua CYP3A4. Suy gan có thể làm tăng độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Xuất huyết nặng",
                "Giảm tế bào máu nặng (neutropenia, thrombocytopenia, anemia)",
                "Bệnh lý thần kinh ngoại biên nặng",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay tisotumab vedotin",
                "Nếu xuất huyết nặng: truyền máu, huyết tương, điều trị hỗ trợ",
                "Nếu giảm tế bào máu nặng: G-CSF, truyền máu, huyết tương",
                "Theo dõi chức năng gan",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, xuất huyết, CBC, chức năng gan, bệnh lý thần kinh cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng theo hướng dẫn",
                "infusion_rate": "Truyền tĩnh mạch trong 30 phút",
                "premedication": "Có thể cần premedication (corticosteroid, antihistamine) để giảm phản ứng truyền",
                "notes": "Truyền tĩnh mạch 2mg/kg trong 30 phút mỗi 3 tuần. Theo dõi phản ứng truyền trong và sau truyền. QUAN TRỌNG: (1) Theo dõi xuất huyết, (2) Theo dõi CBC, (3) Theo dõi bệnh lý thần kinh ngoại biên."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tisotumab vedotin (Tivdak)",
                "FDA Approval Date: 9/20/2021",
                "FDA-approved use: To treat recurrent or metastatic cervical cancer with disease progression on or after chemotherapy",
                "UpToDate - Tisotumab vedotin: Drug information",
                "NCCN Guidelines - Cervical Cancer Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 9/20/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": True,
            "organ_toxicity": ["Hematologic (neutropenia, thrombocytopenia, anemia) - common", "Hepatic (elevated liver enzymes) - common", "Neurologic (peripheral neuropathy) - common"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Bleeding signs - CRITICAL", "CBC (neutropenia, thrombocytopenia, anemia) - CRITICAL", "Peripheral neuropathy - CRITICAL", "Liver function (ALT, AST)", "Infusion reactions", "Treatment response (CT scan every 6-9 weeks)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Tisotumab vedotin and Bleeding",
            "NCCN Guidelines - Cervical Cancer Treatment",
            "FDA Drug Information - Tisotumab vedotin (Tivdak)"
        ],
        "last_updated": "2025-02-18"
    },

    "Zynlonta": {
        "group": "FDA Approved 4/23/2021",
        "vietnamese_name": "Loncastuximab tesirine, Zynlonta",
        "administration": ["IV"],
        "indications": [
            "U lympho tế bào B lớn tái phát hoặc kháng trị (relapsed or refractory large B-cell lymphoma)",
            "Large B-cell lymphoma đã điều trị trước đó với ít nhất 2 phác đồ"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng loncastuximab tesirine hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Giảm tế bào máu nặng - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Có thai - CHỐNG CHỈ ĐỊNH (category D)"
            ]
        },
        "dosage": {
            "adult_cycle1": "0.15mg/kg IV ngày 1, sau đó 0.075mg/kg IV ngày 8 và 15 (chu kỳ 21 ngày)",
            "adult_cycle2plus": "0.075mg/kg IV ngày 1 và 8 (chu kỳ 21 ngày)",
            "notes": "Truyền tĩnh mạch trong 30 phút. Loncastuximab tesirine là ADC (antibody-drug conjugate) cho large B-cell lymphoma. FDA phê duyệt 4/23/2021."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Giảm bạch cầu (neutropenia) - phổ biến, có thể nghiêm trọng",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến, có thể nghiêm trọng",
            "Giảm hồng cầu (anemia) - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Phát ban (rash) - phổ biến",
            "Mệt mỏi - phổ biến",
            "Buồn nôn - phổ biến",
            "Phản ứng truyền (infusion-related reactions) - không phổ biến",
            "Bệnh lý thần kinh ngoại biên (peripheral neuropathy) - không phổ biến",
            "Hội chứng giải phóng cytokine (CRS) - hiếm"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4: có thể tăng nồng độ SG3199 (payload)"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Loncastuximab tesirine là antibody-drug conjugate (ADC) gồm: (1) Loncastuximab - kháng thể đơn dòng kháng CD19, (2) Tesirine - liên kết với SG3199 (pyrrolobenzodiazepine dimer - PBD), một chất gây tổn thương DNA. CD19 được biểu hiện cao trên tế bào B, bao gồm tế bào u lympho tế bào B lớn. Loncastuximab tesirine gắn với CD19 trên tế bào u lympho → nội hóa vào tế bào → giải phóng SG3199 → SG3199 gây tổn thương DNA → ngăn chặn tổng hợp DNA và RNA → gây chết tế bào ung thư. ĐẶC ĐIỂM: (1) ADC kháng CD19 cho large B-cell lymphoma, (2) Giảm tế bào máu (neutropenia, thrombocytopenia, anemia) - phổ biến, có thể nghiêm trọng, (3) Tăng men gan - phổ biến, (4) Phát ban - phổ biến, (5) Truyền tĩnh mạch trong 30 phút, (6) FDA phê duyệt 4/23/2021.",
        "monitoring": [
            "CBC: giảm bạch cầu, giảm tiểu cầu, giảm hồng cầu - phổ biến, có thể nghiêm trọng - QUAN TRỌNG",
            "Chức năng gan: ALT, AST (tăng men gan phổ biến)",
            "Phát ban - phổ biến",
            "Phản ứng truyền - theo dõi trong và sau truyền",
            "Bệnh lý thần kinh ngoại biên - không phổ biến",
            "Đáp ứng điều trị: CT scan mỗi 2-3 chu kỳ"
        ],
        "precautions": [
            "GIẢM TẾ BÀO MÁU - phổ biến, có thể nghiêm trọng. Theo dõi CBC định kỳ. Có thể cần hỗ trợ G-CSF, truyền máu, huyết tương.",
            "Tăng men gan - phổ biến. Theo dõi chức năng gan định kỳ.",
            "Phát ban - phổ biến. Điều trị triệu chứng.",
            "Phản ứng truyền - theo dõi trong và sau truyền",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ (category D)",
            "Truyền tĩnh mạch trong 30 phút",
            "Chu kỳ 21 ngày: chu kỳ 1 (0.15mg/kg ngày 1, 0.075mg/kg ngày 8,15), chu kỳ 2+ (0.075mg/kg ngày 1,8)"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 12-14 ngày",
            "onset": "Vài tuần đến vài tháng (tác dụng lâm sàng)",
            "duration": "21 ngày (chu kỳ)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, SG3199 chuyển hóa qua CYP3A4",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Bảo vệ khỏi ánh sáng.",
        "black_box_warnings": "GIẢM TẾ BÀO MÁU - có thể gây giảm bạch cầu, giảm tiểu cầu nghiêm trọng. Theo dõi CBC định kỳ. Có thể cần hỗ trợ G-CSF, truyền máu. CHỐNG CHỈ ĐỊNH trong thai kỳ (category D).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ SG3199",
                    "effect": "Tăng nồng độ SG3199, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều loncastuximab tesirine."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng loncastuximab tesirine hoặc bất kỳ thành phần nào",
                "Có thai (category D) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Giảm tế bào máu nặng đang hoạt động - tăng nguy cơ",
                "Suy gan nặng - thận trọng, có thể tăng độc tính",
                "Suy thận nặng - thận trọng, dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Loncastuximab tesirine là FDA category D - có nguy cơ cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Loncastuximab tesirine có thể bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Loncastuximab tesirine chuyển hóa qua hệ thống RES, SG3199 chuyển hóa qua CYP3A4. Suy gan có thể làm tăng độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm tế bào máu nặng (neutropenia, thrombocytopenia, anemia)",
                "Tăng men gan nặng",
                "Phản ứng truyền nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay loncastuximab tesirine",
                "Nếu giảm tế bào máu nặng: G-CSF, truyền máu, huyết tương",
                "Theo dõi chức năng gan",
                "Điều trị phản ứng truyền nếu có",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, CBC, chức năng gan, phản ứng truyền cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng theo hướng dẫn",
                "infusion_rate": "Truyền tĩnh mạch trong 30 phút",
                "premedication": "Có thể cần premedication (corticosteroid, antihistamine) để giảm phản ứng truyền",
                "notes": "Truyền tĩnh mạch trong 30 phút. Chu kỳ 21 ngày: chu kỳ 1 (0.15mg/kg ngày 1, 0.075mg/kg ngày 8,15), chu kỳ 2+ (0.075mg/kg ngày 1,8). Theo dõi phản ứng truyền trong và sau truyền. QUAN TRỌNG: (1) Theo dõi CBC, (2) Theo dõi chức năng gan, (3) Theo dõi phát ban."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Loncastuximab tesirine (Zynlonta)",
                "FDA Approval Date: 4/23/2021",
                "FDA-approved use: To treat certain types of relapsed or refractory large B-cell lymphoma",
                "UpToDate - Loncastuximab tesirine: Drug information",
                "NCCN Guidelines - Large B-cell Lymphoma Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 4/23/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hematologic (neutropenia, thrombocytopenia, anemia) - common, can be severe - CRITICAL", "Hepatic (elevated liver enzymes) - common"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (neutropenia, thrombocytopenia, anemia) - CRITICAL", "Liver function (ALT, AST) - CRITICAL", "Rash - common", "Infusion reactions", "Treatment response (CT scan every 2-3 cycles)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Loncastuximab tesirine and Hematologic Toxicity",
            "NCCN Guidelines - Large B-cell Lymphoma Treatment",
            "FDA Drug Information - Loncastuximab tesirine (Zynlonta)"
        ],
        "last_updated": "2025-02-18"
    },





    "Elahere": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Mirvetuximab, Elahere",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat patients with recurrent ovarian cancer that is resistant to platinum therapy",
                ],
                "contraindications": [
                        "Dị ứng mirvetuximab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2022. To treat patients with recurrent ovarian cancer that is resistant to platinum therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Mirvetuximab được FDA phê duyệt 2022 để to treat patients with recurrent ovarian cancer that is resistant to platinum therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng mirvetuximab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng mirvetuximab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Mirvetuximab (Elahere)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat patients with recurrent ovarian cancer that is resistant to platinum therapy",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Mirvetuximab (Elahere)",
                ],
                "last_updated": "2026-01-15",
        },
    "Imjudo": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Tremelimumab, Imjudo",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat unresectable hepatocellular carcinoma",
                ],
                "contraindications": [
                        "Dị ứng tremelimumab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2022. To treat unresectable hepatocellular carcinoma",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Tremelimumab được FDA phê duyệt 2022 để to treat unresectable hepatocellular carcinoma. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng tremelimumab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng tremelimumab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Tremelimumab (Imjudo)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat unresectable hepatocellular carcinoma",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Tremelimumab (Imjudo)",
                ],
                "last_updated": "2026-01-15",
        },
    "Lunsumio": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Mosunetuzumab, Lunsumio",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat adults with relapsed or refractory follicular lymphoma, a type of non-Hodgkin lymphoma",
                ],
                "contraindications": [
                        "Dị ứng mosunetuzumab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2022. To treat adults with relapsed or refractory follicular lymphoma, a type of non-Hodgkin lymphoma",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Mosunetuzumab được FDA phê duyệt 2022 để to treat adults with relapsed or refractory follicular lymphoma, a type of non-hodgkin lymphoma. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng mosunetuzumab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng mosunetuzumab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Mosunetuzumab (Lunsumio)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat adults with relapsed or refractory follicular lymphoma, a type of non-Hodgkin lymphoma",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Mosunetuzumab (Lunsumio)",
                ],
                "last_updated": "2026-01-15",
        },
    "Opdualag": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Nivolumab, Opdualag",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat unresectable or metastatic melanoma",
                ],
                "contraindications": [
                        "Dị ứng nivolumab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2022. To treat unresectable or metastatic melanoma",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Nivolumab được FDA phê duyệt 2022 để to treat unresectable or metastatic melanoma. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng nivolumab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng nivolumab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Nivolumab (Opdualag)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat unresectable or metastatic melanoma",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Nivolumab (Opdualag)",
                ],
                "last_updated": "2026-01-15",
        },
    "Tecvayli": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Teclistamab, Tecvayli",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat relapsed or refractory multiple myeloma among adults who have received at least four specific lines of therapy",
                ],
                "contraindications": [
                        "Dị ứng teclistamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2022. To treat relapsed or refractory multiple myeloma among adults who have received at least four specific lines of therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Teclistamab được FDA phê duyệt 2022 để to treat relapsed or refractory multiple myeloma among adults who have received at least four specific lines of therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng teclistamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng teclistamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Teclistamab (Tecvayli)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat relapsed or refractory multiple myeloma among adults who have received at least four specific lines of therapy",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Teclistamab (Tecvayli)",
                ],
                "last_updated": "2026-01-15",
        },
    "Columvi": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Glofitamab, Columvi",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat diffuse large B-cell lymphoma, not otherwise specified, or large B-cell lymphoma arising from follicular lymphoma after two or more lines of systemic therapy",
                ],
                "contraindications": [
                        "Dị ứng glofitamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat diffuse large B-cell lymphoma, not otherwise specified, or large B-cell lymphoma arising from follicular lymphoma after two or more lines of systemic therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Glofitamab được FDA phê duyệt 2023 để to treat diffuse large b-cell lymphoma, not otherwise specified, or large b-cell lymphoma arising from follicular lymphoma after two or more lines of systemic therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng glofitamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng glofitamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Glofitamab (Columvi)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat diffuse large B-cell lymphoma, not otherwise specified, or large B-cell lymphoma arising from follicular lymphoma after two or more lines of systemic therapy",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Glofitamab (Columvi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Elrexfio": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Elranatamab, Elrexfio",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat adults with relapsed or refractory multiple myeloma who have received at least four prior lines of therapy",
                ],
                "contraindications": [
                        "Dị ứng elranatamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat adults with relapsed or refractory multiple myeloma who have received at least four prior lines of therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Elranatamab được FDA phê duyệt 2023 để to treat adults with relapsed or refractory multiple myeloma who have received at least four prior lines of therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng elranatamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng elranatamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Elranatamab (Elrexfio)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat adults with relapsed or refractory multiple myeloma who have received at least four prior lines of therapy",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Elranatamab (Elrexfio)",
                ],
                "last_updated": "2026-01-15",
        },
    "Epkinly": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Epcoritamab, Epkinly",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat relapsed or refractory diffuse large B-cell lymphoma (not otherwise specified) and high-grade B-cell lymphoma after two or more lines of systemic therapy",
                ],
                "contraindications": [
                        "Dị ứng epcoritamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat relapsed or refractory diffuse large B-cell lymphoma (not otherwise specified) and high-grade B-cell lymphoma after two or more lines of systemic therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Epcoritamab được FDA phê duyệt 2023 để to treat relapsed or refractory diffuse large b-cell lymphoma (not otherwise specified) and high-grade b-cell lymphoma after two or more lines of systemic therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng epcoritamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng epcoritamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Epcoritamab (Epkinly)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat relapsed or refractory diffuse large B-cell lymphoma (not otherwise specified) and high-grade B-cell lymphoma after two or more lines of systemic therapy",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Epcoritamab (Epkinly)",
                ],
                "last_updated": "2026-01-15",
        },
    "Loqtorzi": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Toripalimab, Loqtorzi",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat recurrent or metastatic nasopharyngeal carcinoma when used together with or following other therapies",
                ],
                "contraindications": [
                        "Dị ứng toripalimab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat recurrent or metastatic nasopharyngeal carcinoma when used together with or following other therapies",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Toripalimab được FDA phê duyệt 2023 để to treat recurrent or metastatic nasopharyngeal carcinoma when used together with or following other therapies. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng toripalimab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng toripalimab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Toripalimab (Loqtorzi)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat recurrent or metastatic nasopharyngeal carcinoma when used together with or following other therapies",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Toripalimab (Loqtorzi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Talvey": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Talquetamab, Talvey",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat adults with relapsed or refractory multiple myeloma who have received at least four prior therapies",
                ],
                "contraindications": [
                        "Dị ứng talquetamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat adults with relapsed or refractory multiple myeloma who have received at least four prior therapies",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Talquetamab được FDA phê duyệt 2023 để to treat adults with relapsed or refractory multiple myeloma who have received at least four prior therapies. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng talquetamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng talquetamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Talquetamab (Talvey)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat adults with relapsed or refractory multiple myeloma who have received at least four prior therapies",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Talquetamab (Talvey)",
                ],
                "last_updated": "2026-01-15",
        },
    "Zynyz": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Retifanlimab, Zynyz",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat metastatic or recurrent locally advanced Merkel cell carcinoma",
                ],
                "contraindications": [
                        "Dị ứng retifanlimab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat metastatic or recurrent locally advanced Merkel cell carcinoma",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Retifanlimab được FDA phê duyệt 2023 để to treat metastatic or recurrent locally advanced merkel cell carcinoma. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng retifanlimab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng retifanlimab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Retifanlimab (Zynyz)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat metastatic or recurrent locally advanced Merkel cell carcinoma",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Retifanlimab (Zynyz)",
                ],
                "last_updated": "2026-01-15",
        },
    "Bizengri": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Zenocutuzumab, Bizengri",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat non-small cell lung cancer and pancreatic adenocarcinoma",
                ],
                "contraindications": [
                        "Dị ứng zenocutuzumab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat non-small cell lung cancer and pancreatic adenocarcinoma",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Zenocutuzumab được FDA phê duyệt 2024 để to treat non-small cell lung cancer and pancreatic adenocarcinoma. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng zenocutuzumab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng zenocutuzumab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Zenocutuzumab (Bizengri)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat non-small cell lung cancer and pancreatic adenocarcinoma",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Zenocutuzumab (Bizengri)",
                ],
                "last_updated": "2026-01-15",
        },
    "Imdelltra": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Tarlatamab, Imdelltra",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat extensive stage small cell lung cancer",
                ],
                "contraindications": [
                        "Dị ứng tarlatamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat extensive stage small cell lung cancer",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Tarlatamab được FDA phê duyệt 2024 để to treat extensive stage small cell lung cancer. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng tarlatamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng tarlatamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Tarlatamab (Imdelltra)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat extensive stage small cell lung cancer",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Tarlatamab (Imdelltra)",
                ],
                "last_updated": "2026-01-15",
        },
    "Tevimbra": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Tislelizumab, Tevimbra",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat unresectable or metastatic esophageal squamous cell carcinoma",
                ],
                "contraindications": [
                        "Dị ứng tislelizumab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat unresectable or metastatic esophageal squamous cell carcinoma",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Tislelizumab được FDA phê duyệt 2024 để to treat unresectable or metastatic esophageal squamous cell carcinoma. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng tislelizumab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng tislelizumab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Tislelizumab (Tevimbra)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat unresectable or metastatic esophageal squamous cell carcinoma",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Tislelizumab (Tevimbra)",
                ],
                "last_updated": "2026-01-15",
        },
    "Unloxcyt": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Cosibelimab, Unloxcyt",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat cutaneous squamous cell carcinoma",
                ],
                "contraindications": [
                        "Dị ứng cosibelimab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat cutaneous squamous cell carcinoma",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Cosibelimab được FDA phê duyệt 2024 để to treat cutaneous squamous cell carcinoma. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng cosibelimab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng cosibelimab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Cosibelimab (Unloxcyt)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat cutaneous squamous cell carcinoma",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Cosibelimab (Unloxcyt)",
                ],
                "last_updated": "2026-01-15",
        },
    "Vyloy": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Zolbetuximab, Vyloy",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat gastric or gastroesophageal junction adenocarcinoma",
                ],
                "contraindications": [
                        "Dị ứng zolbetuximab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat gastric or gastroesophageal junction adenocarcinoma",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Zolbetuximab được FDA phê duyệt 2024 để to treat gastric or gastroesophageal junction adenocarcinoma. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng zolbetuximab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng zolbetuximab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Zolbetuximab (Vyloy)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat gastric or gastroesophageal junction adenocarcinoma",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Zolbetuximab (Vyloy)",
                ],
                "last_updated": "2026-01-15",
        },
    "Ziihera": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Zanidatamab, Ziihera",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat unresectable or metastatic HER2-positive (IHC 3+) biliary tract cancer",
                ],
                "contraindications": [
                        "Dị ứng zanidatamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat unresectable or metastatic HER2-positive (IHC 3+) biliary tract cancer",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Zanidatamab được FDA phê duyệt 2024 để to treat unresectable or metastatic her2-positive (ihc 3+) biliary tract cancer. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng zanidatamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng zanidatamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Zanidatamab (Ziihera)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat unresectable or metastatic HER2-positive (IHC 3+) biliary tract cancer",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Zanidatamab (Ziihera)",
                ],
                "last_updated": "2026-01-15",
        },
    "Datroway": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Datopotamab, Datroway",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat unresectable or metastatic, HR-positive, HER2-negative breast cancer who have received prior endocrine-based therapy and chemotherapy for unresectable or metastatic disease",
                ],
                "contraindications": [
                        "Dị ứng datopotamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat unresectable or metastatic, HR-positive, HER2-negative breast cancer who have received prior endocrine-based therapy and chemotherapy for unresectable or metastatic disease",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Datopotamab được FDA phê duyệt 2025 để to treat unresectable or metastatic, hr-positive, her2-negative breast cancer who have received prior endocrine-based therapy and chemotherapy for unresectable or metastatic disease. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng datopotamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng datopotamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Datopotamab (Datroway)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat unresectable or metastatic, HR-positive, HER2-negative breast cancer who have received prior endocrine-based therapy and chemotherapy for unresectable or metastatic disease",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Datopotamab (Datroway)",
                ],
                "last_updated": "2026-01-15",
        },
    "Emrelis": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Telisotuzumab, Emrelis",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat locally advanced or metastatic, non-squamous non-small cell lung cancer (NSCLC) with high c-Met protein overexpression after prior systemic therapy",
                ],
                "contraindications": [
                        "Dị ứng telisotuzumab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat locally advanced or metastatic, non-squamous non-small cell lung cancer (NSCLC) with high c-Met protein overexpression after prior systemic therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Telisotuzumab được FDA phê duyệt 2025 để to treat locally advanced or metastatic, non-squamous non-small cell lung cancer (nsclc) with high c-met protein overexpression after prior systemic therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng telisotuzumab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng telisotuzumab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Telisotuzumab (Emrelis)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat locally advanced or metastatic, non-squamous non-small cell lung cancer (NSCLC) with high c-Met protein overexpression after prior systemic therapy",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Telisotuzumab (Emrelis)",
                ],
                "last_updated": "2026-01-15",
        },
    "KeytrudaQlex": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Pembrolizumab, Keytruda Qlex",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat adult and pediatric (12 years and older) solid tumor indications approved for the intravenous formulation of pembrolizumab",
                ],
                "contraindications": [
                        "Dị ứng pembrolizumab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat adult and pediatric (12 years and older) solid tumor indications approved for the intravenous formulation of pembrolizumab",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Pembrolizumab được FDA phê duyệt 2025 để to treat adult and pediatric (12 years and older) solid tumor indications approved for the intravenous formulation of pembrolizumab. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng pembrolizumab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng pembrolizumab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Pembrolizumab (Keytruda Qlex)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat adult and pediatric (12 years and older) solid tumor indications approved for the intravenous formulation of pembrolizumab",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Pembrolizumab (Keytruda Qlex)",
                ],
                "last_updated": "2026-01-15",
        },
    "Lynozyfic": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Linvoseltamab, Lynozyfic",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat relapsed or refractory multiple myeloma after at least four prior lines of therapy, including a proteasome inhibitor, an immunomodulatory agent, and an anti CD38 monoclonal antibody",
                ],
                "contraindications": [
                        "Dị ứng linvoseltamab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat relapsed or refractory multiple myeloma after at least four prior lines of therapy, including a proteasome inhibitor, an immunomodulatory agent, and an anti CD38 monoclonal antibody",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Linvoseltamab được FDA phê duyệt 2025 để to treat relapsed or refractory multiple myeloma after at least four prior lines of therapy, including a proteasome inhibitor, an immunomodulatory agent, and an anti cd38 monoclonal antibody. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng linvoseltamab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng linvoseltamab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Linvoseltamab (Lynozyfic)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat relapsed or refractory multiple myeloma after at least four prior lines of therapy, including a proteasome inhibitor, an immunomodulatory agent, and an anti CD38 monoclonal antibody",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Linvoseltamab (Lynozyfic)",
                ],
                "last_updated": "2026-01-15",
        },
    "penpulimabkcqx": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Penpulimab, penpulimab-kcqx",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "In combination with either cisplatin or carboplatin and gemcitabine, to treat adults with recurrent or metastatic non-keratinizing nasopharyngeal carcinoma (NPC), or as a single agent while on or after platinum-based chemotherapy and at least one other prior line of therapy",
                ],
                "contraindications": [
                        "Dị ứng penpulimab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. In combination with either cisplatin or carboplatin and gemcitabine, to treat adults with recurrent or metastatic non-keratinizing nasopharyngeal carcinoma (NPC), or as a single agent while on or after platinum-based chemotherapy and at least one other prior line of therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Penpulimab được FDA phê duyệt 2025 để in combination with either cisplatin or carboplatin and gemcitabine, to treat adults with recurrent or metastatic non-keratinizing nasopharyngeal carcinoma (npc), or as a single agent while on or after platinum-based chemotherapy and at least one other prior line of therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng penpulimab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng penpulimab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Penpulimab (penpulimab-kcqx)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: In combination with either cisplatin or carboplatin and gemcitabine, to treat adults with recurrent or metastatic non-keratinizing nasopharyngeal carcinoma (NPC), or as a single agent while on or after platinum-based chemotherapy and at least one other prior line of therapy",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Penpulimab (penpulimab-kcqx)",
                ],
                "last_updated": "2026-01-15",
        },
}

__all__ = ['MONOCLONAL_ANTIBODIES_ADCS_DRUGS']

