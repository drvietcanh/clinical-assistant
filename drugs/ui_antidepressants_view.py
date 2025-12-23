"""
UI components for Antidepressants (SSRIs)
Quick view for Selective Serotonin Reuptake Inhibitors
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


def _get_antidepressant_warnings(drug_data: dict) -> list:
    """Extract important warnings for antidepressants."""
    warnings = []
    
    # Check for black box warnings
    if drug_data.get("black_box_warnings"):
        warnings.append("⚠️ Black Box Warning")
    
    # Check pregnancy category
    pregnancy = drug_data.get("pregnancy", "")
    if pregnancy in ["D", "X"]:
        warnings.append(f"⚠️ Thai kỳ: {pregnancy}")
    
    # Check for serotonin syndrome risk
    side_effects = drug_data.get("side_effects", [])
    precautions = drug_data.get("precautions", [])
    if any("serotonin" in str(s).lower() for s in side_effects + precautions):
        warnings.append("⚠️ Nguy cơ hội chứng serotonin")
    
    # Check for bleeding risk (SSRIs can increase bleeding)
    if any("chảy máu" in str(se).lower() or "bleeding" in str(se).lower() for se in side_effects):
        warnings.append("⚠️ Nguy cơ chảy máu")
    
    # Check for withdrawal symptoms
    if any("ngừng" in str(p).lower() or "withdrawal" in str(p).lower() for p in precautions):
        warnings.append("⚠️ Triệu chứng cai")
    
    return warnings


def render_antidepressants_quick_sections() -> None:
    """
    Render quick view sections for antidepressants (SSRIs).
    Shows common SSRIs: Fluoxetine, Sertraline, Escitalopram, Paroxetine, Citalopram.
    """
    try:
        # Define SSRIs to show (common ones)
        target_drugs = [
            "Fluoxetine",
            "Sertraline",
            "Escitalopram",
            "Paroxetine",
            "Citalopram"
        ]
        
        ssri_drugs = []
        for drug_name in target_drugs:
            if drug_name in DRUG_DATABASE:
                drug_data = DRUG_DATABASE[drug_name]
                # Check if it's actually an SSRI
                group = drug_data.get("group", "").lower()
                if "ssri" in group or "serotonin" in group or "antidepressant" in group:
                    ssri_drugs.append((drug_name, drug_data))
        
        # Also search by group if not enough found
        if len(ssri_drugs) < 3:
            for drug_name, drug_data in DRUG_DATABASE.items():
                group = drug_data.get("group", "").lower()
                if "ssri" in group or ("serotonin" in group and "reuptake" in group):
                    if (drug_name, drug_data) not in ssri_drugs:
                        ssri_drugs.append((drug_name, drug_data))
        
        if not ssri_drugs:
            return
        
        # Limit to 5 most common
        ssri_drugs = ssri_drugs[:5]
        
        with st.expander(
            "🧠 Thuốc chống trầm cảm – SSRIs (tóm tắt nhanh)",
            expanded=False
        ):
            st.caption(
                "Tóm tắt các SSRI (Selective Serotonin Reuptake Inhibitors) thường dùng. "
                "Nhấn vào tên thuốc trong database đầy đủ để xem chi tiết."
            )
            
            num_cols = min(2, len(ssri_drugs))
            cols = st.columns(num_cols)
            
            for idx, (name, data) in enumerate(ssri_drugs):
                with cols[idx % num_cols]:
                    vi_name = data.get("vietnamese_name", "")
                    indications = data.get("indications", [])
                    dosage = data.get("dosage", {})
                    
                    # Build short indications string
                    inds_short = " • ".join(indications[:2]) if indications else ""
                    
                    # Try to pick a representative dose
                    dose_short = ""
                    for key in ("adult_standard", "adult_po", "adult_initial", "adult_maintenance"):
                        if key in dosage:
                            dose_short = dosage[key]
                            break
                    
                    # Get warnings
                    warnings = _get_antidepressant_warnings(data)
                    warnings_html = ""
                    if warnings:
                        warnings_html = f"<div style='font-size:0.75rem;color:#EF4444;margin-top:4px;'>{' • '.join(warnings[:2])}</div>"
                    
                    # Evidence badge
                    evidence = data.get("references", {}).get("evidence_level", "")
                    badge_html = _evidence_badge(evidence) if evidence else ""
                    
                    st.markdown(
                        f"""
<div class="antidepressant-quick-card" style="
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px;
  box-shadow: 0 2px 4px var(--shadow);
  margin-bottom: 0.75rem;
">
  <div style="font-weight:600;font-size:0.95rem;margin-bottom:2px;">🧠 {name}</div>
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
        logging.warning(f"Error rendering antidepressants quick sections: {e}")
        pass


