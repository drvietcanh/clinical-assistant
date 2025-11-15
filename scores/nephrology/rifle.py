"""
RIFLE Criteria for Acute Kidney Injury
========================================

One of the first standardized classification systems for AKI (now superseded by KDIGO)

Reference:
- Bellomo R, et al. Acute renal failure - definition, outcome measures, animal models,
  fluid therapy and information technology needs: the Second International Consensus
  Conference of the Acute Dialysis Quality Initiative (ADQI) Group. Crit Care. 2004;8(4):R204-212.

RIFLE Categories (increasing severity):
- Risk
- Injury
- Failure
- Loss (of kidney function)
- ESRD (End-Stage Renal Disease)

Note: KDIGO has largely replaced RIFLE in modern practice, but RIFLE is still used in some
settings and has extensive historical validation data.
"""

import streamlit as st


def calculate_rifle(
    scr_baseline: float,
    scr_current: float,
    gfr_decrease_percent: float,
    urine_output_6h: float,
    urine_output_12h: float,
    weight: float
) -> dict:
    """Calculate RIFLE classification"""
    
    # Calculate creatinine fold increase
    if scr_baseline > 0:
        scr_fold = scr_current / scr_baseline
    else:
        scr_fold = 0
    
    # Calculate UO rate
    uo_6h_rate = (urine_output_6h / 6 / weight) if weight > 0 and urine_output_6h >= 0 else None
    uo_12h_rate = (urine_output_12h / 12 / weight) if weight > 0 and urine_output_12h >= 0 else None
    
    # Determine category
    category_by_scr = 0  # 0=none, 1=Risk, 2=Injury, 3=Failure
    category_by_uo = 0
    
    # SCr/GFR criteria
    if scr_fold >= 3.0 or gfr_decrease_percent >= 75 or scr_current >= 4.0:
        category_by_scr = 3  # Failure
    elif scr_fold >= 2.0 or gfr_decrease_percent >= 50:
        category_by_scr = 2  # Injury
    elif scr_fold >= 1.5 or gfr_decrease_percent >= 25:
        category_by_scr = 1  # Risk
    
    # UO criteria
    if uo_12h_rate is not None:
        if uo_12h_rate < 0.3 or urine_output_12h == 0:
            category_by_uo = 3  # Failure
        elif uo_12h_rate < 0.5:
            category_by_uo = 2  # Injury
    
    if uo_6h_rate is not None and category_by_uo < 1:
        if uo_6h_rate < 0.5:
            category_by_uo = 1  # Risk
    
    final_category = max(category_by_scr, category_by_uo)
    
    categories = ["Không AKI", "Risk", "Injury", "Failure"]
    colors = ["🟢", "🟡", "🟠", "🔴"]
    
    return {
        'category': final_category,
        'category_name': categories[final_category],
        'color': colors[final_category],
        'scr_fold': scr_fold,
        'uo_6h_rate': uo_6h_rate,
        'uo_12h_rate': uo_12h_rate
    }


def render():
    """Render RIFLE calculator"""
    
    st.title("🧪 RIFLE Criteria - Acute Kidney Injury")
    st.markdown("**Hệ thống phân loại AKI (Historical - KDIGO khuyến cáo hơn)**")
    
    st.info("""
    **ℹ️ Lưu Ý:**
    
    RIFLE là một trong những hệ thống phân loại AKI TIÊN PHONG (2004), nhưng hiện nay đã được 
    **thay thế bởi KDIGO** (2012) trong hầu hết các guidelines hiện đại.
    
    **Khuyến cáo:** Sử dụng **KDIGO** để đánh giá AKI theo guidelines hiện tại.
    
    RIFLE vẫn hữu ích cho:
    - Nghiên cứu sử dụng RIFLE criteria
    - So sánh với dữ liệu lịch sử
    - Hiểu diễn tiến của AKI classification
    """)
    
    with st.expander("ℹ️ Thông Tin RIFLE"):
        st.markdown("""
        ### RIFLE Categories
        
        | Phân Loại | Creatinine / GFR | Nước Tiểu |
        |-----------|------------------|-----------|
        | **Risk** | SCr ×1.5 HOẶC GFR giảm >25% | <0.5 mL/kg/h × 6h |
        | **Injury** | SCr ×2 HOẶC GFR giảm >50% | <0.5 mL/kg/h × 12h |
        | **Failure** | SCr ×3 HOẶC GFR giảm >75% HOẶC SCr ≥4 mg/dL | <0.3 mL/kg/h × 24h HOẶC anuria × 12h |
        | **Loss** | Mất chức năng thận hoàn toàn >4 tuần | |
        | **ESRD** | ESRD >3 tháng | |
        
        **Tài liệu:** Bellomo R, et al. *Crit Care* 2004;8:R204-212
        """)
    
    st.divider()
    
    # Simplified input
    col1, col2 = st.columns(2)
    
    with col1:
        scr_baseline = st.number_input("SCr Baseline (mg/dL)", 0.0, 20.0, 1.0, 0.1, format="%.1f")
        scr_current = st.number_input("SCr Hiện Tại (mg/dL)", 0.0, 20.0, 1.5, 0.1, format="%.1f")
        gfr_decrease_percent = st.number_input("GFR Giảm (%)", 0.0, 100.0, 0.0, 1.0, format="%.1f")
    
    with col2:
        weight = st.number_input("Cân Nặng (kg)", 0.0, 300.0, 70.0, 1.0, format="%.1f")
        urine_output_6h = st.number_input("Nước tiểu 6h (mL)", -1.0, 5000.0, -1.0, 10.0, format="%.0f")
        urine_output_12h = st.number_input("Nước tiểu 12h (mL)", -1.0, 10000.0, -1.0, 10.0, format="%.0f")
    
    if st.button("🧮 Đánh Giá RIFLE", type="primary"):
        result = calculate_rifle(scr_baseline, scr_current, gfr_decrease_percent, 
                                 urine_output_6h, urine_output_12h, weight)
        
        st.subheader("📊 Kết Quả")
        st.markdown(f"### {result['color']} {result['category_name']}")
        
        if result['scr_fold'] > 0:
            st.caption(f"Creatinine: {scr_baseline:.2f} → {scr_current:.2f} mg/dL ({result['scr_fold']:.2f}×)")
        
        if result['category'] > 0:
            st.warning("""
            ⚠️ **Khuyến cáo:**
            
            Để đánh giá và quản lý AKI theo guidelines hiện đại, vui lòng sử dụng **KDIGO Criteria**
            (có trong cùng module Nephrology).
            
            KDIGO cung cấp:
            - Phân loại chính xác hơn (Stage 1, 2, 3)
            - Hướng dẫn quản lý cập nhật
            - Tiêu chuẩn quốc tế hiện hành
            """)
        
        st.session_state['rifle_result'] = result

