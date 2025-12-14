"""
Dosage Results Display
Hiển thị kết quả tính liều chi tiết
"""

import streamlit as st
import pandas as pd
from ..dosing_calculator import calculate_detailed_dose


def render_antibiotic_header(ab_name, ab_data):
    """Render antibiotic header card"""
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #0EA5E9 0%, #0288D1 100%); color: white; padding: 20px; border-radius: 15px; margin: 20px 0;'>
        <h2 style='margin: 0; color: white;'>💊 {ab_name}</h2>
        {f"<p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9);'>{ab_data.get('vietnamese_name', '')}</p>" if ab_data.get('vietnamese_name') else ""}
    </div>
    """, unsafe_allow_html=True)


def render_base_dose(result):
    """Render base dose section"""
    st.markdown("### 📊 Liều Chuẩn (Chức năng thận bình thường):")
    st.info(f"**{result['base_dose']}**")
    
    if result.get('notes'):
        st.caption(f"💡 {result['notes']}")


def render_renal_adjustment(result, crcl, renal_category):
    """Render renal adjustment section"""
    category_labels = {
        'normal': '✅ Bình thường (CrCl ≥ 60)',
        '30_60': '⚠️ Suy thận nhẹ-vừa (CrCl 30-59)',
        '15_30': '🔴 Suy thận nặng (CrCl 15-29)',
        'under_15': '🚨 Suy thận rất nặng (CrCl < 15)',
        'hemodialysis': '💉 Đang lọc máu ngắt quãng (HD)',
        'continuous_hd': '💉 Đang lọc máu liên tục (CRRT/CVVH)',
        'peritoneal_dialysis': '💉 Đang lọc màng bụng (PD)'
    }
    
    st.markdown("### 🫘 Điều Chỉnh Theo Chức Năng Thận:")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
        **CrCl hiện tại:** {crcl:.1f} mL/min
        
        **Phân loại:** {category_labels.get(renal_category, 'Chưa xác định')}
        """)
    
    with col2:
        st.success(f"""
        **Khuyến cáo điều chỉnh:**
        
        {result['adjustment']}
        """)


def render_renal_adjustment_table(result):
    """Render full renal adjustment table"""
    st.markdown("---")
    st.markdown("### 📋 Bảng Điều Chỉnh Đầy Đủ:")
    
    renal_guide = result.get('full_renal_guide', {})
    if renal_guide:
        renal_table = {
            "Chức năng thận": [],
            "CrCl (mL/min)": [],
            "Điều chỉnh liều": []
        }
        
        if 'normal' in renal_guide:
            renal_table["Chức năng thận"].append("Bình thường")
            renal_table["CrCl (mL/min)"].append("≥ 60")
            renal_table["Điều chỉnh liều"].append(renal_guide['normal'])
        
        if '30_60' in renal_guide:
            renal_table["Chức năng thận"].append("Suy thận nhẹ-vừa")
            renal_table["CrCl (mL/min)"].append("30-59")
            renal_table["Điều chỉnh liều"].append(renal_guide['30_60'])
        
        if '15_30' in renal_guide:
            renal_table["Chức năng thận"].append("Suy thận nặng")
            renal_table["CrCl (mL/min)"].append("15-29")
            renal_table["Điều chỉnh liều"].append(renal_guide['15_30'])
        
        if 'under_15' in renal_guide:
            renal_table["Chức năng thận"].append("Suy thận rất nặng")
            renal_table["CrCl (mL/min)"].append("< 15")
            renal_table["Điều chỉnh liều"].append(renal_guide['under_15'])
        
        if 'hemodialysis' in renal_guide:
            renal_table["Chức năng thận"].append("Lọc máu")
            renal_table["CrCl (mL/min)"].append("HD")
            renal_table["Điều chỉnh liều"].append(renal_guide['hemodialysis'])
        
        df_renal = pd.DataFrame(renal_table)
        st.dataframe(df_renal, use_container_width=True, hide_index=True)


def render_detailed_dose(selected_ab, weight, ibw, abw, crcl, indication_code, is_pediatric, height, is_obese, is_malnourished=False, age_years=None):
    """Render detailed dose calculation results"""
    st.markdown("---")
    st.markdown("### 💉 Tính liều chi tiết:")
    
    # Pediatric templates (Phase 5 - Task 5.2)
    if is_pediatric and age_years:
        from ..pediatric_templates import (
            get_pediatric_dosing_adjustment,
            format_pediatric_category,
            get_pediatric_warnings
        )
        
        ped_adjustment = get_pediatric_dosing_adjustment(age_years, weight)
        if ped_adjustment.get('is_pediatric'):
            category = ped_adjustment.get('category')
            st.info(f"""
            **👶 {format_pediatric_category(category)}**
            
            {ped_adjustment.get('notes', '')}
            """)
            
            # Show warnings
            warnings = get_pediatric_warnings(age_years, selected_ab)
            for warning in warnings:
                st.warning(warning)
    
    detailed_dose = calculate_detailed_dose(
        selected_ab, weight, ibw, abw, crcl, 
        indication=indication_code, 
        is_pediatric=is_pediatric,
        height_cm=height
    )
    
    if detailed_dose and detailed_dose.get('calculated_dose_mg'):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Liều tính được", f"{detailed_dose['calculated_dose_mg']:.0f} mg")
            if detailed_dose.get('parsed', {}).get('dose_per_kg'):
                dose_per_kg = detailed_dose['calculated_dose_mg'] / detailed_dose['dosing_weight_kg']
                st.caption(f"≈ {dose_per_kg:.1f} mg/kg")
        
        with col2:
            if detailed_dose.get('interval_hours'):
                st.metric("Khoảng cách", f"{detailed_dose['interval_hours']:.0f} giờ")
            else:
                st.metric("Khoảng cách", "Theo hướng dẫn")
        
        with col3:
            st.metric("Trọng lượng dùng", f"{detailed_dose['dosing_weight_kg']:.1f} kg")
            if is_obese:
                st.caption("ABW")
            elif is_malnourished:
                st.caption("Cân nhắc IBW")
        
        with col4:
            if detailed_dose.get('frequency'):
                st.metric("Tần suất", f"{detailed_dose['frequency']:.0f} lần/ngày")
            else:
                st.metric("Tần suất", "Theo interval")
        
        # Infusion details (if IV)
        if detailed_dose.get('infusion_details'):
            infusion = detailed_dose['infusion_details']
            st.markdown("---")
            st.markdown("#### 💉 Hướng dẫn pha & truyền (IV):")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f"""
                **Thể tích pha:**
                {infusion['volume_ml']:.0f} mL NS/D5W
                
                **Nồng độ:**
                {infusion['concentration_mg_ml']:.2f} mg/mL
                """)
            
            with col2:
                st.info(f"""
                **Thời gian truyền:**
                {infusion['infusion_time_minutes']:.0f} phút
                ({infusion['infusion_time_hours']:.1f} giờ)
                """)
            
            with col3:
                rate_ml_per_hour = infusion['volume_ml'] / infusion['infusion_time_hours']
                st.info(f"""
                **Tốc độ truyền:**
                {rate_ml_per_hour:.0f} mL/giờ
                ({rate_ml_per_hour/60:.1f} mL/phút)
                """)
        
        # Dosing schedule example
        if detailed_dose.get('interval_hours'):
            schedule_text = f"📅 **Lịch dùng:** {detailed_dose['calculated_dose_mg']:.0f} mg mỗi {detailed_dose['interval_hours']:.0f} giờ"
            if detailed_dose.get('infusion_details'):
                schedule_text += f" (truyền {detailed_dose['infusion_details']['infusion_time_minutes']:.0f} phút)"
            st.info(schedule_text)
    
    return detailed_dose


def render_icu_adjustments(result, is_icu, albumin_gdl):
    """Render ICU-specific adjustments"""
    if is_icu and result.get('icu_recommendations'):
        st.markdown("---")
        st.markdown("### 🏥 Điều Chỉnh Cho ICU:")
        
        col1, col2 = st.columns(2)
        with col1:
            if result.get('protein_binding', 0) > 0:
                st.metric("Liên kết protein", f"{result['protein_binding']:.0f}%")
            if albumin_gdl:
                st.metric("Albumin", f"{albumin_gdl:.1f} g/dL")
        
        with col2:
            if result.get('icu_factor', 1.0) > 1.0:
                st.metric("Hệ số điều chỉnh ICU", f"x {result['icu_factor']:.2f}")
        
        for rec in result['icu_recommendations']:
            if "🚨" in rec:
                st.error(rec)
            elif "⚠️" in rec:
                st.warning(rec)
            else:
                st.info(rec)


def render_special_population_guidance(is_hemodialysis, is_continuous_hd, is_peritoneal_dialysis, hd_schedule=None):
    """Render special population guidance (HD/PD/CRRT)"""
    if is_hemodialysis:
        st.markdown("---")
        st.markdown("### 💉 Hướng Dẫn Cho Bệnh Nhân Lọc Máu Ngắt Quãng:")
        
        if hd_schedule:
            hd_freq_text = f"Lịch HD: {hd_schedule}"
        else:
            hd_freq_text = "Lịch HD: 3 lần/tuần"
        
        st.warning(f"""
        **{hd_freq_text}**
        
        **Thời điểm cho thuốc:**
        - Cho thuốc **SAU** khi lọc máu (nếu có thể) để tránh bị lọc bỏ
        - Một số kháng sinh cần liều bổ sung **TRƯỚC** HD (ví dụ: Vancomycin)
        - Tra cứu hướng dẫn cụ thể cho từng kháng sinh
        
        **Lưu ý:**
        - CrCl trong HD ≈ 0, cần dùng liều cho suy thận rất nặng hoặc liều bổ sung
        - Monitor nồng độ thuốc nếu có thể
        """)
    
    if is_continuous_hd:
        st.markdown("---")
        st.markdown("### 💉 Hướng Dẫn Cho Bệnh Nhân Lọc Máu Liên Tục (CRRT/CVVH):")
        st.warning(f"""
        **CRRT/CVVH:**
        - Liều thường cao hơn HD ngắt quãng do thời gian lọc liên tục
        - Cần tính liều dựa trên clearance của CRRT
        - Một số kháng sinh cần tăng liều: Vancomycin, Piperacillin-Tazobactam
        - Tra cứu hướng dẫn cụ thể cho từng kháng sinh
        """)
    
    if is_peritoneal_dialysis:
        st.markdown("---")
        st.markdown("### 💉 Hướng Dẫn Cho Bệnh Nhân Lọc Màng Bụng (PD):")
        st.info(f"""
        **Lọc màng bụng:**
        - Một số kháng sinh có thể cho vào dịch lọc màng bụng (IP - intraperitoneal)
        - Cần điều chỉnh liều khác với HD ngắt quãng
        - Thường dùng liều cho suy thận nặng
        - Tra cứu hướng dẫn cụ thể cho từng kháng sinh
        """)


def render_side_effects(ab_data):
    """Render side effects reminder"""
    if ab_data.get('side_effects'):
        st.markdown("---")
        with st.expander("⚠️ Tác dụng phụ quan trọng"):
            for se in ab_data['side_effects'][:5]:  # Show top 5
                st.markdown(f"- {se}")


def render_monitoring(result):
    """Render monitoring section"""
    if result.get('monitoring'):
        st.markdown("---")
        st.warning(f"**📊 Theo dõi:** {result['monitoring']}")


def render_dosage_results(result, selected_ab, ab_data, crcl, renal_category, patient_data, indication_code):
    """Main function to render all dosage results"""
    # Render antibiotic header
    render_antibiotic_header(selected_ab, ab_data)
    
    # Base dose
    render_base_dose(result)
    st.markdown("---")
    
    # Renal adjustment
    render_renal_adjustment(result, crcl, renal_category)
    
    # Full renal adjustment table
    render_renal_adjustment_table(result)
    
    # Detailed dose calculation
    render_detailed_dose(
        selected_ab,
        patient_data['weight'],
        patient_data['ibw'],
        patient_data['abw'],
        crcl,
        indication_code,
        patient_data['is_pediatric'],
        patient_data['height'],
        patient_data['is_obese'],
        is_malnourished=False,
        age_years=patient_data.get('age', None)
    )
    
    # ICU adjustments
    render_icu_adjustments(result, patient_data['is_icu'], patient_data.get('albumin_gdl'))
    
    # Special population guidance
    render_special_population_guidance(
        patient_data['is_hemodialysis'],
        patient_data['is_continuous_hd'],
        patient_data['is_peritoneal_dialysis'],
        patient_data.get('hd_schedule')
    )
    
    # Monitoring
    render_monitoring(result)
    
    # Side effects
    render_side_effects(ab_data)
    
    # Link to full antibiotic info
    st.markdown("---")
    st.info("💡 **Xem thông tin đầy đủ:** Tra cứu kháng sinh này để xem chỉ định, chống chỉ định, tương tác thuốc chi tiết")

