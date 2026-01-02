"""
Hematology Drugs - Anticoagulants
"""
from typing import Dict, Any


ANTICOAGULANTS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Apixaban": {
            "group": "Hematology - Anticoagulant (Direct Factor Xa Inhibitor, DOAC)",
            "vietnamese_name": "Apixaban, Eliquis",
            "administration": ["PO"],
            "indications": [
                "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
                "Điều trị DVT/PE",
                "Phòng ngừa DVT sau phẫu thuật thay khớp háng/gối",
                "Phòng ngừa huyết khối sau hội chứng mạch vành cấp (với aspirin)"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <15)",
                "Có thai",
                "Dị ứng apixaban"
            ],
            "dosage": {
                "adult_afib": "5mg x 2 lần/ngày (2.5mg nếu ≥2 trong: tuổi ≥80, cân nặng ≤60kg, creatinine ≥1.5mg/dL)",
                "adult_dvt_pe": "10mg x 2 lần/ngày x 7 ngày, sau đó 5mg x 2 lần/ngày",
                "adult_prophylaxis": "2.5mg x 2 lần/ngày",
                "adult_acs": "5mg x 2 lần/ngày (với aspirin)",
                "notes": "Điều chỉnh liều theo chức năng thận và các yếu tố khác. Không cần theo dõi INR/aPTT thường xuyên"
            },
            "side_effects": [
                "Chảy máu (phổ biến)",
                "Rối loạn tiêu hóa",
                "Nhức đầu"
            ],
            "interactions": [
                "CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir): tăng nồng độ (tránh dùng)",
                "CYP3A4 và P-gp inducers (rifampin): giảm nồng độ",
                "Aspirin/NSAID: tăng nguy cơ chảy máu"
            ],
            "pregnancy": "C - Tránh dùng",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "bleeding_risk": "High",
                "icu_critical_care_only": False
            },
            "guideline_tags": [
                "AHA/ACC/HRS AF stroke prevention",
                "ESC AF guidelines",
                "ISTH VTE treatment/prophylaxis"
            ],
            "mechanism_of_action": "Apixaban là direct factor Xa inhibitor, ức chế trực tiếp yếu tố Xa mà không cần antithrombin III. Apixaban gắn trực tiếp với Xa, ngăn chặn chuyển đổi prothrombin thành thrombin, ức chế hình thành cục máu đông. Thuốc là DOAC (direct oral anticoagulant), không cần theo dõi INR/aPTT thường xuyên như warfarin. Apixaban được thải trừ một phần qua thận (25%) và một phần qua gan (75%), nên cần điều chỉnh liều ở suy thận nặng. Có antidote đặc hiệu: andexanet alfa (Andexxa).",
            "monitoring": [
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
                "Chức năng thận (CrCl) - mỗi 3-6 tháng (apixaban thải trừ một phần qua thận)",
                "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
                "Dấu hiệu rối loạn tiêu hóa"
            ],
            "precautions": [
                "Điều chỉnh liều theo chức năng thận (CrCl) và các yếu tố khác (tuổi, cân nặng) - mỗi 3-6 tháng",
                "Suy thận nặng (CrCl <15) - chống chỉ định",
                "Giảm liều xuống 2.5mg x 2 lần/ngày nếu ≥2 trong: tuổi ≥80, cân nặng ≤60kg, creatinine ≥1.5mg/dL",
                "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
                "Có antidote đặc hiệu: andexanet alfa (Andexxa) - đảo ngược tác dụng",
                "Tránh dùng với CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir) - tăng nồng độ",
                "Ngừng 1-2 ngày trước phẫu thuật lớn (tùy chức năng thận)",
                "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
            ],
            "pharmacokinetics": {
                "half_life": "12 giờ (bình thường), 15-18 giờ (suy thận)",
                "onset": "3-4 giờ",
                "duration": "12-24 giờ",
                "protein_binding": "87%",
                "clearance": "Gan (75% - chuyển hóa qua CYP3A4). Thận (25% - thải trừ nguyên dạng). Cần điều chỉnh liều ở suy thận nặng."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Suy thận nặng (CrCl <15) - chống chỉ định. Không ngừng đột ngột (tăng nguy cơ đột quỵ trong rung nhĩ).",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)",
                        "mechanism": "Ức chế CYP3A4 và P-gp, tăng nồng độ apixaban",
                        "effect": "Tăng nồng độ apixaban, tăng nguy cơ chảy máu",
                        "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng CYP3A4 và P-gp inhibitors mạnh."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin, NSAIDs",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                    },
                    {
                        "drug": "CYP3A4 và P-gp inducers (rifampin)",
                        "mechanism": "Cảm ứng CYP3A4 và P-gp, giảm nồng độ apixaban",
                        "effect": "Giảm nồng độ apixaban, giảm hiệu quả",
                        "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Suy thận nặng (CrCl <15) - chống chỉ định",
                    "Dị ứng apixaban",
                    "Dùng CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)"
                ],
                "tương_đối": [
                    "Suy thận (CrCl 15-30) - thận trọng, có thể cần giảm liều",
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Có thai - tránh dùng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Tránh dùng trong thai kỳ. Apixaban có thể gây chảy máu ở mẹ và thai nhi. Chỉ dùng nếu lợi ích > nguy cơ rõ ràng.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Apixaban có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                    "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Thận trọng",
                "severe": "CHỐNG CHỈ ĐỊNH",
                "notes": "Apixaban chuyển hóa chủ yếu qua gan (CYP3A4 - 75%). Không cần điều chỉnh liều ở suy gan nhẹ. Thận trọng ở suy gan trung bình. Chống chỉ định ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
                ],
                "antidote": "Andexanet alfa (Andexxa) - antidote đặc hiệu",
                "treatment": [
                    "Ngừng apixaban ngay lập tức",
                    "Andexanet alfa (Andexxa): 400-800mg IV bolus, sau đó 4-8mg/phút x 2 giờ - đảo ngược tác dụng",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                    "Rửa dạ dày nếu uống trong vòng 2 giờ",
                    "Than hoạt tính",
                    "Nếu không có andexanet: PCC 4 yếu tố (50 IU/kg) + than hoạt sớm",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                    "Theo dõi ít nhất 24 giờ (do half-life 12 giờ)"
                ],
                "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "name": "Andexanet alfa (Andexxa)",
                        "indication": "Đảo ngược tác dụng apixaban, rivaroxaban (chảy máu nặng hoặc phẫu thuật cấp cứu)",
                        "dose": "400-800mg IV bolus, sau đó 4-8mg/phút x 2 giờ",
                        "notes": "Antidote đặc hiệu cho apixaban và rivaroxaban. Đảo ngược tác dụng nhanh chóng."
                    }
                ]
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                    "timing": "Uống 2 lần/ngày (sáng và tối), cách nhau 12 giờ. AFib: 5mg x 2 lần/ngày (2.5mg nếu ≥2 trong: tuổi ≥80, cân nặng ≤60kg, creatinine ≥1.5mg/dL). DVT/PE: 10mg x 2 lần/ngày x 7 ngày, sau đó 5mg x 2 lần/ngày."
                },
                "iv": None
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Eliquis (apixaban)",
                    "ARISTOTLE Study - New England Journal of Medicine",
                    "UpToDate - Apixaban: Drug information"
                ],
                "last_updated": "2025-02-05",
                "evidence_level": "High (FDA-approved, large RCT - ARISTOTLE study)"
            }
        },

        "Dabigatran": {
            "group": "Hematology - Anticoagulant (Direct Thrombin Inhibitor, DOAC)",
            "vietnamese_name": "Dabigatran, Pradaxa",
            "administration": ["PO"],
            "indications": [
                "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
                "Điều trị DVT/PE",
                "Phòng ngừa DVT sau phẫu thuật thay khớp háng/gối"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <30)",
                "Có thai",
                "Dị ứng dabigatran"
            ],
            "dosage": {
                "adult_afib": "150mg x 2 lần/ngày (110mg x 2 lần/ngày nếu ≥75 tuổi hoặc CrCl 30-50)",
                "adult_dvt_pe": "150mg x 2 lần/ngày",
                "adult_prophylaxis": "220mg x 1 lần/ngày (110mg nếu CrCl 30-50)",
                "notes": "Điều chỉnh liều theo chức năng thận. Không cần theo dõi INR/aPTT thường xuyên"
            },
            "side_effects": [
                "Chảy máu (phổ biến)",
                "Khó tiêu, đau bụng",
                "Rối loạn tiêu hóa"
            ],
            "interactions": [
                "P-gp inhibitors (ketoconazole, dronedarone): tăng nồng độ (tránh dùng)",
                "P-gp inducers (rifampin): giảm nồng độ",
                "Aspirin/NSAID: tăng nguy cơ chảy máu"
            ],
            "pregnancy": "C - Tránh dùng",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": "High",
                "organ_toxicity": []
            },
            "guideline_tags": [
                "AHA/ACC/HRS AF stroke prevention",
                "ISTH VTE treatment/prophylaxis",
                "ESC AF guidelines"
            ],
            "mechanism_of_action": "Dabigatran là direct thrombin inhibitor (DTI), ức chế trực tiếp thrombin (yếu tố IIa) mà không cần antithrombin III. Dabigatran gắn trực tiếp với thrombin, ngăn chặn chuyển đổi fibrinogen thành fibrin, ức chế hình thành cục máu đông. Thuốc là DOAC (direct oral anticoagulant), không cần theo dõi INR/aPTT thường xuyên như warfarin. Dabigatran được thải trừ chủ yếu qua thận (80%), nên cần điều chỉnh liều ở suy thận. Có antidote đặc hiệu: idarucizumab (Praxbind).",
            "monitoring": [
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
                "Chức năng thận (CrCl) - mỗi 3-6 tháng (dabigatran thải trừ qua thận)",
                "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
                "Dấu hiệu rối loạn tiêu hóa (khó tiêu, đau bụng)"
            ],
            "precautions": [
                "Điều chỉnh liều theo chức năng thận (CrCl) - mỗi 3-6 tháng",
                "Suy thận nặng (CrCl <30) - chống chỉ định",
                "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
                "Có antidote đặc hiệu: idarucizumab (Praxbind) - đảo ngược tác dụng",
                "Tránh dùng với P-gp inhibitors mạnh (ketoconazole, dronedarone) - tăng nồng độ",
                "Ngừng 1-2 ngày trước phẫu thuật lớn (tùy chức năng thận)",
                "Uống với thức ăn để giảm rối loạn tiêu hóa",
                "Không mở viên nang (tăng hấp thu, tăng nguy cơ chảy máu)"
            ],
            "pharmacokinetics": {
                "half_life": "12-17 giờ (bình thường), 18-27 giờ (suy thận)",
                "onset": "1-2 giờ",
                "duration": "12-24 giờ",
                "protein_binding": "35%",
                "clearance": "Thận (80% - thải trừ nguyên dạng). Gan (20% - chuyển hóa). Cần điều chỉnh liều ở suy thận."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Giữ trong bao bì gốc. Không mở viên nang.",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Suy thận nặng (CrCl <30) - chống chỉ định. Không ngừng đột ngột (tăng nguy cơ đột quỵ trong rung nhĩ).",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "P-gp inhibitors mạnh (ketoconazole, dronedarone)",
                        "mechanism": "Ức chế P-gp, tăng nồng độ dabigatran",
                        "effect": "Tăng nồng độ dabigatran, tăng nguy cơ chảy máu",
                        "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng P-gp inhibitors mạnh."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin, NSAIDs",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                    },
                    {
                        "drug": "P-gp inducers (rifampin)",
                        "mechanism": "Cảm ứng P-gp, giảm nồng độ dabigatran",
                        "effect": "Giảm nồng độ dabigatran, giảm hiệu quả",
                        "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Suy thận nặng (CrCl <30) - chống chỉ định",
                    "Dị ứng dabigatran",
                    "Dùng P-gp inhibitors mạnh (ketoconazole, dronedarone)"
                ],
                "tương_đối": [
                    "Suy thận (CrCl 30-50) - giảm liều (110mg x 2 lần/ngày)",
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Có thai - tránh dùng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Tránh dùng trong thai kỳ. Dabigatran có thể gây chảy máu ở mẹ và thai nhi. Chỉ dùng nếu lợi ích > nguy cơ rõ ràng.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dabigatran có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                    "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Thận trọng",
                "notes": "Dabigatran chuyển hóa một phần qua gan (20%). Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Thận trọng ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
                ],
                "antidote": "Idarucizumab (Praxbind) - antidote đặc hiệu",
                "treatment": [
                    "Ngừng dabigatran ngay lập tức",
                    "Idarucizumab (Praxbind): 5g IV (2.5g x 2 lần, cách nhau 15 phút) - đảo ngược tác dụng",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                    "Rửa dạ dày nếu uống trong vòng 2 giờ",
                    "Than hoạt tính",
                    "Nếu không có idarucizumab: PCC 4 yếu tố (≈50 IU/kg) ± than hoạt; lọc máu có thể giúp do thải qua thận",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                    "Theo dõi ít nhất 24 giờ (do half-life 12-17 giờ)"
                ],
                "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "name": "Idarucizumab (Praxbind)",
                        "indication": "Đảo ngược tác dụng dabigatran (chảy máu nặng hoặc phẫu thuật cấp cứu)",
                        "dose": "5g IV (2.5g x 2 lần, cách nhau 15 phút)",
                        "notes": "Antidote đặc hiệu cho dabigatran. Đảo ngược tác dụng nhanh chóng."
                    }
                ]
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể dùng với hoặc không có thức ăn. Uống với thức ăn để giảm rối loạn tiêu hóa.",
                    "timing": "Uống 2 lần/ngày (sáng và tối), cách nhau 12 giờ. AFib: 150mg x 2 lần/ngày (110mg nếu ≥75 tuổi hoặc CrCl 30-50). DVT/PE: 150mg x 2 lần/ngày. KHÔNG MỞ VIÊN NANG.",
                    "notes": "KHÔNG MỞ VIÊN NANG - tăng hấp thu, tăng nguy cơ chảy máu. Uống với thức ăn để giảm rối loạn tiêu hóa."
                },
                "iv": None
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Pradaxa (dabigatran)",
                    "RE-LY Study - New England Journal of Medicine",
                    "UpToDate - Dabigatran: Drug information"
                ],
                "last_updated": "2025-02-05",
                "evidence_level": "High (FDA-approved, large RCT - RE-LY study)"
            }
        },

        "Edoxaban": {
            "group": "Hematology - Anticoagulant (Direct Factor Xa Inhibitor, DOAC)",
            "vietnamese_name": "Edoxaban, Lixiana, Savaysa",
            "administration": ["PO"],
            "indications": [
                "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
                "Điều trị DVT/PE"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <15)",
                "Có thai",
                "Dị ứng edoxaban"
            ],
            "dosage": {
                "adult_afib": "60mg x 1 lần/ngày (30mg nếu CrCl 15-50, cân nặng ≤60kg, hoặc dùng P-gp inhibitors)",
                "adult_dvt_pe": "60mg x 1 lần/ngày (30mg nếu CrCl 15-50, cân nặng ≤60kg, hoặc dùng P-gp inhibitors)",
                "notes": "Điều chỉnh liều theo chức năng thận, cân nặng, và tương tác thuốc. Không cần theo dõi INR/aPTT thường xuyên"
            },
            "side_effects": [
                "Chảy máu (phổ biến)",
                "Rối loạn tiêu hóa",
                "Nhức đầu"
            ],
            "interactions": [
                "P-gp inhibitors mạnh (ketoconazole, dronedarone): tăng nồng độ (giảm liều xuống 30mg)",
                "P-gp inducers (rifampin): giảm nồng độ",
                "Aspirin/NSAID: tăng nguy cơ chảy máu"
            ],
            "pregnancy": "C - Tránh dùng",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "bleeding_risk": "High",
                "icu_critical_care_only": False
            },
            "guideline_tags": [
                "AHA/ACC/HRS AF stroke prevention",
                "ISTH VTE treatment/prophylaxis",
                "ESC AF guidelines"
            ],
            "mechanism_of_action": "Edoxaban là direct factor Xa inhibitor, ức chế trực tiếp yếu tố Xa mà không cần antithrombin III. Edoxaban gắn trực tiếp với Xa, ngăn chặn chuyển đổi prothrombin thành thrombin, ức chế hình thành cục máu đông. Thuốc là DOAC (direct oral anticoagulant), không cần theo dõi INR/aPTT thường xuyên như warfarin. Edoxaban được thải trừ chủ yếu qua thận (50%) và một phần qua gan (50%), nên cần điều chỉnh liều ở suy thận. Không có antidote đặc hiệu (khác apixaban, rivaroxaban).",
            "monitoring": [
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
                "Chức năng thận (CrCl) - mỗi 3-6 tháng (edoxaban thải trừ một phần qua thận)",
                "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
                "Dấu hiệu rối loạn tiêu hóa"
            ],
            "precautions": [
                "Điều chỉnh liều theo chức năng thận (CrCl), cân nặng, và tương tác thuốc - mỗi 3-6 tháng",
                "Suy thận nặng (CrCl <15) - chống chỉ định",
                "Giảm liều xuống 30mg x 1 lần/ngày nếu CrCl 15-50, cân nặng ≤60kg, hoặc dùng P-gp inhibitors mạnh",
                "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
                "Không có antidote đặc hiệu (khác apixaban, rivaroxaban) - điều trị hỗ trợ nếu chảy máu",
                "Tránh dùng với P-gp inhibitors mạnh (ketoconazole, dronedarone) - giảm liều xuống 30mg nếu phải dùng",
                "Ngừng 1-2 ngày trước phẫu thuật lớn (tùy chức năng thận)",
                "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
            ],
            "pharmacokinetics": {
                "half_life": "10-14 giờ (bình thường), 15-20 giờ (suy thận)",
                "onset": "1-2 giờ",
                "duration": "12-24 giờ",
                "protein_binding": "55%",
                "clearance": "Thận (50% - thải trừ nguyên dạng). Gan (50% - chuyển hóa). Cần điều chỉnh liều ở suy thận."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Suy thận nặng (CrCl <15) - chống chỉ định. Không ngừng đột ngột (tăng nguy cơ đột quỵ trong rung nhĩ).",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "P-gp inhibitors mạnh (ketoconazole, dronedarone)",
                        "mechanism": "Ức chế P-gp, tăng nồng độ edoxaban",
                        "effect": "Tăng nồng độ edoxaban, tăng nguy cơ chảy máu",
                        "management": "Giảm liều xuống 30mg x 1 lần/ngày khi dùng với P-gp inhibitors mạnh. Theo dõi dấu hiệu chảy máu."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin, NSAIDs",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                    },
                    {
                        "drug": "P-gp inducers (rifampin)",
                        "mechanism": "Cảm ứng P-gp, giảm nồng độ edoxaban",
                        "effect": "Giảm nồng độ edoxaban, giảm hiệu quả",
                        "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Suy thận nặng (CrCl <15) - chống chỉ định",
                    "Dị ứng edoxaban"
                ],
                "tương_đối": [
                    "Suy thận (CrCl 15-50) - giảm liều xuống 30mg x 1 lần/ngày",
                    "Cân nặng ≤60kg - giảm liều xuống 30mg x 1 lần/ngày",
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Có thai - tránh dùng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Tránh dùng trong thai kỳ. Edoxaban có thể gây chảy máu ở mẹ và thai nhi. Chỉ dùng nếu lợi ích > nguy cơ rõ ràng.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Edoxaban có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                    "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Thận trọng",
                "severe": "CHỐNG CHỈ ĐỊNH",
                "notes": "Edoxaban chuyển hóa một phần qua gan (50%). Không cần điều chỉnh liều ở suy gan nhẹ. Thận trọng ở suy gan trung bình. Chống chỉ định ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng edoxaban ngay lập tức",
                    "Nếu không có andexanet: PCC 4 yếu tố (≈50 IU/kg) + than hoạt sớm nếu mới uống",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                    "Rửa dạ dày nếu uống trong vòng 2 giờ",
                    "Than hoạt tính",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                    "Theo dõi ít nhất 24 giờ (do half-life 10-14 giờ)"
                ],
                "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                    "timing": "Uống 1 lần/ngày. AFib/DVT/PE: 60mg x 1 lần/ngày (30mg nếu CrCl 15-50, cân nặng ≤60kg, hoặc dùng P-gp inhibitors mạnh)."
                },
                "iv": None
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Savaysa (edoxaban)",
                    "ENGAGE AF-TIMI 48 Study - New England Journal of Medicine",
                    "UpToDate - Edoxaban: Drug information"
                ],
                "last_updated": "2025-02-05",
                "evidence_level": "High (FDA-approved, large RCT - ENGAGE AF-TIMI 48 study)"
            }
        },

        "Enoxaparin": {
            "group": "Hematology - Anticoagulant (Low Molecular Weight Heparin)",
            "vietnamese_name": "Enoxaparin, Lovenox, Clexane",
            "administration": ["SC", "IV"],
            "indications": [
                "Phòng ngừa huyết khối tĩnh mạch sâu (DVT) sau phẫu thuật",
                "Điều trị DVT/PE",
                "Hội chứng mạch vành cấp (với aspirin)",
                "Phòng ngừa DVT ở bệnh nhân nằm viện"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Giảm tiểu cầu do heparin (HIT)",
                "Dị ứng heparin/enoxaparin",
                "Suy thận nặng (CrCl <30) - thận trọng"
            ],
            "dosage": {
                "adult_prophylaxis": "40mg SC x 1 lần/ngày hoặc 30mg SC x 2 lần/ngày",
                "adult_treatment": "1mg/kg SC x 2 lần/ngày hoặc 1.5mg/kg SC x 1 lần/ngày",
                "adult_acs": "1mg/kg SC x 2 lần/ngày (với aspirin)",
                "notes": "Điều chỉnh liều theo cân nặng. Theo dõi anti-Xa nếu cần"
            },
            "side_effects": [
                "Chảy máu (phổ biến)",
                "Giảm tiểu cầu do heparin (HIT) - hiếm nhưng nguy hiểm",
                "Phản ứng tại chỗ tiêm (đau, ban đỏ)",
                "Tăng transaminase (hiếm)",
                "Loãng xương (với điều trị dài ngày)"
            ],
            "interactions": [
                "Warfarin: tăng nguy cơ chảy máu",
                "Aspirin/NSAID: tăng nguy cơ chảy máu",
                "Thrombolytics: tăng nguy cơ chảy máu"
            ],
            "pregnancy": "B - Tương đối an toàn",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hematologic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "ACCP/Antithrombotic Therapy Guidelines",
                "ESC VTE Guidelines",
                "AHA/ACC ACS Guidelines",
                "ISTH HIT Guidelines"
            ],
            "mechanism_of_action": "Enoxaparin là low molecular weight heparin (LMWH), ức chế yếu tố Xa và yếu tố IIa (thrombin) thông qua antithrombin III. Enoxaparin có tỷ lệ anti-Xa/anti-IIa cao hơn heparin không phân đoạn (UFH), nên ức chế Xa mạnh hơn. Enoxaparin có thời gian bán thải dài hơn, dự đoán được hơn, và ít gây HIT hơn UFH. Thuốc được thải trừ chủ yếu qua thận, nên cần điều chỉnh liều ở suy thận. Enoxaparin không cần theo dõi aPTT thường xuyên như UFH, nhưng có thể theo dõi anti-Xa nếu cần.",
            "monitoring": [
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
                "Công thức máu (tiểu cầu) - theo dõi HIT (giảm tiểu cầu >50% hoặc <150,000/μL)",
                "Anti-Xa nếu cần (điều trị dài ngày, suy thận, béo phì)",
                "Chức năng thận (CrCl) - enoxaparin thải trừ qua thận",
                "Dấu hiệu HIT (giảm tiểu cầu, huyết khối mới) - cấp cứu"
            ],
            "precautions": [
                "Điều chỉnh liều theo cân nặng (1mg/kg cho điều trị)",
                "Giảm tiểu cầu do heparin (HIT) - hiếm nhưng nguy hiểm, ngừng ngay nếu nghi ngờ",
                "Suy thận (CrCl <30) - giảm liều hoặc dùng UFH thay thế",
                "Không cần theo dõi aPTT thường xuyên (khác UFH)",
                "Theo dõi anti-Xa nếu cần (điều trị dài ngày, suy thận, béo phì)",
                "Ngừng 12-24 giờ trước phẫu thuật lớn (tùy liều)",
                "Protamine có thể đảo ngược một phần (không hoàn toàn như UFH)",
                "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
            ],
            "pharmacokinetics": {
                "half_life": "4-5 giờ (SC), 2-3 giờ (IV)",
                "onset": "1-2 giờ (SC)",
                "duration": "12-24 giờ",
                "protein_binding": "Không đáng kể",
                "clearance": "Thận (thải trừ chủ yếu - 40% nguyên dạng). Gan (một phần). Cần điều chỉnh liều ở suy thận."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Không rung lắc.",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Nguy cơ giảm tiểu cầu do heparin (HIT) - ngừng ngay nếu nghi ngờ. Suy thận nặng tăng nguy cơ chảy máu.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Warfarin",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                        "management": "Theo dõi INR, dấu hiệu chảy máu. Dùng đồng thời trong quá trình khởi đầu warfarin."
                    },
                    {
                        "drug": "Thrombolytics (alteplase, streptokinase)",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin, NSAIDs",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Giảm tiểu cầu do heparin (HIT) đang hoạt động hoặc tiền sử",
                    "Dị ứng heparin/enoxaparin"
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - giảm liều hoặc dùng UFH thay thế",
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Có thai - tương đối an toàn nhưng thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Tương đối an toàn trong thai kỳ. Enoxaparin không qua nhau thai do kích thước phân tử lớn. Có thể dùng trong thai kỳ nếu cần chống đông. Theo dõi chặt chẽ dấu hiệu chảy máu.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Enoxaparin không bài tiết vào sữa mẹ do kích thước phân tử lớn. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Thận trọng",
                "notes": "Enoxaparin chuyển hóa một phần qua gan. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Thận trọng ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
                ],
                "antidote": "Protamine sulfate - đảo ngược một phần (không hoàn toàn như UFH)",
                "treatment": [
                    "Ngừng enoxaparin ngay lập tức",
                    "Protamine sulfate: 1mg IV cho mỗi 1mg enoxaparin (nếu <8 giờ sau liều cuối). Nếu >8 giờ: 0.5mg protamine cho mỗi 1mg enoxaparin.",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                    "Theo dõi ít nhất 24 giờ (do half-life 4-5 giờ)"
                ],
                "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, anti-Xa nếu có"
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "name": "Protamine sulfate",
                        "indication": "Đảo ngược tác dụng enoxaparin (chảy máu nặng)",
                        "dose": "1mg IV cho mỗi 1mg enoxaparin (nếu <8 giờ sau liều cuối). Nếu >8 giờ: 0.5mg protamine cho mỗi 1mg enoxaparin. Tối đa 50mg.",
                        "notes": "Đảo ngược một phần (không hoàn toàn như UFH). Có thể gây phản ứng quá mẫn."
                    }
                ]
            },
            "administration_instructions": {
                "oral": None,
                "sc": {
                    "reconstitution": "Dùng trực tiếp, không cần pha",
                    "injection_site": "Vùng bụng (tránh rốn 5cm), đùi ngoài, hoặc cánh tay",
                    "technique": "Tiêm SC sâu, không xoa bóp sau tiêm",
                    "notes": "Tiêm SC sâu. Không xoa bóp sau tiêm. Xoay vị trí tiêm. Prophylaxis: 40mg SC x 1 lần/ngày hoặc 30mg SC x 2 lần/ngày. Treatment: 1mg/kg SC x 2 lần/ngày hoặc 1.5mg/kg SC x 1 lần/ngày."
                },
                "iv": {
                    "reconstitution": "Pha với NS hoặc D5W",
                    "infusion_rate": "Truyền IV bolus hoặc infusion",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": [],
                    "notes": "Có thể dùng IV nhưng thường dùng SC. IV thường dùng trong cấp cứu."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Lovenox (enoxaparin)",
                    "UpToDate - Enoxaparin: Drug information",
                    "American College of Chest Physicians (ACCP) guidelines"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "High (FDA-approved, extensive clinical data)"
            }
        },

        "Fondaparinux": {
            "group": "Hematology - Anticoagulant (Synthetic Factor Xa Inhibitor)",
            "vietnamese_name": "Fondaparinux, Arixtra",
            "administration": ["SC"],
            "indications": [
                "Phòng ngừa DVT sau phẫu thuật hông/gối",
                "Điều trị DVT/PE cấp",
                "Hội chứng mạch vành cấp (với aspirin)"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Giảm tiểu cầu nặng (<100,000/μL)",
                "Dị ứng fondaparinux",
                "Suy thận nặng (CrCl <30) - chống chỉ định"
            ],
            "dosage": {
                "adult_prophylaxis": "2.5mg SC x 1 lần/ngày",
                "adult_treatment_dvt_pe": "5mg SC x 1 lần/ngày (<50kg: 5mg; 50-100kg: 7.5mg; >100kg: 10mg)",
                "adult_acs": "2.5mg SC x 1 lần/ngày (với aspirin)",
                "notes": "Liều cố định cho prophylaxis; điều chỉnh theo cân nặng cho điều trị DVT/PE. Không cần theo dõi anti-Xa thường xuyên."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Thận trọng; cân nhắc giảm liều",
                "under_30": "CHỐNG CHỈ ĐỊNH - không dùng",
                "hemodialysis": "CHỐNG CHỈ ĐỊNH"
            },
            "side_effects": [
                "Chảy máu (phổ biến)",
                "Phản ứng tại chỗ tiêm (đau, ban đỏ)",
                "Giảm tiểu cầu (hiếm, ít hơn heparin)",
                "Tăng men gan (hiếm)"
            ],
            "interactions": [
                "Warfarin: tăng nguy cơ chảy máu",
                "Aspirin/NSAID: tăng nguy cơ chảy máu",
                "Thrombolytics: tăng nguy cơ chảy máu"
            ],
            "pregnancy": "B - Tương đối an toàn",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hematologic": True, "renal": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "ACCP/Antithrombotic Therapy Guidelines",
                "ESC VTE Guidelines",
                "AHA/ACC ACS Guidelines"
            ],
            "mechanism_of_action": (
                "Fondaparinux là synthetic pentasaccharide, ức chế chọn lọc yếu tố Xa thông qua antithrombin III. "
                "Khác với heparin/LMWH, fondaparinux chỉ ức chế Xa (không ức chế IIa/thrombin). "
                "Thuốc có thời gian bán thải dài (~17 giờ), dự đoán được, và không gây HIT (heparin-induced thrombocytopenia). "
                "Thải trừ chủ yếu qua thận (100%), nên CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30)."
            ),
            "monitoring": [
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
                "Công thức máu (tiểu cầu) - ít gây HIT hơn heparin",
                "Chức năng thận (CrCl) - CHỐNG CHỈ ĐỊNH nếu CrCl <30",
                "Anti-Xa (fondaparinux-specific) nếu cần (hiếm khi cần)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30) - tích lũy và tăng nguy cơ chảy máu",
                "Không có antidote đặc hiệu (khác với heparin có protamine)",
                "Thời gian bán thải dài (~17 giờ) - tác dụng kéo dài",
                "Không cần theo dõi anti-Xa thường xuyên (khác heparin)",
                "Ngừng 24-36 giờ trước phẫu thuật lớn (do half-life dài)",
                "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
            ],
            "pharmacokinetics": {
                "half_life": "~17 giờ (dài hơn LMWH)",
                "onset": "2-3 giờ (SC)",
                "duration": "24 giờ",
                "protein_binding": ">94% (gắn với antithrombin III)",
                "clearance": "Thận (100% - thải trừ nguyên dạng). CHỐNG CHỈ ĐỊNH ở suy thận nặng."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Không rung lắc.",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30) - tích lũy và tăng nguy cơ chảy máu. Không có antidote đặc hiệu.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Warfarin",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                        "management": "Theo dõi INR, dấu hiệu chảy máu. Dùng đồng thời trong quá trình khởi đầu warfarin."
                    },
                    {
                        "drug": "Thrombolytics (alteplase, tenecteplase)",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin, NSAIDs",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Suy thận nặng (CrCl <30 mL/phút) - CHỐNG CHỈ ĐỊNH",
                    "Giảm tiểu cầu nặng (<100,000/μL)",
                    "Dị ứng fondaparinux"
                ],
                "tương_đối": [
                    "Suy thận trung bình (CrCl 30-50) - thận trọng, cân nhắc giảm liều",
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng 24-36 giờ trước phẫu thuật",
                    "Có thai - tương đối an toàn nhưng thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Tương đối an toàn trong thai kỳ. Fondaparinux không qua nhau thai do kích thước phân tử lớn. Có thể dùng trong thai kỳ nếu cần chống đông. Theo dõi chặt chẽ dấu hiệu chảy máu.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Fondaparinux không bài tiết vào sữa mẹ do kích thước phân tử lớn. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều",
                "moderate": "Không cần chỉnh liều",
                "severe": "Thận trọng (không chuyển hóa qua gan nhưng có thể ảnh hưởng đến đông máu)",
                "notes": "Fondaparinux không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan. Thận trọng ở suy gan nặng do có thể ảnh hưởng đến đông máu."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
                ],
                "antidote": "KHÔNG CÓ ANTIDOTE ĐẶC HIỆU (khác với heparin có protamine)",
                "treatment": [
                    "Ngừng fondaparinux ngay lập tức",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                    "Cân nhắc recombinant factor VIIa (rFVIIa) trong chảy máu đe dọa tính mạng (off-label)",
                    "Theo dõi ít nhất 48 giờ (do half-life ~17 giờ)"
                ],
                "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, anti-Xa (fondaparinux-specific) nếu có"
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "KHÔNG CÓ ANTIDOTE ĐẶC HIỆU. Protamine không đảo ngược fondaparinux. Cân nhắc rFVIIa trong chảy máu đe dọa tính mạng (off-label)."
            },
            "administration_instructions": {
                "oral": None,
                "sc": {
                    "reconstitution": "Dùng trực tiếp, không cần pha",
                    "injection_site": "Vùng bụng (tránh rốn 5cm), đùi ngoài, hoặc cánh tay",
                    "technique": "Tiêm SC sâu, không xoa bóp sau tiêm",
                    "notes": "Tiêm SC sâu. Không xoa bóp sau tiêm. Xoay vị trí tiêm. Prophylaxis: 2.5mg SC x 1 lần/ngày. Treatment DVT/PE: 5mg SC (<50kg), 7.5mg SC (50-100kg), 10mg SC (>100kg) x 1 lần/ngày."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Arixtra (Fondaparinux)",
                    "ACCP/Antithrombotic Therapy Guidelines",
                    "ESC VTE Guidelines",
                    "UpToDate - Fondaparinux: Drug information"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "High (FDA-approved, extensive clinical data)"
            }
        },

        "Heparin": {
            "group": "Hematology - Anticoagulant (Unfractionated Heparin)",
            "vietnamese_name": "Heparin, Unfractionated Heparin, UFH",
            "administration": ["IV", "SC"],
            "indications": [
                "Điều trị DVT/PE",
                "Hội chứng mạch vành cấp",
                "Phòng ngừa huyết khối trong phẫu thuật",
                "Phòng ngừa huyết khối trong lọc máu/thẩm phân phúc mạc",
                "Phòng ngừa huyết khối trong ECMO"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Giảm tiểu cầu do heparin (HIT)",
                "Dị ứng heparin",
                "Suy gan nặng"
            ],
            "dosage": {
                "adult_loading": "80 units/kg IV bolus, sau đó 18 units/kg/giờ IV",
                "adult_prophylaxis": "5000 units SC x 2-3 lần/ngày",
                "adult_treatment": "80 units/kg IV bolus, sau đó 18 units/kg/giờ IV (điều chỉnh theo aPTT)",
                "notes": "Điều chỉnh liều theo aPTT (target: 1.5-2.5 x baseline). Theo dõi aPTT mỗi 6 giờ"
            },
            "side_effects": [
                "Chảy máu (phổ biến)",
                "Giảm tiểu cầu do heparin (HIT) - 1-5%",
                "Loãng xương (với điều trị dài ngày)",
                "Tăng transaminase (hiếm)",
                "Phản ứng quá mẫn (hiếm)"
            ],
            "interactions": [
                "Warfarin: tăng nguy cơ chảy máu",
                "Aspirin/NSAID: tăng nguy cơ chảy máu",
                "Thrombolytics: tăng nguy cơ chảy máu"
            ],
            "pregnancy": "C - Tương đối an toàn",
            "mechanism_of_action": "Heparin là glycosaminoglycan, tăng cường hoạt động của antithrombin III (ATIII), ức chế yếu tố Xa và yếu tố IIa (thrombin). Heparin gắn với ATIII, làm thay đổi cấu trúc ATIII, tăng khả năng ức chế Xa và IIa. Heparin có tác dụng nhanh, có thể đảo ngược bằng protamine. Thuốc cần theo dõi aPTT thường xuyên do dự đoán kém. Heparin có thể gây HIT (heparin-induced thrombocytopenia) do tạo kháng thể chống heparin-PF4 complex.",
            "monitoring": [
                "aPTT (activated partial thromboplastin time) - mỗi 6 giờ cho đến khi ổn định, sau đó mỗi 24 giờ (target: 1.5-2.5 x baseline)",
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
                "Công thức máu (tiểu cầu) - theo dõi HIT (giảm tiểu cầu >50% hoặc <150,000/μL) - mỗi 2-3 ngày",
                "Dấu hiệu HIT (giảm tiểu cầu, huyết khối mới) - cấp cứu",
                "Chức năng gan nếu có triệu chứng"
            ],
            "precautions": [
                "Cần theo dõi aPTT thường xuyên (mỗi 6 giờ cho đến khi ổn định) - dự đoán kém",
                "Giảm tiểu cầu do heparin (HIT) - 1-5%, ngừng ngay nếu nghi ngờ",
                "Điều chỉnh liều theo aPTT (target: 1.5-2.5 x baseline)",
                "Protamine có thể đảo ngược hoàn toàn (khác LMWH)",
                "Ngừng ngay nếu có HIT - chuyển sang thuốc chống đông không chứa heparin (argatroban, bivalirudin)",
                "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao",
                "Có thể gây loãng xương với điều trị dài ngày",
                "Ngừng 4-6 giờ trước phẫu thuật lớn"
            ],
            "pharmacokinetics": {
                "half_life": "1-2 giờ (IV), 2-4 giờ (SC)",
                "onset": "Ngay lập tức (IV), 1-2 giờ (SC)",
                "duration": "4-6 giờ",
                "protein_binding": "Không đáng kể",
                "clearance": "Gan (một phần), thận (một phần), hệ thống reticuloendothelial. Dự đoán kém, cần theo dõi aPTT."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu.",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Nguy cơ giảm tiểu cầu do heparin (HIT) - 1-5%, ngừng ngay nếu nghi ngờ. Cần theo dõi aPTT thường xuyên.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Warfarin",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                        "management": "Theo dõi INR, aPTT, dấu hiệu chảy máu. Dùng đồng thời trong quá trình khởi đầu warfarin."
                    },
                    {
                        "drug": "Thrombolytics (alteplase, streptokinase)",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin, NSAIDs",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Giảm tiểu cầu do heparin (HIT) đang hoạt động hoặc tiền sử",
                    "Dị ứng heparin"
                ],
                "tương_đối": [
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Suy gan nặng - thận trọng",
                    "Có thai - tương đối an toàn nhưng thận trọng"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Giảm tiểu cầu do heparin (HIT) đang hoạt động hoặc tiền sử",
                    "Dị ứng heparin"
                ],
                "tương_đối": [
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Suy gan nặng - thận trọng",
                    "Có thai - tương đối an toàn nhưng thận trọng"
                ]
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Thận trọng, có thể cần giảm liều",
                "under_30": "Thận trọng, giảm liều (thải trừ một phần qua thận)",
                "dialysis": "Thận trọng, giảm liều. Heparin không được lọc sạch hiệu quả qua thẩm phân máu.",
                "notes": "Heparin thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Tương đối an toàn trong thai kỳ. Heparin không qua nhau thai do kích thước phân tử lớn. Có thể dùng trong thai kỳ nếu cần chống đông. Theo dõi chặt chẽ dấu hiệu chảy máu và aPTT.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Heparin không bài tiết vào sữa mẹ do kích thước phân tử lớn. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Thận trọng",
                "severe": "Thận trọng",
                "notes": "Heparin chuyển hóa một phần qua gan. Thận trọng ở suy gan. Theo dõi aPTT chặt chẽ."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
                ],
                "antidote": "Protamine sulfate - đảo ngược hoàn toàn",
                "treatment": [
                    "Ngừng heparin ngay lập tức",
                    "Protamine sulfate: 1mg IV cho mỗi 100 units heparin (nếu <30 phút sau liều cuối). Nếu 30-60 phút: 0.5-0.75mg protamine cho mỗi 100 units heparin. Nếu >60 phút: 0.25-0.375mg protamine cho mỗi 100 units heparin. Tối đa 50mg.",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, aPTT, công thức máu, dấu hiệu chảy máu",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                    "Theo dõi ít nhất 4-6 giờ (do half-life 1-2 giờ)"
                ],
                "monitoring": "Dấu hiệu sống, aPTT, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "name": "Protamine sulfate",
                        "indication": "Đảo ngược tác dụng heparin (chảy máu nặng)",
                        "dose": "1mg IV cho mỗi 100 units heparin (nếu <30 phút sau liều cuối). Tối đa 50mg.",
                        "notes": "Đảo ngược hoàn toàn. Có thể gây phản ứng quá mẫn, hạ huyết áp."
                    }
                ]
            },
            "administration_instructions": {
                "oral": None,
                "sc": {
                    "reconstitution": "Dùng trực tiếp, không cần pha",
                    "injection_site": "Vùng bụng (tránh rốn 5cm), đùi ngoài",
                    "technique": "Tiêm SC sâu, không xoa bóp sau tiêm",
                    "notes": "Prophylaxis: 5000 units SC x 2-3 lần/ngày."
                },
                "iv": {
                    "reconstitution": "Pha với NS hoặc D5W",
                    "infusion_rate": "Loading: 80 units/kg IV bolus. Maintenance: 18 units/kg/giờ IV (điều chỉnh theo aPTT).",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": [],
                    "notes": "Theo dõi aPTT mỗi 6 giờ. Điều chỉnh liều theo aPTT (target: 1.5-2.5 x baseline)."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Heparin",
                    "UpToDate - Heparin: Drug information",
                    "American College of Chest Physicians (ACCP) guidelines"
                ],
                "last_updated": "2025-02-05",
                "evidence_level": "High (FDA-approved, extensive clinical data)"
            }
        },

        "Rivaroxaban": {
            "group": "Hematology - Anticoagulant (Direct Factor Xa Inhibitor, DOAC)",
            "vietnamese_name": "Rivaroxaban, Xarelto",
            "administration": ["PO"],
            "indications": [
                "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
                "Điều trị DVT/PE",
                "Phòng ngừa DVT sau phẫu thuật thay khớp háng/gối",
                "Phòng ngừa huyết khối sau hội chứng mạch vành cấp (với aspirin)"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <15)",
                "Có thai",
                "Dị ứng rivaroxaban"
            ],
            "dosage": {
                "adult_afib": "20mg x 1 lần/ngày (15mg nếu CrCl 15-50)",
                "adult_dvt_pe": "15mg x 2 lần/ngày x 21 ngày, sau đó 20mg x 1 lần/ngày",
                "adult_prophylaxis": "10mg x 1 lần/ngày",
                "adult_acs": "2.5mg x 2 lần/ngày (với aspirin)",
                "notes": "Điều chỉnh liều theo chức năng thận. Uống với thức ăn (liều ≥15mg)"
            },
            "side_effects": [
                "Chảy máu (phổ biến)",
                "Rối loạn tiêu hóa",
                "Nhức đầu"
            ],
            "interactions": [
                "CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir): tăng nồng độ (tránh dùng)",
                "CYP3A4 và P-gp inducers (rifampin): giảm nồng độ",
                "Aspirin/NSAID: tăng nguy cơ chảy máu"
            ],
            "pregnancy": "C - Tránh dùng",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": "High",
                "organ_toxicity": []
            },
            "guideline_tags": [
                "AHA/ACC/HRS AF stroke prevention",
                "ISTH VTE treatment/prophylaxis",
                "ESC AF guidelines"
            ],
            "mechanism_of_action": "Rivaroxaban là direct factor Xa inhibitor, ức chế trực tiếp yếu tố Xa mà không cần antithrombin III. Rivaroxaban gắn trực tiếp với Xa, ngăn chặn chuyển đổi prothrombin thành thrombin, ức chế hình thành cục máu đông. Thuốc là DOAC (direct oral anticoagulant), không cần theo dõi INR/aPTT thường xuyên như warfarin. Rivaroxaban được thải trừ một phần qua thận (33%) và một phần qua gan (66%), nên cần điều chỉnh liều ở suy thận. Có antidote đặc hiệu: andexanet alfa (Andexxa).",
            "monitoring": [
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
                "Chức năng thận (CrCl) - mỗi 3-6 tháng (rivaroxaban thải trừ một phần qua thận)",
                "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
                "Dấu hiệu rối loạn tiêu hóa"
            ],
            "precautions": [
                "Điều chỉnh liều theo chức năng thận (CrCl) - mỗi 3-6 tháng",
                "Suy thận nặng (CrCl <15) - chống chỉ định",
                "Uống với thức ăn (liều ≥15mg) - tăng hấp thu",
                "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
                "Có antidote đặc hiệu: andexanet alfa (Andexxa) - đảo ngược tác dụng",
                "Tránh dùng với CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir) - tăng nồng độ",
                "Ngừng 1-2 ngày trước phẫu thuật lớn (tùy chức năng thận)",
                "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
            ],
            "pharmacokinetics": {
                "half_life": "5-9 giờ (bình thường), 9-13 giờ (suy thận)",
                "onset": "2-4 giờ",
                "duration": "12-24 giờ",
                "protein_binding": "92-95%",
                "clearance": "Gan (66% - chuyển hóa qua CYP3A4). Thận (33% - thải trừ nguyên dạng). Cần điều chỉnh liều ở suy thận."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Suy thận nặng (CrCl <15) - chống chỉ định. Không ngừng đột ngột (tăng nguy cơ đột quỵ trong rung nhĩ).",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)",
                        "mechanism": "Ức chế CYP3A4 và P-gp, tăng nồng độ rivaroxaban",
                        "effect": "Tăng nồng độ rivaroxaban, tăng nguy cơ chảy máu",
                        "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng CYP3A4 và P-gp inhibitors mạnh."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin, NSAIDs",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                    },
                    {
                        "drug": "CYP3A4 và P-gp inducers (rifampin)",
                        "mechanism": "Cảm ứng CYP3A4 và P-gp, giảm nồng độ rivaroxaban",
                        "effect": "Giảm nồng độ rivaroxaban, giảm hiệu quả",
                        "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Suy thận nặng (CrCl <15) - chống chỉ định",
                    "Dị ứng rivaroxaban",
                    "Dùng CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)"
                ],
                "tương_đối": [
                    "Suy thận (CrCl 15-50) - giảm liều (15mg x 1 lần/ngày cho AFib)",
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Có thai - tránh dùng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Tránh dùng trong thai kỳ. Rivaroxaban có thể gây chảy máu ở mẹ và thai nhi. Chỉ dùng nếu lợi ích > nguy cơ rõ ràng.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Rivaroxaban có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                    "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Thận trọng",
                "severe": "CHỐNG CHỈ ĐỊNH",
                "notes": "Rivaroxaban chuyển hóa chủ yếu qua gan (CYP3A4 - 66%). Không cần điều chỉnh liều ở suy gan nhẹ. Thận trọng ở suy gan trung bình. Chống chỉ định ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
                ],
                "antidote": "Andexanet alfa (Andexxa) - antidote đặc hiệu",
                "treatment": [
                    "Ngừng rivaroxaban ngay lập tức",
                    "Andexanet alfa (Andexxa): 400-800mg IV bolus, sau đó 4-8mg/phút x 2 giờ - đảo ngược tác dụng",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                    "Rửa dạ dày nếu uống trong vòng 2 giờ",
                    "Than hoạt tính",
                    "Nếu không có andexanet: PCC 4 yếu tố (≈50 IU/kg) + than hoạt sớm",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                    "Theo dõi ít nhất 24 giờ (do half-life 5-9 giờ)"
                ],
                "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "name": "Andexanet alfa (Andexxa)",
                        "indication": "Đảo ngược tác dụng rivaroxaban, apixaban (chảy máu nặng hoặc phẫu thuật cấp cứu)",
                        "dose": "400-800mg IV bolus, sau đó 4-8mg/phút x 2 giờ",
                        "notes": "Antidote đặc hiệu cho rivaroxaban và apixaban. Đảo ngược tác dụng nhanh chóng."
                    }
                ]
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với thức ăn (liều ≥15mg) - tăng hấp thu. Liều <15mg có thể uống không cần thức ăn.",
                    "timing": "AFib: 20mg x 1 lần/ngày (15mg nếu CrCl 15-50), uống với thức ăn. DVT/PE: 15mg x 2 lần/ngày x 21 ngày, sau đó 20mg x 1 lần/ngày, uống với thức ăn. Prophylaxis: 10mg x 1 lần/ngày, có thể uống không cần thức ăn.",
                    "notes": "Uống với thức ăn (liều ≥15mg) - tăng hấp thu. Liều <15mg có thể uống không cần thức ăn."
                },
                "iv": None
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Xarelto (rivaroxaban)",
                    "ROCKET-AF Study - New England Journal of Medicine",
                    "UpToDate - Rivaroxaban: Drug information"
                ],
                "last_updated": "2025-02-05",
                "evidence_level": "High (FDA-approved, large RCT - ROCKET-AF study)"
            }
        },

}

__all__ = ['ANTICOAGULANTS_DRUGS']
