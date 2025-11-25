"""
VAS - Visual Analogue Scale
Thang đo thị giác đánh giá đau
"""

import streamlit as st


def render():
    """VAS Pain Scale Calculator"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>📏 VAS - Visual Analogue Scale</h2>
    <p style='text-align: center;'><em>Thang đo thị giác đánh giá đau (0-100mm)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **VAS (Visual Analogue Scale)** là thang đo đau bằng đường thẳng 100mm.
        
        **Ưu điểm:**
        - Nhạy cảm với thay đổi nhỏ
        - Phù hợp cho nghiên cứu
        - Không bị giới hạn bởi số nguyên
        
        **Nhược điểm:**
        - Cần thước đo
        - Khó dùng cho bệnh nhân già, rối loạn thị giác
        
        **Sử dụng:**
        - Đánh giá đau cấp tính và mạn tính
        - Nghiên cứu lâm sàng
        - Theo dõi đáp ứng điều trị
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh Giá Đau")
    
    # Visual scale display
    st.markdown("### 📊 Thang Đo VAS (100mm)")
    
    # Create visual scale
    vas_value = st.slider(
        "Đánh dấu mức độ đau trên thang đo (0-100mm):",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        help="0mm = Không đau, 100mm = Đau dữ dội nhất"
    )
    
    # Visual representation
    scale_width = 600
    marker_pos = (vas_value / 100) * scale_width
    
    scale_html = f"""
    <div style='margin: 20px 0; padding: 20px; background: #f9fafb; border-radius: 10px;'>
        <div style='position: relative; width: {scale_width}px; margin: 0 auto;'>
            <!-- Scale line -->
            <div style='width: 100%; height: 4px; background: linear-gradient(to right, #10b981 0%, #fbbf24 50%, #ef4444 100%); 
                        border-radius: 2px; position: relative;'>
                <div style='position: absolute; left: {marker_pos}px; top: -8px; width: 20px; height: 20px; 
                            background: white; border: 3px solid #1f2937; border-radius: 50%; 
                            box-shadow: 0 2px 4px rgba(0,0,0,0.3); transform: translateX(-50%);'></div>
            </div>
            <!-- Labels -->
            <div style='display: flex; justify-content: space-between; margin-top: 10px; font-size: 12px;'>
                <span style='font-weight: bold;'>0mm<br>Không đau</span>
                <span style='font-weight: bold;'>50mm<br>Đau vừa</span>
                <span style='font-weight: bold;'>100mm<br>Đau dữ dội nhất</span>
            </div>
            <!-- Current value -->
            <div style='text-align: center; margin-top: 15px; font-size: 18px; font-weight: bold; color: #1f2937;'>
                VAS = {vas_value}mm
            </div>
        </div>
    </div>
    """
    
    st.markdown(scale_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("📊 Đánh Giá", type="primary", use_container_width=True):
        st.markdown("## 📊 Kết Quả")
        
        # Convert VAS to NRS equivalent for interpretation
        nrs_equivalent = round(vas_value / 10)
        
        # Interpret pain level
        if vas_value == 0:
            severity = "Không đau"
            color = "#10b981"
            icon = "✅"
        elif vas_value <= 30:
            severity = "Đau nhẹ"
            color = "#fbbf24"
            icon = "😐"
        elif vas_value <= 60:
            severity = "Đau vừa"
            color = "#f59e0b"
            icon = "😣"
        else:
            severity = "Đau nặng"
            color = "#ef4444"
            icon = "😰"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} VAS = {vas_value}mm
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {severity} (Tương đương NRS {nrs_equivalent}/10)
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Treatment recommendations (similar to NRS)
        st.markdown("---")
        st.markdown("### 💊 Khuyến Nghị Điều Trị")
        
        if vas_value == 0:
            st.success("**✅ Không cần điều trị giảm đau**")
        elif vas_value <= 30:
            st.info("""
            **💊 Đau nhẹ (VAS 1-30mm):**
            - Paracetamol hoặc NSAID
            - Đánh giá lại sau 30-60 phút
            """)
        elif vas_value <= 60:
            st.warning("""
            **💊 Đau vừa (VAS 31-60mm):**
            - Opioid yếu (Codeine, Tramadol) + Non-opioid
            - Đánh giá lại sau 30 phút
            """)
        else:
            st.error("""
            **🚨 Đau nặng (VAS 61-100mm):**
            - Opioid mạnh (Morphine, Fentanyl) ngay lập tức
            - Đánh giá lại sau 15-30 phút
            """)
        
        with st.expander("📚 Hướng Dẫn Sử Dụng"):
            st.markdown("""
            ### 🎯 Cách Đánh Giá:
            
            1. **Chuẩn bị:**
               - Thước đo 100mm
               - Đường thẳng có đánh dấu 0mm và 100mm
            
            2. **Hướng dẫn bệnh nhân:**
               - "Đầu bên trái (0mm) = Không đau"
               - "Đầu bên phải (100mm) = Đau dữ dội nhất có thể tưởng tượng"
               - "Hãy đánh dấu trên đường thẳng mức độ đau của bạn"
            
            3. **Đo kết quả:**
               - Đo khoảng cách từ 0mm đến vị trí đánh dấu
               - Ghi nhận chính xác đến mm
            
            ### 📋 Chuyển Đổi VAS ↔ NRS:
            - **VAS 0-10mm** ≈ NRS 0-1 (Không đau/đau nhẹ)
            - **VAS 11-30mm** ≈ NRS 2-3 (Đau nhẹ)
            - **VAS 31-60mm** ≈ NRS 4-6 (Đau vừa)
            - **VAS 61-100mm** ≈ NRS 7-10 (Đau nặng)
            
            ### ⚠️ Lưu Ý:
            - VAS nhạy cảm hơn NRS với thay đổi nhỏ
            - Phù hợp cho nghiên cứu và theo dõi dài hạn
            - Khó dùng cho bệnh nhân già, rối loạn thị giác
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **VAS 0-30mm:** Đau nhẹ → Non-opioid
    2. **VAS 31-60mm:** Đau vừa → Opioid yếu
    3. **VAS 61-100mm:** Đau nặng → Opioid mạnh
    4. **Chuyển đổi:** VAS (mm) ÷ 10 ≈ NRS
    5. **Mục tiêu:** VAS ≤ 30mm hoặc giảm ≥20mm
    """)

