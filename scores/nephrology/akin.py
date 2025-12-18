"""
AKIN Criteria for Acute Kidney Injury
======================================

Acute Kidney Injury Network classification (2007)
Modified from RIFLE, now superseded by KDIGO

Reference:
- Mehta RL, et al. Acute Kidney Injury Network: report of an initiative to improve
  outcomes in acute kidney injury. Crit Care. 2007;11(2):R31.

AKIN Stages:
- Stage 1: SCr increase ≥0.3 mg/dL or 1.5-2× baseline; UO <0.5 mL/kg/h × 6h
- Stage 2: SCr 2-3× baseline; UO <0.5 mL/kg/h × 12h
- Stage 3: SCr >3× baseline or ≥4 mg/dL or RRT; UO <0.3 mL/kg/h × 24h or anuria × 12h

Note: AKIN was a refinement of RIFLE and has been incorporated into KDIGO (2012),
which is now the international standard.
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def calculate_akin(
    scr_baseline: float,
    scr_current: float,
    scr_increase_48h: float,
    urine_output_6h: float,
    urine_output_12h: float,
    urine_output_24h: float,
    weight: float,
    on_rrt: bool
) -> dict:
    """Calculate AKIN stage"""
    
    # Calculate creatinine fold increase
    if scr_baseline > 0:
        scr_fold = scr_current / scr_baseline
    else:
        scr_fold = 0
    
    # Calculate UO rates
    uo_6h_rate = (urine_output_6h / 6 / weight) if weight > 0 and urine_output_6h >= 0 else None
    uo_12h_rate = (urine_output_12h / 12 / weight) if weight > 0 and urine_output_12h >= 0 else None
    uo_24h_rate = (urine_output_24h / 24 / weight) if weight > 0 and urine_output_24h >= 0 else None
    
    # Determine stage
    stage_by_scr = 0
    stage_by_uo = 0
    
    # SCr criteria
    if on_rrt or scr_current >= 4.0 or scr_fold >= 3.0:
        stage_by_scr = 3
    elif scr_fold >= 2.0:
        stage_by_scr = 2
    elif scr_fold >= 1.5 or scr_increase_48h >= 0.3:
        stage_by_scr = 1
    
    # UO criteria
    if uo_24h_rate is not None:
        if uo_24h_rate < 0.3 or urine_output_24h == 0:
            stage_by_uo = 3
    
    if uo_12h_rate is not None:
        if uo_12h_rate < 0.5 and stage_by_uo < 2:
            stage_by_uo = 2
        elif uo_12h_rate == 0:
            stage_by_uo = 3
    
    if uo_6h_rate is not None and stage_by_uo < 1:
        if uo_6h_rate < 0.5:
            stage_by_uo = 1
    
    final_stage = max(stage_by_scr, stage_by_uo)
    
    stage_names = ["Không AKI", "Stage 1", "Stage 2", "Stage 3"]
    colors = ["🟢", "🟡", "🟠", "🔴"]
    
    return {
        'stage': final_stage,
        'stage_name': stage_names[final_stage],
        'color': colors[final_stage],
        'scr_fold': scr_fold,
        'uo_6h_rate': uo_6h_rate,
        'uo_12h_rate': uo_12h_rate,
        'uo_24h_rate': uo_24h_rate
    }


def render():
    """Render AKIN calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'akin':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'AKIN')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("🧪 AKIN Criteria - Acute Kidney Injury")
    st.markdown("**Acute Kidney Injury Network Classification (Historical)**")
    
    st.info("""
    **ℹ️ Lưu ý quan trọng:**
    
    AKIN (2007) là phiên bản cải tiến của RIFLE, nhưng hiện nay đã được **hợp nhất vào KDIGO** (2012).
    
    **KDIGO = AKIN + improvements:**
    - KDIGO sử dụng các tiêu chí tương tự AKIN
    - Có thêm các hướng dẫn quản lý chi tiết
    - Là tiêu chuẩn quốc tế hiện hành
    
    **Khuyến cáo:** Sử dụng **KDIGO** để đánh giá và quản lý AKI.
    """)
    
    with st.expander("ℹ️ Thông tin AKIN"):
        st.markdown("""
        ### AKIN Stages (2007)
        
        | Stage | Creatinine | Nước tiểu |
        |-------|------------|-----------|
        | **1** | ↑≥0.3 mg/dL HOẶC ×1.5-2 baseline | <0.5 mL/kg/h × 6h |
        | **2** | ×2-3 baseline | <0.5 mL/kg/h × 12h |
        | **3** | ×>3 baseline HOẶC ≥4 mg/dL HOẶC RRT | <0.3 mL/kg/h × 24h HOẶC anuria × 12h |
        
        **Điểm Khác Biệt với RIFLE:**
        - Thêm tiêu chí "tăng ≥0.3 mg/dL"
        - Rõ ràng hơn về thời gian window (48h)
        - Đơn giản hóa phân loại (3 stages thay vì 5 categories)
        
        **Tài liệu:** Mehta RL, et al. *Crit Care* 2007;11:R31
        """)
    
    st.divider()
    
    # Input
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="akin",
            calculator_name="AKIN",
            category="Thận",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Creatinine")
        scr_baseline = st.number_input("SCr Baseline (mg/dL)", 0.0, 20.0, 1.0, 0.1, format="%.1f")
        scr_current = st.number_input("SCr Hiện tại (mg/dL)", 0.0, 20.0, 1.5, 0.1, format="%.1f")
        scr_increase_48h = st.number_input("SCr Tăng trong 48h (mg/dL)", 0.0, 10.0, 0.0, 0.1, format="%.1f")
        on_rrt = st.checkbox("Đang chạy thận (RRT)")
    
    with col2:
        st.markdown("#### Nước tiểu")
        weight = st.number_input("Cân nặng (kg)", 0.0, 300.0, 50.0, 1.0, format="%.1f")
        urine_output_6h = st.number_input("Nước tiểu 6h (mL)", -1.0, 5000.0, -1.0, 10.0, format="%.0f")
        urine_output_12h = st.number_input("Nước tiểu 12h (mL)", -1.0, 10000.0, -1.0, 10.0, format="%.0f")
        urine_output_24h = st.number_input("Nước tiểu 24h (mL)", -1.0, 20000.0, -1.0, 10.0, format="%.0f")
    
    if st.button("🧮 Đánh giá AKIN Stage", type="primary"):
        result = calculate_akin(scr_baseline, scr_current, scr_increase_48h,
                                urine_output_6h, urine_output_12h, urine_output_24h,
                                weight, on_rrt)
        
        st.subheader("📊 Kết quả")
        st.markdown(f"### {result['color']} {result['stage_name']}")
        
        if result['scr_fold'] > 0:
            st.caption(f"Creatinine: {scr_baseline:.2f} → {scr_current:.2f} mg/dL ({result['scr_fold']:.2f}×)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("AKIN Stage", result['stage'] if result['stage'] > 0 else "Không AKI")
        with col_b:
            if result['stage'] > 0:
                kdigo_equivalent = ["", "KDIGO 1", "KDIGO 2", "KDIGO 3"][result['stage']]
                st.metric("Tương Đương", kdigo_equivalent)
        
        if result['stage'] > 0:
            st.warning("""
            ⚠️ **Khuyến cáo:**
            
            AKIN stage này tương đương với KDIGO stage tương ứng. 
            
            Để có hướng dẫn quản lý chi tiết và cập nhật nhất, vui lòng sử dụng **KDIGO Calculator**
            (có trong cùng module Nephrology).
            
            **KDIGO cung cấp:**
            - Hướng dẫn xử trí chi tiết cho từng giai đoạn
            - Tiêu chuẩn quốc tế hiện hành (2012-2024)
            - Khuyến cáo về RRT và biến chứng
            """)
        
        st.info("""
        **📊 So Sánh RIFLE vs AKIN vs KDIGO:**
        
        | Đặc Điểm | RIFLE (2004) | AKIN (2007) | KDIGO (2012) |
        |----------|--------------|-------------|--------------|
        | **Phân loại** | 5 categories | 3 stages | 3 stages |
        | **Thời gian** | 7 ngày | 48h | 48h (SCr), 7 ngày (fold) |
        | **Tiêu chí SCr** | Fold increase | Fold + absolute (≥0.3) | Giống AKIN |
        | **Tiêu chí UO** | Có | Có | Có (giống AKIN) |
        | **Status** | Historical | Historical | **CURRENT STANDARD** ✅ |
        
        **Kết luận:** KDIGO kết hợp ưu điểm của cả RIFLE và AKIN, là tiêu chuẩn quốc tế hiện tại.
        """)
        
        # Prepare data for history and share
        inputs_dict = {
            "SCr Baseline (mg/dL)": scr_baseline,
            "SCr Hiện tại (mg/dL)": scr_current,
            "SCr Tăng trong 48h (mg/dL)": scr_increase_48h,
            "Cân nặng (kg)": weight,
            "Nước tiểu 6h (mL)": urine_output_6h if urine_output_6h >= 0 else None,
            "Nước tiểu 12h (mL)": urine_output_12h if urine_output_12h >= 0 else None,
            "Nước tiểu 24h (mL)": urine_output_24h if urine_output_24h >= 0 else None,
            "Đang RRT": "Có" if on_rrt else "Không"
        }
        
        results_dict = {
            "AKIN Stage": result['stage_name'],
            "SCr fold increase": round(result['scr_fold'], 2) if result['scr_fold'] > 0 else None,
            "UO rate 6h (mL/kg/h)": round(result['uo_6h_rate'], 2) if result['uo_6h_rate'] else None,
            "UO rate 12h (mL/kg/h)": round(result['uo_12h_rate'], 2) if result['uo_12h_rate'] else None,
            "UO rate 24h (mL/kg/h)": round(result['uo_24h_rate'], 2) if result['uo_24h_rate'] else None
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="AKIN",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="AKIN"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="akin",
            calculator_name="AKIN",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="akin",
            calculator_name="AKIN",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="akin", show_actions=True)
        
        st.session_state['akin_result'] = result
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("AKIN")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

