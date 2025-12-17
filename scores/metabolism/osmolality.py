"""
Serum Osmolality Calculator
Tính độ thẩm thấu huyết thanh và osmolal gap
"""

import streamlit as st
from scores.utils.validation import validate_lab_value
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# =====================================


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def render():
    """Render Osmolality Calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🧪 Serum Osmolality Calculator</h2>
    <p style='text-align: center;'><em>Tính độ thẩm thấu huyết thanh & Osmolal Gap</em></p>
    """, unsafe_allow_html=True)
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "osmolality":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Serum Osmolality')}")
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **Serum Osmolality** đo nồng độ các chất hòa tan trong huyết thanh.
        
        **Công thức tính (mOsm/kg):**
        - **Công thức chuẩn:** 2 × Na + Glucose/18 + BUN/2.8
        - **Đơn giản hóa:** 2 × Na + Glucose + Urea (nếu dùng mmol/L)
        
        **Osmolal Gap = Đo trực tiếp - Tính toán**
        
        **Ý nghĩa:**
        - **Gap bình thường:** < 10 mOsm/kg
        - **Gap tăng:** Nghi ngờ chất độc (methanol, ethylene glycol, ethanol...)
        
        **Khi nào dùng:**
        - Đánh giá rối loạn Na
        - Nghi ngờ ngộ độc (methanol, ethylene glycol...)
        - Đánh giá toan chuyển hóa
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập số liệu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        na = st.number_input(
            "Sodium - Na (mmol/L)",
            min_value=100.0,
            max_value=180.0,
            value=140.0,
            step=1.0,
            format="%.1f",
            help="Bình thường: 135-145 mmol/L"
        )
        
        glucose_unit = st.radio(
            "Đơn vị Glucose",
            options=["mmol/L", "mg/dL"],
            index=0,
            horizontal=True
        )
        
        if glucose_unit == "mmol/L":
            glucose_mmol = st.number_input(
                "Glucose (mmol/L)",
                min_value=0.0,
                max_value=50.0,
                value=5.0,
                step=0.1,
                format="%.1f",
                help="Bình thường: 3.9-6.1 mmol/L"
            )
            glucose_mg = glucose_mmol * 18
            st.caption(f"= {round(glucose_mg)} mg/dL")
        else:
            glucose_mg = st.number_input(
                "Glucose (mg/dL)",
                min_value=0.0,
                max_value=900.0,
                value=90.0,
                step=5.0,
                format="%.0f",
                help="Bình thường: 70-110 mg/dL"
            )
            glucose_mmol = glucose_mg / 18
            st.caption(f"= {_format_num(glucose_mmol, 1)} mmol/L")
    
    with col2:
        bun_unit = st.radio(
            "Đơn vị BUN/Urea",
            options=["mmol/L (Urea)", "mg/dL (BUN)"],
            index=0,
            horizontal=True
        )
        
        if bun_unit == "mmol/L (Urea)":
            urea_mmol = st.number_input(
                "Urea (mmol/L)",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=0.5,
                format="%.1f",
                help="Bình thường: 2.5-7.1 mmol/L"
            )
            bun_mg = urea_mmol * 2.8
            st.caption(f"= {_format_num(bun_mg, 1)} mg/dL BUN")
        else:
            bun_mg = st.number_input(
                "BUN (mg/dL)",
                min_value=0.0,
                max_value=300.0,
                value=14.0,
                step=1.0,
                format="%.0f",
                help="Bình thường: 7-20 mg/dL"
            )
            urea_mmol = bun_mg / 2.8
            st.caption(f"= {_format_num(urea_mmol, 1)} mmol/L Urea")
    
    # Measured osmolality (optional)
    st.markdown("---")
    measured_available = st.checkbox(
        "Có kết quả đo trực tiếp Osmolality (để tính Osmolal Gap)",
        help="Nếu có kết quả đo từ máy osmometer"
    )
    
    if measured_available:
        measured_osm = st.number_input(
            "Osmolality đo trực tiếp (mOsm/kg)",
            min_value=200.0,
            max_value=500.0,
            value=290.0,
            step=1.0,
            help="Bình thường: 275-295 mOsm/kg"
        )
    else:
        measured_osm = None
    
    st.markdown("---")
    
    if st.button("🔬 Tính Osmolality", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_na, na_error = validate_lab_value(na, "Sodium (mmol/L)", 100.0, 180.0)
        if not is_valid_na:
            validation_errors.append(na_error)
        
        if glucose_unit == "mmol/L":
            is_valid_glucose, glucose_error = validate_lab_value(glucose_mmol, "Glucose (mmol/L)", 0.0, 50.0)
        else:
            is_valid_glucose, glucose_error = validate_lab_value(glucose_mg, "Glucose (mg/dL)", 0.0, 900.0)
        if not is_valid_glucose:
            validation_errors.append(glucose_error)
        
        if bun_unit == "mmol/L (Urea)":
            is_valid_bun, bun_error = validate_lab_value(urea_mmol, "Urea (mmol/L)", 0.0, 100.0)
        else:
            is_valid_bun, bun_error = validate_lab_value(bun_mg, "BUN (mg/dL)", 0.0, 300.0)
        if not is_valid_bun:
            validation_errors.append(bun_error)
        
        if measured_available and measured_osm is not None:
            from scores.utils.validation import validate_range
            is_valid_osm, osm_error = validate_range(measured_osm, 200.0, 500.0, "Measured Osmolality (mOsm/kg)")
            if not is_valid_osm:
                validation_errors.append(osm_error)
        
        if validation_errors:
            render_validation_errors(validation_errors)
        
        # Calculate osmolality
        calc_osm = 2 * na + glucose_mg/18 + bun_mg/2.8
        
        st.markdown("## 📊 Kết quả")
        
        # Calculated osmolality
        if calc_osm < 275:
            osm_status = "Thấp"
            osm_color = "warning"
            osm_icon = "⚠️"
        elif calc_osm <= 295:
            osm_status = "Bình thường"
            osm_color = "success"
            osm_icon = "✅"
        else:
            osm_status = "Cao"
            osm_color = "error"
            osm_icon = "🚨"
        
        # Use render_result_box for calculated osmolality
        render_result_box(
            title="Calculated Osmolality",
            value=f"{calc_osm:.1f} mOsm/kg",
            subtitle=osm_status,
            color=osm_color,
            icon=osm_icon,
            size="large"
        )
        
        # Chi tiết
        st.markdown("### 📋 Thành phần:")
        st.markdown(f"""
        - **2 × Na:** 2 × {na} = {2*na:.0f}
        - **Glucose/18:** {glucose_mg:.0f}/18 = {glucose_mg/18:.1f}
        - **BUN/2.8:** {bun_mg:.0f}/2.8 = {bun_mg/2.8:.1f}
        
        **Tổng:** {calc_osm:.1f} mOsm/kg
        """)
        
        # Osmolal gap if measured available
        if measured_available:
            osm_gap = measured_osm - calc_osm
            
            st.markdown("---")
            
            if osm_gap < 10:
                gap_status = "Bình thường"
                gap_color = "success"
                gap_icon = "✅"
            elif osm_gap < 20:
                gap_status = "Tăng nhẹ"
                gap_color = "warning"
                gap_icon = "⚠️"
            else:
                gap_status = "Tăng rõ rệt"
                gap_color = "error"
                gap_icon = "🚨"
            
            # Use render_result_box for osmolal gap
            render_result_box(
                title="Osmolal Gap",
                value=f"{osm_gap:.1f} mOsm/kg",
                subtitle=gap_status,
                color=gap_color,
                icon=gap_icon,
                size="large"
            )
            
            st.markdown(f"""
            **Tính toán:**
            - Đo trực tiếp: {measured_osm:.1f}
            - Tính toán: {calc_osm:.1f}
            - **Gap = {measured_osm:.1f} - {calc_osm:.1f} = {osm_gap:.1f}**
            """)
            
            if osm_gap >= 10:
                st.error("""
                **🚨 OSMOLAL GAP TĂNG - Nghi ngờ chất độc!**
                
                **Nguyên nhân Osmolal Gap tăng (nhớ: ME DIE):**
                
                - **M**ethanol (ngộ độc cồn công nghiệp)
                - **E**thanol (rượu)
                - **D**iethylene glycol / Propylene glycol
                - **I**sopropanol (cồn y tế)
                - **E**thylene glycol (chất chống đông)
                
                **Khác:**
                - Mannitol
                - Glycerol
                - Acetone (DKA)
                - Suy thận nặng
                
                ---
                
                **XỬ TRÍ KHẨN:**
                
                1️⃣ **Xác định chất độc:**
                - **Anion gap metabolic acidosis + Osmolal gap tăng:**
                  - → Nghi ngờ **Methanol** hoặc **Ethylene glycol**
                - **Không acidosis nhưng gap tăng:**
                  - → Nghi ngờ **Ethanol** hoặc **Isopropanol**
                
                2️⃣ **Xét nghiệm:**
                - Methanol level
                - Ethylene glycol level
                - Lactic acid
                - Ketones
                - Anion gap
                - Xét nghiệm nước tiểu (oxalate crystals trong ethylene glycol)
                
                3️⃣ **Điều trị ngộ độc Methanol/Ethylene glycol:**
                
                **A. Fomepizole (Ưu tiên #1):**
                - Loading: 15 mg/kg IV
                - Maintenance: 10 mg/kg q12h × 4 liều, sau đó 15 mg/kg q12h
                - Tiếp tục cho đến methanol/EG < 20 mg/dL
                
                **B. Ethanol (nếu không có Fomepizole):**
                - Loading: 0.6 g/kg (= 7.6 mL/kg ethanol 10%) IV
                - Maintenance: 100-150 mg/kg/h
                - Mục tiêu: Ethanol level 100-150 mg/dL
                
                **C. Lọc máu:**
                - Chỉ định:
                  - Methanol > 50 mg/dL hoặc Ethylene glycol > 50 mg/dL
                  - Suy thận
                  - Toan chuyển hóa nặng (pH < 7.25)
                  - Bất thường điện giải nặng
                  - Rối loạn thị giác (methanol)
                
                **D. Điều chỉnh acidosis:**
                - Sodium bicarbonate nếu pH < 7.3
                - Mục tiêu pH > 7.3
                
                **E. Folinic acid (methanol):**
                - 50 mg IV q4h × 6 liều
                - Tăng chuyển hóa formic acid
                
                **F. Thiamine + Pyridoxine (ethylene glycol):**
                - Giúp chuyển hóa glyoxylic acid → glycine
                """)
            else:
                st.success("""
                **✅ Osmolal Gap bình thường**
                
                - Không có bằng chứng chất độc osmotically active
                - Nếu vẫn nghi ngờ ngộ độc → Xét nghiệm trực tiếp methanol, ethylene glycol
                """)
        
        # Phase 1: history + share + suggestions
        inputs_dict = {
            "Na (mmol/L)": na,
            "Glucose (mg/dL)": glucose_mg,
            "BUN (mg/dL)": bun_mg,
            "Measured Osmolality": measured_osm if measured_available else None
        }
        results_dict = {
            "Calculated Osmolality": round(calc_osm, 1),
            "Osmolal Gap": round(osm_gap, 1) if measured_available else None,
            "Gap Status": gap_status if measured_available else "N/A"
        }
        
        # Export section
        render_export_section(
                title="Serum Osmolality",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="Serum Osmolality"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="osmolality",
            calculator_name="Serum Osmolality",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="osmolality",
            calculator_name="Serum Osmolality",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        render_suggestions(
            calculator_id="osmolality",
            calculator_name="Serum Osmolality",
            category="Nội Tiết",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="osmolality", show_actions=True)
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Giải thích:")
        
        if calc_osm < 275:
            st.warning("""
            **Hypo-osmolality (Osmolality thấp)**
            
            **Nguyên nhân:**
            - **Hạ Na máu** (phổ biến nhất)
            - SIADH
            - Suy thận
            - Suy tim, xơ gan
            - Uống nước quá nhiều
            - Thiazide diuretics
            
            **Xử trí:** Tùy nguyên nhân gây hạ Na
            """)
        
        elif calc_osm > 295:
            st.warning("""
            **Hyper-osmolality (Osmolality cao)**
            
            **Nguyên nhân:**
            - **Tăng Na máu:**
                - Mất nước (tiêu chảy, lợi tiểu, sốt)
                - Thiểu năng ADH (diabetes insipidus)
                - Uống NaCl
            
            - **Tăng đường huyết:**
                - Đái tháo đường
                - DKA, HHS
            
            - **Tăng BUN:**
                - Suy thận
                - Chảy máu tiêu hóa
                - Catabolism tăng
            
            - **Chất độc:**
                - Methanol, ethylene glycol
                - Ethanol, isopropanol
            
            **Xử trí:** Tùy nguyên nhân
            """)
        
        else:
            st.success("""
            **✅ Osmolality bình thường (275-295 mOsm/kg)**
            
            Cân bằng nước và điện giải bình thường.
            """)
        
        # Clinical uses
        with st.expander("📚 Ứng dụng lâm sàng"):
            st.markdown("""
            ### 1. Đánh giá Hạ Na máu:
            
            **Bước 1:** Đo Serum Osmolality
            
            - **< 275 (hypo-osmolar):** Hạ Na máu thật
              - Đo Urine Osm
              - Đánh giá thể tích
            
            - **275-295 (iso-osmolar):** Pseudo-hyponatremia
              - Lipid cao
              - Protein cao
            
            - **> 295 (hyper-osmolar):** Chuyển dịch nước
              - Đường huyết cao
              - Mannitol
            
            ---
            
            ### 2. Nghi ngờ ngộ độc:
            
            **Tính Osmolal Gap:**
            
            - **Gap < 10:** Bình thường
            - **Gap ≥ 10:** Nghi ngờ chất độc
            
            **Kết hợp Anion Gap:**
            
            - **AG tăng + Osm gap tăng:**
              - Methanol
              - Ethylene glycol
            
            - **AG bình thường + Osm gap tăng:**
              - Ethanol
              - Isopropanol
            
            ---
            
            ### 3. Ước tính nồng độ Ethanol:
            
            **Công thức:**
            - Ethanol (mg/dL) = Osmolal Gap × 4.6
            
            **Ví dụ:**
            - Gap = 20 → Ethanol ≈ 92 mg/dL
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Purssell RA, Lynd LD, Koga Y.** The use of the osmole gap as a screening test for the presence of exogenous substances. 
               *Toxicol Rev.* 2004;23(3):189-202.
            
            2. **Kraut JA, Kurtz I.** Toxic alcohol ingestions: clinical features, diagnosis, and management. 
               *Clin J Am Soc Nephrol.* 2008;3(1):208-25.
            
            3. **Lepeytre F, Ghannoum M, Ammann H, Madore F, Troyanov S.** Ethylene glycol poisoning: A rare but life-threatening cause of metabolic acidosis-A single-centre experience. 
               *Nephrology (Carlton).* 2017;22(4):312-316.
            """)
    
    references = get_references("Osmolality")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Công thức:** 2 × Na + Glucose/18 + BUN/2.8
    
    2. **Osmolal Gap = Đo - Tính**
    
    3. **Gap ≥ 10:** Nghi ngờ chất độc (Methanol, Ethylene glycol, Ethanol...)
    
    4. **Gap tăng + Anion gap tăng:** Methanol hoặc Ethylene glycol → CẤP CỨU!
    
    5. **Điều trị:** Fomepizole + Lọc máu
    """)


if __name__ == "__main__":
    render()

