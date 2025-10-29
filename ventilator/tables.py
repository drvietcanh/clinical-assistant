"""
Ventilator Reference Tables
PEEP/FiO2 combinations and other reference data
"""

import streamlit as st
import pandas as pd


def render_peep_fio2_table():
    """ARDSNet PEEP/FiO2 Table"""
    st.subheader("📊 Bảng PEEP/FiO2 - ARDSNet")
    st.caption("Lower PEEP/Higher FiO2 Strategy")
    
    st.markdown("### 🎯 Mục Tiêu Oxy Hóa")
    st.info("""
    **Target oxygenation:**
    - SpO2: 88-95%
    - PaO2: 55-80 mmHg
    """)
    
    st.markdown("---")
    
    # Create PEEP/FiO2 table
    peep_fio2_data = {
        "FiO2": [0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.7, 0.7, 0.7, 0.8, 0.9, 0.9, 0.9, 1.0, 1.0, 1.0, 1.0],
        "PEEP": [5, 5, 8, 8, 10, 10, 10, 12, 14, 14, 14, 16, 18, 18, 20, 22, 24]
    }
    
    df = pd.DataFrame(peep_fio2_data)
    
    st.markdown("### 📋 Bảng Lower PEEP Strategy")
    
    # Display as a nicer table
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Phần 1")
        st.dataframe(
            df.head(9).style.highlight_max(axis=0, color='lightgreen'),
            hide_index=True,
            use_container_width=True
        )
    
    with col2:
        st.markdown("#### Phần 2")
        st.dataframe(
            df.tail(8).style.highlight_max(axis=0, color='lightcoral'),
            hide_index=True,
            use_container_width=True
        )
    
    st.markdown("---")
    
    st.markdown("### 💡 Hướng Dẫn Sử Dụng")
    
    st.success("""
    **Cách điều chỉnh:**
    
    1. **Nếu SpO2 < 88% hoặc PaO2 < 55 mmHg:**
       - Tăng FiO2 và PEEP theo bảng (đi xuống)
       - Ví dụ: Từ FiO2 0.4/PEEP 5 → FiO2 0.4/PEEP 8
    
    2. **Nếu SpO2 > 95% hoặc PaO2 > 80 mmHg:**
       - Giảm FiO2 và PEEP theo bảng (đi lên)
       - Ưu tiên giảm FiO2 trước
    
    3. **Điều chỉnh từng bước:**
       - Không nhảy cóc
       - Theo dõi sau mỗi thay đổi
       - Đợi ít nhất 30 phút trước khi đánh giá lại
    """)
    
    st.warning("""
    **⚠️ Lưu ý:**
    - PEEP tối đa: 24 cmH2O
    - Luôn kiểm tra Plateau Pressure ≤30 cmH2O
    - Theo dõi huyết động sau khi tăng PEEP
    - Cân nhắc recruitment maneuver nếu PEEP cao
    """)
    
    st.markdown("---")
    
    # Alternative: Higher PEEP table
    with st.expander("📊 Bảng Higher PEEP Strategy (Tham Khảo)"):
        st.info("""
        **Higher PEEP/Lower FiO2 Strategy:**
        
        Một số nghiên cứu gợi ý Higher PEEP có thể tốt hơn ở một số bệnh nhân ARDS.
        """)
        
        higher_peep_data = {
            "FiO2": [0.3, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0],
            "PEEP": [5, 8, 10, 10, 12, 12, 14, 16, 16, 16, 16, 16, 20, 24]
        }
        
        df_higher = pd.DataFrame(higher_peep_data)
        st.dataframe(df_higher, hide_index=True, use_container_width=True)
    
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown("""
        **ARDSNet PEEP/FiO2 Table**
        
        **Reference:**
        - ARDSNet. Ventilation with lower tidal volumes. NEJM 2000.
        - ALVEOLI Trial. Higher vs lower PEEP. NEJM 2004.
        
        **Guidelines:**
        - Surviving Sepsis Campaign
        - ATS/ERS Clinical Practice Guidelines
        
        **Chú ý:**
        - Lower PEEP strategy là strategy mặc định trong ARDSNet protocol
        - Higher PEEP có thể cân nhắc ở ARDS nặng với P/F ratio rất thấp
        - Luôn cá thể hóa theo đáp ứng lâm sàng
        """)

