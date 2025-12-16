"""
Visual IV Compatibility Matrix Component
Color-coded interactive matrix for displaying drug compatibility
"""

import streamlit as st
import streamlit.components.v1 as components
from typing import List, Dict, Tuple, Optional, Any
import json
import base64
from io import BytesIO


def get_compatibility_color(status: str) -> Dict[str, str]:
    """
    Get color scheme for compatibility status
    
    Returns:
        Dict with bg_color, border_color, text_color, icon
    """
    color_map = {
        "compatible": {
            "bg_color": "#d4edda",
            "border_color": "#28a745",
            "text_color": "#155724",
            "icon": "✅",
            "label": "Tương thích"
        },
        "questionable": {
            "bg_color": "#fff3cd",
            "border_color": "#ffc107",
            "text_color": "#856404",
            "icon": "⚠️",
            "label": "Thận trọng"
        },
        "incompatible": {
            "bg_color": "#f8d7da",
            "border_color": "#dc3545",
            "text_color": "#721c24",
            "icon": "❌",
            "label": "Không tương thích"
        },
        "unknown": {
            "bg_color": "#e9ecef",
            "border_color": "#6c757d",
            "text_color": "#495057",
            "icon": "❓",
            "label": "Chưa rõ"
        },
        "same": {
            "bg_color": "#f8f9fa",
            "border_color": "#dee2e6",
            "text_color": "#6c757d",
            "icon": "—",
            "label": "Cùng thuốc"
        }
    }
    return color_map.get(status, color_map["unknown"])


def render_visual_compatibility_matrix(
    drugs: List[str],
    compatibility_data: List[Dict[str, Any]],
    show_tooltips: bool = True,
    compact: bool = False
) -> None:
    """
    Render visual compatibility matrix with color-coded cells
    
    Args:
        drugs: List of drug names
        compatibility_data: List of compatibility results with structure:
            [{"drug1": str, "drug2": str, "status": str, "notes": str}, ...]
        show_tooltips: Whether to show tooltips on hover
        compact: Use compact layout
    """
    if not drugs or len(drugs) < 2:
        st.warning("Cần ít nhất 2 thuốc để hiển thị ma trận")
        return
    
    # Create compatibility map for quick lookup
    compat_map = {}
    for item in compatibility_data:
        key = tuple(sorted([item["drug1"], item["drug2"]]))
        compat_map[key] = item
    
    # Build matrix HTML
    cell_size = "40px" if compact else "60px"
    font_size = "0.75rem" if compact else "1rem"
    
    # Header row
    header_html = "<tr><th style='padding: 8px; background: #f8f9fa; border: 1px solid #dee2e6; font-weight: bold;'>Thuốc</th>"
    for drug in drugs:
        # Truncate long drug names
        display_name = drug[:15] + "..." if len(drug) > 15 else drug
        header_html += f"<th style='padding: 8px; background: #f8f9fa; border: 1px solid #dee2e6; font-weight: bold; text-align: center; min-width: {cell_size};' title='{drug}'>{display_name}</th>"
    header_html += "</tr>"
    
    # Data rows
    rows_html = ""
    for i, drug1 in enumerate(drugs):
        # Truncate long drug names
        display_name1 = drug1[:15] + "..." if len(drug1) > 15 else drug1
        rows_html += f"<tr><th style='padding: 8px; background: #f8f9fa; border: 1px solid #dee2e6; font-weight: bold; text-align: left;' title='{drug1}'>{display_name1}</th>"
        
        for j, drug2 in enumerate(drugs):
            if i == j:
                # Same drug - diagonal
                colors = get_compatibility_color("same")
                cell_html = f"""
                <td style='
                    padding: 8px;
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
                # Get compatibility
                key = tuple(sorted([drug1, drug2]))
                if key in compat_map:
                    compat = compat_map[key]
                    status = compat["status"]
                    notes = compat.get("notes", "")
                else:
                    status = "unknown"
                    notes = "Không có dữ liệu"
                
                colors = get_compatibility_color(status)
                
                # Tooltip data
                tooltip_data = {
                    "drug1": drug1,
                    "drug2": drug2,
                    "status": status,
                    "notes": notes,
                    "label": colors["label"]
                }
                tooltip_json = json.dumps(tooltip_data).replace("'", "\\'")
                
                # Cell with tooltip
                cell_html = f"""
                <td style='
                    padding: 8px;
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
                ' 
                title='{drug1} + {drug2}: {colors["label"]} - {notes}'
                data-tooltip='{tooltip_json}'
                onmouseover="this.style.transform='scale(1.1)'; this.style.zIndex='1000';"
                onmouseout="this.style.transform='scale(1)'; this.style.zIndex='auto';"
                >
                    {colors["icon"]}
                </td>
                """
                rows_html += cell_html
        
        rows_html += "</tr>"
    
    # Full table HTML
    table_html = f"""
    <div style="
        margin: 1.5rem 0;
        overflow-x: auto;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    ">
        <table style="
            border-collapse: collapse;
            width: 100%;
            background: white;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        ">
            <thead>
                {header_html}
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """
    
    components.html(table_html, height=600, scrolling=True)
    
    # Legend
    legend_html = """
    <div style="
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin: 1rem 0;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
    ">
    """
    
    for status in ["compatible", "questionable", "incompatible", "unknown"]:
        colors = get_compatibility_color(status)
        legend_html += f"""
        <div style="
            display: flex;
            align-items: center;
            gap: 0.5rem;
        ">
            <div style="
                width: 24px;
                height: 24px;
                background: {colors["bg_color"]};
                border: 2px solid {colors["border_color"]};
                border-radius: 4px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 0.75rem;
            ">{colors["icon"]}</div>
            <span style="font-size: 0.9rem; color: #495057;">{colors["label"]}</span>
        </div>
        """
    
    legend_html += "</div>"
    components.html(legend_html, height=150, scrolling=False)


def render_compatibility_summary(
    compatibility_data: List[Dict[str, Any]]
) -> None:
    """
    Render compatibility summary with statistics
    
    Args:
        compatibility_data: List of compatibility results
    """
    if not compatibility_data:
        return
    
    # Count by status
    counts = {
        "compatible": 0,
        "questionable": 0,
        "incompatible": 0,
        "unknown": 0
    }
    
    for item in compatibility_data:
        status = item.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1
    
    total = len(compatibility_data)
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "✅ Tương thích",
            counts["compatible"],
            delta=f"{counts['compatible']/total*100:.1f}%" if total > 0 else "0%"
        )
    
    with col2:
        st.metric(
            "⚠️ Thận trọng",
            counts["questionable"],
            delta=f"{counts['questionable']/total*100:.1f}%" if total > 0 else "0%"
        )
    
    with col3:
        st.metric(
            "❌ Không tương thích",
            counts["incompatible"],
            delta=f"{counts['incompatible']/total*100:.1f}%" if total > 0 else "0%",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            "❓ Chưa rõ",
            counts["unknown"],
            delta=f"{counts['unknown']/total*100:.1f}%" if total > 0 else "0%"
        )


def export_matrix_to_html(
    drugs: List[str],
    compatibility_data: List[Dict[str, Any]],
    title: str = "IV Compatibility Matrix"
) -> str:
    """
    Export compatibility matrix to HTML string
    
    Args:
        drugs: List of drug names
        compatibility_data: List of compatibility results
        title: Matrix title
    
    Returns:
        HTML string
    """
    # Create compatibility map
    compat_map = {}
    for item in compatibility_data:
        key = tuple(sorted([item["drug1"], item["drug2"]]))
        compat_map[key] = item
    
    # Build HTML
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                padding: 2rem;
                background: #f8f9fa;
            }}
            h1 {{
                color: #212121;
                margin-bottom: 2rem;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                background: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 2rem;
            }}
            th, td {{
                padding: 12px;
                border: 1px solid #dee2e6;
                text-align: center;
            }}
            th {{
                background: #f8f9fa;
                font-weight: bold;
            }}
            .legend {{
                display: flex;
                flex-wrap: wrap;
                gap: 1rem;
                margin-top: 2rem;
            }}
            .legend-item {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <table>
            <thead>
                <tr>
                    <th>Thuốc</th>
    """
    
    for drug in drugs:
        html += f"<th>{drug}</th>"
    
    html += """
                </tr>
            </thead>
            <tbody>
    """
    
    for i, drug1 in enumerate(drugs):
        html += f"<tr><th>{drug1}</th>"
        for j, drug2 in enumerate(drugs):
            if i == j:
                colors = get_compatibility_color("same")
                html += f"""
                <td style="background: {colors['bg_color']}; border: 2px solid {colors['border_color']};">
                    {colors['icon']}
                </td>
                """
            else:
                key = tuple(sorted([drug1, drug2]))
                if key in compat_map:
                    compat = compat_map[key]
                    status = compat["status"]
                else:
                    status = "unknown"
                
                colors = get_compatibility_color(status)
                html += f"""
                <td style="background: {colors['bg_color']}; border: 2px solid {colors['border_color']};" title="{drug1} + {drug2}: {colors['label']}">
                    {colors['icon']}
                </td>
                """
        html += "</tr>"
    
    html += """
            </tbody>
        </table>
        <div class="legend">
    """
    
    for status in ["compatible", "questionable", "incompatible", "unknown"]:
        colors = get_compatibility_color(status)
        html += f"""
        <div class="legend-item">
            <div style="width: 24px; height: 24px; background: {colors['bg_color']}; border: 2px solid {colors['border_color']}; display: flex; align-items: center; justify-content: center;">
                {colors['icon']}
            </div>
            <span>{colors['label']}</span>
        </div>
        """
    
    html += """
        </div>
    </body>
    </html>
    """
    
    return html

