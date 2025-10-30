"""
RCRI - Revised Cardiac Risk Index Calculator
Đánh giá nguy cơ tim mạch phẫu thuật (Lee's Index)
"""

import streamlit as st


def calculate_rcri(high_risk_surgery, ischemic_heart, chf, cvd, dm_insulin, creat):
    """
    Tính RCRI
    Mỗi yếu tố = 1 điểm
    """
    total = high_risk_surgery + ischemic_heart + chf + cvd + dm_insulin + creat
    
    if total == 0:
        risk = "Rất thấp"
        rate = "0.4-0.5%"
        color = "green"
    elif total == 1:
        risk = "Thấp"
        rate = "0.9-1.3%"
        color = "green"
    elif total == 2:
        risk = "Trung bình"
        rate = "4-7%"
        color = "orange"
    else:  # >= 3
        risk = "Cao"
        rate = "≥9-11%"
        color = "red"
    
    return {"total_score": total, "risk_level": risk, "cardiac_event_rate": rate, "color": color}


def render():
    """Render RCRI calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #DC2626;'>❤️ RCRI - Revised Cardiac Risk Index</h2>
    <p style='text-align: center;'><em>Nguy cơ biến chứng tim mạch phẫu thuật (Lee's Index)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về RCRI"):
        st.markdown("""
        **RCRI (Revised Cardiac Risk Index)**, còn gọi là **Lee's Index**, đánh giá nguy cơ 
        biến chứng tim mạch lớn sau phẫu thuật không tim.
        
        **Biến chứng tim mạch lớn:**
        - Nhồi máu cơ tim
        - Ngưng tim
        - Phù phổi cấp
        - Block tim hoàn toàn
        - Rung thất
        
        **Mục đích:** Đánh giá nguy cơ tiền phẫu để tối ưu hóa quản lý
        
        **Thang điểm:** 0-6 điểm
        """)
    
    st.markdown("---")
    st.subheader("📝 Đánh giá 6 yếu tố nguy cơ")
    
    high_risk_surgery = st.checkbox(
        "Phẫu thuật nguy cơ cao",
        help="Phẫu thuật trong ổ bụng, ngực, mạch máu lớn"
    )
    
    ischemic_heart = st.checkbox(
        "Bệnh tim thiếu máu cục bộ",
        help="Tiền sử nhồi máu cơ tim, test gắng sức dương, đau thắt ngực, dùng nitrate, sóng Q bệnh lý trên ECG"
    )
    
    chf = st.checkbox(
        "Suy tim",
        help="Tiền sử suy tim, phù phổi, PND, ran ẩm, S3 tim, X-quang phù phổi"
    )
    
    cvd = st.checkbox(
        "Bệnh mạch não",
        help="Tiền sử đột quỵ hoặc TIA"
    )
    
    dm_insulin = st.checkbox(
        "Đái tháo đường dùng insulin",
        help="Đái tháo đường cần điều trị bằng insulin"
    )
    
    creat = st.checkbox(
        "Creatinine > 2 mg/dL (> 177 μmol/L)",
        help="Suy thận mạn"
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính RCRI", type="primary", use_container_width=True):
        result = calculate_rcri(
            1 if high_risk_surgery else 0,
            1 if ischemic_heart else 0,
            1 if chf else 0,
            1 if cvd else 0,
            1 if dm_insulin else 0,
            1 if creat else 0
        )
        
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                RCRI: {result['total_score']}/6
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color};'>🎯 Nguy cơ: {result['risk_level']}</h3>
            <p style='font-size: 1.2em;'><strong>Tỷ lệ biến chứng tim mạch lớn:</strong> {result['cardiac_event_rate']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if result["total_score"] <= 1:
            st.success("""
            ✅ **Nguy cơ thấp (0-1 điểm)**
            
            **Quản lý:**
            - Phẫu thuật tiến hành bình thường
            - Không cần xét nghiệm tim mạch thêm
            - Tiếp tục thuốc beta-blocker nếu đang dùng
            - Theo dõi ECG, Troponin sau mổ nếu có triệu chứng
            """)
        elif result["total_score"] == 2:
            st.warning("""
            ⚠️ **Nguy cơ trung bình (2 điểm)**
            
            **Quản lý:**
            - Cân nhắc xét nghiệm thêm (Echo, test gắng sức)
            - Beta-blocker nếu chưa có chống chỉ định
            - Tối ưu hóa điều trị nội khoa
            - Theo dõi sát sau mổ
            - ECG, Troponin sau mổ
            """)
        else:
            st.error("""
            🚨 **Nguy cơ cao (≥3 điểm)**
            
            **Quản lý:**
            - ⚠️ Đánh giá tim mạch toàn diện
            - Echo tim
            - Test gắng sức hoặc imaging stress
            - Cân nhắc chụp mạch vành nếu cần
            - Beta-blocker (nếu không chống chỉ định)
            - Statin
            - Aspirin (cân nhắc dừng trước mổ tùy loại phẫu thuật)
            - Theo dõi ICU sau mổ
            - ECG, Troponin định kỳ
            
            **Cân nhắc:**
            - Can thiệp tim trước (PCI, CABG) nếu cần
            - Hoãn phẫu thuật không cấp cứu để tối ưu hóa
            """)
        
        with st.expander("📊 Bảng phân loại RCRI"):
            st.markdown("""
            | Điểm | Nguy cơ | Biến chứng tim mạch lớn |
            |:----:|:--------|:------------------------|
            | 0 | Rất thấp | 0.4-0.5% |
            | 1 | Thấp | 0.9-1.3% |
            | 2 | Trung bình | 4-7% |
            | ≥3 | Cao | ≥9-11% |
            """)


if __name__ == "__main__":
    render()

