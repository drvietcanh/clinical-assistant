"""
Drug Interaction Checker for Antibiotics
Kiểm tra tương tác thuốc khi phối hợp nhiều kháng sinh
"""

from typing import List, Dict, Tuple, Optional
from enum import Enum


class InteractionSeverity(Enum):
    """Mức độ nghiêm trọng của tương tác"""
    MAJOR = "major"  # Nghiêm trọng - cần tránh hoặc theo dõi chặt
    MINOR = "minor"  # Nhẹ - có thể dùng nhưng cần lưu ý
    INFO = "info"  # Thông tin - cần biết nhưng ít ảnh hưởng


# Database các tương tác thuốc phổ biến
# Format: (Drug1, Drug2): {severity, description, recommendation, monitoring}
DRUG_INTERACTIONS_DB = {
    # Vancomycin interactions
    ("Vancomycin", "Aminoglycosides"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ độc tính thận (nephrotoxicity) và độc tính tai (ototoxicity)",
        "recommendation": "Tránh phối hợp nếu có thể. Nếu cần thiết, theo dõi chặt chẽ chức năng thận và thính lực. Điều chỉnh liều dựa trên CrCl và nồng độ trong máu.",
        "monitoring": "Theo dõi SCr, BUN, CrCl hàng ngày. TDM cho cả hai thuốc. Khám thính lực định kỳ.",
        "alternatives": "Xem xét dùng kháng sinh khác hoặc dùng tuần tự thay vì đồng thời"
    },
    ("Vancomycin", "Gentamicin"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ độc tính thận và tai",
        "recommendation": "Tránh phối hợp. Nếu bắt buộc, theo dõi chặt chẽ và điều chỉnh liều.",
        "monitoring": "SCr, BUN, CrCl hàng ngày. TDM cho cả hai. Thính lực định kỳ.",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    ("Vancomycin", "Tobramycin"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ độc tính thận và tai",
        "recommendation": "Tránh phối hợp. Nếu bắt buộc, theo dõi chặt chẽ.",
        "monitoring": "SCr, BUN, CrCl hàng ngày. TDM cho cả hai.",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    ("Vancomycin", "Amikacin"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ độc tính thận và tai",
        "recommendation": "Tránh phối hợp. Nếu bắt buộc, theo dõi chặt chẽ.",
        "monitoring": "SCr, BUN, CrCl hàng ngày. TDM cho cả hai.",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    ("Vancomycin", "Piperacillin-Tazobactam"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ tổn thương thận cấp (acute kidney injury), đặc biệt khi dùng liều cao",
        "recommendation": "Có thể phối hợp nhưng cần theo dõi chặt chẽ chức năng thận. Tránh dùng liều cao đồng thời. Cân nhắc dùng tuần tự hoặc giảm liều.",
        "monitoring": "SCr, BUN, CrCl hàng ngày. Theo dõi nồng độ Vancomycin.",
        "alternatives": "Xem xét dùng beta-lactam khác hoặc điều chỉnh liều"
    },
    ("Vancomycin", "Ceftriaxone"): {
        "severity": InteractionSeverity.MINOR,
        "description": "Có thể tăng nguy cơ độc tính thận nhẹ",
        "recommendation": "Có thể phối hợp nhưng theo dõi chức năng thận.",
        "monitoring": "SCr, BUN định kỳ",
        "alternatives": None
    },
    
    # Aminoglycoside interactions
    ("Gentamicin", "Furosemide"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ độc tính tai và thận",
        "recommendation": "Tránh phối hợp nếu có thể. Nếu cần, theo dõi chặt chẽ và điều chỉnh liều.",
        "monitoring": "SCr, BUN, CrCl hàng ngày. TDM Gentamicin. Thính lực định kỳ.",
        "alternatives": "Xem xét dùng lợi tiểu khác hoặc dùng tuần tự"
    },
    ("Tobramycin", "Furosemide"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ độc tính tai và thận",
        "recommendation": "Tránh phối hợp nếu có thể.",
        "monitoring": "SCr, BUN, CrCl hàng ngày. TDM Tobramycin.",
        "alternatives": "Xem xét dùng lợi tiểu khác"
    },
    ("Amikacin", "Furosemide"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ độc tính tai và thận",
        "recommendation": "Tránh phối hợp nếu có thể.",
        "monitoring": "SCr, BUN, CrCl hàng ngày. TDM Amikacin.",
        "alternatives": "Xem xét dùng lợi tiểu khác"
    },
    
    # Fluoroquinolone interactions
    ("Ciprofloxacin", "Corticosteroids"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ đứt gân (tendon rupture), đặc biệt ở người cao tuổi",
        "recommendation": "Tránh phối hợp nếu có thể. Nếu cần, theo dõi triệu chứng đau gân, sưng. Ngừng ngay nếu có dấu hiệu.",
        "monitoring": "Theo dõi triệu chứng đau gân, sưng, khó vận động",
        "alternatives": "Xem xét dùng kháng sinh khác hoặc giảm liều corticosteroid"
    },
    ("Levofloxacin", "Corticosteroids"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ đứt gân",
        "recommendation": "Tránh phối hợp nếu có thể.",
        "monitoring": "Theo dõi triệu chứng đau gân",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    ("Moxifloxacin", "Corticosteroids"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ đứt gân",
        "recommendation": "Tránh phối hợp nếu có thể.",
        "monitoring": "Theo dõi triệu chứng đau gân",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    ("Ciprofloxacin", "Warfarin"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng tác dụng chống đông, tăng nguy cơ chảy máu",
        "recommendation": "Theo dõi chặt chẽ INR. Có thể cần giảm liều Warfarin.",
        "monitoring": "INR hàng ngày hoặc cách ngày",
        "alternatives": "Xem xét dùng kháng sinh khác hoặc điều chỉnh liều Warfarin"
    },
    ("Levofloxacin", "Warfarin"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng tác dụng chống đông",
        "recommendation": "Theo dõi chặt chẽ INR.",
        "monitoring": "INR hàng ngày",
        "alternatives": "Xem xét điều chỉnh liều Warfarin"
    },
    ("Ciprofloxacin", "Theophylline"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nồng độ Theophylline, tăng nguy cơ độc tính",
        "recommendation": "Theo dõi nồng độ Theophylline. Có thể cần giảm liều.",
        "monitoring": "Nồng độ Theophylline trong máu",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    
    # Metronidazole interactions
    ("Metronidazole", "Alcohol"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Phản ứng giống disulfiram: buồn nôn, nôn, đỏ mặt, nhịp tim nhanh",
        "recommendation": "Tránh uống rượu trong khi dùng và ít nhất 48 giờ sau khi ngừng Metronidazole.",
        "monitoring": "Theo dõi triệu chứng phản ứng disulfiram-like",
        "alternatives": "Tránh hoàn toàn rượu"
    },
    ("Metronidazole", "Warfarin"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng tác dụng chống đông",
        "recommendation": "Theo dõi chặt chẽ INR. Có thể cần giảm liều Warfarin.",
        "monitoring": "INR hàng ngày",
        "alternatives": "Xem xét điều chỉnh liều Warfarin"
    },
    
    # Beta-lactam interactions
    ("Piperacillin-Tazobactam", "Aminoglycosides"): {
        "severity": InteractionSeverity.MINOR,
        "description": "Có thể giảm hiệu quả của aminoglycoside trong ống nghiệm (in vitro), nhưng ít ảnh hưởng lâm sàng",
        "recommendation": "Có thể phối hợp. Dùng riêng biệt, không trộn trong cùng một bơm tiêm.",
        "monitoring": "Theo dõi đáp ứng điều trị và chức năng thận",
        "alternatives": None
    },
    ("Ceftriaxone", "Calcium"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Có thể tạo kết tủa với calcium, đặc biệt ở trẻ sơ sinh",
        "recommendation": "Tránh dùng Ceftriaxone với calcium trong cùng một đường truyền. Ở trẻ sơ sinh, tránh hoàn toàn.",
        "monitoring": "Theo dõi dấu hiệu tắc nghẽn đường truyền",
        "alternatives": "Dùng kháng sinh khác hoặc dùng riêng biệt"
    },
    
    # Macrolide interactions
    ("Erythromycin", "Warfarin"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng tác dụng chống đông",
        "recommendation": "Theo dõi chặt chẽ INR.",
        "monitoring": "INR hàng ngày",
        "alternatives": "Xem xét điều chỉnh liều Warfarin"
    },
    ("Azithromycin", "Warfarin"): {
        "severity": InteractionSeverity.MINOR,
        "description": "Có thể tăng nhẹ tác dụng chống đông",
        "recommendation": "Theo dõi INR.",
        "monitoring": "INR định kỳ",
        "alternatives": None
    },
    
    # Tetracycline interactions
    ("Doxycycline", "Warfarin"): {
        "severity": InteractionSeverity.MINOR,
        "description": "Có thể tăng nhẹ tác dụng chống đông",
        "recommendation": "Theo dõi INR.",
        "monitoring": "INR định kỳ",
        "alternatives": None
    },
    ("Doxycycline", "Calcium"): {
        "severity": InteractionSeverity.MINOR,
        "description": "Giảm hấp thu Doxycycline",
        "recommendation": "Dùng cách nhau ít nhất 2 giờ.",
        "monitoring": "Theo dõi đáp ứng điều trị",
        "alternatives": "Dùng cách thời gian"
    },
    
    # Sulfonamide interactions
    ("Trimethoprim-Sulfamethoxazole", "Warfarin"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng tác dụng chống đông",
        "recommendation": "Theo dõi chặt chẽ INR. Có thể cần giảm liều Warfarin.",
        "monitoring": "INR hàng ngày",
        "alternatives": "Xem xét điều chỉnh liều Warfarin"
    },
    ("Trimethoprim-Sulfamethoxazole", "Methotrexate"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng độc tính của Methotrexate (ức chế thải trừ)",
        "recommendation": "Tránh phối hợp. Nếu cần, giảm liều Methotrexate và theo dõi chặt chẽ.",
        "monitoring": "CBC, chức năng gan, thận",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    
    # Linezolid interactions
    ("Linezolid", "SSRI"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ hội chứng serotonin (serotonin syndrome)",
        "recommendation": "Tránh phối hợp với SSRI (Sertraline, Fluoxetine, Paroxetine, etc.).",
        "monitoring": "Theo dõi triệu chứng: kích động, tăng thân nhiệt, tăng phản xạ",
        "alternatives": "Xem xét dùng kháng sinh khác hoặc ngừng SSRI tạm thời"
    },
    ("Linezolid", "MAO inhibitors"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ hội chứng serotonin",
        "recommendation": "Tránh phối hợp.",
        "monitoring": "Theo dõi triệu chứng serotonin syndrome",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    
    # Colistin interactions
    ("Colistin", "Aminoglycosides"): {
        "severity": InteractionSeverity.MAJOR,
        "description": "Tăng nguy cơ độc tính thận và thần kinh",
        "recommendation": "Tránh phối hợp nếu có thể.",
        "monitoring": "SCr, BUN, CrCl hàng ngày. Theo dõi dấu hiệu thần kinh.",
        "alternatives": "Xem xét dùng kháng sinh khác"
    },
    ("Colistin", "Vancomycin"): {
        "severity": InteractionSeverity.MINOR,
        "description": "Có thể tăng nguy cơ độc tính thận",
        "recommendation": "Theo dõi chặt chẽ chức năng thận.",
        "monitoring": "SCr, BUN, CrCl hàng ngày",
        "alternatives": None
    },
}


def normalize_drug_name(drug_name: str) -> str:
    """
    Chuẩn hóa tên thuốc để so sánh (case-insensitive, loại bỏ khoảng trắng thừa)
    """
    if not drug_name:
        return ""
    return drug_name.strip().lower()


def find_interaction(drug1: str, drug2: str) -> Optional[Dict]:
    """
    Tìm tương tác giữa 2 thuốc
    
    Args:
        drug1: Tên thuốc thứ nhất
        drug2: Tên thuốc thứ hai
        
    Returns:
        Dict chứa thông tin tương tác nếu tìm thấy, None nếu không
    """
    if not drug1 or not drug2:
        return None
    
    # Normalize names
    norm1 = normalize_drug_name(drug1)
    norm2 = normalize_drug_name(drug2)
    
    if norm1 == norm2:
        return None
    
    # Check both orders: (drug1, drug2) and (drug2, drug1)
    for key in DRUG_INTERACTIONS_DB.keys():
        key_norm1 = normalize_drug_name(key[0])
        key_norm2 = normalize_drug_name(key[1])
        
        # Check if matches in either order
        if (norm1 == key_norm1 and norm2 == key_norm2) or \
           (norm1 == key_norm2 and norm2 == key_norm1):
            interaction = DRUG_INTERACTIONS_DB[key].copy()
            interaction["drug1"] = drug1
            interaction["drug2"] = drug2
            return interaction
    
    return None


def check_interactions(drug_list: List[str]) -> List[Dict]:
    """
    Kiểm tra tương tác giữa tất cả các cặp thuốc trong danh sách
    
    Args:
        drug_list: Danh sách tên thuốc
        
    Returns:
        List các tương tác tìm thấy, sắp xếp theo severity (major trước)
    """
    if not drug_list or len(drug_list) < 2:
        return []
    
    interactions = []
    
    # Check all pairs (nC2 combinations)
    for i in range(len(drug_list)):
        for j in range(i + 1, len(drug_list)):
            drug1 = drug_list[i]
            drug2 = drug_list[j]
            
            interaction = find_interaction(drug1, drug2)
            if interaction:
                interactions.append(interaction)
    
    # Sort by severity: MAJOR > MINOR > INFO
    severity_order = {
        InteractionSeverity.MAJOR: 0,
        InteractionSeverity.MINOR: 1,
        InteractionSeverity.INFO: 2
    }
    
    interactions.sort(key=lambda x: severity_order.get(x.get("severity"), 3))
    
    return interactions


def get_severity_color(severity: InteractionSeverity) -> str:
    """
    Trả về màu sắc tương ứng với severity
    """
    color_map = {
        InteractionSeverity.MAJOR: "#f44336",  # Red
        InteractionSeverity.MINOR: "#ff9800",  # Orange
        InteractionSeverity.INFO: "#2196f3"    # Blue
    }
    return color_map.get(severity, "#666")


def get_severity_icon(severity: InteractionSeverity) -> str:
    """
    Trả về icon tương ứng với severity
    """
    icon_map = {
        InteractionSeverity.MAJOR: "🔴",
        InteractionSeverity.MINOR: "🟡",
        InteractionSeverity.INFO: "ℹ️"
    }
    return icon_map.get(severity, "⚠️")


def get_severity_label_vi(severity: InteractionSeverity) -> str:
    """
    Trả về label tiếng Việt cho severity
    """
    label_map = {
        InteractionSeverity.MAJOR: "Nghiêm trọng",
        InteractionSeverity.MINOR: "Nhẹ",
        InteractionSeverity.INFO: "Thông tin"
    }
    return label_map.get(severity, "Không xác định")
