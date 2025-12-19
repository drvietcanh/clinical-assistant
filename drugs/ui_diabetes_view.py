"""
UI components for Diabetes Drugs
Quick view cards for Metformin, SGLT2 inhibitors, and other diabetes medications
"""

import streamlit as st

# Import diabetes drug groups
try:
    from drugs.drug_modules.diabetes.biguanides import BIGUANIDES_DRUGS
except ImportError:
    BIGUANIDES_DRUGS = {}

try:
    from drugs.drug_modules.diabetes.sglt2_inhibitors import SGLT2_INHIBITORS_DRUGS
except ImportError:
    SGLT2_INHIBITORS_DRUGS = {}


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
    max_cards: int = 3,
    special_warning: str = ""
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
            for key in ("adult_usual", "adult_type2_dm", "adult_po", "adult_standard", "adult_start"):
                if key in dosage:
                    dose_short = dosage[key]
                    break
            
            # Get evidence level if available
            evidence = data.get("references", {}).get("evidence_level", "")
            badge_html = _evidence_badge(evidence) if evidence else ""
            
            # Get special warnings
            warning_html = ""
            if special_warning:
                warning_html = f'<div style="font-size:0.7rem;color:#F59E0B;margin-top:4px;">⚠️ {special_warning}</div>'
            
            # Check for black box warnings
            black_box = data.get("black_box_warnings", "")
            if black_box and "lactic" in black_box.lower():
                warning_html = '<div style="font-size:0.7rem;color:#E74C3C;margin-top:4px;">⚠️ Nguy cơ nhiễm toan lactic</div>'
            
            st.markdown(
                f"""
<div class="diabetes-drug-card" style="
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
  {warning_html}
  {badge_html}
</div>
""",
                unsafe_allow_html=True,
            )


def render_metformin_quick_section() -> None:
    """Render Metformin (Biguanides) quick view section."""
    if not BIGUANIDES_DRUGS:
        return
    
    with st.expander("🍬 Metformin – Biguanide (tóm tắt nhanh)", expanded=False):
        st.caption(
            "Thuốc đầu tay cho đái tháo đường type 2. "
            "Lưu ý: Chống chỉ định khi CrCl <30 hoặc eGFR <30. "
            "Ngừng 48h trước và sau khi dùng thuốc cản quang. Nguy cơ nhiễm toan lactic."
        )
        _render_drug_group_cards(
            BIGUANIDES_DRUGS, 
            "Metformin", 
            "🍬", 
            max_cards=2,
            special_warning="Chống chỉ định: CrCl <30"
        )


def render_sglt2_quick_section() -> None:
    """Render SGLT2 Inhibitors quick view section."""
    if not SGLT2_INHIBITORS_DRUGS:
        return
    
    with st.expander("💊 SGLT2 Inhibitors – Ức chế SGLT2 (tóm tắt nhanh)", expanded=False):
        st.caption(
            "Thuốc mới với lợi ích tim mạch và thận. "
            "Lưu ý: Không dùng cho type 1. Nguy cơ nhiễm trùng đường tiết niệu/sinh dục. "
            "Không dùng nếu eGFR <20."
        )
        _render_drug_group_cards(
            SGLT2_INHIBITORS_DRUGS, 
            "SGLT2 Inhibitors", 
            "💊", 
            max_cards=3,
            special_warning="Không dùng: eGFR <20"
        )


def render_diabetes_quick_sections() -> None:
    """Render all diabetes quick view sections."""
    render_metformin_quick_section()
    render_sglt2_quick_section()

