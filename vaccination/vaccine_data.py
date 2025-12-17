"""
Vaccine Data - Comprehensive vaccine information for Vietnam
Includes vaccines for children and adults, schedules, and prices
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class Vaccine:
    """Vaccine information"""
    name: str
    name_vn: str
    category: str
    target_age: str  # "children", "adults", "both"
    manufacturer: str
    price_range: str  # Price in VND
    description: str
    indications: List[str]
    contraindications: List[str]
    side_effects: List[str]
    schedule: Dict[str, str]  # Age/condition: schedule description
    notes: str = ""


# Vaccines for Children
VACCINES_CHILDREN = [
    Vaccine(
        name="BCG",
        name_vn="Vắc xin phòng lao",
        category="Bắt buộc",
        target_age="children",
        manufacturer="Việt Nam",
        price_range="Miễn phí (Chương trình TCMR)",
        description="Vắc xin phòng bệnh lao, tiêm ngay sau sinh",
        indications=["Trẻ sơ sinh", "Trẻ chưa tiêm BCG"],
        contraindications=["Nhiễm trùng cấp", "Suy giảm miễn dịch nặng"],
        side_effects=["Sưng đỏ tại chỗ tiêm", "Sốt nhẹ", "Áp xe tại chỗ tiêm"],
        schedule={
            "Sơ sinh": "1 mũi ngay sau sinh hoặc trong tháng đầu"
        },
        notes="Tiêm trong da, thường ở cánh tay trái"
    ),
    Vaccine(
        name="Hepatitis B",
        name_vn="Vắc xin viêm gan B",
        category="Bắt buộc",
        target_age="children",
        manufacturer="Việt Nam, Hàn Quốc",
        price_range="Miễn phí (TCMR) hoặc 150.000 - 300.000 VNĐ",
        description="Vắc xin phòng viêm gan B, tiêm ngay sau sinh",
        indications=["Trẻ sơ sinh", "Trẻ em chưa tiêm đủ"],
        contraindications=["Dị ứng với thành phần", "Sốt cao"],
        side_effects=["Đau tại chỗ tiêm", "Sốt nhẹ"],
        schedule={
            "Sơ sinh": "Mũi 1: trong 24h đầu sau sinh",
            "2 tháng": "Mũi 2",
            "3-4 tháng": "Mũi 3",
            "Nhắc lại": "Sau 1 năm (mũi 4)"
        }
    ),
    Vaccine(
        name="DTP",
        name_vn="Vắc xin bạch hầu - ho gà - uốn ván",
        category="Bắt buộc",
        target_age="children",
        manufacturer="Việt Nam, Ấn Độ",
        price_range="Miễn phí (TCMR) hoặc 200.000 - 400.000 VNĐ",
        description="Vắc xin phối hợp phòng 3 bệnh: bạch hầu, ho gà, uốn ván",
        indications=["Trẻ từ 2 tháng tuổi"],
        contraindications=["Dị ứng với thành phần", "Sốt cao", "Co giật"],
        side_effects=["Sưng đỏ tại chỗ", "Sốt", "Quấy khóc"],
        schedule={
            "2 tháng": "Mũi 1",
            "3 tháng": "Mũi 2",
            "4 tháng": "Mũi 3",
            "18 tháng": "Mũi 4 (nhắc lại)",
            "6-7 tuổi": "Mũi 5 (nhắc lại)"
        }
    ),
    Vaccine(
        name="Polio",
        name_vn="Vắc xin bại liệt",
        category="Bắt buộc",
        target_age="children",
        manufacturer="Việt Nam",
        price_range="Miễn phí (TCMR)",
        description="Vắc xin phòng bại liệt, có thể uống hoặc tiêm",
        indications=["Trẻ từ 2 tháng tuổi"],
        contraindications=["Suy giảm miễn dịch", "Dị ứng"],
        side_effects=["Sốt nhẹ", "Tiêu chảy nhẹ (nếu uống)"],
        schedule={
            "2 tháng": "Liều 1",
            "3 tháng": "Liều 2",
            "4 tháng": "Liều 3",
            "18 tháng": "Liều 4 (nhắc lại)"
        }
    ),
    Vaccine(
        name="MMR",
        name_vn="Vắc xin sởi - quai bị - rubella",
        category="Bắt buộc",
        target_age="children",
        manufacturer="Ấn Độ, Bỉ",
        price_range="Miễn phí (TCMR) hoặc 200.000 - 400.000 VNĐ",
        description="Vắc xin phối hợp phòng sởi, quai bị, rubella",
        indications=["Trẻ từ 9 tháng tuổi"],
        contraindications=["Dị ứng trứng", "Suy giảm miễn dịch", "Mang thai"],
        side_effects=["Sốt", "Phát ban nhẹ", "Sưng tuyến nước bọt"],
        schedule={
            "9 tháng": "Mũi 1 (Sởi đơn)",
            "18 tháng": "Mũi 2 (MMR)",
            "6-7 tuổi": "Mũi 3 (MMR nhắc lại)"
        }
    ),
    Vaccine(
        name="Japanese Encephalitis",
        name_vn="Vắc xin viêm não Nhật Bản",
        category="Bắt buộc",
        target_age="children",
        manufacturer="Việt Nam, Ấn Độ",
        price_range="Miễn phí (TCMR) hoặc 200.000 - 350.000 VNĐ",
        description="Vắc xin phòng viêm não Nhật Bản",
        indications=["Trẻ từ 12 tháng tuổi"],
        contraindications=["Dị ứng", "Sốt cao"],
        side_effects=["Sưng đỏ tại chỗ", "Sốt"],
        schedule={
            "12 tháng": "Mũi 1",
            "13 tháng": "Mũi 2 (cách 1-2 tuần)",
            "24 tháng": "Mũi 3 (nhắc lại)"
        }
    ),
    Vaccine(
        name="Pneumococcal",
        name_vn="Vắc xin phế cầu khuẩn",
        category="Khuyến nghị",
        target_age="children",
        manufacturer="Pháp, Bỉ",
        price_range="1.200.000 - 1.500.000 VNĐ/mũi",
        description="Vắc xin phòng viêm phổi, viêm màng não do phế cầu",
        indications=["Trẻ từ 2 tháng tuổi", "Trẻ có nguy cơ cao"],
        contraindications=["Dị ứng", "Sốt cao"],
        side_effects=["Sưng đỏ", "Sốt", "Quấy khóc"],
        schedule={
            "2-6 tháng": "3 mũi cơ bản (cách 1-2 tháng), 1 mũi nhắc lại (12-15 tháng)",
            "7-11 tháng": "2 mũi (cách 1-2 tháng), 1 mũi nhắc lại (12-15 tháng)",
            "12-23 tháng": "2 mũi (cách 2 tháng)",
            "2-5 tuổi": "1 mũi"
        },
        notes="Prevenar 13 hoặc Synflorix"
    ),
    Vaccine(
        name="Rotavirus",
        name_vn="Vắc xin rota",
        category="Khuyến nghị",
        target_age="children",
        manufacturer="Bỉ, Bỉ",
        price_range="700.000 - 1.000.000 VNĐ/mũi",
        description="Vắc xin phòng tiêu chảy do rotavirus",
        indications=["Trẻ từ 6 tuần tuổi"],
        contraindications=["Dị ứng", "Lồng ruột trước đó", "Suy giảm miễn dịch"],
        side_effects=["Quấy khóc", "Tiêu chảy nhẹ", "Nôn"],
        schedule={
            "6 tuần - 6 tháng": "2-3 mũi (Rotarix: 2 mũi, Rotateq: 3 mũi), cách 1-2 tháng"
        },
        notes="Uống, không tiêm"
    ),
    Vaccine(
        name="Hib",
        name_vn="Vắc xin Hib",
        category="Khuyến nghị",
        target_age="children",
        manufacturer="Pháp, Bỉ",
        price_range="400.000 - 600.000 VNĐ/mũi",
        description="Vắc xin phòng viêm màng não, viêm phổi do Hib",
        indications=["Trẻ từ 2 tháng tuổi"],
        contraindications=["Dị ứng"],
        side_effects=["Sưng đỏ", "Sốt"],
        schedule={
            "2-6 tháng": "3 mũi cơ bản (cách 1-2 tháng), 1 mũi nhắc lại (12-18 tháng)",
            "7-11 tháng": "2 mũi (cách 1-2 tháng), 1 mũi nhắc lại (12-18 tháng)",
            "12-59 tháng": "1 mũi"
        }
    ),
    Vaccine(
        name="Varicella",
        name_vn="Vắc xin thủy đậu",
        category="Khuyến nghị",
        target_age="children",
        manufacturer="Bỉ, Hàn Quốc",
        price_range="400.000 - 600.000 VNĐ/mũi",
        description="Vắc xin phòng thủy đậu",
        indications=["Trẻ từ 12 tháng tuổi", "Chưa mắc thủy đậu"],
        contraindications=["Dị ứng", "Suy giảm miễn dịch", "Mang thai"],
        side_effects=["Sưng đỏ", "Sốt", "Phát ban nhẹ"],
        schedule={
            "12-18 tháng": "Mũi 1",
            "4-6 tuổi": "Mũi 2 (nhắc lại)"
        }
    ),
    Vaccine(
        name="Hepatitis A",
        name_vn="Vắc xin viêm gan A",
        category="Khuyến nghị",
        target_age="children",
        manufacturer="Pháp, Bỉ",
        price_range="1.000.000 - 1.300.000 VNĐ/mũi",
        description="Vắc xin phòng viêm gan A",
        indications=["Trẻ từ 12 tháng tuổi"],
        contraindications=["Dị ứng", "Sốt cao"],
        side_effects=["Sưng đỏ", "Sốt", "Mệt mỏi"],
        schedule={
            "12-23 tháng": "2 mũi (cách 6-12 tháng)",
            "≥2 tuổi": "2 mũi (cách 6-12 tháng)"
        },
        notes="Avaxim hoặc Havrix"
    ),
    Vaccine(
        name="Meningococcal",
        name_vn="Vắc xin não mô cầu",
        category="Khuyến nghị",
        target_age="children",
        manufacturer="Pháp, Bỉ",
        price_range="600.000 - 900.000 VNĐ/mũi",
        description="Vắc xin phòng viêm màng não do não mô cầu",
        indications=["Trẻ từ 6 tháng tuổi", "Trẻ có nguy cơ cao"],
        contraindications=["Dị ứng"],
        side_effects=["Sưng đỏ", "Sốt"],
        schedule={
            "6-23 tháng": "2 mũi (cách 2-3 tháng)",
            "≥2 tuổi": "1 mũi, nhắc lại sau 3-5 năm"
        },
        notes="Menactra hoặc Menveo"
    ),
    Vaccine(
        name="Influenza",
        name_vn="Vắc xin cúm",
        category="Khuyến nghị",
        target_age="both",
        manufacturer="Pháp, Hàn Quốc",
        price_range="300.000 - 500.000 VNĐ/mũi",
        description="Vắc xin phòng cúm mùa, tiêm hàng năm",
        indications=["Trẻ từ 6 tháng tuổi", "Người lớn"],
        contraindications=["Dị ứng trứng nặng", "Dị ứng với thành phần"],
        side_effects=["Sưng đỏ", "Sốt nhẹ", "Mệt mỏi"],
        schedule={
            "6-35 tháng": "1-2 mũi (lần đầu: 2 mũi cách 1 tháng)",
            "≥3 tuổi": "1 mũi hàng năm",
            "Người lớn": "1 mũi hàng năm"
        },
        notes="Vaxigrip Tetra hoặc Influvac"
    ),
    Vaccine(
        name="HPV",
        name_vn="Vắc xin HPV",
        category="Khuyến nghị",
        target_age="children",
        manufacturer="Mỹ, Bỉ",
        price_range="1.800.000 - 2.500.000 VNĐ/mũi",
        description="Vắc xin phòng ung thư cổ tử cung và các bệnh do HPV",
        indications=["Trẻ từ 9 tuổi", "Nữ giới đến 26 tuổi", "Nam giới đến 21 tuổi"],
        contraindications=["Dị ứng", "Mang thai"],
        side_effects=["Sưng đỏ", "Sốt", "Đau đầu"],
        schedule={
            "9-14 tuổi": "2 mũi (cách 6 tháng)",
            "≥15 tuổi": "3 mũi (0, 2, 6 tháng)"
        },
        notes="Gardasil 9 hoặc Cervarix"
    ),
]

# Vaccines for Adults
VACCINES_ADULTS = [
    Vaccine(
        name="Influenza",
        name_vn="Vắc xin cúm",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Pháp, Hàn Quốc",
        price_range="300.000 - 500.000 VNĐ/mũi",
        description="Vắc xin phòng cúm mùa, tiêm hàng năm",
        indications=["Tất cả người lớn", "Đặc biệt: người già, phụ nữ mang thai, bệnh mạn tính"],
        contraindications=["Dị ứng trứng nặng"],
        side_effects=["Sưng đỏ", "Sốt nhẹ", "Mệt mỏi"],
        schedule={
            "Người lớn": "1 mũi hàng năm (tốt nhất vào tháng 9-11)"
        }
    ),
    Vaccine(
        name="Tdap/Td",
        name_vn="Vắc xin uốn ván - bạch hầu - ho gà",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Pháp, Ấn Độ",
        price_range="200.000 - 400.000 VNĐ/mũi",
        description="Vắc xin nhắc lại phòng uốn ván, bạch hầu, ho gà",
        indications=["Người lớn", "Phụ nữ mang thai (Tdap)"],
        contraindications=["Dị ứng", "Phản ứng nặng trước đó"],
        side_effects=["Sưng đỏ", "Sốt", "Mệt mỏi"],
        schedule={
            "Người lớn": "1 mũi Tdap, sau đó Td mỗi 10 năm",
            "Phụ nữ mang thai": "1 mũi Tdap mỗi lần mang thai (tuần 27-36)"
        }
    ),
    Vaccine(
        name="Hepatitis B",
        name_vn="Vắc xin viêm gan B",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Hàn Quốc, Pháp",
        price_range="150.000 - 300.000 VNĐ/mũi",
        description="Vắc xin phòng viêm gan B cho người chưa tiêm",
        indications=["Người chưa tiêm", "Người có nguy cơ cao"],
        contraindications=["Dị ứng"],
        side_effects=["Sưng đỏ", "Sốt nhẹ"],
        schedule={
            "Người lớn": "3 mũi (0, 1, 6 tháng) hoặc (0, 1, 2, 12 tháng)"
        }
    ),
    Vaccine(
        name="Hepatitis A",
        name_vn="Vắc xin viêm gan A",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Pháp, Bỉ",
        price_range="1.000.000 - 1.300.000 VNĐ/mũi",
        description="Vắc xin phòng viêm gan A",
        indications=["Người chưa mắc", "Người có nguy cơ cao"],
        contraindications=["Dị ứng"],
        side_effects=["Sưng đỏ", "Sốt", "Mệt mỏi"],
        schedule={
            "Người lớn": "2 mũi (cách 6-12 tháng)"
        }
    ),
    Vaccine(
        name="Pneumococcal",
        name_vn="Vắc xin phế cầu khuẩn",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Pháp, Mỹ",
        price_range="1.200.000 - 1.500.000 VNĐ/mũi",
        description="Vắc xin phòng viêm phổi, nhiễm trùng do phế cầu",
        indications=["Người ≥65 tuổi", "Người có bệnh mạn tính", "Người suy giảm miễn dịch"],
        contraindications=["Dị ứng"],
        side_effects=["Sưng đỏ", "Sốt", "Mệt mỏi"],
        schedule={
            "≥65 tuổi": "1 mũi PCV13, sau 1 năm tiêm PPSV23",
            "Người có nguy cơ": "PCV13 trước, sau đó PPSV23"
        },
        notes="PCV13 (Prevenar 13) và PPSV23 (Pneumovax 23)"
    ),
    Vaccine(
        name="MMR",
        name_vn="Vắc xin sởi - quai bị - rubella",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Ấn Độ, Bỉ",
        price_range="200.000 - 400.000 VNĐ/mũi",
        description="Vắc xin phòng sởi, quai bị, rubella cho người chưa tiêm đủ",
        indications=["Người chưa tiêm đủ", "Phụ nữ trước mang thai"],
        contraindications=["Dị ứng trứng", "Mang thai", "Suy giảm miễn dịch"],
        side_effects=["Sốt", "Phát ban nhẹ"],
        schedule={
            "Người lớn": "1-2 mũi (cách ít nhất 1 tháng) nếu chưa tiêm đủ"
        }
    ),
    Vaccine(
        name="Varicella",
        name_vn="Vắc xin thủy đậu",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Bỉ, Hàn Quốc",
        price_range="400.000 - 600.000 VNĐ/mũi",
        description="Vắc xin phòng thủy đậu cho người chưa mắc",
        indications=["Người chưa mắc thủy đậu", "Phụ nữ trước mang thai"],
        contraindications=["Dị ứng", "Mang thai", "Suy giảm miễn dịch"],
        side_effects=["Sưng đỏ", "Sốt", "Phát ban nhẹ"],
        schedule={
            "Người lớn": "2 mũi (cách 4-8 tuần)"
        }
    ),
    Vaccine(
        name="HPV",
        name_vn="Vắc xin HPV",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Mỹ, Bỉ",
        price_range="1.800.000 - 2.500.000 VNĐ/mũi",
        description="Vắc xin phòng ung thư cổ tử cung và các bệnh do HPV",
        indications=["Nữ giới đến 26 tuổi", "Nam giới đến 21 tuổi", "Người có nguy cơ đến 45 tuổi"],
        contraindications=["Dị ứng", "Mang thai"],
        side_effects=["Sưng đỏ", "Sốt", "Đau đầu"],
        schedule={
            "Người lớn": "3 mũi (0, 2, 6 tháng)"
        },
        notes="Gardasil 9 hoặc Cervarix"
    ),
    Vaccine(
        name="Meningococcal",
        name_vn="Vắc xin não mô cầu",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Pháp, Bỉ",
        price_range="600.000 - 900.000 VNĐ/mũi",
        description="Vắc xin phòng viêm màng não do não mô cầu",
        indications=["Người có nguy cơ", "Du lịch đến vùng dịch", "Sinh viên sống ký túc xá"],
        contraindications=["Dị ứng"],
        side_effects=["Sưng đỏ", "Sốt"],
        schedule={
            "Người lớn": "1 mũi, nhắc lại sau 3-5 năm nếu có nguy cơ"
        }
    ),
    Vaccine(
        name="Shingles",
        name_vn="Vắc xin zona",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Mỹ",
        price_range="2.500.000 - 3.500.000 VNĐ/mũi",
        description="Vắc xin phòng zona (herpes zoster)",
        indications=["Người ≥50 tuổi", "Người đã từng mắc thủy đậu"],
        contraindications=["Dị ứng", "Suy giảm miễn dịch nặng"],
        side_effects=["Sưng đỏ", "Sốt", "Mệt mỏi"],
        schedule={
            "≥50 tuổi": "2 mũi (cách 2-6 tháng)"
        },
        notes="Shingrix (ưu tiên) hoặc Zostavax"
    ),
    Vaccine(
        name="Typhoid",
        name_vn="Vắc xin thương hàn",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Ấn Độ, Pháp",
        price_range="300.000 - 500.000 VNĐ/mũi",
        description="Vắc xin phòng thương hàn",
        indications=["Du lịch đến vùng dịch", "Người có nguy cơ"],
        contraindications=["Dị ứng"],
        side_effects=["Sưng đỏ", "Sốt"],
        schedule={
            "Người lớn": "1 mũi, nhắc lại sau 3 năm"
        }
    ),
    Vaccine(
        name="Rabies",
        name_vn="Vắc xin dại",
        category="Khuyến nghị",
        target_age="adults",
        manufacturer="Pháp, Ấn Độ",
        price_range="200.000 - 400.000 VNĐ/mũi",
        description="Vắc xin phòng dại (tiêm phòng hoặc sau phơi nhiễm)",
        indications=["Người có nguy cơ cao", "Sau khi bị cắn"],
        contraindications=["Dị ứng"],
        side_effects=["Sưng đỏ", "Sốt", "Đau đầu"],
        schedule={
            "Tiêm phòng": "3 mũi (0, 7, 21-28 ngày)",
            "Sau phơi nhiễm": "4-5 mũi (0, 3, 7, 14, 28 ngày) + huyết thanh"
        }
    ),
]

# Combined list
ALL_VACCINES = VACCINES_CHILDREN + VACCINES_ADULTS

# Vaccine Schedules by Age Group
VACCINE_SCHEDULES = {
    "Trẻ sơ sinh (0-1 tháng)": {
        "BCG": "1 mũi ngay sau sinh",
        "Hepatitis B": "Mũi 1 trong 24h đầu"
    },
    "Trẻ 2 tháng": {
        "Hepatitis B": "Mũi 2",
        "DTP": "Mũi 1",
        "Polio": "Liều 1",
        "Hib": "Mũi 1",
        "Pneumococcal": "Mũi 1",
        "Rotavirus": "Mũi 1"
    },
    "Trẻ 3 tháng": {
        "DTP": "Mũi 2",
        "Polio": "Liều 2",
        "Hib": "Mũi 2",
        "Pneumococcal": "Mũi 2",
        "Rotavirus": "Mũi 2"
    },
    "Trẻ 4 tháng": {
        "DTP": "Mũi 3",
        "Polio": "Liều 3",
        "Hib": "Mũi 3",
        "Pneumococcal": "Mũi 3",
        "Rotavirus": "Mũi 3 (nếu Rotateq)"
    },
    "Trẻ 6 tháng": {
        "Hepatitis B": "Mũi 3",
        "Influenza": "Mũi 1 (nếu mùa cúm)"
    },
    "Trẻ 9 tháng": {
        "MMR": "Mũi 1 (Sởi đơn)"
    },
    "Trẻ 12 tháng": {
        "Japanese Encephalitis": "Mũi 1",
        "Hepatitis A": "Mũi 1",
        "Varicella": "Mũi 1",
        "Meningococcal": "Mũi 1 (nếu có nguy cơ)"
    },
    "Trẻ 18 tháng": {
        "DTP": "Mũi 4 (nhắc lại)",
        "Polio": "Liều 4 (nhắc lại)",
        "MMR": "Mũi 2",
        "Hib": "Mũi nhắc lại",
        "Pneumococcal": "Mũi nhắc lại"
    },
    "Trẻ 24 tháng": {
        "Japanese Encephalitis": "Mũi 3 (nhắc lại)",
        "Hepatitis A": "Mũi 2"
    },
    "Trẻ 4-6 tuổi": {
        "Varicella": "Mũi 2",
        "DTP": "Mũi 5 (nhắc lại)",
        "MMR": "Mũi 3 (nhắc lại)"
    },
    "Trẻ 9-14 tuổi": {
        "HPV": "2 mũi (cách 6 tháng)"
    },
    "Người lớn": {
        "Influenza": "1 mũi hàng năm",
        "Tdap/Td": "1 mũi Tdap, sau đó Td mỗi 10 năm",
        "Pneumococcal": "PCV13 + PPSV23 (nếu ≥65 tuổi)",
        "Shingles": "2 mũi (nếu ≥50 tuổi)"
    }
}

# Price Reference (in VND)
VACCINE_PRICES = {
    "Miễn phí (TCMR)": ["BCG", "Hepatitis B", "DTP", "Polio", "MMR", "Japanese Encephalitis"],
    "150.000 - 300.000": ["Hepatitis B (dịch vụ)", "Rabies"],
    "200.000 - 400.000": ["DTP (dịch vụ)", "MMR (dịch vụ)", "Tdap/Td"],
    "300.000 - 500.000": ["Influenza", "Typhoid"],
    "400.000 - 600.000": ["Hib", "Varicella"],
    "600.000 - 900.000": ["Meningococcal"],
    "700.000 - 1.000.000": ["Rotavirus"],
    "1.000.000 - 1.300.000": ["Hepatitis A"],
    "1.200.000 - 1.500.000": ["Pneumococcal"],
    "1.800.000 - 2.500.000": ["HPV"],
    "2.500.000 - 3.500.000": ["Shingles"]
}


def get_vaccine_by_name(name: str) -> Optional[Vaccine]:
    """Get vaccine by name (English or Vietnamese)"""
    for vaccine in ALL_VACCINES:
        if vaccine.name.lower() == name.lower() or vaccine.name_vn.lower() == name.lower():
            return vaccine
    return None


def get_vaccines_by_category(category: str, target_age: str = "both") -> List[Vaccine]:
    """Get vaccines by category and target age"""
    result = []
    for vaccine in ALL_VACCINES:
        if vaccine.category == category:
            if target_age == "both" or vaccine.target_age == target_age or vaccine.target_age == "both":
                result.append(vaccine)
    return result


def get_schedule_by_age_group(age_group: str) -> Dict[str, str]:
    """Get vaccine schedule for specific age group"""
    return VACCINE_SCHEDULES.get(age_group, {})

