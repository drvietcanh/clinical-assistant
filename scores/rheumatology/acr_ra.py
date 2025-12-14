"""ACR/EULAR RA Classification Criteria 2010"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦴 ACR/EULAR RA Classification</h2><p style='text-align: center;'><em>Tiêu chuẩn phân loại viêm khớp dạng thấp</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ ACR/EULAR 2010"): st.markdown("Tiêu chuẩn chẩn đoán RA. Cần **≥6 điểm** để chẩn đoán RA.")
    st.markdown("---"); joint = st.radio("A. Số khớp/vị trí", [0,1,2,3,5], format_func=lambda x: ["0đ: Không", "1đ: 1 khớp lớn", "2đ: 2-10 khớp lớn", "3đ: 1-3 khớp nhỏ", "5đ: 4-10 khớp nhỏ hoặc >10 khớp"][x]); serology = st.radio("B. Huyết thanh học", [0,2,3], format_func=lambda x: ["0đ: RF(-) và ACPA(-)", "2đ: RF thấp hoặc ACPA thấp", "3đ: RF cao hoặc ACPA cao"][x]); duration = st.radio("C. Thời gian triệu chứng", [0,1], format_func=lambda x: ["0đ: < 6 tuần", "1đ: ≥ 6 tuần"][x]); acute_phase = st.radio("D. Protein giai đoạn cấp", [0,1], format_func=lambda x: ["0đ: CRP và ESR bình thường", "1đ: CRP hoặc ESR tăng"][x]); total = joint + serology + duration + acute_phase
    if st.button("🔬 Đánh giá ACR/EULAR", type="primary", use_container_width=True):
        if total >= 6: st.error(f"🚨 **{total}/10 điểm - Đáp ứng tiêu chuẩn RA**\n\nCó thể chẩn đoán viêm khớp dạng thấp"); st.info("**Điều trị:** DMARDs sớm (Methotrexate), theo dõi hoạt động bệnh (DAS28/CDAI/SDAI)")
        else: st.success(f"✅ **{total}/10 điểm - Chưa đủ tiêu chuẩn RA**\n\nTheo dõi tiếp, có thể là viêm khớp khác hoặc RA giai đoạn sớm")
if __name__ == "__main__": render()

