"""
Neurology Scoring Systems
All neurological assessment calculators
"""

import streamlit as st


def render_gcs():
    """Glasgow Coma Scale Calculator"""
    st.subheader("🧠 Glasgow Coma Scale (GCS)")
    st.caption("Đánh Giá Mức Độ Ý Thức")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thang Đánh Giá")
        
        # Eye Opening (E)
        st.markdown("#### 👁️ Eye Opening (Mở Mắt)")
        eye_options = {
            "Spontaneous (Tự nhiên)": 4,
            "To speech (Khi gọi)": 3,
            "To pain (Khi đau)": 2,
            "None (Không mở)": 1
        }
        eye_response = st.radio(
            "Phản ứng mở mắt:",
            list(eye_options.keys()),
            key="gcs_eye"
        )
        eye_score = eye_options[eye_response]
        
        # Verbal Response (V)
        st.markdown("#### 🗣️ Verbal Response (Lời Nói)")
        verbal_options = {
            "Oriented (Tỉnh táo, định hướng đúng)": 5,
            "Confused (Lẫn lộn)": 4,
            "Inappropriate words (Nói lung tung)": 3,
            "Incomprehensible sounds (Rên rỉ)": 2,
            "None (Không nói)": 1
        }
        verbal_response = st.radio(
            "Phản ứng lời nói:",
            list(verbal_options.keys()),
            key="gcs_verbal"
        )
        verbal_score = verbal_options[verbal_response]
        
        # Motor Response (M)
        st.markdown("#### 💪 Motor Response (Vận Động)")
        motor_options = {
            "Obeys commands (Làm theo lệnh)": 6,
            "Localizes pain (Định vị đau)": 5,
            "Withdraws from pain (Rút tay khi đau)": 4,
            "Flexion to pain (Cử động bất thường)": 3,
            "Extension to pain (Duỗi cứng)": 2,
            "None (Không cử động)": 1
        }
        motor_response = st.radio(
            "Phản ứng vận động:",
            list(motor_options.keys()),
            key="gcs_motor"
        )
        motor_score = motor_options[motor_response]
        
        if st.button("🧮 Tính GCS", type="primary"):
            total_score = eye_score + verbal_score + motor_score
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                st.markdown(f"**E{eye_score} V{verbal_score} M{motor_score}**")
                
                if total_score >= 14:
                    st.success(f"## GCS = {total_score}")
                    st.success("✅ Tổn Thương Nhẹ")
                    severity = "Mild TBI"
                elif total_score >= 9:
                    st.warning(f"## GCS = {total_score}")
                    st.warning("⚠️ Tổn Thương Trung Bình")
                    severity = "Moderate TBI"
                else:
                    st.error(f"## GCS = {total_score}")
                    st.error("🚨 Tổn Thương Nặng")
                    severity = "Severe TBI"
            
            st.markdown("### 💡 Giải Thích")
            
            st.write(f"**Tổng điểm:** {total_score}/15")
            st.write(f"**Phân loại:** {severity}")
            
            st.markdown(f"""
            **Chi tiết:**
            - Eye Opening: {eye_score}/4 - {eye_response}
            - Verbal Response: {verbal_score}/5 - {verbal_response}
            - Motor Response: {motor_score}/6 - {motor_response}
            """)
            
            st.markdown("---")
            st.markdown("### 💊 Ý Nghĩa Lâm Sàng")
            
            if total_score >= 14:
                st.success("""
                **GCS 14-15: Chấn thương sọ não nhẹ**
                - Theo dõi lâm sàng
                - CT scan nếu có triệu chứng
                - Thường hồi phục tốt
                """)
            elif total_score >= 9:
                st.warning("""
                **GCS 9-13: Chấn thương sọ não trung bình**
                - Nhập viện theo dõi
                - CT scan sọ não
                - Theo dõi sát các dấu hiệu tăng áp lực nội sọ
                - Có thể cần can thiệp
                """)
            else:
                st.error("""
                **GCS ≤8: Chấn thương sọ não nặng**
                - **ĐẶT NỘI KHÍ QUẢN NGAY** (GCS ≤8)
                - Nhập ICU
                - CT scan khẩn cấp
                - Theo dõi áp lực nội sọ
                - Có thể cần phẫu thuật
                - Tiên lượng xấu
                """)
            
            # Additional warnings
            if total_score <= 8:
                st.error("""
                **⚠️ QUAN TRỌNG:**
                - GCS ≤8 = Mất khả năng bảo vệ đường thở
                - Chỉ định đặt nội khí quản
                - Nguy cơ hít sặc cao
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **Glasgow Coma Scale (GCS)**
                
                **Thang điểm (3-15):**
                
                **Eye Opening (1-4):**
                - 4: Spontaneous
                - 3: To speech
                - 2: To pain
                - 1: None
                
                **Verbal Response (1-5):**
                - 5: Oriented
                - 4: Confused
                - 3: Inappropriate words
                - 2: Incomprehensible sounds
                - 1: None
                
                **Motor Response (1-6):**
                - 6: Obeys commands
                - 5: Localizes pain
                - 4: Withdraws from pain
                - 3: Flexion to pain (decorticate)
                - 2: Extension to pain (decerebrate)
                - 1: None
                
                **Phân loại chấn thương sọ não:**
                - GCS 14-15: Mild TBI
                - GCS 9-13: Moderate TBI
                - GCS 3-8: Severe TBI
                
                **Chỉ định đặt nội khí quản:**
                - GCS ≤8 (mất khả năng bảo vệ đường thở)
                
                **Reference:**
                Teasdale G, Jennett B. Assessment of coma and impaired consciousness. A practical scale. Lancet. 1974;2(7872):81-84.
                
                **Validation:**
                - Widely validated across trauma, neurosurgery, ICU
                - Gold standard for consciousness assessment
                """)


def render_nihss():
    """NIHSS Score Calculator"""
    st.subheader("🧠 NIHSS - NIH Stroke Scale")
    st.caption("Mức Độ Nặng Đột Quỵ")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2")
    
    st.info("""
    **NIHSS đánh giá:**
    - Level of consciousness
    - Gaze
    - Visual fields
    - Facial palsy
    - Motor arm/leg
    - Ataxia
    - Sensory
    - Language
    - Dysarthria
    - Extinction/inattention
    
    **Tổng điểm:** 0-42
    """)


def render_ich_score():
    """ICH Score Calculator"""
    st.subheader("🧠 ICH Score")
    st.caption("Tiên Lượng Xuất Huyết Nội Sọ")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


def render_hunt_hess():
    """Hunt & Hess Scale Calculator"""
    st.subheader("🧠 Hunt & Hess Scale")
    st.caption("Phân Loại Xuất Huyết Dưới Nhện")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


def render_mrs():
    """Modified Rankin Scale Calculator"""
    st.subheader("🧠 mRS - Modified Rankin Scale")
    st.caption("Mức Độ Khuyết Tật Sau Đột Quỵ")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


# Router function
def render_neurology_calculator(calculator_id):
    """
    Route to the correct neurology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    calculators = {
        "GCS": render_gcs,
        "NIHSS": render_nihss,
        "ICH Score": render_ich_score,
        "Hunt & Hess": render_hunt_hess,
        "mRS": render_mrs,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")

