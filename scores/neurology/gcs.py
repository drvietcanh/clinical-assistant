"""
Thang điểm hôn mê Glasgow (GCS)
Consciousness level assessment
"""

import streamlit as st


def render():
    """Thang điểm hôn mê Glasgow Calculator"""
    st.subheader("🧠 Thang điểm hôn mê Glasgow (GCS)")
    st.caption("Đánh giá Mức độ ý thức")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thang Đánh giá")
        
        # Eye Opening (E)
        st.markdown("#### 👁️ Mở mắt (Eye Opening)")
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
        st.markdown("#### 🗣️ Phản Ứng Lời nói (Verbal Response)")
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
        st.markdown("#### 💪 Phản Ứng Vận động (Motor Response)")
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
                st.markdown("### 📊 Kết quả")
                
                st.markdown(f"**E{eye_score} V{verbal_score} M{motor_score}**")
                
                if total_score >= 14:
                    st.success(f"## GCS = {total_score}")
                    st.success("✅ Tổn Thương Nhẹ")
                    severity = "Chấn thương sọ não nhẹ (Mild TBI)"
                elif total_score >= 9:
                    st.warning(f"## GCS = {total_score}")
                    st.warning("⚠️ Tổn Thương Trung Bình")
                    severity = "Chấn thương sọ não trung bình (Moderate TBI)"
                else:
                    st.error(f"## GCS = {total_score}")
                    st.error("🚨 Tổn Thương Nặng")
                    severity = "Chấn thương sọ não nặng (Severe TBI)"
            
            st.markdown("### 💡 Giải thích")
            
            st.write(f"**Tổng điểm:** {total_score}/15")
            st.write(f"**Phân loại:** {severity}")
            
            st.markdown(f"""
            **Chi tiết:**
            - Mở mắt (Eye Opening): {eye_score}/4 - {eye_response}
            - Phản Ứng Lời nói (Verbal Response): {verbal_score}/5 - {verbal_response}
            - Phản Ứng Vận động (Motor Response): {motor_score}/6 - {motor_response}
            """)
            
            st.markdown("---")
            st.markdown("### 💊 Ý nghĩa lâm sàng")
            
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
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown("""
                **Thang điểm hôn mê Glasgow (GCS)**
                
                **Thang điểm (3-15):**
                
                **Mở mắt (Eye Opening) (1-4):**
                - 4: Tự nhiên (Spontaneous)
                - 3: Khi gọi (To speech)
                - 2: Khi đau (To pain)
                - 1: Không mở (None)
                
                **Phản Ứng Lời nói (Verbal Response) (1-5):**
                - 5: Tỉnh táo, định hướng đúng (Oriented)
                - 4: Lẫn lộn (Confused)
                - 3: Nói lung tung (Inappropriate words)
                - 2: Rên rỉ (Incomprehensible sounds)
                - 1: Không nói (None)
                
                **Phản Ứng Vận động (Motor Response) (1-6):**
                - 6: Làm theo lệnh (Obeys commands)
                - 5: Định vị đau (Localizes pain)
                - 4: Rút tay khi đau (Withdraws from pain)
                - 3: Gấp cứng khi đau (decorticate) (Flexion to pain)
                - 2: Duỗi cứng khi đau (decerebrate) (Extension to pain)
                - 1: Không cử động (None)
                
                **Phân loại chấn thương sọ não:**
                - GCS 14-15: Chấn thương sọ não nhẹ (Mild TBI)
                - GCS 9-13: Chấn thương sọ não trung bình (Moderate TBI)
                - GCS 3-8: Chấn thương sọ não nặng (Severe TBI)
                
                **Chỉ định đặt nội khí quản:**
                - GCS ≤8 (mất khả năng bảo vệ đường thở)
                
                **Tài liệu tham khảo:**
                Teasdale G, Jennett B. Assessment of coma and impaired consciousness. A practical scale. Lancet. 1974;2(7872):81-84.
                
                **Xác nhận giá trị:**
                - Được xác nhận rộng rãi trong chấn thương, phẫu thuật thần kinh, hồi sức cấp cứu
                - Tiêu chuẩn vàng để đánh giá mức độ ý thức
                """)

