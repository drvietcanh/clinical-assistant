"""
4AT - 4 A's Test for Delirium Calculator
Sàng lọc mê sảng nhanh (2 phút)
"""

import streamlit as st
from scores.utils.anesthesia_validation import validate_4at_components


def calculate_4at(alertness, amt4, attention, acute_change):
    """
    Tính điểm 4AT
    
    Parameters:
    - alertness: Mức độ tỉnh táo (0=normal, 1=abnormal, 2=severe)
    - amt4: AMT4 test (0=normal, 1=abnormal)
    - attention: Test chú ý (0=normal, 1=abnormal)
    - acute_change: Thay đổi cấp tính (0=no, 1=yes)
    
    Returns:
    - dict với total_score và interpretation
    """
    total = alertness + amt4 + attention + acute_change
    
    # Interpretation
    if total == 0:
        result = "Không có mê sảng"
        recommendation = "Tiếp tục theo dõi, đánh giá lại khi có thay đổi"
        color = "green"
    elif total <= 3:
        result = "Có thể có mê sảng"
        recommendation = "Cần đánh giá thêm bằng CAM-ICU hoặc đánh giá lâm sàng chi tiết"
        color = "orange"
    else:  # ≥4
        result = "Có mê sảng"
        recommendation = "Cần điều trị mê sảng: tìm nguyên nhân, điều chỉnh yếu tố nguy cơ, cân nhắc thuốc"
        color = "red"
    
    return {
        "total_score": total,
        "result": result,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render 4AT interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🧠 4AT - 4 A's Test for Delirium</h2>
    <p style='text-align: center;'><em>Sàng lọc mê sảng nhanh (2 phút)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về 4AT"):
        st.markdown("""
        **4AT (4 A's Test for Delirium)** là công cụ sàng lọc mê sảng nhanh chóng (2 phút),
        có thể sử dụng cho cả bệnh nhân có thể và không thể giao tiếp.
        
        **4 thành phần (tổng 12 điểm):**
        
        1. **Alertness (Mức độ tỉnh táo)** - 0-2 điểm
           - 0 điểm: Tỉnh táo bình thường
           - 1 điểm: Buồn ngủ (nhưng đánh thức được)
           - 2 điểm: Không đánh thức được hoặc kích động
        
        2. **AMT4 (Abbreviated Mental Test 4)** - 0-1 điểm
           - Hỏi 4 câu: Tuổi, Năm sinh, Tên bệnh viện, Ngày trong tuần
           - 0 điểm: Đúng cả 4 câu
           - 1 điểm: Sai ≥1 câu
        
        3. **Attention (Chú ý)** - 0-1 điểm
           - Test: Đếm ngược từ 20 đến 1
           - 0 điểm: Đúng hoặc sai 1-2 lần
           - 1 điểm: Sai ≥3 lần hoặc không thể làm
        
        4. **Acute Change (Thay đổi cấp tính)** - 0-1 điểm
           - 0 điểm: Không có thay đổi cấp tính
           - 1 điểm: Có thay đổi cấp tính trong tình trạng tâm thần
        
        **Điểm số:**
        - **0 điểm:** Không có mê sảng
        - **1-3 điểm:** Có thể có mê sảng (cần đánh giá thêm)
        - **≥4 điểm:** Có mê sảng
        
        **Ưu điểm:**
        - Nhanh chóng (2 phút)
        - Không cần bệnh nhân giao tiếp (có thể đánh giá mức độ tỉnh táo)
        - Độ nhạy và độ đặc hiệu cao
        - Phù hợp cả ICU và phòng bệnh thường
        
        **So sánh với CAM-ICU:**
        - 4AT: Sàng lọc nhanh, phù hợp mọi bệnh nhân
        - CAM-ICU: Chẩn đoán chi tiết, cần bệnh nhân giao tiếp (RASS ≥-3)
        
        **Reference:** Bellelli G, et al. Validation of the 4AT, a new instrument for rapid 
        delirium screening: a study in 234 hospitalised older people. Age Ageing. 2014;43(4):496-502.
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá 4 thành phần")
    
    # Alertness
    st.markdown("### 1️⃣ Alertness (Mức độ tỉnh táo)")
    alertness = st.radio(
        "Mức độ tỉnh táo:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Tỉnh táo bình thường",
            1: "1 điểm - Buồn ngủ (nhưng đánh thức được bằng lời nói hoặc chạm nhẹ)",
            2: "2 điểm - Không đánh thức được hoặc kích động mạnh"
        }[x],
        key="4at_alertness",
        horizontal=False
    )
    
    # AMT4
    st.markdown("### 2️⃣ AMT4 (Abbreviated Mental Test 4)")
    st.markdown("""
    **Hỏi 4 câu hỏi:**
    1. Tuổi của bạn là bao nhiêu?
    2. Năm sinh của bạn là gì?
    3. Tên bệnh viện này là gì? (hoặc địa điểm hiện tại)
    4. Hôm nay là thứ mấy? (hoặc ngày trong tuần)
    
    **Đánh giá:**
    - Đúng cả 4 câu → 0 điểm
    - Sai ≥1 câu → 1 điểm
    """)
    amt4 = st.radio(
        "Kết quả AMT4:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Đúng cả 4 câu",
            1: "1 điểm - Sai ≥1 câu"
        }[x],
        key="4at_amt4",
        horizontal=False
    )
    
    # Attention
    st.markdown("### 3️⃣ Attention (Chú ý)")
    st.markdown("""
    **Test chú ý:**
    - Yêu cầu bệnh nhân đếm ngược từ 20 đến 1
    
    **Đánh giá:**
    - Đúng hoặc sai 1-2 lần → 0 điểm
    - Sai ≥3 lần hoặc không thể làm → 1 điểm
    """)
    attention = st.radio(
        "Kết quả test chú ý:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Đúng hoặc sai 1-2 lần",
            1: "1 điểm - Sai ≥3 lần hoặc không thể làm"
        }[x],
        key="4at_attention",
        horizontal=False
    )
    
    # Acute change
    st.markdown("### 4️⃣ Acute Change (Thay đổi cấp tính)")
    st.markdown("""
    **Đánh giá:**
    - Có thay đổi cấp tính trong tình trạng tâm thần không?
    - So với baseline (trước khi nhập viện hoặc 24-48 giờ trước)
    - Thay đổi trong vài giờ đến vài ngày
    """)
    acute_change = st.radio(
        "Thay đổi cấp tính:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Không có thay đổi cấp tính",
            1: "1 điểm - Có thay đổi cấp tính trong tình trạng tâm thần"
        }[x],
        key="4at_change",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm 4AT", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_4at_components(alertness, amt4, attention, acute_change)
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = calculate_4at(alertness, amt4, attention, acute_change)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Tổng điểm", f"{result['total_score']}/12")
            
            with col2:
                st.metric("Kết quả", result['result'])
            
            st.markdown("---")
            
            # Result interpretation
            if result['color'] == "green":
                st.success(f"**{result['result']}**")
            elif result['color'] == "orange":
                st.warning(f"**{result['result']}**")
            else:
                st.error(f"**{result['result']}**")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            st.markdown("---")
            
            # Breakdown
            st.subheader("📋 Chi tiết điểm số")
            components = [
                ("Alertness", alertness, 2),
                ("AMT4", amt4, 1),
                ("Attention", attention, 1),
                ("Acute Change", acute_change, 1)
            ]
            
            for name, score, max_score in components:
                percentage = (score / max_score) * 100 if max_score > 0 else 0
                st.progress(percentage / 100, text=f"{name}: {score}/{max_score}")
            
            st.markdown("---")
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
        
        # Additional information
        with st.expander("📚 Thông tin bổ sung"):
            st.markdown("""
            **Khi nào sử dụng 4AT:**
            
            - Sàng lọc ban đầu mê sảng
            - Bệnh nhân không thể giao tiếp (có thể đánh giá alertness)
            - Cần kết quả nhanh (2 phút)
            - Phòng bệnh thường (không chỉ ICU)
            
            **Khi nào sử dụng CAM-ICU:**
            
            - Chẩn đoán chi tiết mê sảng
            - Bệnh nhân có thể giao tiếp (RASS ≥-3)
            - ICU (được thiết kế cho ICU)
            - Cần đánh giá đầy đủ 4 đặc điểm
            
            **Điều trị mê sảng (nếu 4AT ≥4):**
            
            1. **Tìm nguyên nhân:**
               - Nhiễm trùng
               - Rối loạn điện giải
               - Thuốc (an thần, kháng cholinergic)
               - Thiếu oxy, tăng CO₂
               - Đau, khó chịu
            
            2. **Điều chỉnh yếu tố nguy cơ:**
               - Giảm liều an thần
               - Đảm bảo giấc ngủ
               - Vận động sớm
               - Kích thích nhận thức
            
            3. **Thuốc (nếu cần):**
               - Haloperidol 0.5-2mg IV/IM
               - Quetiapine 25-100mg PO
               - Olanzapine 2.5-10mg PO/IM
            """)

