"""
Differential Diagnosis Generator
Main logic for generating ranked differential diagnoses
"""

import streamlit as st
from typing import List, Dict, Any, Optional
from .ddx_data import get_scenario_data, get_symptom_matches
from .vietnamese_translations import translate_symptom, translate_risk_factor


def calculate_diagnosis_score(
    diagnosis_name: str,
    diagnosis_data: Dict[str, Any],
    user_symptoms: List[str],
    age: Optional[int] = None,
    sex: Optional[str] = None,
    risk_factors: List[str] = None
) -> Dict[str, Any]:
    """
    Calculate score for a diagnosis based on symptoms, demographics, and risk factors
    
    Args:
        diagnosis_name: Name of diagnosis
        diagnosis_data: Diagnosis data from knowledge base
        user_symptoms: List of user-reported symptoms
        age: Patient age
        sex: Patient sex
        risk_factors: List of risk factors
    
    Returns:
        dict with score and details
    """
    if risk_factors is None:
        risk_factors = []
    
    # Get symptom matches
    symptom_matches = get_symptom_matches(user_symptoms, diagnosis_data["symptoms"])
    
    # Base score from specificity
    base_score = diagnosis_data.get("specificity", 0.5) * 40
    
    # Symptom matching score
    symptom_score = 0
    required_symptoms = diagnosis_data["symptoms"].get("required", [])
    supporting_symptoms = diagnosis_data["symptoms"].get("supporting", [])
    
    # Required symptoms (critical - missing = big penalty)
    if required_symptoms:
        required_match_ratio = symptom_matches["required"] / len(required_symptoms)
        symptom_score += required_match_ratio * 30
    else:
        # If no required, give points for any matching
        if symptom_matches["supporting"] > 0:
            symptom_score += 20
    
    # Supporting symptoms
    if supporting_symptoms:
        supporting_match_ratio = min(symptom_matches["supporting"] / len(supporting_symptoms), 1.0)
        symptom_score += supporting_match_ratio * 20
    else:
        if symptom_matches["supporting"] > 0:
            symptom_score += 10
    
    # Contradictory symptoms (penalty)
    if symptom_matches["contradictory"] > 0:
        symptom_score -= symptom_matches["contradictory"] * 15
    
    # Demographics score
    demographic_score = 0
    if age and sex:
        demographics = diagnosis_data.get("demographics", {})
        age_risk = demographics.get("age_risk", {})
        sex_risk = demographics.get("sex_risk", {})
        
        # Age risk
        if age < 40:
            age_multiplier = age_risk.get("<40", 0.5)
        elif age <= 70:
            age_multiplier = age_risk.get("40-70", 0.5)
        else:
            age_multiplier = age_risk.get(">70", 0.5)
        
        # Sex risk
        sex_multiplier = sex_risk.get(sex.lower(), 1.0)
        
        demographic_score = (age_multiplier + sex_multiplier - 1.0) * 10
    
    # Risk factors score
    risk_factor_score = 0
    diagnosis_risk_factors = diagnosis_data.get("risk_factors", [])
    matched_risk_factors = [rf for rf in risk_factors if rf in diagnosis_risk_factors]
    if diagnosis_risk_factors:
        risk_factor_ratio = len(matched_risk_factors) / len(diagnosis_risk_factors)
        risk_factor_score = risk_factor_ratio * 10
    
    # Total score
    total_score = base_score + symptom_score + demographic_score + risk_factor_score
    
    # Cap at 100
    total_score = min(100, max(0, total_score))
    
    return {
        "diagnosis": diagnosis_name,
        "score": round(total_score, 1),
        "base_score": round(base_score, 1),
        "symptom_score": round(symptom_score, 1),
        "demographic_score": round(demographic_score, 1),
        "risk_factor_score": round(risk_factor_score, 1),
        "symptom_matches": symptom_matches,
        "matched_risk_factors": matched_risk_factors,
        "urgency": diagnosis_data.get("urgency", "non_urgent"),
        "rule_out_first": diagnosis_data.get("rule_out_first", False),
        "workup": diagnosis_data.get("workup", {}),
        "management_hints": diagnosis_data.get("management_hints", ""),
        "data": diagnosis_data
    }


def generate_ddx(
    scenario_name: str,
    user_symptoms: List[str],
    age: Optional[int] = None,
    sex: Optional[str] = None,
    risk_factors: List[str] = None
) -> List[Dict[str, Any]]:
    """
    Generate ranked differential diagnoses for a scenario
    
    Args:
        scenario_name: Name of clinical scenario (e.g., "Chest Pain")
        user_symptoms: List of symptoms reported by user
        age: Patient age
        sex: Patient sex
        risk_factors: List of risk factors
    
    Returns:
        List of diagnoses ranked by score (highest first)
    """
    scenario_data = get_scenario_data(scenario_name)
    
    if not scenario_data:
        return []
    
    results = []
    
    for diagnosis_name, diagnosis_data in scenario_data.items():
        score_result = calculate_diagnosis_score(
            diagnosis_name,
            diagnosis_data,
            user_symptoms,
            age,
            sex,
            risk_factors
        )
        results.append(score_result)
    
    # Sort by score (highest first)
    results.sort(key=lambda x: x["score"], reverse=True)
    
    return results


def render_ddx_interface():
    """Render the DDx generator interface with Standard and Quick modes"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🩺 Chẩn đoán phân biệt</h2>
    <p style='text-align: center;'><em>Công cụ hỗ trợ quyết định lâm sàng</em></p>
    """, unsafe_allow_html=True)
    
    st.warning("""
    **⚠️ DISCLAIMER:**
    - Công cụ này CHỈ mang tính hỗ trợ quyết định lâm sàng
    - KHÔNG thay thế đánh giá lâm sàng của bác sĩ
    - Luôn đánh giá toàn diện và xét nghiệm phù hợp
    - Các chẩn đoán được sắp xếp theo khả năng, không phải chẩn đoán cuối cùng
    """)
    
    st.markdown("---")
    
    # Mode selection
    # Note: st.radio automatically stores value in session_state when key is provided
    mode = st.radio(
        "**Chọn chế độ:**",
        ["📋 Chế độ tiêu chuẩn (Chọn scenario trước)", "⚡ Chế độ nhanh (Nhập triệu chứng trước)"],
        key="ddx_mode",
        horizontal=True
    )
    
    st.markdown("---")
    
    from .ddx_data import get_all_scenarios, suggest_scenarios_from_symptoms
    scenarios = get_all_scenarios()
    
    # Quick Mode: Symptom-first approach
    if "nhanh" in mode.lower() or "quick" in mode.lower():
        st.markdown("### ⚡ Chế độ nhanh: Nhập triệu chứng")
        st.info("💡 Nhập các triệu chứng chính, hệ thống sẽ gợi ý scenario phù hợp nhất")
        
        # Symptom input (quick mode)
        quick_symptoms_text = st.text_input(
            "Nhập các triệu chứng (phân cách bằng dấu phẩy):",
            placeholder="Ví dụ: Đau ngực, Khó thở, Vã mồ hôi...",
            key="ddx_quick_symptoms",
            help="Nhập triệu chứng bằng tiếng Việt hoặc tiếng Anh"
        )
        
        if quick_symptoms_text:
            quick_symptoms_list = [s.strip() for s in quick_symptoms_text.split(',') if s.strip()]
            
            if st.button("🔍 Tìm scenario phù hợp", type="primary", use_container_width=True):
                suggested_scenarios = suggest_scenarios_from_symptoms(quick_symptoms_list)
                
                if suggested_scenarios:
                    st.success(f"✅ Tìm thấy {len(suggested_scenarios)} scenario phù hợp:")
                    
                    # Show top suggestions
                    top_3 = suggested_scenarios[:3]
                    cols = st.columns(min(len(top_3), 3))
                    for idx, (scenario_name, score) in enumerate(top_3):
                        with cols[idx]:
                            st.metric(
                                scenario_name,
                                f"{score:.1f}%",
                                help=f"Độ phù hợp: {score:.1f}%"
                            )
                    
                    # Let user select from suggestions or all scenarios
                    scenario_options = [f"{name} (Phù hợp: {score:.1f}%)" for name, score in suggested_scenarios[:5]]
                    scenario_options.extend([name for name in scenarios if name not in [s[0] for s in suggested_scenarios[:5]]])
                    
                    selected_idx = st.selectbox(
                        "Chọn scenario để tiếp tục:",
                        range(len(scenario_options)),
                        format_func=lambda x: scenario_options[x],
                        key="ddx_quick_scenario_select"
                    )
                    
                    # Extract scenario name (remove score suffix if present)
                    selected_option = scenario_options[selected_idx]
                    scenario = selected_option.split(" (")[0]
                    
                    # Store for later use
                    st.session_state['ddx_selected_scenario'] = scenario
                    st.session_state['ddx_quick_symptoms'] = quick_symptoms_list
                else:
                    st.warning("Không tìm thấy scenario phù hợp. Vui lòng chọn scenario thủ công:")
                    scenario = st.selectbox(
                        "Chọn clinical scenario:",
                        scenarios,
                        key="ddx_scenario_manual"
                    )
                    st.session_state['ddx_selected_scenario'] = scenario
            else:
                scenario = None
        else:
            scenario = None
            
        # Use selected scenario from session state if available
        if 'ddx_selected_scenario' in st.session_state:
            scenario = st.session_state['ddx_selected_scenario']
    
    # Standard Mode: Scenario-first approach
    else:
        scenario = st.selectbox(
            "**Chọn clinical scenario:**",
            scenarios,
            key="ddx_scenario"
        )
        st.session_state['ddx_selected_scenario'] = scenario
    
    if not scenario:
        st.info("👆 Vui lòng chọn scenario hoặc nhập triệu chứng để bắt đầu")
        return
    
    st.markdown("---")
    
    # Get scenario-specific symptoms
    scenario_data = get_scenario_data(scenario)
    all_symptoms = set()
    for dx_data in scenario_data.values():
        all_symptoms.update(dx_data["symptoms"].get("required", []))
        all_symptoms.update(dx_data["symptoms"].get("supporting", []))
    
    # Patient demographics
    st.markdown("### 📋 Thông tin bệnh nhân (Tùy chọn)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=0,
            max_value=120,
            value=None,
            step=1,
            key="ddx_age",
            help="Optional - Helps refine diagnosis probability"
        )
    
    with col2:
        sex = st.selectbox(
            "Giới tính",
            ["", "Nam", "Nữ"],
            key="ddx_sex",
            help="Optional"
        )
        sex = sex if sex else None
    
    st.markdown("---")
    
    # Symptoms selection
    st.markdown("### 🩺 Triệu chứng")
    st.info(f"Chọn các triệu chứng phù hợp với bệnh nhân. Scenario: **{scenario}**")
    
    # Group symptoms by category
    symptom_list = sorted(list(all_symptoms))
    
    # Pre-populate from quick mode if available
    pre_selected_symptoms = []
    if 'ddx_quick_symptoms' in st.session_state and st.session_state.get('ddx_mode', '').lower().find('nhanh') >= 0:
        quick_symptoms = st.session_state['ddx_quick_symptoms']
        # Try to match quick symptoms with scenario symptoms
        from .ddx_data import symptoms_match
        for quick_sym in quick_symptoms:
            for scenario_sym in symptom_list:
                if symptoms_match(quick_sym, scenario_sym):
                    if scenario_sym not in pre_selected_symptoms:
                        pre_selected_symptoms.append(scenario_sym)
                    break
    
    selected_symptoms = []
    
    # Display as checkboxes in columns
    num_cols = 3
    cols = st.columns(num_cols)
    
    for i, symptom in enumerate(symptom_list):
        col_idx = i % num_cols
        with cols[col_idx]:
            # Translate symptom to Vietnamese
            symptom_display = translate_symptom(symptom)
            # Pre-check if in quick mode and matched
            default_value = symptom in pre_selected_symptoms
            if st.checkbox(
                symptom_display,
                value=default_value,
                key=f"ddx_symptom_{i}_{scenario}",  # Include scenario in key to avoid conflicts
                help=f"Triệu chứng: {symptom_display}"
            ):
                selected_symptoms.append(symptom)
    
    # Allow free text input for additional symptoms
    st.markdown("---")
    additional_symptoms_text = st.text_input(
        "Triệu chứng khác (phân cách bằng dấu phẩy):",
        key="ddx_additional",
        help="Nhập các triệu chứng khác không có trong danh sách"
    )
    
    if additional_symptoms_text:
        additional_symptoms = [s.strip().lower() for s in additional_symptoms_text.split(",")]
        selected_symptoms.extend(additional_symptoms)
    
    st.markdown("---")
    
    # Risk factors (optional)
    st.markdown("### ⚠️ Yếu tố nguy cơ (Tùy chọn)")
    
    common_risk_factors = [
        "diabetes", "hypertension", "smoking", "obesity",
        "family_history_cad", "hyperlipidemia", "atrial_fibrillation",
        "malignancy", "immobility", "recent_surgery", "pregnancy"
    ]
    
    selected_risk_factors = []
    risk_cols = st.columns(4)
    
    for i, rf in enumerate(common_risk_factors):
        col_idx = i % 4
        with risk_cols[col_idx]:
            # Translate risk factor to Vietnamese
            rf_display = translate_risk_factor(rf)
            if st.checkbox(
                rf_display,
                key=f"ddx_rf_{i}",
                help=f"Yếu tố nguy cơ: {rf_display}"
            ):
                selected_risk_factors.append(rf)
    
    st.markdown("---")
    
    # Generate DDx button
    if st.button("🔍 Tạo Danh Sách Chẩn đoán Phân biệt", type="primary", use_container_width=True):
        if not selected_symptoms:
            st.error("⚠️ Vui lòng chọn ít nhất một triệu chứng!")
        else:
            # Generate DDx
            results = generate_ddx(
                scenario,
                selected_symptoms,
                age,
                sex,
                selected_risk_factors
            )
            
            if not results:
                st.warning("Không tìm thấy chẩn đoán phù hợp. Vui lòng thử lại với các triệu chứng khác.")
            else:
                # Separate into rule-out-first and others
                rule_out_first = [r for r in results if r["rule_out_first"]]
                others = [r for r in results if not r["rule_out_first"]]
                
                # Tabs for different views
                tab1, tab2, tab3 = st.tabs(["🚨 Rule-Out First", "📊 Tất Cả DDx", "🔬 Suggested Workup"])
                
                # Tab 1: Rule-Out First
                with tab1:
                    if rule_out_first:
                        st.error("## 🚨 RULE-OUT FIRST (Emergency/Urgent)")
                        st.warning("Các chẩn đoán này cần được loại trừ trước tiên do tính nguy hiểm cao!")
                        
                        for idx, result in enumerate(rule_out_first, 1):
                            urgency_color = {
                                "emergency": "🔴",
                                "urgent": "🟠",
                                "non_urgent": "🟢"
                            }.get(result["urgency"], "⚪")
                            
                            st.markdown(f"""
                            ### {urgency_color} **{idx}. {result['diagnosis']}** (Score: {result['score']:.1f}/100)
                            
                            **Mức độ khẩn cấp:** {result['urgency'].upper()}
                            """)
                            
                            # Score breakdown
                            with st.expander(f"📊 Chi tiết điểm số cho {result['diagnosis']}"):
                                col1, col2, col3, col4 = st.columns(4)
                                col1.metric("Base", f"{result['base_score']:.1f}")
                                col2.metric("Symptoms", f"{result['symptom_score']:.1f}")
                                col3.metric("Demographics", f"{result['demographic_score']:.1f}")
                                col4.metric("Risk Factors", f"{result['risk_factor_score']:.1f}")
                                
                                st.caption(f"Required symptoms matched: {result['symptom_matches']['required']}")
                                st.caption(f"Supporting symptoms matched: {result['symptom_matches']['supporting']}")
                                if result['matched_risk_factors']:
                                    st.caption(f"Risk factors: {', '.join(result['matched_risk_factors'])}")
                            
                            # Workup
                            st.markdown("**🔬 Immediate Workup:**")
                            workup = result.get("workup", {})
                            immediate = workup.get("immediate", [])
                            if immediate:
                                for item in immediate:
                                    st.markdown(f"☐ {item}")
                            else:
                                st.info("Không có xét nghiệm khẩn cấp cụ thể")
                            
                            # Management hints
                            if result.get("management_hints"):
                                st.info(f"💡 **Management:** {result['management_hints']}")
                            
                            st.markdown("---")
                    else:
                        st.success("✅ Không có chẩn đoán cần rule-out first trong danh sách này.")
                
                # Tab 2: All DDx
                with tab2:
                    st.markdown("## 📊 Tất Cả Chẩn đoán Phân biệt (Ranked)")
                    
                    for idx, result in enumerate(results, 1):
                        urgency_badge = {
                            "emergency": "🔴 EMERGENCY",
                            "urgent": "🟠 URGENT",
                            "non_urgent": "🟢 Non-urgent"
                        }.get(result["urgency"], "⚪")
                        
                        st.markdown(f"""
                        ### {idx}. **{result['diagnosis']}**
                        
                        **Score:** {result['score']:.1f}/100 | **Urgency:** {urgency_badge}
                        """)
                        
                        if result.get("rule_out_first"):
                            st.warning("⚠️ **Rule-out first!**")
                        
                        with st.expander(f"Chi tiết {result['diagnosis']}"):
                            st.markdown(f"**Symptom matches:**")
                            st.json(result['symptom_matches'])
                            
                            if result.get("workup"):
                                st.markdown(f"**Workup:**")
                                st.json(result["workup"])
                            
                            if result.get("management_hints"):
                                st.markdown(f"**Management hints:** {result['management_hints']}")
                        
                        st.markdown("---")
                
                # Tab 3: Suggested Workup Summary
                with tab3:
                    st.markdown("## 🔬 Suggested Workup Summary")
                    
                    # Collect all workup items
                    immediate_tests = set()
                    urgent_tests = set()
                    optional_tests = set()
                    
                    for result in rule_out_first:
                        workup = result.get("workup", {})
                        immediate_tests.update(workup.get("immediate", []))
                        urgent_tests.update(workup.get("within_6h", []))
                        optional_tests.update(workup.get("optional", []))
                    
                    if immediate_tests:
                        st.error("### 🚨 IMMEDIATE (< 1 hour):")
                        for test in sorted(immediate_tests):
                            st.markdown(f"☐ **{test}**")
                        st.markdown("")
                    
                    if urgent_tests:
                        st.warning("### ⚠️ URGENT (< 6 hours):")
                        for test in sorted(urgent_tests):
                            st.markdown(f"☐ **{test}**")
                        st.markdown("")
                    
                    if optional_tests:
                        st.info("### ℹ️ OPTIONAL:")
                        for test in sorted(optional_tests):
                            st.markdown(f"☐ **{test}**")

