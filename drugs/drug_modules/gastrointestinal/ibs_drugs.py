"""Gastrointestinal Drugs - IBS (Irritable Bowel Syndrome) Medications
Alosetron, Lubiprostone, Linaclotide, Plecanatide"""

IBS_DRUGS = {
    "Alosetron": {
        "group": "Gastrointestinal - IBS-D Treatment (5-HT3 Antagonist)",
        "vietnamese_name": "Alosetron, Lotronex",
        "brand_names": {
            "common": ["Lotronex"],
            "vietnam": ["Alosetron 0.5mg", "Lotronex"]
        },
        "administration": ["PO"],
        "indications": [
            "Hội chứng ruột kích thích thể tiêu chảy nặng ở nữ (IBS-D)",
            "Chỉ dùng khi các điều trị khác thất bại",
            "CHỈ DÙNG CHO NỮ (không dùng cho nam)"
        ],
        "contraindications": [
            "NAM GIỚI - CHỐNG CHỈ ĐỊNH",
            "IBS thể táo bón (IBS-C)",
            "Táo bón nặng",
            "Tắc ruột cơ học",
            "Viêm đại tràng",
            "Bệnh túi thừa",
            "Crohn's disease, Ulcerative colitis",
            "Dị ứng alosetron"
        ],
        "dosage": {
            "adult_female_initial": "0.5mg PO x 2 lần/ngày",
            "adult_female_increase": "Có thể tăng lên 1mg PO x 2 lần/ngày sau 4 tuần nếu đáp ứng tốt",
            "adult_female_max": "1mg PO x 2 lần/ngày",
            "pediatric_dosing": "Không khuyến cáo cho trẻ em",
            "geriatric_dosing": "Không cần chỉnh liều, nhưng thận trọng ở người già",
            "notes": "CHỈ DÙNG CHO NỮ. Bắt đầu liều thấp. Ngừng ngay nếu táo bón hoặc dấu hiệu thiếu máu cục bộ đại tràng. Cần đăng ký với chương trình quản lý rủi ro (REMS)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Táo bón (phổ biến, có thể nặng)",
            "Thiếu máu cục bộ đại tràng (ischemic colitis) - NGHIÊM TRỌNG, có thể tử vong",
            "Đau bụng",
            "Buồn nôn",
            "Đầy hơi"
        ],
        "interactions": [
            "Fluvoxamine (CYP1A2 inhibitor): tăng nồng độ alosetron",
            "Thuốc khác chuyển hóa qua CYP1A2: có thể tương tác"
        ],
        "pregnancy": "B - Dữ liệu hạn chế, chỉ dùng khi lợi ích > nguy cơ",
        "mechanism_of_action": "5-HT3 receptor antagonist. Ức chế chọn lọc receptor 5-HT3 ở ruột, giảm nhu động ruột và giảm cảm giác đau ở ruột. Giảm tiêu chảy và đau bụng trong IBS-D. Tuy nhiên, có nguy cơ nghiêm trọng gây thiếu máu cục bộ đại tràng và táo bón nặng.",
        "monitoring": [
            "Triệu chứng IBS-D: tần suất đi ngoài, đau bụng",
            "Dấu hiệu táo bón - ngừng ngay nếu táo bón",
            "Dấu hiệu thiếu máu cục bộ đại tràng: đau bụng đột ngột, dữ dội, máu trong phân, sốt - NGỪNG NGAY VÀ ĐI CẤP CỨU",
            "Công thức máu (CBC) - theo dõi thiếu máu"
        ],
        "precautions": [
            "CHỈ DÙNG CHO NỮ - CHỐNG CHỈ ĐỊNH ở nam",
            "CHỐNG CHỈ ĐỊNH ở IBS-C hoặc táo bón",
            "Nguy cơ thiếu máu cục bộ đại tràng - NGHIÊM TRỌNG, có thể tử vong",
            "Ngừng ngay nếu táo bón hoặc dấu hiệu thiếu máu cục bộ đại tràng",
            "Cần đăng ký với chương trình quản lý rủi ro (REMS)",
            "Chỉ dùng khi các điều trị khác thất bại"
        ],
        "pharmacokinetics": {
            "half_life": "1.5 giờ",
            "onset": "1-4 tuần",
            "duration": "Cần dùng liên tục",
            "protein_binding": "82%",
            "metabolism": "Gan (CYP1A2, CYP2C9, CYP3A4)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "NGUY CƠ NGHIÊM TRỌNG GÂY THIẾU MÁU CỤC BỘ ĐẠI TRÀNG (ischemic colitis), có thể tử vong. Nguy cơ táo bón nặng. CHỈ DÙNG CHO NỮ. CHỐNG CHỈ ĐỊNH ở nam, IBS-C, táo bón. Ngừng ngay nếu táo bón hoặc dấu hiệu thiếu máu cục bộ đại tràng (đau bụng đột ngột, dữ dội, máu trong phân).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Fluvoxamine",
                    "mechanism": "Fluvoxamine ức chế CYP1A2, làm giảm chuyển hóa alosetron",
                    "effect": "Tăng nồng độ alosetron, tăng nguy cơ tác dụng phụ",
                    "management": "Tránh dùng cùng hoặc giảm liều alosetron."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "NAM GIỚI - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "IBS thể táo bón (IBS-C)",
                "Táo bón nặng",
                "Tắc ruột cơ học",
                "Viêm đại tràng",
                "Bệnh túi thừa",
                "Crohn's disease, Ulcerative colitis",
                "Dị ứng alosetron"
            ],
            "tương_đối": [
                "Tiền sử thiếu máu cục bộ đại tràng",
                "Bệnh mạch máu",
                "Suy thận nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Tránh dùng",
            "notes": "Alosetron chuyển hóa ở gan. Suy gan nặng có thể làm tăng nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Táo bón nặng",
                "Đau bụng",
                "Dấu hiệu thiếu máu cục bộ đại tràng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc ngay",
                "Điều trị táo bón nếu có",
                "Điều trị thiếu máu cục bộ đại tràng nếu có (cấp cứu)"
            ],
            "monitoring": "Theo dõi triệu chứng, dấu hiệu thiếu máu cục bộ đại tràng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không với thức ăn",
                "timing": "Uống 2 lần/ngày. Bắt đầu liều thấp (0.5mg x 2 lần/ngày)."
            }
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["gastrointestinal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC", "Bowel symptoms"]
        },
        "guideline_tags": [
            "ACG IBS Guidelines",
            "FDA REMS Program",
            "FDA Black Box Warning"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Alosetron (Lotronex)",
                "UpToDate - Alosetron: Drug information",
                "ACG IBS Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved with REMS program, black box warning"
        },
        "cost_estimate": {
            "generic": "Cao",
            "brand": "Rất cao",
            "notes": "Thuốc đặc biệt, có REMS program, giá cao"
        }
    },
    
    "Lubiprostone": {
        "group": "Gastrointestinal - IBS-C Treatment (Chloride Channel Activator)",
        "vietnamese_name": "Lubiprostone, Amitiza",
        "brand_names": {
            "common": ["Amitiza"],
            "vietnam": ["Lubiprostone 8mcg/24mcg", "Amitiza"]
        },
        "administration": ["PO"],
        "indications": [
            "Hội chứng ruột kích thích thể táo bón ở nữ (IBS-C)",
            "Táo bón mạn tính vô căn",
            "Táo bón do opioid"
        ],
        "contraindications": [
            "Tắc ruột cơ học",
            "Dị ứng lubiprostone"
        ],
        "dosage": {
            "adult_ibs_c": "8mcg PO x 2 lần/ngày với thức ăn",
            "adult_chronic_constipation": "24mcg PO x 2 lần/ngày với thức ăn",
            "adult_opioid_constipation": "24mcg PO x 2 lần/ngày với thức ăn",
            "pediatric_dosing": "Không khuyến cáo cho trẻ em",
            "geriatric_dosing": "Không cần chỉnh liều, nhưng thận trọng ở người già",
            "notes": "Uống với thức ăn để giảm buồn nôn. Không nhai hoặc nghiền viên."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Buồn nôn (phổ biến, giảm khi uống với thức ăn)",
            "Tiêu chảy",
            "Đau bụng",
            "Đau đầu",
            "Chóng mặt",
            "Đầy hơi"
        ],
        "interactions": [
            "Ít tương tác thuốc đáng kể"
        ],
        "pregnancy": "C - Tránh dùng trong thai kỳ",
        "mechanism_of_action": "Chloride channel activator (CIC-2). Kích thích kênh chloride CIC-2 ở niêm mạc ruột, tăng tiết chloride vào lòng ruột. Chloride kéo theo natri và nước vào lòng ruột, làm mềm phân và tăng nhu động ruột. Giúp điều trị táo bón trong IBS-C và táo bón mạn tính.",
        "monitoring": [
            "Triệu chứng IBS-C: tần suất đi ngoài, đau bụng",
            "Dấu hiệu tiêu chảy",
            "Dấu hiệu buồn nôn"
        ],
        "precautions": [
            "Uống với thức ăn để giảm buồn nôn",
            "Không nhai hoặc nghiền viên",
            "Thận trọng ở bệnh nhân có tiền sử tắc ruột",
            "Tránh dùng trong thai kỳ"
        ],
        "pharmacokinetics": {
            "half_life": "0.9-1.4 giờ",
            "onset": "24-48 giờ",
            "duration": "Cần dùng liên tục",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa nhanh ở gan và các mô",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tránh dùng trong thai kỳ. Có thể gây sảy thai.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tắc ruột cơ học",
                "Dị ứng lubiprostone"
            ],
            "tương_đối": [
                "Mang thai - tránh dùng",
                "Tiền sử tắc ruột - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Có thể gây sảy thai.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng",
            "notes": "Lubiprostone chuyển hóa ở gan. Suy gan nặng có thể làm tăng nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn",
                "Tiêu chảy",
                "Đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Hỗ trợ triệu chứng",
                "Bù dịch nếu tiêu chảy nhiều"
            ],
            "monitoring": "Theo dõi triệu chứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm buồn nôn",
                "timing": "Uống 2 lần/ngày với thức ăn. Không nhai hoặc nghiền viên."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "ACG IBS Guidelines",
            "FDA Drug Information"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lubiprostone (Amitiza)",
                "UpToDate - Lubiprostone: Drug information",
                "ACG IBS Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, multiple RCTs"
        },
        "cost_estimate": {
            "generic": "Cao",
            "brand": "Rất cao",
            "notes": "Thuốc mới, giá cao"
        }
    },
    
    "Linaclotide": {
        "group": "Gastrointestinal - IBS-C Treatment (Guanylate Cyclase-C Agonist)",
        "vietnamese_name": "Linaclotide, Linzess",
        "brand_names": {
            "common": ["Linzess"],
            "vietnam": ["Linaclotide 145mcg/290mcg", "Linzess"]
        },
        "administration": ["PO"],
        "indications": [
            "Hội chứng ruột kích thích thể táo bón (IBS-C)",
            "Táo bón mạn tính vô căn"
        ],
        "contraindications": [
            "Trẻ em <6 tuổi - CHỐNG CHỈ ĐỊNH (nguy cơ mất nước nặng)",
            "Tắc ruột cơ học",
            "Dị ứng linaclotide"
        ],
        "dosage": {
            "adult_ibs_c": "290mcg PO x 1 lần/ngày khi bụng đói, 30 phút trước bữa ăn đầu tiên",
            "adult_chronic_constipation": "145mcg PO x 1 lần/ngày khi bụng đói, 30 phút trước bữa ăn đầu tiên",
            "pediatric_dosing": "CHỐNG CHỈ ĐỊNH ở trẻ em <6 tuổi. Trẻ em 6-17 tuổi: không khuyến cáo",
            "geriatric_dosing": "Không cần chỉnh liều, nhưng thận trọng ở người già",
            "notes": "Uống khi bụng đói, 30 phút trước bữa ăn đầu tiên. Không nhai hoặc nghiền viên. CHỐNG CHỈ ĐỊNH ở trẻ em <6 tuổi."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
            "notes": "Linaclotide không hấp thu đáng kể, tác dụng tại chỗ ở ruột."
        },
        "side_effects": [
            "Tiêu chảy (phổ biến, có thể nặng)",
            "Đau bụng",
            "Đầy hơi",
            "Mất nước (ở trẻ em - nguy hiểm)"
        ],
        "interactions": [
            "Ít tương tác thuốc đáng kể do không hấp thu đáng kể"
        ],
        "pregnancy": "C - Dữ liệu hạn chế, chỉ dùng khi lợi ích > nguy cơ",
        "mechanism_of_action": "Guanylate cyclase-C (GC-C) agonist. Kích thích thụ thể GC-C ở niêm mạc ruột, tăng cGMP nội bào. cGMP kích thích kênh CFTR (cystic fibrosis transmembrane conductance regulator), tăng tiết chloride và bicarbonate vào lòng ruột. Chloride và bicarbonate kéo theo natri và nước vào lòng ruột, làm mềm phân và tăng nhu động ruột. Giảm đau bụng do giảm nhạy cảm thần kinh ruột.",
        "monitoring": [
            "Triệu chứng IBS-C: tần suất đi ngoài, đau bụng",
            "Dấu hiệu tiêu chảy - có thể nặng",
            "Dấu hiệu mất nước (đặc biệt ở trẻ em)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở trẻ em <6 tuổi - nguy cơ mất nước nặng",
            "Uống khi bụng đói, 30 phút trước bữa ăn đầu tiên",
            "Không nhai hoặc nghiền viên",
            "Ngừng ngay nếu tiêu chảy nặng",
            "Thận trọng ở bệnh nhân có tiền sử tắc ruột"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu đáng kể)",
            "onset": "1-2 tuần",
            "duration": "Cần dùng liên tục",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân (không hấp thu đáng kể)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở trẻ em <6 tuổi. Nguy cơ mất nước nặng ở trẻ em do tiêu chảy.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Trẻ em <6 tuổi - CHỐNG CHỈ ĐỊNH",
                "Tắc ruột cơ học",
                "Dị ứng linaclotide"
            ],
            "tương_đối": [
                "Tiền sử tắc ruột - thận trọng",
                "Tiêu chảy nặng - ngừng thuốc"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Linaclotide không hấp thu đáng kể, không vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Linaclotide không hấp thu đáng kể, không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nhiều",
                "Mất nước",
                "Đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Bù dịch và điện giải",
                "Theo dõi dấu hiệu mất nước"
            ],
            "monitoring": "Theo dõi triệu chứng, dấu hiệu mất nước, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi bụng đói, 30 phút trước bữa ăn đầu tiên",
                "timing": "Uống 1 lần/ngày khi bụng đói, 30 phút trước bữa ăn đầu tiên. Không nhai hoặc nghiền viên."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "ACG IBS Guidelines",
            "FDA Drug Information",
            "FDA Black Box Warning"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Linaclotide (Linzess)",
                "UpToDate - Linaclotide: Drug information",
                "ACG IBS Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, multiple RCTs, black box warning for pediatric use"
        },
        "cost_estimate": {
            "generic": "Cao",
            "brand": "Rất cao",
            "notes": "Thuốc mới, giá cao"
        }
    }
}

__all__ = ["IBS_DRUGS"]
