"""
Ventilator Calculators
ARDSNet and initial ventilator settings
"""

import streamlit as st


def render_ardsnet():
    """ARDSNet Tidal Volume Calculator"""
    st.subheader("🫁 ARDSNet - Tidal Volume")
    st.caption("Lung-Protective Ventilation Strategy")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="ardsnet_sex"
        )
        
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=100,
            max_value=220,
            value=170,
            step=1,
            help="Chiều cao thực tế của bệnh nhân"
        )
        
        st.markdown("---")
        st.markdown("### ⚙️ Tham Số Máy Thở Hiện Tại")
        
        current_vt = st.number_input(
            "Vt hiện tại (mL)",
            min_value=0,
            max_value=1000,
            value=0,
            step=10,
            help="Để trống nếu chưa đặt máy thở"
        )
        
        if st.button("🧮 Tính ARDSNet", type="primary", key="ardsnet_calc"):
            # Calculate PBW (Predicted Body Weight)
            if sex == "Nam":
                pbw = 50 + 0.91 * (height - 152.4)
            else:  # Nữ
                pbw = 45.5 + 0.91 * (height - 152.4)
            
            pbw = round(pbw, 1)
            
            # Calculate target Vt (6-8 mL/kg PBW)
            vt_low = pbw * 6
            vt_target = pbw * 6  # Start at 6 mL/kg
            vt_high = pbw * 8
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                st.metric("PBW", f"{pbw} kg")
                st.metric("Vt Mục Tiêu", f"{vt_target:.0f} mL")
                
                st.info(f"""
                **Khoảng an toàn:**
                - Min: {vt_low:.0f} mL (6 mL/kg)
                - Max: {vt_high:.0f} mL (8 mL/kg)
                """)
            
            st.markdown("### 💡 Khuyến Cáo")
            
            if current_vt > 0:
                if current_vt > vt_high:
                    st.error(f"""
                    ⚠️ **Vt hiện tại QUÁ CAO!**
                    
                    - Hiện tại: {current_vt} mL
                    - Mục tiêu: {vt_target:.0f} mL
                    - Giảm: {current_vt - vt_target:.0f} mL
                    
                    **Hành động:**
                    - Giảm Vt từ từ (50-100 mL mỗi lần)
                    - Theo dõi pH, PaCO2
                    - Cho phép hypercapnia nếu cần
                    """)
                elif current_vt < vt_low:
                    st.warning(f"""
                    ⚠️ **Vt hiện tại thấp**
                    
                    - Hiện tại: {current_vt} mL
                    - Mục tiêu: {vt_target:.0f} mL
                    - Có thể tăng thêm: {vt_target - current_vt:.0f} mL
                    """)
                else:
                    st.success(f"""
                    ✅ **Vt trong khoảng an toàn**
                    
                    - Hiện tại: {current_vt} mL
                    - Mục tiêu: {vt_target:.0f} mL
                    - Tiếp tục theo dõi
                    """)
            
            st.markdown("---")
            st.markdown("### 📋 ARDSNet Protocol")
            
            st.info(f"""
            **Thông số khởi đầu:**
            - **Vt:** {vt_target:.0f} mL (6 mL/kg PBW)
            - **RR:** 20-35 (điều chỉnh theo pH)
            - **PEEP/FiO2:** Theo bảng PEEP/FiO2
            - **I:E:** 1:1 đến 1:3
            
            **Mục tiêu:**
            - **Plateau Pressure:** ≤30 cmH2O
            - **pH:** 7.30-7.45
            - **SpO2:** 88-95%
            - **PaO2:** 55-80 mmHg
            """)
            
            st.warning("""
            **⚠️ Lưu ý:**
            - Ưu tiên giới hạn áp lực
            - Cho phép hypercapnia (pH ≥7.15)
            - Điều chỉnh PEEP theo bảng
            - Theo dõi sát compliance, driving pressure
            """)
            
            with st.expander("📐 Công Thức PBW"):
                st.markdown(f"""
                **Predicted Body Weight (PBW):**
                
                **Nam:**
                ```
                PBW = 50 + 0.91 × (Height - 152.4)
                    = 50 + 0.91 × ({height} - 152.4)
                    = {pbw} kg
                ```
                
                **Nữ:**
                ```
                PBW = 45.5 + 0.91 × (Height - 152.4)
                ```
                
                **Target Vt:**
                ```
                Vt = 6 mL/kg × PBW
                   = 6 × {pbw}
                   = {vt_target:.0f} mL
                ```
                
                **Reference:**
                ARDSNet. Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and the acute respiratory distress syndrome. N Engl J Med. 2000;342(18):1301-1308.
                """)


def render_initial_settings():
    """Initial Ventilator Settings Calculator"""
    st.subheader("⚙️ Cài Đặt Ban Đầu Máy Thở")
    st.caption("Thông Số Khởi Đầu Theo Bệnh Lý")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2")
    
    st.info("""
    **Cài đặt máy thở theo bệnh lý:**
    - ARDS/ALI
    - COPD
    - Asthma
    - Normal lungs
    - Neuromuscular
    
    **Thông số bao gồm:**
    - Mode (AC/VC, SIMV, PSV...)
    - Vt, RR, PEEP, FiO2
    - I:E ratio
    - Trigger sensitivity
    """)

