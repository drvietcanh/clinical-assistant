"""
Goldman Cardiac Risk Index Calculator
Đánh giá nguy cơ tim mạch trong phẫu thuật (Historical - vẫn được dùng)
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


def calculate_goldman_cardiac(
    age_70, mi_6mo, s3_jvd, aortic_stenosis, rhythm_other_sinus, 
    premature_beats, po2_60_or_pco2_50, k_3_or_hco3_20, bun_50_or_cr_3,
    abnormal_sgot, bedridden, intraperitoneal_intrathoracic_aortic
):
    """
    Tính điểm Goldman Cardiac Risk Index
    
    Parameters (mỗi yếu tố có điểm riêng):
    - age_70: Tuổi ≥70 (5 điểm)
    - mi_6mo: Nhồi máu cơ tim <6 tháng (10 điểm)
    - s3_jvd: S3 gallop hoặc JVD (11 điểm)
    - aortic_stenosis: Hẹp van động mạch chủ nặng (3 điểm)
    - rhythm_other_sinus: Nhịp không phải xoang (7 điểm)
    - premature_beats: Ngoại tâm thu >5/phút (7 điểm)
    - po2_60_or_pco2_50: PO₂<60 hoặc PCO₂>50 (3 điểm)
    - k_3_or_hco3_20: K<3 hoặc HCO₃<20 (3 điểm)
    - bun_50_or_cr_3: BUN>50 hoặc Cr>3 (3 điểm)
    - abnormal_sgot: SGOT bất thường (3 điểm)
    - bedridden: Nằm liệt giường (3 điểm)
    - intraperitoneal_intrathoracic_aortic: Phẫu thuật trong ổ bụng, ngực, động mạch chủ (3 điểm)
    
    Returns:
    - dict với total_score, risk_class, và interpretation
    """
    total = (age_70 * 5 + mi_6mo * 10 + s3_jvd * 11 + aortic_stenosis * 3 +
             rhythm_other_sinus * 7 + premature_beats * 7 + po2_60_or_pco2_50 * 3 +
             k_3_or_hco3_20 * 3 + bun_50_or_cr_3 * 3 + abnormal_sgot * 3 +
             bedridden * 3 + intraperitoneal_intrathoracic_aortic * 3)
    
    # Risk classification based on Goldman et al. 1977
    if total <= 5:
        risk_class = "Class I"
        risk_pct = 0.2
        risk_level = "Nguy cơ rất thấp"
        recommendation = "Phẫu thuật an toàn"
        color = COLORS["success"]
    elif total <= 12:
        risk_class = "Class II"
        risk_pct = 2.0
        risk_level = "Nguy cơ thấp"
        recommendation = "Phẫu thuật an toàn, theo dõi thường quy"
        color = COLORS["success"]
    elif total <= 25:
        risk_class = "Class III"
        risk_pct = 11.0
        risk_level = "Nguy cơ trung bình"
        recommendation = "Cân nhắc đánh giá tim mạch, theo dõi sát"
        color = COLORS["warning"]
    else:  # >25
        risk_class = "Class IV"
        risk_pct = 22.0
        risk_level = "Nguy cơ cao"
        recommendation = "Đánh giá tim mạch đầy đủ, cân nhắc hoãn phẫu thuật"
        color = COLORS["error"]
    
    return {
        "total_score": total,
        "risk_class": risk_class,
        "risk_percentage": risk_pct,
        "risk_level": risk_level,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render Goldman Cardiac Risk Index interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'goldman_cardiac':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['error']};'>❤️ Goldman Cardiac Risk Index</h2>
    <p style='text-align: center;'><em>Đánh giá nguy cơ tim mạch trong phẫu thuật (Historical)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Goldman Cardiac Risk Index"):
        st.markdown("""
        **Goldman Cardiac Risk Index** là thang điểm cổ điển để đánh giá nguy cơ biến chứng tim mạch
        trong phẫu thuật không tim, được phát triển năm 1977.
        
        **12 yếu tố nguy cơ (tổng điểm 53):**
        
        **Yếu tố nguy cơ cao:**
        - S3 gallop hoặc JVD: **11 điểm**
        - Nhồi máu cơ tim <6 tháng: **10 điểm**
        - Nhịp không phải xoang: **7 điểm**
        - Ngoại tâm thu >5/phút: **7 điểm**
        - Tuổi ≥70: **5 điểm**
        
        **Yếu tố nguy cơ trung bình (mỗi yếu tố 3 điểm):**
        - Hẹp van động mạch chủ nặng
        - PO₂<60 hoặc PCO₂>50
        - K<3 hoặc HCO₃<20
        - BUN>50 hoặc Cr>3
        - SGOT bất thường
        - Nằm liệt giường
        - Phẫu thuật trong ổ bụng, ngực, động mạch chủ
        
        **Phân loại nguy cơ:**
        - **Class I (0-5 điểm):** 0.2% nguy cơ
        - **Class II (6-12 điểm):** 2% nguy cơ
        - **Class III (13-25 điểm):** 11% nguy cơ
        - **Class IV (>25 điểm):** 22% nguy cơ
        
        **Lưu ý:**
        - Thang điểm cũ nhưng vẫn được dùng
        - RCRI và Gupta Index chính xác hơn
        - Hữu ích khi cần đánh giá nhanh
        
        **Reference:** Goldman L, et al. Multifactorial index of cardiac risk in noncardiac 
        surgical procedures. N Engl J Med. 1977;297(16):845-50.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 12 yếu tố nguy cơ")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="goldman_cardiac",
            calculator_name="Goldman Cardiac Risk Index",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.info("**Lưu ý:** Đây là thang điểm cũ. Nên dùng RCRI hoặc Gupta Index cho đánh giá chính xác hơn.")
    
    # High risk factors
    st.markdown("### Yếu tố nguy cơ cao")
    
    s3_jvd = st.checkbox("S3 gallop hoặc JVD (11 điểm)", key="goldman_s3")
    mi_6mo = st.checkbox("Nhồi máu cơ tim <6 tháng (10 điểm)", key="goldman_mi")
    rhythm_other_sinus = st.checkbox("Nhịp không phải xoang (7 điểm)", key="goldman_rhythm")
    premature_beats = st.checkbox("Ngoại tâm thu >5/phút (7 điểm)", key="goldman_pvc")
    age_70 = st.checkbox("Tuổi ≥70 (5 điểm)", key="goldman_age")
    
    st.markdown("---")
    
    # Medium risk factors (3 points each)
    st.markdown("### Yếu tố nguy cơ trung bình (mỗi yếu tố 3 điểm)")
    
    aortic_stenosis = st.checkbox("Hẹp van động mạch chủ nặng", key="goldman_aortic")
    po2_60_or_pco2_50 = st.checkbox("PO₂<60 hoặc PCO₂>50", key="goldman_abg")
    k_3_or_hco3_20 = st.checkbox("K<3 hoặc HCO₃<20", key="goldman_electrolyte")
    bun_50_or_cr_3 = st.checkbox("BUN>50 hoặc Cr>3", key="goldman_renal")
    abnormal_sgot = st.checkbox("SGOT bất thường", key="goldman_liver")
    bedridden = st.checkbox("Nằm liệt giường", key="goldman_bedridden")
    intraperitoneal_intrathoracic_aortic = st.checkbox("Phẫu thuật trong ổ bụng, ngực, động mạch chủ", key="goldman_surgery")
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm Goldman Cardiac Risk", type="primary", use_container_width=True):
        try:
            result = calculate_goldman_cardiac(
                age_70, mi_6mo, s3_jvd, aortic_stenosis, rhythm_other_sinus,
                premature_beats, po2_60_or_pco2_50, k_3_or_hco3_20, bun_50_or_cr_3,
                abnormal_sgot, bedridden, intraperitoneal_intrathoracic_aortic
            )
            
            # Display results
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Tổng điểm", f"{result['total_score']}/53")
            
            with col2:
                st.metric("Risk Class", result['risk_class'])
            
            with col3:
                st.metric("Nguy cơ", result['risk_level'])
            
            with col4:
                st.metric("Biến chứng", f"{result['risk_percentage']:.1f}%")
            
            st.markdown("---")
            
            # Risk interpretation
            if result['color'] == COLORS["success"]:
                st.success(f"**{result['risk_class']} - {result['risk_level']}** - Tỷ lệ biến chứng: {result['risk_percentage']:.1f}%")
            elif result['color'] == COLORS["warning"]:
                st.warning(f"**{result['risk_class']} - {result['risk_level']}** - Tỷ lệ biến chứng: {result['risk_percentage']:.1f}%")
            else:
                st.error(f"**{result['risk_class']} - {result['risk_level']}** - Tỷ lệ biến chứng: {result['risk_percentage']:.1f}%")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Tuổi ≥70": "Có" if age_70 else "Không",
                "MI <6 tháng": "Có" if mi_6mo else "Không",
                "S3/JVD": "Có" if s3_jvd else "Không",
                "Hẹp van ĐMC": "Có" if aortic_stenosis else "Không",
                "Nhịp không xoang": "Có" if rhythm_other_sinus else "Không",
                "Ngoại tâm thu >5/phút": "Có" if premature_beats else "Không",
                "PO₂<60 hoặc PCO₂>50": "Có" if po2_60_or_pco2_50 else "Không",
                "K<3 hoặc HCO₃<20": "Có" if k_3_or_hco3_20 else "Không",
                "BUN>50 hoặc Cr>3": "Có" if bun_50_or_cr_3 else "Không",
                "SGOT bất thường": "Có" if abnormal_sgot else "Không",
                "Nằm liệt giường": "Có" if bedridden else "Không",
                "Phẫu thuật nguy cơ cao": "Có" if intraperitoneal_intrathoracic_aortic else "Không"
            }
            
            results_dict = {
                "Tổng điểm": f"{result['total_score']}/53",
                "Risk Class": result['risk_class'],
                "Nguy cơ": result['risk_level'],
                "Tỷ lệ biến chứng": f"{result['risk_percentage']:.1f}%",
                "Khuyến nghị": result['recommendation']
            }
            
            # Save to history
            # Export section
            render_export_section(
                title="Goldman Cardiac Risk Index",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="Goldman Cardiac Risk Index"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="goldman_cardiac",
                calculator_name="Goldman Cardiac Risk Index",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="goldman_cardiac",
                calculator_name="Goldman Cardiac Risk Index",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="goldman_cardiac", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("Goldman Cardiac")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

