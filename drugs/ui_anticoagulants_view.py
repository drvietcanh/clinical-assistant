"""
UI components for Anticoagulants
Quick view for Warfarin and DOACs (Direct Oral Anticoagulants)
"""

import streamlit as st
from drugs.drug_database import DRUG_DATABASE


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


def _get_anticoagulant_warnings(drug_data: dict) -> list:
    """Extract important warnings for anticoagulants."""
    warnings = []
    
    # Check for black box warnings
    if drug_data.get("black_box_warnings"):
        warnings.append("⚠️ Black Box Warning")
    
    # Check pregnancy category
    pregnancy = drug_data.get("pregnancy", "")
    if pregnancy in ["D", "X"]:
        warnings.append(f"⚠️ Thai kỳ: {pregnancy}")
    
    # Check for bleeding risk
    side_effects = drug_data.get("side_effects", [])
    if any("chảy máu" in str(se).lower() or "bleeding" in str(se).lower() for se in side_effects):
        warnings.append("⚠️ Nguy cơ chảy máu")
    
    # Check for monitoring requirements
    monitoring = drug_data.get("monitoring", [])
    if any("inr" in str(m).lower() for m in monitoring):
        warnings.append("⚠️ Theo dõi INR")
    
    # Check for renal adjustment (DOACs)
    if drug_data.get("renal_adjustment"):
        warnings.append("⚠️ Cần điều chỉnh theo thận")
    
    return warnings


def render_anticoagulants_quick_sections() -> None:
    """
    Render quick view sections for anticoagulants.
    Shows Warfarin and DOACs (Rivaroxaban, Apixaban, Dabigatran).
    """
    try:
        # Define specific anticoagulants to show
        target_drugs = [
            "Warfarin",
            "Rivaroxaban",
            "Apixaban",
            "Dabigatran"
        ]
        
        anticoagulant_drugs = []
        for drug_name in target_drugs:
            if drug_name in DRUG_DATABASE:
                anticoagulant_drugs.append((drug_name, DRUG_DATABASE[drug_name]))
        
        if not anticoagulant_drugs:
            return
        
        with st.expander(
            "💉 Thuốc chống đông – Anticoagulants (tóm tắt nhanh)",
            expanded=False
        ):
            st.caption(
                "Tóm tắt các thuốc chống đông thường dùng (Warfarin và DOACs). "
                "Nhấn vào tên thuốc trong database đầy đủ để xem chi tiết."
            )
            
            num_cols = 2
            cols = st.columns(num_cols)
            
            for idx, (name, data) in enumerate(anticoagulant_drugs):
                with cols[idx % num_cols]:
                    vi_name = data.get("vietnamese_name", "")
                    indications = data.get("indications", [])
                    dosage = data.get("dosage", {})
                    
                    # Build short indications string
                    inds_short = " • ".join(indications[:2]) if indications else ""
                    
                    # Try to pick a representative dose
                    dose_short = ""
                    for key in ("adult_maintenance", "adult_standard", "adult_af", "adult_dvt"):
                        if key in dosage:
                            dose_short = dosage[key]
                            break
                    
                    # Special handling for Warfarin (show target INR)
                    if name == "Warfarin" and "target_inr" in dosage:
                        dose_short = f"{dosage.get('adult_maintenance', '')} (INR: {dosage.get('target_inr', '')})"
                    
                    # Get warnings
                    warnings = _get_anticoagulant_warnings(data)
                    warnings_html = ""
                    if warnings:
                        warnings_html = f"<div style='font-size:0.75rem;color:#EF4444;margin-top:4px;'>{' • '.join(warnings[:2])}</div>"
                    
                    # Evidence badge
                    evidence = data.get("references", {}).get("evidence_level", "")
                    badge_html = _evidence_badge(evidence) if evidence else ""
                    
                    # Color code: Warfarin vs DOACs
                    card_color = "#EF4444" if name == "Warfarin" else "#3B82F6"
                    
                    st.markdown(
                        f"""
<div class="anticoagulant-quick-card" style="
  background: var(--card-bg);
  border: 2px solid {card_color}40;
  border-radius: 12px;
  padding: 12px;
  box-shadow: 0 2px 4px var(--shadow);
  margin-bottom: 0.75rem;
">
  <div style="font-weight:600;font-size:0.95rem;margin-bottom:2px;color:{card_color};">💉 {name}</div>
  <div style="font-size:0.8rem;color:var(--text-secondary);margin-bottom:4px;">{vi_name}</div>
  {f'<div style="font-size:0.8rem;color:var(--text-secondary);margin-bottom:4px;">{inds_short}</div>' if inds_short else ''}
  {f'<div style="font-size:0.8rem;margin-bottom:4px;"><b>Liều:</b> {dose_short}</div>' if dose_short else ''}
  {warnings_html}
  {badge_html}
</div>
""",
                        unsafe_allow_html=True,
                    )
    except Exception as e:
        # Silently fail if there's an error (don't break the page)
        import logging
        logging.warning(f"Error rendering anticoagulants quick sections: {e}")
        pass

