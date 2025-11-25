"""SLICC Classification Criteria for SLE"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦋 SLICC Criteria</h2><p style='text-align: center;'><em>Tiêu chuẩn Lupus ban đỏ hệ thống</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ SLICC 2012"): st.markdown("**SLICC 2012** chẩn đoán SLE. Cần **≥4 tiêu chuẩn** (ít nhất 1 lâm sàng + 1 miễn dịch) HOẶC **Lupus nephritis + ANA/anti-dsDNA**")
    st.markdown("---"); st.markdown("### Lâm sàng (Clinical):"); acute_cutaneous = st.checkbox("1. Da cấp (hồng bướm...)"); chronic_cutaneous = st.checkbox("2. Da mạn (lupus disoid...)"); oral_ulcers = st.checkbox("3. Loét miệng"); alopecia = st.checkbox("4. Rụng tóc"); arthritis = st.checkbox("5. Viêm khớp"); serositis = st.checkbox("6. Viêm màng (màng phổi/tim)"); renal = st.checkbox("7. Thận (protein niệu)"); neuro = st.checkbox("8. Thần kinh (co giật, loạn thần)"); hemolytic = st.checkbox("9. Thiếu máu tan máu"); leukopenia = st.checkbox("10. Giảm bạch cầu/lympho"); thrombocytopenia = st.checkbox("11. Giảm tiểu cầu"); clinical_score = sum([acute_cutaneous, chronic_cutaneous, oral_ulcers, alopecia, arthritis, serositis, renal, neuro, hemolytic, leukopenia, thrombocytopenia])
    st.markdown("### Miễn dịch (Immunologic):"); ana = st.checkbox("1. ANA (+)"); anti_dsdna = st.checkbox("2. Anti-dsDNA"); anti_sm = st.checkbox("3. Anti-Sm"); antiphospholipid = st.checkbox("4. Antiphospholipid Ab"); low_complement = st.checkbox("5. Giảm complement (C3, C4, CH50)"); coombs = st.checkbox("6. Coombs test (+)"); immuno_score = sum([ana, anti_dsdna, anti_sm, antiphospholipid, low_complement, coombs]); total = clinical_score + immuno_score
    if st.button("🔬 Đánh giá SLICC", type="primary", use_container_width=True):
        lupus_nephritis_positive = renal and (ana or anti_dsdna)
        if (total >= 4 and clinical_score >= 1 and immuno_score >= 1) or lupus_nephritis_positive: st.error(f"🚨 **Đáp ứng tiêu chuẩn SLE (SLICC 2012)**\n\n- Tổng: {total} tiêu chuẩn\n- Lâm sàng: {clinical_score}\n- Miễn dịch: {immuno_score}"); st.info("**Điều Trị:** Hydroxychloroquine + Glucocorticoid ± Immunosuppressants")
        else: st.success(f"✅ **Chưa đủ tiêu chuẩn SLE**\n\n- Tổng: {total} tiêu chuẩn\n- Lâm sàng: {clinical_score}\n- Miễn dịch: {immuno_score}\n\nTheo dõi tiếp, cân nhắc bệnh khác")
if __name__ == "__main__": render()

