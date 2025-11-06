"""
Cardiovascular Drugs (Other) - Antiplatelets, Statins, ACE IV
"""

CARDIOVASCULAR_OTHER_DRUGS = {
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
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Cả hai đều ức chế tiểu cầu, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu chảy máu."
                },
                {
                    "drug": "Warfarin, Anticoagulants",
                    "mechanism": "Tác dụng cộng dồn chống đông máu.",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng, tăng INR",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, theo dõi INR chặt chẽ và điều chỉnh liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacids",
                    "mechanism": "Giảm hấp thu ticlopidine.",
                    "effect": "Giảm hiệu quả ticlopidine",
                    "management": "Cách ít nhất 2 giờ giữa ticlopidine và antacid."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Giảm bạch cầu nặng (<3500/μL)",
                "Giảm tiểu cầu nặng (<100,000/μL)",
                "Chảy máu đang hoạt động",
                "TTP (thrombotic thrombocytopenic purpura) trước đây",
                "Dị ứng ticlopidine"
            ],
            "tương_đối": [
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ độc tính",
                "Suy thận nặng - thận trọng",
                "Có thai - category B, thận trọng",
                "Đang dùng aspirin hoặc warfarin - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ticlopidine là category B. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt thứ ba (tăng nguy cơ chảy máu ở mẹ và thai nhi).",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết ticlopidine có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi chức năng gan. Ticlopidine chuyển hóa ở gan.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan và công thức máu chặt chẽ.",
            "severe": "Chống chỉ định hoặc thận trọng tối đa. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc tính.",
            "notes": "Ticlopidine là prodrug, chuyển hóa ở gan thành chất hoạt động. Suy gan làm giảm chuyển hóa, có thể giảm hiệu quả hoặc tăng độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu nghiêm trọng (xuất huyết, chảy máu cam, chảy máu tiêu hóa)",
                "Giảm bạch cầu, giảm tiểu cầu",
                "TTP (sốt, thiếu máu, giảm tiểu cầu, rối loạn thần kinh)",
                "Rối loạn tiêu hóa (buồn nôn, tiêu chảy)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ticlopidine ngay lập tức",
                "Theo dõi công thức máu (CBC) chặt chẽ",
                "Nếu chảy máu: truyền tiểu cầu nếu cần, điều trị hỗ trợ",
                "Nếu TTP: điều trị cấp cứu (plasma exchange, corticosteroids)",
                "Nếu giảm bạch cầu nặng: điều trị nhiễm trùng, có thể cần G-CSF",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Công thức máu, dấu hiệu chảy máu, dấu hiệu TTP, dấu hiệu nhiễm trùng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 2 lần/ngày (sáng và tối), cách đều. Cách xa antacid ít nhất 2 giờ."
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
                "FDA Drug Label - Ticlopidine (Ticlid)",
                "UpToDate - Ticlopidine: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },

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
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, Anticoagulants",
                    "mechanism": "Tác dụng cộng dồn chống đông máu.",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng, tăng INR",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, theo dõi INR chặt chẽ và điều chỉnh liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin",
                    "mechanism": "Cả hai đều ức chế tiểu cầu, tác dụng cộng dồn.",
                    "effect": "Tăng hiệu quả chống đông nhưng tăng nguy cơ chảy máu",
                    "management": "Thường dùng kết hợp (dipyridamole + aspirin 25mg x 2 lần/ngày). Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "Theophylline, Caffeine",
                    "mechanism": "Dipyridamole ức chế adenosine deaminase, tăng adenosine. Theophylline/caffeine đối kháng adenosine.",
                    "effect": "Giảm hiệu quả dipyridamole",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi đáp ứng điều trị."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Nhồi máu cơ tim cấp - có thể làm nặng thêm",
                "Co thắt mạch vành (vasospasm) - có thể làm nặng thêm",
                "Dị ứng dipyridamole"
            ],
            "tương_đối": [
                "Hạ huyết áp nặng - dipyridamole gây giãn mạch, có thể làm nặng hạ huyết áp",
                "Suy tim nặng - thận trọng",
                "Có thai - category B, thận trọng",
                "Đang dùng warfarin - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Dipyridamole là category B. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt thứ ba (tăng nguy cơ chảy máu ở mẹ và thai nhi).",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết dipyridamole có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan.",
            "severe": "Thận trọng, giảm liều. Suy gan nặng làm giảm chuyển hóa, có thể tăng nồng độ.",
            "notes": "Dipyridamole chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu nghiêm trọng (xuất huyết, chảy máu cam, chảy máu tiêu hóa)",
                "Hạ huyết áp nặng, ngất",
                "Nhức đầu nặng",
                "Chóng mặt, buồn nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng dipyridamole ngay lập tức",
                "Theo dõi huyết áp, nhịp tim",
                "Nếu chảy máu: điều trị hỗ trợ, truyền tiểu cầu nếu cần",
                "Nếu hạ huyết áp: truyền dịch, thuốc vận mạch nếu cần",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Huyết áp, nhịp tim, dấu hiệu chảy máu, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 2 lần/ngày (sáng và tối), cách đều. Dạng modified-release: uống 1-2 lần/ngày theo chỉ định."
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
                "FDA Drug Label - Dipyridamole (Persantine)",
                "UpToDate - Dipyridamole: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },

    "Rosuvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Rosuvastatin, Crestor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Phòng ngừa biến cố tim mạch",
            "Hội chứng chuyển hóa"
        ],
        "contraindications": [
            "Dị ứng rosuvastatin",
            "Bệnh gan hoạt động",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_start": "5-10mg x 1 lần/ngày (tối)",
            "adult_usual": "10-20mg x 1 lần/ngày",
            "adult_max": "40mg x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. Mạnh hơn atorvastatin ở liều tương đương"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Bắt đầu với 5mg/ngày"
        },
        "side_effects": [
            "Đau cơ, yếu cơ",
            "Tăng transaminase",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Đau đầu",
            "Táo bón",
            "Đái tháo đường (nguy cơ tăng nhẹ)"
        ],
        "interactions": [
            "Cyclosporine: tăng nguy cơ độc tính",
            "Gemfibrozil: tăng nguy cơ độc cơ",
            "Warfarin: tăng INR",
            "Rifampin: giảm nồng độ rosuvastatin"
        ],
        "pregnancy": "X - Chống chỉ định",
        "mechanism_of_action": "Statin (HMG-CoA reductase inhibitor). Ức chế không chọn lọc enzyme HMG-CoA reductase trong gan, enzyme chính trong tổng hợp cholesterol. Giảm tổng hợp cholesterol nội sinh → tăng số lượng LDL receptors trên bề mặt tế bào gan → tăng thanh thải LDL từ máu. Giảm LDL cholesterol, giảm triglyceride, tăng nhẹ HDL cholesterol. Có tác dụng chống viêm và ổn định mảng xơ vữa (pleiotropic effects). Được dùng trong tăng cholesterol máu, dự phòng biến cố tim mạch (nhồi máu cơ tim, đột quỵ).",
        "monitoring": [
            "Lipid profile (LDL, HDL, triglyceride, total cholesterol) - kiểm tra 4-12 tuần sau khi bắt đầu, sau đó định kỳ",
            "Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan",
            "CK (creatine kinase) - tăng CK, dấu hiệu tiêu cơ vân (myopathy, rhabdomyolysis)",
            "Dấu hiệu tiêu cơ vân (đau cơ, yếu cơ, nước tiểu sẫm màu) - nguy hiểm",
            "Đường huyết (có thể tăng nhẹ đường huyết)",
            "HbA1c (tăng nguy cơ đái tháo đường type 2)"
        ],
        "precautions": [
            "Nguy cơ tiêu cơ vân (myopathy, rhabdomyolysis) - nguy hiểm, có thể gây suy thận cấp",
            "Nguy cơ tăng ở: liều cao, suy thận, suy gan, người cao tuổi, dùng với fibrate, niacin, cyclosporine, diltiazem, verapamil",
            "NGỪNG NGAY nếu có đau cơ, yếu cơ, CK tăng > 10 lần ULN, hoặc dấu hiệu tiêu cơ vân",
            "Nguy cơ tăng men gan - kiểm tra ALT/AST trước khi bắt đầu, sau 12 tuần, và định kỳ",
            "Tăng nguy cơ đái tháo đường type 2 (nhẹ)",
            "Không dùng trong thai kỳ (gây dị tật thai nhi) - dùng biện pháp tránh thai",
            "Không dùng ở suy gan hoạt động",
            "Tương tác với nhiều thuốc: cyclosporine, gemfibrozil, diltiazem, verapamil → tăng nguy cơ tiêu cơ vân",
            "Liều khởi đầu thường: 10-20mg/ngày, liều tối đa: 40mg/ngày",
            "Uống với hoặc không có thức ăn"
        ],
        "pharmacokinetics": {
            "half_life": "19 giờ (dài)",
            "onset": "1-2 tuần (giảm LDL)",
            "duration": "Dài (nhiều ngày)",
            "protein_binding": "88%",
            "metabolism": "Gan (CYP2C9, CYP2C19) - chuyển hóa yếu, ít tương tác hơn các statin khác",
            "clearance": "Chủ yếu qua gan (90%), một phần qua thận (10%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Nguy cơ tiêu cơ vân (rhabdomyolysis), có thể gây suy thận cấp và tử vong. Nguy cơ tăng ở liều cao, suy thận, và dùng với một số thuốc. Ngừng ngay nếu có đau cơ, yếu cơ, hoặc dấu hiệu tiêu cơ vân. Không dùng trong thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cyclosporine ức chế OATP1B1 transporter và P-glycoprotein, tăng nồng độ rosuvastatin đáng kể",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, có thể gây suy thận cấp, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: giảm liều rosuvastatin tối đa 5mg/ngày, theo dõi CK và men gan thường xuyên. Cân nhắc dùng pravastatin (ít tương tác hơn)."
                },
                {
                    "drug": "Gemfibrozil, Fenofibrate (fibrates)",
                    "mechanism": "Fibrates và rosuvastatin đều có thể gây độc cơ, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể. Nếu cần: dùng liều thấp cả hai, theo dõi CK và dấu hiệu đau cơ thường xuyên. KHÔNG dùng gemfibrozil với rosuvastatin (tăng nguy cơ cao). Có thể cân nhắc fenofibrate (ít tương tác hơn gemfibrozil)."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Rosuvastatin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên khi bắt đầu hoặc thay đổi liều rosuvastatin. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Diltiazem, Verapamil",
                    "mechanism": "Có thể tăng nhẹ nồng độ rosuvastatin qua OATP1B1",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Giảm liều rosuvastatin 50% hoặc tối đa 10mg/ngày. Theo dõi CK và dấu hiệu đau cơ."
                },
                {
                    "drug": "Niacin (liều cao)",
                    "mechanism": "Cả hai đều có thể gây độc cơ, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Theo dõi CK và dấu hiệu đau cơ thường xuyên. Có thể cần giảm liều một trong hai thuốc."
                },
                {
                    "drug": "Colchicine",
                    "mechanism": "Có thể tăng tác dụng phụ độc cơ",
                    "effect": "Tăng nguy cơ độc cơ, đặc biệt ở bệnh nhân suy thận",
                    "management": "Thận trọng, đặc biệt ở bệnh nhân suy thận. Theo dõi CK và dấu hiệu đau cơ. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng OATP1B1, giảm hấp thu rosuvastatin",
                    "effect": "Giảm hiệu quả rosuvastatin",
                    "management": "Có thể cần tăng liều rosuvastatin. Theo dõi lipid profile."
                },
                {
                    "drug": "Oral contraceptives",
                    "mechanism": "Rosuvastatin có thể tăng nhẹ nồng độ estrogen",
                    "effect": "Tăng nhẹ tác dụng phụ của thuốc tránh thai",
                    "management": "Thường không cần điều chỉnh. Theo dõi tác dụng phụ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                "Dị ứng với rosuvastatin hoặc bất kỳ thành phần nào",
                "Dùng cùng cyclosporine (tăng nguy cơ tiêu cơ vân nghiêm trọng)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - bắt đầu với liều thấp (5mg/ngày)",
                "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                "Uống rượu nhiều - tăng nguy cơ viêm gan",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                "Dùng với fibrate, niacin liều cao - tăng nguy cơ tiêu cơ vân",
                "Bệnh nhân Châu Á - tăng nồng độ rosuvastatin, có thể cần liều thấp hơn"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Rosuvastatin gây dị tật thai nhi, đặc biệt trong tam cá nguyệt đầu tiên. Statins ức chế tổng hợp cholesterol, cần thiết cho sự phát triển của thai nhi. Có thể gây dị tật bẩm sinh, chậm phát triển. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Phải ngừng rosuvastatin ít nhất 1-2 tháng trước khi có thai. Nếu có thai khi đang dùng, ngừng ngay lập tức.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Rosuvastatin bài tiết vào sữa mẹ. Có thể gây tác dụng phụ trên trẻ bú mẹ. Chưa có dữ liệu đầy đủ về an toàn. Statins có thể ảnh hưởng đến sự phát triển của trẻ.",
                "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Ngừng rosuvastatin hoặc ngừng cho con bú. Cân nhắc thuốc thay thế nếu cần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều. Theo dõi men gan thường xuyên.",
            "moderate": "Thận trọng. Giảm liều hoặc dùng liều thấp hơn. Theo dõi men gan mỗi 3-6 tháng. Ngừng nếu ALT >3 lần ULN.",
            "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh nhân suy gan nặng hoặc bệnh gan hoạt động.",
            "notes": "Rosuvastatin chuyển hóa qua gan (CYP2C9, CYP2C19) - chuyển hóa yếu hơn atorvastatin/simvastatin, ít tương tác hơn. Tuy nhiên, suy gan vẫn có thể làm tăng nồng độ và tăng nguy cơ độc tính. Kiểm tra men gan trước điều trị. Ngừng nếu ALT >3 lần ULN hoặc có dấu hiệu viêm gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu cơ vân (rhabdomyolysis) - triệu chứng chính và nguy hiểm nhất",
                "Đau cơ dữ dội, yếu cơ",
                "Nước tiểu sẫm màu (myoglobinuria)",
                "Suy thận cấp (do myoglobin)",
                "Tăng men gan (ALT, AST)",
                "Tăng CK (creatine kinase)",
                "Mệt mỏi, buồn nôn",
                "Rối loạn tiêu hóa"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng rosuvastatin, truyền dịch tích cực để phòng suy thận, lọc máu nếu cần",
            "treatment": [
                "Ngừng rosuvastatin ngay lập tức",
                "Đo CK, men gan, chức năng thận ngay",
                "Nếu có tiêu cơ vân:",
                "  - Truyền dịch tích cực (normal saline 1-2L/giờ) để duy trì lượng nước tiểu >100-200ml/giờ",
                "  - Kiềm hóa nước tiểu (sodium bicarbonate) để giảm độc tính myoglobin trên thận",
                "  - Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu)",
                "  - Hemodialysis nếu suy thận cấp, tăng kali máu, hoặc quá tải dịch",
                "  - Theo dõi điện giải (natri, kali, canxi, phosphate)",
                "Điều trị hỗ trợ:",
                "  - Điều chỉnh rối loạn điện giải",
                "  - Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "  - Giảm đau (opioids) nếu đau cơ nặng",
                "Theo dõi CK, men gan, chức năng thận hàng ngày cho đến khi ổn định",
                "Theo dõi ít nhất 48-72 giờ do half-life 19 giờ (dài)"
            ],
            "monitoring": "CK, ALT, AST, creatinine, BUN, kali, canxi, phosphate, lượng nước tiểu, ECG (nếu có rối loạn điện giải), dấu hiệu suy thận"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, có thể uống vào buổi sáng hoặc buổi tối. Uống cùng một giờ mỗi ngày để nhớ. Không cần thiết phải uống buổi tối như simvastatin (rosuvastatin có half-life dài 19 giờ)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Rosuvastatin chỉ có dạng uống (PO)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Crestor (rosuvastatin)",
                "UpToDate - Rosuvastatin: Drug information",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "NLA Guidelines - Statin Safety (2014)",
                "JUPITER Study - New England Journal of Medicine (2008) - Rosuvastatin trong dự phòng biến cố tim mạch",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics - Lipid-lowering drugs"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (JUPITER, CORONA) showing cardiovascular benefit"
        }
    },

    "Enalaprilat": {
        "group": "Cardiovascular - ACE Inhibitor (IV)",
        "vietnamese_name": "Enalaprilat, Enalapril IV",
        "administration": ["IV"],
        "indications": [
            "Tăng huyết áp cấp cứu",
            "Suy tim cấp",
            "Khi không uống được"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "0.625-1.25mg IV mỗi 6 giờ",
            "adult_heart_failure": "0.625mg IV mỗi 6 giờ, tăng dần đến 1.25mg mỗi 6 giờ",
            "notes": "Khởi đầu với liều thấp, theo dõi huyết áp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Thận trọng, giảm liều 50%"
        },
        "side_effects": [
            "Hạ huyết áp (phổ biến)",
            "Ho khan",
            "Tăng kali máu",
            "Phù mạch",
            "Suy thận cấp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "Diuretics: tăng nguy cơ hạ huyết áp",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Enalaprilat là dạng hoạt chất của enalapril (enalapril là prodrug, chuyển hóa thành enalaprilat trong gan). Enalaprilat ức chế angiotensin converting enzyme (ACE), enzyme chuyển angiotensin I thành angiotensin II. Angiotensin II là chất co mạch mạnh và kích thích tiết aldosterone. Bằng cách ức chế ACE, enalaprilat giảm nồng độ angiotensin II, dẫn đến: giãn mạch (giảm sức cản mạch máu ngoại biên), giảm aldosterone (giảm tái hấp thu natri và nước ở thận, tăng bài tiết kali), giảm tiền gánh và hậu gánh tim, và giảm huyết áp. Enalaprilat cũng ức chế phân hủy bradykinin (chất giãn mạch), có thể góp phần vào tác dụng hạ huyết áp nhưng cũng gây ho khan (tác dụng phụ). Dạng IV tác dụng nhanh hơn enalapril uống, phù hợp cho cấp cứu tăng huyết áp và suy tim cấp.",
        "monitoring": [
            "Huyết áp liên tục (đặc biệt trong 30-60 phút đầu sau liều đầu tiên) - nguy cơ hạ huyết áp đột ngột",
            "Kali máu (tăng kali máu do giảm aldosterone) - theo dõi định kỳ",
            "Creatinine và eGFR (suy thận cấp có thể xảy ra, đặc biệt ở bệnh nhân hẹp động mạch thận)",
            "Dấu hiệu phù mạch (angioedema): sưng mặt, môi, lưỡi, họng - cấp cứu, cần ngừng ngay",
            "Dấu hiệu ho khan (tác dụng phụ phổ biến, có thể dai dẳng)",
            "Nhịp tim và ECG (đặc biệt nếu có tiền sử rối loạn nhịp)",
            "Dấu hiệu suy tim: khó thở, phù, tăng cân"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (0.625mg) và theo dõi huyết áp sát trong 30-60 phút đầu",
            "Nguy cơ hạ huyết áp đột ngột cao hơn so với enalapril uống (tác dụng nhanh hơn)",
            "Thận trọng ở bệnh nhân đang dùng diuretics (tăng nguy cơ hạ huyết áp) - có thể tạm ngừng diuretic trước khi bắt đầu",
            "Thận trọng ở bệnh nhân hẹp động mạch thận (có thể gây suy thận cấp)",
            "Thận trọng ở bệnh nhân suy thận (giảm liều, theo dõi creatinine)",
            "Thận trọng ở bệnh nhân đang dùng kali hoặc kali-sparing diuretics (tăng nguy cơ tăng kali máu)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Theo dõi phù mạch (angioedema) - có thể xảy ra ngay sau liều đầu tiên hoặc sau vài giờ",
            "Chuyển sang enalapril uống khi bệnh nhân có thể uống được",
            "Không dùng trong thai kỳ (chống chỉ định tuyệt đối - gây dị tật thai nhi)",
            "Thận trọng ở bệnh nhân có tiền sử phù mạch với ACE inhibitor khác"
        ],
        "pharmacokinetics": {
            "half_life": "11 giờ (enalaprilat, dài hơn enalapril)",
            "onset": "15 phút (IV, nhanh hơn enalapril uống)",
            "duration": "6 giờ (tiêm mỗi 6 giờ)",
            "protein_binding": "50-60%",
            "clearance": "Thận: bài tiết chủ yếu qua nước tiểu (không cần chuyển hóa như enalapril). Thời gian bán thải dài (11 giờ) so với enalapril (1 giờ) vì enalaprilat là chất chuyển hóa cuối cùng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Sau khi pha: dùng ngay, không bảo quản lâu. Theo hướng dẫn của nhà sản xuất về thời gian sử dụng sau khi pha.",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây tổn thương thai nhi và tử vong khi dùng trong tam cá nguyệt thứ hai và thứ ba. Phù mạch (angioedema) có thể xảy ra bất cứ lúc nào, có thể đe dọa tính mạng, cần ngừng ngay và điều trị cấp cứu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu.",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Giảm tác dụng giãn mạch, giảm lưu lượng máu thận.",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận, huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp.",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều diuretic hoặc tạm ngừng trước khi bắt đầu enalaprilat."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor giảm thải trừ lithium qua thận.",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium. Giảm liều lithium nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Có thai - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (gây dị tật thai nhi, tử vong thai nhi)",
                "Hẹp động mạch thận 2 bên - có thể gây suy thận cấp",
                "Phù mạch (angioedema) trước đây với ACE inhibitor",
                "Dị ứng enalaprilat hoặc ACE inhibitor"
            ],
            "tương_đối": [
                "Hẹp động mạch thận 1 bên - thận trọng, theo dõi chức năng thận",
                "Suy thận nặng - giảm liều, theo dõi creatinine",
                "Đang dùng diuretics - tăng nguy cơ hạ huyết áp",
                "Đang dùng kali hoặc kali-sparing diuretics - tăng nguy cơ tăng kali máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Enalaprilat là category D - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây tổn thương thai nhi và tử vong khi dùng trong tam cá nguyệt thứ hai và thứ ba. Có thể gây dị tật thai nhi (hội chứng ACE inhibitor: thiểu ối, suy thận, hạ huyết áp, thiểu sản phổi, gãy xương sọ, tử vong). Ngừng ngay nếu phát hiện có thai.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết enalaprilat có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Enalaprilat không cần chuyển hóa ở gan (là dạng hoạt động).",
            "moderate": "Không cần điều chỉnh liều. Enalaprilat không cần chuyển hóa ở gan.",
            "severe": "Không cần điều chỉnh liều. Enalaprilat không cần chuyển hóa ở gan.",
            "notes": "Enalaprilat là dạng hoạt động, không cần chuyển hóa ở gan (khác với enalapril uống là prodrug). Suy gan không ảnh hưởng đến nồng độ enalaprilat."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng, sốc",
                "Tăng kali máu nặng (rối loạn nhịp tim)",
                "Suy thận cấp",
                "Phù mạch (angioedema) - sưng mặt, môi, lưỡi, họng",
                "Ho khan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng enalaprilat ngay lập tức",
                "Nếu hạ huyết áp: đặt bệnh nhân nằm ngửa, nâng chân cao, truyền dịch (normal saline), thuốc vận mạch nếu cần (norepinephrine)",
                "Nếu tăng kali máu: điều chỉnh kali (calcium gluconate, insulin+glucose, sodium bicarbonate, kayexalate)",
                "Nếu phù mạch: epinephrine, corticosteroids, antihistamines, hỗ trợ hô hấp nếu cần",
                "Nếu suy thận cấp: điều trị hỗ trợ, có thể cần lọc máu",
                "Theo dõi huyết áp, nhịp tim, kali máu, creatinine liên tục"
            ],
            "monitoring": "Huyết áp, nhịp tim, kali máu, creatinine, dấu hiệu phù mạch, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - chỉ có dạng IV",
                "timing": "N/A - chỉ có dạng IV"
            },
            "iv": {
                "reconstitution": "Pha với normal saline hoặc D5W. Dùng ngay sau khi pha.",
                "infusion_rate": "Tiêm tĩnh mạch chậm trong 5 phút. Không truyền nhanh.",
                "compatibility": ["Normal saline", "D5W"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Tiêm tĩnh mạch chậm trong 5 phút. Theo dõi huyết áp sát trong 30-60 phút đầu. Chuyển sang enalapril uống khi bệnh nhân có thể uống được."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Enalaprilat (Vasotec IV)",
                "UpToDate - Enalaprilat: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },

}

__all__ = ['CARDIOVASCULAR_OTHER_DRUGS']
