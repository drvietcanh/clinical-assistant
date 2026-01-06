"""
Morse Fall Scale
Đánh giá nguy cơ té ngã ở bệnh nhân nội trú
Dùng hàng ngày trong bệnh viện
"""

import streamlit as st

def render_morse_fall(score_id: str = "Morse Fall Scale"):
    """Render Morse Fall Scale calculator"""
    
    st.markdown("### Morse Fall Scale")
    st.markdown("**Đánh giá nguy cơ té ngã ở bệnh nhân nội trú**")
    st.info("""
    **Morse Fall Scale** đánh giá 6 yếu tố nguy cơ té ngã.
    Điểm số từ 0-125, ngưỡng nguy cơ cao: ≥45 điểm.
    
    **Dùng hàng ngày** trong bệnh viện để đánh giá và can thiệp giảm nguy cơ té ngã.
    """)
    
    st.markdown("---")
    
    # Scoring components
    st.markdown("#### Các yếu tố đánh giá")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 1. History of falling
        history_fall = st.selectbox(
            "1. Tiền sử té ngã:",
            ["Không", "Có (trong 3 tháng qua)"],
            key="morse_history"
        )
        score_history = 25 if "Có" in history_fall else 0
        
        # 2. Secondary diagnosis
        secondary_dx = st.selectbox(
            "2. Bệnh lý thứ phát:",
            ["Không", "Có"],
            key="morse_secondary"
        )
        score_secondary = 15 if "Có" in secondary_dx else 0
        
        # 3. Ambulatory aid
        ambulatory_aid = st.selectbox(
            "3. Dụng cụ hỗ trợ di chuyển:",
            ["Không/Bedrest/Nurse assist", "Crutches/Cane/Walker", "Được hỗ trợ giữ thăng bằng khi di chuyển"],
            key="morse_ambulatory"
        )
        if "Crutches/Cane/Walker" in ambulatory_aid:
            score_ambulatory = 15
        elif "Được hỗ trợ" in ambulatory_aid:
            score_ambulatory = 30
        else:
            score_ambulatory = 0
    
    with col2:
        # 4. IV/Heparin Lock
        iv_lock = st.selectbox(
            "4. Có IV/Heparin lock:",
            ["Không", "Có"],
            key="morse_iv"
        )
        score_iv = 20 if "Có" in iv_lock else 0
        
        # 5. Gait
        gait = st.selectbox(
            "5. Dáng đi:",
            ["Bình thường/Bedrest/Immobile", "Yếu", "Rối loạn"],
            key="morse_gait"
        )
        if "Yếu" in gait:
            score_gait = 10
        elif "Rối loạn" in gait:
            score_gait = 20
        else:
            score_gait = 0
        
        # 6. Mental status
        mental_status = st.selectbox(
            "6. Tình trạng tinh thần:",
            ["Oriented to own ability", "Quên giới hạn của bản thân"],
            key="morse_mental"
        )
        score_mental = 15 if "Quên" in mental_status else 0
    
    # Calculate total score
    total_score = score_history + score_secondary + score_ambulatory + score_iv + score_gait + score_mental
    
    st.markdown("---")
    
    # Results
    st.markdown("#### Kết quả")
    st.markdown(f"### **Điểm số: {total_score}**")
    
    if total_score < 25:
        st.success("**Nguy cơ thấp (0-24 điểm)**")
        st.markdown("""
        **Can thiệp:**
        - Theo dõi thông thường
        - Đánh giá lại khi có thay đổi tình trạng
        """)
    elif total_score < 45:
        st.warning("**Nguy cơ trung bình (25-44 điểm)**")
        st.markdown("""
        **Can thiệp:**
        - Đánh giá lại thường xuyên (mỗi ca làm việc)
        - Giáo dục bệnh nhân về nguy cơ té ngã
        - Xem xét các biện pháp an toàn (giường thấp, đèn gọi, v.v.)
        """)
    else:
        st.error("**Nguy cơ cao (≥45 điểm)**")
        st.markdown("""
        **Can thiệp ngay:**
        - Đánh giá hàng ngày
        - Đặt giường ở vị trí thấp nhất
        - Đèn gọi trong tầm với
        - Đặt biển cảnh báo nguy cơ té ngã
        - Hỗ trợ khi di chuyển
        - Xem xét sử dụng dụng cụ hỗ trợ
        - Đánh giá thuốc có thể gây té ngã
        - Giáo dục bệnh nhân và người nhà
        """)
    
    st.markdown("---")
    
    # References
    st.markdown("#### References")
    st.markdown("""
    - Morse JM, et al. A prospective study to identify the fall-prone patient. Soc Sci Med. 1989;28(1):81-93.
    - Morse JM. Preventing patient falls. Sage Publications, 2008.
    """)
