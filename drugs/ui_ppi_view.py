"""
UI components for Proton Pump Inhibitors (PPIs)
Uses PROTON_PUMP_INHIBITOR_PPIS_DRUGS to render mobile-friendly cards for doctors
"""

import streamlit as st

from drugs.drug_modules.gastrointestinal.proton_pump_inhibitor_ppis import (
    PROTON_PUMP_INHIBITOR_PPIS_DRUGS,
)


def _normalize_evidence_level(level: str) -> str:
    """Normalize raw evidence_level string to High / Moderate / Limited."""
    if not level:
        return "Unknown"
    lower = level.lower()
    if "high" in lower:
        return "High"
    if "moderate" in lower:
        return "Moderate"
    if "low" in lower or "limited" in lower:
        return "Limited"
    return "Unknown"


def _evidence_badge(level: str) -> str:
    """Return small HTML badge for evidence level."""
    normalized = _normalize_evidence_level(level)
    color_map = {
        "High": "#16A34A",      # green
        "Moderate": "#F59E0B",  # amber
        "Limited": "#F97316",   # orange
        "Unknown": "#6B7280",   # gray
    }
    color = color_map.get(normalized, "#6B7280")
    return (
        f"<span style='background:{color}1A;color:{color};"
        "padding:2px 8px;border-radius:999px;font-size:0.75rem;"
        "font-weight:600;white-space:nowrap;'>"
        f"Evidence: {normalized}"
        "</span>"
    )


def render_ppi_quick_section() -> None:
    """
    Render a compact PPIs section for the drug database page.

    - Shows 3–4 key PPIs as cards
    - Optimized for mobile and desktop
    - Uses evidence_level badge for quick appraisal
    """
    if not PROTON_PUMP_INHIBITOR_PPIS_DRUGS:
        return

    with st.expander("💊 PPIs – Ức chế bơm proton (tóm tắt nhanh)", expanded=False):
        st.caption(
            "Tóm tắt một số thuốc PPI thường dùng (liều cơ bản, chỉ định chính, mức độ bằng chứng). "
            "Nhấn vào tên thuốc trong database đầy đủ để xem chi tiết."
        )

        # Limit number of cards to avoid noise
        max_cards = 4
        items = list(PROTON_PUMP_INHIBITOR_PPIS_DRUGS.items())[:max_cards]

        num_cols = min(2, len(items))
        cols = st.columns(num_cols) if items else []

        for idx, (name, data) in enumerate(items):
            with cols[idx % num_cols]:
                vi_name = data.get("vietnamese_name", "")
                indications = data.get("indications", [])
                dosage = data.get("dosage", {})

                # Build short indications string
                inds_short = " • ".join(indications[:3]) if indications else ""

                # Try to pick a representative adult dose field
                dose_short = ""
                for key in ("adult_po", "adult_standard", "adult_ulcer", "adult_gerd"):
                    if key in dosage:
                        dose_short = dosage[key]
                        break

                evidence = (
                    data.get("references", {}).get("evidence_level", "")
                )
                badge_html = _evidence_badge(evidence) if evidence else ""

                st.markdown(
                    f"""
<div class="ppi-quick-card" style="
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px;
  box-shadow: 0 2px 4px var(--shadow);
  margin-bottom: 0.75rem;
">
  <div style="font-weight:600;font-size:0.95rem;margin-bottom:2px;">💊 {name}</div>
  <div style="font-size:0.8rem;color:var(--text-secondary);margin-bottom:4px;">{vi_name}</div>
  {f'<div style="font-size:0.8rem;color:var(--text-secondary);margin-bottom:4px;">{inds_short}</div>' if inds_short else ''}
  {f'<div style="font-size:0.8rem;margin-bottom:4px;"><b>Liều (gợi ý):</b> {dose_short}</div>' if dose_short else ''}
  {badge_html}
</div>
""",
                    unsafe_allow_html=True,
                )



