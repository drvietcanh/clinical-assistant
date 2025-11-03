"""
Export Results Component
Copy to clipboard and download text functionality for calculator results
"""

import streamlit as st
from typing import Optional, Dict, Any


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


def render_export_buttons(
    export_text: str,
    filename: Optional[str] = None,
    button_label_copy: str = "📋 Copy",
    button_label_download: str = "💾 Download",
    show_copy: bool = True,
    show_download: bool = True
) -> None:
    """
    Render export buttons (copy and download)
    
    Args:
        export_text: Text to export
        filename: Filename for download (without extension)
        button_label_copy: Label for copy button
        button_label_download: Label for download button
        show_copy: Show copy button
        show_download: Show download button
    """
    if not export_text:
        return
    
    col1, col2 = st.columns(2)
    
    # Copy button
    if show_copy:
        with col1:
            if st.button(button_label_copy, use_container_width=True, key="export_copy"):
                try:
                    # Streamlit's copy to clipboard (requires streamlit-clipboard or manual implementation)
                    # For now, we'll use a workaround with download or text area
                    st.code(export_text, language="text")
                    st.success("✅ Đã copy! Bạn có thể chọn và copy từ khung trên")
                except Exception as e:
                    st.error(f"Lỗi khi copy: {e}")
    
    # Download button
    if show_download:
        with col2:
            filename = filename or "clinical_result"
            if not filename.endswith('.txt'):
                filename += '.txt'
            
            st.download_button(
                label=button_label_download,
                data=export_text,
                file_name=filename,
                mime="text/plain",
                use_container_width=True,
                key="export_download"
            )


def render_export_section(
    title: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    calculator_name: str,
    filename: Optional[str] = None,
    show_preview: bool = True
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
    """
    export_text = format_result_for_export(title, inputs, results, calculator_name)
    
    with st.expander("📤 Export Kết Quả", expanded=False):
        if show_preview:
            st.markdown("**Preview:**")
            st.code(export_text, language="text")
            st.markdown("---")
        
        render_export_buttons(
            export_text=export_text,
            filename=filename,
            show_copy=True,
            show_download=True
        )


__all__ = [
    'format_result_for_export',
    'render_export_buttons',
    'render_export_section',
]

