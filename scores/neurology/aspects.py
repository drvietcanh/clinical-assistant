"""
ASPECTS - Alberta Stroke Program Early CT Score
Assessment of early ischemic changes on CT head for stroke patients
Used to determine eligibility for thrombolysis/thrombectomy

Reference:
Barber PA, et al. Validity and reliability of a quantitative computed tomography score in predicting outcome of hyperacute stroke before thrombolytic therapy.
Lancet. 2000;355(9216):1670-1674.
"""

import streamlit as st


def calculate_aspects(regions):
    """
    Calculate ASPECTS Score
    
    Args:
        regions: dict with 10 regions (M1-M6, Insula, Caudate, Lentiform, Internal Capsule)
                Each region: 1 = normal, 0 = early ischemic change
    
    Returns:
        dict with total score and interpretation
    """
    # ASPECTS = 10 - number of regions with early ischemic changes
    total_score = 10 - sum(1 for v in regions.values() if v == 0)
    
    # Interpretation
    if total_score >= 7:
        interpretation = "Low risk - Favorable for thrombolysis/thrombectomy"
        color = "success"
    elif total_score >= 4:
        interpretation = "Moderate risk - Consider carefully"
        color = "warning"
    else:
        interpretation = "High risk - Poor prognosis, may not benefit from thrombolysis"
        color = "error"
    
    return {
        "total_score": total_score,
        "regions_affected": 10 - total_score,
        "interpretation": interpretation,
        "color": color
    }


def render():
    """ASPECTS Score Calculator"""
    st.subheader("🧠 ASPECTS Score")
    st.caption("Alberta Stroke Program Early CT Score - Stroke Imaging Assessment")
    
    st.info("""
    **ASPECTS** đánh giá thay đổi thiếu máu sớm trên CT đầu ở bệnh nhân đột quỵ.
    
    **Mục đích:**
    - Xác định bệnh nhân có thể hưởng lợi từ thrombolysis/thrombectomy
    - Tiên lượng kết cục
    - Quyết định điều trị
    
    **10 Vùng đánh giá:**
    - M1-M6: Middle cerebral artery territories
    - Insula, Caudate, Lentiform, Internal Capsule
    
    **Điểm số:** 0-10 (10 = bình thường, 0 = thay đổi nhiều)
    """)
    
    st.markdown("---")
    
    # Instructions
    st.markdown("### 📋 Hướng Dẫn Đánh giá")
    
    with st.expander("🔍 Xem hướng dẫn đánh giá", expanded=True):
        st.markdown("""
        **Đánh giá từng vùng trên CT đầu:**
        
        **1 = Bình thường (Normal):**
        - Không có thay đổi thiếu máu
        - Mật độ bình thường
        - Ranh giới rõ
        
        **0 = Có thay đổi thiếu máu sớm (Early Ischemic Change):**
        - Giảm mật độ (hypodensity)
        - Mất ranh giới chất xám-chất trắng
        - Phù nề nhẹ
        - Mất sulci
        
        **⚠️ Lưu ý:**
        - Đánh giá trên CT không tiêm thuốc cản quang
        - So sánh 2 bên (bên đối diện làm control)
        - Cần kinh nghiệm đọc CT
        - Nếu không chắc, chọn "Bình thường" (conservative)
        """)
    
    st.markdown("---")
    
    # Visual guide
    st.markdown("### 🗺️ Sơ Đồ 10 Vùng ASPECTS")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Vùng MCA (Middle Cerebral Artery):**
        
        **M1:** Anterior MCA territory (frontal)
        **M2:** MCA territory anterior to M1
        **M3:** Lateral MCA territory
        **M4:** Posterior MCA territory
        **M5:** MCA territory posterior to M4
        **M6:** Superior MCA territory
        """)
    
    with col2:
        st.markdown("""
        **Vùng Deep Structures:**
        
        **Caudate:** Nhân đuôi
        **Lentiform:** Nhân bèo (Putamen + Globus pallidus)
        **Internal Capsule:** Bao trong
        **Insula:** Vỏ não insula
        """)
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📊 Đánh giá 10 Vùng")
    
    st.markdown("**Vùng MCA (M1-M6):**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        m1 = st.radio("M1", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_m1", horizontal=True)
        m2 = st.radio("M2", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_m2", horizontal=True)
    
    with col2:
        m3 = st.radio("M3", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_m3", horizontal=True)
        m4 = st.radio("M4", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_m4", horizontal=True)
    
    with col3:
        m5 = st.radio("M5", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_m5", horizontal=True)
        m6 = st.radio("M6", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_m6", horizontal=True)
    
    st.markdown("---")
    st.markdown("**Vùng Deep Structures:**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        insula = st.radio("Insula", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_insula", horizontal=True)
    
    with col2:
        caudate = st.radio("Caudate", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_caudate", horizontal=True)
    
    with col3:
        lentiform = st.radio("Lentiform", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_lentiform", horizontal=True)
    
    with col4:
        internal_capsule = st.radio("Internal Capsule", ["1 - Bình thường", "0 - Có thay đổi"], key="aspects_ic", horizontal=True)
    
    st.markdown("---")
    
    # Calculate
    regions = {
        "M1": 1 if "Bình thường" in m1 else 0,
        "M2": 1 if "Bình thường" in m2 else 0,
        "M3": 1 if "Bình thường" in m3 else 0,
        "M4": 1 if "Bình thường" in m4 else 0,
        "M5": 1 if "Bình thường" in m5 else 0,
        "M6": 1 if "Bình thường" in m6 else 0,
        "Insula": 1 if "Bình thường" in insula else 0,
        "Caudate": 1 if "Bình thường" in caudate else 0,
        "Lentiform": 1 if "Bình thường" in lentiform else 0,
        "Internal Capsule": 1 if "Bình thường" in internal_capsule else 0,
    }
    
    result = calculate_aspects(regions)
    
    # Display results
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 Kết quả")
        
        if result["color"] == "success":
            st.success(f"## **ASPECTS Score: {result['total_score']}/10**")
        elif result["color"] == "warning":
            st.warning(f"## **ASPECTS Score: {result['total_score']}/10**")
        else:
            st.error(f"## **ASPECTS Score: {result['total_score']}/10**")
        
        st.markdown(f"**Vùng bị ảnh hưởng:** {result['regions_affected']}/10")
        st.markdown(f"**Đánh giá:** {result['interpretation']}")
        
        # Show affected regions
        affected_regions = [k for k, v in regions.items() if v == 0]
        if affected_regions:
            st.markdown(f"**Vùng có thay đổi:** {', '.join(affected_regions)}")
        else:
            st.success("✅ Không có vùng nào bị ảnh hưởng")
    
    with col2:
        st.markdown("### 📈 Tiên Lượng")
        
        if result["total_score"] >= 7:
            st.success("""
            **✅ Favorable:**
            - Có thể hưởng lợi từ thrombolysis
            - Có thể hưởng lợi từ thrombectomy
            - Tiên lượng tốt hơn
            """)
        elif result["total_score"] >= 4:
            st.warning("""
            **⚠️ Moderate:**
            - Cân nhắc cẩn thận
            - Có thể vẫn hưởng lợi
            - Tiên lượng trung bình
            """)
        else:
            st.error("""
            **🚨 Poor:**
            - Nguy cơ cao không hưởng lợi
            - Nguy cơ xuất huyết cao
            - Tiên lượng xấu
            """)
    
    st.markdown("---")
    
    # Clinical implications
    st.markdown("### 💊 Ý Nghĩa Lâm Sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Thrombolysis (tPA):**
        - **ASPECTS ≥7:** Có thể dùng tPA (nếu đủ tiêu chuẩn khác)
        - **ASPECTS 4-6:** Cân nhắc cẩn thận
        - **ASPECTS <4:** Thường không khuyến nghị
        
        **Thrombectomy:**
        - **ASPECTS ≥6:** Có thể hưởng lợi
        - **ASPECTS <6:** Cân nhắc cẩn thận
        - Phụ thuộc vào các yếu tố khác (thời gian, occlusion site)
        """)
    
    with col2:
        st.markdown("""
        **Tiên lượng:**
        - **ASPECTS ≥7:** Tỷ lệ phục hồi tốt cao hơn
        - **ASPECTS 4-6:** Tỷ lệ phục hồi trung bình
        - **ASPECTS <4:** Tỷ lệ phục hồi kém
        
        **⚠️ Lưu ý:**
        - ASPECTS chỉ là một yếu tố
        - Cần kết hợp với lâm sàng, thời gian, occlusion site
        - Quyết định điều trị phải toàn diện
        """)
    
    st.markdown("---")
    
    # References
    st.markdown("### 📚 Tài Liệu Tham Khảo")
    
    st.markdown("""
    1. **Barber PA, et al.** Validity and reliability of a quantitative computed tomography score in predicting outcome of hyperacute stroke before thrombolytic therapy.
       Lancet. 2000;355(9216):1670-1674.
    
    2. **Pexman JH, et al.** Use of the Alberta Stroke Program Early CT Score (ASPECTS) for assessing CT scans in patients with acute stroke.
       AJNR Am J Neuroradiol. 2001;22(8):1534-1542.
    
    3. **UpToDate:** Acute ischemic stroke - Neuroimaging - Last updated 2024
       - ASPECTS scoring
       - Thrombolysis eligibility
    
    4. **AHA/ASA Guidelines** - Acute Stroke Management (2021)
       - ASPECTS in treatment decision
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ ASPECTS chỉ mang tính tham khảo. Quyết định điều trị phải dựa trên đánh giá toàn diện bởi bác sĩ có kinh nghiệm. Đọc CT cần kinh nghiệm và có thể có sự khác biệt giữa các người đọc.")

