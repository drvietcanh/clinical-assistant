"""Gastrointestinal Drugs - Digestive Enzymes
Pancreatin, Pancrelipase for pancreatic insufficiency"""

DIGESTIVE_ENZYMES_DRUGS = {
    "Pancreatin": {
        "group": "Gastrointestinal - Digestive Enzyme (Pancreatic Enzyme Replacement)",
        "vietnamese_name": "Pancreatin, Pancrex",
        "brand_names": {
            "common": ["Pancrex", "Creon (generic)", "Pancreaze"],
            "vietnam": ["Pancreatin", "Pancrex"]
        },
        "administration": ["PO"],
        "indications": [
            "Suy tụy ngoại tiết (pancreatic exocrine insufficiency)",
            "Xơ nang (cystic fibrosis)",
            "Viêm tụy mạn",
            "Cắt tụy",
            "Thiếu hụt enzyme tiêu hóa"
        ],
        "contraindications": [
            "Dị ứng pancreatin hoặc lợn (porcine)",
            "Viêm tụy cấp",
            "Tắc ruột cơ học"
        ],
        "dosage": {
            "adult_typical": "25,000-50,000 units lipase PO với mỗi bữa ăn, 10,000-25,000 units với bữa ăn nhẹ",
            "adult_cystic_fibrosis": "500-2,500 units lipase/kg/bữa ăn, tối đa 10,000 units/kg/ngày",
            "adult_max": "10,000 units lipase/kg/bữa ăn hoặc 4,000 units lipase/kg/bữa ăn nhẹ",
            "pediatric_dosing": "500-2,500 units lipase/kg/bữa ăn, tối đa 10,000 units/kg/ngày. Không vượt quá 6,000 units/kg/bữa ăn (nguy cơ fibrosing colonopathy)",
            "geriatric_dosing": "Không cần chỉnh liều, nhưng thận trọng ở người già",
            "notes": "Liều tính theo đơn vị lipase. Uống cùng với thức ăn. Không nhai hoặc nghiền viên (enteric-coated). Bắt đầu liều thấp và tăng dần theo đáp ứng."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
            "notes": "Pancreatin không hấp thu đáng kể, tác dụng tại chỗ ở ruột."
        },
        "side_effects": [
            "Đau bụng",
            "Buồn nôn",
            "Tiêu chảy",
            "Táo bón",
            "Phát ban (dị ứng protein lợn)",
            "Tăng acid uric máu (liều cao)",
            "Fibrosing colonopathy (liều rất cao ở trẻ em)"
        ],
        "interactions": [
            "Acarbose, Miglitol: giảm hiệu quả (pancreatin chứa amylase)",
            "Iron: có thể giảm hấp thu sắt"
        ],
        "pregnancy": "C - Dữ liệu hạn chế, chỉ dùng khi lợi ích > nguy cơ",
        "mechanism_of_action": "Pancreatic enzyme replacement. Pancreatin chứa các enzyme tiêu hóa từ tụy lợn: lipase (tiêu hóa chất béo), amylase (tiêu hóa tinh bột), và protease (tiêu hóa protein). Bù đắp thiếu hụt enzyme tiêu hóa trong suy tụy ngoại tiết, giúp tiêu hóa và hấp thu chất dinh dưỡng.",
        "monitoring": [
            "Triệu chứng lâm sàng: giảm đau bụng, cải thiện tiêu hóa, tăng cân",
            "Phân: giảm phân mỡ (steatorrhea)",
            "Dấu hiệu dị ứng (phát ban, khó thở)",
            "Acid uric máu (nếu dùng liều cao)"
        ],
        "precautions": [
            "Uống cùng với thức ăn để tăng hiệu quả",
            "Không nhai hoặc nghiền viên (enteric-coated, sẽ bị phá hủy bởi acid dạ dày)",
            "Bắt đầu liều thấp và tăng dần theo đáp ứng",
            "Tránh liều quá cao (nguy cơ fibrosing colonopathy ở trẻ em)",
            "Thận trọng ở bệnh nhân dị ứng protein lợn"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (enzyme, không hấp thu)",
            "onset": "Ngay lập tức khi vào ruột non",
            "duration": "Trong thời gian tiêu hóa bữa ăn",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân (không hấp thu đáng kể)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Không bảo quản trong tủ lạnh.",
        "black_box_warnings": "Nguy cơ fibrosing colonopathy ở trẻ em nếu dùng liều rất cao (>6,000 units lipase/kg/bữa ăn). Không vượt quá liều khuyến cáo.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Acarbose, Miglitol",
                    "mechanism": "Pancreatin chứa amylase, làm giảm hiệu quả acarbose/miglitol",
                    "effect": "Giảm hiệu quả điều trị đái tháo đường",
                    "management": "Thận trọng khi phối hợp."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng pancreatin hoặc protein lợn",
                "Viêm tụy cấp",
                "Tắc ruột cơ học"
            ],
            "tương_đối": [
                "Dị ứng protein lợn - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Pancreatin không hấp thu đáng kể, không vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Pancreatin không hấp thu đáng kể, không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Đau bụng",
                "Tiêu chảy",
                "Tăng acid uric máu",
                "Fibrosing colonopathy (liều rất cao)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Giảm liều",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "Theo dõi triệu chứng, acid uric máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống cùng với thức ăn để tăng hiệu quả",
                "timing": "Uống với mỗi bữa ăn và bữa ăn nhẹ. Không nhai hoặc nghiền viên (enteric-coated)."
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
            "FDA Drug Information",
            "Cystic Fibrosis Foundation Guidelines"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pancreatin",
                "UpToDate - Pancreatic enzyme replacement therapy",
                "Cystic Fibrosis Foundation Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, guideline-recommended"
        },
        "cost_estimate": {
            "generic": "Trung bình",
            "brand": "Trung bình-cao",
            "notes": "Có generic, giá hợp lý"
        }
    },
    
    "Pancrelipase": {
        "group": "Gastrointestinal - Digestive Enzyme (Pancreatic Enzyme Replacement)",
        "vietnamese_name": "Pancrelipase, Creon, Zenpep, Pertzye",
        "brand_names": {
            "common": ["Creon", "Zenpep", "Pertzye", "Viokace"],
            "vietnam": ["Pancrelipase", "Creon"]
        },
        "administration": ["PO"],
        "indications": [
            "Suy tụy ngoại tiết (pancreatic exocrine insufficiency)",
            "Xơ nang (cystic fibrosis)",
            "Viêm tụy mạn",
            "Cắt tụy",
            "Thiếu hụt enzyme tiêu hóa"
        ],
        "contraindications": [
            "Dị ứng pancrelipase hoặc lợn (porcine)",
            "Viêm tụy cấp",
            "Tắc ruột cơ học"
        ],
        "dosage": {
            "adult_typical": "25,000-50,000 units lipase PO với mỗi bữa ăn, 10,000-25,000 units với bữa ăn nhẹ",
            "adult_cystic_fibrosis": "500-2,500 units lipase/kg/bữa ăn, tối đa 10,000 units/kg/ngày",
            "adult_max": "10,000 units lipase/kg/bữa ăn hoặc 4,000 units lipase/kg/bữa ăn nhẹ",
            "pediatric_dosing": "500-2,500 units lipase/kg/bữa ăn, tối đa 10,000 units/kg/ngày. Không vượt quá 6,000 units/kg/bữa ăn (nguy cơ fibrosing colonopathy)",
            "geriatric_dosing": "Không cần chỉnh liều, nhưng thận trọng ở người già",
            "notes": "Liều tính theo đơn vị lipase. Uống cùng với thức ăn. Không nhai hoặc nghiền viên (enteric-coated). Bắt đầu liều thấp và tăng dần theo đáp ứng. Pancrelipase là dạng tinh khiết hơn pancreatin."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
            "notes": "Pancrelipase không hấp thu đáng kể, tác dụng tại chỗ ở ruột."
        },
        "side_effects": [
            "Đau bụng",
            "Buồn nôn",
            "Tiêu chảy",
            "Táo bón",
            "Phát ban (dị ứng protein lợn)",
            "Tăng acid uric máu (liều cao)",
            "Fibrosing colonopathy (liều rất cao ở trẻ em)"
        ],
        "interactions": [
            "Acarbose, Miglitol: giảm hiệu quả (pancrelipase chứa amylase)",
            "Iron: có thể giảm hấp thu sắt"
        ],
        "pregnancy": "C - Dữ liệu hạn chế, chỉ dùng khi lợi ích > nguy cơ",
        "mechanism_of_action": "Pancreatic enzyme replacement. Pancrelipase là dạng tinh khiết hơn pancreatin, chứa các enzyme tiêu hóa từ tụy lợn: lipase (tiêu hóa chất béo), amylase (tiêu hóa tinh bột), và protease (tiêu hóa protein). Bù đắp thiếu hụt enzyme tiêu hóa trong suy tụy ngoại tiết, giúp tiêu hóa và hấp thu chất dinh dưỡng.",
        "monitoring": [
            "Triệu chứng lâm sàng: giảm đau bụng, cải thiện tiêu hóa, tăng cân",
            "Phân: giảm phân mỡ (steatorrhea)",
            "Dấu hiệu dị ứng (phát ban, khó thở)",
            "Acid uric máu (nếu dùng liều cao)"
        ],
        "precautions": [
            "Uống cùng với thức ăn để tăng hiệu quả",
            "Không nhai hoặc nghiền viên (enteric-coated, sẽ bị phá hủy bởi acid dạ dày)",
            "Bắt đầu liều thấp và tăng dần theo đáp ứng",
            "Tránh liều quá cao (nguy cơ fibrosing colonopathy ở trẻ em)",
            "Thận trọng ở bệnh nhân dị ứng protein lợn"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (enzyme, không hấp thu)",
            "onset": "Ngay lập tức khi vào ruột non",
            "duration": "Trong thời gian tiêu hóa bữa ăn",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân (không hấp thu đáng kể)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Không bảo quản trong tủ lạnh.",
        "black_box_warnings": "Nguy cơ fibrosing colonopathy ở trẻ em nếu dùng liều rất cao (>6,000 units lipase/kg/bữa ăn). Không vượt quá liều khuyến cáo.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Acarbose, Miglitol",
                    "mechanism": "Pancrelipase chứa amylase, làm giảm hiệu quả acarbose/miglitol",
                    "effect": "Giảm hiệu quả điều trị đái tháo đường",
                    "management": "Thận trọng khi phối hợp."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng pancrelipase hoặc protein lợn",
                "Viêm tụy cấp",
                "Tắc ruột cơ học"
            ],
            "tương_đối": [
                "Dị ứng protein lợn - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Pancrelipase không hấp thu đáng kể, không vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Pancrelipase không hấp thu đáng kể, không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Đau bụng",
                "Tiêu chảy",
                "Tăng acid uric máu",
                "Fibrosing colonopathy (liều rất cao)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Giảm liều",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "Theo dõi triệu chứng, acid uric máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống cùng với thức ăn để tăng hiệu quả",
                "timing": "Uống với mỗi bữa ăn và bữa ăn nhẹ. Không nhai hoặc nghiền viên (enteric-coated)."
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
            "FDA Drug Information",
            "Cystic Fibrosis Foundation Guidelines"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pancrelipase (Creon, Zenpep, Pertzye)",
                "UpToDate - Pancreatic enzyme replacement therapy",
                "Cystic Fibrosis Foundation Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, guideline-recommended"
        },
        "cost_estimate": {
            "generic": "Trung bình-cao",
            "brand": "Cao",
            "notes": "Thuốc tinh chế, giá cao hơn pancreatin"
        }
    }
}

__all__ = ["DIGESTIVE_ENZYMES_DRUGS"]
