"""
Unified Application Configuration
Single source of truth for all app configuration
"""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class CalculatorInfo:
    """Calculator information"""
    id: str
    name: str
    category: str
    icon: str
    page: str
    specialty: Optional[str] = None
    status: str = "✅"
    description: Optional[str] = None


@dataclass
class ModuleInfo:
    """Module/page information"""
    id: str
    title: str
    icon: str
    page_path: str
    description: str
    color: str
    border: str


# Unified configuration
APP_CONFIG = {
    "version": "2.3.0",
    "last_updated": "2025-01-30",
    
    # Google Analytics Configuration
    # Có thể set qua environment variable: GOOGLE_ANALYTICS_ID
    # Hoặc thay đổi giá trị mặc định bên dưới
    "google_analytics_id": os.getenv("GOOGLE_ANALYTICS_ID", "G-JRPOGQLG70"),
    
    "pages": {
        "scores": ModuleInfo(
            id="scores",
            title="Calculators & Thang điểm",
            icon="📊",
            page_path="pages/01_📊_Scores.py",
            description="110 calculators, 19 specialties",
            color="linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",
            border="#1976d2"
        ),
        "antibiotics": ModuleInfo(
            id="antibiotics",
            title="Kháng sinh (chuyên sâu)",
            icon="💊",
            page_path="pages/02_💊_Antibiotics.py",
            description="So sánh & phác đồ điều trị kháng sinh",
            color="linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
            border="#4caf50"
        ),
        "ventilator": ModuleInfo(
            id="ventilator",
            title="Thở máy",
            icon="🫁",
            page_path="pages/03_🫁_Ventilator.py",
            description="Đã tích hợp vào Critical Care - Redirect",
            color="linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%)",
            border="#e91e63"
        ),
        "protocols": ModuleInfo(
            id="protocols",
            title="Phác đồ điều trị",
            icon="📋",
            page_path="pages/04_📋_Protocols.py",
            description="5 protocols, Evidence-based",
            color="linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%)",
            border="#9c27b0"
        ),
        "labs": ModuleInfo(
            id="labs",
            title="Xét nghiệm & Calculators",
            icon="🔬",
            page_path="pages/05_🔬_Labs_and_Calculators.py",
            description="9 panels + Calculators, Integrated workflow",
            color="linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
            border="#ff9800"
        ),
        "diagnosis": ModuleInfo(
            id="diagnosis",
            title="Chẩn đoán phân biệt",
            icon="🩺",
            page_path="pages/06_🩺_Diagnosis.py",
            description="DDx Generator, Clinical decision support",
            color="linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%)",
            border="#f44336"
        ),
        "drug_database": ModuleInfo(
            id="drug_database",
            title="Cơ sở dữ liệu thuốc",
            icon="💊",
            page_path="pages/07_💊_Drug_Database.py",
            description="Database thuốc, tính liều theo thận, tương tác, IV",
            color="linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%)",
            border="#0288d1"
        ),
        "tdm": ModuleInfo(
            id="tdm",
            title="TDM - Theo dõi nồng độ",
            icon="📊",
            page_path="pages/08_📊_TDM.py",
            description="Tính toán và theo dõi nồng độ thuốc (5 thuốc)",
            color="linear-gradient(135deg, #f3e5f5 0%, #ce93d8 100%)",
            border="#7b1fa2"
        ),
        "critical_care": ModuleInfo(
            id="critical_care",
            title="Hồi sức",
            icon="🫁",
            page_path="pages/09_🫁_Critical_Care.py",
            description="Ventilator, Fluids, Vasopressors, Transfusion, Sedation",
            color="linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
            border="#ff6f00"
        ),
        "phase2_features": ModuleInfo(
            id="phase2_features",
            title="Hỗ trợ quyết định",
            icon="🧭",
            page_path="pages/10_🧭_Decision_Support.py",
            description="Flowcharts, thai kỳ/cho bú, liều Nhi khoa",
            color="linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
            border="#4caf50"
        ),
        "vaccination": ModuleInfo(
            id="vaccination",
            title="Tiêm chủng và Vắc xin",
            icon="💉",
            page_path="pages/11_💉_Vaccination.py",
            description="Lịch tiêm, giá cả, phác đồ tiêm các loại vắc xin tại Việt Nam",
            color="linear-gradient(135deg, #fff9c4 0%, #fff59d 100%)",
            border="#fbc02d"
        ),
        "in_depth_articles": ModuleInfo(
            id="in_depth_articles",
            title="Bài viết chuyên sâu",
            icon="📚",
            page_path="pages/12_📚_In_Depth_Articles.py",
            description="Bài viết chuyên sâu theo guideline, phân tích điều trị",
            color="linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",
            border="#1e88e5"
        ),
        "icd10_lookup": ModuleInfo(
            id="icd10_lookup",
            title="Tra cứu mã ICD-10",
            icon="🏷️",
            page_path="pages/13_🏷️_ICD10_Lookup.py",
            description="Tra cứu mã ICD-10 theo tên bệnh, mã code, hoặc chuyên khoa",
            color="linear-gradient(135deg, #f1f8e9 0%, #dcedc8 100%)",
            border="#689f38"
        ),
        "medical_news": ModuleInfo(
            id="medical_news",
            title="Tin tức y khoa",
            icon="📰",
            page_path="pages/14_📰_Medical_News.py",
            description="Tin tức y khoa mới nhất từ Medscape, Healthline, PubMed, NEJM",
            color="linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
            border="#ff9800"
        ),
        "guidelines_tracker": ModuleInfo(
            id="guidelines_tracker",
            title="Theo dõi Guidelines",
            icon="📋",
            page_path="pages/15_📋_Guidelines_Tracker.py",
            description="Theo dõi và cập nhật guidelines từ AHA/ACC, ESC, IDSA, KDIGO, GOLD, GINA",
            color="linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%)",
            border="#9c27b0"
        ),
        "disease_encyclopedia": ModuleInfo(
            id="disease_encyclopedia",
            title="Bách khoa Bệnh lý",
            icon="📖",
            page_path="pages/16_📖_Disease_Encyclopedia.py",
            description="Thông tin toàn diện về các bệnh lý phổ biến: định nghĩa, nguyên nhân, triệu chứng, chẩn đoán, điều trị",
            color="linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
            border="#4caf50"
        ),
        "symptom_checker": ModuleInfo(
            id="symptom_checker",
            title="Kiểm tra Triệu chứng",
            icon="🩺",
            page_path="pages/17_🩺_Symptom_Checker.py",
            description="Phân tích triệu chứng và gợi ý chẩn đoán có thể với xác suất, đánh giá mức độ nghiêm trọng",
            color="linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%)",
            border="#f44336"
        ),
    },
    
    "navigation": {
        "default_page": "scores",
        "show_search": True,
        "show_favorites": True,
        "show_recently_used": True,
    },
}


def get_all_calculators() -> Dict:
    """
    Get all calculators from config/calculators.py
    (Maintains backward compatibility)
    """
    from config.calculators import ALL_CALCULATORS
    return ALL_CALCULATORS


def get_module_info(module_id: str) -> Optional[ModuleInfo]:
    """Get module information by ID"""
    return APP_CONFIG["pages"].get(module_id)


def get_all_modules() -> Dict[str, ModuleInfo]:
    """Get all module information"""
    return APP_CONFIG["pages"]


def get_module_list_for_navigation() -> List[Dict]:
    """
    Get modules formatted for navigation display
    
    Returns:
        List of dicts with module info for UI display
    """
    modules = []
    for module_id, module_info in APP_CONFIG["pages"].items():
        modules.append({
            "id": module_id,
            "icon": module_info.icon,
            "title": module_info.title,
            "desc": module_info.description,
            "color": module_info.color,
            "border": module_info.border,
            "page": module_info.page_path,
            "key": f"quick_{module_id}"
        })
    return modules


# Export main config
__all__ = [
    'APP_CONFIG',
    'CalculatorInfo',
    'ModuleInfo',
    'get_all_calculators',
    'get_module_info',
    'get_all_modules',
    'get_module_list_for_navigation',
]

