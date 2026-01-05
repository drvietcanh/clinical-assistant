"""
Anemia Drugs (Thuốc điều trị thiếu máu)
Bao gồm: Iron supplements, Erythropoietin
"""

ANEMIA_DRUGS = {
    "Ferrous Sulfate": {
        "group": "Hematology - Iron Supplement (Oral)",
        "vietnamese_name": "Ferrous Sulfate, Sắt sulfat",
        "brand_names": {
            "common": ["Feosol", "Fer-In-Sol"],
            "vietnam": ["Ferrous Sulfate 200mg", "Tardyferon"]
        },
        "administration": ["PO"],
        "indications": [
            "Thiếu máu do thiếu sắt (Iron Deficiency Anemia)",
            "Dự phòng thiếu sắt trong thai kỳ"
        ],
        "dosage": {
            "treatment": "60-120mg sắt nguyên tố/ngày (tương đương 300-600mg Ferrous Sulfate), chia 1-3 lần.",
            "prophylaxis_pregnancy": "30-60mg sắt nguyên tố/ngày.",
            "notes": "Uống lúc đói để hấp thu tốt nhất (1h trước hoặc 2h sau ăn). Nếu không dung nạp, uống cùng thức ăn."
        },
        "side_effects": [
            "Táo bón (phổ biến nhất)",
            "Phân đen (lành tính, do sắt)",
            "Buồn nôn, đau bụng",
            "Ngộ độc sắt cấp (ở trẻ em nếu uống nhầm liều cao)"
        ],
        "interactions": [
            "PPI, H2 blockers (Omeprazole, Ranitidine): Giảm hấp thu sắt (cần môi trường acid).",
            "Tetracycline, Quinolone: Sắt làm giảm hấp thu kháng sinh. Uống cách xa ≥2h.",
            "Levothyroxine: Sắt làm giảm hấp thu. Uống cách xa ≥4h.",
            "Vitamin C: Tăng hấp thu sắt (có thể uống cùng)."
        ],
        "monitoring": [
            "Hemoglobin, Hematocrit (sau 2-4 tuần điều trị)",
            "Ferritin, TIBC (Total Iron Binding Capacity)",
            "Reticulocyte count (tăng sau 7-10 ngày - dấu hiệu đáp ứng)"
        ]
    },

    "Iron Sucrose": {
        "group": "Hematology - Iron Supplement (IV)",
        "vietnamese_name": "Iron Sucrose, Venofer",
        "brand_names": {
            "common": ["Venofer"],
            "vietnam": ["Venofer 100mg/5ml"]
        },
        "administration": ["IV"],
        "indications": [
            "Thiếu máu do thiếu sắt khi không dung nạp hoặc không đáp ứng với sắt uống",
            "Thiếu máu do bệnh thận mạn (CKD) đang lọc máu",
            "Thiếu máu do bệnh viêm ruột (IBD)"
        ],
        "dosage": {
            "ckd_hemodialysis": "100mg IV trong mỗi lần lọc máu (tổng 1000mg trong 10 lần).",
            "ckd_non_dialysis": "200mg IV x 5 lần (tổng 1000mg).",
            "notes": "Truyền chậm (ít nhất 15 phút cho 100mg). Nguy cơ phản ứng quá mẫn thấp hơn Iron Dextran."
        },
        "side_effects": [
            "Hạ huyết áp (nếu truyền nhanh)",
            "Phản ứng quá mẫn (hiếm hơn Iron Dextran)",
            "Đau đầu, buồn nôn",
            "Vị kim loại trong miệng"
        ],
        "monitoring": [
            "Hemoglobin, Ferritin",
            "Huyết áp trong khi truyền",
            "Dấu hiệu phản ứng quá mẫn"
        ]
    },

    "Erythropoietin (EPO)": {
        "group": "Hematology - Erythropoiesis-Stimulating Agent (ESA)",
        "vietnamese_name": "Erythropoietin, EPO, Epoetin alfa",
        "brand_names": {
            "common": ["Epogen", "Procrit", "Eprex"],
            "vietnam": ["Eprex 2000/4000 IU"]
        },
        "administration": ["SC", "IV"],
        "indications": [
            "Thiếu máu do bệnh thận mạn (CKD)",
            "Thiếu máu do hóa trị ung thư",
            "Thiếu máu do HIV (điều trị bằng Zidovudine)"
        ],
        "contraindications": [
            "Tăng huyết áp không kiểm soát",
            "Ung thư đầu cổ, vú (tăng nguy cơ tiến triển khối u)"
        ],
        "dosage": {
            "ckd": "Khởi đầu 50-100 IU/kg SC/IV x 3 lần/tuần. Điều chỉnh để đạt Hb 10-12 g/dL.",
            "chemotherapy": "150 IU/kg SC x 3 lần/tuần hoặc 40,000 IU SC x 1 lần/tuần.",
            "notes": "Target Hb: 10-12 g/dL. KHÔNG tăng Hb >12 g/dL (tăng nguy cơ tim mạch, tử vong)."
        },
        "side_effects": [
            "Tăng huyết áp (phổ biến nhất)",
            "Huyết khối (DVT, PE, Stroke) - Nguy cơ cao nếu Hb >12 g/dL",
            "Tiến triển khối u (ở bệnh nhân ung thư)",
            "Thiếu sắt (do tăng sản xuất hồng cầu)"
        ],
        "monitoring": [
            "Hemoglobin - Mỗi 1-2 tuần khi khởi đầu, sau đó mỗi tháng",
            "Huyết áp - Mỗi lần tiêm",
            "Ferritin, TSAT (Transferrin Saturation) - Cần bổ sung sắt nếu thiếu",
            "Dấu hiệu huyết khối"
        ],
        "black_box_warnings": "Tăng nguy cơ tử vong, biến cố tim mạch nghiêm trọng, và tiến triển khối u khi target Hb >12 g/dL. Chỉ dùng khi Hb <10 g/dL và target Hb 10-12 g/dL."
    }
}
