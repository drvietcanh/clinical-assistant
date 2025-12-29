"""
Scores Export Component
Export calculator results to PDF, CSV, and print
"""

import streamlit as st
from typing import Dict, Any, Optional, List
from datetime import datetime
from io import BytesIO
import csv


def format_score_result_for_text(
    calculator_name: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    specialty: Optional[str] = None
) -> str:
    """
    Format score result as text for export.
    
    Args:
        calculator_name: Name of calculator
        inputs: Input values
        results: Results dictionary
        specialty: Optional specialty name
    
    Returns:
        Formatted text string
    """
    lines = []
    lines.append("=" * 70)
    lines.append(f"CALCULATOR: {calculator_name}")
    if specialty:
        lines.append(f"CHUYÊN KHOA: {specialty}")
    lines.append(f"NGÀY GIỜ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 70)
    lines.append("")
    
    # Inputs
    if inputs:
        lines.append("📥 GIÁ TRỊ ĐẦU VÀO:")
        lines.append("-" * 70)
        for key, value in inputs.items():
            lines.append(f"  {key}: {value}")
        lines.append("")
    
    # Results
    if results:
        lines.append("📊 KẾT QUẢ:")
        lines.append("-" * 70)
        for key, value in results.items():
            if isinstance(value, dict):
                lines.append(f"  {key}:")
                for sub_key, sub_value in value.items():
                    lines.append(f"    - {sub_key}: {sub_value}")
            elif isinstance(value, list):
                lines.append(f"  {key}:")
                for item in value:
                    lines.append(f"    - {item}")
            else:
                lines.append(f"  {key}: {value}")
        lines.append("")
    
    lines.append("=" * 70)
    lines.append("Trợ lý lâm sàng - Medical Assistant")
    lines.append("=" * 70)
    
    return "\n".join(lines)


def export_to_csv(
    calculator_name: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    specialty: Optional[str] = None
) -> BytesIO:
    """
    Export score result to CSV format.
    
    Returns:
        BytesIO object with CSV data
    """
    output = BytesIO()
    
    # Flatten results for CSV
    csv_data = []
    
    # Add metadata
    csv_data.append(["Calculator", calculator_name])
    if specialty:
        csv_data.append(["Specialty", specialty])
    csv_data.append(["Date", datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    csv_data.append([])
    
    # Add inputs
    csv_data.append(["INPUTS"])
    for key, value in inputs.items():
        csv_data.append([key, value])
    csv_data.append([])
    
    # Add results
    csv_data.append(["RESULTS"])
    for key, value in results.items():
        if isinstance(value, (dict, list)):
            csv_data.append([key, str(value)])
        else:
            csv_data.append([key, value])
    
    # Write to CSV
    writer = csv.writer(output)
    writer.writerows(csv_data)
    
    output.seek(0)
    return output


def render_export_section(
    calculator_name: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    specialty: Optional[str] = None
):
    """
    Render export section with buttons for different export formats.
    
    Args:
        calculator_name: Name of calculator
        inputs: Input values
        results: Results dictionary
        specialty: Optional specialty name
    """
    st.markdown("---")
    st.subheader("📤 Xuất kết quả")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Copy to clipboard
        text_result = format_score_result_for_text(calculator_name, inputs, results, specialty)
        if st.button("📋 Copy", use_container_width=True, help="Copy kết quả vào clipboard"):
            st.code(text_result, language="text")
            st.success("✅ Đã copy vào clipboard! (Sử dụng Ctrl+C trên code block)")
    
    with col2:
        # Download as text
        text_result = format_score_result_for_text(calculator_name, inputs, results, specialty)
        st.download_button(
            label="💾 Download TXT",
            data=text_result,
            file_name=f"{calculator_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True,
            help="Tải về file text"
        )
    
    with col3:
        # Download as CSV
        csv_data = export_to_csv(calculator_name, inputs, results, specialty)
        st.download_button(
            label="📊 Download CSV",
            data=csv_data,
            file_name=f"{calculator_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True,
            help="Tải về file CSV"
        )
    
    # Print button
    st.markdown("---")
    if st.button("🖨️ In kết quả", use_container_width=True, help="Mở dialog in"):
        st.info("💡 Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in trang này")
        # Show printable version
        st.markdown("### 📄 Bản in")
        st.markdown(f"**Calculator:** {calculator_name}")
        if specialty:
            st.markdown(f"**Chuyên khoa:** {specialty}")
        st.markdown(f"**Ngày giờ:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.markdown("---")
        
        # Inputs
        if inputs:
            st.markdown("**📥 Giá trị đầu vào:**")
            for key, value in inputs.items():
                st.markdown(f"- {key}: {value}")
        
        # Results
        if results:
            st.markdown("**📊 Kết quả:**")
            for key, value in results.items():
                if isinstance(value, dict):
                    st.markdown(f"**{key}:**")
                    for sub_key, sub_value in value.items():
                        st.markdown(f"  - {sub_key}: {sub_value}")
                elif isinstance(value, list):
                    st.markdown(f"**{key}:**")
                    for item in value:
                        st.markdown(f"  - {item}")
                else:
                    st.markdown(f"- {key}: {value}")


def render_quick_export_button(
    calculator_name: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    specialty: Optional[str] = None
):
    """
    Render a quick export button in a compact format.
    """
    with st.expander("📤 Xuất kết quả", expanded=False):
        render_export_section(calculator_name, inputs, results, specialty)

