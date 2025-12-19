"""
UI components for Statins (HMG-CoA Reductase Inhibitors)
Quick view cards for cholesterol-lowering medications
"""

import streamlit as st

# Import statins
try:
    from drugs.drug_modules.cardiovascular.statins import STATINS
except ImportError:
    STATINS = {}


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
        "Moderate": "#F59E0B",   # amber
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


def _render_drug_group_cards(
    drugs_dict: dict,
    group_name: str,
    group_icon: str,
    max_cards: int = 4
) -> None:
    """Generic function to render drug group cards."""
    if not drugs_dict:
        return
    
    items = list(drugs_dict.items())[:max_cards]
    if not items:
        return
    
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
            for key in ("adult_standard", "adult_high_intensity", "adult_po", "adult_usual"):
                if key in dosage:
                    dose_short = dosage[key]
                    break
            
            # Get evidence level if available
            evidence = data.get("references", {}).get("evidence_level", "")
            badge_html = _evidence_badge(evidence) if evidence else ""
            
            # Get pregnancy category for warning
            pregnancy = data.get("pregnancy", "")
            preg_warning = ""
            if pregnancy in ("X", "D"):
                preg_warning = '<div style="font-size:0.7rem;color:#E74C3C;margin-top:4px;">⚠️ Chống chỉ định thai kỳ</div>'
            
            # Check for black box warnings about rhabdomyolysis
            black_box = data.get("black_box_warnings", "")
            rhabdo_warning = ""
            if black_box and "tiêu cơ" in black_box.lower():
                rhabdo_warning = '<div style="font-size:0.7rem;color:#E74C3C;margin-top:4px;">⚠️ Nguy cơ tiêu cơ vân</div>'
            
            st.markdown(
                f"""
<div class="statin-drug-card" style="
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px;
  box-shadow: 0 2px 4px var(--shadow);
  margin-bottom: 0.75rem;
">
  <div style="font-weight:600;font-size:0.95rem;margin-bottom:2px;">{group_icon} {name}</div>
  <div style="font-size:0.8rem;color:var(--text-secondary);margin-bottom:4px;">{vi_name}</div>
  {f'<div style="font-size:0.8rem;color:var(--text-secondary);margin-bottom:4px;">{inds_short}</div>' if inds_short else ''}
  {f'<div style="font-size:0.8rem;margin-bottom:4px;"><b>Liều (gợi ý):</b> {dose_short}</div>' if dose_short else ''}
  {preg_warning}
  {rhabdo_warning}
  {badge_html}
</div>
""",
                unsafe_allow_html=True,
            )


def render_statins_quick_section() -> None:
    """Render Statins quick view section."""
    if not STATINS:
        return
    
    with st.expander("💊 Statins – Hạ mỡ máu (tóm tắt nhanh)", expanded=False):
        st.caption(
            "Thuốc hạ cholesterol, dự phòng biến cố tim mạch. "
            "Lưu ý: Chống chỉ định trong thai kỳ (category X). "
            "Nguy cơ tiêu cơ vân, đặc biệt khi dùng với macrolide, azole antifungal, cyclosporine. "
            "Theo dõi CK nếu đau cơ, men gan định kỳ."
        )
        _render_drug_group_cards(STATINS, "Statins", "💊", max_cards=4)


def render_statins_quick_sections() -> None:
    """Render all statins quick view sections (wrapper for consistency)."""
    render_statins_quick_section()

