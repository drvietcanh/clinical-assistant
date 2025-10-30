"""CIPN - Chemotherapy-Induced Peripheral Neuropathy Grading"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #8B5CF6;'>💊 CIPN Grading</h2><p style='text-align: center;'><em>Phân độ tổn thương thần kinh ngoại biên do hóa trị</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ CIPN"): st.markdown("**CIPN** phân độ tổn thương thần kinh ngoại biên do hóa trị (taxanes, platinum, vinca alkaloids). **Độ:** 0-4")
    st.markdown("---"); grade = st.radio("Chọn độ CIPN:", [0,1,2,3,4], format_func=lambda x: ["0: Không triệu chứng", "1: Tê nhẹ, không ảnh hưởng chức năng", "2: Tê/đau trung bình, ảnh hưởng ADL", "3: Tê/đau nặng, ảnh hưởng ADL nặng", "4: Liệt, mất chức năng"][x])
    if st.button("🔬 Đánh giá CIPN", type="primary", use_container_width=True):
        if grade == 0: st.success("✅ **Độ 0:** Không CIPN")
        elif grade == 1: st.info("**Độ 1:** CIPN nhẹ - Tiếp tục hóa trị, theo dõi")
        elif grade == 2: st.warning("⚠️ **Độ 2:** CIPN trung bình - Cân nhắc giảm liều 25%")
        elif grade == 3: st.error("🚨 **Độ 3:** CIPN nặng - Tạm ngừng hóa trị đến khi giảm xuống Độ 1")
        else: st.error("🆘 **Độ 4:** Liệt - NGỪNG hóa trị gây CIPN"); st.info("""**Điều trị CIPN:** Duloxetine (30-60mg/ngày) - Bằng chứng tốt nhất""")
if __name__ == "__main__": render()

