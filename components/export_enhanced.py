"""
Enhanced Export Component
PDF export, QR Code generation, Email results, and Print-friendly view
"""

import streamlit as st
from typing import Optional, Dict, Any, List
from io import BytesIO
from datetime import datetime
import json
import base64

# Try to import qrcode
try:
    import qrcode
    from PIL import Image
    HAS_QRCODE = True
except ImportError:
    HAS_QRCODE = False

# Try to import reportlab
try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
    from reportlab.lib import colors
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False


def generate_qr_code(data: str, size: int = 300) -> Optional[bytes]:
    """
    Generate QR code from data
    
    Args:
        data: Data to encode in QR code
        size: QR code size in pixels
    
    Returns:
        QR code image bytes (PNG) or None if qrcode not available
    """
    if not HAS_QRCODE:
        return None
    
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((size, size))
        
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        return buffer.getvalue()
    except Exception as e:
        st.error(f"Lỗi khi tạo QR code: {e}")
        return None


def generate_result_url(
    calculator_name: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any]
) -> str:
    """
    Generate shareable URL for results (for QR code)
    
    Args:
        calculator_name: Name of calculator
        inputs: Input values
        results: Results values
    
    Returns:
        URL string (can be used for QR code)
    """
    # Create a shareable data structure
    data = {
        "calculator": calculator_name,
        "timestamp": datetime.now().isoformat(),
        "inputs": inputs,
        "results": results
    }
    
    # Encode as base64 JSON (simplified approach)
    json_str = json.dumps(data, ensure_ascii=False, default=str)
    encoded = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    
    # Return a URL (in real app, this would be a shareable link)
    # For now, return the encoded data
    return f"clinical://result/{encoded}"


def format_result_for_export_enhanced(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str,
    include_timestamp: bool = True,
    include_qr_code: bool = False
) -> str:
    """
    Format calculator results for export (enhanced version)
    
    Args:
        title: Result title
        inputs: Input values dictionary
        results: Results dictionary
        calculator_name: Name of the calculator
        include_timestamp: Include timestamp in export
        include_qr_code: Include QR code data in export
    
    Returns:
        Formatted string ready for export
    """
    lines = []
    
    # Header
    lines.append("=" * 60)
    lines.append(f"Clinical Assistant - {calculator_name}")
    lines.append("=" * 60)
    if include_timestamp:
        lines.append(f"Ngày giờ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("-" * 60)
    
    # Title
    lines.append(f"\n{title}")
    lines.append("-" * 60)
    
    # Inputs
    if inputs:
        lines.append("\n📥 GIÁ TRỊ ĐẦU VÀO:")
        for key, value in inputs.items():
            lines.append(f"  • {key}: {value}")
    
    # Results
    if results:
        lines.append("\n📊 KẾT QUẢ:")
        for key, value in results.items():
            if isinstance(value, (dict, list)):
                lines.append(f"  • {key}:")
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        lines.append(f"    - {sub_key}: {sub_value}")
                else:
                    for item in value:
                        lines.append(f"    - {item}")
            else:
                lines.append(f"  • {key}: {value}")
    
    # QR Code data (if requested)
    if include_qr_code:
        lines.append("\n📱 QR CODE:")
        result_url = generate_result_url(calculator_name, inputs, results)
        lines.append(f"  Share URL: {result_url}")
        lines.append("  (Scan QR code để xem kết quả)")
    
    # Footer
    lines.append("\n" + "=" * 60)
    lines.append("⚠️ Lưu ý: Kết quả chỉ mang tính tham khảo")
    lines.append("   Không thay thế đánh giá lâm sàng của bác sĩ")
    lines.append("=" * 60)
    
    return "\n".join(lines)


def generate_pdf_enhanced(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str,
    include_qr_code: bool = True
) -> Optional[bytes]:
    """
    Generate enhanced PDF from calculator results with QR code
    
    Args:
        title: Result title
        inputs: Input values dictionary
        results: Results dictionary
        calculator_name: Name of the calculator
        include_qr_code: Include QR code in PDF
    
    Returns:
        PDF bytes or None if reportlab not available
    """
    if not HAS_REPORTLAB:
        return None
    
    try:
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer, 
            pagesize=A4, 
            topMargin=0.5*inch, 
            bottomMargin=0.5*inch,
            leftMargin=0.5*inch,
            rightMargin=0.5*inch
        )
        story = []
        styles = getSampleStyleSheet()
        
        # Title style
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#1976d2'),
            spaceAfter=12,
            alignment=1  # Center
        )
        
        # Header
        story.append(Paragraph(f"Clinical Assistant - {calculator_name}", title_style))
        story.append(Paragraph(
            f"Ngày giờ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
            styles['Normal']
        ))
        story.append(Spacer(1, 0.2*inch))
        
        # Title
        story.append(Paragraph(f"<b>{title}</b>", styles['Heading2']))
        story.append(Spacer(1, 0.1*inch))
        
        # Inputs section
        if inputs:
            story.append(Paragraph("<b>📥 GIÁ TRỊ ĐẦU VÀO:</b>", styles['Heading3']))
            input_data = [["Thông số", "Giá trị"]]
            for key, value in inputs.items():
                input_data.append([str(key), str(value)])
            
            input_table = Table(input_data, colWidths=[3*inch, 2*inch])
            input_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1976d2')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(input_table)
            story.append(Spacer(1, 0.2*inch))
        
        # Results section
        if results:
            story.append(Paragraph("<b>📊 KẾT QUẢ:</b>", styles['Heading3']))
            result_data = [["Kết quả", "Giá trị"]]
            for key, value in results.items():
                if isinstance(value, (dict, list)):
                    result_data.append([str(key), ""])
                    if isinstance(value, dict):
                        for sub_key, sub_value in value.items():
                            result_data.append([f"  • {sub_key}", str(sub_value)])
                    else:
                        for item in value:
                            result_data.append(["  •", str(item)])
                else:
                    result_data.append([str(key), str(value)])
            
            result_table = Table(result_data, colWidths=[3*inch, 2*inch])
            result_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4caf50')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(result_table)
            story.append(Spacer(1, 0.2*inch))
        
        # QR Code section
        if include_qr_code and HAS_QRCODE:
            story.append(Spacer(1, 0.3*inch))
            story.append(Paragraph("<b>📱 QR CODE:</b>", styles['Heading3']))
            story.append(Paragraph("Quét mã QR để xem kết quả", styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
            
            # Generate QR code
            result_url = generate_result_url(calculator_name, inputs, results)
            qr_bytes = generate_qr_code(result_url, size=200)
            
            if qr_bytes:
                # Save QR code to temporary file
                qr_buffer = BytesIO(qr_bytes)
                qr_image = RLImage(qr_buffer, width=1.5*inch, height=1.5*inch)
                story.append(qr_image)
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph(f"<i>{result_url}</i>", styles['Normal']))
        
        # Footer
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph(
            "⚠️ <i>Lưu ý: Kết quả chỉ mang tính tham khảo. Không thay thế đánh giá lâm sàng của bác sĩ.</i>", 
            styles['Normal']
        ))
        
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    except ImportError:
        return None
    except Exception as e:
        st.error(f"Lỗi khi tạo PDF: {e}")
        return None


def render_export_buttons_enhanced(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str,
    filename: Optional[str] = None,
    show_copy: bool = True,
    show_download_txt: bool = True,
    show_download_pdf: bool = True,
    show_qr_code: bool = True,
    show_email: bool = False  # Optional, requires email setup
) -> None:
    """
    Render enhanced export buttons with PDF, QR code, and email options
    
    Args:
        title: Result title
        inputs: Input values
        results: Results values
        calculator_name: Calculator name
        filename: Optional filename for download
        show_copy: Show copy button
        show_download_txt: Show download TXT button
        show_download_pdf: Show download PDF button
        show_qr_code: Show QR code button
        show_email: Show email button (optional)
    """
    if not inputs and not results:
        return
    
    # Format export text
    export_text = format_result_for_export_enhanced(
        title, inputs, results, calculator_name,
        include_timestamp=True,
        include_qr_code=False
    )
    
    # Count buttons
    num_buttons = sum([
        show_copy,
        show_download_txt,
        show_download_pdf,
        show_qr_code,
        show_email
    ])
    
    if num_buttons == 0:
        return
    
    # Create columns for buttons
    cols = st.columns(num_buttons)
    col_idx = 0
    
    # Copy button
    if show_copy:
        with cols[col_idx]:
            if st.button("📋 Copy", use_container_width=True, key="export_copy_enhanced"):
                st.code(export_text, language="text")
                st.success("✅ Đã copy! Chọn và copy từ khung trên")
        col_idx += 1
    
    # Download TXT button
    if show_download_txt:
        with cols[col_idx]:
            txt_filename = filename or f"{calculator_name.lower().replace(' ', '_')}_result"
            if not txt_filename.endswith('.txt'):
                txt_filename += '.txt'
            
            st.download_button(
                label="💾 Tải TXT",
                data=export_text,
                file_name=txt_filename,
                mime="text/plain",
                use_container_width=True,
                key="export_download_txt_enhanced"
            )
        col_idx += 1
    
    # Download PDF button
    if show_download_pdf:
        with cols[col_idx]:
            pdf_bytes = generate_pdf_enhanced(
                title, inputs, results, calculator_name,
                include_qr_code=True
            )
            if pdf_bytes:
                pdf_filename = filename or f"{calculator_name.lower().replace(' ', '_')}_result"
                if not pdf_filename.endswith('.pdf'):
                    pdf_filename += '.pdf'
                
                st.download_button(
                    label="📄 Tải PDF",
                    data=pdf_bytes,
                    file_name=pdf_filename,
                    mime="application/pdf",
                    use_container_width=True,
                    key="export_download_pdf_enhanced"
                )
            else:
                st.info("📄 PDF requires reportlab. Install: pip install reportlab")
        col_idx += 1
    
    # QR Code button
    if show_qr_code and HAS_QRCODE:
        with cols[col_idx]:
            result_url = generate_result_url(calculator_name, inputs, results)
            qr_bytes = generate_qr_code(result_url, size=300)
            
            if qr_bytes:
                # Display QR code
                with st.expander("📱 QR Code", expanded=False):
                    st.image(qr_bytes, caption="Quét mã QR để xem kết quả", use_container_width=True)
                    st.caption(f"**URL:** `{result_url}`")
                    
                    # Download QR code as image
                    qr_filename = filename or f"{calculator_name.lower().replace(' ', '_')}_qr"
                    if not qr_filename.endswith('.png'):
                        qr_filename += '.png'
                    
                    st.download_button(
                        label="💾 Tải QR Code",
                        data=qr_bytes,
                        file_name=qr_filename,
                        mime="image/png",
                        use_container_width=True,
                        key="export_download_qr_enhanced"
                    )
            else:
                st.info("📱 QR Code requires qrcode. Install: pip install qrcode Pillow")
        col_idx += 1
    
    # Email button (optional, requires email setup)
    if show_email:
        with cols[col_idx]:
            if st.button("📧 Gửi Email", use_container_width=True, key="export_email_enhanced"):
                st.info("📧 Tính năng gửi email cần cấu hình email server. Sắp có!")


def render_export_section_enhanced(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str,
    filename: Optional[str] = None,
    show_preview: bool = True,
    show_pdf: bool = True,
    show_qr_code: bool = True
) -> None:
    """
    Render complete enhanced export section with preview, PDF, and QR code
    
    Args:
        title: Result title
        inputs: Input values
        results: Results values
        calculator_name: Calculator name
        filename: Optional filename for download
        show_preview: Show preview of export text
        show_pdf: Show PDF export
        show_qr_code: Show QR code
    """
    export_text = format_result_for_export_enhanced(
        title, inputs, results, calculator_name,
        include_timestamp=True,
        include_qr_code=False
    )
    
    with st.expander("📤 Export Kết quả", expanded=False):
        if show_preview:
            st.markdown("**📋 Preview:**")
            st.code(export_text, language="text")
            st.markdown("---")
        
        # Export buttons
        render_export_buttons_enhanced(
            title=title,
            inputs=inputs,
            results=results,
            calculator_name=calculator_name,
            filename=filename,
            show_copy=True,
            show_download_txt=True,
            show_download_pdf=show_pdf,
            show_qr_code=show_qr_code,
            show_email=False
        )


def render_print_friendly_view(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str
) -> None:
    """
    Render print-friendly view with CSS for printing
    
    Args:
        title: Result title
        inputs: Input values
        results: Results values
        calculator_name: Calculator name
    """
    # Add print CSS
    st.markdown("""
    <style>
    @media print {
        .no-print {
            display: none !important;
        }
        .print-only {
            display: block !important;
        }
        body {
            font-size: 12pt;
            line-height: 1.5;
        }
        .print-header {
            border-bottom: 2px solid #1976d2;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .print-section {
            margin-bottom: 20px;
            page-break-inside: avoid;
        }
        .print-table {
            width: 100%;
            border-collapse: collapse;
        }
        .print-table th,
        .print-table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        .print-table th {
            background-color: #1976d2;
            color: white;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Print button
    st.markdown("""
    <div class="no-print">
        <button onclick="window.print()" style="
            padding: 10px 20px;
            background-color: #1976d2;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        ">
            🖨️ Print
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # Print-friendly content
    st.markdown(f"""
    <div class="print-only">
        <div class="print-header">
            <h1>Clinical Assistant - {calculator_name}</h1>
            <p>Ngày giờ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="print-section">
            <h2>{title}</h2>
        </div>
        
        <div class="print-section">
            <h3>📥 GIÁ TRỊ ĐẦU VÀO:</h3>
            <table class="print-table">
                <tr>
                    <th>Thông số</th>
                    <th>Giá trị</th>
                </tr>
    """, unsafe_allow_html=True)
    
    # Inputs table
    for key, value in inputs.items():
        st.markdown(f"""
        <tr>
            <td>{key}</td>
            <td>{value}</td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("""
            </table>
        </div>
        
        <div class="print-section">
            <h3>📊 KẾT QUẢ:</h3>
            <table class="print-table">
                <tr>
                    <th>Kết quả</th>
                    <th>Giá trị</th>
                </tr>
    """, unsafe_allow_html=True)
    
    # Results table
    for key, value in results.items():
        if isinstance(value, dict):
            st.markdown(f"""
            <tr>
                <td colspan="2"><strong>{key}</strong></td>
            </tr>
            """, unsafe_allow_html=True)
            for sub_key, sub_value in value.items():
                st.markdown(f"""
                <tr>
                    <td>&nbsp;&nbsp;• {sub_key}</td>
                    <td>{sub_value}</td>
                </tr>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <tr>
                <td>{key}</td>
                <td>{value}</td>
            </tr>
            """, unsafe_allow_html=True)
    
    st.markdown("""
            </table>
        </div>
        
        <div class="print-section">
            <p><em>⚠️ Lưu ý: Kết quả chỉ mang tính tham khảo. Không thay thế đánh giá lâm sàng của bác sĩ.</em></p>
        </div>
    </div>
    """, unsafe_allow_html=True)


__all__ = [
    'generate_qr_code',
    'generate_result_url',
    'format_result_for_export_enhanced',
    'generate_pdf_enhanced',
    'render_export_buttons_enhanced',
    'render_export_section_enhanced',
    'render_print_friendly_view',
]

