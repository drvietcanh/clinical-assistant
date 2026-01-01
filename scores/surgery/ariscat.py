"""
ARISCAT - Assess Respiratory Risk in Surgical Patients Calculator
Nguy cơ biến chứng hô hấp sau phẫu thuật
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.anesthesia_validation import validate_ariscat_components
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_ariscat(age, spo2, respiratory_infection, anemia, surgical_incision, duration_surgery, emergency):
    """
    Tính điểm ARISCAT
    
    Parameters:
    - age: Tuổi (0=<50, 1=50-80, 2=>80)
    - spo2: SpO₂ (0=>95%, 1=91-95%, 2=<91%)
    - respiratory_infection: Nhiễm trùng hô hấp gần đây (0=no, 1=yes)
    - anemia: Thiếu máu (0=no, 1=yes)
    - surgical_incision: Vị trí đường mổ (0=peripheral, 1=upper abdominal/thoracic)
    - duration_surgery: Thời gian phẫu thuật (0=<2h, 1=2-3h, 2=>3h)
    - emergency: Phẫu thuật cấp cứu (0=no, 1=yes)
    
    Returns:
    - dict với total_score, risk_percentage, và recommendations
    """
    total = (age + spo2 + respiratory_infection + anemia + 
             surgical_incision + duration_surgery + emergency)
    
    # Risk percentages based on ARISCAT study
    if total <= 25:
        risk_pct = 1.6
        risk_level = "Nguy cơ thấp"
        recommendation = "Phẫu thuật an toàn, không cần biện pháp đặc biệt"
        color = "green"
    elif total <= 44:
        risk_pct = 5.2
        risk_level = "Nguy cơ trung bình"
        recommendation = "Cân nhắc biện pháp dự phòng: tập thở, vật lý trị liệu hô hấp"
        color = "orange"
    else:  # ≥45
        risk_pct = 11.6
        risk_level = "Nguy cơ cao"
        recommendation = "Cần biện pháp dự phòng tích cực: tập thở, vật lý trị liệu, cân nhắc gây tê vùng thay vì gây mê toàn thân"
        color = "red"
    
    return {
        "total_score": total,
        "risk_percentage": risk_pct,
        "risk_level": risk_level,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render ARISCAT interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'ariscat':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🫁 ARISCAT - Assess Respiratory Risk in Surgical Patients</h2>
    <p style='text-align: center;'><em>Nguy cơ biến chứng hô hấp sau phẫu thuật</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về ARISCAT"):
        st.markdown("""
        **ARISCAT (Assess Respiratory Risk in Surgical Patients in Catalonia)** là thang điểm 
        đánh giá nguy cơ biến chứng hô hấp sau phẫu thuật, giúp bác sĩ gây mê và phẫu thuật 
        chuẩn bị biện pháp dự phòng.
        
        **7 yếu tố nguy cơ:**
        
        1. **Tuổi**
           - 0 điểm: <50 tuổi
           - 1 điểm: 50-80 tuổi
           - 2 điểm: >80 tuổi
        
        2. **SpO₂**
           - 0 điểm: >95%
           - 1 điểm: 91-95%
           - 2 điểm: <91%
        
        3. **Nhiễm trùng hô hấp gần đây** (trong 1 tháng)
           - 0 điểm: Không
           - 1 điểm: Có
        
        4. **Thiếu máu** (Hb <10 g/dL)
           - 0 điểm: Không
           - 1 điểm: Có
        
        5. **Vị trí đường mổ**
           - 0 điểm: Ngoại vi (chi, bụng dưới)
           - 1 điểm: Bụng trên/ngực
        
        6. **Thời gian phẫu thuật**
           - 0 điểm: <2 giờ
           - 1 điểm: 2-3 giờ
           - 2 điểm: >3 giờ
        
        7. **Phẫu thuật cấp cứu**
           - 0 điểm: Không
           - 1 điểm: Có
        
        **Nguy cơ theo điểm số:**
        - **≤25 điểm:** Nguy cơ thấp (1.6% biến chứng hô hấp)
        - **26-44 điểm:** Nguy cơ trung bình (5.2% biến chứng hô hấp)
        - **≥45 điểm:** Nguy cơ cao (11.6% biến chứng hô hấp)
        
        **Biến chứng hô hấp sau phẫu thuật:**
        - Viêm phổi
        - Suy hô hấp
        - Xẹp phổi
        - Tràn khí màng phổi
        - Cần thở máy kéo dài
        
        **Reference:** Canet J, et al. Prediction of postoperative pulmonary complications in a 
        population-based surgical cohort. Anesthesiology. 2010;113(6):1338-50.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 7 yếu tố nguy cơ")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="ariscat",
            calculator_name="ARISCAT - Assess Respiratory Risk in Surgical Patients",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Age
    st.markdown("### 1️⃣ Tuổi")
    age = st.radio(
        "Tuổi bệnh nhân:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - <50 tuổi",
            1: "1 điểm - 50-80 tuổi",
            2: "2 điểm - >80 tuổi"
        }[x],
        key="ariscat_age",
        horizontal=False
    )
    
    # SpO2
    st.markdown("### 2️⃣ SpO₂ (trước phẫu thuật)")
    spo2 = st.radio(
        "SpO₂ trong không khí phòng:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - >95%",
            1: "1 điểm - 91-95%",
            2: "2 điểm - <91%"
        }[x],
        key="ariscat_spo2",
        horizontal=False
    )
    
    # Respiratory infection
    st.markdown("### 3️⃣ Nhiễm trùng hô hấp gần đây")
    respiratory_infection = st.radio(
        "Có nhiễm trùng hô hấp trong 1 tháng gần đây:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Không",
            1: "1 điểm - Có (viêm phổi, viêm phế quản)"
        }[x],
        key="ariscat_infection",
        horizontal=False
    )
    
    # Anemia
    st.markdown("### 4️⃣ Thiếu máu")
    anemia = st.radio(
        "Hemoglobin:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Hb ≥10 g/dL",
            1: "1 điểm - Hb <10 g/dL"
        }[x],
        key="ariscat_anemia",
        horizontal=False
    )
    
    # Surgical incision
    st.markdown("### 5️⃣ Vị trí đường mổ")
    surgical_incision = st.radio(
        "Vị trí phẫu thuật:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Ngoại vi (chi, bụng dưới)",
            1: "1 điểm - Bụng trên/ngực (thoracic, upper abdominal)"
        }[x],
        key="ariscat_incision",
        horizontal=False
    )
    
    # Duration
    st.markdown("### 6️⃣ Thời gian phẫu thuật")
    duration_surgery = st.radio(
        "Thời gian dự kiến:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - <2 giờ",
            1: "1 điểm - 2-3 giờ",
            2: "2 điểm - >3 giờ"
        }[x],
        key="ariscat_duration",
        horizontal=False
    )
    
    # Emergency
    st.markdown("### 7️⃣ Phẫu thuật cấp cứu")
    emergency = st.radio(
        "Loại phẫu thuật:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Phẫu thuật có kế hoạch",
            1: "1 điểm - Phẫu thuật cấp cứu"
        }[x],
        key="ariscat_emergency",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm ARISCAT", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_ariscat_components(age, spo2, respiratory_infection, anemia, surgical_incision, duration_surgery, emergency)
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = calculate_ariscat(age, spo2, respiratory_infection, anemia, surgical_incision, duration_surgery, emergency)
            
            # Display results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Tổng điểm", f"{result['total_score']}")
            
            with col2:
                st.metric("Nguy cơ", result['risk_level'])
            
            with col3:
                st.metric("Tỷ lệ biến chứng", f"{result['risk_percentage']:.1f}%")
            
            st.markdown("---")
            
            # Risk interpretation
            if result['color'] == "green":
                st.success(f"**{result['risk_level']}** - Tỷ lệ biến chứng hô hấp: {result['risk_percentage']:.1f}%")
            elif result['color'] == "orange":
                st.warning(f"**{result['risk_level']}** - Tỷ lệ biến chứng hô hấp: {result['risk_percentage']:.1f}%")
            else:
                st.error(f"**{result['risk_level']}** - Tỷ lệ biến chứng hô hấp: {result['risk_percentage']:.1f}%")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            st.markdown("---")
            
            # Prevention strategies
            with st.expander("🛡️ Biện pháp dự phòng biến chứng hô hấp"):
                st.markdown("""
                **Biện pháp dự phòng:**
            
            1. **Trước phẫu thuật:**
               - Điều trị nhiễm trùng hô hấp (nếu có)
               - Điều chỉnh thiếu máu (truyền máu nếu cần)
               - Tập thở sâu, ho có hiệu quả
               - Bỏ thuốc lá (ít nhất 4-6 tuần trước phẫu thuật)
               - Giảm cân (nếu béo phì)
            
            2. **Trong phẫu thuật:**
               - Cân nhắc gây tê vùng thay vì gây mê toàn thân (nếu có thể)
               - Sử dụng PEEP (Positive End-Expiratory Pressure)
               - Tránh thông khí quá mức
               - Đảm bảo đủ oxy hóa
            
            3. **Sau phẫu thuật:**
               - Tập thở sâu, ho có hiệu quả
               - Vật lý trị liệu hô hấp
               - Động viên vận động sớm
               - Sử dụng incentive spirometry
               - Tránh nằm lâu một tư thế
               - Kiểm soát đau tốt (để bệnh nhân có thể ho, thở sâu)
            
            **Theo dõi:**
            - Đánh giá thường xuyên dấu hiệu sinh tồn
            - Chụp X-quang ngực nếu có triệu chứng
            - Theo dõi SpO₂ liên tục
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Tuổi": {0: "<50", 1: "50-80", 2: ">80"}[age],
                "SpO₂": {0: ">95%", 1: "91-95%", 2: "<91%"}[spo2],
                "Nhiễm trùng hô hấp": "Có" if respiratory_infection == 1 else "Không",
                "Thiếu máu": "Có" if anemia == 1 else "Không",
                "Vị trí đường mổ": "Bụng trên/ngực" if surgical_incision == 1 else "Ngoại vi",
                "Thời gian phẫu thuật": {0: "<2h", 1: "2-3h", 2: ">3h"}[duration_surgery],
                "Phẫu thuật cấp cứu": "Có" if emergency == 1 else "Không"
            }
            
            results_dict = {
                "Tổng điểm": result['total_score'],
                "Nguy cơ": result['risk_level'],
                "Tỷ lệ biến chứng": f"{result['risk_percentage']:.1f}%",
                "Khuyến nghị": result['recommendation']
            }
            
            # Export section
            render_export_section(
                title="ARISCAT - Assess Respiratory Risk in Surgical Patients",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="ARISCAT - Assess Respiratory Risk in Surgical Patients"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="ariscat",
                calculator_name="ARISCAT - Assess Respiratory Risk in Surgical Patients",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="ariscat",
                calculator_name="ARISCAT - Assess Respiratory Risk in Surgical Patients",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="ariscat", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("ARISCAT")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

