"""
Drug Interaction Matrix Component
Visual matrix for displaying drug-drug interactions with severity levels
"""

import streamlit as st
import streamlit.components.v1 as components
from typing import List, Dict, Any, Optional
from drugs.interactions_data import (
    SEVERITY_MAJOR,
    SEVERITY_MODERATE,
    SEVERITY_MINOR,
    get_interaction
)


def get_severity_color(severity: str) -> Dict[str, str]:
    """
    Get color scheme for interaction severity
    
    Returns:
        Dict with bg_color, border_color, text_color, icon, label
    """
    color_map = {
        SEVERITY_MAJOR: {
            "bg_color": "#f8d7da",
            "border_color": "#dc3545",
            "text_color": "#721c24",
            "icon": "🔴",
            "label": "Major"
        },
        SEVERITY_MODERATE: {
            "bg_color": "#fff3cd",
            "border_color": "#ffc107",
            "text_color": "#856404",
            "icon": "🟡",
            "label": "Moderate"
        },
        SEVERITY_MINOR: {
            "bg_color": "#d1ecf1",
            "border_color": "#17a2b8",
            "text_color": "#0c5460",
            "icon": "🔵",
            "label": "Minor"
        },
        "none": {
            "bg_color": "#d4edda",
            "border_color": "#28a745",
            "text_color": "#155724",
            "icon": "✅",
            "label": "No Interaction"
        },
        "same": {
            "bg_color": "#f8f9fa",
            "border_color": "#dee2e6",
            "text_color": "#6c757d",
            "icon": "—",
            "label": "Same Drug"
        }
    }
    return color_map.get(severity, color_map["none"])


def render_interaction_matrix(
    drugs: List[str],
    interactions: List[Dict[str, Any]],
    show_tooltips: bool = True,
    compact: bool = False
) -> None:
    """
    Render visual interaction matrix with color-coded cells
    
    Args:
        drugs: List of drug names
        interactions: List of interaction results
        show_tooltips: Whether to show tooltips on hover
        compact: Use compact layout
    """
    if not drugs or len(drugs) < 2:
        st.warning("Cần ít nhất 2 thuốc để hiển thị ma trận")
        return
    
    # Create interaction map for quick lookup
    interaction_map = {}
    for interaction in interactions:
        key = tuple(sorted([interaction["drug1"], interaction["drug2"]]))
        interaction_map[key] = interaction
    
    # Build matrix HTML
    cell_size = "50px" if compact else "70px"
    font_size = "0.8rem" if compact else "1rem"
    
    # Header row
    header_html = "<tr><th style='padding: 10px; background: #f8f9fa; border: 1px solid #dee2e6; font-weight: bold;'>Thuốc</th>"
    for drug in drugs:
        # Truncate long drug names
        display_name = drug[:12] + "..." if len(drug) > 12 else drug
        header_html += f"<th style='padding: 10px; background: #f8f9fa; border: 1px solid #dee2e6; font-weight: bold; text-align: center; min-width: {cell_size};' title='{drug}'>{display_name}</th>"
    header_html += "</tr>"
    
    # Data rows
    rows_html = ""
    for i, drug1 in enumerate(drugs):
        # Truncate long drug names
        display_name1 = drug1[:12] + "..." if len(drug1) > 12 else drug1
        rows_html += f"<tr><th style='padding: 10px; background: #f8f9fa; border: 1px solid #dee2e6; font-weight: bold; text-align: left;' title='{drug1}'>{display_name1}</th>"
        
        for j, drug2 in enumerate(drugs):
            if i == j:
                # Same drug - diagonal
                colors = get_severity_color("same")
                cell_html = f"""
                <td style='
                    padding: 10px;
                    background: {colors["bg_color"]};
                    border: 2px solid {colors["border_color"]};
                    text-align: center;
                    min-width: {cell_size};
                    height: {cell_size};
                    font-size: {font_size};
                    color: {colors["text_color"]};
                    font-weight: bold;
                ' title='Cùng thuốc'>
                    {colors["icon"]}
                </td>
                """
                rows_html += cell_html
            else:
                # Get interaction
                key = tuple(sorted([drug1, drug2]))
                if key in interaction_map:
                    interaction = interaction_map[key]
                    severity = interaction.get("severity", SEVERITY_MINOR)
                    mechanism = interaction.get("mechanism", "")
                    description = interaction.get("description", "")
                else:
                    # Check if interaction exists in database
                    interaction_data = get_interaction(drug1, drug2)
                    if interaction_data:
                        severity = interaction_data.get("severity", SEVERITY_MINOR)
                        mechanism = interaction_data.get("mechanism", "")
                        description = interaction_data.get("description", "")
                    else:
                        severity = "none"
                        mechanism = ""
                        description = "Không có tương tác được ghi nhận"
                
                colors = get_severity_color(severity)
                
                # Tooltip text
                tooltip_text = f"{drug1} + {drug2}"
                if mechanism:
                    tooltip_text += f"\n{colors['label']}: {mechanism}"
                if description:
                    tooltip_text += f"\n{description}"
                
                # Cell with tooltip
                cell_html = f"""
                <td style='
                    padding: 10px;
                    background: {colors["bg_color"]};
                    border: 2px solid {colors["border_color"]};
                    text-align: center;
                    min-width: {cell_size};
                    height: {cell_size};
                    font-size: {font_size};
                    color: {colors["text_color"]};
                    font-weight: bold;
                    cursor: pointer;
                    position: relative;
                    transition: transform 0.2s;
                ' 
                title='{tooltip_text.replace(chr(39), "&apos;")}'
                onmouseover="this.style.transform='scale(1.15)'; this.style.zIndex='1000'; this.style.boxShadow='0 4px 8px rgba(0,0,0,0.2)';"
                onmouseout="this.style.transform='scale(1)'; this.style.zIndex='auto'; this.style.boxShadow='none';"
                >
                    {colors["icon"]}
                </td>
                """
                rows_html += cell_html
        
        rows_html += "</tr>"
    
    # Enhanced table HTML with better styling (inspired by Drugs.com & Epocrates)
    table_html = f"""
    <div style="
        margin: 1.5rem 0;
        overflow-x: auto;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        background: white;
        border: 1px solid #e2e8f0;
    ">
        <style>
            .interaction-matrix-table {{
                border-collapse: collapse;
                width: 100%;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            }}
            .interaction-matrix-table th {{
                position: sticky;
                top: 0;
                z-index: 10;
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            }}
            .interaction-matrix-table td:hover {{
                z-index: 100 !important;
            }}
        </style>
        <table class="interaction-matrix-table">
            <thead>
                {header_html}
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """
    
    # Calculate height dynamically based on number of drugs
    matrix_height = min(600, max(300, len(drugs) * 80 + 100))
    components.html(table_html, height=matrix_height, scrolling=True)
    
    # Legend
    legend_html = '<div style="display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0; padding: 1rem; background: #f8f9fa; border-radius: 8px;">'
    
    for severity in [SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR, "none"]:
        colors = get_severity_color(severity)
        label = "Không tương tác" if severity == "none" else colors["label"]
        legend_html += f'''<div style="display: flex; align-items: center; gap: 0.5rem;"><div style="width: 28px; height: 28px; background: {colors["bg_color"]}; border: 2px solid {colors["border_color"]}; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem;">{colors["icon"]}</div><span style="font-size: 0.9rem; color: #495057; font-weight: 500;">{label}</span></div>'''
    
    legend_html += '</div>'
    st.markdown(legend_html, unsafe_allow_html=True)


def render_interaction_summary(
    interactions: List[Dict[str, Any]]
) -> None:
    """
    Render interaction summary with statistics
    
    Args:
        interactions: List of interaction results
    """
    if not interactions:
        st.success("✅ **Không phát hiện tương tác thuốc**")
        return
    
    # Count by severity
    counts = {
        SEVERITY_MAJOR: 0,
        SEVERITY_MODERATE: 0,
        SEVERITY_MINOR: 0
    }
    
    for interaction in interactions:
        severity = interaction.get("severity", SEVERITY_MINOR)
        counts[severity] = counts.get(severity, 0) + 1
    
    total = len(interactions)
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "🔴 Major",
            counts[SEVERITY_MAJOR],
            delta=f"{counts[SEVERITY_MAJOR]/total*100:.1f}%" if total > 0 else "0%",
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            "🟡 Moderate",
            counts[SEVERITY_MODERATE],
            delta=f"{counts[SEVERITY_MODERATE]/total*100:.1f}%" if total > 0 else "0%"
        )
    
    with col3:
        st.metric(
            "🔵 Minor",
            counts[SEVERITY_MINOR],
            delta=f"{counts[SEVERITY_MINOR]/total*100:.1f}%" if total > 0 else "0%"
        )

