"""
Antibiotics Export Module
Export dosing results, protocols, and comparisons to PDF, Excel, and clipboard
"""

import streamlit as st
from typing import Dict, List, Any, Optional
from datetime import datetime
from io import BytesIO
import pandas as pd
import base64

from components.export_pdf import generate_pdf_html, render_pdf_export_button


def format_dosing_result_for_export(
    drug_name: str,
    dose_result: Dict[str, Any],
    patient_info: Optional[Dict[str, Any]] = None
) -> str:
    """
    Format dosing calculation result for export
    
    Args:
        drug_name: Name of antibiotic
        dose_result: Dosing calculation result dict
        patient_info: Patient information dict
    
    Returns:
        Formatted HTML string
    """
    html = f"""
    <h2>💊 Kết Quả Tính Liều: {drug_name}</h2>
    """
    
    if patient_info:
        html += """
        <div style="background: #f5f5f5; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
            <h3>📋 Thông Tin Bệnh Nhân</h3>
            <table style="width: 100%; border-collapse: collapse;">
        """
        for key, value in patient_info.items():
            html += f"""
                <tr>
                    <td style="padding: 5px; font-weight: bold; width: 40%;">{key}:</td>
                    <td style="padding: 5px;">{value}</td>
                </tr>
            """
        html += """
            </table>
        </div>
        """
    
    html += """
    <div style="background: #e3f2fd; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3>💉 Liều Dùng Đề Xuất</h3>
        <table style="width: 100%; border-collapse: collapse;">
    """
    
    # Add dosing information
    if 'dose' in dose_result:
        html += f"""
            <tr>
                <td style="padding: 8px; font-weight: bold; border: 1px solid #ddd;">Liều:</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{dose_result.get('dose', 'N/A')}</td>
            </tr>
        """
    
    if 'frequency' in dose_result:
        html += f"""
            <tr>
                <td style="padding: 8px; font-weight: bold; border: 1px solid #ddd;">Tần suất:</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{dose_result.get('frequency', 'N/A')}</td>
            </tr>
        """
    
    if 'route' in dose_result:
        html += f"""
            <tr>
                <td style="padding: 8px; font-weight: bold; border: 1px solid #ddd;">Đường dùng:</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{dose_result.get('route', 'N/A')}</td>
            </tr>
        """
    
    if 'total_daily_dose' in dose_result:
        html += f"""
            <tr>
                <td style="padding: 8px; font-weight: bold; border: 1px solid #ddd;">Tổng liều/ngày:</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{dose_result.get('total_daily_dose', 'N/A')}</td>
            </tr>
        """
    
    html += """
        </table>
    </div>
    """
    
    # Add warnings if any
    if 'warnings' in dose_result and dose_result['warnings']:
        html += """
        <div style="background: #fff3cd; padding: 15px; border-radius: 5px; margin-bottom: 20px; border-left: 4px solid #ffc107;">
            <h3>⚠️ Cảnh Báo</h3>
            <ul>
        """
        for warning in dose_result['warnings']:
            html += f"<li>{warning}</li>"
        html += """
            </ul>
        </div>
        """
    
    # Add notes if any
    if 'notes' in dose_result and dose_result['notes']:
        html += f"""
        <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
            <h3>📝 Ghi Chú</h3>
            <p>{dose_result['notes']}</p>
        </div>
        """
    
    html += f"""
    <p style="color: #666; font-size: 0.9em; margin-top: 20px;">
        <em>Xuất ngày: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em>
    </p>
    """
    
    return html


def format_protocol_for_export(
    protocol: Dict[str, Any]
) -> str:
    """
    Format treatment protocol for export
    
    Args:
        protocol: Protocol dict with title, infection, regimens, etc.
    
    Returns:
        Formatted HTML string
    """
    html = f"""
    <h2>📋 Phác Đồ Điều Trị: {protocol.get('title', 'N/A')}</h2>
    """
    
    if 'infection_site' in protocol:
        html += f"""
        <p><strong>Vị trí nhiễm trùng:</strong> {protocol['infection_site']}</p>
        """
    
    if 'severity' in protocol:
        html += f"""
        <p><strong>Mức độ nặng:</strong> {protocol['severity']}</p>
        """
    
    if 'guideline' in protocol:
        html += f"""
        <p><strong>Nguồn hướng dẫn:</strong> {protocol['guideline']}</p>
        """
    
    html += "<hr style='margin: 20px 0;'>"
    
    # Add regimens
    if 'regimens' in protocol:
        html += "<h3>💊 Phác Đồ Điều Trị</h3>"
        for i, regimen in enumerate(protocol['regimens'], 1):
            html += f"""
            <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 4px solid #1976d2;">
                <h4>Phác đồ {i}: {regimen.get('name', 'N/A')}</h4>
            """
            
            if 'drugs' in regimen:
                html += "<p><strong>Thuốc:</strong></p><ul>"
                for drug in regimen['drugs']:
                    html += f"<li>{drug}</li>"
                html += "</ul>"
            
            if 'duration' in regimen:
                html += f"<p><strong>Thời gian điều trị:</strong> {regimen['duration']}</p>"
            
            if 'notes' in regimen:
                html += f"<p><strong>Ghi chú:</strong> {regimen['notes']}</p>"
            
            html += "</div>"
    
    html += f"""
    <p style="color: #666; font-size: 0.9em; margin-top: 20px;">
        <em>Xuất ngày: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em>
    </p>
    """
    
    return html


def format_comparison_for_export(
    comparison_data: List[Dict[str, Any]],
    drugs: List[str]
) -> str:
    """
    Format drug comparison for export
    
    Args:
        comparison_data: List of comparison dicts
        drugs: List of drug names being compared
    
    Returns:
        Formatted HTML string
    """
    html = f"""
    <h2>📊 So Sánh Kháng Sinh</h2>
    <p><strong>Các thuốc so sánh:</strong> {', '.join(drugs)}</p>
    <hr style='margin: 20px 0;'>
    """
    
    # Create comparison table
    html += """
    <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
        <thead>
            <tr style="background: #f5f5f5;">
                <th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Thuốc</th>
                <th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Liều</th>
                <th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Tần suất</th>
                <th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Phổ tác dụng</th>
                <th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Ghi chú</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for drug_data in comparison_data:
        html += f"""
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">{drug_data.get('name', 'N/A')}</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{drug_data.get('dose', 'N/A')}</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{drug_data.get('frequency', 'N/A')}</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{drug_data.get('spectrum', 'N/A')}</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{drug_data.get('notes', 'N/A')}</td>
            </tr>
        """
    
    html += """
        </tbody>
    </table>
    """
    
    html += f"""
    <p style="color: #666; font-size: 0.9em; margin-top: 20px;">
        <em>Xuất ngày: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em>
    </p>
    """
    
    return html


def copy_to_clipboard(text: str, button_label: str = "📋 Copy", key: Optional[str] = None) -> None:
    """
    Render button to copy text to clipboard
    
    Args:
        text: Text to copy
        button_label: Button label
        key: Unique key for the button
    """
    if key is None:
        key = f"copy_{hash(text) % 10000}"
    
    # Use Streamlit's download button approach for better compatibility
    # Create a text file in memory and use download button
    text_bytes = text.encode('utf-8')
    
    # Also provide JavaScript fallback for direct clipboard copy
    text_encoded = base64.b64encode(text_bytes).decode('utf-8')
    
    # Create a container with both options
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Download as text file (works everywhere)
        st.download_button(
            label=button_label,
            data=text_bytes,
            file_name="clipboard.txt",
            mime="text/plain",
            key=f"{key}_download"
        )
    
    with col2:
        # JavaScript clipboard copy (works in modern browsers)
        st.markdown(f"""
        <button onclick="
            const text = atob('{text_encoded}');
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(text).then(function() {{
                    alert('✅ Đã sao chép vào clipboard!');
                }}, function(err) {{
                    console.error('Lỗi sao chép:', err);
                    alert('⚠️ Không thể sao chép tự động. Vui lòng sử dụng nút Download.');
                }});
            }} else {{
                // Fallback: select text
                const textarea = document.createElement('textarea');
                textarea.value = text;
                document.body.appendChild(textarea);
                textarea.select();
                try {{
                    document.execCommand('copy');
                    alert('✅ Đã sao chép vào clipboard!');
                }} catch (err) {{
                    alert('⚠️ Vui lòng sử dụng nút Download.');
                }}
                document.body.removeChild(textarea);
            }}
        " style="
            background: #4caf50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            width: 100%;
        ">📋 Copy (JS)</button>
        """, unsafe_allow_html=True)


def export_to_excel(
    data: List[Dict[str, Any]],
    filename: Optional[str] = None,
    sheet_name: str = "Data"
) -> None:
    """
    Export data to Excel file
    
    Args:
        data: List of dicts to export
        filename: Output filename
        sheet_name: Sheet name
    """
    if not data:
        st.warning("Không có dữ liệu để xuất")
        return
    
    df = pd.DataFrame(data)
    
    if filename is None:
        filename = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    
    # Create Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    output.seek(0)
    
    # Download button
    st.download_button(
        label="📊 Xuất Excel",
        data=output.getvalue(),
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def render_export_buttons(
    content_type: str,
    content_data: Any,
    title: str,
    filename: Optional[str] = None
) -> None:
    """
    Render export buttons (PDF, Copy, Excel) for different content types
    
    Args:
        content_type: Type of content ('dosing', 'protocol', 'comparison')
        content_data: Data to export
        title: Document title
        filename: Suggested filename
    """
    col1, col2, col3 = st.columns(3)
    
    # Format content based on type
    if content_type == 'dosing':
        html_content = format_dosing_result_for_export(
            content_data.get('drug_name', ''),
            content_data.get('result', {}),
            content_data.get('patient_info')
        )
        text_content = f"""
Kết Quả Tính Liều: {content_data.get('drug_name', '')}

Liều: {content_data.get('result', {}).get('dose', 'N/A')}
Tần suất: {content_data.get('result', {}).get('frequency', 'N/A')}
Đường dùng: {content_data.get('result', {}).get('route', 'N/A')}
        """
    elif content_type == 'protocol':
        html_content = format_protocol_for_export(content_data)
        text_content = f"""
Phác Đồ Điều Trị: {content_data.get('title', 'N/A')}

Vị trí nhiễm trùng: {content_data.get('infection_site', 'N/A')}
Mức độ nặng: {content_data.get('severity', 'N/A')}
        """
    elif content_type == 'comparison':
        html_content = format_comparison_for_export(
            content_data.get('comparison_data', []),
            content_data.get('drugs', [])
        )
        text_content = f"""
So Sánh Kháng Sinh: {', '.join(content_data.get('drugs', []))}
        """
    else:
        st.error(f"Unknown content type: {content_type}")
        return
    
    with col1:
        render_pdf_export_button(
            title=title,
            content=html_content,
            filename=filename,
            button_text="📄 PDF"
        )
    
    with col2:
        copy_to_clipboard(text_content, "📋 Copy")
    
    with col3:
        if content_type == 'comparison' and 'comparison_data' in content_data:
            export_to_excel(
                content_data['comparison_data'],
                filename=filename.replace('.pdf', '.xlsx') if filename else None
            )


# Print-friendly CSS injection
PRINT_CSS = """
<style>
@media print {
    .stSidebar,
    .stHeader,
    .stButton,
    .stDownloadButton,
    button {
        display: none !important;
    }
    
    .main-content {
        width: 100% !important;
        margin: 0 !important;
        padding: 20px !important;
    }
    
    .protocol-card,
    .regimen-card,
    .dosing-result {
        page-break-inside: avoid;
        border: 1px solid #000 !important;
        margin-bottom: 20px !important;
    }
    
    h1, h2, h3 {
        page-break-after: avoid;
    }
    
    table {
        page-break-inside: auto;
    }
    
    tr {
        page-break-inside: avoid;
        page-break-after: auto;
    }
}
</style>
"""


def inject_print_css() -> None:
    """Inject print-friendly CSS"""
    st.markdown(PRINT_CSS, unsafe_allow_html=True)


__all__ = [
    'format_dosing_result_for_export',
    'format_protocol_for_export',
    'format_comparison_for_export',
    'copy_to_clipboard',
    'export_to_excel',
    'render_export_buttons',
    'inject_print_css',
]
