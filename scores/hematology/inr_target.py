"""
INR Target Calculator
=====================

Determine appropriate INR target range for different clinical conditions requiring anticoagulation.

Reference:
- ACCP Guidelines for Antithrombotic Therapy
- AHA/ACC Guidelines for Atrial Fibrillation
- ESC Guidelines for Valvular Heart Disease
- ASH Guidelines for Venous Thromboembolism

Clinical Utility:
- Guide INR target selection based on indication
- Reduce bleeding and thrombotic complications
- Optimize anticoagulation management
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================

from components.ui.scoring import render_score_result, render_score_breakdown
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.scores_export import render_export_section as render_scores_export


def get_inr_target(indication: str, additional_factors: dict = None) -> dict:
    """
    Get INR target range for specific indication
    
    Args:
        indication: Clinical indication for anticoagulation
        additional_factors: Additional clinical factors (age, bleeding risk, etc.)
    
    Returns:
        dict with target INR range, recommendations, and clinical guidance
    """
    additional_factors = additional_factors or {}
    
    # Standard INR targets by indication
    targets = {
        "atrial_fibrillation": {
            "min": 2.0,
            "max": 3.0,
            "target": 2.5,
            "description": "Rung nhĩ (Atrial Fibrillation)",
            "evidence": "AHA/ACC Guidelines 2019",
            "rationale": "Ngăn ngừa đột quỵ và huyết khối hệ thống"
        },
        "mechanical_valve_mvr": {
            "min": 2.5,
            "max": 3.5,
            "target": 3.0,
            "description": "Van hai lá cơ học (Mechanical Mitral Valve)",
            "evidence": "AHA/ACC Guidelines 2020",
            "rationale": "Nguy cơ huyết khối cao hơn van động mạch chủ"
        },
        "mechanical_valve_avr": {
            "min": 2.0,
            "max": 3.0,
            "target": 2.5,
            "description": "Van động mạch chủ cơ học (Mechanical Aortic Valve)",
            "evidence": "AHA/ACC Guidelines 2020",
            "rationale": "Nguy cơ huyết khối thấp hơn van hai lá"
        },
        "mechanical_valve_dual": {
            "min": 2.5,
            "max": 3.5,
            "target": 3.0,
            "description": "Hai van cơ học (Dual Mechanical Valves)",
            "evidence": "AHA/ACC Guidelines 2020",
            "rationale": "Nguy cơ huyết khối cao nhất"
        },
        "dvt_pe_acute": {
            "min": 2.0,
            "max": 3.0,
            "target": 2.5,
            "description": "DVT/PE cấp tính (Acute DVT/PE)",
            "evidence": "ACCP Guidelines 2016",
            "rationale": "Điều trị ban đầu và duy trì"
        },
        "dvt_pe_recurrent": {
            "min": 2.0,
            "max": 3.0,
            "target": 2.5,
            "description": "DVT/PE tái phát (Recurrent DVT/PE)",
            "evidence": "ACCP Guidelines 2016",
            "rationale": "Dự phòng tái phát"
        },
        "antiphospholipid_syndrome": {
            "min": 2.5,
            "max": 3.5,
            "target": 3.0,
            "description": "Hội chứng kháng phospholipid",
            "evidence": "ASH Guidelines 2020",
            "rationale": "Nguy cơ huyết khối cao, cần INR cao hơn"
        },
        "cardiomyopathy": {
            "min": 2.0,
            "max": 3.0,
            "target": 2.5,
            "description": "Bệnh cơ tim (Cardiomyopathy)",
            "evidence": "AHA/ACC Guidelines",
            "rationale": "Dự phòng huyết khối trong buồng tim"
        },
        "other": {
            "min": 2.0,
            "max": 3.0,
            "target": 2.5,
            "description": "Chỉ định khác",
            "evidence": "Clinical judgment",
            "rationale": "Target chuẩn cho hầu hết chỉ định"
        }
    }
    
    result = targets.get(indication, targets["other"]).copy()
    
    # Adjust for additional factors
    adjustments = []
    
    # Age adjustment
    if additional_factors.get("age") and additional_factors["age"] >= 75:
        # Elderly patients - consider lower target
        if result["min"] > 2.0:
            result["min"] = max(2.0, result["min"] - 0.5)
            adjustments.append("Điều chỉnh cho người cao tuổi (≥75): giảm target tối thiểu")
    
    # High bleeding risk
    if additional_factors.get("bleeding_risk") == "high":
        if result["min"] > 2.0:
            result["min"] = max(2.0, result["min"] - 0.5)
            result["max"] = max(2.5, result["max"] - 0.5)
            adjustments.append("Điều chỉnh cho nguy cơ chảy máu cao: giảm target range")
    
    # Recalculate target center
    result["target"] = (result["min"] + result["max"]) / 2
    
    # Determine monitoring frequency
    if indication in ["mechanical_valve_mvr", "mechanical_valve_dual", "antiphospholipid_syndrome"]:
        monitoring_frequency = "Mỗi 2-4 tuần (khi ổn định)"
        monitoring_initial = "Mỗi 1-2 tuần (giai đoạn đầu)"
    else:
        monitoring_frequency = "Mỗi 4-6 tuần (khi ổn định)"
        monitoring_initial = "Mỗi 1-2 tuần (giai đoạn đầu)"
    
    result["monitoring_initial"] = monitoring_initial
    result["monitoring_frequency"] = monitoring_frequency
    result["adjustments"] = adjustments
    
    # Clinical recommendations
    recommendations = []
    
    if indication.startswith("mechanical_valve"):
        recommendations.append("✅ INR target quan trọng để ngăn ngừa huyết khối van")
        recommendations.append("⚠️ INR < target: tăng nguy cơ huyết khối")
        recommendations.append("⚠️ INR > target: tăng nguy cơ chảy máu")
    elif indication in ["dvt_pe_acute", "dvt_pe_recurrent"]:
        recommendations.append("✅ Điều trị tối thiểu 3 tháng cho DVT/PE cấp")
        recommendations.append("✅ Xem xét điều trị dài hạn nếu nguy cơ tái phát cao")
    elif indication == "atrial_fibrillation":
        recommendations.append("✅ Cân nhắc CHA₂DS₂-VASc score để đánh giá nguy cơ đột quỵ")
        recommendations.append("✅ Cân nhắc HAS-BLED score để đánh giá nguy cơ chảy máu")
    
    result["recommendations"] = recommendations
    
    return result


def render():
    """INR Target Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🎯 INR Target Calculator</h3>
    """, unsafe_allow_html=True)
    st.caption("Xác định INR mục tiêu cho các chỉ định khác nhau")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'inr_target':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Chỉ Định Lâm Sàng")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        indication = st.selectbox(
            "Chỉ định dùng kháng đông",
            [
                "atrial_fibrillation",
                "mechanical_valve_mvr",
                "mechanical_valve_avr",
                "mechanical_valve_dual",
                "dvt_pe_acute",
                "dvt_pe_recurrent",
                "antiphospholipid_syndrome",
                "cardiomyopathy",
                "other"
            ],
            format_func=lambda x: {
                "atrial_fibrillation": "Rung nhĩ (Atrial Fibrillation)",
                "mechanical_valve_mvr": "Van hai lá cơ học (Mechanical Mitral Valve)",
                "mechanical_valve_avr": "Van động mạch chủ cơ học (Mechanical Aortic Valve)",
                "mechanical_valve_dual": "Hai van cơ học (Dual Mechanical Valves)",
                "dvt_pe_acute": "DVT/PE cấp tính (Acute DVT/PE)",
                "dvt_pe_recurrent": "DVT/PE tái phát (Recurrent DVT/PE)",
                "antiphospholipid_syndrome": "Hội chứng kháng phospholipid",
                "cardiomyopathy": "Bệnh cơ tim (Cardiomyopathy)",
                "other": "Chỉ định khác"
            }[x],
            index=0
        )
        
        st.markdown("### 👤 Yếu Tố Bổ Sung (Tùy chọn)")
        
        col_age, col_bleeding = st.columns(2)
        with col_age:
            age = st.number_input(
                "Tuổi (năm)",
                min_value=18,
                max_value=120,
                value=int(shared_inputs.get('age', 65)) if shared_inputs.get('age') else None,
                step=1,
                help="Tuổi bệnh nhân"
            )
        with col_bleeding:
            bleeding_risk = st.selectbox(
                "Nguy cơ chảy máu",
                ["low", "medium", "high"],
                format_func=lambda x: {
                    "low": "Thấp",
                    "medium": "Trung bình",
                    "high": "Cao"
                }[x],
                index=0,
                help="Đánh giá nguy cơ chảy máu"
            )
        
        # Calculate
        if st.button("🔄 Xác Định INR Mục Tiêu", type="primary", use_container_width=True):
            additional_factors = {
                "age": age if age else None,
                "bleeding_risk": bleeding_risk
            }
            
            result = get_inr_target(indication, additional_factors)
            
            st.session_state['inr_target_result'] = result
            
            # Display results
            st.markdown("---")
            st.markdown("### 📊 INR Mục Tiêu")
            
            col_res1, col_res2, col_res3 = st.columns(3)
            
            with col_res1:
                st.metric(
                    "INR Tối Thiểu",
                    f"{result['min']:.1f}",
                    help="Giá trị INR thấp nhất được chấp nhận"
                )
            
            with col_res2:
                st.metric(
                    "INR Mục Tiêu",
                    f"{result['target']:.1f}",
                    delta=f"Range: {result['min']:.1f}-{result['max']:.1f}",
                    help="INR mục tiêu trung tâm"
                )
            
            with col_res3:
                st.metric(
                    "INR Tối Đa",
                    f"{result['max']:.1f}",
                    help="Giá trị INR cao nhất được chấp nhận"
                )
            
            # Description
            st.info(f"**{result['description']}** - {result['rationale']}")
            
            # Evidence
            st.caption(f"📚 Dựa trên: {result['evidence']}")
            
            # Adjustments
            if result.get('adjustments'):
                st.warning("⚠️ **Điều chỉnh:** " + " | ".join(result['adjustments']))
            
            # Detailed breakdown
            with st.expander("📋 Chi tiết", expanded=True):
                st.markdown(f"""
                **Chỉ định:** {result['description']}
                
                **INR Target Range:** {result['min']:.1f} - {result['max']:.1f}
                
                **INR Target Trung Tâm:** {result['target']:.1f}
                
                **Lý do:** {result['rationale']}
                
                **Cơ sở bằng chứng:** {result['evidence']}
                """)
            
            # Monitoring
            st.markdown("### 📅 Theo Dõi INR")
            
            col_mon1, col_mon2 = st.columns(2)
            with col_mon1:
                st.info(f"**Giai đoạn đầu:** {result['monitoring_initial']}")
            with col_mon2:
                st.success(f"**Khi ổn định:** {result['monitoring_frequency']}")
            
            # Recommendations
            if result.get('recommendations'):
                st.markdown("### 💡 Khuyến nghị Lâm Sàng")
                for rec in result['recommendations']:
                    st.markdown(rec)
            
            # Clinical guidance
            st.markdown("### 🎯 Hướng Dẫn Lâm Sàng")
            
            if indication.startswith("mechanical_valve"):
                st.warning("""
                **Van cơ học:**
                - INR < target: Tăng nguy cơ huyết khối van, cần tăng liều warfarin
                - INR > target: Tăng nguy cơ chảy máu, cần giảm liều warfarin
                - Theo dõi INR thường xuyên, đặc biệt khi thay đổi thuốc hoặc bệnh
                """)
            elif indication in ["dvt_pe_acute", "dvt_pe_recurrent"]:
                st.info("""
                **DVT/PE:**
                - Điều trị tối thiểu 3 tháng cho DVT/PE cấp
                - Xem xét điều trị dài hạn nếu nguy cơ tái phát cao
                - Cân nhắc chuyển sang DOACs nếu phù hợp
                """)
            elif indication == "atrial_fibrillation":
                st.info("""
                **Rung nhĩ:**
                - Cân nhắc CHA₂DS₂-VASc score để đánh giá nguy cơ đột quỵ
                - Cân nhắc HAS-BLED score để đánh giá nguy cơ chảy máu
                - Cân nhắc chuyển sang DOACs nếu phù hợp
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="inr_target",
                calculator_name="INR Target Calculator",
                inputs={
                    "Chỉ định": result['description'],
                    "Tuổi": f"{age} tuổi" if age else "N/A",
                    "Nguy cơ chảy máu": bleeding_risk
                },
                result={
                    "INR Target": f"{result['min']:.1f}-{result['max']:.1f}",
                    "INR Trung Tâm": f"{result['target']:.1f}",
                    "Theo dõi": result['monitoring_frequency']
                }
            )
            
            render_share_section(
                calculator_id="inr_target",
                calculator_name="INR Target Calculator"
            )
            render_scores_export(
                calculator_id="inr_target",
                calculator_name="INR Target Calculator",
                data={"result": result}
            )
            render_suggestions(calculator_id="inr_target", result=result)
    
    with col2:
        st.markdown("### 📚 Thông tin")
        
        st.markdown("""
        **INR Target Ranges:**
        
        - **Rung nhĩ:** 2.0-3.0
        - **Van cơ học (hai lá):** 2.5-3.5
        - **Van cơ học (động mạch chủ):** 2.0-3.0
        - **DVT/PE:** 2.0-3.0
        - **Hội chứng kháng phospholipid:** 2.5-3.5
        
        **Lưu ý:**
        - Target có thể điều chỉnh theo yếu tố lâm sàng
        - Người cao tuổi: cân nhắc target thấp hơn
        - Nguy cơ chảy máu cao: cân nhắc target thấp hơn
        """)
        
        if st.session_state.get('inr_target_result'):
            result = st.session_state['inr_target_result']
            risk_level = "low" if result['target'] <= 2.5 else "medium"
            render_risk_badge(
                risk_level,
                f"Target: {result['target']:.1f}",
                size="large"
            )
    
    render_history_ui(calculator_id="inr_target", show_actions=True)
    references = get_references("INR Target")
    if references:
        render_references_section(references)

