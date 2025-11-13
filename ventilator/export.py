"""
Ventilator Data Export - PHIÊN 5
Export lịch sử và báo cáo ra CSV, PDF
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from typing import List, Dict, Any
from io import BytesIO
import base64

from .history import get_history, get_history_dataframe


def export_history_to_csv() -> bytes:
    """
    Export lịch sử ra CSV
    
    Returns:
        CSV data as bytes
    """
    df = get_history_dataframe()
    
    if df.empty:
        return b""
    
    # Chuyển đổi sang CSV
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')  # utf-8-sig để Excel đọc được tiếng Việt
    csv_data = csv_buffer.getvalue()
    csv_buffer.close()
    
    return csv_data


def generate_csv_download_link(csv_data: bytes, filename: str = None) -> str:
    """
    Tạo download link cho CSV
    
    Args:
        csv_data: Dữ liệu CSV dạng bytes
        filename: Tên file (optional)
    
    Returns:
        HTML download link
    """
    if filename is None:
        filename = f"ventilator_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    b64 = base64.b64encode(csv_data).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">📥 Tải xuống CSV</a>'
    return href


def format_report_text(history: List[Dict[str, Any]]) -> str:
    """
    Format báo cáo dạng text
    
    Args:
        history: Danh sách entries
    
    Returns:
        Báo cáo dạng text
    """
    if not history:
        return "Không có dữ liệu"
    
    report = []
    report.append("=" * 80)
    report.append("BÁO CÁO LỊCH SỬ MÁY THỞ")
    report.append("=" * 80)
    report.append(f"Ngày tạo: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    report.append(f"Tổng số entries: {len(history)}")
    report.append("")
    
    # Thông tin từng entry
    for i, entry in enumerate(history, 1):
        report.append("-" * 80)
        report.append(f"Entry {i} - {entry['timestamp'].strftime('%d/%m/%Y %H:%M:%S')}")
        report.append("-" * 80)
        
        # Thông số máy thở
        report.append("Thông số máy thở:")
        vent = entry['vent_settings']
        report.append(f"  - Mode: {vent.get('mode', 'N/A')}")
        report.append(f"  - Vt: {vent.get('vt', 0)} mL")
        report.append(f"  - RR: {vent.get('rr', 0)} /phút")
        report.append(f"  - PEEP: {vent.get('peep', 0)} cmH2O")
        report.append(f"  - FiO₂: {vent.get('fio2', 0)}%")
        report.append(f"  - Plateau: {vent.get('plateau', 0)} cmH2O")
        if vent.get('peak', 0) > 0:
            report.append(f"  - Peak: {vent.get('peak', 0)} cmH2O")
        
        # ABG
        report.append("")
        report.append("ABG:")
        abg = entry['abg_data']
        if abg.get('ph'):
            report.append(f"  - pH: {abg.get('ph', 0):.2f}")
        if abg.get('po2'):
            report.append(f"  - PaO₂: {abg.get('po2', 0):.1f} mmHg")
        if abg.get('pco2'):
            report.append(f"  - PaCO₂: {abg.get('pco2', 0):.1f} mmHg")
        if abg.get('hco3'):
            report.append(f"  - HCO₃⁻: {abg.get('hco3', 0):.1f} mmol/L")
        
        # Tính toán
        report.append("")
        report.append("Kết quả tính toán:")
        calc = entry['calculations']
        if calc.get('pf_ratio'):
            report.append(f"  - P/F Ratio: {calc.get('pf_ratio', 0):.0f}")
        if calc.get('driving_pressure') is not None:
            report.append(f"  - Driving Pressure: {calc.get('driving_pressure', 0):.1f} cmH2O")
        if calc.get('compliance'):
            report.append(f"  - Compliance: {calc.get('compliance', 0):.1f} mL/cmH2O")
        if calc.get('vt_per_kg'):
            report.append(f"  - Vt/kg: {calc.get('vt_per_kg', 0):.2f} mL/kg")
        
        # Ghi chú
        if entry.get('notes'):
            report.append("")
            report.append(f"Ghi chú: {entry['notes']}")
        
        report.append("")
    
    report.append("=" * 80)
    
    return "\n".join(report)


def export_report_to_text() -> str:
    """
    Export báo cáo dạng text
    
    Returns:
        Báo cáo dạng text
    """
    history = get_history()
    return format_report_text(history)


def generate_text_download_link(text: str, filename: str = None) -> str:
    """
    Tạo download link cho text file
    
    Args:
        text: Nội dung text
        filename: Tên file (optional)
    
    Returns:
        HTML download link
    """
    if filename is None:
        filename = f"ventilator_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    b64 = base64.b64encode(text.encode('utf-8')).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Tải xuống TXT</a>'
    return href


def render_export_panel():
    """Hiển thị panel export dữ liệu"""
    history = get_history()
    
    if not history:
        st.info("📝 Chưa có dữ liệu. Tính toán và lưu để export.")
        return
    
    st.markdown("### 📤 Export Dữ Liệu")
    
    st.info(f"""
    **📊 Dữ liệu hiện có:**
    - Tổng số entries: **{len(history)}**
    - Thời gian: {history[0]['timestamp'].strftime('%d/%m/%Y %H:%M:%S')} → {history[-1]['timestamp'].strftime('%d/%m/%Y %H:%M:%S')}
    """)
    
    st.markdown("---")
    
    # Export CSV
    st.markdown("#### 📊 Export CSV")
    st.caption("Export lịch sử dạng bảng CSV (có thể mở bằng Excel)")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("File CSV chứa tất cả thông số theo thời gian")
    with col2:
        csv_data = export_history_to_csv()
        if csv_data:
            filename = f"ventilator_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            st.download_button(
                label="📥 Tải CSV",
                data=csv_data,
                file_name=filename,
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.warning("Không có dữ liệu")
    
    st.markdown("---")
    
    # Export Text Report
    st.markdown("#### 📄 Export Báo Cáo Text")
    st.caption("Export báo cáo chi tiết dạng text")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("File text chứa báo cáo chi tiết từng entry")
    with col2:
        report_text = export_report_to_text()
        if report_text:
            filename = f"ventilator_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            st.download_button(
                label="📥 Tải TXT",
                data=report_text,
                file_name=filename,
                mime="text/plain",
                use_container_width=True
            )
        else:
            st.warning("Không có dữ liệu")
    
    st.markdown("---")
    
    # Preview
    st.markdown("#### 👁️ Xem Trước Dữ Liệu")
    
    preview_type = st.radio(
        "Chọn loại preview:",
        ["Bảng CSV", "Báo cáo Text"],
        horizontal=True,
        key="export_preview_type"
    )
    
    if preview_type == "Bảng CSV":
        df = get_history_dataframe()
        if not df.empty:
            st.dataframe(df, use_container_width=True, height=300)
        else:
            st.info("Không có dữ liệu")
    
    else:  # Báo cáo Text
        report_text = export_report_to_text()
        if report_text:
            st.text_area(
                "Nội dung báo cáo:",
                value=report_text,
                height=400,
                disabled=True
            )
        else:
            st.info("Không có dữ liệu")
    
    st.markdown("---")
    
    # Thông tin thêm
    with st.expander("ℹ️ Thông Tin Export"):
        st.markdown("""
        **CSV Format:**
        - Encoding: UTF-8 with BOM (Excel compatible)
        - Separator: Comma (,)
        - Có thể mở trực tiếp bằng Excel, Google Sheets
        
        **Text Report Format:**
        - Encoding: UTF-8
        - Format: Plain text với cấu trúc rõ ràng
        - Phù hợp để in hoặc lưu trữ
        
        **Lưu ý:**
        - Dữ liệu được export từ session hiện tại
        - Nếu refresh trang, dữ liệu sẽ mất (trừ khi đã lưu)
        - Khuyến nghị export thường xuyên để backup
        """)

