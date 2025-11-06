"""
Aminoglycosides TDM Calculator
Therapeutic Drug Monitoring cho Amikacin, Gentamicin, Tobramycin, Netilmicin
Peak and Trough monitoring
"""

import streamlit as st
import math
from drugs.tdm.base_template import TDMCalculator
from drugs.tdm.tdm_config import TDM_DRUGS


def calculate_aminoglycoside_dose(
    drug_name,
    weight_kg,
    crcl,
    indication="standard",
    target_peak=None,
    target_trough=None
):
    """
    Calculate Aminoglycoside dose
    
    Args:
        drug_name: "amikacin", "gentamicin", "tobramycin", "netilmicin"
        weight_kg: Body weight
        crcl: Creatinine clearance
        indication: "standard", "severe", "pneumonia", "uti"
        target_peak: Target peak level
        target_trough: Target trough level
    
    Returns:
        dict with dosing information
    """
    # Drug-specific parameters
    drug_params = {
        "amikacin": {
            "peak_target": 20.0 if indication == "severe" else 15.0,
            "trough_target": 5.0,
            "loading_mg_kg": 7.5,
            "maintenance_mg_kg": 7.5
        },
        "gentamicin": {
            "peak_target": 8.0 if indication == "severe" else 5.0,
            "trough_target": 1.0,
            "loading_mg_kg": 2.0,
            "maintenance_mg_kg": 1.7
        },
        "tobramycin": {
            "peak_target": 8.0 if indication == "severe" else 5.0,
            "trough_target": 1.0,
            "loading_mg_kg": 2.0,
            "maintenance_mg_kg": 1.7
        },
        "netilmicin": {
            "peak_target": 8.0 if indication == "severe" else 5.0,
            "trough_target": 1.0,
            "loading_mg_kg": 2.0,
            "maintenance_mg_kg": 1.7
        }
    }
    
    params = drug_params.get(drug_name, drug_params["gentamicin"])
    
    # Loading dose
    loading_dose_mg = params["loading_mg_kg"] * weight_kg
    
    # Maintenance dose (daily)
    maintenance_dose_mg = params["maintenance_mg_kg"] * weight_kg
    
    # Adjust for renal function
    if crcl < 30:
        maintenance_dose_mg *= 0.5
        frequency = 48  # Q48h
    elif crcl < 50:
        maintenance_dose_mg *= 0.7
        frequency = 36  # Q36h
    elif crcl < 80:
        frequency = 24  # Q24h
    else:
        frequency = 12  # Q12h
    
    # Round to practical dosing
    if drug_name == "amikacin":
        practical_doses = [250, 500, 750, 1000]
    else:
        practical_doses = [40, 60, 80, 100, 120, 160, 200, 240]
    
    loading_rounded = min(practical_doses, key=lambda x: abs(x - loading_dose_mg))
    maintenance_rounded = min(practical_doses, key=lambda x: abs(x - maintenance_dose_mg))
    
    return {
        "loading_dose_mg": loading_rounded,
        "maintenance_dose_mg": maintenance_rounded,
        "frequency_hours": frequency,
        "target_peak": target_peak or params["peak_target"],
        "target_trough": target_trough or params["trough_target"],
        "dosing_interval": f"Q{frequency}h"
    }


def interpret_aminoglycoside_levels(drug_name, peak_mg_l, trough_mg_l):
    """
    Interpret Aminoglycoside levels
    
    Args:
        drug_name: Drug name
        peak_mg_l: Peak level (mg/L)
        trough_mg_l: Trough level (mg/L)
    
    Returns:
        dict with interpretation
    """
    # Get target ranges
    drug_info = TDM_DRUGS.get(drug_name, TDM_DRUGS["gentamicin"])
    target_min = drug_info["target_min"]
    target_max = drug_info["target_max"]
    trough_max = drug_info.get("trough_max", 1.0)
    
    results = []
    
    # Peak interpretation
    if peak_mg_l < target_min:
        peak_status = "subtherapeutic"
        peak_text = f"⬇️ Peak thấp (< {target_min} mg/L)"
        peak_rec = "Peak thấp. Cân nhắc tăng liều hoặc rút ngắn thời gian truyền."
        peak_color = "info"
    elif peak_mg_l <= target_max:
        peak_status = "therapeutic"
        peak_text = f"✅ Peak trong mục tiêu ({target_min}-{target_max} mg/L)"
        peak_rec = "Peak trong khoảng điều trị. Tiếp tục liều hiện tại."
        peak_color = "success"
    else:
        peak_status = "supratherapeutic"
        peak_text = f"⚠️ Peak cao (> {target_max} mg/L)"
        peak_rec = "Peak cao. Cân nhắc giảm liều hoặc kéo dài thời gian truyền."
        peak_color = "warning"
    
    results.append({
        "type": "peak",
        "value": peak_mg_l,
        "status": peak_status,
        "level_text": peak_text,
        "recommendation": peak_rec,
        "color": peak_color
    })
    
    # Trough interpretation (critical - must be low)
    if trough_mg_l <= trough_max:
        trough_status = "therapeutic"
        trough_text = f"✅ Trough an toàn (≤ {trough_max} mg/L)"
        trough_rec = "Trough trong giới hạn an toàn. Tiếp tục liều hiện tại."
        trough_color = "success"
    elif trough_mg_l <= trough_max * 2:
        trough_status = "supratherapeutic"
        trough_text = f"⚠️ Trough hơi cao ({trough_max}-{trough_max * 2} mg/L)"
        trough_rec = "Trough hơi cao. Nguy cơ tích lũy và độc tính. Giảm liều hoặc tăng khoảng cách liều."
        trough_color = "warning"
    else:
        trough_status = "toxic"
        trough_text = f"🚨 Trough quá cao (> {trough_max * 2} mg/L) - Nguy cơ độc tính"
        trough_rec = "Trough quá cao! Nguy cơ độc tính thận và ốc tai. Ngừng thuốc, đánh giá độc tính."
        trough_color = "error"
    
    results.append({
        "type": "trough",
        "value": trough_mg_l,
        "status": trough_status,
        "level_text": trough_text,
        "recommendation": trough_rec,
        "color": trough_color
    })
    
    return results


def render_aminoglycosides_tdm():
    """Render Aminoglycosides TDM Calculator Interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>💉 Aminoglycosides TDM Calculator</h2>
    <p style='text-align: center;'><em>Therapeutic Drug Monitoring - Peak & Trough Monitoring</em></p>
    """, unsafe_allow_html=True)
    
    # Drug selection
    drug_selection = st.selectbox(
        "Chọn thuốc:",
        ["Amikacin", "Gentamicin", "Tobramycin", "Netilmicin"],
        key="amino_drug"
    )
    
    drug_id = drug_selection.lower()
    drug_info = TDM_DRUGS.get(drug_id, TDM_DRUGS["gentamicin"])
    
    st.info(f"""
    **{drug_selection} TDM:**
    - **Peak:** {drug_info['therapeutic_range'].split(',')[0]}
    - **Trough:** {drug_info['therapeutic_range'].split(',')[1] if ',' in drug_info['therapeutic_range'] else 'N/A'}
    - **Thời điểm lấy mẫu:** {drug_info['sampling_time']}
    - **Half-life:** {drug_info.get('half_life_hours', 'N/A')} giờ
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2 = st.tabs(["🧮 Tính Liều", "📊 Giải Thích Nồng Độ"])
    
    with tab1:
        st.markdown("### 📋 Thông Số Bệnh Nhân")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key=f"{drug_id}_weight"
            )
            
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=5.0,
                max_value=150.0,
                value=60.0,
                step=5.0,
                format="%.1f",
                key=f"{drug_id}_crcl"
            )
        
        with col2:
            indication = st.selectbox(
                "Chỉ định:",
                ["Chuẩn", "Nhiễm khuẩn nặng", "Viêm phổi", "Nhiễm khuẩn tiết niệu"],
                key=f"{drug_id}_indication"
            )
            
            indication_map = {
                "Chuẩn": "standard",
                "Nhiễm khuẩn nặng": "severe",
                "Viêm phổi": "pneumonia",
                "Nhiễm khuẩn tiết niệu": "uti"
            }
            indication_code = indication_map[indication]
        
        st.markdown("---")
        
        if st.button(f"🧮 Tính Liều {drug_selection}", type="primary", use_container_width=True):
            result = calculate_aminoglycoside_dose(
                drug_id, weight, crcl, indication_code
            )
            
            st.markdown("### 💊 Kết Quả Tính Liều")
            
            st.markdown("#### 🔴 Loading Dose:")
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"**Loading dose:** {result['loading_dose_mg']:.0f} mg (một lần)")
            
            with col2:
                st.caption("""
                **Cách cho:**
                - Truyền tĩnh mạch trong 30-60 phút
                - Lấy mẫu peak: 30 phút sau khi truyền xong
                """)
            
            st.markdown("---")
            st.markdown("#### 📅 Maintenance Dose:")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều đề xuất",
                    f"{result['maintenance_dose_mg']:.0f} mg"
                )
            
            with col2:
                st.metric(
                    "Tần suất",
                    result['dosing_interval']
                )
            
            with col3:
                st.metric(
                    "Mục tiêu Peak",
                    f"{result['target_peak']:.1f} mg/L"
                )
            
            st.markdown("---")
            
            st.success(f"""
            **💊 Khuyến nghị:**
            
            **Loading:** {result['loading_dose_mg']:.0f} mg (một lần)
            **Maintenance:** {result['maintenance_dose_mg']:.0f} mg **{result['dosing_interval']}**
            
            **Lưu ý:**
            - Mục tiêu Peak: {result['target_peak']:.1f} mg/L
            - Mục tiêu Trough: ≤ {result['target_trough']:.1f} mg/L
            - Lấy mẫu peak: 30 phút sau khi truyền xong
            - Lấy mẫu trough: Trước liều tiếp theo
            - CrCl {crcl:.0f} mL/min: Dùng liều điều chỉnh cho suy thận
            """)
            
            st.markdown("---")
            st.markdown("### ⚠️ Cảnh Báo Độc Tính")
            
            st.error("""
            **Triệu chứng độc tính Aminoglycosides:**
            
            **Thận:**
            - Tăng creatinine
            - Giảm GFR
            - Protein niệu
            
            **Ốc tai:**
            - Mất thính lực (thường không hồi phục)
            - Ù tai
            - Chóng mặt
            
            **Yếu tố tăng nguy cơ:**
            - Trough cao (> 2 mg/L cho gentamicin/tobramycin, > 10 mg/L cho amikacin)
            - Dùng kéo dài (> 7-10 ngày)
            - Suy thận
            - Tuổi cao
            - Dùng đồng thời với thuốc độc thận khác
            """)
    
    with tab2:
        st.markdown("### 📊 Giải Thích Nồng Độ Aminoglycosides")
        
        col1, col2 = st.columns(2)
        
        with col1:
            peak = st.number_input(
                f"Peak {drug_selection} (mg/L)",
                min_value=0.0,
                max_value=50.0,
                value=(drug_info['target_min'] + drug_info['target_max']) / 2,
                step=0.5,
                key=f"{drug_id}_peak"
            )
            
            st.caption("Lấy mẫu: 30 phút sau khi truyền xong")
        
        with col2:
            trough = st.number_input(
                f"Trough {drug_selection} (mg/L)",
                min_value=0.0,
                max_value=10.0,
                value=drug_info.get('trough_max', 1.0),
                step=0.1,
                key=f"{drug_id}_trough"
            )
            
            st.caption("Lấy mẫu: Trước liều tiếp theo")
        
        st.markdown("---")
        
        if st.button("📊 Giải Thích Nồng Độ", type="primary", use_container_width=True):
            interpretations = interpret_aminoglycoside_levels(drug_id, peak, trough)
            
            st.markdown("### 📈 Kết Quả Giải Thích")
            
            for interp in interpretations:
                st.markdown(f"#### {interp['type'].upper()}: {interp['value']:.2f} mg/L")
                
                if interp['color'] == 'success':
                    st.success(f"**{interp['level_text']}**")
                elif interp['color'] == 'info':
                    st.info(f"**{interp['level_text']}**")
                elif interp['color'] == 'warning':
                    st.warning(f"**{interp['level_text']}**")
                else:
                    st.error(f"**{interp['level_text']}**")
                
                st.markdown(f"**💡 Khuyến nghị:** {interp['recommendation']}")
                st.markdown("---")
    
    # References
    st.markdown("---")
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown(f"""
        - **{drug_selection} TDM Guidelines**
        - **Peak target:** {drug_info['target_min']}-{drug_info['target_max']} mg/L
        - **Trough target:** < {drug_info.get('trough_max', 1.0)} mg/L
        - **Half-life:** {drug_info.get('half_life_hours', 'N/A')} giờ (normal renal function)
        - **Volume of distribution:** 0.2-0.3 L/kg
        - **Protein binding:** < 10%
        """)

