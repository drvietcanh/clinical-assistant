"""
KDIGO Criteria for Acute Kidney Injury (AKI)
=============================================

Current gold standard for AKI classification and staging

Reference:
- KDIGO Clinical Practice Guideline for Acute Kidney Injury. 
  Kidney Int Suppl. 2012;2(1):1-138.
- Kellum JA, et al. Diagnosis, evaluation, and management of acute kidney injury: 
  a KDIGO summary (Part 1). Crit Care. 2013;17(1):204.

Definition of AKI (ANY of the following):
1. Serum creatinine increase ≥0.3 mg/dL (≥26.5 μmol/L) within 48 hours
2. Serum creatinine increase ≥1.5× baseline within 7 days
3. Urine output <0.5 mL/kg/h for 6 hours

KDIGO Stages:
- Stage 1: SCr 1.5-1.9× baseline OR ≥0.3 mg/dL increase; UO <0.5 mL/kg/h for 6-12h
- Stage 2: SCr 2.0-2.9× baseline; UO <0.5 mL/kg/h for ≥12h
- Stage 3: SCr ≥3× baseline OR ≥4.0 mg/dL OR initiation of RRT; UO <0.3 mL/kg/h for ≥24h OR anuria ≥12h

Clinical Utility:
- Internationally accepted standard
- Combines and improves upon RIFLE and AKIN
- Guides management and prognosis
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def calculate_kdigo(
    scr_baseline: float,
    scr_current: float,
    scr_increase_48h: float,
    urine_output_6h: float,
    urine_output_12h: float,
    urine_output_24h: float,
    weight: float,
    on_rrt: bool
) -> dict:
    """
    Calculate KDIGO AKI stage
    
    Args:
        scr_baseline: Baseline serum creatinine (mg/dL)
        scr_current: Current serum creatinine (mg/dL)
        scr_increase_48h: SCr increase within 48h (mg/dL)
        urine_output_6h: Total urine output in 6 hours (mL)
        urine_output_12h: Total urine output in 12 hours (mL)
        urine_output_24h: Total urine output in 24 hours (mL)
        weight: Body weight (kg)
        on_rrt: Patient on renal replacement therapy
    
    Returns:
        Dictionary containing stage, interpretation, recommendations
    """
    
    # Calculate fold increase
    if scr_baseline > 0:
        scr_fold = scr_current / scr_baseline
    else:
        scr_fold = 0
    
    # Calculate hourly urine output (mL/kg/h)
    uo_6h_rate = (urine_output_6h / 6 / weight) if weight > 0 and urine_output_6h >= 0 else None
    uo_12h_rate = (urine_output_12h / 12 / weight) if weight > 0 and urine_output_12h >= 0 else None
    uo_24h_rate = (urine_output_24h / 24 / weight) if weight > 0 and urine_output_24h >= 0 else None
    
    # Determine stage based on creatinine
    stage_by_scr = 0
    scr_criteria = []
    
    if on_rrt:
        stage_by_scr = 3
        scr_criteria.append("Đang chạy thận nhân tạo (RRT) → Giai đoạn 3")
    elif scr_current >= 4.0:
        stage_by_scr = 3
        scr_criteria.append(f"SCr ≥4.0 mg/dL (hiện tại: {scr_current:.2f}) → Giai đoạn 3")
    elif scr_fold >= 3.0:
        stage_by_scr = 3
        scr_criteria.append(f"SCr tăng ≥3× baseline ({scr_fold:.1f}×) → Giai đoạn 3")
    elif scr_fold >= 2.0:
        stage_by_scr = 2
        scr_criteria.append(f"SCr tăng 2.0-2.9× baseline ({scr_fold:.1f}×) → Giai đoạn 2")
    elif scr_fold >= 1.5:
        stage_by_scr = 1
        scr_criteria.append(f"SCr tăng 1.5-1.9× baseline ({scr_fold:.1f}×) → Giai đoạn 1")
    elif scr_increase_48h >= 0.3:
        stage_by_scr = 1
        scr_criteria.append(f"SCr tăng ≥0.3 mg/dL trong 48h (+{scr_increase_48h:.2f}) → Giai đoạn 1")
    
    # Determine stage based on urine output
    stage_by_uo = 0
    uo_criteria = []
    
    if uo_24h_rate is not None:
        if uo_24h_rate < 0.3:
            stage_by_uo = 3
            uo_criteria.append(f"Nước tiểu <0.3 mL/kg/h × 24h ({uo_24h_rate:.2f} mL/kg/h) → Giai đoạn 3")
        elif uo_24h_rate < 0.5 and urine_output_24h >= 0:
            # Check if <0.5 for 24h (Stage 3) or just 12h (Stage 2)
            if uo_12h_rate is not None and uo_12h_rate < 0.5:
                stage_by_uo = max(stage_by_uo, 2)
                uo_criteria.append(f"Nước tiểu <0.5 mL/kg/h × 12h ({uo_12h_rate:.2f} mL/kg/h) → Giai đoạn 2")
    
    if uo_12h_rate is not None and uo_12h_rate < 0.5 and stage_by_uo < 2:
        stage_by_uo = max(stage_by_uo, 2)
        uo_criteria.append(f"Nước tiểu <0.5 mL/kg/h × 12h ({uo_12h_rate:.2f} mL/kg/h) → Giai đoạn 2")
    
    if uo_6h_rate is not None and uo_6h_rate < 0.5 and stage_by_uo == 0:
        stage_by_uo = 1
        uo_criteria.append(f"Nước tiểu <0.5 mL/kg/h × 6-12h ({uo_6h_rate:.2f} mL/kg/h) → Giai đoạn 1")
    
    # Check for anuria
    if uo_12h_rate is not None and uo_12h_rate == 0:
        stage_by_uo = 3
        uo_criteria.append(f"Vô niệu (anuria) ≥12h → Giai đoạn 3")
    
    # Final stage is the higher of the two
    final_stage = max(stage_by_scr, stage_by_uo)
    
    # Generate interpretation
    if final_stage == 0:
        stage_text = "KHÔNG CÓ AKI"
        stage_color = "🟢"
        risk_class = "NO_AKI"
        interpretation = """
        **🟢 Không đủ tiêu chuẩn chẩn đoán AKI**
        
        Bệnh nhân hiện tại không đáp ứng tiêu chuẩn KDIGO cho AKI.
        
        **Lưu ý:**
        - Tiếp tục theo dõi chức năng thận
        - Tránh các yếu tố nguy cơ AKI
        - Nếu có nghi ngờ lâm sàng → tái đánh giá
        """
    elif final_stage == 1:
        stage_text = "AKI GIAI ĐOẠN 1 (Mild)"
        stage_color = "🟡"
        risk_class = "STAGE_1"
        interpretation = """
        **🟡 AKI Giai Đoạn 1 - Nhẹ**
        
        **Tỷ lệ tử vong:**
        - Trong bệnh viện: ~5-10%
        - Nếu tiến triển sang Stage 2-3: nguy cơ tăng đáng kể
        
        **Tiên lượng:**
        - Hầu hết hồi phục hoàn toàn nếu điều trị sớm
        - Nguy cơ chuyển thành CKD: thấp (~5-10%)
        - Cần theo dõi sát để phát hiện tiến triển
        """
    elif final_stage == 2:
        stage_text = "AKI GIAI ĐOẠN 2 (Moderate)"
        stage_color = "🟠"
        risk_class = "STAGE_2"
        interpretation = """
        **🟠 AKI Giai Đoạn 2 - Trung Bình**
        
        **Tỷ lệ tử vong:**
        - Trong bệnh viện: ~15-25%
        - Nguy cơ tiến triển sang Stage 3: ~30-40%
        
        **Tiên lượng:**
        - Hồi phục: ~60-70% nếu điều trị kịp thời
        - Nguy cơ chuyển thành CKD: trung bình (~15-25%)
        - Cần can thiệp tích cực và theo dõi sát
        """
    else:  # stage == 3
        stage_text = "AKI GIAI ĐOẠN 3 (Severe)"
        stage_color = "🔴"
        risk_class = "STAGE_3"
        interpretation = """
        **🔴 AKI Giai Đoạn 3 - Nặng**
        
        **Tỷ lệ tử vong:**
        - Trong bệnh viện: ~30-60%
        - Nếu cần RRT: tử vong ~50-70%
        
        **Tiên lượng:**
        - Hồi phục hoàn toàn: ~40-50%
        - Nguy cơ chuyển thành CKD: cao (~25-40%)
        - Nguy cơ cần RRT lâu dài: ~10-15%
        - Cần can thiệp tích cực NGAY, xem xét RRT
        """
    
    # Management recommendations
    if final_stage == 0:
        management = """
        **Quản lý - Không AKI:**
        
        1. **Dự phòng:**
           - Duy trì euvolemia
           - Tránh thuốc độc thận (NSAIDs, aminoglycosides, contrast)
           - Điều chỉnh liều thuốc theo chức năng thận
        
        2. **Theo dõi:**
           - SCr, BUN định kỳ nếu có yếu tố nguy cơ
           - Theo dõi cân nặng, cân bằng dịch
           - Đánh giá nước tiểu
        """
    elif final_stage == 1:
        management = """
        **Xử trí khuyến cáo - Stage 1:**
        
        1. **TÌM VÀ XỬ TRÍ NGUYÊN NHÂN:**
           - **Tiền thận (Pre-renal):** Giảm thể tích, giảm CO, thuốc giãn mạch
             → Truyền dịch, ngừng ACEI/ARB, vasopressor nếu cần
           - **Thận (Intrinsic):** ATN, AIN, GN, rhabdomyolysis
             → Điều trị specific (corticosteroid cho AIN, hydration cho rhabdo)
           - **Sau thận (Post-renal):** Tắc nghẽn
             → Đặt catheter, nephrostomy, xử lý tắc nghẽn
        
        2. **HỒI SỨC DỊCH:**
           - Đánh giá tình trạng dịch (CVP, echo, passive leg raise)
           - Nếu giảm thể tích → NS/LR 500-1000 mL bolus, đánh giá lại
           - Tránh truyền dịch quá mức (nguy cơ phù phổi)
        
        3. **ĐIỀU CHỈNH THUỐC:**
           - **DỪNG:** NSAIDs, ACEI/ARB, aminoglycosides, contrast agents
           - **Điều chỉnh liều:** Vancomycin, metformin, digoxin, LMWH
           - Xem lại TẤT CẢ thuốc - adjust theo GFR
        
        4. **Theo dõi:**
           - SCr, BUN: Hàng ngày hoặc 2 lần/ngày
           - Điện giải (K, Na, Mg, PO4): Hàng ngày
           - Nước tiểu: Mỗi 4-6 giờ
           - Cân nặng: Hàng ngày
           - Cân bằng dịch: Chặt chẽ
        
        5. **XÉT NGHIỆM BỔ SUNG:**
           - Urinalysis, urine microscopy (tìm casts, cells)
           - FENa / FEUrea (phân biệt tiền thận vs thận)
           - Siêu âm thận (loại trừ tắc nghẽn, hydronephrosis)
           - Consider: ANA, ANCA, complement (nếu nghi GN)
        """
    elif final_stage == 2:
        management = """
        **Xử trí khuyến cáo - Stage 2:**
        
        1. **CẤP CỨU & TÌM NGUYÊN NHÂN:**
           - Đánh giá NGAY: Pre-renal vs Intrinsic vs Post-renal
           - Siêu âm thận CẤP (loại trừ tắc nghẽn)
           - Xem xét tư vấn Thận sớm
        
        2. **HỒI SỨC DỊCH TÍCH CỰC:**
           - Đánh giá hemodynamic toàn diện
           - Nếu hypovolemic → NS/LR 1000-2000 mL, theo dõi đáp ứng
           - Nếu shock → vasopressor (norepinephrine ưu tiên)
           - Mục tiêu: MAP ≥65 mmHg, CVP 8-12 mmHg, UO >0.5 mL/kg/h
        
        3. **ĐIỀU CHỈNH THUỐC TRIỆT ĐỂ:**
           - **DỪNG NGAY:** Tất cả thuốc độc thận
           - **Điều chỉnh liều:** Tất cả thuốc bài tiết qua thận
           - **Tránh:** Contrast agents (trừ khi cực kỳ cần thiết)
        
        4. **QUẢN LÝ BIẾN CHỨNG:**
           - **Tăng kali:** Mục tiêu K <5.5 mEq/L
             * Calcium gluconate 10% 10 mL IV (nếu K >6.5 hoặc ECG thay đổi)
             * Insulin 10 U + D50 50 mL IV
             * Salbutamol nebulizer 10-20 mg
             * Kayexalate hoặc patiromer
           - **Tăng phosphate:** Phosphate binder
           - **Toan chuyển hóa:** Sodium bicarbonate (nếu pH <7.2)
           - **Phù:** Furosemide (nếu còn đáp ứng); cân nhắc RRT nếu phù phổi
        
        5. **THEO DÕI SÁT:**
           - SCr, BUN: 2 lần/ngày
           - Điện giải: 2-3 lần/ngày
           - Nước tiểu: Mỗi 1-2 giờ
           - ABG: Nếu acidosis
           - Cân nặng: 2 lần/ngày
        
        6. **CHUẨN BỊ RRT:**
           - Sẵn sàng cho RRT nếu tiến triển
           - Bảo vệ tĩnh mạch cánh tay (cho fistula sau này)
        """
    else:  # stage == 3
        management = """
        **Xử trí khuyến cáo - Stage 3:**
        
        1. **TƯ VẤN THẬN NGAY LẬP TỨC:**
           - Đây là cấp cứu thận học
           - Xem xét RRT (chạy thận nhân tạo)
        
        2. **CHỈ ĐỊNH RRT (Renal Replacement Therapy):**
           
           **Chỉ định TUYỆT ĐỐI:**
           - **A**cidosis: pH <7.1, không đáp ứng bicarbonate
           - **E**lectrolyte: Hyperkalemia (K >6.5) không đáp ứng điều trị
           - **I**ntoxication: Methanol, ethylene glycol, lithium, salicylates
           - **O**verload: Phù phổi không đáp ứng lợi tiểu
           - **U**remia: BUN >100 mg/dL + triệu chứng (pericarditis, encephalopathy, bleeding)
           
           **Chỉ định TƯƠNG ĐỐI:**
           - Oliguria (<200 mL/12h) không đáp ứng
           - BUN >80-100 mg/dL
           - Không thể cung cấp dinh dưỡng do hạn chế dịch
        
        3. **LOẠI HÌNH RRT:**
           - **CRRT (Continuous RRT):** Ưu tiên nếu hemodynamic không ổn định
           - **IHD (Intermittent Hemodialysis):** Nếu hemodynamic ổn định
           - **SLED (Sustained Low-Efficiency Dialysis):** Thỏa hiệp giữa CRRT và IHD
        
        4. **HỒI SỨC TÍCH CỰC:**
           - ICU monitoring
           - Hỗ trợ hemodynamic (vasopressor/inotrope)
           - Điều trị nhiễm trùng nếu có (sepsis thường gặp)
           - Điều trị nguyên nhân gốc
        
        5. **QUẢN LÝ BIẾN CHỨNG:**
           - **Hyperkalemia (K >6.5):**
             * Calcium gluconate 10% 10-20 mL IV STAT
             * Insulin 10 U + D50 50 mL IV
             * Salbutamol nebulizer 10-20 mg
             * RRT nếu không đáp ứng
           - **Phù phổi:**
             * O2, NIPPV/intubation nếu cần
             * Furosemide 40-200 mg IV (có thể không hiệu quả)
             * RRT khẩn cấp
           - **Toan nặng (pH <7.2):**
             * Sodium bicarbonate 1-2 amps IV
             * RRT nếu không đáp ứng
           - **Uremic pericarditis:**
             * RRT NGAY
           - **Rối loạn đông máu:**
             * Tránh thủ thuật xâm lấn
             * Xem xét DDAVP, cryoprecipitate
        
        6. **DINH DƯỠNG:**
           - Năng lượng: 25-30 kcal/kg/day
           - Protein: 1.2-1.5 g/kg/day (nếu trên RRT)
           - Hạn chế K, PO4
        
        7. **Theo dõi:**
           - SCr, BUN: 2-3 lần/ngày
           - Điện giải: 3-4 lần/ngày
           - ABG: Khi cần (nếu acidosis)
           - Nước tiểu: Liên tục
        
        8. **DỰ PHÒNG BIẾN CHỨNG:**
           - DVT prophylaxis (LMWH dose-adjusted hoặc SCDs)
           - Stress ulcer prophylaxis (PPI)
           - Avoid nephrotoxins TUYỆT ĐỐI
        """
    
    return {
        'stage': final_stage,
        'stage_text': stage_text,
        'stage_color': stage_color,
        'risk_class': risk_class,
        'interpretation': interpretation,
        'management': management,
        'scr_criteria': scr_criteria,
        'uo_criteria': uo_criteria,
        'scr_fold': scr_fold,
        'uo_6h_rate': uo_6h_rate,
        'uo_12h_rate': uo_12h_rate,
        'uo_24h_rate': uo_24h_rate
    }


def render():
    """Render KDIGO AKI calculator in Streamlit"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'kdigo':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'KDIGO')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("🧪 KDIGO Criteria - Acute Kidney Injury (AKI)")
    st.markdown("**Phân loại và đánh giá giai đoạn suy thận cấp**")
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **KDIGO (Kidney Disease: Improving Global Outcomes)** là tiêu chuẩn hiện đại nhất để:
        - Chẩn đoán Acute Kidney Injury (AKI)
        - Phân loại giai đoạn AKI (Stage 1, 2, 3)
        - Hướng dẫn quản lý và tiên lượng
        
        **AKI** là tình trạng giảm đột ngột chức năng thận:
        - Phổ biến: 10-15% bệnh nhân nhập viện, ~50% ICU
        - Tăng tử vong: 2-5× so với không AKI
        - Nguy cơ CKD dài hạn
        
        ### 🎯 Tiêu chí chẩn đoán AKI
        
        **AKI khi có MỘT trong các tiêu chí sau:**
        
        1. **Serum Creatinine:**
           - Tăng ≥0.3 mg/dL trong 48 giờ
           - HOẶC tăng ≥1.5× baseline trong 7 ngày
        
        2. **Nước tiểu:**
           - <0.5 mL/kg/h trong 6 giờ
        
        ### 📊 Giai Đoạn KDIGO
        
        | Stage | Serum Creatinine | Nước tiểu |
        |-------|------------------|-----------|
        | **1** | 1.5-1.9× baseline HOẶC ↑≥0.3 mg/dL | <0.5 mL/kg/h × 6-12h |
        | **2** | 2.0-2.9× baseline | <0.5 mL/kg/h × ≥12h |
        | **3** | ≥3× baseline HOẶC ≥4.0 mg/dL HOẶC RRT | <0.3 mL/kg/h × ≥24h HOẶC anuria ≥12h |
        
        ### ⚠️ Lưu ý quan trọng
        
        - **Baseline creatinine:** Sử dụng SCr thấp nhất trong 3 tháng trước
        - **Nếu không có baseline:** Ước tính từ MDRD (giả định GFR = 75 mL/min/1.73m²)
        - **Giai đoạn cuối cùng:** Lấy giai đoạn CAO NHẤT từ SCr hoặc nước tiểu
        - **RRT (Renal Replacement Therapy):** Dialysis = Stage 3 tự động
        
        ### 📚 Tài liệu tham khảo
        
        - KDIGO AKI Guideline 2012
        - Kellum JA, et al. *Crit Care* 2013;17:204
        """)
    
    st.divider()
    
    # Input section
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="kdigo",
            calculator_name="KDIGO",
            category="Thận",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    with col_main:
        st.subheader("📝 Nhập dữ liệu lâm sàng")
    
    # Creatinine section
    st.markdown("#### 🩺 Serum Creatinine")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        scr_baseline = st.number_input(
            "**SCr Baseline (mg/dL)**",
            min_value=0.0,
            max_value=20.0,
            value=1.0,
            step=0.1,
            format="%.1f",
            help="Creatinine cơ bản (trước khi bệnh). Nếu không biết, ước tính từ GFR = 75 mL/min"
        )
    
    with col2:
        scr_current = st.number_input(
            "**SCr Hiện tại (mg/dL)**",
            min_value=0.0,
            max_value=20.0,
            value=1.5,
            step=0.1,
            format="%.1f",
            help="Creatinine hiện tại của bệnh nhân"
        )
    
    with col3:
        scr_increase_48h = st.number_input(
            "**SCr Tăng trong 48h (mg/dL)**",
            min_value=0.0,
            max_value=10.0,
            value=0.0,
            step=0.1,
            format="%.1f",
            help="Mức tăng creatinine trong 48 giờ qua"
        )
    
    st.caption("💡 Chuyển đổi: μmol/L ÷ 88.4 = mg/dL")
    
    st.divider()
    
    # Urine output section
    st.markdown("#### 💧 Nước tiểu (Urine Output)")
    
    weight = st.number_input(
        "**Cân nặng (kg)**",
        min_value=0,
        max_value=300,
        value=70,
        step=1,
        format="%d",
        help="Cân nặng hiện tại của bệnh nhân"
    )
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        urine_output_6h = st.number_input(
            "**Tổng nước tiểu 6 giờ (mL)**",
            min_value=-1,
            max_value=5000,
            value=-1,
            step=10,
            format="%d",
            help="Tổng lượng nước tiểu trong 6 giờ. Nhập -1 nếu không đo"
        )
    
    with col5:
        urine_output_12h = st.number_input(
            "**Tổng nước tiểu 12 giờ (mL)**",
            min_value=-1,
            max_value=10000,
            value=-1,
            step=10,
            format="%d",
            help="Tổng lượng nước tiểu trong 12 giờ. Nhập -1 nếu không đo"
        )
    
    with col6:
        urine_output_24h = st.number_input(
            "**Tổng nước tiểu 24 giờ (mL)**",
            min_value=-1,
            max_value=20000,
            value=-1,
            step=10,
            format="%d",
            help="Tổng lượng nước tiểu trong 24 giờ. Nhập -1 nếu không đo"
        )
    
    st.divider()
    
    # RRT status
    on_rrt = st.checkbox(
        "**Bệnh nhân đang chạy thận nhân tạo (RRT/Dialysis)**",
        help="Nếu đang RRT → tự động Stage 3"
    )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Đánh giá KDIGO AKI Stage", type="primary", use_container_width=True):
        result = calculate_kdigo(
            scr_baseline=scr_baseline,
            scr_current=scr_current,
            scr_increase_48h=scr_increase_48h,
            urine_output_6h=urine_output_6h,
            urine_output_12h=urine_output_12h,
            urine_output_24h=urine_output_24h,
            weight=weight,
            on_rrt=on_rrt
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Stage box
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            if result['stage'] == 0:
                st.metric(
                    label="**Đánh giá**",
                    value="Không AKI"
                )
            else:
                st.metric(
                    label="**KDIGO Stage**",
                    value=f"Giai đoạn {result['stage']}"
                )
        
        with col_r2:
            st.markdown(f"### {result['stage_color']} {result['stage_text']}")
            if result['scr_fold'] > 0:
                st.caption(f"SCr: {scr_baseline:.2f} → {scr_current:.2f} mg/dL ({result['scr_fold']:.2f}×)")
        
        # Details
        with st.expander("📋 Chi tiết đánh giá", expanded=True):
            if result['scr_criteria']:
                st.markdown("**Tiêu chí Creatinine:**")
                for criterion in result['scr_criteria']:
                    st.markdown(f"- {criterion}")
            else:
                st.markdown("- ❌ Không đáp ứng tiêu chí creatinine")
            
            st.markdown("")
            
            if result['uo_criteria']:
                st.markdown("**Tiêu chí Nước tiểu:**")
                for criterion in result['uo_criteria']:
                    st.markdown(f"- {criterion}")
            else:
                if result['uo_6h_rate'] is None and result['uo_12h_rate'] is None and result['uo_24h_rate'] is None:
                    st.markdown("- ℹ️ Không có dữ liệu nước tiểu")
                else:
                    st.markdown("- ❌ Không đáp ứng tiêu chí nước tiểu")
        
        # Interpretation
        st.markdown("---")
        st.markdown(result['interpretation'])
        
        # Management
        st.markdown("---")
        st.markdown("### 💊 Xử trí & quản lý")
        st.markdown(result['management'])
        
        # Additional info
        if result['stage'] > 0:
            st.info("""
            **🔬 Xét nghiệm bổ sung khuyến cáo:**
            
            - **Phân biệt nguyên nhân:**
              * FENa / FEUrea (phân biệt tiền thận vs thận)
              * Urinalysis + urine microscopy (casts, cells, crystals)
              * Renal ultrasound (loại trừ tắc nghẽn)
            
            - **Đánh giá mức độ:**
              * Điện giải: Na, K, Cl, HCO3, Mg, PO4
              * ABG (nếu nghi acidosis)
              * CBC (thiếu máu, nhiễm trùng)
            
            - **Xem xét nếu cần:**
              * ANA, ANCA, anti-GBM (nếu nghi glomerulonephritis)
              * Complement C3, C4 (lupus nephritis, MPGN)
              * CPK (rhabdomyolysis)
              * Urine eosinophils (acute interstitial nephritis)
              * Renal biopsy (nếu nguyên nhân không rõ + không hồi phục)
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "SCr Baseline (mg/dL)": scr_baseline,
            "SCr Hiện tại (mg/dL)": scr_current,
            "SCr Tăng trong 48h (mg/dL)": scr_increase_48h,
            "Nước tiểu 6h (mL)": urine_output_6h if urine_output_6h >= 0 else None,
            "Nước tiểu 12h (mL)": urine_output_12h if urine_output_12h >= 0 else None,
            "Nước tiểu 24h (mL)": urine_output_24h if urine_output_24h >= 0 else None,
            "Cân nặng (kg)": weight,
            "Đang RRT": "Có" if on_rrt else "Không"
        }
        
        results_dict = {
            "KDIGO Stage": f"Stage {result['stage']}" if result['stage'] > 0 else "Không có AKI",
            "SCr fold increase": round(result['scr_fold'], 2) if result['scr_fold'] > 0 else None,
            "UO rate 6h (mL/kg/h)": round(result['uo_6h_rate'], 2) if result['uo_6h_rate'] else None,
            "UO rate 12h (mL/kg/h)": round(result['uo_12h_rate'], 2) if result['uo_12h_rate'] else None,
            "UO rate 24h (mL/kg/h)": round(result['uo_24h_rate'], 2) if result['uo_24h_rate'] else None
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="kdigo",
            calculator_name="KDIGO",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="kdigo",
            calculator_name="KDIGO",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="kdigo",
            calculator_name="KDIGO",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="kdigo", show_actions=True)
        
        # Save to session state
        st.session_state['kdigo_result'] = result
        
        # Warning
        st.warning("""
        ⚠️ **Lưu ý y khoa:**
        - KDIGO là hệ thống phân loại, không thay thế đánh giá lâm sàng
        - Điều trị then chốt: TÌM VÀ XỬ TRÍ NGUYÊN NHÂN (pre-renal/intrinsic/post-renal)
        - Stage 3 AKI: Tư vấn thận ngay, xem xét RRT
        - Quyết định điều trị cuối cùng thuộc về bác sĩ điều trị
        """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("KDIGO")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    
    # Quick reference
    with st.expander("📖 Bảng tham khảo Nhanh - Nguyên nhân AKI"):
        st.markdown("""
        ### Phân Loại Nguyên Nhân AKI
        
        #### 1. 🔽 Tiền thận (Pre-Renal) - 40-70%
        
        **Giảm thể tích:**
        - Mất dịch: Chảy máu, tiêu chảy, nôn, polyuria, bỏng
        - Giảm thể tích hiệu dụng: Suy tim, xơ gan, hội chứng thận hư
        
        **Giảm tưới máu thận:**
        - Thuốc giãn mạch: ACEI, ARB, NSAIDs
        - Shock: Septic, cardiogenic, hypovolemic
        - Hẹp động mạch thận
        
        **Chẩn đoán:** FENa <1%, BUN/Cr >20, đáp ứng với truyền dịch
        
        #### 2. 🔴 Thận (Intrinsic/Renal) - 25-40%
        
        **Acute Tubular Necrosis (ATN):**
        - Ischemic ATN: Kéo dài pre-renal, shock
        - Nephrotoxic ATN: Aminoglycosides, contrast, cisplatin, rhabdomyolysis
        
        **Acute Interstitial Nephritis (AIN):**
        - Thuốc: β-lactams, NSAIDs, PPIs, allopurinol
        - Nhiễm trùng: Pyelonephritis, viral
        - Tự miễn: Lupus, Sjögren
        
        **Glomerulonephritis:**
        - Rapidly progressive GN: ANCA vasculitis, anti-GBM, lupus
        - Post-infectious GN
        
        **Vascular:**
        - Renal artery thrombosis/embolism
        - Renal vein thrombosis
        - Atheroembolic disease (sau thủ thuật mạch máu)
        - TTP/HUS, DIC
        
        **Chẩn đoán:** FENa >2%, BUN/Cr <20, urine casts (muddy brown, RBC, WBC)
        
        #### 3. 🔼 Sau thận (Post-Renal) - 5-10%
        
        **Tắc nghẽn đường tiểu:**
        - Phì đại/ung thư tuyến tiền liệt tuyến
        - Ung thư bàng quang, cổ tử cung, đại trực tràng
        - Sỏi thận hai bên (hoặc sỏi ở thận đơn độc)
        - Xơ hóa sau phúc mạc
        - Nấm cầu (fungal ball), cục máu đông
        - Catheter bị tắc
        
        **Chẩn đoán:** Siêu âm thận (hydronephrosis), FENa có thể >1%
        
        ### 🔍 Các xét nghiệm giúp phân biệt
        
        | Xét nghiệm | Pre-Renal | ATN (Intrinsic) | Post-Renal |
        |------------|-----------|-----------------|------------|
        | FENa | <1% | >2% | >1% (thường) |
        | FEUrea | <35% | >50% | Không đặc hiệu |
        | BUN/Cr | >20:1 | <20:1 | >20:1 (ban đầu) |
        | Urine Na | <20 mEq/L | >40 mEq/L | Variable |
        | Urine Osm | >500 | <350 | Variable |
        | Urine sediment | Bình thường | Muddy brown casts | Bình thường |
        | Siêu âm | Bình thường | Bình thường | Hydronephrosis |
        
        **Lưu ý:** Nhiều trường hợp có nguyên nhân PHỐI HỢP (ví dụ: sepsis + nephrotoxin)
        """)

