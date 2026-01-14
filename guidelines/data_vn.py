"""
Vietnam Guidelines Database (Bộ Y tế / Hội chuyên khoa VN)

This module is intentionally small and easy to extend.
Add more entries over time as you curate official Vietnamese guidance.
"""

from typing import List

from .data import Guideline


# Minimal starter set (placeholders) — extend with official links and richer summaries
GUIDELINES_VN: List[Guideline] = [
    Guideline(
        id="moh_vn_hypertension",
        title="Vietnam Ministry of Health - Hypertension Guideline",
        title_vn="Bộ Y tế - Hướng dẫn chẩn đoán và điều trị Tăng huyết áp",
        organization="Bộ Y tế VN",
        year=2020,
        category="Cardiology",
        version="2020",
        last_updated="2020-01-01",
        url="",
        description="Khung dữ liệu ban đầu. Bổ sung đường dẫn chính thức và tóm tắt theo tài liệu Bộ Y tế.",
        evidence_level="moderate",
        is_high_impact=False,
    ),
    Guideline(
        id="moh_vn_diabetes",
        title="Vietnam Ministry of Health - Diabetes Guideline",
        title_vn="Bộ Y tế - Hướng dẫn chẩn đoán và điều trị Đái tháo đường",
        organization="Bộ Y tế VN",
        year=2020,
        category="Endocrinology",
        version="2020",
        last_updated="2020-01-01",
        url="",
        description="Khung dữ liệu ban đầu. Bổ sung đường dẫn chính thức và tóm tắt theo tài liệu Bộ Y tế.",
        evidence_level="moderate",
        is_high_impact=False,
    ),
    Guideline(
        id="moh_vn_asthma",
        title="Vietnam Ministry of Health - Asthma Guideline",
        title_vn="Bộ Y tế - Hướng dẫn chẩn đoán và điều trị Hen phế quản",
        organization="Bộ Y tế VN",
        year=2020,
        category="Respiratory",
        version="2020",
        last_updated="2020-01-01",
        url="",
        description="Khung dữ liệu ban đầu. Bổ sung đường dẫn chính thức và tóm tắt theo tài liệu Bộ Y tế.",
        evidence_level="low",
        is_high_impact=False,
    ),
]

