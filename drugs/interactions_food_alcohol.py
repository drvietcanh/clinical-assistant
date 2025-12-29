"""
Food and Alcohol Interactions Database
Drug-food and drug-alcohol interactions
"""

from typing import Dict, List, Optional
from .interactions_data import SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR

# Food interactions database
FOOD_INTERACTIONS: Dict[str, Dict] = {
    # === WARFARIN ===
    "Warfarin": {
        "foods": {
            "Vitamin K (Rau xanh)": {
                "severity": SEVERITY_MAJOR,
                "mechanism": "Vitamin K đối kháng với warfarin, làm giảm tác dụng chống đông",
                "description": "Rau xanh giàu vitamin K (cải bó xôi, bông cải xanh, rau diếp) làm giảm tác dụng warfarin",
                "management": "Duy trì lượng vitamin K ổn định trong chế độ ăn. Không nên thay đổi đột ngột lượng rau xanh. Theo dõi INR thường xuyên",
                "foods_list": ["Cải bó xôi", "Bông cải xanh", "Rau diếp", "Cải xoăn", "Bắp cải", "Đậu nành"]
            },
            "Cranberry": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Có thể tăng tác dụng warfarin",
                "description": "Nước ép cranberry có thể tăng nguy cơ xuất huyết",
                "management": "Tránh uống nhiều nước ép cranberry. Nếu uống, theo dõi INR"
            },
            "Alcohol": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Rượu ảnh hưởng đến chuyển hóa warfarin",
                "description": "Uống nhiều rượu có thể tăng hoặc giảm tác dụng warfarin",
                "management": "Hạn chế uống rượu. Nếu uống, chỉ uống vừa phải (1-2 ly/ngày)"
            }
        }
    },
    
    # === MAOIs ===
    "MAO Inhibitor": {
        "foods": {
            "Tyramine-rich foods": {
                "severity": SEVERITY_MAJOR,
                "mechanism": "Tyramine gây tăng huyết áp đột ngột, có thể gây đột quỵ",
                "description": "Thực phẩm giàu tyramine + MAOI gây tăng huyết áp nguy hiểm",
                "management": "Tránh hoàn toàn thực phẩm giàu tyramine khi dùng MAOI",
                "foods_list": ["Phô mai già", "Thịt xông khói", "Xúc xích", "Cá hun khói", "Rượu vang đỏ", "Bia", "Đậu fava", "Chuối chín"]
            }
        }
    },
    
    # === TETRACYCLINES ===
    "Tetracycline": {
        "foods": {
            "Dairy products": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Canxi trong sữa gắn với tetracycline, giảm hấp thu",
                "description": "Sữa, phô mai làm giảm hấp thu tetracycline",
                "management": "Uống tetracycline 1 giờ trước hoặc 2 giờ sau bữa ăn. Tránh sữa trong 2 giờ"
            },
            "Iron supplements": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Sắt gắn với tetracycline, giảm hấp thu cả hai",
                "management": "Uống cách nhau ít nhất 2 giờ"
            }
        }
    },
    "Doxycycline": {
        "foods": {
            "Dairy products": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Canxi làm giảm hấp thu doxycycline",
                "management": "Uống doxycycline với nước, tránh sữa trong 2 giờ"
            }
        }
    },
    
    # === FLUOROQUINOLONES ===
    "Ciprofloxacin": {
        "foods": {
            "Dairy products": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Canxi làm giảm hấp thu ciprofloxacin",
                "management": "Uống ciprofloxacin 1 giờ trước hoặc 2 giờ sau bữa ăn có sữa"
            },
            "Iron/Multivitamins": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Khoáng chất làm giảm hấp thu",
                "management": "Uống cách nhau ít nhất 2 giờ"
            }
        }
    },
    "Levofloxacin": {
        "foods": {
            "Dairy products": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Canxi làm giảm hấp thu",
                "management": "Uống cách xa bữa ăn có sữa"
            }
        }
    },
    
    # === STATINS ===
    "Atorvastatin": {
        "foods": {
            "Grapefruit": {
                "severity": SEVERITY_MAJOR,
                "mechanism": "Grapefruit ức chế CYP3A4, tăng nồng độ atorvastatin",
                "description": "Tăng nguy cơ tác dụng phụ (tiêu cơ vân, tổn thương gan)",
                "management": "Tránh hoàn toàn grapefruit và nước ép grapefruit"
            }
        }
    },
    "Simvastatin": {
        "foods": {
            "Grapefruit": {
                "severity": SEVERITY_MAJOR,
                "mechanism": "Grapefruit ức chế CYP3A4, tăng nồng độ simvastatin",
                "description": "Tăng nguy cơ tiêu cơ vân",
                "management": "Tránh hoàn toàn grapefruit"
            }
        }
    },
    "Lovastatin": {
        "foods": {
            "Grapefruit": {
                "severity": SEVERITY_MAJOR,
                "mechanism": "Grapefruit ức chế CYP3A4",
                "management": "Tránh hoàn toàn grapefruit"
            }
        }
    },
    
    # === METFORMIN ===
    "Metformin": {
        "foods": {
            "Alcohol": {
                "severity": SEVERITY_MAJOR,
                "mechanism": "Tăng nguy cơ nhiễm toan lactic",
                "description": "Rượu + metformin có thể gây nhiễm toan lactic nguy hiểm",
                "management": "Tránh uống rượu khi dùng metformin"
            }
        }
    },
    
    # === METRONIDAZOLE ===
    "Metronidazole": {
        "foods": {
            "Alcohol": {
                "severity": SEVERITY_MAJOR,
                "mechanism": "Phản ứng giống disulfiram (buồn nôn, nôn, đỏ mặt, nhịp tim nhanh)",
                "description": "Rượu + metronidazole gây phản ứng nghiêm trọng",
                "management": "Tránh hoàn toàn rượu trong và 48 giờ sau khi dùng metronidazole"
            }
        }
    },
    
    # === DISULFIRAM ===
    "Disulfiram": {
        "foods": {
            "Alcohol": {
                "severity": SEVERITY_MAJOR,
                "mechanism": "Ức chế aldehyde dehydrogenase, tích tụ acetaldehyde",
                "description": "Gây phản ứng nghiêm trọng: buồn nôn, nôn, đỏ mặt, nhịp tim nhanh, hạ huyết áp",
                "management": "Tránh hoàn toàn rượu và các sản phẩm có cồn"
            }
        }
    },
    
    # === ACE INHIBITORS ===
    "ACE Inhibitor": {
        "foods": {
            "Potassium-rich foods": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Tăng nguy cơ tăng kali máu",
                "description": "ACE inhibitor + thực phẩm giàu kali có thể gây tăng kali máu",
                "management": "Thận trọng với thực phẩm giàu kali (chuối, cam, khoai tây). Theo dõi kali máu",
                "foods_list": ["Chuối", "Cam", "Khoai tây", "Cà chua", "Rau xanh"]
            }
        }
    },
    
    # === LEVOTHYROXINE ===
    "Levothyroxine": {
        "foods": {
            "Soy": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Đậu nành làm giảm hấp thu levothyroxine",
                "management": "Uống levothyroxine 4 giờ trước hoặc sau khi ăn đậu nành"
            },
            "Iron/Calcium": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Khoáng chất làm giảm hấp thu",
                "management": "Uống cách nhau ít nhất 4 giờ"
            },
            "Coffee": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Cà phê làm giảm hấp thu",
                "management": "Uống levothyroxine với nước, không phải cà phê"
            }
        }
    },
    
    # === IRON SUPPLEMENTS ===
    "Iron": {
        "foods": {
            "Tea/Coffee": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Tanin trong trà/cà phê làm giảm hấp thu sắt",
                "management": "Uống sắt cách xa trà/cà phê ít nhất 1 giờ"
            },
            "Dairy products": {
                "severity": SEVERITY_MODERATE,
                "mechanism": "Canxi làm giảm hấp thu sắt",
                "management": "Uống cách nhau ít nhất 2 giờ"
            }
        }
    },
}


# Alcohol interactions database (standalone)
ALCOHOL_INTERACTIONS: Dict[str, Dict] = {
    "Warfarin": {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rượu ảnh hưởng đến chuyển hóa warfarin",
        "description": "Uống nhiều rượu có thể tăng hoặc giảm tác dụng warfarin, tăng nguy cơ xuất huyết",
        "management": "Hạn chế uống rượu. Nếu uống, chỉ uống vừa phải (1-2 ly/ngày). Theo dõi INR"
    },
    "Metformin": {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ nhiễm toan lactic",
        "description": "Rượu + metformin có thể gây nhiễm toan lactic nguy hiểm, đặc biệt ở bệnh nhân suy thận",
        "management": "Tránh uống rượu khi dùng metformin"
    },
    "Metronidazole": {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Phản ứng giống disulfiram",
        "description": "Rượu + metronidazole gây phản ứng nghiêm trọng: buồn nôn, nôn, đỏ mặt, nhịp tim nhanh",
        "management": "Tránh hoàn toàn rượu trong và 48 giờ sau khi dùng metronidazole"
    },
    "Disulfiram": {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ức chế aldehyde dehydrogenase",
        "description": "Gây phản ứng nghiêm trọng: buồn nôn, nôn, đỏ mặt, nhịp tim nhanh, hạ huyết áp",
        "management": "Tránh hoàn toàn rượu và các sản phẩm có cồn"
    },
    "Benzodiazepines": {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng an thần, ức chế hô hấp",
        "description": "Rượu + benzodiazepine tăng nguy cơ ức chế hô hấp, ngủ gà, tai nạn",
        "management": "Tránh uống rượu khi dùng benzodiazepine"
    },
    "Opioids": {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế hô hấp",
        "description": "Rượu + opioid tăng nguy cơ ức chế hô hấp, quá liều, tử vong",
        "management": "Tránh hoàn toàn rượu khi dùng opioid"
    },
    "Antihistamines": {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng an thần",
        "description": "Tăng nguy cơ ngủ gà, tai nạn",
        "management": "Thận trọng khi uống rượu"
    },
    "NSAIDs": {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày",
        "description": "Rượu + NSAID tăng nguy cơ loét và xuất huyết dạ dày",
        "management": "Hạn chế uống rượu khi dùng NSAID"
    },
    "Acetaminophen": {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tổn thương gan",
        "description": "Rượu + acetaminophen (đặc biệt liều cao) tăng nguy cơ tổn thương gan nghiêm trọng",
        "management": "Tránh uống rượu khi dùng acetaminophen, đặc biệt liều cao"
    },
    "Antibiotics": {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể ảnh hưởng đến hiệu quả và tăng tác dụng phụ",
        "description": "Một số kháng sinh có thể tương tác với rượu",
        "management": "Thận trọng khi uống rượu. Một số kháng sinh (metronidazole, tinidazole) cần tránh hoàn toàn"
    },
}


def get_food_interactions(drug_name: str) -> Optional[Dict]:
    """
    Get food interactions for a drug
    
    Args:
        drug_name: Drug name
        
    Returns:
        Dictionary of food interactions or None
    """
    return FOOD_INTERACTIONS.get(drug_name)


def get_alcohol_interaction(drug_name: str) -> Optional[Dict]:
    """
    Get alcohol interaction for a drug
    
    Args:
        drug_name: Drug name
        
    Returns:
        Dictionary with alcohol interaction info or None
    """
    return ALCOHOL_INTERACTIONS.get(drug_name)


def check_food_interactions(drug_list: List[str]) -> Dict[str, Dict]:
    """
    Check food interactions for a list of drugs
    
    Args:
        drug_list: List of drug names
        
    Returns:
        Dictionary mapping drug names to their food interactions
    """
    results = {}
    for drug in drug_list:
        food_interactions = get_food_interactions(drug)
        if food_interactions:
            results[drug] = food_interactions
    return results


def check_alcohol_interactions(drug_list: List[str]) -> Dict[str, Dict]:
    """
    Check alcohol interactions for a list of drugs
    
    Args:
        drug_list: List of drug names
        
    Returns:
        Dictionary mapping drug names to their alcohol interactions
    """
    results = {}
    for drug in drug_list:
        alcohol_interaction = get_alcohol_interaction(drug)
        if alcohol_interaction:
            results[drug] = alcohol_interaction
    return results

