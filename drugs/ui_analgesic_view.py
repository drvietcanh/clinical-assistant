"""
UI components for Analgesic Drugs
Quick view cards for NSAIDs and Opioids
"""

import streamlit as st

# Import analgesic drug groups
try:
    from drugs.drug_modules.analgesics.nsaids import NSAIDS_DRUGS
except ImportError:
    NSAIDS_DRUGS = {}

try:
    from drugs.drug_modules.analgesics.opioid_agonist_strongs import OPIOID_AGONIST_STRONGS_DRUGS
except ImportError:
    OPIOID_AGONIST_STRONGS_DRUGS = {}


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
            inds_short = " • ".join(indications[:2]) if indications else ""
            
            # Try to pick a representative adult dose field
            dose_short = ""
            for key in ("adult_pain", "adult_po", "adult_iv", "adult_standard", "adult_po_immediate"):
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
            if black_box:
                if "ức chế hô hấp" in black_box.lower() or "nghiện" in black_box.lower():
                    warning_html = '<div style="font-size:0.7rem;color:#E74C3C;margin-top:4px;">⚠️ Nguy cơ ức chế hô hấp, nghiện</div>'
                elif "nhồi máu" in black_box.lower() or "đột quỵ" in black_box.lower():
                    warning_html = '<div style="font-size:0.7rem;color:#E74C3C;margin-top:4px;">⚠️ Nguy cơ tim mạch</div>'
            
            st.markdown(
                f"""
<div class="analgesic-drug-card" style="
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


def render_nsaids_quick_section() -> None:
    """Render NSAIDs quick view section."""
    if not NSAIDS_DRUGS:
        return
    
    with st.expander("😣 NSAIDs – Chống viêm không steroid (tóm tắt nhanh)", expanded=False):
        st.caption(
            "Thuốc giảm đau, chống viêm, hạ sốt. "
            "Lưu ý: Nguy cơ chảy máu dạ dày, suy thận, tăng huyết áp. "
            "Chống chỉ định trong 3 tháng cuối thai kỳ."
        )
        _render_drug_group_cards(
            NSAIDS_DRUGS, 
            "NSAIDs", 
            "😣", 
            max_cards=3,
            special_warning="Nguy cơ chảy máu dạ dày, suy thận"
        )


def render_opioids_quick_section() -> None:
    """Render Opioids quick view section."""
    if not OPIOID_AGONIST_STRONGS_DRUGS:
        return
    
    with st.expander("💉 Opioids – Thuốc giảm đau mạnh (tóm tắt nhanh)", expanded=False):
        st.caption(
            "Thuốc giảm đau mạnh cho đau nặng. "
            "Lưu ý: Nguy cơ ức chế hô hấp, nghiện, lệ thuộc. "
            "Cần theo dõi hô hấp chặt chẽ. Có naloxone sẵn sàng."
        )
        _render_drug_group_cards(
            OPIOID_AGONIST_STRONGS_DRUGS, 
            "Opioids", 
            "💉", 
            max_cards=3,
            special_warning="Nguy cơ ức chế hô hấp, nghiện"
        )


def render_analgesic_quick_sections() -> None:
    """Render all analgesic quick view sections."""
    render_nsaids_quick_section()
    render_opioids_quick_section()

