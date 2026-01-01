"""
eGFR/GFR Calculator - Comprehensive
Tính tốc độ lọc cầu thận với nhiều công thức và tính BSA
Chuẩn hóa và tuyệt đối GFR
"""

import streamlit as st
from config.theme import COLORS

from .egfr_bsa import (
    calculate_bsa_mosteller,
    calculate_bsa_dubois,
    calculate_bsa_haycock,
    calculate_bsa_boyd,
    calculate_bsa_shuter_aslani
)
from .egfr_calculators import (
    calculate_ckd_epi,
    calculate_mdrd,
    calculate_cockcroft_gault
)
from .egfr_helpers import (
    convert_egfr_to_absolute_gfr,
    interpret_egfr,
    get_recommended_formula
)
from .egfr_ui_input import render_input_form
from .egfr_ui_results import render_results_display
from .egfr_ui_help import (
    render_overview_expander,
    render_calculation_details,
    render_formula_guide,
    render_example,
    render_ckd_stages_table,
    render_bsa_comparison,
    render_references,
    render_detailed_explanations,
    render_summary_info
)
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# =====================================

def render():
    """Render comprehensive eGFR/GFR calculator"""
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🧪 eGFR/GFR Calculator</h2>
    <p style='text-align: center;'><em>Tính tốc độ lọc cầu thận với nhiều công thức</em></p>
    """, unsafe_allow_html=True)
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "egfr":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'eGFR/GFR Calculator')}")
    
    # Overview expander
    render_overview_expander()
    
    st.markdown("---")
    
    # Input form
    inputs = render_input_form()
    
    # Calculate button
    if st.button("🔬 Tính tất cả", type="primary", use_container_width=True):
        # Calculate BSA using selected formula
        bsa_formulas = {
            "mosteller": calculate_bsa_mosteller,
            "dubois": calculate_bsa_dubois,
            "haycock": calculate_bsa_haycock,
            "boyd": calculate_bsa_boyd,
            "shuter_aslani": calculate_bsa_shuter_aslani
        }
        bsa = bsa_formulas[inputs["bsa_formula"]](inputs["weight_kg"], inputs["height_cm"])
        
        # Also calculate with other formulas for comparison
        bsa_mosteller = calculate_bsa_mosteller(inputs["weight_kg"], inputs["height_cm"])
        bsa_dubois = calculate_bsa_dubois(inputs["weight_kg"], inputs["height_cm"])
        bsa_haycock = calculate_bsa_haycock(inputs["weight_kg"], inputs["height_cm"])
        bsa_boyd = calculate_bsa_boyd(inputs["weight_kg"], inputs["height_cm"])
        bsa_shuter = calculate_bsa_shuter_aslani(inputs["weight_kg"], inputs["height_cm"])
        
        # Calculate all GFR formulas
        egfr_ckd_epi = calculate_ckd_epi(inputs["creatinine_mg"], inputs["age"], inputs["gender"], inputs["race"])
        egfr_mdrd = calculate_mdrd(inputs["creatinine_mg"], inputs["age"], inputs["gender"], inputs["race"])
        crcl = calculate_cockcroft_gault(
            inputs["age"], 
            inputs["weight_kg"], 
            inputs["creatinine_mg"], 
            inputs["gender"], 
            inputs["use_abw"], 
            inputs["abw"]
        )
        
        # Calculate absolute GFRs (for drug dosing)
        gfr_absolute_ckd_epi = convert_egfr_to_absolute_gfr(egfr_ckd_epi, bsa)
        gfr_absolute_mdrd = convert_egfr_to_absolute_gfr(egfr_mdrd, bsa)
        
        # Interpret CKD stage
        interpretation = interpret_egfr(egfr_ckd_epi)
        
        # Get recommended formula
        recommended, reason = get_recommended_formula(inputs["bmi"], inputs["age"], "normal")
        
        # Display results
        dosing_gfr = render_results_display(
            inputs["age"], inputs["gender"], inputs["height_cm"], inputs["weight_kg"],
            inputs["race"], inputs["creatinine_unit"], inputs["creatinine"], inputs["creatinine_mg"],
            inputs["use_abw"], inputs["abw"], inputs["bmi"], inputs["bsa_formula"],
            bsa, bsa_mosteller, bsa_dubois, bsa_haycock, bsa_boyd, bsa_shuter,
            egfr_ckd_epi, egfr_mdrd, crcl, gfr_absolute_ckd_epi, gfr_absolute_mdrd,
            interpretation, recommended, reason
        )
        
        inputs_dict = {
            "Age": inputs["age"],
            "Gender": inputs["gender"],
            "Height (cm)": inputs["height_cm"],
            "Weight (kg)": inputs["weight_kg"],
            "Creatinine (mg/dL)": inputs["creatinine_mg"],
            "Race": inputs["race"],
            "Use ABW": inputs["use_abw"],
            "ABW": inputs["abw"],
            "BSA Formula": inputs["bsa_formula"]
        }
        results_dict = {
            "eGFR CKD-EPI": round(egfr_ckd_epi, 1),
            "eGFR MDRD": round(egfr_mdrd, 1),
            "CrCl": round(crcl, 1),
            "Absolute GFR (CKD-EPI)": round(gfr_absolute_ckd_epi, 1)
        }
        
        # Export section
        render_export_section(
            title=f"eGFR CKD-EPI = {egfr_ckd_epi:.1f} mL/min/1.73m²",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="eGFR/GFR Calculator"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="egfr",
            calculator_name="eGFR/GFR Calculator",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="egfr",
            calculator_name="eGFR/GFR Calculator",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        render_suggestions(
            calculator_id="egfr",
            calculator_name="eGFR/GFR Calculator",
            category="Thận",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="egfr", show_actions=True)
        
        # Help expanders
        render_calculation_details(
            inputs["weight_kg"], inputs["height_cm"], inputs["age"],
            inputs["creatinine_mg"], inputs["creatinine_unit"], inputs["creatinine"],
            inputs["use_abw"], inputs["abw"], bsa, egfr_ckd_epi, egfr_mdrd, crcl, gfr_absolute_ckd_epi
        )
        render_formula_guide()
        render_example(
            inputs["age"], inputs["height_cm"], inputs["weight_kg"],
            inputs["creatinine"], inputs["creatinine_unit"], inputs["creatinine_mg"],
            bsa, egfr_ckd_epi, interpretation, gfr_absolute_ckd_epi, dosing_gfr
        )
        render_ckd_stages_table()
        render_bsa_comparison(bsa_mosteller, bsa_dubois, bsa_haycock, bsa_boyd, bsa_shuter, bsa)
        render_references()
    
    # Always show these expanders
    render_detailed_explanations()
    render_summary_info()
    
    references = get_references("eGFR")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()
