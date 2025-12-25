"""Respiratory Medications
Active module - fixed-dose combination inhalers (ICS/LABA, LAMA/LABA, SAMA/SABA)"""

COMBINATION_INHALERS_DRUGS = {
    "Budesonide/Formoterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LABA)",
        "vietnamese_name": "Budesonide/Formoterol, Symbicort",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát + cắt cơn theo GINA: SMART/MART)",
            "COPD có nhiều đợt cấp (ICS/LABA)",
        ],
        "contraindications": [
            "Dị ứng với budesonide, formoterol hoặc bất kỳ thành phần nào",
            "Hen phế quản cấp (không dùng đơn độc để cắt cơn nếu không theo phác đồ SMART/MART)",
        ],
        "dosage": {
            "adult_asthma_maintenance": "160/4.5mcg: 2 hít x 2 lần/ngày (sáng, tối)",
            "adult_asthma_smart": "160/4.5mcg: 1-2 hít x 1-2 lần/ngày duy trì + 1 hít khi cần, tối đa 12 hít/ngày",
            "adult_copd": "160/4.5mcg: 2 hít x 2 lần/ngày",
            "notes": "Dùng đều đặn hàng ngày. Trong phác đồ SMART/MART, có thể dùng thêm để cắt cơn nhẹ thay SABA.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi"},
        "side_effects": [
            "Nấm miệng (do ICS)",
            "Khàn tiếng",
            "Ho, kích ứng họng",
            "Tim đập nhanh, run cơ (do LABA)",
            "Đau đầu",
        ],
        "interactions": [
            "Ritonavir, ketoconazole, itraconazole: tăng nồng độ budesonide",
            "Beta-blocker: đối kháng tác dụng formoterol",
            "Theophylline: tăng tác dụng phụ tim mạch",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Phối hợp ICS (budesonide) kháng viêm tại chỗ và LABA (formoterol) giãn phế quản kéo dài, khởi phát nhanh. Dùng vừa để kiểm soát vừa để cắt cơn (SMART/MART).",
        "monitoring": [
            "Triệu chứng hen/COPD, số lần cơn cấp, nhu cầu SABA",
            "Nấm miệng, khàn tiếng",
            "Nhịp tim, run cơ",
        ],
        "precautions": [
            "Súc miệng sau khi dùng để tránh nấm miệng.",
            "Không dùng LABA đơn độc cho hen – luôn đi kèm ICS.",
            "Trong phác đồ SMART/MART: cần hướng dẫn rõ cho bệnh nhân về tối đa số hít/ngày.",
        ],
    },
    "Fluticasone/Salmeterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LABA)",
        "vietnamese_name": "Fluticasone/Salmeterol, Seretide, Advair",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát, phòng ngừa)",
            "COPD có nhiều đợt cấp",
        ],
        "contraindications": [
            "Dị ứng với fluticasone, salmeterol hoặc thành phần khác",
            "Hen phế quản cấp (không dùng để cắt cơn)",
        ],
        "dosage": {
            "adult_asthma": "250/50mcg: 1 hít x 2 lần/ngày; điều chỉnh theo mức độ hen",
            "adult_copd": "250/50mcg: 1 hít x 2 lần/ngày",
            "notes": "Không dùng để cắt cơn; cần SABA kèm theo.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi"},
        "side_effects": [
            "Nấm miệng, khàn tiếng (ICS)",
            "Tim đập nhanh, run cơ (LABA)",
            "Đau đầu",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Ritonavir: tăng mạnh nồng độ fluticasone (tránh dùng)",
            "Ketoconazole/itraconazole: tăng nồng độ fluticasone",
            "Beta-blocker: đối kháng tác dụng salmeterol",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "ICS (fluticasone) kháng viêm + LABA (salmeterol) giãn phế quản kéo dài 12 giờ. Cải thiện kiểm soát hen/COPD khi đơn trị ICS hoặc LABA không đủ.",
        "monitoring": [
            "Triệu chứng hen/COPD, FEV1",
            "Nấm miệng, khàn tiếng",
            "Nhịp tim, huyết áp",
        ],
        "precautions": [
            "Súc miệng sau khi dùng.",
            "Không dùng LABA đơn độc cho hen.",
            "Tránh dùng với ritonavir nếu có thể.",
        ],
    },
    "Ipratropium/Salbutamol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (SAMA/SABA)",
        "vietnamese_name": "Ipratropium/Salbutamol, Combivent, Duoneb",
        "administration": ["Inhalation", "Nebulizer"],
        "indications": [
            "COPD đợt cấp",
            "Cơn hen nặng (kết hợp SABA + SAMA)",
        ],
        "contraindications": [
            "Dị ứng với ipratropium, atropine, salbutamol",
            "Glaucoma góc đóng, tăng nhãn áp nặng",
        ],
        "dosage": {
            "adult_inhaler": "1-2 puffs mỗi 4-6 giờ khi cần",
            "adult_nebulizer": "2.5mg salbutamol + 0.5mg ipratropium mỗi 4-6 giờ",
            "notes": "Thường dùng trong cấp cứu/đợt cấp; theo dõi sát nhịp tim và hô hấp.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi"},
        "side_effects": [
            "Tim đập nhanh, run cơ (SABA)",
            "Khô miệng, đắng miệng (SAMA)",
            "Ho, kích ứng họng",
        ],
        "interactions": [
            "Anticholinergics khác: tăng tác dụng phụ khô miệng, bí tiểu",
            "Beta-blocker: giảm tác dụng salbutamol",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Hiệp đồng SABA (salbutamol – kích thích beta-2) và SAMA (ipratropium – ức chế muscarinic), giãn phế quản mạnh trong đợt cấp COPD/hen.",
        "monitoring": [
            "Nhịp tim, huyết áp",
            "Đáp ứng phế quản, SpO2",
            "Dấu hiệu tăng nhãn áp nếu thuốc vào mắt",
        ],
        "precautions": [
            "Tránh thuốc vào mắt (nguy cơ tăng nhãn áp).",
            "Thận trọng ở bệnh nhân tim mạch, loạn nhịp.",
        ],
    },
    "Tiotropium/Olodaterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (LAMA/LABA)",
        "vietnamese_name": "Tiotropium/Olodaterol, Spiolto Respimat, Stiolto Respimat",
        "administration": ["Inhalation"],
        "indications": [
            "COPD (phòng ngừa triệu chứng và đợt cấp)",
        ],
        "contraindications": [
            "Dị ứng với tiotropium, olodaterol",
            "Glaucoma góc đóng, phì đại tuyến tiền liệt nặng",
            "Hen phế quản cấp (không dùng để cắt cơn)",
        ],
        "dosage": {
            "adult_copd": "2 puffs (5/5mcg) x 1 lần/ngày",
            "notes": "Dùng đều đặn 1 lần/ngày, không dùng để cắt cơn.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Tránh dùng hoặc theo dõi rất sát"},
        "side_effects": [
            "Khô miệng, bí tiểu (LAMA)",
            "Tim đập nhanh, run cơ (LABA – hiếm)",
            "Ho, kích ứng họng",
        ],
        "interactions": [
            "Anticholinergics khác: tăng tác dụng phụ",
            "Beta-blocker: đối kháng tác dụng olodaterol",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Kết hợp LAMA (tiotropium) và LABA (olodaterol) giúp giãn phế quản tối ưu và kéo dài 24 giờ cho COPD.",
        "monitoring": [
            "Triệu chứng COPD, FEV1",
            "Dấu hiệu bí tiểu, tăng nhãn áp",
            "Nhịp tim, huyết áp ở bệnh nhân có bệnh tim mạch",
        ],
        "precautions": [
            "Không dùng để cắt cơn; cần SABA dự phòng.",
            "Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
        ],
    },
    "Umeclidinium/Vilanterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (LAMA/LABA)",
        "vietnamese_name": "Umeclidinium/Vilanterol, Anoro Ellipta",
        "administration": ["Inhalation"],
        "indications": [
            "COPD (phòng ngừa triệu chứng và đợt cấp)",
        ],
        "contraindications": [
            "Dị ứng với umeclidinium, vilanterol",
            "Glaucoma góc đóng, phì đại tuyến tiền liệt nặng",
        ],
        "dosage": {
            "adult_copd": "62.5/25mcg: 1 hít x 1 lần/ngày",
            "notes": "Dùng đều đặn 1 lần/ngày, không dùng cho hen đơn độc.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng"},
        "side_effects": [
            "Khô miệng, bí tiểu",
            "Tim đập nhanh, run cơ",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Anticholinergics khác: tăng tác dụng phụ",
            "Beta-blocker: đối kháng tác dụng vilanterol",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "LAMA (umeclidinium) + LABA (vilanterol) cho giãn phế quản kéo dài 24 giờ, cải thiện triệu chứng COPD.",
        "monitoring": [
            "Triệu chứng COPD, FEV1",
            "Dấu hiệu bí tiểu, tăng nhãn áp",
        ],
        "precautions": [
            "Không dùng cho hen phế quản nếu không có ICS kèm.",
            "Tránh thuốc vào mắt.",
        ],
    },
    "Fluticasone/Umeclidinium/Vilanterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LAMA/LABA)",
        "vietnamese_name": "Fluticasone/Umeclidinium/Vilanterol, Trelegy Ellipta",
        "administration": ["Inhalation"],
        "indications": [
            "COPD nặng, nhiều đợt cấp (triple therapy)",
            "Hen phế quản không kiểm soát với ICS/LABA",
        ],
        "contraindications": [
            "Dị ứng với fluticasone, umeclidinium, vilanterol",
            "Dùng cùng ritonavir (tăng mạnh nồng độ fluticasone)",
        ],
        "dosage": {
            "adult_copd": "100/62.5/25mcg: 1 hít x 1 lần/ngày",
            "adult_asthma": "200/62.5/25mcg: 1 hít x 1 lần/ngày (tùy mức độ)",
            "notes": "Dùng đều đặn 1 lần/ngày; không dùng để cắt cơn.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng"},
        "side_effects": [
            "Nấm miệng, khàn tiếng (ICS)",
            "Khô miệng, bí tiểu (LAMA)",
            "Tim đập nhanh, run cơ (LABA)",
        ],
        "interactions": [
            "Ritonavir: chống chỉ định (tăng mạnh nồng độ fluticasone)",
            "Ketoconazole/itraconazole: tăng nồng độ fluticasone",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Phối hợp 3 trong 1: ICS (fluticasone) kháng viêm, LAMA (umeclidinium) và LABA (vilanterol) giãn phế quản kéo dài, tối ưu hóa kiểm soát COPD/hen nặng.",
        "monitoring": [
            "Triệu chứng hen/COPD, FEV1",
            "Nấm miệng, tác dụng phụ anticholinergic",
            "Nhịp tim, huyết áp",
        ],
        "precautions": [
            "Súc miệng sau khi dùng.",
            "Không dùng với ritonavir.",
        ],
    },
}

__all__ = ["COMBINATION_INHALERS_DRUGS"]


