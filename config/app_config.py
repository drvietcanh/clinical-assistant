"""
Unified Application Configuration
Single source of truth for all app configuration
"""

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
    
    "pages": {
        "scores": ModuleInfo(
            id="scores",
            title="Thang Điểm Lâm Sàng",
            icon="📊",
            page_path="pages/01_📊_Scores.py",
            description="110 calculators, 19 specialties",
            color="linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",
            border="#1976d2"
        ),
        "antibiotics": ModuleInfo(
            id="antibiotics",
            title="Kháng Sinh",
            icon="💊",
            page_path="pages/02_💊_Antibiotics.py",
            description="Tra cứu & so sánh kháng sinh",
            color="linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
            border="#4caf50"
        ),
        "ventilator": ModuleInfo(
            id="ventilator",
            title="Thở Máy",
            icon="🫁",
            page_path="pages/03_🫁_Ventilator.py",
            description="ARDSNet, PEEP/FiO₂",
            color="linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%)",
            border="#e91e63"
        ),
        "protocols": ModuleInfo(
            id="protocols",
            title="Phác Đồ Điều Trị",
            icon="📋",
            page_path="pages/04_📋_Protocols.py",
            description="5 protocols, Evidence-based",
            color="linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%)",
            border="#9c27b0"
        ),
        "labs": ModuleInfo(
            id="labs",
            title="Labs & Calculators",
            icon="🔬",
            page_path="pages/05_🔬_Labs_and_Calculators.py",
            description="9 panels + Calculators, Integrated workflow",
            color="linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
            border="#ff9800"
        ),
        "diagnosis": ModuleInfo(
            id="diagnosis",
            title="Chẩn Đoán Phân Biệt",
            icon="🩺",
            page_path="pages/06_🩺_Diagnosis.py",
            description="DDx Generator, Clinical decision support",
            color="linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%)",
            border="#f44336"
        ),
        "drug_database": ModuleInfo(
            id="drug_database",
            title="Tra Cứu Thuốc",
            icon="💊",
            page_path="pages/07_💊_Drug_Database.py",
            description="Database thuốc, tính liều theo thận, tương tác, IV",
            color="linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%)",
            border="#0288d1"
        ),
        "tdm": ModuleInfo(
            id="tdm",
            title="TDM - Theo Dõi Nồng Độ",
            icon="📊",
            page_path="pages/08_📊_TDM.py",
            description="Tính toán và theo dõi nồng độ thuốc (5 thuốc)",
            color="linear-gradient(135deg, #f3e5f5 0%, #ce93d8 100%)",
            border="#7b1fa2"
        ),
        "critical_care": ModuleInfo(
            id="critical_care",
            title="Hồi Sức",
            icon="🫁",
            page_path="pages/09_🫁_Critical_Care.py",
            description="Fluids, Vasopressors, Transfusion, Sedation",
            color="linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
            border="#ff6f00"
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

