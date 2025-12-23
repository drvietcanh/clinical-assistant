"""
UI components for Antibiotics
Quick view for common antibiotic groups: Beta-lactams, Fluoroquinolones, Macrolides
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


def _get_antibiotic_warnings(drug_data: dict) -> list:
    """Extract important warnings for antibiotics."""
    warnings = []
    
    # Check for black box warnings
    if drug_data.get("black_box_warnings"):
        warnings.append("⚠️ Black Box Warning")
    
    # Check pregnancy category
    pregnancy = drug_data.get("pregnancy", "")
    if pregnancy in ["D", "X"]:
        warnings.append(f"⚠️ Thai kỳ: {pregnancy}")
    
    # Check for renal adjustment
    if drug_data.get("renal_adjustment"):
        warnings.append("⚠️ Cần điều chỉnh theo thận")
    
    # Check for monitoring requirements
    monitoring = drug_data.get("monitoring", [])
    if any("creatinine" in str(m).lower() or "egfr" in str(m).lower() for m in monitoring):
        warnings.append("⚠️ Theo dõi chức năng thận")
    
    # Check for C. difficile risk
    precautions = drug_data.get("precautions", [])
    if any("difficile" in str(p).lower() or "c. diff" in str(p).lower() for p in precautions):
        warnings.append("⚠️ Nguy cơ C. difficile")
    
    return warnings


def render_antibiotics_quick_sections() -> None:
    """
    Render quick view sections for antibiotics.
    Shows Beta-lactams, Fluoroquinolones, and Macrolides.
    """
    try:
        # Define antibiotic groups to show
        antibiotic_groups = [
        {
            "name": "Beta-lactams",
            "keywords": ["Beta-lactam", "Penicillin", "Carbapenem", "Cephalosporin"],
            "icon": "💉",
            "color": "#3B82F6"
        },
        {
            "name": "Fluoroquinolones",
            "keywords": ["Fluoroquinolone"],
            "icon": "🦠",
            "color": "#EF4444"
        },
        {
            "name": "Macrolides",
            "keywords": ["Macrolide"],
            "icon": "💊",
            "color": "#10B981"
        }
    ]
    
        for group_info in antibiotic_groups:
            # Find drugs in this group
            group_drugs = []
            for drug_name, drug_data in DRUG_DATABASE.items():
                group = drug_data.get("group", "").lower()
                if any(kw.lower() in group for kw in group_info["keywords"]):
                    group_drugs.append((drug_name, drug_data))
            
            if not group_drugs:
                continue
            
            # Limit to 4 most common drugs
            max_cards = 4
            items = group_drugs[:max_cards]
            
            with st.expander(
                f"{group_info['icon']} {group_info['name']} – Kháng sinh ({len(group_drugs)} thuốc)",
                expanded=False
            ):
                st.caption(
                    f"Tóm tắt một số {group_info['name']} thường dùng. "
                    "Nhấn vào tên thuốc trong database đầy đủ để xem chi tiết."
                )
                
                num_cols = min(2, len(items))
                cols = st.columns(num_cols) if items else []
                
                for idx, (name, data) in enumerate(items):
                    with cols[idx % num_cols]:
                        vi_name = data.get("vietnamese_name", "")
                        indications = data.get("indications", [])
                        dosage = data.get("dosage", {})
                        
                        # Build short indications string
                        inds_short = " • ".join(indications[:2]) if indications else ""
                        
                        # Try to pick a representative dose
                        dose_short = ""
                        for key in ("adult_standard", "adult_iv", "adult_po", "adult_severe"):
                            if key in dosage:
                                dose_short = dosage[key]
                                break
                        
                        # Get warnings
                        warnings = _get_antibiotic_warnings(data)
                        warnings_html = ""
                        if warnings:
                            warnings_html = f"<div style='font-size:0.75rem;color:#EF4444;margin-top:4px;'>{' • '.join(warnings[:2])}</div>"
                        
                        # Evidence badge
                        evidence = data.get("references", {}).get("evidence_level", "")
                        badge_html = _evidence_badge(evidence) if evidence else ""
                        
                        st.markdown(
                            f"""
<div class="antibiotic-quick-card" style="
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px;
  box-shadow: 0 2px 4px var(--shadow);
  margin-bottom: 0.75rem;
">
  <div style="font-weight:600;font-size:0.95rem;margin-bottom:2px;">{group_info['icon']} {name}</div>
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
        logging.warning(f"Error rendering antibiotics quick sections: {e}")
        pass

