"""P-POSSUM - Portsmouth Physiological and Operative Severity Score"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #DC2626;'>🏥 P-POSSUM Score</h2><p style='text-align: center;'><em>Nguy cơ tử vong phẫu thuật</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ P-POSSUM"): st.markdown("**P-POSSUM** dự đoán tử vong sau phẫu thuật dựa trên 12 yếu tố sinh lý và 6 yếu tố phẫu thuật. Phức tạp, thường dùng trong nghiên cứu.")
    st.markdown("---"); st.warning("⚠️ **Lưu ý:** P-POSSUM rất phức tạp (18 biến số), thường cần máy tính chuyên dụng. Đây là phiên bản đơn giản hóa."); age = st.number_input("Tuổi", 20, 100, 60); cardiac = st.selectbox("Tim mạch", ["Bình thường", "Bệnh tim", "Suy tim"]); respiratory = st.selectbox("Hô hấp", ["Bình thường", "Khó thở nhẹ", "COPD"]); bp = st.number_input("SBP (mmHg)", 50, 200, 120); pulse_rate = st.number_input("Mạch", 40, 150, 80); gcs_score = st.number_input("GCS", 3, 15, 15); operation_severity = st.selectbox("Mức độ phẫu thuật", ["Nhỏ", "Trung bình", "Lớn", "Lớn+"])
    if st.button("🔬 Ước tính P-POSSUM", type="primary", use_container_width=True):
        risk_score = 0; risk_score += max(0, (age - 60) // 5); risk_score += 1 if cardiac != "Bình thường" else 0; risk_score += 1 if respiratory != "Bình thường" else 0; risk_score += 1 if bp < 100 else 0; risk_score += 1 if gcs_score < 15 else 0; risk_score += {"Nhỏ": 0, "Trung bình": 1, "Lớn": 2, "Lớn+": 3}[operation_severity]
        if risk_score <= 2: risk = "Thấp (<5%)"; color = "#28a745"
        elif risk_score <= 4: risk = "Trung bình (5-15%)"; color = "#fd7e14"
        else: risk = "Cao (>15%)"; color = "#dc3545"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>Nguy cơ: {risk}</h2></div>", unsafe_allow_html=True); st.info("💡 **Lưu ý:** Đây chỉ là ước tính đơn giản. P-POSSUM thực tế cần 18 biến số và công thức phức tạp.")
if __name__ == "__main__": render()

