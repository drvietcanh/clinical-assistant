"""
Export Results Component
Copy to clipboard, download text, PDF export, and batch export functionality
"""

import streamlit as st
from typing import Optional, Dict, Any, List
from io import BytesIO
from datetime import datetime
import re


def _sanitize_key_prefix(prefix: str) -> str:
    """
    Sanitize a string to be used as a Streamlit key prefix.
    Streamlit keys can only contain alphanumeric characters, underscores, and hyphens.
    
    Args:
        prefix: String to sanitize
        
    Returns:
        Sanitized string safe for use as Streamlit key
    """
    if not prefix:
        return "export"
    
    # Convert to lowercase
    prefix = prefix.lower()
    
    # Replace spaces and common separators with underscores
    prefix = re.sub(r'[\s/\\\-]+', '_', prefix)
    
    # Remove all characters that are not alphanumeric, underscore, or hyphen
    prefix = re.sub(r'[^a-z0-9_-]', '', prefix)
    
    # Remove leading/trailing underscores and hyphens
    prefix = prefix.strip('_-')
    
    # Ensure it's not empty and not too long (Streamlit has key length limits)
    if not prefix:
        prefix = "export"
    elif len(prefix) > 50:
        prefix = prefix[:50]
    
    return prefix


def format_result_for_export(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str,
    include_timestamp: bool = True
) -> str:
    """
    Format calculator results for export
    
    Args:
        title: Result title
        inputs: Input values dictionary
        results: Results dictionary
        calculator_name: Name of the calculator
        include_timestamp: Include timestamp in export
    
    Returns:
        Formatted string ready for export
    """
    from datetime import datetime
    
    lines = []
    
    # Header
    lines.append("=" * 60)
    lines.append(f"Trợ lý lâm sàng - {calculator_name}")
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
                for sub_key, sub_value in (value.items() if isinstance(value, dict) else enumerate(value)):
                    lines.append(f"    - {sub_key}: {sub_value}")
            else:
                lines.append(f"  • {key}: {value}")
    
    # Footer
    lines.append("\n" + "=" * 60)
    lines.append("⚠️ Lưu ý: Kết quả chỉ mang tính tham khảo")
    lines.append("   Không thay thế đánh giá lâm sàng của bác sĩ")
    lines.append("=" * 60)
    
    return "\n".join(lines)


def generate_pdf(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str
) -> bytes:
    """
    Generate PDF from calculator results
    
    Args:
        title: Result title
        inputs: Input values dictionary
        results: Results dictionary
        calculator_name: Name of the calculator
    
    Returns:
        PDF bytes
    """
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
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
        story.append(Paragraph(f"Trợ lý lâm sàng - {calculator_name}", title_style))
        story.append(Paragraph(f"Ngày giờ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
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
        
        # Footer
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph("⚠️ <i>Lưu ý: Kết quả chỉ mang tính tham khảo. Không thay thế đánh giá lâm sàng của bác sĩ.</i>", styles['Normal']))
        
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    except ImportError:
        # If reportlab is not installed, return None
        return None
    except Exception as e:
        st.error(f"Lỗi khi tạo PDF: {e}")
        return None


def render_export_buttons(
    export_text: str,
    filename: Optional[str] = None,
    title: Optional[str] = None,
    inputs: Optional[Dict[str, Any]] = None,
    results: Optional[Dict[str, Any]] = None,
    calculator_name: Optional[str] = None,
    button_label_copy: str = "📋 Copy",
    button_label_download: str = "💾 Tải TXT",
    button_label_pdf: str = "📄 Tải PDF",
    show_copy: bool = True,
    show_download: bool = True,
    show_pdf: bool = True,
    key_prefix: Optional[str] = None
) -> None:
    """
    Render export buttons (copy, download TXT, and PDF)
    
    Args:
        export_text: Text to export
        filename: Filename for download (without extension)
        title: Result title (for PDF)
        inputs: Input values (for PDF)
        results: Results values (for PDF)
        calculator_name: Calculator name (for PDF)
        button_label_copy: Label for copy button
        button_label_download: Label for download button
        button_label_pdf: Label for PDF button
        show_copy: Show copy button
        show_download: Show download button
        show_pdf: Show PDF button
        key_prefix: Optional prefix for unique button keys (prevents duplicate key errors)
    """
    if not export_text:
        return
    
    # Generate unique key prefix if not provided
    if key_prefix is None:
        if calculator_name:
            # Use calculator name as prefix, sanitized for use as key
            key_prefix = _sanitize_key_prefix(str(calculator_name))
        elif title:
            # Use title hash as prefix
            import hashlib
            key_prefix = hashlib.md5(str(title).encode()).hexdigest()[:8]
        else:
            # Fallback to timestamp-based prefix
            import time
            key_prefix = f"export_{int(time.time() * 1000) % 100000}"
    
    # Ensure key_prefix is always a valid string
    if not key_prefix or not isinstance(key_prefix, str):
        key_prefix = "export"
    else:
        key_prefix = _sanitize_key_prefix(str(key_prefix))
    
    # Ensure key_prefix is sanitized even if provided
    key_prefix = _sanitize_key_prefix(key_prefix)
    
    num_cols = sum([show_copy, show_download, show_pdf])
    if num_cols == 0:
        return
    
    cols = st.columns(num_cols)
    col_idx = 0
    
    # Copy button
    if show_copy:
        with cols[col_idx]:
            if st.button(button_label_copy, use_container_width=True, key=f"{key_prefix}_export_copy"):
                try:
                    st.code(export_text, language="text")
                    st.success("✅ Đã copy! Bạn có thể chọn và copy từ khung trên")
                except Exception as e:
                    st.error(f"Lỗi khi copy: {e}")
        col_idx += 1
    
    # Download TXT button
    if show_download:
        with cols[col_idx]:
            txt_filename = filename or "clinical_result"
            if not txt_filename.endswith('.txt'):
                txt_filename += '.txt'
            
            st.download_button(
                label=button_label_download,
                data=export_text,
                file_name=txt_filename,
                mime="text/plain",
                use_container_width=True,
                key=f"{key_prefix}_export_download"
            )
        col_idx += 1
    
    # Download PDF button
    if show_pdf and title and inputs is not None and results is not None and calculator_name:
        with cols[col_idx]:
            pdf_bytes = generate_pdf(title, inputs, results, calculator_name)
            if pdf_bytes:
                pdf_filename = filename or "clinical_result"
                if not pdf_filename.endswith('.pdf'):
                    pdf_filename += '.pdf'
                
                st.download_button(
                    label=button_label_pdf,
                    data=pdf_bytes,
                    file_name=pdf_filename,
                    mime="application/pdf",
                    use_container_width=True,
                    key=f"{key_prefix}_export_pdf"
                )
            else:
                st.info("📄 PDF export requires reportlab library. Install with: pip install reportlab")


def render_export_section(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str,
    filename: Optional[str] = None,
    show_preview: bool = True,
    show_pdf: bool = True,
    key_prefix: Optional[str] = None
) -> None:
    """
    Render complete export section with preview and buttons
    
    Args:
        title: Result title
        inputs: Input values
        results: Results values
        calculator_name: Calculator name
        filename: Optional filename for download
        show_preview: Show preview of export text
        show_pdf: Show PDF export button
        key_prefix: Optional prefix for unique button keys (prevents duplicate key errors)
    """
    import hashlib
    
    export_text = format_result_for_export(title, inputs, results, calculator_name)
    
    # Generate unique key prefix if not provided
    if key_prefix is None:
        # Use calculator name as prefix, sanitized for use as key
        if calculator_name:
            key_prefix = _sanitize_key_prefix(str(calculator_name))
        else:
            key_prefix = "export"
    else:
        # Ensure key_prefix is sanitized even if provided
        key_prefix = _sanitize_key_prefix(str(key_prefix))
    
    # Add hash of title + inputs to ensure uniqueness when same calculator is called multiple times
    # This prevents duplicate key errors when the same calculator renders multiple results
    # Include inputs in hash to ensure uniqueness even when title is the same
    unique_data = f"{title}_{str(sorted(inputs.items()))}"
    unique_hash = hashlib.md5(unique_data.encode()).hexdigest()[:8]
    unique_key = f"{key_prefix}_{unique_hash}"
    
    # Limit length to avoid issues (Streamlit keys should be reasonable length)
    if len(unique_key) > 50:
        unique_key = unique_key[:50]
    
    # Final safety check - ensure unique_key is never empty and is a valid string
    if not unique_key or not isinstance(unique_key, str):
        unique_key = "export"
    
    # Construct the final key for the expander (hash is already alphanumeric, so safe)
    expander_key = f"{unique_key}_export_expander"
    
    # Final validation - ensure key doesn't exceed reasonable length
    if len(expander_key) > 100:
        # Truncate but keep the suffix
        prefix_len = 100 - len("_export_expander")
        expander_key = unique_key[:prefix_len] + "_export_expander"
    
    with st.expander("📤 Export Kết quả", expanded=False, key=expander_key):
        if show_preview:
            st.markdown("**Preview:**")
            st.code(export_text, language="text")
            st.markdown("---")
        
        render_export_buttons(
            export_text=export_text,
            filename=filename,
            title=title,
            inputs=inputs,
            results=results,
            calculator_name=calculator_name,
            show_copy=True,
            show_download=True,
            show_pdf=show_pdf,
            key_prefix=unique_key
        )


def render_batch_export(
    calculations: List[Dict[str, Any]],
    filename: Optional[str] = None,
    key_prefix: Optional[str] = None
) -> None:
    """
    Render batch export for multiple calculations
    
    Args:
        calculations: List of calculation dictionaries, each with:
            - title: Result title
            - inputs: Input values dict
            - results: Results values dict
            - calculator_name: Calculator name
        filename: Optional filename for batch export
        key_prefix: Optional prefix for unique button keys (prevents duplicate key errors)
    """
    if not calculations:
        st.warning("Không có kết quả nào để export")
        return
    
    # Generate unique key prefix if not provided
    if key_prefix is None:
        import time
        key_prefix = f"batch_export_{int(time.time() * 1000) % 100000}"
    
    # Ensure key_prefix is sanitized even if provided
    key_prefix = _sanitize_key_prefix(key_prefix)
    
    with st.expander("📦 Batch Export - Xuất Nhiều Kết quả", expanded=False, key=f"{key_prefix}_batch_expander"):
        st.info(f"📊 Tổng số: {len(calculations)} kết quả")
        
        # Format all calculations
        all_texts = []
        for i, calc in enumerate(calculations, 1):
            text = format_result_for_export(
                calc.get('title', f'Kết quả {i}'),
                calc.get('inputs', {}),
                calc.get('results', {}),
                calc.get('calculator_name', 'Không xác định'),
                include_timestamp=(i == 1)  # Only include timestamp in first
            )
            all_texts.append(text)
            if i < len(calculations):
                all_texts.append("\n" + "="*60 + "\n")
        
        batch_text = "\n".join(all_texts)
        
        # Preview
        st.markdown("**Preview (first 500 chars):**")
        st.code(batch_text[:500] + "..." if len(batch_text) > 500 else batch_text, language="text")
        st.markdown("---")
        
        # Export buttons
        col1, col2 = st.columns(2)
        
        with col1:
            batch_filename = filename or f"batch_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            if not batch_filename.endswith('.txt'):
                batch_filename += '.txt'
            
            st.download_button(
                label="💾 Download Tất Cả (TXT)",
                data=batch_text,
                file_name=batch_filename,
                mime="text/plain",
                use_container_width=True,
                key=f"{key_prefix}_batch_export_txt"
            )
        
        with col2:
            # Generate combined PDF
            try:
                from reportlab.lib.pagesizes import A4
                from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
                from reportlab.lib.units import inch
                from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
                from reportlab.lib import colors
                
                buffer = BytesIO()
                doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
                story = []
                styles = getSampleStyleSheet()
                
                title_style = ParagraphStyle(
                    'CustomTitle',
                    parent=styles['Heading1'],
                    fontSize=18,
                    textColor=colors.HexColor('#1976d2'),
                    spaceAfter=12,
                    alignment=1
                )
                
                story.append(Paragraph("Trợ lý lâm sàng - Xuất hàng loạt", title_style))
                story.append(Paragraph(f"Ngày giờ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
                story.append(Paragraph(f"Tổng số: {len(calculations)} kết quả", styles['Normal']))
                story.append(Spacer(1, 0.3*inch))
                
                for i, calc in enumerate(calculations, 1):
                    if i > 1:
                        story.append(PageBreak())
                    
                    story.append(Paragraph(f"<b>{calc.get('title', f'Kết quả {i}')}</b>", styles['Heading2']))
                    story.append(Paragraph(f"Calculator: {calc.get('calculator_name', 'Không xác định')}", styles['Normal']))
                    story.append(Spacer(1, 0.1*inch))
                    
                    # Add inputs and results (simplified for batch)
                    inputs = calc.get('inputs', {})
                    if inputs:
                        story.append(Paragraph("<b>Inputs:</b>", styles['Heading3']))
                        for key, value in inputs.items():
                            story.append(Paragraph(f"• {key}: {value}", styles['Normal']))
                    
                    results = calc.get('results', {})
                    if results:
                        story.append(Spacer(1, 0.1*inch))
                        story.append(Paragraph("<b>Results:</b>", styles['Heading3']))
                        for key, value in results.items():
                            if isinstance(value, dict):
                                story.append(Paragraph(f"• {key}:", styles['Normal']))
                                for sub_key, sub_value in value.items():
                                    story.append(Paragraph(f"  - {sub_key}: {sub_value}", styles['Normal']))
                            else:
                                story.append(Paragraph(f"• {key}: {value}", styles['Normal']))
                
                doc.build(story)
                buffer.seek(0)
                pdf_bytes = buffer.getvalue()
                
                pdf_filename = filename or f"batch_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                if not pdf_filename.endswith('.pdf'):
                    pdf_filename += '.pdf'
                
                st.download_button(
                    label="📄 Download Tất Cả (PDF)",
                    data=pdf_bytes,
                    file_name=pdf_filename,
                    mime="application/pdf",
                    use_container_width=True,
                    key=f"{key_prefix}_batch_export_pdf"
                )
            except ImportError:
                st.info("📄 PDF export requires reportlab. Install: pip install reportlab")
            except Exception as e:
                st.error(f"Lỗi tạo PDF: {e}")


__all__ = [
    'format_result_for_export',
    'render_export_buttons',
    'render_export_section',
    'generate_pdf',
    'render_batch_export',
]

