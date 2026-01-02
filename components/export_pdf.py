"""
PDF Export Component
Export calculations and protocols to PDF format
"""

import streamlit as st
from typing import Dict, Any, Optional
from io import BytesIO
from datetime import datetime
import base64


def generate_pdf_html(
    title: str,
    content: str,
    include_header: bool = True,
    include_footer: bool = True
) -> str:
    """
    Generate HTML for PDF export (using browser print to PDF)
    
    Args:
        title: Document title
        content: Main content HTML
        include_header: Include header
        include_footer: Include footer
    
    Returns:
        Complete HTML string
    """
    header = f"""
    <div style="text-align: center; margin-bottom: 20px; border-bottom: 2px solid #1976d2; padding-bottom: 10px;">
        <h1 style="color: #1976d2; margin: 0;">🩺 Trợ lý lâm sàng</h1>
        <p style="color: #666; margin: 5px 0 0 0;">{title}</p>
        <p style="color: #999; font-size: 0.9em; margin: 5px 0 0 0;">{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    """ if include_header else ""
    
    footer = f"""
    <div style="text-align: center; margin-top: 30px; padding-top: 10px; border-top: 1px solid #e0e0e0; color: #999; font-size: 0.8em;">
        <p>Trợ lý lâm sàng - Hệ thống công cụ hỗ trợ lâm sàng toàn diện</p>
        <p>⚠️ Chỉ mục đích tham khảo - Không thay thế đánh giá lâm sàng</p>
    </div>
    """ if include_footer else ""
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            @media print {{
                @page {{
                    margin: 2cm;
                    size: A4;
                }}
                body {{
                    font-family: Arial, sans-serif;
                    font-size: 12pt;
                    line-height: 1.6;
                    color: #212121;
                }}
                h1, h2, h3 {{
                    color: #1976d2;
                    page-break-after: avoid;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 10px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f5f5f5;
                    font-weight: bold;
                }}
            }}
            body {{
                font-family: Arial, sans-serif;
                font-size: 12pt;
                line-height: 1.6;
                color: #212121;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        {header}
        <div class="content">
            {content}
        </div>
        {footer}
    </body>
    </html>
    """
    
    return html


def render_pdf_export_button(
    title: str,
    content: str,
    filename: Optional[str] = None,
    button_text: str = "📄 Xuất PDF"
) -> None:
    """
    Render button to export content as PDF (using browser print)
    
    Args:
        title: Document title
        content: Content to export (HTML string)
        filename: Suggested filename
        button_text: Button text
    """
    if filename is None:
        filename = f"{title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    html_content = generate_pdf_html(title, content)
    
    # Encode HTML for data URI
    html_encoded = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    
    st.markdown(f"""
    <button onclick="
        const html = atob('{html_encoded}');
        const blob = new Blob([html], {{type: 'text/html'}});
        const url = URL.createObjectURL(blob);
        const printWindow = window.open(url, '_blank');
        printWindow.onload = function() {{
            printWindow.print();
        }};
    " style="
        background: #1976d2;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
    ">{button_text}</button>
    """, unsafe_allow_html=True)


def render_qr_code_share(
    data: str,
    title: str = "Chia sẻ kết quả"
) -> None:
    """
    Render QR code for sharing results
    
    Args:
        data: Data to encode in QR code
        title: Title for the share section
    """
    st.markdown(f"### {title}")
    
    # Use a QR code library via CDN
    st.markdown(f"""
    <div id="qrcode" style="text-align: center; padding: 20px;"></div>
    <script src="https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js"></script>
    <script>
        new QRCode(document.getElementById("qrcode"), {{
            text: "{data}",
            width: 200,
            height: 200,
            colorDark: "#000000",
            colorLight: "#ffffff",
            correctLevel: QRCode.CorrectLevel.H
        }});
    </script>
    """, unsafe_allow_html=True)


__all__ = [
    'generate_pdf_html',
    'render_pdf_export_button',
    'render_qr_code_share',
]

