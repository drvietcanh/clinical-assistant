"""
Mallampati Classification Calculator
Đánh giá đường thở khó - Dự đoán đặt nội khí quản khó
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def interpret_mallampati(class_num):
    """Interpret Mallampati class"""
    
    if class_num == 1:
        difficulty = "Dễ"
        description = "Nhìn thấy toàn bộ khẩu cái mềm, lưỡi gà, trụ amidan"
        risk = "Rất thấp"
        color = "green"
    elif class_num == 2:
        difficulty = "Tương đối dễ"
        description = "Nhìn thấy khẩu cái mềm, lưỡi gà, phần trên trụ amidan"
        risk = "Thấp"
        color = "green"
    elif class_num == 3:
        difficulty = "Có thể khó"
        description = "Nhìn thấy khẩu cái mềm, một phần lưỡi gà"
        risk = "Trung bình"
        color = "orange"
    else:  # class 4
        difficulty = "Khó"
        description = "Chỉ nhìn thấy khẩu cái cứng"
        risk = "Cao"
        color = "red"
    
    return {
        "class": class_num,
        "difficulty": difficulty,
        "description": description,
        "risk": risk,
        "color": color
    }


def render():
    """Render Mallampati Classification interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'mallampati':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['error']};'>👄 Mallampati Classification</h2>
    <p style='text-align: center;'><em>Đánh giá đường thở khó</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Mallampati"):
        st.markdown("""
        **Mallampati Classification** là công cụ sàng lọc đơn giản để dự đoán 
        đường thở khó và khó khăn khi đặt nội khí quản.
        
        **Mục đích:**
        - Đánh giá tiền phẫu đường thở
        - Dự đoán đặt NKQ khó
        - Chuẩn bị kế hoạch gây mê
        
        **Cách đánh giá:**
        - Bệnh nhân ngồi thẳng
        - Hé miệng tối đa
        - Lưỡi thè ra tối đa (không phát âm)
        - Quan sát thấy cấu trúc nào
        
        **Giới hạn:**
        - Chỉ là một trong nhiều yếu tố đánh giá đường thở
        - Cần kết hợp: khoảng cách thyromental, mở miệng, cử động cổ...
        - Độ nhạy không cao nhưng hữu ích cho sàng lọc
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Chọn Class Mallampati")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="mallampati",
            calculator_name="Mallampati Classification",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Visual guide
    st.markdown(f"""
    <div style='background-color: {COLORS['warning']}22; padding: 15px; border-radius: 10px; border-left: 4px solid {COLORS['warning']}; margin-bottom: 20px;'>
        <p style='margin: 0;'><strong>Cách đánh giá:</strong></p>
        <ul style='margin: 5px 0;'>
            <li>Bệnh nhân ngồi thẳng, đầu ở tư thế trung tính</li>
            <li>Hé miệng tối đa, thè lưỡi ra tối đa</li>
            <li><strong>KHÔNG</strong> phát âm "Ahh" (sẽ làm sai kết quả)</li>
            <li>Quan sát cấu trúc nhìn thấy</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    mallampati_class = st.radio(
        "Chọn Class phù hợp:",
        options=[1, 2, 3, 4],
        format_func=lambda x: {
            1: "Class I - Thấy toàn bộ: Khẩu cái mềm + Lưỡi gà + Trụ amidan",
            2: "Class II - Thấy: Khẩu cái mềm + Lưỡi gà + Phần trên trụ amidan",
            3: "Class III - Thấy: Khẩu cái mềm + Một phần lưỡi gà",
            4: "Class IV - Chỉ thấy: Khẩu cái cứng"
        }[x],
        help="Chọn Class dựa trên cấu trúc nhìn thấy"
    )
    
    st.markdown("---")
    
    # Visual representation
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Hình ảnh minh họa")
        st.markdown("""
        ```
        Class I:   🟢  [====|====|====]
                       Cái  Gà  Trụ
                       mềm      
        
        Class II:  🟢  [====|====|==  ]
                       Cái  Gà  Phần
                       mềm      trên
        
        Class III: 🟡  [====|==  |    ]
                       Cái  1/2
                       mềm  Gà
        
        Class IV:  🔴  [====|    |    ]
                       Chỉ
                       cái
                       cứng
        ```
        """)
    
    with col2:
        st.markdown("### 🔍 Cấu trúc giải phẫu")
        st.markdown("""
        **Khẩu cái mềm (Soft palate):**
        - Phần mềm phía sau khẩu cái
        
        **Lưỡi gà (Uvula):**
        - Cấu trúc lủng lẳng ở giữa
        
        **Trụ amidan (Tonsillar pillars):**
        - Nếp gấp hai bên amidan
        
        **Khẩu cái cứng (Hard palate):**
        - Phần xương ở trước
        """)
    
    if st.button("🔬 Đánh giá Mallampati", type="primary", use_container_width=True):
        result = interpret_mallampati(mallampati_class)
        
        st.markdown("## 📊 Kết quả")
        
        score_color = {
            "green": COLORS["success"],
            "orange": COLORS["warning"],
            "red": COLORS["error"]
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                Mallampati Class {result['class']}
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {result['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Đánh giá</h3>
            <p style='font-size: 1.2em;'><strong>Đường thở:</strong> {result['difficulty']}</p>
            <p style='font-size: 1.2em;'><strong>Nguy cơ đặt NKQ khó:</strong> {result['risk']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Clinical implications
        if result["class"] <= 2:
            st.success("""
            ✅ **Class I-II: Đường thở dễ**
            
            **Ý nghĩa:**
            - Nguy cơ thấp đặt nội khí quản khó
            - Thường dễ dàng soi thanh quản
            
            **Kế hoạch:**
            - Gây mê tiêu chuẩn
            - Chuẩn bị dụng cụ thông thường
            """)
        elif result["class"] == 3:
            st.warning("""
            ⚠️ **Class III: Có thể khó**
            
            **Ý nghĩa:**
            - Nguy cơ trung bình đặt NKQ khó
            - Cần đánh giá thêm các yếu tố khác
            
            **Kế hoạch:**
            - Chuẩn bị kế hoạch dự phòng
            - Có sẵn dụng cụ đặt NKQ khó
            - Cân nhắc có bác sĩ gây mê giàu kinh nghiệm
            """)
        else:  # Class 4
            st.error("""
            🔴 **Class IV: Đường thở khó**
            
            **Ý nghĩa:**
            - Nguy cơ cao đặt NKQ khó
            - Cần đánh giá toàn diện đường thở
            
            **Kế hoạch:**
            - ⚠️ Chuẩn bị kỹ lưỡng cho đường thở khó
            - Có bác sĩ gây mê giàu kinh nghiệm
            - Chuẩn bị đầy đủ dụng cụ (video laryngoscope, LMA, cricothyrotomy kit)
            - Cân nhắc đặt NKQ tỉnh (awake intubation)
            - Thảo luận kế hoạch với bệnh nhân
            """)
        
        # Additional assessment needed
        with st.expander("🔍 Đánh giá toàn diện đường thở"):
            st.markdown("""
            **Mallampati chỉ là 1 phần! Cần đánh giá thêm:**
            
            ### 1. Khoảng cách Thyromental (TMD)
            - Đo từ sụn giáp đến cằm (đầu ngửa tối đa)
            - **< 6 cm (3 ngón tay):** Nguy cơ cao
            
            ### 2. Độ mở miệng
            - Đo khoảng cách giữa răng cửa trên-dưới
            - **< 3 cm (2 ngón tay):** Khó
            
            ### 3. Cử động cổ
            - Ngửa-cúi cổ
            - **Hạn chế:** Khó đặt NKQ
            
            ### 4. Lùi hàm dưới (Jaw protrusion)
            - Đưa răng dưới ra trước răng trên
            - **Không làm được:** Khó
            
            ### 5. Yếu tố khác:
            - Béo phì (BMI > 30)
            - Cổ ngắn, dày
            - Răng cửa nhô
            - Có râu dày
            - Tiền sử đặt NKQ khó
            - Bệnh lý: Sleep apnea, viêm khớp, khối u cổ...
            
            ### Thang điểm tổng hợp:
            - **Wilson Score**
            - **LEMON Score**
            - **El-Ganzouri Score**
            """)
        
        with st.expander("📋 Kế hoạch đường thở khó"):
            st.markdown("""
            ### ASA Difficult Airway Algorithm:
            
            **1. Đánh giá:**
            - Khả năng đặt NKQ khó?
            - Khả năng thông khí mặt nạ khó?
            - Bệnh nhân hợp tác được không?
            - Tình huống khẩn cấp không?
            
            **2. Kế hoạch A - Chính:**
            - Video laryngoscope
            - Bougie
            - Blade khác
            
            **3. Kế hoạch B - Dự phòng:**
            - LMA/i-gel
            - Đánh thức bệnh nhân
            
            **4. Kế hoạch C - Khẩn cấp:**
            - CICO (Can't Intubate, Can't Oxygenate)
            - Cricothyrotomy khẩn cấp
            
            **Chuẩn bị:**
            - Dụng cụ đầy đủ, kiểm tra trước
            - Nhân lực: Có bác sĩ giàu kinh nghiệm
            - Thông báo phẫu thuật viên
            - Đánh thức bệnh nhân nếu thất bại
            
            **Đặt NKQ tỉnh (Awake intubation):**
            - Khi tiên đoán rất khó
            - Gây tê niêm mạc tốt
            -進鏡 nội soi mềm hoặc video laryngoscope
            """)
        
        with st.expander("📊 Độ chính xác Mallampati"):
            st.markdown("""
            ### Giá trị dự đoán:
            
            | Chỉ số | Giá trị |
            |:-------|:--------|
            | Độ nhạy | 40-60% |
            | Độ đặc hiệu | 80-90% |
            | PPV (Giá trị dự đoán dương) | Thấp (~15%) |
            | NPV (Giá trị dự đoán âm) | Cao (~95%) |
            
            **Ý nghĩa:**
            - Class I-II → Thường KHÔNG khó (NPV cao)
            - Class III-IV → CHƯA CHẮC khó (PPV thấp)
            - ➜ Cần đánh giá toàn diện, không chỉ dựa Mallampati
            
            **Lưu ý:**
            - Inter-observer variability cao (người khác nhau đánh giá khác nhau)
            - Thay đổi theo tư thế, thời gian thai kỳ...
            - Là công cụ sàng lọc, không thay thế đánh giá lâm sàng
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Mallampati Class": f"Class {mallampati_class}"
            }
            
            results_dict = {
                "Class": f"{result['class']}",
                "Đường thở": result['difficulty'],
                "Nguy cơ": result['risk'],
                "Mô tả": result['description']
            }
            
            # Save to history
            # Export section
            render_export_section(
                title="Mallampati Classification",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="Mallampati Classification"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="mallampati",
                calculator_name="Mallampati Classification",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="mallampati",
                calculator_name="Mallampati Classification",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="mallampati", show_actions=True)
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("Mallampati")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

