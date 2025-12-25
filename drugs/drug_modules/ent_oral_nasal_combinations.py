"""ENT / Upper Respiratory Combination Medications
Đường uống và xịt mũi: kháng histamin + thuốc thông mũi, corticoid mũi phối hợp.
Nhóm này dùng nhiều trong tai mũi họng và hô hấp trên (viêm mũi dị ứng, viêm xoang…)."""

ENT_ORAL_NASAL_COMBINATIONS_DRUGS = {
    "Loratadine/Pseudoephedrine": {
        "group": "ENT - Combination (Oral Antihistamine + Decongestant)",
        "vietnamese_name": "Loratadine/Pseudoephedrine, Clarityne-D",
        "administration": ["PO"],
        "indications": [
            "Viêm mũi dị ứng có nghẹt mũi (allergic rhinitis with nasal congestion)",
            "Cảm lạnh, viêm mũi xoang kèm nghẹt mũi",
        ],
        "contraindications": [
            "Dị ứng với loratadine, pseudoephedrine hoặc thành phần khác",
            "Tăng huyết áp nặng, bệnh mạch vành, nhồi máu cơ tim gần đây",
            "Cường giáp, glaucom góc đóng",
            "Đang dùng IMAO hoặc trong vòng 14 ngày ngừng IMAO",
        ],
        "dosage": {
            "adult": "1 viên (loratadine 5mg + pseudoephedrine 120mg) mỗi 12 giờ",
            "adult_max": "2 viên/ngày",
            "notes": "Không dùng quá 10 ngày liên tục. Uống trước 18h để tránh mất ngủ.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Cân nhắc kéo dài khoảng cách liều pseudoephedrine",
            "under_30": "Tránh dùng hoặc chọn thuốc khác an toàn hơn",
        },
        "side_effects": [
            "Tim đập nhanh, tăng huyết áp (do pseudoephedrine)",
            "Mất ngủ, kích thích, lo âu",
            "Khô miệng, nhức đầu",
        ],
        "interactions": [
            "IMAO: nguy cơ tăng huyết áp ác tính (CHỐNG CHỈ ĐỊNH)",
            "Thuốc cường giao cảm khác: tăng nguy cơ tim mạch",
            "Thuốc hạ huyết áp: giảm hiệu quả",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Loratadine kháng H1 ngoại vi, giảm hắt hơi, chảy mũi, ngứa. Pseudoephedrine là chất cường giao cảm, co mạch niêm mạc mũi, giảm sung huyết và nghẹt mũi.",
        "monitoring": [
            "Huyết áp, nhịp tim (đặc biệt ở người có bệnh tim mạch)",
            "Triệu chứng mất ngủ, kích thích",
        ],
        "precautions": [
            "Không dùng kéo dài; chỉ dùng ngắn ngày cho giai đoạn cấp.",
            "Thận trọng ở người tăng huyết áp, bệnh mạch vành, người cao tuổi.",
        ],
    },
    "Cetirizine/Pseudoephedrine": {
        "group": "ENT - Combination (Oral Antihistamine + Decongestant)",
        "vietnamese_name": "Cetirizine/Pseudoephedrine, Zyrtec-D",
        "administration": ["PO"],
        "indications": [
            "Viêm mũi dị ứng kèm nghẹt mũi",
        ],
        "contraindications": [
            "Dị ứng với cetirizine, pseudoephedrine hoặc thành phần khác",
            "Tăng huyết áp nặng, bệnh mạch vành",
            "Cường giáp, glaucom góc đóng",
            "Đang dùng IMAO hoặc trong vòng 14 ngày ngừng IMAO",
        ],
        "dosage": {
            "adult": "1 viên (cetirizine 5mg + pseudoephedrine 120mg) mỗi 12 giờ",
            "adult_max": "2 viên/ngày",
            "notes": "Có thể gây buồn ngủ (cetirizine) và mất ngủ (pseudoephedrine); đánh giá trên từng bệnh nhân.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm tần suất dùng (mỗi 24 giờ)",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Buồn ngủ hoặc mất ngủ",
            "Tim đập nhanh, tăng huyết áp",
            "Khô miệng, nhức đầu",
        ],
        "interactions": [
            "IMAO: CHỐNG CHỈ ĐỊNH",
            "Alcohol, thuốc ức chế TKTW: tăng buồn ngủ (cetirizine)",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Cetirizine kháng H1, pseudoephedrine co mạch niêm mạc mũi, kết hợp giúp giảm cả triệu chứng dị ứng và nghẹt mũi.",
        "monitoring": [
            "Huyết áp, nhịp tim",
            "Mức độ buồn ngủ/kích thích",
        ],
        "precautions": [
            "Không dùng cho bệnh nhân tim mạch nặng, tăng huyết áp khó kiểm soát.",
            "Không dùng kéo dài >10 ngày.",
        ],
    },
    "Fexofenadine/Pseudoephedrine": {
        "group": "ENT - Combination (Oral Antihistamine + Decongestant)",
        "vietnamese_name": "Fexofenadine/Pseudoephedrine, Allegra-D",
        "administration": ["PO"],
        "indications": [
            "Viêm mũi dị ứng theo mùa kèm nghẹt mũi",
        ],
        "contraindications": [
            "Dị ứng với fexofenadine, pseudoephedrine",
            "Tăng huyết áp nặng, bệnh mạch vành",
            "Cường giáp, glaucom góc đóng",
            "Đang dùng IMAO hoặc trong vòng 14 ngày ngừng IMAO",
        ],
        "dosage": {
            "adult": "60/120mg mỗi 12 giờ hoặc 180/240mg mỗi 24 giờ (tùy chế phẩm)",
            "notes": "Fexofenadine ít gây buồn ngủ; pseudoephedrine có thể gây mất ngủ.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm tần suất dùng",
            "under_30": "Thận trọng hoặc tránh dùng",
        },
        "side_effects": [
            "Mất ngủ, kích thích",
            "Tim đập nhanh, tăng huyết áp",
            "Đau đầu, khô miệng",
        ],
        "interactions": [
            "Fruit juices: giảm hấp thu fexofenadine (uống cách xa 2 giờ)",
            "IMAO: CHỐNG CHỈ ĐỊNH (pseudoephedrine)",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Fexofenadine kháng H1 không gây buồn ngủ; pseudoephedrine co mạch niêm mạc mũi, giảm nghẹt mũi.",
        "monitoring": [
            "Huyết áp, nhịp tim",
            "Triệu chứng kích thích TKTW (mất ngủ, lo âu)",
        ],
        "precautions": [
            "Không dùng với nước hoa quả (giảm hấp thu fexofenadine).",
            "Không dùng kéo dài, chỉ dùng ngắn ngày.",
        ],
    },
    "Azelastine/Fluticasone nasal spray": {
        "group": "ENT - Combination (Intranasal Antihistamine + Corticosteroid)",
        "vietnamese_name": "Azelastine/Fluticasone xịt mũi, Dymista",
        "administration": ["Nasal"],
        "indications": [
            "Viêm mũi dị ứng trung bình–nặng (perennial/seasonal)",
            "Bệnh nhân không đáp ứng đủ với corticoid mũi đơn độc",
        ],
        "contraindications": [
            "Dị ứng với azelastine, fluticasone hoặc thành phần khác",
            "Nhiễm trùng mũi chưa điều trị (nấm, lao…) – thận trọng",
        ],
        "dosage": {
            "adult": "1 nhát xịt mỗi bên mũi x 2 lần/ngày",
            "notes": "Lắc kỹ trước khi dùng. Hướng đầu xịt hơi ra ngoài vách ngăn để tránh chảy máu mũi.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
        },
        "side_effects": [
            "Cảm giác đắng ở miệng (azelastine)",
            "Kích ứng mũi, khô mũi",
            "Chảy máu mũi nhẹ",
            "Nấm họng/mũi (hiếm, do corticoid)",
        ],
        "interactions": [
            "Ritonavir, ketoconazole, itraconazole: tăng nồng độ fluticasone (thận trọng)",
            "Rượu hoặc thuốc an thần: có thể tăng buồn ngủ nhẹ (azelastine)",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Azelastine là kháng H1 tại chỗ, giảm ngứa, hắt hơi, chảy mũi; fluticasone là corticoid mũi kháng viêm mạnh, giảm phù nề niêm mạc mũi. Phối hợp cho hiệu quả nhanh và mạnh hơn đơn trị.",
        "monitoring": [
            "Triệu chứng viêm mũi (ngứa, hắt hơi, chảy mũi, nghẹt mũi)",
            "Chảy máu mũi, kích ứng mũi",
            "Dấu hiệu nhiễm trùng nấm tại chỗ",
        ],
        "precautions": [
            "Hướng vòi xịt lệch ra ngoài vách ngăn để tránh loét vách ngăn.",
            "Súc miệng/nước sau xịt để giảm vị đắng và nguy cơ nấm.",
            "Không dùng kéo dài liều cao nếu không cần thiết; đánh giá định kỳ.",
        ],
    },
}

__all__ = ["ENT_ORAL_NASAL_COMBINATIONS_DRUGS"]


