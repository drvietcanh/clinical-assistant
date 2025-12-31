import streamlit as st

def render_sickle_cell_crisis():
    st.header("🩸 Cơn Đau Hồng Cầu Hình Liềm (Sickle Cell Pain Crisis)")
    st.caption("Dựa trên hướng dẫn ASH 2020")

    st.error("🚨 Vaso-occlusive Crisis (VOC) - Cần giảm đau tích cực trong vòng 1 giờ.")

    st.subheader("1. Đánh giá & Xử trí ban đầu")
    st.markdown("- **Đánh giá đau:** Sử dụng thang điểm ngay lập tức. Tin tưởng lời khai của bệnh nhân (họ thường có kinh nghiệm).")
    st.markdown("- **Tìm yếu tố thúc đẩy:** Nhiễm trùng, mất nước, lạnh, stress, độ cao.")
    st.markdown("- **Xét nghiệm:** Công thức máu (Hct, Reticulocyte để loại trừ cơn bất sản), Nhóm máu.")

    st.markdown("---")
    st.subheader("2. Giảm đau (Trong vòng 60 phút)")
    st.warning("Mục tiêu: Giảm đau nhanh chóng.")
    
    st.markdown("**A. Opioids (Lựa chọn chính):**")
    st.markdown("- Dùng đường tĩnh mạch (IV) hoặc dưới da (SC). Tránh tiêm bắp.")
    st.markdown("- **Morphine Sulfate:** 0.1 mg/kg IV.")
    st.markdown("- **Hydromorphone:** 0.015 mg/kg IV.")
    st.markdown("- Đánh giá lại mỗi 15-30 phút. Lặp lại liều cho đến khi kiểm soát đau.")
    st.markdown("- Dùng PCA (Patient Controlled Analgesia) nếu nhập viện.")

    st.markdown("**B. Adjuvant (Hỗ trợ):**")
    st.markdown("- **NSAIDs:** Ketorolac hoặc Ibuprofen (tăng hiệu quả opioid).")
    st.markdown("- **Ketamine liều thấp:** Cân nhắc nếu đau kháng trị.")
    st.markdown("- **Dịch truyền:** Duy trì thể tích nội mạch (Euvelomia). Tránh quá tải dịch (gây phù phổi cấp/hội chứng ngực cấp). Ưu tiên dịch nhược trương (D5 1/2NS).")

    st.markdown("---")
    st.subheader("3. Biến chứng Cấp cứu")
    st.error("**Hội chứng Ngực cấp (Acute Chest Syndrome - ACS):**")
    st.markdown("- **Dấu hiệu:** Sốt + Triệu chứng hô hấp (ho, đau ngực, khó thở) + Tổn thương phổi mới trên X-quang.")
    st.markdown("- **Xử trí:** Oxy, Giảm đau, Kháng sinh (Macrolide + Cephalosporin), Truyền máu (Simple hoặc Exchange) để giảm HbS < 30%.")
