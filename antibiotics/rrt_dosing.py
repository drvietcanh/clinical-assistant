"""
Renal Replacement Therapy dosing guidance (CRRT/ECMO) - Phase 1

Mục tiêu:
- Cung cấp guidance nhanh cho CRRT (CVVH/CVVHD/CVVHDF) và ECMO.
- Dùng để bổ sung vào dosing calculator UI (không thay thế judgment lâm sàng).

Phạm vi Phase 1:
- Vancomycin, Piperacillin-Tazobactam, Meropenem, Ceftazidime, Gentamicin/Amikacin.

Lưu ý:
- Đây là khuyến cáo khung (template). Cần hiệu chỉnh theo effluent rate, mức độ nặng, MIC,
  và mục tiêu PK/PD (T>MIC, AUC/MIC).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Any


@dataclass(frozen=True)
class RRTGuidance:
    crtt_summary: str
    ecmo_summary: str
    monitoring: str
    caveats: str

    def as_dict(self) -> Dict[str, str]:
        return {
            "CRRT": self.crtt_summary,
            "ECMO": self.ecmo_summary,
            "Theo dõi": self.monitoring,
            "Lưu ý": self.caveats,
        }


RRT_DOSING_GUIDE: Dict[str, RRTGuidance] = {
    "Vancomycin": RRTGuidance(
        crtt_summary=(
            "Ưu tiên TDM/AUC. Gợi ý: loading 20–25 mg/kg (theo ABW), "
            "duy trì 10–15 mg/kg mỗi 24h (hoặc chia q12h) tùy effluent và mục tiêu AUC."
        ),
        ecmo_summary=(
            "ECMO có thể tăng Vd. Gợi ý: cân nhắc loading 25–30 mg/kg, "
            "theo dõi nồng độ sớm (trough/AUC) để chỉnh liều."
        ),
        monitoring="AUC24/MIC mục tiêu 400–600 (nếu có); hoặc trough theo guideline; creatinine hàng ngày.",
        caveats="CRRT modality/effluent rate thay đổi lớn. Luôn chỉnh theo nồng độ và đáp ứng lâm sàng.",
    ),
    "Piperacillin-Tazobactam": RRTGuidance(
        crtt_summary=(
            "Ưu tiên extended infusion. Gợi ý: 4.5g q8h (truyền 3–4h) "
            "hoặc 4.5g q6–8h tùy effluent và mức độ nặng."
        ),
        ecmo_summary="ECMO: cân nhắc liều cao/extended infusion trong nhiễm nặng; theo dõi đáp ứng.",
        monitoring="Theo dõi lâm sàng, cấy/KSĐ; cân nhắc beta-lactam TDM nếu có.",
        caveats="Không có một liều chung; phụ thuộc effluent, MIC, ổ nhiễm và ARC đồng thời.",
    ),
    "Meropenem": RRTGuidance(
        crtt_summary=(
            "Ưu tiên extended infusion. Gợi ý: 1g q8h (truyền 3h) "
            "hoặc 2g q8h (nhiễm rất nặng/Pseudomonas) tùy effluent."
        ),
        ecmo_summary="ECMO: cân nhắc 1–2g q8h (truyền kéo dài) trong nhiễm nặng; theo dõi đáp ứng.",
        monitoring="Theo dõi lâm sàng; cân nhắc TDM beta-lactam nếu có; lưu ý độc tính thần kinh khi tích lũy.",
        caveats="Nguy cơ underdosing cao nếu effluent lớn; ưu tiên tối ưu T>MIC bằng truyền kéo dài.",
    ),
    "Ceftazidime": RRTGuidance(
        crtt_summary="Gợi ý: 2g q8–12h (truyền kéo dài) tùy effluent và mức độ nặng.",
        ecmo_summary="ECMO: cân nhắc liều cao hơn trong nhiễm nặng; ưu tiên truyền kéo dài.",
        monitoring="Theo dõi lâm sàng; TDM beta-lactam nếu có.",
        caveats="Chỉnh theo MIC/KSĐ; độc tính thần kinh tăng khi tích lũy.",
    ),
    "Gentamicin": RRTGuidance(
        crtt_summary="Ưu tiên TDM. Gợi ý liều theo cân nặng, dùng liều cách quãng và chỉnh theo peak/trough.",
        ecmo_summary="ECMO: Vd có thể tăng; TDM bắt buộc để tránh độc thận/độc tai.",
        monitoring="TDM (peak/trough hoặc AUC), creatinine, triệu chứng độc tai.",
        caveats="Aminoglycoside trong CRRT/ECMO biến thiên lớn; không khuyến cáo nếu có lựa chọn an toàn hơn.",
    ),
    "Amikacin": RRTGuidance(
        crtt_summary="Ưu tiên TDM. Gợi ý liều tải 15–25 mg/kg, sau đó chỉnh theo nồng độ và effluent.",
        ecmo_summary="ECMO: Vd tăng; cân nhắc liều tải cao hơn, TDM sớm.",
        monitoring="TDM (peak/trough), creatinine, độc tai.",
        caveats="Biến thiên lớn; chỉ nên dùng khi cần và có khả năng TDM.",
    ),
}


def get_rrt_guidance(drug_name: str) -> Optional[RRTGuidance]:
    if not drug_name:
        return None
    return RRT_DOSING_GUIDE.get(drug_name)

