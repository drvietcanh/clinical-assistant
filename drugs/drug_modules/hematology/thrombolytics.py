"""
Hematology Drugs - Thrombolytics
"""
from typing import Dict, Any


THROMBOLYTICS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Alteplase": {
            "group": "Hematology - Thrombolytic (tPA)",
            "vietnamese_name": "Alteplase, rt-PA",
            "administration": ["IV"],
            "indications": [
                "Đột quỵ thiếu máu não cấp (AIS) trong cửa sổ 3–4.5 giờ",
                "Nhồi máu cơ tim cấp (STEMI) khi không thể PCI kịp thời",
                "Thuyên tắc phổi (PE) nguy kịch/huyết động không ổn định"
            ],
            "contraindications": [
                "Bất kỳ chảy máu nội sọ hoặc xuất huyết nội sọ trước đây",
                "Đột quỵ xuất huyết hoặc nhồi máu não gần đây (thường <3 tháng, tùy chỉ định)",
                "Phẫu thuật lớn, chấn thương nặng gần đây",
                "Huyết áp rất cao không kiểm soát",
                "Rối loạn đông máu nặng, giảm tiểu cầu rõ"
            ],
            "dosage": {
                "stroke_adult": "0.9 mg/kg (tối đa 90mg): 10% bolus IV trong 1 phút, 90% truyền trong 60 phút",
                "stemi_adult": "15mg bolus IV, sau đó 0.75mg/kg (tối đa 50mg) trong 30 phút, tiếp theo 0.5mg/kg (tối đa 35mg) trong 60 phút",
                "pe_adult": "100mg truyền IV trong 2 giờ (hoặc protocol tại bệnh viện)",
                "notes": "TUÂN THỦ chặt chẽ protocol từng chỉ định (AIS/STEMI/PE) và kiểm tra checklist chống chỉ định trước khi dùng."
            },
            "side_effects": [
                "Chảy máu lớn (xuất huyết nội sọ, xuất huyết tiêu hóa)",
                "Chảy máu tại vị trí chọc kim, catheter",
                "Hạ huyết áp thoáng qua",
                "Phản vệ (hiếm)"
            ],
            "interactions": [
                "Heparin, enoxaparin, DOACs, warfarin: tăng mạnh nguy cơ chảy máu",
                "Thuốc kháng tiểu cầu (aspirin, clopidogrel): tăng nguy cơ chảy máu"
            ],
            "pregnancy": "C - Cân nhắc rất thận trọng, chỉ dùng khi lợi ích vượt xa nguy cơ",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": True,
                "bleeding_risk": "Very High",
                "organ_toxicity": []
            },
            "guideline_tags": [
                "AHA/ASA AIS tPA (0.9 mg/kg)",
                "ESC STEMI thrombolysis",
                "CHEST PE thrombolysis"
            ],
            "mechanism_of_action": "Alteplase là tissue plasminogen activator (tPA) tái tổ hợp. Gắn vào fibrin trong cục huyết khối và chuyển plasminogen thành plasmin, từ đó phân giải fibrin và làm tan cục máu đông. Tác dụng mạnh nhất trên huyết khối mới hình thành.",
            "monitoring": [
                "Dấu hiệu thần kinh mỗi 15 phút trong và sau truyền (AIS)",
                "Dấu hiệu chảy máu (da, niêm mạc, tiêu hóa, tiểu máu)",
                "Huyết áp, mạch, SpO2 liên tục trong quá trình truyền",
                "aPTT, INR, tiểu cầu (nếu dùng kèm hoặc sau heparin/kháng đông khác)"
            ],
            "precautions": [
                "TUYỆT ĐỐI tuân thủ checklist chống chỉ định cho AIS/STEMI/PE theo guideline.",
                "Không chọc kim, đặt catheter không cần thiết trong và 24 giờ sau truyền nếu có thể tránh.",
                "Kiểm soát huyết áp trước và trong khi truyền (đặc biệt AIS).",
                "Ngừng heparin/kháng đông khác trước truyền theo khuyến cáo.",
                "Nếu nghi ngờ xuất huyết nội sọ: ngừng truyền ngay, chụp CT, xử trí cấp cứu."
            ],
            "pharmacokinetics": {
                "half_life": "4-5 phút (nhanh, do bị ức chế bởi PAI-1 và α2-antiplasmin)",
                "onset": "Ngay lập tức sau khi bắt đầu truyền",
                "duration": "Tác dụng kéo dài sau khi ngừng truyền do plasmin đã được tạo ra",
                "protein_binding": "Gắn với fibrin trong cục máu đông",
                "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Bị ức chế bởi PAI-1 và α2-antiplasmin trong huyết tương."
            },
            "storage": "Bảo quản bột đông khô trong tủ lạnh (2–8°C). Sau khi pha, dùng trong thời gian theo khuyến cáo của nhà sản xuất (thường ≤8 giờ), tránh lắc mạnh.",
            "black_box_warnings": "Nguy cơ xuất huyết nội sọ nghiêm trọng, có thể tử vong. TUYỆT ĐỐI tuân thủ checklist chống chỉ định. Không dùng ở bệnh nhân có xuất huyết nội sọ, đột quỵ xuất huyết, hoặc chống chỉ định khác.",
            "references": {
                "primary_sources": [
                    "AHA/ASA Guidelines for the Early Management of Patients With Acute Ischemic Stroke",
                    "ESC STEMI Guidelines",
                    "CHEST Guidelines for VTE",
                    "FDA Drug Label - Alteplase"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A"
            },
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C - Cân nhắc rất thận trọng, chỉ dùng khi lợi ích vượt xa nguy cơ",
                "pregnancy_details": "Category C - Cân nhắc rất thận trọng, chỉ dùng khi lợi ích vượt xa nguy cơ - cần xem xét dữ liệu an toàn thai kỳ.",
                "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Cần xem xét dữ liệu an toàn khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Thận trọng",
                "severe": "Thận trọng",
                "notes": "Cần xem xét chuyển hóa qua gan.",
            },
            "overdose_management": {
                "symptoms": [
                "Cần xem xét triệu chứng quá liều",
            ],
                "antidote": "Không có antidote đặc hiệu",
                "treatment": [
                "Ngừng ngay thuốc",
                "Hỗ trợ và điều trị triệu chứng",
                "Theo dõi dấu hiệu sinh tồn",
            ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu lâm sàng",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
            "administration_instructions": {
                "iv": {
                "reconstitution": "Cần xem xét cách pha",
                "infusion_rate": "Cần xem xét tốc độ truyền",
                "compatibility": [
                "Cần xem xét",
            ],
                "incompatibility": [
                "Cần xem xét",
            ],
                "notes": "Cần xem xét hướng dẫn cụ thể",
            },
            },
        },

        "Tenecteplase": {
            "group": "Hematology - Fibrin-specific thrombolytic (tPA variant)",
            "vietnamese_name": "Tenecteplase, TNK-tPA",
            "administration": ["IV"],
            "indications": [
                "Đột quỵ thiếu máu não cấp (AIS) trong cửa sổ 4.5 giờ – thay thế alteplase ở một số trung tâm",
                "Nhồi máu cơ tim cấp (STEMI) khi không thể PCI kịp thời",
                "Thuyên tắc phổi nguy kịch/huyết động không ổn định (off-label tại nhiều nơi)"
            ],
            "contraindications": [
                "Tiền sử hoặc bằng chứng xuất huyết nội sọ",
                "Đột quỵ xuất huyết hoặc nhồi máu não gần đây (thường <3 tháng, tùy chỉ định)",
                "Phẫu thuật lớn hoặc chấn thương nặng gần đây",
                "Huyết áp rất cao không kiểm soát",
                "Rối loạn đông máu nặng, giảm tiểu cầu rõ",
            ],
            "dosage": {
                "stroke_adult": "0.25 mg/kg IV bolus (tối đa 25mg) một lần duy nhất trong AIS; không khuyến cáo liều 0.4 mg/kg do nguy cơ xuất huyết cao hơn",
                "stemi_adult": "Bolus IV duy nhất: <60kg: 30mg; 60-69kg: 35mg; 70-79kg: 40mg; 80-89kg: 45mg; ≥90kg: 50mg",
                "pe_adult": "0.5 mg/kg IV bolus (tối đa 50mg) – off-label, tùy protocol bệnh viện",
                "notes": "Đảm bảo đáp ứng checklist chống chỉ định trước dùng. Không pha chung với heparin/kháng đông khác trong cùng đường truyền.",
            },
            "side_effects": [
                "Xuất huyết nội sọ (nguy cơ thấp nhưng nghiêm trọng)",
                "Chảy máu tiêu hóa, chảy máu chỗ chọc kim",
                "Hạ huyết áp thoáng qua",
                "Phản vệ (rất hiếm)",
            ],
            "interactions": [
                "Heparin, enoxaparin, DOACs, warfarin: tăng nguy cơ chảy máu",
                "Thuốc kháng tiểu cầu (aspirin, clopidogrel): tăng nguy cơ chảy máu",
            ],
            "pregnancy": "C - Cân nhắc thận trọng, chỉ dùng khi lợi ích vượt trội nguy cơ",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": True,
                "bleeding_risk": "Very High",
                "organ_toxicity": []
            },
            "guideline_tags": [
                "AHA/ASA AIS thrombolysis (0.25 mg/kg bolus centers)",
                "ESC STEMI thrombolysis",
                "CHEST/PE off-label (institutional protocols)"
            ],
            "mechanism_of_action": (
                "Tenecteplase là biến thể tái tổ hợp của tPA với ái lực fibrin cao hơn và kháng PAI-1, "
                "chuyển plasminogen thành plasmin tại cục huyết khối, phân giải fibrin và làm tan huyết khối."
            ),
            "monitoring": [
                "Dấu hiệu thần kinh và NIHSS (AIS) mỗi 15 phút trong và sau bolus, sau đó thưa dần",
                "Huyết áp, mạch, SpO2 liên tục trong 24 giờ đầu",
                "Dấu hiệu chảy máu (da, niêm mạc, tiêu hóa, tiểu máu)",
                "aPTT/INR/tiểu cầu nếu dùng hoặc dự định dùng kháng đông khác",
            ],
            "precautions": [
                "Tuân thủ checklist chống chỉ định tương tự alteplase cho AIS/STEMI.",
                "Tránh chọc kim/đặt catheter không cần thiết trong 24 giờ sau dùng.",
                "Kiểm soát huyết áp trước và sau tiêm (AIS: mục tiêu <185/110 mmHg trước dùng).",
                "Nếu nghi ngờ xuất huyết nội sọ: dừng ngay, chụp CT, xử trí cấp cứu.",
            ],
            "pharmacokinetics": {
                "half_life": "Pha alpha ~20 phút; pha beta ~90-130 phút (dài hơn alteplase)",
                "onset": "Ngay sau bolus",
                "duration": "Hiệu ứng tiêu sợi huyết kéo dài vài giờ",
                "protein_binding": "Gắn fibrin tại huyết khối",
                "clearance": "Gan (chuyển hóa), thận thải trừ một phần",
            },
            "storage": "Bảo quản bột đông khô ở 2–8°C. Sau pha theo hướng dẫn chế phẩm, dùng trong thời gian khuyến cáo; tránh lắc mạnh.",
            "black_box_warnings": "Nguy cơ xuất huyết nội sọ và chảy máu lớn. Chỉ dùng khi đáp ứng tiêu chuẩn lựa chọn và không có chống chỉ định.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Heparin/Enoxaparin/DOACs/Warfarin",
                        "mechanism": "Tăng hiệu ứng chống đông trên nền tiêu sợi huyết",
                        "effect": "Tăng mạnh nguy cơ chảy máu",
                        "management": "Tránh chồng lấp không cần thiết. Nếu phải dùng, theo dõi sát chảy máu và xét nghiệm đông máu.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin, Clopidogrel, Ticagrelor",
                        "mechanism": "Cộng hưởng ức chế kết tập tiểu cầu",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng; giám sát chảy máu. Thường vẫn dùng sau tái tưới máu theo guideline nhưng cần kiểm soát nguy cơ.",
                    }
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Xuất huyết nội sọ hoặc xuất huyết hoạt động",
                    "Đột quỵ xuất huyết/nhồi máu não trong 3 tháng (trừ AIS hiện tại)",
                    "Phẫu thuật lớn hoặc chấn thương nặng trong 3 tuần gần đây",
                    "U não, dị dạng mạch não, phình mạch chưa xử trí",
                    "Tiểu cầu <100.000/mm³, INR >1.7 (không do dùng thuốc), aPTT kéo dài không rõ nguyên nhân",
                ],
                "tương_đối": [
                    "HA >185/110 mmHg (AIS) hoặc >180/110 (STEMI) chưa kiểm soát",
                    "Đái tháo đường kèm đột quỵ cũ (tùy guideline AIS)",
                    "Mang thai hoặc hậu sản <10 ngày",
                    "Viêm nội tâm mạc nhiễm khuẩn nghi ngờ",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Dữ liệu rất hạn chế; cân nhắc nếu lợi ích cứu mạng vượt nguy cơ chảy máu cho mẹ/thai.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Không rõ bài tiết sữa; phân tử lớn, hấp thu đường tiêu hóa kém ở trẻ.",
                    "recommendation": "Có thể tiếp tục cho bú sau 24 giờ nếu mẹ ổn định; theo dõi chảy máu ở trẻ.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh",
                "moderate": "Không cần chỉnh nhưng thận trọng",
                "severe": "Tránh nếu có rối loạn đông máu nặng do suy gan",
            },
            "overdose_management": {
                "symptoms": ["Chảy máu lớn, xuất huyết nội sọ, tụt huyết áp"],
                "antidote": "Không có antidote đặc hiệu; có thể dùng các sản phẩm máu/thuốc chống tiêu sợi huyết",
                "treatment": [
                    "Ngừng thuốc, ép chặt vị trí chảy máu nếu có",
                    "Truyền cryoprecipitate hoặc fibrinogen concentrate nếu giảm fibrinogen",
                    "Truyền tiểu cầu nếu giảm tiểu cầu hoặc dùng kháng tiểu cầu gần đây",
                    "Cân nhắc tranexamic acid hoặc aminocaproic acid trong xuất huyết nặng",
                    "Hồi sức tích cực, kiểm soát huyết áp, chụp CT nếu nghi xuất huyết nội sọ",
                ],
                "monitoring": "Huyết động, Hb/Hct, tiểu cầu, fibrinogen, aPTT/INR, đánh giá thần kinh lặp lại",
            },
            "reversal_agents": {
                "available": False,
                "agents": ["Tranexamic acid (supportive)", "Cryoprecipitate/fibrinogen concentrate"],
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha bột theo hướng dẫn chế phẩm; thường pha với nước pha tiêm rồi pha loãng nếu cần",
                    "infusion_rate": "Tiêm IV bolus chậm trong 5–10 giây (AIS/STEMI)",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": ["Không truyền chung heparin/kháng đông cùng đường IV"],
                    "notes": "Chuẩn bị sẵn bộ hồi sức và phương án xử trí xuất huyết.",
                }
            },
            "references": {
                "primary_sources": [
                    "AHA/ASA 2023–2024 updates on Tenecteplase for AIS (0.25 mg/kg bolus)",
                    "ESC STEMI Guidelines (tenecteplase bolus)",
                    "CHEST/Institutional protocols for PE thrombolysis (off-label)",
                    "FDA Drug Label - Tenecteplase (STEMI)",
                ],
                "last_updated": "2025-03-02",
                "evidence_level": "A (STEMI), B (AIS – trung tâm chọn lọc)",
            },
        },

}

__all__ = ['THROMBOLYTICS_DRUGS']
