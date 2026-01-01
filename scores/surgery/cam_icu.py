"""
CAM-ICU - Confusion Assessment Method for ICU Calculator
Chẩn đoán mê sảng trong ICU (DÙNG HÀNG NGÀY)
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


def calculate_cam_icu(acute_onset, inattention, disorganized_thinking, altered_consciousness):
    """
    Tính CAM-ICU
    
    Parameters:
    - acute_onset: Khởi phát cấp tính (0=no, 1=yes)
    - inattention: Rối loạn chú ý (0=no, 1=yes)
    - disorganized_thinking: Rối loạn tư duy (0=no, 1=yes)
    - altered_consciousness: Thay đổi ý thức (0=no, 1=yes)
    
    Returns:
    - dict với result và interpretation
    """
    # CAM-ICU criteria:
    # Feature 1: Acute onset AND fluctuating course
    # Feature 2: Inattention
    # Feature 3: Disorganized thinking
    # Feature 4: Altered level of consciousness
    
    # Positive if: Feature 1 AND Feature 2 AND (Feature 3 OR Feature 4)
    feature_1 = acute_onset  # Acute onset/fluctuating
    feature_2 = inattention
    feature_3 = disorganized_thinking
    feature_4 = altered_consciousness
    
    is_positive = feature_1 and feature_2 and (feature_3 or feature_4)
    
    if is_positive:
        result = "Dương tính - Có mê sảng"
        recommendation = "Cần điều trị mê sảng: tìm nguyên nhân, điều chỉnh yếu tố nguy cơ, cân nhắc thuốc (haloperidol, quetiapine)"
        color = "red"
    else:
        result = "Âm tính - Không có mê sảng"
        recommendation = "Tiếp tục theo dõi, đánh giá lại hàng ngày"
        color = "green"
    
    return {
        "is_positive": is_positive,
        "result": result,
        "recommendation": recommendation,
        "color": color,
        "feature_1": feature_1,
        "feature_2": feature_2,
        "feature_3": feature_3,
        "feature_4": feature_4
    }


def render():
    """Render CAM-ICU interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'cam_icu':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🧠 CAM-ICU - Confusion Assessment Method for ICU</h2>
    <p style='text-align: center;'><em>Chẩn đoán mê sảng trong ICU (DÙNG HÀNG NGÀY)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về CAM-ICU"):
        st.markdown("""
        **CAM-ICU (Confusion Assessment Method for ICU)** là công cụ tiêu chuẩn vàng để chẩn đoán 
        mê sảng trong ICU, được khuyến nghị sử dụng hàng ngày.
        
        **4 đặc điểm chính:**
        
        1. **Khởi phát cấp tính và dao động (Acute onset and fluctuating course)**
           - Thay đổi tình trạng tâm thần cấp tính (trong vài giờ đến vài ngày)
           - Dao động trong ngày
        
        2. **Rối loạn chú ý (Inattention)**
           - Không thể tập trung
           - Dễ bị phân tâm
           - Test: Đếm ngược từ 20 đến 1, hoặc đọc chữ cái (S-A-V-E-A-H-A-A-R-T)
        
        3. **Rối loạn tư duy (Disorganized thinking)**
           - Lời nói không mạch lạc
           - Trả lời không phù hợp
           - Test: Câu hỏi đơn giản (Có con voi trong tên bạn không? Có cá trong biển không?)
        
        4. **Thay đổi ý thức (Altered level of consciousness)**
           - Không tỉnh táo hoàn toàn
           - RASS ≠ 0 (không tỉnh táo)
        
        **Tiêu chuẩn chẩn đoán:**
        - **Dương tính:** Feature 1 AND Feature 2 AND (Feature 3 OR Feature 4)
        - **Âm tính:** Không đủ tiêu chuẩn
        
        **Mê sảng là gì?**
        - Rối loạn ý thức cấp tính
        - Thường gặp trong ICU (20-80% bệnh nhân)
        - Tăng nguy cơ tử vong, thời gian nằm viện, suy giảm nhận thức lâu dài
        - Có thể phòng ngừa và điều trị
        
        **Reference:** Ely EW, et al. Delirium in mechanically ventilated patients: validity and 
        reliability of the confusion assessment method for the intensive care unit (CAM-ICU). 
        JAMA. 2001;286(21):2703-10.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 4 đặc điểm")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="cam_icu",
            calculator_name="CAM-ICU - Confusion Assessment Method for ICU",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.info("""
    **Lưu ý:** Đánh giá CAM-ICU cần bệnh nhân có thể giao tiếp (RASS ≥-3).
    Nếu bệnh nhân quá sâu (RASS -4, -5), không thể đánh giá CAM-ICU.
    """)
    
    # Feature 1: Acute onset
    st.markdown("### 1️⃣ Khởi phát cấp tính và dao động")
    st.markdown("""
    **Đánh giá:**
    - Thay đổi tình trạng tâm thần cấp tính (trong vài giờ đến vài ngày)?
    - Có dao động trong ngày (tốt hơn/tệ hơn)?
    """)
    acute_onset = st.radio(
        "Khởi phát cấp tính và dao động:",
        options=[0, 1],
        format_func=lambda x: {
            0: "Không - Tình trạng ổn định hoặc thay đổi từ từ",
            1: "Có - Thay đổi cấp tính và dao động"
        }[x],
        key="cam_icu_acute",
        horizontal=False
    )
    
    # Feature 2: Inattention
    st.markdown("### 2️⃣ Rối loạn chú ý")
    st.markdown("""
    **Test chú ý:**
    - Yêu cầu bệnh nhân đếm ngược từ 20 đến 1
    - Hoặc đọc chữ cái: S-A-V-E-A-H-A-A-R-T (bỏ qua chữ A)
    - Nếu sai ≥2 lần → Rối loạn chú ý
    """)
    inattention = st.radio(
        "Rối loạn chú ý:",
        options=[0, 1],
        format_func=lambda x: {
            0: "Không - Bệnh nhân tập trung tốt",
            1: "Có - Bệnh nhân không thể tập trung, dễ bị phân tâm"
        }[x],
        key="cam_icu_inattention",
        horizontal=False
    )
    
    # Feature 3: Disorganized thinking
    st.markdown("### 3️⃣ Rối loạn tư duy")
    st.markdown("""
    **Test tư duy (hỏi 4 câu hỏi):**
    1. "Có con voi trong tên bạn không?" (Đúng: Không)
    2. "Có cá trong biển không?" (Đúng: Có)
    3. "Một pound nặng hơn hai pound không?" (Đúng: Không)
    4. "Bạn có thể dùng búa để đóng đinh không?" (Đúng: Có)
    
    Nếu sai ≥2 câu → Rối loạn tư duy
    """)
    disorganized_thinking = st.radio(
        "Rối loạn tư duy:",
        options=[0, 1],
        format_func=lambda x: {
            0: "Không - Tư duy mạch lạc",
            1: "Có - Lời nói không mạch lạc, trả lời không phù hợp"
        }[x],
        key="cam_icu_thinking",
        horizontal=False
    )
    
    # Feature 4: Altered consciousness
    st.markdown("### 4️⃣ Thay đổi ý thức")
    st.markdown("""
    **Đánh giá:**
    - Bệnh nhân có tỉnh táo hoàn toàn không? (RASS = 0)
    - Nếu RASS ≠ 0 → Thay đổi ý thức
    """)
    altered_consciousness = st.radio(
        "Thay đổi ý thức:",
        options=[0, 1],
        format_func=lambda x: {
            0: "Không - Tỉnh táo hoàn toàn (RASS = 0)",
            1: "Có - Không tỉnh táo hoàn toàn (RASS ≠ 0)"
        }[x],
        key="cam_icu_consciousness",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm CAM-ICU", type="primary", use_container_width=True):
        try:
            result = calculate_cam_icu(acute_onset, inattention, disorganized_thinking, altered_consciousness)
            
            # Display results
            st.markdown("### 📊 Kết quả CAM-ICU")
            
            if result['is_positive']:
                st.error(f"**{result['result']}**")
            else:
                st.success(f"**{result['result']}**")
            
            st.markdown("---")
            
            # Show criteria
            st.subheader("📋 Đánh giá từng tiêu chuẩn")
            criteria = [
                ("1. Khởi phát cấp tính và dao động", result['feature_1']),
                ("2. Rối loạn chú ý", result['feature_2']),
                ("3. Rối loạn tư duy", result['feature_3']),
                ("4. Thay đổi ý thức", result['feature_4'])
            ]
            
            for name, present in criteria:
                status = "✅ Có" if present else "❌ Không"
                st.markdown(f"- **{name}:** {status}")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            st.markdown("---")
            
            # Additional information
            if result['is_positive']:
                with st.expander("🛠️ Điều trị mê sảng"):
                    st.markdown("""
                **Nguyên tắc điều trị:**
                
                1. **Tìm và điều chỉnh nguyên nhân:**
                   - Nhiễm trùng
                   - Rối loạn điện giải
                   - Thuốc (an thần, kháng cholinergic)
                   - Thiếu oxy, tăng CO₂
                   - Đau, khó chịu
                   - Rối loạn giấc ngủ
                
                2. **Điều chỉnh yếu tố nguy cơ:**
                   - Giảm liều an thần (nếu có thể)
                   - Đảm bảo giấc ngủ (chu kỳ ngày/đêm)
                   - Vận động sớm
                   - Kích thích nhận thức
                   - Gia đình thăm viếng
                
                3. **Thuốc điều trị (nếu cần):**
                   - **Haloperidol:** 0.5-2mg IV/IM, có thể lặp lại
                   - **Quetiapine:** 25-100mg PO (nếu có thể uống)
                   - **Olanzapine:** 2.5-10mg PO/IM
                   - Tránh benzodiazepine (trừ khi cai rượu)
                
                4. **Theo dõi:**
                   - Đánh giá CAM-ICU hàng ngày
                   - Theo dõi tác dụng phụ thuốc
                   - Đánh giá lại khi có thay đổi
                    """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Khởi phát cấp tính": "Có" if acute_onset == 1 else "Không",
                "Rối loạn chú ý": "Có" if inattention == 1 else "Không",
                "Rối loạn tư duy": "Có" if disorganized_thinking == 1 else "Không",
                "Thay đổi ý thức": "Có" if altered_consciousness == 1 else "Không"
            }
            
            results_dict = {
                "Kết quả": result['result'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Export section
            render_export_section(
                title="CAM-ICU - Confusion Assessment Method for ICU",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="CAM-ICU - Confusion Assessment Method for ICU"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="cam_icu",
                calculator_name="CAM-ICU - Confusion Assessment Method for ICU",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="cam_icu",
                calculator_name="CAM-ICU - Confusion Assessment Method for ICU",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="cam_icu", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("CAM-ICU")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

