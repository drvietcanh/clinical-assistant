"""
Wilson Risk Score Calculator
Dự đoán đặt nội khí quản khó
"""

import streamlit as st


def calculate_wilson_risk(weight, head_neck_movement, jaw_movement, receding_mandible, buck_teeth):
    """
    Tính điểm Wilson Risk Score
    
    Parameters (mỗi yếu tố 0-2 điểm):
    - weight: Cân nặng (0=normal, 1=obese, 2=morbidly obese)
    - head_neck_movement: Cử động đầu cổ (0=normal, 1=limited, 2=severe)
    - jaw_movement: Cử động hàm (0=normal, 1=limited, 2=severe)
    - receding_mandible: Hàm lùi (0=no, 1=moderate, 2=severe)
    - buck_teeth: Răng hô (0=no, 1=moderate, 2=severe)
    
    Returns:
    - dict với total_score và interpretation
    """
    total = weight + head_neck_movement + jaw_movement + receding_mandible + buck_teeth
    
    # Interpretation
    if total <= 1:
        risk = "Nguy cơ thấp"
        difficulty = "Đặt NKQ dễ dàng"
        recommendation = "Gây mê tiêu chuẩn, bác sĩ gây mê thường quy"
        color = "green"
    elif total == 2:
        risk = "Nguy cơ trung bình"
        difficulty = "Có thể đặt NKQ khó"
        recommendation = "Chuẩn bị dụng cụ đường thở khó, có bác sĩ gây mê giàu kinh nghiệm"
        color = "orange"
    else:  # ≥3
        risk = "Nguy cơ cao"
        difficulty = "Đặt NKQ khó - Cần chuẩn bị đặc biệt"
        recommendation = "Bắt buộc có bác sĩ gây mê giàu kinh nghiệm, chuẩn bị đầy đủ dụng cụ đường thở khó (video laryngoscope, LMA, fiberoptic), cân nhắc đặt NKQ tỉnh"
        color = "red"
    
    return {
        "total_score": total,
        "risk": risk,
        "difficulty": difficulty,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render Wilson Risk Score interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🔍 Wilson Risk Score</h2>
    <p style='text-align: center;'><em>Dự đoán đặt nội khí quản khó</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Wilson Risk Score"):
        st.markdown("""
        **Wilson Risk Score** là thang điểm đánh giá nguy cơ đặt nội khí quản khó,
        giúp bác sĩ gây mê chuẩn bị trước phẫu thuật.
        
        **5 yếu tố đánh giá (mỗi yếu tố 0-2 điểm):**
        1. **Cân nặng** - Béo phì làm tăng nguy cơ
        2. **Cử động đầu cổ** - Hạn chế cử động làm tăng nguy cơ
        3. **Cử động hàm** - Hạn chế mở miệng làm tăng nguy cơ
        4. **Hàm lùi (Receding mandible)** - Hàm nhỏ/lùi làm tăng nguy cơ
        5. **Răng hô (Buck teeth)** - Răng hô làm tăng nguy cơ
        
        **Điểm số:**
        - **0-1 điểm:** Nguy cơ thấp - Đặt NKQ dễ dàng
        - **2 điểm:** Nguy cơ trung bình - Có thể đặt NKQ khó
        - **≥3 điểm:** Nguy cơ cao - Đặt NKQ khó, cần chuẩn bị đặc biệt
        
        **Reference:** Wilson ME, et al. Predicting difficult intubation. 
        Br J Anaesth. 1988;61(2):211-6.
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá 5 yếu tố (mỗi yếu tố 0-2 điểm)")
    
    # Weight
    st.markdown("### 1️⃣ Cân nặng")
    weight = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (BMI <30)",
            1: "1 điểm - Béo phì (BMI 30-40)",
            2: "2 điểm - Béo phì nặng (BMI >40)"
        }[x],
        key="wilson_weight",
        horizontal=False
    )
    
    # Head/Neck movement
    st.markdown("### 2️⃣ Cử động đầu cổ")
    head_neck_movement = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (≥90° extension)",
            1: "1 điểm - Hạn chế (30-90° extension)",
            2: "2 điểm - Nghiêm trọng (<30° extension)"
        }[x],
        key="wilson_head_neck",
        horizontal=False
    )
    
    # Jaw movement
    st.markdown("### 3️⃣ Cử động hàm (mở miệng)")
    jaw_movement = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (IGD ≥5cm)",
            1: "1 điểm - Hạn chế (IGD 3-5cm)",
            2: "2 điểm - Nghiêm trọng (IGD <3cm)"
        }[x],
        key="wilson_jaw",
        horizontal=False
    )
    st.caption("IGD = Inter-incisor gap distance (khoảng cách giữa 2 răng cửa)")
    
    # Receding mandible
    st.markdown("### 4️⃣ Hàm lùi (Receding mandible)")
    receding_mandible = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Không",
            1: "1 điểm - Trung bình",
            2: "2 điểm - Nghiêm trọng"
        }[x],
        key="wilson_mandible",
        horizontal=False
    )
    
    # Buck teeth
    st.markdown("### 5️⃣ Răng hô (Buck teeth/Protruding teeth)")
    buck_teeth = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Không",
            1: "1 điểm - Trung bình",
            2: "2 điểm - Nghiêm trọng"
        }[x],
        key="wilson_teeth",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔍 Tính toán", type="primary", use_container_width=True):
        result = calculate_wilson_risk(weight, head_neck_movement, jaw_movement, receding_mandible, buck_teeth)
        
        # Display results
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Tổng điểm", f"{result['total_score']}/10")
        
        with col2:
            st.metric("Nguy cơ", result['risk'])
        
        st.markdown("---")
        
        # Risk interpretation
        if result['color'] == "green":
            st.success(f"**{result['risk']}** - {result['difficulty']}")
        elif result['color'] == "orange":
            st.warning(f"**{result['risk']}** - {result['difficulty']}")
        else:
            st.error(f"**{result['risk']}** - {result['difficulty']}")
        
        st.markdown("---")
        
        st.subheader("💡 Khuyến nghị")
        st.markdown(f"""
        {result['recommendation']}
        """)
        
        st.markdown("---")
        
        # Additional information
        with st.expander("📚 Dụng cụ đường thở khó"):
            st.markdown("""
            **Chuẩn bị dụng cụ khi nguy cơ cao:**
            
            1. **Video laryngoscope** (Glidescope, C-MAC, etc.)
               - Tầm nhìn tốt hơn laryngoscope thường
               - Dễ sử dụng hơn fiberoptic
            
            2. **Laryngeal Mask Airway (LMA)**
               - Dự phòng nếu không đặt được NKQ
               - Có thể dùng để đặt NKQ qua LMA
            
            3. **Fiberoptic bronchoscope**
               - Đặt NKQ tỉnh hoặc dưới gây mê
               - Cần kỹ năng đặc biệt
            
            4. **Bougie/Gum elastic bougie**
               - Hỗ trợ đặt NKQ khi tầm nhìn hạn chế
            
            5. **Cricothyrotomy kit**
               - Dự phòng cuối cùng nếu không đặt được NKQ
               - Cần có sẵn trong phòng mổ
            
            **Chiến lược:**
            - Điểm ≥3: Cân nhắc đặt NKQ tỉnh với fiberoptic
            - Luôn có kế hoạch B và C
            - Thông báo trước cho đội ngũ phẫu thuật
            """)

