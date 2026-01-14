"""
Hematology Drugs - Antiplatelets
"""
from typing import Dict, Any


ANTIPLATELETS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Dipyridamole": {
            "group": "Cardiovascular - Antiplatelet",
            "vietnamese_name": "Dipyridamole, Persantine",
            "administration": ["PO"],
            "indications": [
                "Phòng ngừa đột quỵ/TIA (kết hợp với aspirin)",
                "Phòng ngừa huyết khối sau phẫu thuật van tim"
            ],
            "contraindications": [
                "Nhồi máu cơ tim cấp",
                "Co thắt mạch vành (vasospasm)"
            ],
            "dosage": {
                "adult_standard": "200mg x 2 lần/ngày (với aspirin)",
                "adult_modified_release": "200mg x 2 lần/ngày",
                "notes": "Thường dùng kết hợp với aspirin 25mg x 2 lần/ngày"
            },
            "side_effects": [
                "Nhức đầu (phổ biến)",
                "Chóng mặt",
                "Đau bụng",
                "Chảy máu",
                "Tim đập nhanh"
            ],
            "interactions": [
                "Aspirin: dùng kèm để tăng hiệu quả",
                "Warfarin: tăng nguy cơ chảy máu"
            ],
        "pregnancy": "B",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": "Medium",
                "organ_toxicity": ["vasodilation_headache"]
            },
            "guideline_tags": [
                "AHA/ASA stroke secondary prevention",
                "ESC antiplatelet (secondary prevention)"
            ],
            "mechanism_of_action": "Dipyridamole ức chế phosphodiesterase và adenosine deaminase, làm tăng nồng độ cAMP và adenosine trong tiểu cầu, ức chế aggregation tiểu cầu. Thuốc cũng ức chế tái hấp thu adenosine, làm giãn mạch vành. Dipyridamole thường dùng kết hợp với aspirin để phòng ngừa đột quỵ/TIA sau stroke hoặc TIA. Thuốc có tác dụng chống đông và giãn mạch, nhưng có thể gây nhức đầu do giãn mạch. Thường dùng dạng modified-release để giảm tác dụng phụ.",
            "monitoring": [
                "Dấu hiệu chảy máu (xuất huyết, chảy máu chân răng, chảy máu cam)",
                "Nhức đầu (tác dụng phụ phổ biến, có thể giảm khi dùng liều thấp hơn)",
                "Huyết áp (có thể giảm nhẹ do giãn mạch)",
                "Nhịp tim (có thể tăng nhẹ)",
                "Đáp ứng điều trị (giảm nguy cơ đột quỵ/TIA)"
            ],
            "precautions": [
                "Thường dùng kết hợp với aspirin 25mg x 2 lần/ngày để tăng hiệu quả",
                "Nhức đầu là tác dụng phụ phổ biến (có thể giảm khi dùng liều thấp hơn hoặc dạng modified-release)",
                "Tránh dùng trong nhồi máu cơ tim cấp (có thể làm nặng thêm)",
                "Thận trọng ở bệnh nhân co thắt mạch vành (vasospasm)",
                "Tránh dùng với warfarin (tăng nguy cơ chảy máu)",
                "Có thể gây chóng mặt, đau bụng",
                "Ngừng 5-7 ngày trước phẫu thuật lớn",
                "Thận trọng ở bệnh nhân hạ huyết áp"
            ],
            "pharmacokinetics": {
                "half_life": "10-12 giờ",
                "onset": "2-4 giờ",
                "duration": "12-24 giờ",
                "protein_binding": "91-99%",
                "clearance": "Gan (chuyển hóa), thận (thải trừ)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
            "black_box_warnings": "Cần xem xét black box warnings",
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Category B - cần xem xét dữ liệu an toàn thai kỳ.",
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
                "oral": {
                "with_food": "Cần xem xét uống với hoặc không có thức ăn",
                "timing": "Cần xem xét thời điểm dùng",
                "notes": "Cần xem xét hướng dẫn cụ thể",
            },
            },
            "references": {
                "primary_sources": [
                "FDA Drug Label - Dipyridamole, Persantine",
                "UpToDate - Drug information",
            ],
                "last_updated": "2025-02-05",
                "evidence_level": "A",
            },
        },

        "Prasugrel": {
            "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
            "vietnamese_name": "Prasugrel, Effient",
            "administration": ["PO"],
            "indications": [
                "Hội chứng mạch vành cấp cần PCI",
                "Sau đặt stent"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Tiền sử TIA/đột quỵ",
                "Tuổi ≥75 (trừ nguy cơ cao)",
                "Cân nặng <60kg (trừ nguy cơ cao)"
            ],
            "dosage": {
                "adult_loading": "60mg x 1 lần",
                "adult_maintenance": "10mg x 1 lần/ngày (5mg nếu <60kg hoặc ≥75 tuổi)",
                "notes": "Mạnh hơn clopidogrel, nguy cơ chảy máu cao hơn"
            },
            "side_effects": [
                "Chảy máu (nhiều hơn clopidogrel)",
                "Chảy máu lớn (hiếm nhưng nguy hiểm)",
                "Thrombotic thrombocytopenic purpura (TTP) - hiếm"
            ],
            "interactions": [
                "Aspirin: dùng kèm (dual antiplatelet therapy)",
                "Warfarin: tăng nguy cơ chảy máu"
            ],
        "pregnancy": "B",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": "High",
                "organ_toxicity": []
            },
            "guideline_tags": [
                "ACC/AHA ACS DAPT (PCI)",
                "ESC ACS DAPT (PCI)"
            ],
            "mechanism_of_action": "Prasugrel là chất ức chế P2Y12 receptor, đối kháng không thể đảo ngược (irreversible) với P2Y12 receptor trên tiểu cầu. P2Y12 receptor là một thụ thể adenosine diphosphate (ADP) quan trọng trong quá trình hoạt hóa và kết tập tiểu cầu. Prasugrel là một prodrug, được chuyển hóa nhanh chóng qua CYP3A4 và CYP2B6 thành metabolite hoạt động. Metabolite hoạt động gắn không thể đảo ngược với P2Y12 receptor, ức chế kết tập tiểu cầu do ADP. Prasugrel mạnh hơn và có tác dụng nhanh hơn clopidogrel, với ít biến thể di truyền (genetic variation) hơn. Prasugrel giảm nguy cơ huyết khối trong hội chứng mạch vành cấp cần can thiệp mạch vành (PCI), nhưng tăng nguy cơ chảy máu lớn so với clopidogrel, đặc biệt ở bệnh nhân có tiền sử TIA/đột quỵ hoặc tuổi ≥75.",
            "monitoring": [
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu tại vị trí tiêm)",
                "Chảy máu lớn (xuất huyết tiêu hóa, xuất huyết nội sọ, chảy máu sau phẫu thuật) - nguy cơ cao hơn clopidogrel",
                "Thrombotic thrombocytopenic purpura (TTP) - hiếm nhưng nguy hiểm (sốt, thiếu máu, giảm tiểu cầu, rối loạn thần kinh)",
                "Chức năng gan nếu có triệu chứng (hiếm)",
                "Công thức máu (tiểu cầu) nếu có dấu hiệu chảy máu"
            ],
            "precautions": [
                "Dùng kèm với aspirin 75-100mg/ngày (dual antiplatelet therapy - DAPT)",
                "Không dùng ở bệnh nhân có tiền sử TIA hoặc đột quỵ - tăng nguy cơ chảy máu nội sọ",
                "Thận trọng ở bệnh nhân ≥75 tuổi - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
                "Thận trọng ở bệnh nhân <60kg - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
                "Nguy cơ chảy máu cao hơn clopidogrel - không dùng nếu có chảy máu đang hoạt động",
                "Không ngừng đột ngột (tăng nguy cơ huyết khối)",
                "Không dùng ở bệnh nhân có nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây)",
                "Thời gian DAPT thường 12 tháng sau ACS với PCI, có thể kéo dài ở một số bệnh nhân nguy cơ cao",
                "Mạnh hơn clopidogrel - giảm nguy cơ huyết khối nhưng tăng nguy cơ chảy máu",
                "Liều khởi đầu: 60mg loading dose, sau đó 10mg/ngày (5mg nếu <60kg hoặc ≥75 tuổi)"
            ],
            "pharmacokinetics": {
                "half_life": "7 giờ",
                "onset": "30 phút - 1 giờ (nhanh hơn clopidogrel)",
                "duration": "7-10 ngày (do irreversible binding - tiểu cầu mới không bị ảnh hưởng)",
                "protein_binding": "Không đáng kể",
                "clearance": "Gan: chuyển hóa nhanh qua CYP3A4 và CYP2B6 thành metabolite hoạt động (không cần chuyển hóa qua CYP2C19 như clopidogrel). Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có tiền sử TIA hoặc đột quỵ - tăng nguy cơ chảy máu nội sọ. Không dùng ở bệnh nhân có chảy máu đang hoạt động. Thận trọng ở bệnh nhân ≥75 tuổi, <60kg, hoặc có nguy cơ chảy máu cao.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Warfarin",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                        "management": "Thận trọng. Theo dõi INR, dấu hiệu chảy máu. Thường tránh dùng cùng."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Aspirin",
                        "mechanism": "Dùng kèm trong dual antiplatelet therapy",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Dùng kèm aspirin 75-100mg/ngày. Theo dõi dấu hiệu chảy máu."
                    },
                    {
                        "drug": "NSAIDs (ibuprofen, naproxen)",
                        "mechanism": "Tác dụng hiệp đồng chống kết tập tiểu cầu",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "Thận trọng. Tránh dùng nếu có thể."
                    }
                ],
                "minor": [
                    {
                        "drug": "CYP inducers/inhibitors",
                        "mechanism": "Prasugrel chuyển hóa qua CYP3A4, CYP2B6, nhưng ít bị ảnh hưởng bởi CYP inhibitors/inducers hơn clopidogrel",
                        "effect": "Tương tác tối thiểu",
                        "management": "Không cần điều chỉnh liều"
                    }
                ]
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Tiền sử TIA hoặc đột quỵ",
                    "Dị ứng prasugrel"
                ],
                "tương_đối": [
                    "Tuổi ≥75 (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
                    "Cân nặng <60kg (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Suy gan nặng - thận trọng",
                    "Suy thận nặng - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Không có bằng chứng về nguy cơ gây dị tật thai nhi ở động vật. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ chảy máu ở mẹ và thai nhi. Cân nhắc nguy cơ huyết khối vs nguy cơ chảy máu. Theo dõi chặt chẽ dấu hiệu chảy máu.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Prasugrel và metabolite có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                    "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ về dấu hiệu chảy máu."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Thận trọng",
                "notes": "Prasugrel chuyển hóa ở gan qua CYP3A4 và CYP2B6. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Thận trọng ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Chảy máu lớn có thể nghiêm trọng và đe dọa tính mạng",
                    "Thrombotic thrombocytopenic purpura (TTP) - hiếm nhưng nguy hiểm"
                ],
                "antidote": "Không có antidote đặc hiệu. Truyền tiểu cầu nếu cần (hiệu quả hạn chế do irreversible binding)",
                "treatment": [
                    "Ngừng prasugrel ngay lập tức",
                    "Truyền tiểu cầu nếu chảy máu nghiêm trọng (hiệu quả hạn chế do irreversible binding - cần tiểu cầu mới)",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                    "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                    "Than hoạt tính",
                    "Theo dõi ít nhất 7-10 ngày (do irreversible binding - tiểu cầu mới không bị ảnh hưởng)",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                    "Nếu có TTP: điều trị với plasma exchange"
                ],
                "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, dấu hiệu TTP"
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                    "timing": "Uống 1 lần/ngày. Loading dose: 60mg x 1 lần. Maintenance: 10mg x 1 lần/ngày (5mg nếu <60kg hoặc ≥75 tuổi). Dùng kèm aspirin 75-100mg/ngày."
                },
                "iv": {
                    "reconstitution": "Không có dạng IV",
                    "infusion_rate": "N/A",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Chỉ có dạng uống"
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Effient (prasugrel)",
                    "TRITON-TIMI 38 Study - New England Journal of Medicine",
                    "UpToDate - Prasugrel: Drug information",
                    "American Heart Association/American College of Cardiology guidelines"
                ],
                "last_updated": "2024-12-19",
                "evidence_level": "High - Large RCT (TRITON-TIMI 38 study)"
            }
        },

        "Ticagrelor": {
            "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
            "vietnamese_name": "Ticagrelor, Brilinta",
            "administration": ["PO"],
            "indications": [
                "Hội chứng mạch vành cấp",
                "Sau đặt stent",
                "Sau nhồi máu cơ tim",
                "Phòng ngừa đột quỵ/TIA"
            ],
            "contraindications": [
                "Chảy máu đang hoạt động",
                "Xuất huyết nội sọ",
                "Suy gan nặng",
                "Dị ứng"
            ],
            "dosage": {
                "adult_loading": "180mg x 1 lần",
                "adult_maintenance": "90mg x 2 lần/ngày",
                "notes": "Dùng kèm aspirin 75-100mg/ngày (dual antiplatelet therapy). Dùng với thức ăn để giảm dyspnea"
            },
            "side_effects": [
                "Chảy máu",
                "Khó thở (dyspnea) - phổ biến nhưng thường nhẹ",
                "Chóng mặt",
                "Nhức đầu"
            ],
            "interactions": [
                "Aspirin: dùng kèm (nhưng liều aspirin >100mg/ngày có thể giảm hiệu quả)",
                "Warfarin: tăng nguy cơ chảy máu",
                "Strong CYP3A4 inhibitors: tăng nồng độ (tránh dùng)"
            ],
        "pregnancy": "C",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": "High",
                "organ_toxicity": ["bradycardia_dyspnea"]
            },
            "guideline_tags": [
                "ACC/AHA ACS DAPT",
                "ESC ACS DAPT"
            ],
            "mechanism_of_action": "Ticagrelor là chất ức chế P2Y12 receptor chọn lọc, đối kháng có thể đảo ngược (reversible) với P2Y12 receptor trên tiểu cầu. P2Y12 receptor là một thụ thể adenosine diphosphate (ADP) quan trọng trong quá trình hoạt hóa và kết tập tiểu cầu. Khác với clopidogrel và prasugrel (irreversible inhibitors), ticagrelor gắn trực tiếp với P2Y12 receptor mà không cần chuyển hóa thành metabolite hoạt động, và có thể đảo ngược (reversible). Ticagrelor ức chế kết tập tiểu cầu do ADP, giảm nguy cơ huyết khối trong hội chứng mạch vành cấp và sau can thiệp mạch vành. Ticagrelor cũng ức chế tái hấp thu adenosine (adenosine reuptake inhibitor), làm tăng nồng độ adenosine ngoại bào, có thể gây khó thở (dyspnea) và bradycardia. Tác dụng khởi phát nhanh hơn clopidogrel và hiệu quả hơn trong một số nghiên cứu.",
            "monitoring": [
                "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu tại vị trí tiêm)",
                "Chảy máu lớn (xuất huyết tiêu hóa, xuất huyết nội sọ, chảy máu sau phẫu thuật)",
                "Khó thở (dyspnea) - phổ biến (10-20%) nhưng thường nhẹ, có thể do ức chế tái hấp thu adenosine",
                "Nhịp tim chậm (bradycardia) - do tăng adenosine",
                "Chức năng gan nếu có triệu chứng (hiếm)",
                "Tương tác với strong CYP3A4 inhibitors (ketoconazole, clarithromycin) - tăng nồng độ"
            ],
            "precautions": [
                "Dùng kèm với aspirin 75-100mg/ngày (dual antiplatelet therapy - DAPT) - không dùng aspirin >100mg/ngày (có thể giảm hiệu quả)",
                "Không ngừng đột ngột (tăng nguy cơ huyết khối)",
                "Khó thở (dyspnea) - phổ biến nhưng thường nhẹ, có thể giảm khi dùng với thức ăn, thường tự khỏi",
                "Nguy cơ chảy máu cao - không dùng nếu có chảy máu đang hoạt động, xuất huyết nội sọ",
                "Tránh dùng với strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir) - tăng nồng độ",
                "Tránh dùng với strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin) - giảm nồng độ",
                "Dùng với thức ăn để giảm dyspnea và tăng hấp thu",
                "Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình",
                "Thận trọng ở bệnh nhân có tiền sử nhịp tim chậm hoặc block nhĩ thất",
                "Thời gian DAPT thường 12 tháng sau ACS hoặc đặt stent, có thể kéo dài ở một số bệnh nhân nguy cơ cao"
            ],
            "pharmacokinetics": {
                "half_life": "7-9 giờ (ticagrelor), 8-12 giờ (metabolite hoạt động)",
                "onset": "30 phút - 2 giờ (nhanh hơn clopidogrel)",
                "duration": "12 giờ (cần dùng 2 lần/ngày do reversible binding)",
                "protein_binding": ">99%",
                "clearance": "Gan: chuyển hóa qua CYP3A4 thành metabolite hoạt động. Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
            "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có xuất huyết nội sọ đang hoạt động, chảy máu đang hoạt động. Không dùng aspirin >100mg/ngày vì có thể giảm hiệu quả của ticagrelor.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                        "mechanism": "Ức chế chuyển hóa ticagrelor, tăng nồng độ",
                        "effect": "Tăng nguy cơ chảy máu",
                        "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng strong CYP3A4 inhibitors."
                    },
                    {
                        "drug": "Aspirin >100mg/ngày",
                        "mechanism": "Có thể giảm hiệu quả của ticagrelor",
                        "effect": "Giảm hiệu quả chống kết tập tiểu cầu",
                        "management": "Dùng aspirin 75-100mg/ngày. Không dùng aspirin >100mg/ngày."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Warfarin",
                        "mechanism": "Tác dụng hiệp đồng chống đông",
                        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                        "management": "Thận trọng. Theo dõi INR, dấu hiệu chảy máu. Thường tránh dùng cùng."
                    },
                    {
                        "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                        "mechanism": "Tăng chuyển hóa ticagrelor, giảm nồng độ",
                        "effect": "Giảm hiệu quả ticagrelor",
                        "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                    }
                ],
                "minor": [
                    {
                        "drug": "Moderate CYP3A4 inhibitors (diltiazem, verapamil)",
                        "mechanism": "Có thể tăng nhẹ nồng độ ticagrelor",
                        "effect": "Tăng nhẹ nguy cơ chảy máu",
                        "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                    }
                ]
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Chảy máu đang hoạt động",
                    "Xuất huyết nội sọ đang hoạt động",
                    "Dị ứng ticagrelor",
                    "Dùng strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)"
                ],
                "tương_đối": [
                    "Suy gan nặng - chống chỉ định",
                    "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                    "Tiền sử nhịp tim chậm hoặc block nhĩ thất - tăng nguy cơ bradycardia",
                    "Suy thận nặng - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ chảy máu ở mẹ và thai nhi. Cân nhắc nguy cơ huyết khối vs nguy cơ chảy máu. Theo dõi chặt chẽ dấu hiệu chảy máu.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Ticagrelor và metabolite có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                    "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ về dấu hiệu chảy máu."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "CHỐNG CHỈ ĐỊNH",
                "notes": "Ticagrelor chuyển hóa ở gan qua CYP3A4. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chống chỉ định ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                    "Khó thở (dyspnea) - do tăng adenosine",
                    "Nhịp tim chậm (bradycardia)",
                    "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
                ],
                "antidote": "Không có antidote đặc hiệu. Truyền tiểu cầu nếu cần",
                "treatment": [
                    "Ngừng ticagrelor ngay lập tức",
                    "Truyền tiểu cầu nếu chảy máu nghiêm trọng (hiệu quả hạn chế do ticagrelor reversible)",
                    "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                    "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                    "Than hoạt tính",
                    "Theo dõi ít nhất 24-48 giờ (do half-life metabolite 8-12 giờ)",
                    "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần"
                ],
                "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, ECG (bradycardia)"
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Nên dùng với thức ăn để giảm dyspnea và tăng hấp thu",
                    "timing": "Uống 2 lần/ngày (sáng và tối), cách nhau 12 giờ. Loading dose: 180mg x 1 lần. Maintenance: 90mg x 2 lần/ngày. Dùng kèm aspirin 75-100mg/ngày."
                },
                "iv": {
                    "reconstitution": "Không có dạng IV",
                    "infusion_rate": "N/A",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Chỉ có dạng uống"
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Brilinta (ticagrelor)",
                    "PLATO Study - New England Journal of Medicine",
                    "UpToDate - Ticagrelor: Drug information",
                    "American Heart Association/American College of Cardiology guidelines"
                ],
                "last_updated": "2024-12-19",
                "evidence_level": "High - Large RCT (PLATO study)"
            }
        },

        "Ticlopidine": {
            "group": "Cardiovascular - Antiplatelet",
            "vietnamese_name": "Ticlopidine, Ticlid",
            "administration": ["PO"],
            "indications": [
                "Phòng ngừa đột quỵ sau TIA",
                "Phòng ngừa huyết khối sau stent (ít dùng, thay bằng clopidogrel)"
            ],
            "contraindications": [
                "Giảm bạch cầu/giảm tiểu cầu",
                "Chảy máu đang hoạt động",
                "Suy gan nặng"
            ],
            "dosage": {
                "adult_standard": "250mg x 2 lần/ngày",
                "notes": "Ít dùng do nguy cơ giảm bạch cầu/tiểu cầu. Clopidogrel thay thế tốt hơn"
            },
            "side_effects": [
                "Giảm bạch cầu (nguy hiểm - cần theo dõi)",
                "Giảm tiểu cầu",
                "Ban xuất huyết giảm tiểu cầu huyết khối (TTP)",
                "Chảy máu",
                "Rối loạn tiêu hóa"
            ],
            "interactions": [
                "Aspirin: tăng nguy cơ chảy máu",
                "Warfarin: tăng nguy cơ chảy máu",
                "Antacids: giảm hấp thu"
            ],
        "pregnancy": "B",
            "mechanism_of_action": "Ticlopidine là thienopyridine, ức chế P2Y12 receptor trên tiểu cầu, ngăn chặn kích hoạt tiểu cầu bởi ADP. Thuốc ức chế aggregation tiểu cầu và giải phóng các chất tiểu cầu, làm giảm hình thành huyết khối. Ticlopidine là prodrug, chuyển hóa trong gan thành chất hoạt động. Thuốc ức chế mạnh hơn clopidogrel nhưng có nhiều tác dụng phụ nghiêm trọng, đặc biệt giảm bạch cầu và giảm tiểu cầu, nên ít dùng, thay bằng clopidogrel. Thường dùng để phòng ngừa đột quỵ sau TIA, nhưng hiện tại clopidogrel là lựa chọn ưu tiên.",
            "monitoring": [
                "Công thức máu (CBC) - mỗi 2 tuần trong 3 tháng đầu (nguy cơ giảm bạch cầu cao nhất)",
                "Bạch cầu (WBC) - nếu <3500/μL: ngừng ngay",
                "Tiểu cầu - nếu <100,000/μL: ngừng ngay",
                "Dấu hiệu nhiễm trùng (sốt, đau họng) - dấu hiệu giảm bạch cầu",
                "Dấu hiệu chảy máu (xuất huyết, chảy máu chân răng)",
                "Dấu hiệu TTP (sốt, thiếu máu, giảm tiểu cầu, rối loạn thần kinh) - cấp cứu"
            ],
            "precautions": [
                "Ít dùng do nguy cơ giảm bạch cầu/tiểu cầu cao - clopidogrel thay thế tốt hơn",
                "Theo dõi sát công thức máu mỗi 2 tuần trong 3 tháng đầu (nguy cơ cao nhất)",
                "Ngừng ngay nếu giảm bạch cầu <3500/μL hoặc giảm tiểu cầu <100,000/μL",
                "Nguy cơ TTP (thrombotic thrombocytopenic purpura) - cấp cứu, có thể tử vong",
                "Thận trọng ở bệnh nhân suy gan (giảm chuyển hóa)",
                "Tránh dùng với aspirin và warfarin (tăng nguy cơ chảy máu)",
                "Có thể gây rối loạn tiêu hóa (buồn nôn, tiêu chảy)",
                "Ngừng 10-14 ngày trước phẫu thuật lớn"
            ],
            "pharmacokinetics": {
                "half_life": "4-5 ngày (rất dài)",
                "onset": "3-5 ngày (tác dụng tích tụ)",
                "duration": "7-10 ngày sau khi ngừng (do half-life dài)",
                "protein_binding": "98%",
                "clearance": "Gan (chuyển hóa), thận (thải trừ)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
            "black_box_warnings": "Nguy cơ giảm bạch cầu và giảm tiểu cầu nghiêm trọng, đe dọa tính mạng. Nguy cơ TTP (thrombotic thrombocytopenic purpura) có thể tử vong. Cần theo dõi công thức máu thường xuyên",
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Giảm bạch cầu/giảm tiểu cầu",
                    "Chảy máu đang hoạt động",
                    "Suy gan nặng"
                ],
                "tương_đối": [
                    "Suy thận nặng - thận trọng",
                    "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                    "Dùng với aspirin/warfarin - tăng nguy cơ chảy máu"
                ]
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Thận trọng, có thể cần giảm liều",
                "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
                "dialysis": "Thận trọng, giảm liều. Ticlopidine không được lọc sạch hiệu quả qua thẩm phân máu.",
                "notes": "Ticlopidine thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy."
            },
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Category B - cần xem xét dữ liệu an toàn thai kỳ.",
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
                "oral": {
                "with_food": "Cần xem xét uống với hoặc không có thức ăn",
                "timing": "Cần xem xét thời điểm dùng",
                "notes": "Cần xem xét hướng dẫn cụ thể",
            },
            },
            "references": {
                "primary_sources": [
                "FDA Drug Label - Ticlopidine, Ticlid",
                "UpToDate - Drug information",
            ],
                "last_updated": "2025-02-05",
                "evidence_level": "A",
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["hematologic"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CBC", "WBC", "Platelet count"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Agranulocytosis/Thrombocytopenia",
                "FDA Black Box Warning - TTP (Thrombotic Thrombocytopenic Purpura)",
                "AHA/ASA Stroke Secondary Prevention Guidelines",
                "ISMP High Alert Medications - Antiplatelets"
            ]
        },

}

__all__ = ['ANTIPLATELETS_DRUGS']
