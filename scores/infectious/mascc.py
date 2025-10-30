"""
MASCC Risk Index Calculator
Nguy cơ biến chứng trong sốt giảm bạch cầu hạt
"""

import streamlit as st


def calculate_mascc(burden, hypotension, copd, solid_tumor_fungal, dehydration, outpatient, age):
    """Tính MASCC Risk Index"""
    total = burden + hypotension + copd + solid_tumor_fungal + dehydration + outpatient + age
    
    if total >= 21:
        risk = "Thấp"
        mortality = "< 1-5%"
        management = "Có thể điều trị ngoại trú với kháng sinh uống"
        color = "green"
    else:
        risk = "Cao"
        mortality = "> 10-20%"
        management = "Cần nhập viện, kháng sinh tĩnh mạch"
        color = "red"
    
    return {"total_score": total, "risk_level": risk, "mortality": mortality, "management": management, "color": color}


def render():
    """Render MASCC Risk Index interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #8B5CF6;'>🦠 MASCC Risk Index</h2>
    <p style='text-align: center;'><em>Nguy cơ biến chứng sốt giảm bạch cầu hạt (Febrile Neutropenia)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về MASCC"):
        st.markdown("""
        **MASCC (Multinational Association for Supportive Care in Cancer) Risk Index** 
        đánh giá nguy cơ biến chứng nghiêm trọng ở bệnh nhân ung thư có sốt giảm bạch cầu hạt.
        
        **Sốt giảm bạch cầu hạt:**
        - Nhiệt độ ≥ 38.3°C hoặc ≥ 38°C trong > 1 giờ
        - Số lượng bạch cầu hạt (ANC) < 500/µL
        
        **Mục đích:** Phân loại nguy cơ để quyết định điều trị nội trú hoặc ngoại trú
        
        **Tiêu chuẩn:**
        - ≥ 21 điểm: Nguy cơ thấp → Có thể ngoại trú
        - < 21 điểm: Nguy cơ cao → Nhập viện
        """)
    
    st.markdown("---")
    st.subheader("📝 Đánh giá các yếu tố")
    
    burden = st.radio(
        "Mức độ triệu chứng nhiễm trùng",
        options=[5, 3, 0],
        format_func=lambda x: {5: "5 điểm - Không/nhẹ", 3: "3 điểm - Trung bình", 0: "0 điểm - Nặng"}[x]
    )
    
    hypotension = st.radio(
        "Hạ huyết áp (SBP < 90)",
        options=[0, 5],
        format_func=lambda x: "5 điểm - Không" if x == 5 else "0 điểm - Có"
    )
    
    copd = st.radio(
        "COPD (Bệnh phổi tắc nghẽn mạn)",
        options=[0, 4],
        format_func=lambda x: "4 điểm - Không" if x == 4 else "0 điểm - Có"
    )
    
    solid_tumor_fungal = st.radio(
        "U đặc không có nhiễm nấm trước đó",
        options=[0, 4],
        format_func=lambda x: "4 điểm - Có (U đặc, không nhiễm nấm)" if x == 4 else "0 điểm - Không"
    )
    
    dehydration = st.radio(
        "Mất nước cần truyền tĩnh mạch",
        options=[0, 3],
        format_func=lambda x: "3 điểm - Không" if x == 3 else "0 điểm - Có"
    )
    
    outpatient = st.radio(
        "Khởi phát khi đang ngoại trú",
        options=[0, 3],
        format_func=lambda x: "3 điểm - Có" if x == 3 else "0 điểm - Không (đang nội trú)"
    )
    
    age = st.radio(
        "Tuổi < 60",
        options=[0, 2],
        format_func=lambda x: "2 điểm - Có (< 60 tuổi)" if x == 2 else "0 điểm - Không (≥ 60 tuổi)"
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính MASCC Score", type="primary", use_container_width=True):
        result = calculate_mascc(burden, hypotension, copd, solid_tumor_fungal, dehydration, outpatient, age)
        
        score_color = "#28a745" if result["color"] == "green" else "#dc3545"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                MASCC Score: {result['total_score']}/26
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color};'>🎯 Nguy cơ: {result['risk_level']}</h3>
            <p><strong>Tử vong:</strong> {result['mortality']}</p>
            <p style='font-size: 1.2em; font-weight: bold;'><strong>Quản lý:</strong> {result['management']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if result["total_score"] >= 21:
            st.success("""
            ✅ **Nguy cơ thấp - Cân nhắc điều trị ngoại trú**
            
            **Tiêu chuẩn điều trị ngoại trú:**
            - MASCC ≥ 21
            - Bệnh nhân ổn định, không biến chứng
            - Có khả năng tuân thủ, tái khám
            - Kháng sinh: Ciprofloxacin + Amoxicillin-clavulanate
            - Theo dõi sát hàng ngày
            """)
        else:
            st.error("""
            🚨 **Nguy cơ cao - Cần nhập viện**
            
            **Quản lý:**
            - Nhập viện ngay
            - Kháng sinh phổ rộng tĩnh mạch trong 1 giờ
            - Nuôi cấy máu, nước tiểu trước khi kháng sinh
            - G-CSF nếu nguy cơ cao
            - Theo dõi ICU nếu cần
            """)


if __name__ == "__main__":
    render()

