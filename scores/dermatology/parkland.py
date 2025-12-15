"""
Parkland Formula Calculator
Công thức truyền dịch cho bệnh nhân bỏng
"""

import streamlit as st
from scores.utils.validation import (
    validate_range,
    validate_positive
)
from components.ui.validation import render_validation_errors


def calculate_parkland(tbsa, weight):
    """
    Parkland Formula: 4 ml × TBSA% × Weight(kg) trong 24h
    
    50% trong 8h đầu, 50% trong 16h sau
    """
    total_24h = 4 * tbsa * weight
    first_8h = total_24h / 2
    next_16h = total_24h / 2
    rate_first_8h = first_8h / 8
    rate_next_16h = next_16h / 16
    
    return {
        "total_24h": total_24h,
        "first_8h": first_8h,
        "next_16h": next_16h,
        "rate_first_8h": rate_first_8h,
        "rate_next_16h": rate_next_16h
    }


def render():
    """Render Parkland Formula interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #F59E0B;'>💧 Parkland Formula</h2>
    <p style='text-align: center;'><em>Truyền dịch ban đầu cho bệnh nhân bỏng</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Parkland Formula"):
        st.markdown("""
        **Parkland Formula** tính lượng dịch Ringer Lactate cần truyền trong 24 giờ đầu cho bệnh nhân bỏng.
        
        **Công thức:**
        ```
        Thể tích (ml) = 4 ml × TBSA% × Cân nặng (kg)
        ```
        
        **Phân bố:**
        - 50% trong 8 giờ đầu (tính từ lúc bỏng)
        - 50% trong 16 giờ sau
        
        **Dịch sử dụng:** Ringer Lactate (RL)
        
        **Điều Chỉnh:** Theo nước tiểu (0.5-1 ml/kg/h)
        """)
    
    st.markdown("---")
    st.subheader("📝 Nhập số liệu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tbsa = st.number_input(
            "% TBSA (Total Body Surface Area bỏng)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=1.0,
            help="Chỉ tính bỏng độ 2 và độ 3"
        )
    
    with col2:
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=10.0,
            max_value=200.0,
            value=70.0,
            step=1.0
        )
    
    st.markdown("---")
    
    if st.button("💧 Tính lượng dịch", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # TBSA validation (0-100%)
        is_valid_tbsa, tbsa_error = validate_range(tbsa, 0.0, 100.0, "TBSA (%)")
        if not is_valid_tbsa:
            validation_errors.append(f"TBSA: {tbsa_error}")
        
        # Weight validation
        is_valid_weight, weight_error = validate_positive(weight, "Cân nặng")
        if not is_valid_weight:
            validation_errors.append(f"Cân nặng: {weight_error}")
        elif weight < 10.0:
            validation_errors.append("Cân nặng phải ≥ 10 kg")
        elif weight > 200.0:
            validation_errors.append("Cân nặng phải ≤ 200 kg (kiểm tra lại)")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_parkland(tbsa, weight)
        
        st.markdown("## 📊 Kết quả - Parkland Formula")
        
        st.success(f"""
        ### Công thức:
        **4 ml × {tbsa}% × {weight} kg = {result['total_24h']:.0f} ml Ringer Lactate trong 24h**
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style='background-color: #FEE2E2; padding: 20px; border-radius: 10px; border-left: 5px solid #DC2626;'>
                <h3 style='color: #DC2626; margin-top: 0;'>⏱️ 8 giờ ĐẦU</h3>
                <p style='font-size: 1.5em; font-weight: bold; margin: 10px 0;'>{:.0f} ml</p>
                <p style='margin: 0;'>Tốc độ: <strong>{:.0f} ml/giờ</strong></p>
            </div>
            """.format(result['first_8h'], result['rate_first_8h']), unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background-color: #DBEAFE; padding: 20px; border-radius: 10px; border-left: 5px solid #2563EB;'>
                <h3 style='color: #2563EB; margin-top: 0;'>⏱️ 16 giờ SAU</h3>
                <p style='font-size: 1.5em; font-weight: bold; margin: 10px 0;'>{:.0f} ml</p>
                <p style='margin: 0;'>Tốc độ: <strong>{:.0f} ml/giờ</strong></p>
            </div>
            """.format(result['next_16h'], result['rate_next_16h']), unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.warning("""
        ⚠️ **Lưu ý quan trọng:**
        
        **1. Thời gian tính:**
        - Tính từ lúc BỎng, KHÔNG phải lúc nhập viện
        - Nếu đến viện muộn 2h → Truyền 8h đầu trong 6h
        
        **2. Chỉ là công thức KHỞI ĐẦU:**
        - **ĐIỀU CHỈNH** theo đáp ứng lâm sàng
        - Mục tiêu: Nước tiểu **0.5-1 ml/kg/h** (Người Lớn)
        - Trẻ em: 1-2 ml/kg/h
        
        **3. Theo dõi:**
        - ✅ Nước tiểu (đặt sonde tiểu)
        - ✅ Huyết áp, mạch
        - ✅ Lactate máu
        - ✅ Tình trạng ý thức
        - ✅ Tình trạng tưới máu ngoại vi
        
        **4. Tránh:**
        - ❌ Truyền quá nhiều → phù, ARDS, compartment syndrome
        - ❌ Truyền quá ít → sốc, suy thận
        """)
        
        st.info("""
        💡 **Bổ sung dịch colloid:**
        - Sau 24h có thể cân nhắc albumin
        - Nếu TBSA > 30% và cần thể tích lớn
        
        💡 **Dinh dưỡng:**
        - Bắt đầu sớm (trong 24-48h)
        - Đường tiêu hóa ưu tiên
        """)


if __name__ == "__main__":
    render()

