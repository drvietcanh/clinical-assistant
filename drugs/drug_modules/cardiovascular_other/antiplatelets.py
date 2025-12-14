"""
Cardiovascular Antiplatelet Drugs
Aspirin, Clopidogrel, Ticagrelor, Prasugrel, Ticlopidine, Dipyridamole
"""

ANTIPLATELETS_DRUGS = {
    "Aspirin": {
        "group": "Cardiovascular - Antiplatelet (COX-1 Inhibitor)",
        "vietnamese_name": "Aspirin, Acetylsalicylic acid, ASA",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa nhồi máu cơ tim",
            "Phòng ngừa đột quỵ/TIA",
            "Đau nhẹ đến trung bình",
            "Sốt",
            "Viêm khớp",
            "Hội chứng mạch vành cấp (kết hợp với P2Y12 inhibitor)",
            "Sau đặt stent (dual antiplatelet therapy)"
        ],
        "contraindications": [
            "Dị ứng aspirin/salicylate",
            "Loét dạ dày đang hoạt động",
            "Xuất huyết tiêu hóa",
            "Hemophilia",
            "Suy gan nặng",
            "Trẻ em <18 tuổi (hội chứng Reye)",
            "Tam cá nguyệt thứ ba thai kỳ"
        ],
        "dosage": {
            "adult_cardioprotection": "75-100mg x 1 lần/ngày",
            "adult_acs": "150-325mg x 1 lần (loading), sau đó 75-100mg/ngày",
            "adult_pain": "325-650mg mỗi 4-6 giờ (tối đa 4g/ngày)",
            "adult_arthritis": "3-6g/ngày chia nhiều lần",
            "notes": "Liều thấp (75-100mg/ngày) cho cardioprotection. Liều cao hơn cho đau/viêm"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, tránh liều cao"
        },
        "side_effects": [
            "Chảy máu tiêu hóa",
            "Loét dạ dày",
            "Chảy máu (tăng thời gian chảy máu)",
            "Buồn nôn, nôn",
            "Ợ nóng",
            "Hội chứng Reye (trẻ em)",
            "Phản ứng dị ứng (hen suyễn, phát ban)",
            "Suy thận (liều cao, kéo dài)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "NSAIDs: tăng nguy cơ loét dạ dày",
            "ACE inhibitors: có thể giảm hiệu quả",
            "Methotrexate: tăng độc tính",
            "Alcohol: tăng nguy cơ chảy máu tiêu hóa"
        ],
        "pregnancy": "D (tam cá nguyệt thứ ba), C (tam cá nguyệt 1-2)",
        "mechanism_of_action": "Aspirin (acetylsalicylic acid) ức chế không thể đảo ngược (irreversible) enzyme cyclooxygenase (COX), đặc biệt COX-1 trong tiểu cầu. COX-1 chuyển đổi arachidonic acid thành thromboxane A2 (TXA2), một chất kích thích mạnh aggregation tiểu cầu. Bằng cách ức chế COX-1, aspirin ngăn chặn sản xuất TXA2, ức chế kết tập tiểu cầu và giảm hình thành huyết khối. Tác dụng này kéo dài suốt đời tiểu cầu (7-10 ngày) vì tiểu cầu không thể tổng hợp protein mới. Aspirin cũng ức chế COX-2, giảm sản xuất prostaglandin gây viêm và đau. Liều thấp (75-100mg/ngày) đủ để ức chế COX-1 trong tiểu cầu mà ít ảnh hưởng đến COX-2, giảm tác dụng phụ. Liều cao hơn cần thiết cho tác dụng chống viêm và giảm đau.",
        "monitoring": [
            "Dấu hiệu chảy máu tiêu hóa (phân đen, nôn ra máu, đau bụng)",
            "Dấu hiệu loét dạ dày (đau thượng vị, ợ nóng)",
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, dễ bầm tím)",
            "Chức năng thận (nếu dùng liều cao, kéo dài)",
            "Chức năng gan (nếu dùng liều cao)",
            "Đáp ứng điều trị (giảm nguy cơ nhồi máu cơ tim, đột quỵ)"
        ],
        "precautions": [
            "Liều thấp (75-100mg/ngày) cho cardioprotection - đủ để ức chế tiểu cầu, ít tác dụng phụ",
            "Nguy cơ chảy máu tiêu hóa - đặc biệt ở người cao tuổi, tiền sử loét dạ dày, dùng NSAIDs",
            "Có thể dùng với PPI để giảm nguy cơ loét dạ dày",
            "Không dùng ở trẻ em <18 tuổi (hội chứng Reye - hiếm nhưng nguy hiểm)",
            "Tránh dùng trong tam cá nguyệt thứ ba (tăng nguy cơ chảy máu ở mẹ và thai nhi)",
            "Tránh dùng với warfarin (tăng nguy cơ chảy máu)",
            "Tránh dùng với NSAIDs (tăng nguy cơ loét dạ dày)",
            "Ngừng 7-10 ngày trước phẫu thuật lớn (do tác dụng kéo dài)",
            "Uống với thức ăn hoặc nước để giảm kích ứng dạ dày",
            "Enteric-coated aspirin có thể giảm kích ứng dạ dày nhưng không giảm nguy cơ chảy máu"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (aspirin), nhưng tác dụng trên tiểu cầu kéo dài 7-10 ngày (do irreversible inhibition)",
            "onset": "30-60 phút (giảm đau), ngay lập tức (ức chế tiểu cầu)",
            "duration": "7-10 ngày (ức chế tiểu cầu - suốt đời tiểu cầu), 4-6 giờ (giảm đau)",
            "protein_binding": "50-80%",
            "metabolism": "Gan (thủy phân thành salicylic acid, sau đó chuyển hóa)",
            "clearance": "Thận (bài tiết salicylic acid và metabolites)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Enteric-coated: bảo quản trong bao bì kín.",
        "black_box_warnings": "Không dùng ở trẻ em <18 tuổi với sốt hoặc nhiễm virus (hội chứng Reye - hiếm nhưng có thể tử vong). Tam cá nguyệt thứ ba: có thể gây chảy máu ở mẹ và thai nhi, đóng sớm ống động mạch.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, Anticoagulants",
                    "mechanism": "Aspirin ức chế tiểu cầu, tăng nguy cơ chảy máu. Aspirin cũng có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột.",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng, tăng INR",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ. Thường tránh dùng cùng, hoặc dùng liều aspirin thấp (75-100mg/ngày) với theo dõi sát."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "Cả hai đều ức chế COX, tác dụng cộng dồn. NSAIDs cũng có thể cạnh tranh với aspirin tại vị trí gắn COX-1.",
                    "effect": "Tăng nguy cơ loét dạ dày, chảy máu tiêu hóa",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, dùng với PPI. Ibuprofen có thể làm giảm hiệu quả cardioprotection của aspirin nếu dùng trước aspirin."
                }
            ],
            "moderate": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "Aspirin giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate",
                    "effect": "Tăng nguy cơ độc tính methotrexate (giảm bạch cầu, độc thận, viêm niêm mạc)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ nồng độ methotrexate, công thức máu, chức năng thận."
                },
                {
                    "drug": "ACE Inhibitors (captopril, lisinopril, enalapril)",
                    "mechanism": "Aspirin có thể ức chế tác dụng giãn mạch của ACE inhibitors",
                    "effect": "Có thể giảm hiệu quả hạ huyết áp và bảo vệ thận của ACE inhibitors",
                    "management": "Thận trọng. Thường dùng được nhưng có thể cần tăng liều ACE inhibitor. Theo dõi huyết áp, chức năng thận."
                }
            ],
            "minor": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Cả hai đều kích ứng niêm mạc dạ dày, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu tiêu hóa",
                    "management": "Tránh uống rượu khi dùng aspirin, đặc biệt liều cao."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng aspirin hoặc salicylate",
                "Loét dạ dày đang hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Hemophilia hoặc rối loạn đông máu khác",
                "Trẻ em <18 tuổi với sốt hoặc nhiễm virus (hội chứng Reye)",
                "Tam cá nguyệt thứ ba thai kỳ"
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày - thận trọng, cân nhắc dùng với PPI",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng, tránh liều cao",
                "Hen suyễn - có thể gây co thắt phế quản",
                "Gout - aspirin liều thấp có thể tăng acid uric, liều cao giảm acid uric"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D (tam cá nguyệt thứ ba), C (tam cá nguyệt 1-2)",
            "pregnancy_details": "Tam cá nguyệt 1-2: Category C. Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt thứ ba: Category D. Có thể gây chảy máu ở mẹ và thai nhi, đóng sớm ống động mạch. Tránh dùng trong tam cá nguyệt thứ ba, đặc biệt gần ngày sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Aspirin bài tiết vào sữa mẹ ở nồng độ thấp. Liều thấp (75-100mg/ngày) thường an toàn. Liều cao có thể gây tác dụng phụ ở trẻ bú mẹ (chảy máu, hội chứng Reye).",
                "recommendation": "Liều thấp (75-100mg/ngày) có thể dùng khi cho con bú. Tránh liều cao. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, tránh liều cao (giảm chuyển hóa)",
            "notes": "Aspirin chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu tiêu hóa (nôn ra máu, phân đen)",
                "Rối loạn thính giác (ù tai, điếc)",
                "Rối loạn hô hấp (tăng thông khí, toan chuyển hóa hô hấp)",
                "Toan chuyển hóa",
                "Sốt",
                "Co giật (liều rất cao)",
                "Hôn mê (liều rất cao)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Alkalinization nước tiểu để tăng thải trừ.",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Alkalinization nước tiểu (sodium bicarbonate IV) để tăng thải trừ salicylate",
                "Điều chỉnh toan chuyển hóa (sodium bicarbonate)",
                "Điều trị chảy máu: truyền máu, huyết tương tươi đông lạnh nếu cần",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi nồng độ salicylate trong máu",
                "Lọc máu (hemodialysis) nếu nồng độ salicylate rất cao (>100 mg/dL) hoặc có triệu chứng nặng"
            ],
            "monitoring": "Nồng độ salicylate trong máu, dấu hiệu sống, công thức máu, chức năng thận, dấu hiệu chảy máu, thính giác"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn hoặc nước để giảm kích ứng dạ dày. Enteric-coated aspirin có thể uống với hoặc không thức ăn.",
                "timing": "Liều cardioprotection (75-100mg/ngày): uống 1 lần/ngày, cùng giờ mỗi ngày. Liều đau/viêm: uống mỗi 4-6 giờ khi cần. Enteric-coated: không nghiền, không nhai."
            },
            "iv": {
                "reconstitution": "Không có dạng IV thông thường",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Aspirin chủ yếu có dạng uống. Có dạng IV (Lysine acetylsalicylate) nhưng ít dùng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aspirin",
                "American Heart Association/American College of Cardiology guidelines - Primary and Secondary Prevention",
                "UpToDate - Aspirin: Drug information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple large RCTs (Antithrombotic Trialists' Collaboration) and extensive clinical experience"
        }
    },

    "Clopidogrel": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Clopidogrel, Plavix",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp",
            "Sau đặt stent",
            "Sau nhồi máu cơ tim",
            "Sau đột quỵ/TIA",
            "Bệnh động mạch ngoại biên",
            "Phòng ngừa huyết khối"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Xuất huyết nội sọ",
            "Dị ứng"
        ],
        "dosage": {
            "adult_loading": "300-600mg x 1 lần",
            "adult_maintenance": "75mg x 1 lần/ngày",
            "notes": "Dùng kèm aspirin 75-100mg/ngày (dual antiplatelet therapy). Prodrug, cần chuyển hóa qua CYP2C19"
        },
        "side_effects": [
            "Chảy máu",
            "Ban xuất huyết giảm tiểu cầu huyết khối (TTP) - hiếm",
            "Rối loạn tiêu hóa",
            "Phát ban"
        ],
        "interactions": [
            "Aspirin: dùng kèm (dual antiplatelet therapy)",
            "Warfarin: tăng nguy cơ chảy máu",
            "PPIs (omeprazole, esomeprazole): có thể giảm hiệu quả (CYP2C19)",
            "CYP2C19 inhibitors: giảm hiệu quả"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Clopidogrel là thienopyridine, chất ức chế P2Y12 receptor, đối kháng không thể đảo ngược (irreversible) với P2Y12 receptor trên tiểu cầu. P2Y12 receptor là một thụ thể adenosine diphosphate (ADP) quan trọng trong quá trình hoạt hóa và kết tập tiểu cầu. Clopidogrel là prodrug, được chuyển hóa trong gan qua nhiều bước, chủ yếu qua CYP2C19, thành metabolite hoạt động. Metabolite hoạt động gắn không thể đảo ngược với P2Y12 receptor, ức chế kết tập tiểu cầu do ADP. Clopidogrel giảm nguy cơ huyết khối trong hội chứng mạch vành cấp, sau can thiệp mạch vành (PCI), và sau đột quỵ/TIA. Hiệu quả phụ thuộc vào chuyển hóa qua CYP2C19 - một số bệnh nhân có biến thể di truyền (poor metabolizers) có thể giảm đáp ứng.",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu tại vị trí tiêm)",
            "Chảy máu lớn (xuất huyết tiêu hóa, xuất huyết nội sọ, chảy máu sau phẫu thuật)",
            "Thrombotic thrombocytopenic purpura (TTP) - hiếm nhưng nguy hiểm (sốt, thiếu máu, giảm tiểu cầu, rối loạn thần kinh)",
            "Công thức máu (tiểu cầu) nếu có dấu hiệu chảy máu",
            "Đáp ứng điều trị (giảm nguy cơ huyết khối)",
            "Tương tác với CYP2C19 inhibitors (omeprazole, esomeprazole) - có thể giảm hiệu quả"
        ],
        "precautions": [
            "Dùng kèm với aspirin 75-100mg/ngày (dual antiplatelet therapy - DAPT)",
            "Không ngừng đột ngột (tăng nguy cơ huyết khối)",
            "Nguy cơ chảy máu cao - không dùng nếu có chảy máu đang hoạt động, xuất huyết nội sọ",
            "Tương tác với PPIs (omeprazole, esomeprazole) - có thể giảm hiệu quả do ức chế CYP2C19. Cân nhắc dùng pantoprazole hoặc H2 blockers thay thế.",
            "Biến thể di truyền CYP2C19 (poor metabolizers) - có thể giảm đáp ứng, cân nhắc dùng prasugrel hoặc ticagrelor",
            "Thời gian DAPT thường 12 tháng sau ACS hoặc đặt stent, có thể kéo dài ở một số bệnh nhân nguy cơ cao",
            "Ngừng 5-7 ngày trước phẫu thuật lớn (do irreversible binding)"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ (clopidogrel), nhưng tác dụng trên tiểu cầu kéo dài 7-10 ngày (do irreversible binding)",
            "onset": "2-6 giờ (sau loading dose 300-600mg), 3-7 ngày (sau liều duy trì 75mg/ngày)",
            "duration": "7-10 ngày sau khi ngừng (do irreversible binding - tiểu cầu mới không bị ảnh hưởng)",
            "protein_binding": "98%",
            "clearance": "Gan: chuyển hóa qua CYP2C19 (chủ yếu), CYP3A4, CYP2B6 thành metabolite hoạt động. Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có xuất huyết nội sọ đang hoạt động, chảy máu đang hoạt động. Hiệu quả phụ thuộc vào chuyển hóa qua CYP2C19 - một số bệnh nhân có biến thể di truyền (poor metabolizers) có thể giảm đáp ứng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, Anticoagulants",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi INR, dấu hiệu chảy máu. Thường tránh dùng cùng."
                },
                {
                    "drug": "PPIs - Omeprazole, Esomeprazole",
                    "mechanism": "Ức chế CYP2C19, giảm chuyển hóa clopidogrel thành metabolite hoạt động",
                    "effect": "Giảm hiệu quả clopidogrel, tăng nguy cơ huyết khối",
                    "management": "Tránh dùng omeprazole và esomeprazole. Có thể dùng pantoprazole (ít ức chế CYP2C19) hoặc H2 blockers (ranitidine, famotidine)."
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
                    "drug": "CYP2C19 inhibitors khác (fluconazole, voriconazole, cimetidine)",
                    "mechanism": "Ức chế chuyển hóa clopidogrel qua CYP2C19",
                    "effect": "Giảm hiệu quả clopidogrel",
                    "management": "Thận trọng. Có thể cần tăng liều clopidogrel hoặc đổi sang prasugrel/ticagrelor."
                }
            ],
            "minor": [
                {
                    "drug": "CYP3A4 inhibitors/inducers",
                    "mechanism": "Clopidogrel chuyển hóa một phần qua CYP3A4",
                    "effect": "Có thể ảnh hưởng nhẹ đến hiệu quả",
                    "management": "Thận trọng. Theo dõi đáp ứng điều trị."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Xuất huyết nội sọ đang hoạt động",
                "Dị ứng clopidogrel"
            ],
            "tương_đối": [
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Poor metabolizers CYP2C19 - có thể giảm đáp ứng, cân nhắc dùng prasugrel/ticagrelor"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ chảy máu ở mẹ và thai nhi. Cân nhắc nguy cơ huyết khối vs nguy cơ chảy máu. Theo dõi chặt chẽ dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Caution",
                "details": "Clopidogrel và metabolite có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ về dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng",
            "notes": "Clopidogrel chuyển hóa ở gan qua CYP2C19, CYP3A4, CYP2B6. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu lớn có thể nghiêm trọng và đe dọa tính mạng",
                "Thrombotic thrombocytopenic purpura (TTP) - hiếm nhưng nguy hiểm"
            ],
            "antidote": "Không có antidote đặc hiệu. Truyền tiểu cầu nếu cần (hiệu quả hạn chế do irreversible binding)",
            "treatment": [
                "Ngừng clopidogrel ngay lập tức",
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
                "timing": "Uống 1 lần/ngày. Loading dose: 300-600mg x 1 lần. Maintenance: 75mg x 1 lần/ngày. Dùng kèm aspirin 75-100mg/ngày."
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
                "FDA Drug Label - Plavix (clopidogrel)",
                "CURE Study - New England Journal of Medicine",
                "CAPRIE Study - The Lancet",
                "UpToDate - Clopidogrel: Drug information",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Large RCTs (CURE, CAPRIE studies) and extensive clinical experience"
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
    }
}

__all__ = ['ANTIPLATELETS_DRUGS']

