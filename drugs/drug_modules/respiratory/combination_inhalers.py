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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
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
        "pharmacokinetics": {
            "half_life": "Budesonide: 2-3 giờ; Formoterol: 10 giờ",
            "onset": "Formoterol: 1-3 phút (khởi phát nhanh); Budesonide: vài giờ",
            "duration": "Formoterol: 12 giờ; Budesonide: tác dụng tại chỗ kéo dài",
            "protein_binding": "Budesonide: 88-90%; Formoterol: 50-65%",
            "clearance": "Budesonide: chuyển hóa gan (CYP3A4) thành chất không hoạt tính, thải qua thận; Formoterol: chuyển hóa gan (CYP2D6, CYP2C19), thải qua thận và phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
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
        "pharmacokinetics": {
            "half_life": "Fluticasone: 7.8 giờ; Salmeterol: 5.5 giờ",
            "onset": "Salmeterol: 10-20 phút; Fluticasone: vài giờ",
            "duration": "Salmeterol: 12 giờ; Fluticasone: tác dụng tại chỗ kéo dài",
            "protein_binding": "Fluticasone: 91%; Salmeterol: 96%",
            "clearance": "Fluticasone: chuyển hóa gan (CYP3A4) thành chất không hoạt tính, thải qua phân; Salmeterol: chuyển hóa gan (CYP3A4), thải qua phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Không dùng LABA đơn độc cho hen phế quản - luôn phải kết hợp với ICS. Tăng nguy cơ tử vong do hen khi dùng LABA không kèm ICS.",
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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
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
        "pharmacokinetics": {
            "half_life": "Ipratropium: 2 giờ; Salbutamol: 3.8 giờ",
            "onset": "Salbutamol: 5-15 phút; Ipratropium: 15-30 phút",
            "duration": "Salbutamol: 3-6 giờ; Ipratropium: 4-6 giờ",
            "protein_binding": "Ipratropium: <20%; Salbutamol: 10%",
            "clearance": "Ipratropium: thải trừ chủ yếu qua thận (dạng nguyên dạng); Salbutamol: chuyển hóa gan (sulfation), thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
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
        "pharmacokinetics": {
            "half_life": "Tiotropium: 5-6 ngày (rất dài); Olodaterol: 22 giờ",
            "onset": "Olodaterol: 5 phút; Tiotropium: 30 phút",
            "duration": "Cả hai: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Tiotropium: 72%; Olodaterol: 60%",
            "clearance": "Tiotropium: thải trừ chủ yếu qua thận (dạng nguyên dạng), một phần qua gan; Olodaterol: chuyển hóa gan (UGT, O-methylation), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "LAMA (umeclidinium) + LABA (vilanterol) cho giãn phế quản kéo dài 24 giờ, cải thiện triệu chứng COPD.",
        "monitoring": [
            "Triệu chứng COPD, FEV1",
            "Dấu hiệu bí tiểu, tăng nhãn áp",
        ],
        "precautions": [
            "Không dùng cho hen phế quản nếu không có ICS kèm.",
            "Tránh thuốc vào mắt.",
        ],
        "pharmacokinetics": {
            "half_life": "Umeclidinium: 11 giờ; Vilanterol: 11 giờ",
            "onset": "Vilanterol: 5 phút; Umeclidinium: 5-15 phút",
            "duration": "Cả hai: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Umeclidinium: 89%; Vilanterol: 94%",
            "clearance": "Umeclidinium: chuyển hóa gan (CYP2D6), thải qua phân và thận; Vilanterol: chuyển hóa gan (CYP3A4), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
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
        "pharmacokinetics": {
            "half_life": "Fluticasone: 7.8 giờ; Umeclidinium: 11 giờ; Vilanterol: 11 giờ",
            "onset": "Vilanterol: 5 phút; Umeclidinium: 5-15 phút; Fluticasone: vài giờ",
            "duration": "Cả ba: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Fluticasone: 91%; Umeclidinium: 89%; Vilanterol: 94%",
            "clearance": "Fluticasone: chuyển hóa gan (CYP3A4), thải qua phân; Umeclidinium: chuyển hóa gan (CYP2D6), thải qua phân và thận; Vilanterol: chuyển hóa gan (CYP3A4), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Không dùng với ritonavir do tăng mạnh nồng độ fluticasone gây tác dụng phụ nghiêm trọng. Không dùng LABA đơn độc cho hen phế quản.",
    },
}

__all__ = ["COMBINATION_INHALERS_DRUGS"]


