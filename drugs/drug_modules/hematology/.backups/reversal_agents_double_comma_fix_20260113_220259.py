"""
Hematology Drugs - Reversal Agents
"""
from typing import Dict, Any


REVERSAL_AGENTS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Andexanet alfa": {
            "group": "Hematology - DOAC Reversal Agent (Factor Xa Inhibitors)",
            "vietnamese_name": "Andexanet alfa, Andexxa",
            "administration": ["IV"],
            "indications": [
                "Đảo ngược tác dụng chống đông của apixaban hoặc rivaroxaban trong trường hợp chảy máu đe dọa tính mạng",
                "Đảo ngược tác dụng apixaban/rivaroxaban trước phẫu thuật khẩn cấp hoặc thủ thuật xâm lấn",
                "Quá liều apixaban/rivaroxaban có triệu chứng"
            ],
            "contraindications": [
                "Dị ứng với andexanet alfa hoặc các thành phần",
                "Không có chỉ định đảo ngược factor Xa inhibitor"
            ],
            "dosage": {
                "adult_low_dose": "400mg IV bolus, sau đó truyền 4mg/phút x 2 giờ (cho apixaban ≤5mg hoặc rivaroxaban ≤10mg, hoặc không biết liều)",
                "adult_high_dose": "800mg IV bolus, sau đó truyền 8mg/phút x 2 giờ (cho apixaban >5mg hoặc rivaroxaban >10mg)",
                "notes": "Liều dựa trên liều DOAC cuối cùng và thời gian từ liều cuối. Tác dụng đảo ngược trong vài phút."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Không cần chỉnh liều",
                "under_30": "Không cần chỉnh liều",
                "hemodialysis": "Không cần chỉnh liều"
            },
            "side_effects": [
                "Phản ứng dị ứng/phản vệ (hiếm)",
                "Huyết khối tái phát (sau khi đảo ngược) - nguy cơ cao hơn idarucizumab",
                "Tăng men gan (hiếm)"
            ],
            "interactions": [
                "Không có tương tác thuốc đáng kể",
                "Sau khi đảo ngược: có thể dùng lại DOAC sau 24 giờ nếu cần"
            ],
            "pregnancy": "C - Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt nguy cơ",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True},
                "icu_critical_care_only": True,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "ISTH 2020 DOAC Reversal Guidelines",
                "ACC/AHA/HRS AF Guidelines",
                "FDA Drug Label - Andexxa"
            ],
            "mechanism_of_action": (
                "Andexanet alfa là protein tái tổ hợp (modified factor Xa) gắn với các direct factor Xa inhibitors "
                "(apixaban, rivaroxaban, edoxaban, betrixaban) với ái lực cao, tạo phức hợp không hoạt tính. "
                "Andexanet alfa không có hoạt tính procoagulant do thiếu vị trí hoạt hóa. Đảo ngược tác dụng "
                "chống đông trong vài phút, có thể đo được bằng anti-factor Xa activity."
            ),
            "monitoring": [
                "Anti-factor Xa activity (apixaban/rivaroxaban-specific) trước và sau khi dùng",
                "Dấu hiệu chảy máu (nếu dùng cho chảy máu)",
                "Dấu hiệu huyết khối tái phát sau đảo ngược (nguy cơ cao hơn idarucizumab)",
                "Men gan (ALT/AST) nếu dùng kéo dài hoặc có bệnh gan nền",
                "Huyết áp, mạch trong quá trình truyền"
            ],
            "precautions": [
                "Chỉ dùng khi thật sự cần đảo ngược factor Xa inhibitor (chảy máu đe dọa tính mạng hoặc phẫu thuật khẩn cấp)",
                "Sau đảo ngược: nguy cơ huyết khối tái phát cao hơn idarucizumab - cân nhắc dùng lại chống đông sau 24 giờ",
                "Có thể dùng lại DOAC sau 24 giờ nếu cần",
                "Chuẩn bị sẵn phương tiện hồi sức cho phản ứng dị ứng",
                "Theo dõi men gan nếu có bệnh gan nền"
            ],
            "pharmacokinetics": {
                "half_life": "~1 giờ (ngắn)",
                "onset": "Vài phút sau khi bắt đầu bolus",
                "duration": "Đảo ngược trong vài phút, kéo dài trong thời gian truyền (2 giờ)",
                "protein_binding": "Gắn với factor Xa inhibitors",
                "clearance": "Chuyển hóa qua gan và thải trừ qua thận"
            },
            "storage": "Bảo quản lạnh 2-8°C, tránh đông lạnh. Sau khi pha, dùng trong 8 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
            "black_box_warnings": (
                "Sau khi đảo ngược factor Xa inhibitor, nguy cơ huyết khối tái phát tăng lên đáng kể. "
                "Cân nhắc dùng lại chống đông sau khi đảo ngược nếu bệnh nhân vẫn có chỉ định chống đông. "
                "Theo dõi sát dấu hiệu huyết khối trong 24-48 giờ sau đảo ngược."
            ),
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với andexanet alfa hoặc các thành phần"
                ],
                "tương_đối": [
                    "Không có chỉ định đảo ngược factor Xa inhibitor rõ ràng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt nguy cơ (chảy máu đe dọa tính mạng hoặc phẫu thuật khẩn cấp).",
                "lactation": {
                    "safety": "Caution",
                    "details": "Không rõ bài tiết sữa; phân tử lớn, hấp thu đường tiêu hóa kém ở trẻ.",
                    "recommendation": "Có thể tiếp tục cho bú; theo dõi trẻ nếu có dấu hiệu bất thường."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều",
                "moderate": "Không cần chỉnh liều; theo dõi men gan",
                "severe": "Thận trọng; theo dõi men gan",
                "notes": "Andexanet alfa chuyển hóa qua gan; suy gan có thể ảnh hưởng đến thanh thải nhưng không cần điều chỉnh liều."
            },
            "overdose_management": {
                "symptoms": [
                    "Phản ứng dị ứng/phản vệ (hiếm)",
                    "Huyết khối tái phát (nếu đã đảo ngược quá mức)",
                    "Tăng men gan (hiếm)"
                ],
                "antidote": "Không có antidote đặc hiệu",
                "treatment": [
                    "Xử trí phản ứng dị ứng: epinephrine, diphenhydramine, hydrocortisone nếu cần",
                    "Nếu huyết khối tái phát: cân nhắc dùng lại chống đông (DOAC hoặc thuốc khác) sau 24 giờ",
                    "Theo dõi men gan nếu có tăng men gan"
                ],
                "monitoring": "Huyết động, dấu hiệu dị ứng, dấu hiệu huyết khối, men gan trong 24-48 giờ"
            },
            "reversal_agents": None,
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha bột theo hướng dẫn chế phẩm với NS hoặc D5W",
                    "infusion_rate": "Bolus: 400mg hoặc 800mg trong 15-30 phút, sau đó truyền liên tục 4mg/phút (low-dose) hoặc 8mg/phút (high-dose) x 2 giờ",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": [],
                    "notes": "Liều dựa trên liều DOAC cuối cùng. Low-dose: 400mg bolus + 4mg/phút x 2h. High-dose: 800mg bolus + 8mg/phút x 2h."
                }
            },
            "references": {
                "primary_sources": [
                    "ISTH 2020 Guidelines for DOAC Reversal",
                    "ACC/AHA/HRS AF Guidelines",
                    "FDA Drug Label - Andexxa (Andexanet alfa)",
                    "ANNEXA-4 Study"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - FDA-approved, guideline-supported"
            }
        },

        "Idarucizumab": {
            "group": "Hematology - DOAC Reversal Agent (Dabigatran)",
            "vietnamese_name": "Idarucizumab, Praxbind",
            "administration": ["IV"],
            "indications": [
                "Đảo ngược tác dụng chống đông của dabigatran trong trường hợp chảy máu đe dọa tính mạng",
                "Đảo ngược tác dụng dabigatran trước phẫu thuật khẩn cấp hoặc thủ thuật xâm lấn",
                "Quá liều dabigatran có triệu chứng"
            ],
            "contraindications": [
                "Dị ứng với idarucizumab hoặc các thành phần",
                "Không có chỉ định đảo ngược dabigatran"
            ],
            "dosage": {
                "adult_standard": "5g IV (2 lọ 2.5g), tiêm nhanh liên tiếp hoặc truyền trong 5-10 phút",
                "notes": "Liều cố định, không cần điều chỉnh theo tuổi, cân nặng, hoặc chức năng thận/gan. Tác dụng ngay lập tức."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Không cần chỉnh liều",
                "under_30": "Không cần chỉnh liều",
                "hemodialysis": "Không cần chỉnh liều"
            },
            "side_effects": [
                "Phản ứng dị ứng/phản vệ (hiếm)",
                "Huyết khối tái phát (sau khi đảo ngược)",
                "Hạ kali máu nhẹ (hiếm)"
            ],
            "interactions": [
                "Không có tương tác thuốc đáng kể",
                "Sau khi đảo ngược: có thể dùng lại dabigatran sau 24 giờ nếu cần"
            ],
            "pregnancy": "C - Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt nguy cơ",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {},
                "icu_critical_care_only": True,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "ISTH 2020 DOAC Reversal Guidelines",
                "ACC/AHA/HRS AF Guidelines",
                "FDA Drug Label - Praxbind"
            ],
            "mechanism_of_action": (
                "Idarucizumab là kháng thể đơn dòng humanized (Fab fragment) gắn đặc hiệu và với ái lực cao "
                "với dabigatran và các chất chuyển hóa của nó. Gắn với dabigatran tạo phức hợp không hoạt tính, "
                "đảo ngược tác dụng chống đông ngay lập tức. Tác dụng đảo ngược hoàn toàn và có thể đo được "
                "bằng aPTT và dTT (dilute thrombin time)."
            ),
            "monitoring": [
                "aPTT, dTT (dilute thrombin time) trước và sau khi dùng để xác nhận đảo ngược",
                "Dấu hiệu chảy máu (nếu dùng cho chảy máu)",
                "Dấu hiệu huyết khối tái phát sau đảo ngược (đặc biệt nếu đã ngừng dabigatran)",
                "Huyết áp, mạch trong quá trình tiêm"
            ],
            "precautions": [
                "Chỉ dùng khi thật sự cần đảo ngược dabigatran (chảy máu đe dọa tính mạng hoặc phẫu thuật khẩn cấp)",
                "Sau đảo ngược: nguy cơ huyết khối tái phát nếu bệnh nhân vẫn cần chống đông",
                "Có thể dùng lại dabigatran sau 24 giờ nếu cần",
                "Chuẩn bị sẵn phương tiện hồi sức cho phản ứng dị ứng (hiếm)"
            ],
            "pharmacokinetics": {
                "half_life": "~10 giờ (Fab fragment)",
                "onset": "Ngay lập tức sau khi tiêm",
                "duration": "Đảo ngược hoàn toàn trong vài phút, kéo dài vài giờ",
                "protein_binding": "Gắn với dabigatran",
                "clearance": "Thải trừ qua thận (không chuyển hóa)"
            },
            "storage": "Bảo quản lạnh 2-8°C, tránh đông lạnh. Sau khi pha, dùng trong 1 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
            "black_box_warnings": (
                "Sau khi đảo ngược dabigatran, nguy cơ huyết khối tái phát tăng lên. "
                "Cân nhắc dùng lại chống đông sau khi đảo ngược nếu bệnh nhân vẫn có chỉ định chống đông."
            ),
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với idarucizumab hoặc các thành phần"
                ],
                "tương_đối": [
                    "Không có chỉ định đảo ngược dabigatran rõ ràng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt nguy cơ (chảy máu đe dọa tính mạng hoặc phẫu thuật khẩn cấp).",
                "lactation": {
                    "safety": "Caution",
                    "details": "Không rõ bài tiết sữa; phân tử lớn, hấp thu đường tiêu hóa kém ở trẻ.",
                    "recommendation": "Có thể tiếp tục cho bú; theo dõi trẻ nếu có dấu hiệu bất thường."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều",
                "moderate": "Không cần chỉnh liều",
                "severe": "Không cần chỉnh liều",
                "notes": "Idarucizumab không chuyển hóa qua gan; không cần điều chỉnh liều."
            },
            "overdose_management": {
                "symptoms": [
                    "Phản ứng dị ứng/phản vệ (hiếm)",
                    "Huyết khối tái phát (nếu đã đảo ngược quá mức)"
                ],
                "antidote": "Không có antidote đặc hiệu",
                "treatment": [
                    "Xử trí phản ứng dị ứng: epinephrine, diphenhydramine, hydrocortisone nếu cần",
                    "Nếu huyết khối tái phát: cân nhắc dùng lại chống đông (dabigatran hoặc thuốc khác) sau 24 giờ"
                ],
                "monitoring": "Huyết động, dấu hiệu dị ứng, dấu hiệu huyết khối trong 24-48 giờ"
            },
            "reversal_agents": None,
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha mỗi lọ 2.5g với 50ml NS hoặc D5W (tổng 100ml cho 2 lọ)",
                    "infusion_rate": "Tiêm nhanh liên tiếp hoặc truyền trong 5-10 phút",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": [],
                    "notes": "Liều cố định 5g (2 lọ 2.5g). Không cần điều chỉnh liều. Tác dụng ngay lập tức."
                }
            },
            "references": {
                "primary_sources": [
                    "ISTH 2020 Guidelines for DOAC Reversal",
                    "ACC/AHA/HRS AF Guidelines",
                    "FDA Drug Label - Praxbind (Idarucizumab)",
                    "RE-VERSE AD Study"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - FDA-approved, guideline-supported"
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Protamine": {
            "group": "Hematology - Anticoagulant Reversal Agent",
            "vietnamese_name": "Protamine sulfate",
            "administration": ["IV"],
            "indications": [
                "Đảo ngược heparin (unfractionated heparin)",
                "Đảo ngược LMWH (một phần, không hoàn toàn)",
                "Chảy máu do heparin",
                "Sau phẫu thuật tim mạch (đảo ngược heparin)"
            ],
            "contraindications": [
                "Dị ứng protamine (đặc biệt bệnh nhân dị ứng cá)",
                "Đã dùng protamine trước đó (tăng nguy cơ phản ứng)",
                "Không dùng để đảo ngược LMWH (không hiệu quả)"
            ],
            "dosage": {
                "adult_heparin_reversal": "1mg protamine cho mỗi 100 units heparin (tối đa 50mg)",
                "adult_lmwh_reversal": "1mg protamine cho mỗi 1mg enoxaparin (không hoàn toàn)",
                "notes": "Tiêm IV chậm (trong 10 phút). Theo dõi aPTT sau 5-15 phút."
            },
            "side_effects": [
                "Hạ huyết áp (phổ biến)",
                "Phản ứng dị ứng (hiếm nhưng nguy hiểm)",
                "Suy hô hấp",
                "Bradycardia",
                "Đông máu (nếu quá liều)"
            ],
            "interactions": [
                "Heparin: đảo ngược tác dụng",
                "LMWH: đảo ngược một phần (không hoàn toàn)"
            ],
            "pregnancy": "C",
            "mechanism_of_action": "Protamine là protein có nguồn gốc từ tinh trùng cá hồi, có điện tích dương mạnh. Protamine gắn với heparin (có điện tích âm) tạo thành phức hợp không hoạt động, đảo ngược tác dụng chống đông của heparin. Protamine gắn với heparin theo tỷ lệ 1:1 (1mg protamine cho 100 units heparin). Protamine đảo ngược hoàn toàn unfractionated heparin (UFH) nhưng chỉ đảo ngược một phần low molecular weight heparin (LMWH) do LMWH có chuỗi ngắn hơn. Protamine có thể gây phản ứng dị ứng, đặc biệt ở bệnh nhân dị ứng cá hoặc đã dùng protamine trước đó.",
            "monitoring": [
                "Huyết áp (có thể hạ huyết áp)",
                "aPTT (sau 5-15 phút để xác nhận đảo ngược)",
                "Dấu hiệu phản ứng dị ứng (phát ban, khó thở, sốc phản vệ)",
                "Nhịp tim (có thể bradycardia)",
                "Dấu hiệu chảy máu (xem có còn chảy máu sau đảo ngược)"
            ],
            "precautions": [
                "Tiêm IV CHẬM (trong 10 phút) - tiêm nhanh có thể gây hạ huyết áp nghiêm trọng",
                "Thận trọng với bệnh nhân dị ứng cá - tăng nguy cơ phản ứng dị ứng",
                "Thận trọng với bệnh nhân đã dùng protamine trước đó - tăng nguy cơ phản ứng",
                "Theo dõi huyết áp trong khi tiêm",
                "Đảo ngược hoàn toàn UFH, nhưng chỉ đảo ngược một phần LMWH",
                "Không dùng quá liều (có thể gây đông máu)",
                "Theo dõi aPTT sau 5-15 phút để xác nhận đảo ngược",
                "Có thể cần truyền máu nếu chảy máu nặng"
            ],
            "pharmacokinetics": {
                "half_life": "5-7 phút",
                "onset": "Ngay lập tức",
                "duration": "Phụ thuộc vào liều heparin",
                "protein_binding": "Gắn với heparin",
                "clearance": "Chuyển hóa nhanh, thải trừ qua thận"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng, dùng trong 24 giờ.",
            "black_box_warnings": "Phản ứng dị ứng nghiêm trọng, có thể gây sốc phản vệ và tử vong. Đặc biệt nguy hiểm ở bệnh nhân dị ứng cá hoặc đã dùng protamine trước đó. Tiêm IV chậm và theo dõi sát.",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["cardiovascular", "respiratory", "immunologic"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Blood pressure (hypotension common - Black Box Warning)", "aPTT (after 5-15 min to confirm reversal)", "Signs of allergic reaction/anaphylaxis (Black Box Warning - especially in fish allergy)", "Heart rate (bradycardia)", "Signs of bleeding"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Severe Allergic Reactions/Anaphylaxis (can be fatal)",
                "FDA Black Box Warning - Fish Allergy (increased risk)",
                "ACC/AHA Guidelines - Anticoagulation Reversal",
                "WHO Essential Medicines List"
            ],
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng protamine",
                    "Dị ứng cá (tăng nguy cơ phản ứng dị ứng)"
                ],
                "tương_đối": [
                    "Đã dùng protamine trước đó - tăng nguy cơ phản ứng",
                    "Bệnh nhân có tiền sử phản ứng dị ứng nặng - thận trọng"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng protamine",
                    "Dị ứng cá (tăng nguy cơ phản ứng dị ứng)"
                ],
                "tương_đối": [
                    "Đã dùng protamine trước đó - tăng nguy cơ phản ứng",
                    "Bệnh nhân có tiền sử phản ứng dị ứng nặng - thận trọng"
                ]
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Không cần chỉnh liều",
                "under_30": "Thận trọng, có thể cần giảm liều",
                "dialysis": "Thận trọng, giảm liều. Protamine thải trừ qua thận.",
                "notes": "Protamine thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy."
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần thiết. Protamine được dùng để đảo ngược heparin trong phẫu thuật tim mạch ở phụ nữ có thai.",
                "lactation": {
                    "safety": "Unknown",
                    "details": "Không rõ protamine có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng.",
                    "recommendation": "Thận trọng khi dùng khi cho con bú."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Không đổi",
                "notes": "Protamine không chuyển hóa ở gan. Suy gan không ảnh hưởng đến protamine."
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nghiêm trọng",
                    "Suy hô hấp",
                    "Bradycardia",
                    "Đông máu (nếu quá liều)",
                    "Phản ứng dị ứng nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng protamine ngay lập tức",
                    "Hỗ trợ hô hấp (intubation nếu cần)",
                    "Truyền dịch, vasopressors nếu hạ huyết áp",
                    "Điều trị phản ứng dị ứng (epinephrine, corticosteroid, antihistamine)",
                    "Theo dõi aPTT, dấu hiệu chảy máu hoặc đông máu"
                ],
                "monitoring": "Huyết áp, nhịp tim, hô hấp, aPTT, dấu hiệu dị ứng"
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha loãng trong NS hoặc D5W (10mg/ml)",
                    "infusion_rate": "Tiêm IV CHẬM trong 10 phút (không quá 5mg/phút)",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": [],
                    "notes": "Tiêm IV chậm trong 10 phút. Theo dõi huyết áp trong khi tiêm. Liều: 1mg protamine cho mỗi 100 units heparin (tối đa 50mg)."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Protamine sulfate",
                    "UpToDate - Protamine: Drug information",
                    "ACCP Guidelines - Anticoagulant reversal"
                ],
                "last_updated": "2025-02-05",
                "evidence_level": "High - FDA-approved, widely used in clinical practice"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Severe allergic reactions (anaphylaxis) - CRITICAL", "Hypotension", "Respiratory depression"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Blood pressure - CRITICAL (during and after injection)", "aPTT (after 5-15 minutes to confirm reversal)", "Signs of allergic reaction (rash, dyspnea, anaphylaxis) - CRITICAL", "Heart rate (bradycardia)", "Signs of bleeding (check if bleeding persists after reversal)"]
            },
            "guideline_tags": [
                "ACCP Guidelines - Anticoagulant Reversal",
                "AHA/ACC Guidelines - Anticoagulant Reversal",
                "FDA Black Box Warning - Protamine and Anaphylaxis",
                "FDA Drug Information - Protamine"
            ]
        },

        "Vitamin K": {
            "group": "Hematology - Anticoagulant Reversal Agent / Vitamin",
            "vietnamese_name": "Vitamin K, Phytomenadione, Phytonadione",
            "administration": ["PO", "IV", "SC", "IM"],
            "indications": [
                "Đảo ngược warfarin (quá liều hoặc chảy máu)",
                "Thiếu vitamin K (thiếu máu, chảy máu)",
                "Dự phòng chảy máu ở trẻ sơ sinh",
                "Bệnh nhân kém hấp thu chất béo",
                "Đang dùng kháng sinh dài ngày"
            ],
            "contraindications": [
                "Dị ứng vitamin K",
                "Không dùng IV nhanh (có thể gây sốc phản vệ)"
            ],
            "dosage": {
                "adult_warfarin_reversal_minor": "1-2.5mg PO x 1 lần",
                "adult_warfarin_reversal_major": "5-10mg IV chậm",
                "adult_deficiency": "10mg SC/IM x 1 lần/ngày x 3 ngày",
                "pediatric_newborn": "0.5-1mg IM x 1 lần (dự phòng)",
                "notes": "IV phải tiêm chậm (không quá 1mg/phút). PO tác dụng chậm hơn (6-12 giờ)."
            },
            "side_effects": [
                "Phản ứng dị ứng (IV nhanh)",
                "Đỏ da tại chỗ tiêm (IV)",
                "Huyết khối (IV nhanh, hiếm)",
                "Tăng bilirubin (trẻ sơ sinh, liều cao)"
            ],
            "interactions": [
                "Warfarin: đảo ngược tác dụng",
                "Cholestyramine: giảm hấp thu vitamin K",
                "Antibiotics: có thể giảm vitamin K (do giảm vi khuẩn đường ruột)"
            ],
            "pregnancy": "C",
            "mechanism_of_action": "Vitamin K là vitamin tan trong chất béo, cần thiết cho tổng hợp các yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X) và các protein chống đông (protein C, protein S). Vitamin K hoạt động như cofactor cho enzyme gamma-glutamyl carboxylase, tham gia vào quá trình carboxyl hóa các yếu tố đông máu. Warfarin ức chế vitamin K epoxide reductase, ngăn chặn tái chế vitamin K, dẫn đến giảm tổng hợp các yếu tố đông máu. Bổ sung vitamin K đảo ngược tác dụng của warfarin bằng cách cung cấp vitamin K để tổng hợp lại các yếu tố đông máu. Vitamin K có thể dùng đường uống (tác dụng chậm, 6-12 giờ), tiêm dưới da, tiêm bắp, hoặc tiêm tĩnh mạch (tác dụng nhanh hơn nhưng nguy hiểm hơn).",
            "monitoring": [
                "INR (sau 6-12 giờ với PO, sau 2-4 giờ với IV) - theo dõi đảo ngược warfarin",
                "Dấu hiệu chảy máu (xem có còn chảy máu sau đảo ngược)",
                "Dấu hiệu phản ứng dị ứng (đặc biệt với IV)",
                "Huyết áp, nhịp tim (với IV)",
                "Bilirubin (trẻ sơ sinh, liều cao)"
            ],
            "precautions": [
                "IV phải tiêm CHẬM (không quá 1mg/phút) - tiêm nhanh có thể gây sốc phản vệ",
                "PO tác dụng chậm hơn (6-12 giờ) - phù hợp cho đảo ngược nhẹ",
                "IV tác dụng nhanh hơn (2-4 giờ) - phù hợp cho chảy máu nặng",
                "Có thể cần FFP hoặc PCC nếu chảy máu nặng (vitamin K tác dụng chậm)",
                "Thận trọng với trẻ sơ sinh (liều cao có thể gây tăng bilirubin)",
                "Cần chất béo để hấp thu tốt (đường uống)",
                "Không dùng IV nhanh - nguy cơ sốc phản vệ"
            ],
            "pharmacokinetics": {
                "half_life": "1-2 giờ (vitamin K1)",
                "onset": "2-4 giờ (IV), 6-12 giờ (PO)",
                "duration": "24-48 giờ",
                "protein_binding": "Không đáng kể",
                "clearance": "Gan: chuyển hóa. Thận: bài tiết một phần."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch IV: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
            "black_box_warnings": "Tiêm IV nhanh có thể gây sốc phản vệ và tử vong. Phải tiêm IV chậm (không quá 1mg/phút).",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Warfarin",
                        "mechanism": "Vitamin K đảo ngược tác dụng warfarin",
                        "effect": "Giảm hiệu quả warfarin, giảm INR",
                        "management": "Dùng để đảo ngược warfarin khi quá liều hoặc chảy máu. Sau đó cần điều chỉnh lại liều warfarin."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Cholestyramine",
                        "mechanism": "Giảm hấp thu vitamin K",
                        "effect": "Giảm hiệu quả vitamin K",
                        "management": "Cách xa ít nhất 2 giờ."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng vitamin K",
                    "Tiêm IV nhanh - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Trẻ sơ sinh - thận trọng với liều cao (tăng bilirubin)"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng vitamin K",
                    "Tiêm IV nhanh - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Trẻ sơ sinh - thận trọng với liều cao (tăng bilirubin)"
                ]
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Không cần chỉnh liều",
                "under_30": "Không cần chỉnh liều",
                "dialysis": "Không cần chỉnh liều",
                "notes": "Vitamin K chủ yếu chuyển hóa ở gan, không cần điều chỉnh liều ở suy thận."
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần thiết. Vitamin K an toàn trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Vitamin K bài tiết vào sữa mẹ. An toàn cho trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Thận trọng",
                "notes": "Vitamin K chuyển hóa ở gan. Suy gan nặng có thể ảnh hưởng đến chuyển hóa."
            },
            "overdose_management": {
                "symptoms": [
                    "Phản ứng dị ứng (đặc biệt với IV)",
                    "Huyết khối (IV nhanh, hiếm)",
                    "Tăng bilirubin (trẻ sơ sinh, liều cao)"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng vitamin K nếu có phản ứng",
                    "Điều trị phản ứng dị ứng nếu có",
                    "Theo dõi INR (có thể quá đảo ngược)",
                    "Theo dõi bilirubin (trẻ sơ sinh)"
                ],
                "monitoring": "INR, dấu hiệu dị ứng, bilirubin (trẻ sơ sinh)"
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Nên dùng với thức ăn có chất béo để tăng hấp thu",
                    "timing": "Dùng 1 lần. Tác dụng chậm (6-12 giờ). Phù hợp cho đảo ngược warfarin nhẹ."
                },
                "iv": {
                    "reconstitution": "Pha loãng trong NS hoặc D5W (1mg/ml)",
                    "infusion_rate": "Tiêm IV CHẬM (không quá 1mg/phút)",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": [],
                    "notes": "Tiêm IV chậm (không quá 1mg/phút). Theo dõi huyết áp, dấu hiệu dị ứng. Tác dụng nhanh (2-4 giờ). Phù hợp cho chảy máu nặng."
                },
                "sc_im": {
                    "reconstitution": "Dùng trực tiếp từ lọ",
                    "injection_site": "Tiêm dưới da hoặc tiêm bắp",
                    "notes": "Tác dụng trung bình (4-6 giờ). Phù hợp cho thiếu vitamin K."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Vitamin K (Phytonadione)",
                    "UpToDate - Vitamin K: Drug information",
                    "ACCP Guidelines - Warfarin reversal"
                ],
                "last_updated": "2025-02-05",
                "evidence_level": "High - FDA-approved, widely used in clinical practice"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["INR", "Blood pressure", "Allergic reactions"]
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "ACCP Guidelines - Warfarin Reversal",
                "FDA Black Box Warning - IV Administration"
            ]
        },

}

__all__ = ['REVERSAL_AGENTS_DRUGS']
