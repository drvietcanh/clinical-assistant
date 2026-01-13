"""
Diagnosis Module Configuration
------------------------------

Configuration and metadata for the Diagnosis / Differential Diagnosis module.

This provides a small, Scores‑style config layer so that:
- the main page (`pages/06_🩺_Diagnosis.py`) can query available tabs/tools
- other modules can link to diagnosis features in a stable way
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class DiagnosisTab:
    id: str
    name: str
    icon: str
    description: str


DIAGNOSIS_TABS: Dict[str, DiagnosisTab] = {
    "ddx": DiagnosisTab(
        id="ddx",
        name="Differential Diagnosis",
        icon="🩺",
        description="Công cụ gợi ý chẩn đoán phân biệt dựa trên triệu chứng và hệ cơ quan.",
    ),
    "disease_encyclopedia": DiagnosisTab(
        id="disease_encyclopedia",
        name="Disease Encyclopedia",
        icon="📖",
        description="Bách khoa bệnh lý: định nghĩa, nguyên nhân, triệu chứng, chẩn đoán, điều trị.",
    ),
    "icd10": DiagnosisTab(
        id="icd10",
        name="ICD‑10 Lookup",
        icon="🏷️",
        description="Tra cứu mã ICD‑10 theo tên bệnh, code hoặc chuyên khoa.",
    ),
    "in_depth_articles": DiagnosisTab(
        id="in_depth_articles",
        name="In‑Depth Articles",
        icon="📚",
        description="Bài viết chuyên sâu phân tích guideline và chiến lược điều trị.",
    ),
    "patient_education": DiagnosisTab(
        id="patient_education",
        name="Patient Education",
        icon="👥",
        description="Tài liệu giáo dục bệnh nhân với ngôn ngữ đơn giản, dễ hiểu.",
    ),
}


def get_all_diagnosis_tabs() -> List[DiagnosisTab]:
    return list(DIAGNOSIS_TABS.values())


def get_diagnosis_tab(tab_id: str) -> DiagnosisTab | None:
    return DIAGNOSIS_TABS.get(tab_id)


__all__ = [
    "DiagnosisTab",
    "DIAGNOSIS_TABS",
    "get_all_diagnosis_tabs",
    "get_diagnosis_tab",
]

