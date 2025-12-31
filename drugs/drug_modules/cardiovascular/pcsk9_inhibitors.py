"""
PCSK9 Inhibitors (Proprotein Convertase Subtilisin/Kexin type 9 Inhibitors)
Nhóm thuốc mới hạ cholesterol - Thế hệ sau Statins
Alirocumab, Evolocumab, Inclisiran
"""

PCSK9_INHIBITORS = {
    "Alirocumab": {
        "group": "Cardiovascular - PCSK9 Inhibitor",
        "vietnamese_name": "Alirocumab, Praluent",
        "administration": ["SC"],
        "indications": [
            "Tăng cholesterol máu gia đình (Familial Hypercholesterolemia)",
            "Rối loạn lipid máu tiên phát",
            "Dự phòng biến cố tim mạch thứ phát (sau ACS, stroke)",
            "Bệnh động mạch vành",
            "Không đạt mục tiêu LDL-C với statin tối đa liều"
        ],
        "contraindications": [
            "Dị ứng với alirocumab",
            "Dị ứng với protein tái tổ hợp"
        ],
        "dosage": {
            "adult_sc_initial": "75mg SC mỗi 2 tuần",
            "adult_sc_high_ldl": "150mg SC mỗi 2 tuần (nếu LDL-C không đạt mục tiêu sau 4-8 tuần)",
            "adult_sc_alternative": "300mg SC mỗi 4 tuần (liều tương đương 150mg/2 tuần)",
            "notes": "Tiêm dưới da (bụng, đùi, hoặc cánh tay). Có thể tự tiêm sau khi được hướng dẫn. Điều chỉnh liều dựa trên LDL-C sau 4-8 tuần."
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng)",
            "Nhiễm trùng đường hô hấp trên",
            "Cúm",
            "Đau cơ",
            "Phản ứng dị ứng (hiếm)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Có thể dùng cùng với statin",
            "Có thể dùng cùng với ezetimibe",
            "Không có tương tác với CYP450",
            "Không có tương tác với warfarin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Monoclonal antibody ức chế PCSK9 (Proprotein Convertase Subtilisin/Kexin type 9). PCSK9 là protein tham gia vào quá trình thoái hóa thụ thể LDL trên bề mặt tế bào gan. Bằng cách ức chế PCSK9, alirocumab tăng số lượng thụ thể LDL trên bề mặt tế bào gan, dẫn đến tăng clearance LDL-C từ máu và giảm nồng độ LDL-C đáng kể (50-60%).",
        "monitoring": [
            "Lipid profile (LDL-C, HDL-C, TG, Total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "LFT (AST, ALT) trước điều trị và mỗi 6-12 tháng",
            "CK nếu có đau cơ",
            "Dấu hiệu phản ứng dị ứng tại chỗ tiêm",
            "Đánh giá đáp ứng: Mục tiêu LDL-C <70 mg/dL (hoặc <55 mg/dL nếu có bệnh tim mạch)"
        ],
        "precautions": [
            "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh",
            "Để ở nhiệt độ phòng 30 phút trước khi tiêm",
            "Không lắc",
            "Kiểm tra hạn sử dụng và màu sắc (phải trong suốt, không màu đến vàng nhạt)",
            "Thận trọng ở bệnh nhân suy gan nặng (chưa có dữ liệu đầy đủ)",
            "Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều)",
            "Có thể tự tiêm sau khi được hướng dẫn",
            "Luân phiên vị trí tiêm (bụng, đùi, cánh tay)"
        ],
        "pharmacokinetics": {
            "half_life": "17-20 ngày (rất dài)",
            "onset": "Giảm LDL-C trong 2-4 tuần",
            "duration": "2 tuần (liều 75-150mg) hoặc 4 tuần (liều 300mg)",
            "protein_binding": "N/A (monoclonal antibody)",
            "clearance": "Phân hủy bởi hệ thống reticuloendothelial (giống các protein khác)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh. Có thể bảo quản ở nhiệt độ phòng (≤25°C) tối đa 30 ngày. Tránh ánh sáng trực tiếp.",
        "black_box_warnings": "Không có",
        "drug_interactions": {
            "minor": [
                {
                    "drug": "Statin, Ezetimibe",
                    "mechanism": "Cơ chế khác nhau, có thể dùng cùng",
                    "effect": "Tăng hiệu quả giảm LDL-C (additive effect)",
                    "management": "Có thể dùng cùng để đạt mục tiêu LDL-C."
                }
            ]
        },
        "pregnancy_lactation": {
            "pregnancy_category": "B",
            "pregnancy_notes": "Chưa có dữ liệu đầy đủ về sử dụng trong thai kỳ. Chỉ dùng nếu lợi ích vượt trội nguy cơ.",
            "lactation": "Chưa biết có bài tiết vào sữa mẹ hay không. Thận trọng khi cho con bú."
        },
        "overdose_management": "Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.",
        "administration_instructions": "Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn.",
        "references": "FDA Label (Praluent), UpToDate - PCSK9 Inhibitors, AHA/ACC Guidelines 2018 - Cholesterol Management",
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },
    },
    
    "Evolocumab": {
        "group": "Cardiovascular - PCSK9 Inhibitor",
        "vietnamese_name": "Evolocumab, Repatha",
        "administration": ["SC"],
        "indications": [
            "Tăng cholesterol máu gia đình (Familial Hypercholesterolemia)",
            "Tăng cholesterol máu gia đình đồng hợp tử (HoFH)",
            "Rối loạn lipid máu tiên phát",
            "Dự phòng biến cố tim mạch thứ phát (sau ACS, stroke)",
            "Bệnh động mạch vành",
            "Không đạt mục tiêu LDL-C với statin tối đa liều"
        ],
        "contraindications": [
            "Dị ứng với evolocumab",
            "Dị ứng với protein tái tổ hợp"
        ],
        "dosage": {
            "adult_sc_standard": "140mg SC mỗi 2 tuần",
            "adult_sc_monthly": "420mg SC mỗi tháng (liều tương đương 140mg/2 tuần)",
            "adult_sc_hofh": "420mg SC mỗi tháng; có thể tăng lên 420mg mỗi 2 tuần nếu đang lọc huyết tương định kỳ",
            "notes": "Tiêm dưới da (bụng, đùi, hoặc cánh tay). Có thể tự tiêm sau khi được hướng dẫn."
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng)",
            "Nhiễm trùng đường hô hấp trên",
            "Cúm",
            "Đau lưng",
            "Đau cơ",
            "Phản ứng dị ứng (hiếm)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Có thể dùng cùng với statin",
            "Có thể dùng cùng với ezetimibe",
            "Không có tương tác với CYP450",
            "Không có tương tác với warfarin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Monoclonal antibody ức chế PCSK9 (Proprotein Convertase Subtilisin/Kexin type 9). PCSK9 là protein tham gia vào quá trình thoái hóa thụ thể LDL trên bề mặt tế bào gan. Bằng cách ức chế PCSK9, evolocumab tăng số lượng thụ thể LDL trên bề mặt tế bào gan, dẫn đến tăng clearance LDL-C từ máu và giảm nồng độ LDL-C đáng kể (50-60%). Tương tự alirocumab nhưng có chỉ định đặc biệt cho HoFH.",
        "monitoring": [
            "Lipid profile (LDL-C, HDL-C, TG, Total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "LFT (AST, ALT) trước điều trị và mỗi 6-12 tháng",
            "CK nếu có đau cơ",
            "Dấu hiệu phản ứng dị ứng tại chỗ tiêm",
            "Đánh giá đáp ứng: Mục tiêu LDL-C <70 mg/dL (hoặc <55 mg/dL nếu có bệnh tim mạch)",
            "Với HoFH: Đánh giá đáp ứng sau 12 tuần, có thể tăng liều nếu đang lọc huyết tương"
        ],
        "precautions": [
            "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh",
            "Để ở nhiệt độ phòng 30 phút trước khi tiêm",
            "Không lắc",
            "Kiểm tra hạn sử dụng và màu sắc (phải trong suốt, không màu đến vàng nhạt)",
            "Thận trọng ở bệnh nhân suy gan nặng (chưa có dữ liệu đầy đủ)",
            "Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều)",
            "Có thể tự tiêm sau khi được hướng dẫn",
            "Luân phiên vị trí tiêm (bụng, đùi, cánh tay)",
            "Với HoFH: Có thể tăng liều lên 420mg mỗi 2 tuần nếu đang lọc huyết tương định kỳ"
        ],
        "pharmacokinetics": {
            "half_life": "11-17 ngày (rất dài)",
            "onset": "Giảm LDL-C trong 2-4 tuần",
            "duration": "2 tuần (liều 140mg) hoặc 4 tuần (liều 420mg)",
            "protein_binding": "N/A (monoclonal antibody)",
            "clearance": "Phân hủy bởi hệ thống reticuloendothelial (giống các protein khác)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh. Có thể bảo quản ở nhiệt độ phòng (≤25°C) tối đa 30 ngày. Tránh ánh sáng trực tiếp.",
        "black_box_warnings": "Không có",
        "drug_interactions": {
            "minor": [
                {
                    "drug": "Statin, Ezetimibe",
                    "mechanism": "Cơ chế khác nhau, có thể dùng cùng",
                    "effect": "Tăng hiệu quả giảm LDL-C (additive effect)",
                    "management": "Có thể dùng cùng để đạt mục tiêu LDL-C."
                }
            ]
        },
        "pregnancy_lactation": {
            "pregnancy_category": "B",
            "pregnancy_notes": "Chưa có dữ liệu đầy đủ về sử dụng trong thai kỳ. Chỉ dùng nếu lợi ích vượt trội nguy cơ.",
            "lactation": "Chưa biết có bài tiết vào sữa mẹ hay không. Thận trọng khi cho con bú."
        },
        "overdose_management": "Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.",
        "administration_instructions": "Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn.",
        "references": "FDA Label (Repatha), UpToDate - PCSK9 Inhibitors, AHA/ACC Guidelines 2018 - Cholesterol Management",
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },
    },
    
    "Inclisiran": {
        "group": "Cardiovascular - PCSK9 Inhibitor (siRNA)",
        "vietnamese_name": "Inclisiran, Leqvio",
        "administration": ["SC"],
        "indications": [
            "Tăng cholesterol máu gia đình (Familial Hypercholesterolemia)",
            "Rối loạn lipid máu tiên phát",
            "Dự phòng biến cố tim mạch thứ phát",
            "Bệnh động mạch vành",
            "Không đạt mục tiêu LDL-C với statin tối đa liều"
        ],
        "contraindications": [
            "Dị ứng với inclisiran",
            "Dị ứng với các thành phần khác"
        ],
        "dosage": {
            "adult_sc_initial": "284mg SC × 1 liều",
            "adult_sc_3months": "284mg SC sau 3 tháng",
            "adult_sc_maintenance": "284mg SC mỗi 6 tháng (sau liều thứ 2)",
            "notes": "Tiêm dưới da (bụng, đùi, hoặc cánh tay). Liều đầu tiên, sau đó liều thứ 2 sau 3 tháng, sau đó mỗi 6 tháng. Có thể tự tiêm sau khi được hướng dẫn."
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng)",
            "Nhiễm trùng đường hô hấp trên",
            "Viêm khớp",
            "Đau cơ",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Có thể dùng cùng với statin",
            "Có thể dùng cùng với ezetimibe",
            "Không có tương tác với CYP450",
            "Không có tương tác với warfarin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Small interfering RNA (siRNA) ức chế tổng hợp PCSK9 ở mức RNA. Khác với alirocumab và evolocumab (monoclonal antibodies ức chế PCSK9 protein), inclisiran ức chế tổng hợp PCSK9 ở mức gene, dẫn đến giảm nồng độ PCSK9 và tăng số lượng thụ thể LDL trên bề mặt tế bào gan. Kết quả: Giảm LDL-C 50-60% với liều mỗi 6 tháng (tiện lợi hơn so với mỗi 2 tuần).",
        "monitoring": [
            "Lipid profile (LDL-C, HDL-C, TG, Total cholesterol) sau 3 tháng (sau liều thứ 2), sau đó mỗi 6 tháng",
            "LFT (AST, ALT) trước điều trị và mỗi 6-12 tháng",
            "CK nếu có đau cơ",
            "Dấu hiệu phản ứng dị ứng tại chỗ tiêm",
            "Đánh giá đáp ứng: Mục tiêu LDL-C <70 mg/dL (hoặc <55 mg/dL nếu có bệnh tim mạch)"
        ],
        "precautions": [
            "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh",
            "Để ở nhiệt độ phòng 30 phút trước khi tiêm",
            "Không lắc",
            "Kiểm tra hạn sử dụng và màu sắc",
            "Thận trọng ở bệnh nhân suy gan nặng (chưa có dữ liệu đầy đủ)",
            "Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều)",
            "Có thể tự tiêm sau khi được hướng dẫn",
            "Luân phiên vị trí tiêm (bụng, đùi, cánh tay)",
            "Ưu điểm: Liều mỗi 6 tháng (tiện lợi hơn so với mỗi 2 tuần)"
        ],
        "pharmacokinetics": {
            "half_life": "N/A (siRNA, không phải protein)",
            "onset": "Giảm LDL-C trong 2-4 tuần",
            "duration": "6 tháng (sau liều thứ 2)",
            "protein_binding": "N/A (siRNA)",
            "clearance": "Phân hủy bởi hệ thống nội bào"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), không đông lạnh. Có thể bảo quản ở nhiệt độ phòng (≤25°C) tối đa 30 ngày. Tránh ánh sáng trực tiếp.",
        "black_box_warnings": "Không có",
        "drug_interactions": {
            "minor": [
                {
                    "drug": "Statin, Ezetimibe",
                    "mechanism": "Cơ chế khác nhau, có thể dùng cùng",
                    "effect": "Tăng hiệu quả giảm LDL-C (additive effect)",
                    "management": "Có thể dùng cùng để đạt mục tiêu LDL-C."
                }
            ]
        },
        "pregnancy_lactation": {
            "pregnancy_category": "B",
            "pregnancy_notes": "Chưa có dữ liệu đầy đủ về sử dụng trong thai kỳ. Chỉ dùng nếu lợi ích vượt trội nguy cơ.",
            "lactation": "Chưa biết có bài tiết vào sữa mẹ hay không. Thận trọng khi cho con bú."
        },
        "overdose_management": "Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.",
        "administration_instructions": "Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn. Lịch tiêm: Liều đầu tiên, sau đó liều thứ 2 sau 3 tháng, sau đó mỗi 6 tháng.",
        "references": "FDA Label (Leqvio), UpToDate - PCSK9 Inhibitors, AHA/ACC Guidelines 2018 - Cholesterol Management",
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },
    },
}

