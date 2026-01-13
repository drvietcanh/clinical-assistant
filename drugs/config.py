"""
Drugs Module Configuration
--------------------------

High‑level configuration and metadata for the Drug Database module.

This file plays a similar role to `scores/config.py`:
- provides a single source of truth for available tools in the Drugs domain
- exposes lightweight helper functions for the UI layer (pages/07_💊_Drug_Database.py)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class DrugTool:
    """Metadata for a top‑level drug tool in the UI."""

    id: str          # internal ID, e.g. "database", "interactions"
    name: str        # display name
    icon: str        # emoji icon
    description: str


# Top‑level tools shown in the Drug Database page.
# NOTE: Keep IDs stable – they may be stored in session_state or analytics later.
DRUG_TOOLS: Dict[str, DrugTool] = {
    "database": DrugTool(
        id="database",
        name="Tra cứu thuốc (Tất cả)",
        icon="💊",
        description="Tra cứu toàn bộ thuốc: tên, nhóm, liều dùng, dược động, lưu ý lâm sàng.",
    ),
    "renal_dosing": DrugTool(
        id="renal_dosing",
        name="Tính liều theo eGFR/CrCl (Kháng sinh)",
        icon="🧮",
        description="Tính liều kháng sinh theo chức năng thận (CrCl/eGFR) với gợi ý chỉnh liều.",
    ),
    "visual_comparison": DrugTool(
        id="visual_comparison",
        name="So sánh thuốc trực quan",
        icon="📊",
        description="So sánh nhanh nhiều thuốc trong cùng nhóm (liều, tần suất, lưu ý).",
    ),
    "dosing_schedule": DrugTool(
        id="dosing_schedule",
        name="Tạo lịch trình liều dùng",
        icon="📅",
        description="Sinh lịch liều dùng chi tiết cho một hoặc nhiều thuốc.",
    ),
    "iv_compatibility": DrugTool(
        id="iv_compatibility",
        name="Kiểm tra tương thích IV",
        icon="💉",
        description="Kiểm tra tương thích truyền tĩnh mạch giữa các thuốc/ dịch truyền.",
    ),
    "interactions": DrugTool(
        id="interactions",
        name="Kiểm tra tương tác thuốc",
        icon="🔍",
        description="Phát hiện và phân loại tương tác thuốc (mức độ, khuyến cáo lâm sàng).",
    ),
}


def get_all_drug_tools() -> List[DrugTool]:
    """Return list of all configured drug tools."""

    # Preserve insertion order for predictable UI
    return list(DRUG_TOOLS.values())


def get_drug_tool(tool_id: str) -> DrugTool | None:
    """Get a single tool by internal ID."""

    return DRUG_TOOLS.get(tool_id)


__all__ = [
    "DrugTool",
    "DRUG_TOOLS",
    "get_all_drug_tools",
    "get_drug_tool",
]

