"""
Burn TBSA Calculator - Rule of Nines
Tính diện tích bỏng theo Quy tắc số 9
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================
from scores.utils.validation import (
    validate_range,
    validate_positive
)
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result


def calculate_tbsa(head, chest, abdomen, back_upper, back_lower, 
                   arm_right, arm_left, leg_right, leg_left, genitalia):
    """Tính % TBSA bỏng"""
    total = (head + chest + abdomen + back_upper + back_lower + 
             arm_right + arm_left + leg_right + leg_left + genitalia)
    
    if total < 10:
        severity = "Nhẹ (Minor)"
        management = "Điều trị ngoại trú nếu không bỏng sâu"
        color = COLORS["success"]
    elif total < 20:
        severity = "Trung bình (Moderate)"
        management = "Cần nhập viện"
        color = COLORS["warning"]
    else:
        severity = "Nặng (Major)"
        management = "Cần chuyển trung tâm bỏng, hồi sức tích cực"
        color = COLORS["error"]
    
    # Parkland formula
    fluid_24h = total * 4  # ml/kg (will multiply by weight)
    
    return {"total_tbsa": total, "severity": severity, "management": management, 
            "color": color, "fluid_factor": fluid_24h}


def render():
    """Render Burn TBSA calculator interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'burn_tbsa':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Burn TBSA')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🔥 Burn TBSA - Rule of Nines</h3>
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
                            min_value=10, max_value=200, value=50, step=1, format="%d")
    
    st.markdown("---")
    
    if st.button("🔬 Tính TBSA", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Weight validation
        is_valid_weight, weight_error = validate_positive(weight, "Cân nặng")
        if not is_valid_weight:
            validation_errors.append(f"Cân nặng: {weight_error}")
        elif weight < 10.0:
            validation_errors.append("Cân nặng phải ≥ 10 kg")
        elif weight > 200.0:
            validation_errors.append("Cân nặng phải ≤ 200 kg")
        
        # TBSA validation (should be 0-100%)
        total_tbsa_input = head + chest + abdomen + back_upper + back_lower + arm_right + arm_left + leg_right + leg_left + genitalia
        if total_tbsa_input > 100:
            validation_errors.append(f"Tổng TBSA ({total_tbsa_input}%) không thể > 100%")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_tbsa(head, chest, abdomen, back_upper, back_lower,
                               arm_right, arm_left, leg_right, leg_left, genitalia)
        
        st.markdown("---")
        st.subheader("📊 Kết quả")
        
        # Determine icon
        if result['color'] == COLORS["success"]:
            icon = "🟢"
        elif result['color'] == COLORS["warning"]:
            icon = "🟠"
        else:
            icon = "🔴"

        render_score_result(
            title="Diện tích bỏng (TBSA)",
            score=f"{result['total_tbsa']}%",
            interpretation=f"{result['severity']}",
            mortality=result['management'],
            color=result['color'],
            icon=icon,
            size="large"
        )
        
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
        - Điều chỉnh theo nước tiểu: Mục tiêu 0.5-1 ml/kg/h (Người lớn)
        - Theo dõi sát: BP, HR, nước tiểu, lactate
        """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Head": f"{head}%",
            "Chest": f"{chest}%",
            "Abdomen": f"{abdomen}%",
            "Back Upper": f"{back_upper}%",
            "Back Lower": f"{back_lower}%",
            "Arm Right": f"{arm_right}%",
            "Arm Left": f"{arm_left}%",
            "Leg Right": f"{leg_right}%",
            "Leg Left": f"{leg_left}%",
            "Genitalia": f"{genitalia}%",
            "Weight": f"{weight} kg"
        }
        
        results_dict = {
            "TBSA": f"{result['total_tbsa']}%",
            "Severity": result['severity'],
            "Management": result['management'],
            "Total Fluid 24h": f"{total_fluid:.0f} ml",
            "First 8h": f"{first_8h:.0f} ml",
            "Next 16h": f"{next_16h:.0f} ml"
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="Burn TBSA",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="Burn TBSA"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="burn_tbsa",
            calculator_name="Burn TBSA",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="burn_tbsa",
            calculator_name="Burn TBSA",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="burn_tbsa", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="burn_tbsa",
            calculator_name="Burn TBSA",
            category="Da liễu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("Burn TBSA")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

