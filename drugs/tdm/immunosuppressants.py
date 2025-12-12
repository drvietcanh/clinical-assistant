"""
Immunosuppressants TDM Calculator
Tacrolimus, Cyclosporine TDM
"""

import streamlit as st


def get_transplant_targets(transplant_type, time_post_transplant_months):
    """
    Get target trough levels based on transplant type and time
    
    Args:
        transplant_type: "kidney", "liver", "heart", "lung", "pancreas"
        time_post_transplant_months: Months since transplant
    
    Returns:
        dict with target ranges
    """
    targets = {
        "kidney": {
            "early": (10, 15),  # 0-3 months
            "intermediate": (8, 12),  # 3-12 months
            "late": (5, 10)  # > 12 months
        },
        "liver": {
            "early": (8, 12),
            "intermediate": (6, 10),
            "late": (5, 8)
        },
        "heart": {
            "early": (10, 15),
            "intermediate": (8, 12),
            "late": (5, 10)
        },
        "lung": {
            "early": (10, 15),
            "intermediate": (8, 12),
            "late": (5, 10)
        },
        "pancreas": {
            "early": (10, 15),
            "intermediate": (8, 12),
            "late": (5, 10)
        }
    }
    
    if time_post_transplant_months <= 3:
        period = "early"
    elif time_post_transplant_months <= 12:
        period = "intermediate"
    else:
        period = "late"
    
    target_min, target_max = targets[transplant_type][period]
    
    return {
        "target_min": target_min,
        "target_max": target_max,
        "period": period,
        "transplant_type": transplant_type
    }


def interpret_tacrolimus_level(level_ng_ml, transplant_type="kidney", time_post_months=1):
    """
    Interpret Tacrolimus level
    
    Args:
        level_ng_ml: Tacrolimus trough level (ng/mL)
        transplant_type: Type of transplant
        time_post_months: Months post-transplant
    
    Returns:
        dict with interpretation
    """
    targets = get_transplant_targets(transplant_type, time_post_months)
    target_min = targets["target_min"]
    target_max = targets["target_max"]
    
    if level_ng_ml < target_min:
        status = "subtherapeutic"
        level_text = "⬇️ Dưới mục tiêu"
        recommendation = f"Nồng độ thấp (< {target_min} ng/mL). Nguy cơ thải ghép. Cân nhắc tăng liều."
        color = "error"  # Critical for transplant
    elif level_ng_ml <= target_max:
        status = "therapeutic"
        level_text = "✅ Trong mục tiêu điều trị"
        recommendation = f"Nồng độ trong khoảng điều trị ({target_min}-{target_max} ng/mL). Tiếp tục liều hiện tại."
        color = "success"
    elif level_ng_ml <= target_max * 1.5:
        status = "supratherapeutic"
        level_text = "⚠️ Trên mục tiêu"
        recommendation = f"Nồng độ cao (> {target_max} ng/mL). Nguy cơ độc tính. Cân nhắc giảm liều."
        color = "warning"
    else:
        status = "toxic"
        level_text = "🚨 ĐỘC TÍNH - Nguy hiểm"
        recommendation = f"Nồng độ độc tính! Giảm liều ngay, theo dõi triệu chứng độc tính."
        color = "error"
    
    return {
        "status": status,
        "level_text": level_text,
        "therapeutic_range": f"{target_min}-{target_max} ng/mL",
        "recommendation": recommendation,
        "color": color,
        "current_level": level_ng_ml,
        "target_min": target_min,
        "target_max": target_max
    }


def interpret_cyclosporine_level(level_ng_ml, transplant_type="kidney", time_post_months=1, c2_level_ng_ml=None):
    """
    Interpret Cyclosporine level
    
    Args:
        level_ng_ml: Cyclosporine trough level (C0, ng/mL)
        transplant_type: Type of transplant
        time_post_months: Months post-transplant
        c2_level_ng_ml: Optional C2 level (2h post-dose)
    
    Returns:
        dict with interpretation
    """
    # Cyclosporine targets (C0 - trough)
    targets = {
        "kidney": {
            "early": (200, 300),
            "intermediate": (150, 250),
            "late": (100, 200)
        },
        "liver": {
            "early": (200, 300),
            "intermediate": (150, 250),
            "late": (100, 200)
        },
        "heart": {
            "early": (250, 350),
            "intermediate": (200, 300),
            "late": (150, 250)
        }
    }
    
    if time_post_months <= 3:
        period = "early"
    elif time_post_months <= 12:
        period = "intermediate"
    else:
        period = "late"
    
    target_min, target_max = targets.get(transplant_type, targets["kidney"])[period]
    
    if level_ng_ml < target_min:
        status = "subtherapeutic"
        level_text = "⬇️ Dưới mục tiêu"
        recommendation = f"Nồng độ thấp (< {target_min} ng/mL). Nguy cơ thải ghép. Cân nhắc tăng liều."
        color = "error"
    elif level_ng_ml <= target_max:
        status = "therapeutic"
        level_text = "✅ Trong mục tiêu điều trị"
        recommendation = f"Nồng độ trong khoảng điều trị ({target_min}-{target_max} ng/mL). Tiếp tục liều hiện tại."
        color = "success"
    elif level_ng_ml <= target_max * 1.5:
        status = "supratherapeutic"
        level_text = "⚠️ Trên mục tiêu"
        recommendation = f"Nồng độ cao (> {target_max} ng/mL). Nguy cơ độc tính. Cân nhắc giảm liều."
        color = "warning"
    else:
        status = "toxic"
        level_text = "🚨 ĐỘC TÍNH"
        recommendation = f"Nồng độ độc tính! Giảm liều ngay."
        color = "error"
    
    result = {
        "status": status,
        "level_text": level_text,
        "therapeutic_range": f"{target_min}-{target_max} ng/mL",
        "recommendation": recommendation,
        "color": color,
        "current_level": level_ng_ml,
        "target_min": target_min,
        "target_max": target_max
    }
    
    # Add C2 if available
    if c2_level_ng_ml:
        # C2 targets: usually 800-1200 ng/mL for kidney
        if 800 <= c2_level_ng_ml <= 1200:
            result["c2_status"] = "therapeutic"
        else:
            result["c2_status"] = "out_of_range"
        result["c2_level"] = c2_level_ng_ml
    
    return result


def render_immunosuppressants_tdm():
    """Render Immunosuppressants TDM Calculator Interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>💊 Immunosuppressants TDM</h2>
    <p style='text-align: center;'><em>Tacrolimus & Cyclosporine TDM for Transplant</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Immunosuppressants TDM (Transplant):**
    - **Tacrolimus:** Trough level (C0) - Mục tiêu thay đổi theo thời gian
    - **Cyclosporine:** Trough level (C0) hoặc C2 (2h post-dose)
    - **Quan trọng:** Mục tiêu phụ thuộc loại ghép và thời gian sau ghép
    - **Therapeutic index:** Rất hẹp - cần theo dõi chặt chẽ
    """)
    
    st.markdown("---")
    
    # Drug selection
    drug = st.radio(
        "Chọn thuốc:",
        ["Tacrolimus", "Cyclosporine"],
        horizontal=True,
        key="immuno_drug"
    )
    
    st.markdown("---")
    
    if drug == "Tacrolimus":
        st.markdown("### 💊 Tacrolimus TDM")
        
        tab1, tab2 = st.tabs(["📊 Giải thích nồng độ", "📋 Mục Tiêu Theo Thời Gian"])
        
        with tab1:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                level = st.number_input(
                    "Nồng độ Tacrolimus (ng/mL)",
                    min_value=0.0,
                    max_value=30.0,
                    value=8.0,
                    step=0.5,
                    format="%.1f",
                    key="tac_level",
                    help="Trough level (C0)"
                )
            
            with col2:
                transplant_type = st.selectbox(
                    "Loại ghép:",
                    ["Thận (Kidney)", "Gan (Liver)", "Tim (Heart)", "Phổi (Lung)", "Tụy (Pancreas)"],
                    key="tac_transplant"
                )
            
            with col3:
                time_post = st.number_input(
                    "Thời gian sau ghép (tháng)",
                    min_value=0,
                    max_value=120,
                    value=6,
                    step=1,
                    key="tac_time"
                )
            
            transplant_code = {
                "Thận": "kidney",
                "Gan": "liver",
                "Tim": "heart",
                "Phổi": "lung",
                "Tụy": "pancreas"
            }[transplant_type.split()[0]]
            
            st.markdown("---")
            
            if st.button("📊 Giải thích nồng độ", type="primary", use_container_width=True):
                interpretation = interpret_tacrolimus_level(level, transplant_code, time_post)
                
                st.markdown("### 📈 Kết quả")
                
                if interpretation['color'] == 'success':
                    st.success(f"**{interpretation['level_text']}**")
                elif interpretation['color'] == 'warning':
                    st.warning(f"**{interpretation['level_text']}**")
                else:
                    st.error(f"**{interpretation['level_text']}**")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric(
                        "Nồng độ hiện tại",
                        f"{interpretation['current_level']:.1f} ng/mL"
                    )
                
                with col2:
                    st.metric(
                        "Mục tiêu",
                        interpretation['therapeutic_range']
                    )
                
                st.markdown("---")
                
                if interpretation['color'] == 'error':
                    st.error(interpretation['recommendation'])
                elif interpretation['color'] == 'warning':
                    st.warning(interpretation['recommendation'])
                else:
                    st.success(interpretation['recommendation'])
                
                # Adjustment guide
                if interpretation['status'] == "subtherapeutic":
                    st.markdown("---")
                    st.error("""
                    **🚨 Nguy cơ thải ghép:**
                    
                    - Nồng độ dưới mục tiêu → Nguy cơ thải ghép tăng
                    - Cần tăng liều ngay
                    - Theo dõi triệu chứng thải ghép
                    - Kiểm tra compliance
                    """)
                
                if interpretation['status'] == "toxic":
                    st.markdown("---")
                    st.error("""
                    **🚨 Độc Tính Tacrolimus:**
                    
                    **Triệu chứng:**
                    - Độc thận (tăng creatinine)
                    - Độc thần kinh (run tay, co giật)
                    - Tăng đường huyết
                    - Huyết áp cao
                    - Hạ magne máu
                    
                    **Xử trí:**
                    - Giảm liều ngay
                    - Theo dõi creatinine, glucose, huyết áp
                    """)
        
        with tab2:
            st.markdown("### 📋 Mục Tiêu Tacrolimus Theo Thời Gian")
            
            transplant_type_table = st.selectbox(
                "Loại ghép:",
                ["Thận", "Gan", "Tim", "Phổi", "Tụy"],
                key="tac_table_type"
            )
            
            transplant_code = {
                "Thận": "kidney",
                "Gan": "liver",
                "Tim": "heart",
                "Phổi": "lung",
                "Tụy": "pancreas"
            }[transplant_type_table]
            
            st.markdown("---")
            
            import pandas as pd
            
            periods = []
            targets = []
            times = []
            
            for months, period_name in [(0, "0-3 tháng"), (4, "3-12 tháng"), (13, "> 12 tháng")]:
                targets_info = get_transplant_targets(transplant_code, months)
                periods.append(period_name)
                targets.append(f"{targets_info['target_min']}-{targets_info['target_max']} ng/mL")
                times.append(f"{months}-{months+12 if months < 12 else '∞'} tháng")
            
            df = pd.DataFrame({
                "Thời gian sau ghép": periods,
                "Mục tiêu (ng/mL)": targets,
                "Khoảng thời gian": times
            })
            
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            st.info("""
            **Lưu ý:**
            - Mục tiêu cao hơn trong giai đoạn sớm (0-3 tháng) - nguy cơ thải ghép cao nhất
            - Giảm dần theo thời gian để giảm độc tính
            - Mục tiêu có thể thay đổi theo protocol của từng trung tâm
            """)
    
    else:  # Cyclosporine
        st.markdown("### 💊 Cyclosporine TDM")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            level = st.number_input(
                "Nồng độ C0 - Trough (ng/mL)",
                min_value=0.0,
                max_value=500.0,
                value=150.0,
                step=10.0,
                format="%.0f",
                key="csa_c0_level"
            )
            
            c2_level = st.number_input(
                "Nồng độ C2 (ng/mL) - nếu có",
                min_value=0.0,
                max_value=2000.0,
                value=0.0,
                step=50.0,
                format="%.0f",
                key="csa_c2_level",
                help="C2 = 2 giờ sau liều (một số protocol dùng C2 thay vì C0)"
            )
        
        with col2:
            transplant_type = st.selectbox(
                "Loại ghép:",
                ["Thận (Kidney)", "Gan (Liver)", "Tim (Heart)"],
                key="csa_transplant"
            )
        
        with col3:
            time_post = st.number_input(
                "Thời gian sau ghép (tháng)",
                min_value=0,
                max_value=120,
                value=6,
                step=1,
                key="csa_time"
            )
        
        transplant_code = {
            "Thận": "kidney",
            "Gan": "liver",
            "Tim": "heart"
        }[transplant_type.split()[0]]
        
        st.markdown("---")
        
        if st.button("📊 Giải thích nồng độ", type="primary", use_container_width=True):
            c2_val = c2_level if c2_level > 0 else None
            interpretation = interpret_cyclosporine_level(level, transplant_code, time_post, c2_val)
            
            st.markdown("### 📈 Kết quả")
            
            if interpretation['color'] == 'success':
                st.success(f"**{interpretation['level_text']}**")
            elif interpretation['color'] == 'warning':
                st.warning(f"**{interpretation['level_text']}**")
            else:
                st.error(f"**{interpretation['level_text']}**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "C0 - Trough",
                    f"{interpretation['current_level']:.0f} ng/mL"
                )
                
                st.metric(
                    "Mục tiêu C0",
                    interpretation['therapeutic_range']
                )
            
            with col2:
                if interpretation.get('c2_level'):
                    st.metric(
                        "C2 - 2h post-dose",
                        f"{interpretation['c2_level']:.0f} ng/mL"
                    )
                    
                    if interpretation.get('c2_status') == 'therapeutic':
                        st.success("✅ C2 trong mục tiêu (800-1200 ng/mL)")
                    else:
                        st.warning("⚠️ C2 ngoài mục tiêu")
            
            st.markdown("---")
            
            if interpretation['color'] == 'error':
                st.error(interpretation['recommendation'])
            elif interpretation['color'] == 'warning':
                st.warning(interpretation['recommendation'])
            else:
                st.success(interpretation['recommendation'])
            
            st.markdown("---")
            st.info("""
            **📋 Cyclosporine TDM:**
            
            **C0 (Trough):** Ngay trước liều tiếp theo
            **C2:** 2 giờ sau liều (một số protocol ưa dùng C2 hơn)
            
            **Mục tiêu C2 (Kidney):**
            - Giai đoạn sớm: 800-1200 ng/mL
            - Giai đoạn muộn: 600-1000 ng/mL
            """)
    
    # Common monitoring
    st.markdown("---")
    with st.expander("📊 Monitoring Định Kỳ"):
        st.markdown("""
        **Theo dõi định kỳ cho bệnh nhân ghép tạng:**
        
        **TDM:**
        - Lần đầu: Sau 2-3 ngày
        - Giai đoạn sớm: 2-3 lần/tuần
        - Giai đoạn muộn: Mỗi 1-3 tháng
        
        **Labs khác:**
        - Creatinine, eGFR
        - LFT (AST, ALT, bilirubin)
        - Glucose
        - Huyết áp
        - Magne máu (Tacrolimus)
        """)
    
    # Drug interactions
    st.markdown("---")
    with st.expander("⚠️ Tương Tác Thuốc Quan Trọng"):
        st.markdown("""
        **Thuốc TĂNG nồng độ (tăng độc tính):**
        - **Ketoconazole, Itraconazole, Voriconazole** (rất mạnh!)
        - **Clarithromycin, Erythromycin**
        - **Diltiazem, Verapamil**
        - **Grapefruit juice** (Cyclosporine)
        
        **Thuốc GIẢM nồng độ (tăng nguy cơ thải ghép):**
        - **Rifampin** (rất mạnh!)
        - **Carbamazepine, Phenytoin**
        - **St. John's wort**
        
        **⚠️ Cực kỳ quan trọng:** Kiểm tra tương tác trước khi thêm thuốc mới!
        """)
    
    # References
    st.markdown("---")
    with st.expander("📚 Tài liệu tham khảo"):
        st.markdown("""
        - **AST/ASTS Guidelines - Transplant**
        - **KDIGO Guidelines - Kidney Transplant**
        - **Tacrolimus:** Half-life ~12 giờ
        - **Cyclosporine:** Half-life ~8-27 giờ (variable)
        - **Therapeutic index:** Rất hẹp
        """)

