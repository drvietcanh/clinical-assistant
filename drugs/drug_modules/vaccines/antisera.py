"""
Antisera & Antivenoms (Huyết thanh kháng độc & Kháng nọc rắn)
"""

ANTISERA_DRUGS = {
    "SAT (Tetanus Antitoxin)": {
        "group": "Antisera - Tetanus (Huyết thanh kháng uốn ván)",
        "vietnamese_name": "Huyết thanh kháng độc tố uốn ván (SAT)",
        "brand_names": {
            "common": ["SAT"],
            "vietnam": ["SAT (IVAC)"]
        },
        "administration": ["IM (tiêm bắp), SC (dưới da)"],
        "indications": [
            "Dự phòng uốn ván khi bị vết thương (thụ động)",
            "Điều trị bệnh uốn ván (liều cao)"
        ],
        "contraindications": [
            "Dị ứng với huyết thanh nguồn gốc ngựa (thử test trước khi tiêm là BẮT BUỘC)"
        ],
        "dosage": {
            "prophylaxis": "1500 IU (1 ống) tiêm bắp sau khi test âm tính.",
            "treatment": "Liều cao (10.000 - 20.000 IU hoặc hơn) theo phác đồ điều trị.",
            "test_dose": "Pha loãng 1/10, tiêm 0.1ml trong da. Đọc kết quả sau 15 phút. Nếu (+) -> Giải mẫn cảm Besredka."
        },
        "side_effects": [
            "Sốc phản vệ (nguy cơ cao do nguồn gốc ngựa)",
            "Bệnh huyết thanh (Serum sickness) - sốt, đau khớp, hạch to sau 7-10 ngày"
        ],
        "storage": "2-8 độ C."
    },

    "SAR (Rabies Antiserum)": {
        "group": "Antisera - Rabies (Huyết thanh kháng dại)",
        "vietnamese_name": "Huyết thanh kháng dại (SAR)",
        "brand_names": {
            "common": ["Favirab", "SAR"],
            "vietnam": ["SAR (IVAC) - gốc ngựa", "Favirab (Pháp) - gốc ngựa", "HBIg (người) - hiếm"]
        },
        "administration": ["Tiêm thấm nhiễm quanh vết thương (càng nhiều càng tốt) + IM phần còn lại"],
        "indications": [
            "Dự phòng bệnh dại sau phơi nhiễm độ III (vết thương chảy máu, niêm mạc, đầu mặt cổ)"
        ],
        "dosage": {
            "equine_sar": "40 IU/kg (SAR, Favirab). Thử test trước tiêm.",
            "human_hbig": "20 IU/kg (Ít gây dị ứng, không cần test, nhưng đắt/hiếm).",
            "notes": "Tiêm càng sớm càng tốt (ngày 0). Thấm nhiễm tối đa vào vết thương."
        },
        "side_effects": ["Sốc phản vệ (gốc ngựa). Bệnh huyết thanh."],
        "storage": "2-8 độ C."
    },

    "Snake Antivenom (Luc Tre)": {
        "group": "Antivenom - Snake (Kháng nọc rắn)",
        "vietnamese_name": "Huyết thanh kháng nọc rắn Lục Tre",
        "brand_names": {
            "vietnam": ["SAV Lục Tre (IVAC)"]
        },
        "administration": ["IV chậm hoặc truyền tĩnh mạch (pha loãng)"],
        "indications": ["Rắn Lục Tre cắn có rối loạn đông máu nặng hoặc triệu chứng toàn thân"],
        "dosage": {
            "initial": "10-20 lọ (tùy tình trạng, theo phác đồ BV Chợ Rẫy/Bạch Mai).",
            "notes": "Cần thử test trước (bắt buộc). Theo dõi sát phản vệ."
        },
        "side_effects": ["Sốc phản vệ (tỷ lệ cao)."],
        "storage": "2-8 độ C."
    },

    "Snake Antivenom (Ho Dat)": {
        "group": "Antivenom - Snake (Kháng nọc rắn)",
        "vietnamese_name": "Huyết thanh kháng nọc rắn Hổ Đất",
        "brand_names": {
            "vietnam": ["SAV Hổ Đất (IVAC)"]
        },
        "administration": ["IV chậm/Truyền TM"],
        "indications": ["Rắn Hổ Đất cắn có liệt cơ/suy hô hấp"],
        "dosage": {
            "initial": "Liều cao, đánh giá đáp ứng lâm sàng (cải thiện liệt, mở mắt).",
            "notes": "Thử test trước. Chuẩn bị sẵn Adrenalin."
        },
        "storage": "2-8 độ C."
    }
}
