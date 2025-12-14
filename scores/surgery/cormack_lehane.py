"""
Cormack-Lehane Classification Calculator
Phân loại tầm nhìn khi soi thanh quản
"""

import streamlit as st


def get_cormack_lehane_interpretation(grade):
    """
    Trả về thông tin về Cormack-Lehane grade
    
    Parameters:
    - grade: Grade 1-4
    
    Returns:
    - dict với description, difficulty, và recommendation
    """
    interpretations = {
        1: {
            "description": "Nhìn thấy toàn bộ thanh môn",
            "difficulty": "Dễ dàng",
            "recommendation": "Đặt NKQ dễ dàng, không cần hỗ trợ đặc biệt",
            "color": "green"
        },
        2: {
            "description": "Nhìn thấy một phần thanh môn (chỉ thấy nắp thanh môn)",
            "difficulty": "Trung bình",
            "recommendation": "Có thể đặt NKQ, có thể cần bougie hoặc stylet",
            "color": "orange"
        },
        3: {
            "description": "Chỉ thấy nắp thanh môn, không thấy thanh môn",
            "difficulty": "Khó",
            "recommendation": "Đặt NKQ khó, cần bougie, có thể cần video laryngoscope hoặc LMA",
            "color": "red"
        },
        4: {
            "description": "Không thấy gì (không thấy nắp thanh môn)",
            "difficulty": "Rất khó",
            "recommendation": "Không thể đặt NKQ bằng laryngoscope thường, cần video laryngoscope, fiberoptic, hoặc LMA. Cân nhắc cricothyrotomy nếu cấp cứu",
            "color": "red"
        }
    }
    
    return interpretations.get(grade, interpretations[1])


def render():
    """Render Cormack-Lehane Classification interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🔍 Cormack-Lehane Classification</h2>
    <p style='text-align: center;'><em>Phân loại tầm nhìn khi soi thanh quản</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Cormack-Lehane Classification"):
        st.markdown("""
        **Cormack-Lehane Classification** là hệ thống phân loại tầm nhìn khi soi thanh quản,
        giúp mô tả và ghi nhận mức độ khó khăn khi đặt nội khí quản.
        
        **4 mức độ:**
        
        **Grade 1:** Nhìn thấy toàn bộ thanh môn
        - Đặt NKQ dễ dàng
        
        **Grade 2:** Nhìn thấy một phần thanh môn (chỉ thấy nắp thanh môn)
        - Có thể đặt NKQ, có thể cần hỗ trợ
        
        **Grade 3:** Chỉ thấy nắp thanh môn, không thấy thanh môn
        - Đặt NKQ khó, cần dụng cụ hỗ trợ
        
        **Grade 4:** Không thấy gì (không thấy nắp thanh môn)
        - Rất khó đặt NKQ, cần dụng cụ đặc biệt
        
        **Modified Cormack-Lehane (POGO - Percentage of Glottic Opening):**
        - Mô tả chi tiết hơn bằng phần trăm thanh môn nhìn thấy
        - 100% = Grade 1
        - 50-99% = Grade 2a
        - 1-49% = Grade 2b
        - 0% = Grade 3-4
        
        **Reference:** Cormack RS, Lehane J. Difficult tracheal intubation in obstetrics. 
        Anaesthesia. 1984;39(11):1105-11.
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Chọn mức độ tầm nhìn")
    
    grade = st.radio(
        "Cormack-Lehane Grade:",
        options=[1, 2, 3, 4],
        format_func=lambda x: {
            1: "Grade 1 - Nhìn thấy toàn bộ thanh môn",
            2: "Grade 2 - Nhìn thấy một phần thanh môn (chỉ thấy nắp thanh môn)",
            3: "Grade 3 - Chỉ thấy nắp thanh môn, không thấy thanh môn",
            4: "Grade 4 - Không thấy gì (không thấy nắp thanh môn)"
        }[x],
        key="cormack_grade",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔍 Xem kết quả", type="primary", use_container_width=True):
        result = get_cormack_lehane_interpretation(grade)
        
        # Display results
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Grade", f"Grade {grade}")
        
        with col2:
            st.metric("Mức độ khó", result['difficulty'])
        
        st.markdown("---")
        
        st.subheader("📋 Mô tả")
        st.info(f"**{result['description']}**")
        
        st.markdown("---")
        
        # Recommendation
        if result['color'] == "green":
            st.success(f"**Khuyến nghị:** {result['recommendation']}")
        elif result['color'] == "orange":
            st.warning(f"**Khuyến nghị:** {result['recommendation']}")
        else:
            st.error(f"**Khuyến nghị:** {result['recommendation']}")
        
        st.markdown("---")
        
        # Additional information based on grade
        if grade >= 3:
            with st.expander("🔧 Dụng cụ hỗ trợ cho Grade 3-4"):
                st.markdown("""
                **Khi gặp Grade 3-4, cần chuẩn bị:**
                
                1. **Bougie (Gum elastic bougie)**
                   - Đưa vào dưới nắp thanh môn
                   - Cảm nhận "click" khi vào khí quản
                   - Luồn NKQ qua bougie
                
                2. **Video laryngoscope**
                   - Glidescope, C-MAC, McGrath, etc.
                   - Tầm nhìn tốt hơn laryngoscope thường
                   - Dễ sử dụng hơn fiberoptic
                
                3. **Laryngeal Mask Airway (LMA)**
                   - Dự phòng nếu không đặt được NKQ
                   - Có thể dùng để đặt NKQ qua LMA (LMA-Fastrach)
                
                4. **Fiberoptic bronchoscope**
                   - Đặt NKQ tỉnh hoặc dưới gây mê
                   - Cần kỹ năng đặc biệt
                   - Phù hợp khi có thời gian chuẩn bị
                
                5. **Cricothyrotomy kit**
                   - Dự phòng cuối cùng nếu không đặt được NKQ
                   - Cần có sẵn trong phòng mổ
                   - Chỉ dùng khi cấp cứu
                
                **Chiến lược:**
                - Grade 3: Thử bougie trước, nếu không được → video laryngoscope
                - Grade 4: Video laryngoscope hoặc LMA ngay, chuẩn bị cricothyrotomy
                """)
        
        # Modified classification
        with st.expander("📊 Modified Cormack-Lehane (POGO)"):
            st.markdown("""
            **POGO (Percentage of Glottic Opening)** mô tả chi tiết hơn:
            
            - **100%:** Nhìn thấy toàn bộ thanh môn (Grade 1)
            - **50-99%:** Nhìn thấy >50% thanh môn (Grade 2a)
            - **1-49%:** Nhìn thấy <50% thanh môn (Grade 2b)
            - **0%:** Không thấy thanh môn (Grade 3-4)
            
            **Ưu điểm:**
            - Mô tả chính xác hơn mức độ nhìn thấy
            - Hữu ích trong nghiên cứu và đào tạo
            """)

