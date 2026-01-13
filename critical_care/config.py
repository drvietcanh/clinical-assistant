"""
Critical Care Module Configuration
----------------------------------

High‑level configuration and metadata for the Critical Care module.

This is the analogue of `scores/config.py` and `drugs/config.py`:
- defines the main tools available on the Critical Care page
- gives the UI layer a single source of truth for labels/icons/descriptions
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class CriticalCareTool:
    """Metadata for a top‑level critical care tool in the UI."""

    id: str
    name: str
    icon: str
    description: str


CRITICAL_CARE_TOOLS: Dict[str, CriticalCareTool] = {
    "dashboard": CriticalCareTool(
        id="dashboard",
        name="Dashboard",
        icon="🏠",
        description="Tổng quan hồi sức: tiles truy cập nhanh tới các công cụ quan trọng.",
    ),
    "scoring": CriticalCareTool(
        id="scoring",
        name="Scoring Systems",
        icon="📊",
        description="Các thang điểm ICU (RASS, CAM‑ICU, AKI staging, …).",
    ),
    "ventilator": CriticalCareTool(
        id="ventilator",
        name="Ventilator Management",
        icon="🫁",
        description="Quản lý máy thở: IBW, tidal volume, PEEP, ARDSNet, weaning…",
    ),
    "ards": CriticalCareTool(
        id="ards",
        name="ARDS Protocols",
        icon="🫁",
        description="Phác đồ ARDS: ARDSNet, PEEP/FiO2 table, prone positioning…",
    ),
    "sepsis": CriticalCareTool(
        id="sepsis",
        name="Sepsis Protocols",
        icon="🦠",
        description="Nhận diện sepsis, 1‑hour bundle, kháng sinh, hồi sức dịch, lactate.",
    ),
    "shock": CriticalCareTool(
        id="shock",
        name="Shock Management",
        icon="💉",
        description="Quản lý shock: vasopressors, shock index, fluid responsiveness.",
    ),
    "rrt": CriticalCareTool(
        id="rrt",
        name="RRT Calculator",
        icon="🩺",
        description="CRRT, IHD, SLED, chống đông trong lọc máu.",
    ),
    "scenarios": CriticalCareTool(
        id="scenarios",
        name="Clinical Scenarios",
        icon="🎯",
        description="Tình huống lâm sàng tổng hợp cho đào tạo và kiểm tra kiến thức.",
    ),
    "fluids": CriticalCareTool(
        id="fluids",
        name="Fluid Therapy",
        icon="💧",
        description="Tính nhu cầu dịch, maintenance, bolus, cân bằng dịch.",
    ),
    "vasopressors": CriticalCareTool(
        id="vasopressors",
        name="Vasopressors",
        icon="💉",
        description="Liều, pha, titration norepinephrine, vasopressin, epinephrine…",
    ),
    "transfusion": CriticalCareTool(
        id="transfusion",
        name="Transfusion",
        icon="🩸",
        description="PRBC, PLT, FFP, massive transfusion protocol.",
    ),
    "sedation": CriticalCareTool(
        id="sedation",
        name="Sedation & Analgesia",
        icon="💤",
        description="Chiến lược an thần, giảm đau, RASS, CAM‑ICU integration.",
    ),
    "dirc": CriticalCareTool(
        id="dirc",
        name="Drug Infusion (DIRC)",
        icon="💉",
        description="Tính liều truyền tĩnh mạch liên tục (Drug Infusion Rate Calculator).",
    ),
}


def get_all_critical_care_tools() -> List[CriticalCareTool]:
    """Return list of all configured Critical Care tools."""

    return list(CRITICAL_CARE_TOOLS.values())


def get_critical_care_tool(tool_id: str) -> CriticalCareTool | None:
    """Get a single tool by internal ID."""

    return CRITICAL_CARE_TOOLS.get(tool_id)


__all__ = [
    "CriticalCareTool",
    "CRITICAL_CARE_TOOLS",
    "get_all_critical_care_tools",
    "get_critical_care_tool",
]

