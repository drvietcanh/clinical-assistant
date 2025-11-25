"""
Burn TBSA Calculator - Rule of Nines
Tính diện tích bỏng theo Quy tắc số 9
"""

import streamlit as st


def calculate_tbsa(head, chest, abdomen, back_upper, back_lower, 
                   arm_right, arm_left, leg_right, leg_left, genitalia):
    """Tính % TBSA bỏng"""
    total = (head + chest + abdomen + back_upper + back_lower + 
             arm_right + arm_left + leg_right + leg_left + genitalia)
    
    if total < 10:
        severity = "Nhẹ (Minor)"
        management = "Điều trị ngoại trú nếu không bỏng sâu"
        color = "green"
    elif total < 20:
        severity = "Trung bình (Moderate)"
        management = "Cần nhập viện"
        color = "orange"
    else:
        severity = "Nặng (Major)"
        management = "Cần chuyển trung tâm bỏng, hồi sức tích cực"
        color = "red"
    
    # Parkland formula
    fluid_24h = total * 4  # ml/kg (will multiply by weight)
    
    return {"total_tbsa": total, "severity": severity, "management": management, 
            "color": color, "fluid_factor": fluid_24h}


def render():
    """Render Burn TBSA calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #F59E0B;'>🔥 Burn TBSA - Rule of Nines</h2>
    <p style='text-align: center;'><em>Tính diện tích bỏng (Total Body Surface Area)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Quy tắc số 9 (Rule of Nines)"):
        st.markdown("""
        **Rule of Nines** là phương pháp nhanh ước tính % diện tích bỏng ở người lớn.
        
        **Phân bố theo 9% hoặc bội số của 9:**
        - Đầu cổ: 9%
        - Mỗi tay: 9%
        - Ngực: 9%
        - Bụng: 9%
        - Lưng trên: 9%
        - Lưng dưới: 9%
        - Mỗi chân (mặt trước): 9%
        - Mỗi chân (mặt sau): 9%
        - Bộ phận sinh dục: 1%
        
        **Tổng = 100%**
        
        **Lưu ý:** Chỉ tính bỏng độ 2 và độ 3 (không tính độ 1)
        """)
    
    st.markdown("---")
    st.subheader("📝 Chọn vùng bị bỏng")
    
    st.info("💡 Chỉ tính bỏng độ 2 (phồng rộp) và độ 3 (da chết), không tính độ 1 (đỏ)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        head = st.selectbox("👤 Đầu + Cổ", [0, 9], format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
        chest = st.selectbox("🫁 Ngực", [0, 9], format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
        abdomen = st.selectbox("🫃 Bụng", [0, 9], format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
        back_upper = st.selectbox("⬆️ Lưng trên", [0, 9], format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
        back_lower = st.selectbox("⬇️ Lưng dưới", [0, 9], format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
        genitalia = st.selectbox("🔻 Bộ phận sinh dục", [0, 1], format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
    
    with col2:
        arm_right = st.selectbox("🦾 Tay phải", [0, 9], format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
        arm_left = st.selectbox("🦾 Tay trái", [0, 9], format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
        leg_right = st.selectbox("🦵 Chân phải (mặt trước + sau)", [0, 9, 18], 
                                format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
        leg_left = st.selectbox("🦵 Chân trái (mặt trước + sau)", [0, 9, 18],
                               format_func=lambda x: f"{x}%" if x > 0 else "Không bỏng")
    
    st.markdown("---")
    
    # Weight for Parkland formula
    weight = st.number_input("⚖️ Cân nặng (kg) - để tính Parkland formula",
                            min_value=10.0, max_value=200.0, value=70.0, step=1.0, format="%.1f")
    
    st.markdown("---")
    
    if st.button("🔬 Tính TBSA", type="primary", use_container_width=True):
        result = calculate_tbsa(head, chest, abdomen, back_upper, back_lower,
                               arm_right, arm_left, leg_right, leg_left, genitalia)
        
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                TBSA: {result['total_tbsa']}%
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color};'>Mức độ: {result['severity']}</h3>
            <p style='font-size: 1.1em;'>{result['management']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 💧 Parkland Formula - Dịch truyền 24h đầu")
        
        total_fluid = result["fluid_factor"] * weight
        first_8h = total_fluid / 2
        next_16h = total_fluid / 2
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tổng 24h", f"{total_fluid:.0f} ml")
        with col2:
            st.metric("8h đầu", f"{first_8h:.0f} ml")
        with col3:
            st.metric("16h sau", f"{next_16h:.0f} ml")
        
        st.info(f"""
        **Parkland Formula:** {result['total_tbsa']}% × 4 ml × {weight} kg = **{total_fluid:.0f} ml** Ringer Lactate trong 24h
        
        - **50% (={first_8h:.0f} ml)** trong 8 giờ đầu (tính từ lúc bỏng)
        - **50% (={next_16h:.0f} ml)** trong 16 giờ tiếp theo
        
        ⏱️ Tốc độ truyền 8h đầu: ~{first_8h/8:.0f} ml/giờ
        """)
        
        st.warning("""
        ⚠️ **Lưu ý quan trọng:**
        - Parkland chỉ là công thức khởi đầu
        - Điều chỉnh theo nước tiểu: Mục tiêu 0.5-1 ml/kg/h (Người Lớn)
        - Theo dõi sát: BP, HR, nước tiểu, lactate
        """)


if __name__ == "__main__":
    render()

