"""
Electrolyte Calculator UI Component
Calculate and adjust electrolyte concentrations in IV fluids
"""

import streamlit as st
from critical_care.electrolyte_calculator import (
    calculate_electrolyte_addition,
    calculate_potassium_addition,
    calculate_calcium_addition,
    calculate_osmolarity,
    calculate_final_concentration
)
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert


def render_electrolyte_calculator():
    """Render electrolyte calculator interface."""
    
    st.markdown("## ⚡ Electrolyte Calculator")
    st.markdown("""
    Tính toán và điều chỉnh nồng độ điện giải trong dịch truyền.
    
    **Tính năng:**
    - Tính lượng Na+, K+, Ca++ cần thêm
    - Tính áp lực thẩm thấu (osmolarity)
    - Tính nồng độ cuối khi trộn dịch
    """)
    
    st.markdown("---")
    
    # Tabs for different calculations
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🧂 Na+ (Sodium)",
        "⚡ K+ (Potassium)",
        "🦴 Ca++ (Calcium)",
        "💧 Osmolarity",
        "🔄 Mixing Calculator"
    ])
    
    # Tab 1: Sodium
    with tab1:
        st.markdown("### 🧂 Điều chỉnh Na+ (Sodium)")
        st.caption("Tính lượng NaCl cần thêm để đạt nồng độ Na+ mong muốn")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            volume_ml = st.number_input(
                "**Thể tích dịch (ml):**",
                min_value=1.0,
                max_value=10000.0,
                value=500.0,
                step=10.0,
                format="%.0f",
                key="na_volume"
            )
        
        with col2:
            current_na = st.number_input(
                "**Na+ hiện tại (mmol/L):**",
                min_value=0.0,
                max_value=200.0,
                value=0.0,
                step=1.0,
                format="%.1f",
                key="na_current"
            )
        
        with col3:
            target_na = st.number_input(
                "**Na+ mong muốn (mmol/L):**",
                min_value=0.0,
                max_value=200.0,
                value=140.0,
                step=1.0,
                format="%.1f",
                key="na_target"
            )
        
        if st.button("🧮 Tính toán", key="na_calculate", type="primary"):
            try:
                result = calculate_electrolyte_addition(volume_ml, current_na, target_na)
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                if result["na_deficit_mmol"] > 0:
                    metrics = [
                        {
                            "label": "Thiếu Na+",
                            "value": f"{result['na_deficit_mmol']:.1f} mmol",
                            "icon": "🧂"
                        },
                        {
                            "label": "3% NaCl",
                            "value": f"{result['nacl_3_percent_ml']:.1f} ml",
                            "icon": "💧"
                        },
                        {
                            "label": "0.9% NaCl",
                            "value": f"{result['nacl_0_9_percent_ml']:.1f} ml",
                            "icon": "💧"
                        }
                    ]
                    
                    render_result_card("Lượng NaCl cần thêm", metrics, color="primary")
                    
                    if result["nacl_10_percent_ml"] > 0:
                        st.markdown("---")
                        render_warning_alert(
                            f"10% NaCl: {result['nacl_10_percent_ml']:.1f} ml",
                            title="⚠️ Lưu ý: 10% NaCl là dung dịch ưu trương"
                        )
                    
                    # Recommendations
                    st.markdown("---")
                    st.markdown("### 💡 Khuyến nghị")
                    for rec in result["recommendations"]:
                        st.markdown(f"  • {rec}")
                else:
                    render_info_alert("Không cần thêm Na+", title="✅")
                    
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 2: Potassium
    with tab2:
        st.markdown("### ⚡ Điều chỉnh K+ (Potassium)")
        st.caption("Tính lượng KCl cần thêm để đạt nồng độ K+ mong muốn")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            volume_ml = st.number_input(
                "**Thể tích dịch (ml):**",
                min_value=1.0,
                max_value=10000.0,
                value=500.0,
                step=10.0,
                format="%.0f",
                key="k_volume"
            )
        
        with col2:
            current_k = st.number_input(
                "**K+ hiện tại (mmol/L):**",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=0.5,
                format="%.1f",
                key="k_current"
            )
        
        with col3:
            target_k = st.number_input(
                "**K+ mong muốn (mmol/L):**",
                min_value=0.0,
                max_value=100.0,
                value=20.0,
                step=0.5,
                format="%.1f",
                key="k_target"
            )
        
        if st.button("🧮 Tính toán", key="k_calculate", type="primary"):
            try:
                result = calculate_potassium_addition(volume_ml, current_k, target_k)
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                if result["k_deficit_mmol"] > 0:
                    metrics = [
                        {
                            "label": "Thiếu K+",
                            "value": f"{result['k_deficit_mmol']:.1f} mmol",
                            "icon": "⚡"
                        },
                        {
                            "label": "10% KCl",
                            "value": f"{result['kcl_10_percent_ml']:.1f} ml",
                            "icon": "💧"
                        },
                        {
                            "label": "15% KCl",
                            "value": f"{result['kcl_15_percent_ml']:.1f} ml",
                            "icon": "💧"
                        }
                    ]
                    
                    render_result_card("Lượng KCl cần thêm", metrics, color="primary")
                    
                    # Recommendations
                    st.markdown("---")
                    st.markdown("### 💡 Khuyến nghị")
                    for rec in result["recommendations"]:
                        if "⚠️" in rec:
                            render_warning_alert(rec.replace("⚠️ ", ""), title="⚠️ Cảnh báo")
                        else:
                            st.markdown(f"  • {rec}")
                else:
                    render_info_alert("Không cần thêm K+", title="✅")
                    
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 3: Calcium
    with tab3:
        st.markdown("### 🦴 Điều chỉnh Ca++ (Calcium)")
        st.caption("Tính lượng Ca++ cần thêm để đạt nồng độ Ca++ mong muốn")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            volume_ml = st.number_input(
                "**Thể tích dịch (ml):**",
                min_value=1.0,
                max_value=10000.0,
                value=500.0,
                step=10.0,
                format="%.0f",
                key="ca_volume"
            )
        
        with col2:
            current_ca = st.number_input(
                "**Ca++ hiện tại (mmol/L):**",
                min_value=0.0,
                max_value=50.0,
                value=0.0,
                step=0.5,
                format="%.1f",
                key="ca_current"
            )
        
        with col3:
            target_ca = st.number_input(
                "**Ca++ mong muốn (mmol/L):**",
                min_value=0.0,
                max_value=50.0,
                value=2.5,
                step=0.5,
                format="%.1f",
                key="ca_target"
            )
        
        if st.button("🧮 Tính toán", key="ca_calculate", type="primary"):
            try:
                result = calculate_calcium_addition(volume_ml, current_ca, target_ca)
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                if result["ca_deficit_mmol"] > 0:
                    metrics = [
                        {
                            "label": "Thiếu Ca++",
                            "value": f"{result['ca_deficit_mmol']:.1f} mmol",
                            "icon": "🦴"
                        },
                        {
                            "label": "10% CaCl2",
                            "value": f"{result['cacl2_10_percent_ml']:.1f} ml",
                            "icon": "💧"
                        },
                        {
                            "label": "10% Ca gluconate",
                            "value": f"{result['cagluconate_10_percent_ml']:.1f} ml",
                            "icon": "💧"
                        }
                    ]
                    
                    render_result_card("Lượng Ca++ cần thêm", metrics, color="primary")
                    
                    # Recommendations
                    st.markdown("---")
                    st.markdown("### 💡 Khuyến nghị")
                    for rec in result["recommendations"]:
                        if "⚠️" in rec:
                            render_warning_alert(rec.replace("⚠️ ", ""), title="⚠️ Cảnh báo")
                        else:
                            st.markdown(f"  • {rec}")
                else:
                    render_info_alert("Không cần thêm Ca++", title="✅")
                    
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 4: Osmolarity
    with tab4:
        st.markdown("### 💧 Tính áp lực thẩm thấu (Osmolarity)")
        st.caption("Tính osmolarity của dung dịch")
        
        col1, col2 = st.columns(2)
        
        with col1:
            na_mmol_l = st.number_input(
                "**Na+ (mmol/L):**",
                min_value=0.0,
                max_value=200.0,
                value=140.0,
                step=1.0,
                format="%.1f",
                key="osm_na"
            )
            
            glucose_mmol_l = st.number_input(
                "**Glucose (mmol/L):**",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=1.0,
                format="%.1f",
                key="osm_glucose"
            )
            
            bun_mmol_l = st.number_input(
                "**BUN (mmol/L):**",
                min_value=0.0,
                max_value=50.0,
                value=0.0,
                step=0.5,
                format="%.1f",
                key="osm_bun"
            )
        
        with col2:
            k_mmol_l = st.number_input(
                "**K+ (mmol/L):**",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=0.5,
                format="%.1f",
                key="osm_k"
            )
            
            ca_mmol_l = st.number_input(
                "**Ca++ (mmol/L):**",
                min_value=0.0,
                max_value=50.0,
                value=0.0,
                step=0.5,
                format="%.1f",
                key="osm_ca"
            )
        
        if st.button("🧮 Tính toán", key="osm_calculate", type="primary"):
            try:
                result = calculate_osmolarity(na_mmol_l, glucose_mmol_l, bun_mmol_l, k_mmol_l, ca_mmol_l)
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                color = "success" if result["is_isotonic"] else ("warning" if result["osmolarity_mosm_l"] < 280 else "error")
                
                render_result_box(
                    "Osmolarity",
                    f"{result['osmolarity_mosm_l']:.1f} mOsm/L",
                    color=color,
                    icon="💧"
                )
                
                st.markdown("---")
                st.markdown(f"**Phân loại:** {result['classification']}")
                render_info_alert(result['notes'], title="ℹ️")
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 5: Mixing Calculator
    with tab5:
        st.markdown("### 🔄 Tính nồng độ cuối khi trộn dịch")
        st.caption("Tính nồng độ cuối cùng khi trộn hai dung dịch")
        
        st.markdown("#### Dung dịch 1")
        col1, col2 = st.columns(2)
        
        with col1:
            vol1 = st.number_input(
                "**Thể tích (ml):**",
                min_value=1.0,
                max_value=10000.0,
                value=250.0,
                step=10.0,
                format="%.0f",
                key="mix_vol1"
            )
        
        with col2:
            conc1 = st.number_input(
                "**Nồng độ (mmol/L):**",
                min_value=0.0,
                max_value=500.0,
                value=154.0,
                step=1.0,
                format="%.1f",
                key="mix_conc1"
            )
        
        st.markdown("#### Dung dịch 2")
        col3, col4 = st.columns(2)
        
        with col3:
            vol2 = st.number_input(
                "**Thể tích (ml):**",
                min_value=1.0,
                max_value=10000.0,
                value=250.0,
                step=10.0,
                format="%.0f",
                key="mix_vol2"
            )
        
        with col4:
            conc2 = st.number_input(
                "**Nồng độ (mmol/L):**",
                min_value=0.0,
                max_value=500.0,
                value=0.0,
                step=1.0,
                format="%.1f",
                key="mix_conc2"
            )
        
        if st.button("🧮 Tính toán", key="mix_calculate", type="primary"):
            try:
                final_conc = calculate_final_concentration(vol1, conc1, vol2, conc2)
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                total_vol = vol1 + vol2
                
                metrics = [
                    {
                        "label": "Tổng thể tích",
                        "value": f"{total_vol:.0f} ml",
                        "icon": "💧"
                    },
                    {
                        "label": "Nồng độ cuối",
                        "value": f"{final_conc:.1f} mmol/L",
                        "icon": "🧪"
                    }
                ]
                
                render_result_card("Kết quả trộn", metrics, color="primary")
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Reference values
    with st.expander("📋 Giá trị tham khảo"):
        st.markdown("""
        **Nồng độ bình thường trong máu:**
        - Na+: 135-145 mmol/L
        - K+: 3.5-5.0 mmol/L
        - Ca++: 2.1-2.6 mmol/L
        
        **Nồng độ trong dịch truyền thường dùng:**
        - 0.9% NaCl: 154 mmol/L Na+
        - 3% NaCl: 513 mmol/L Na+
        - 10% NaCl: 1713 mmol/L Na+
        - 10% KCl: 1342 mmol/L K+
        - 15% KCl: 2013 mmol/L K+
        - 10% CaCl2: 680 mmol/L Ca++
        - 10% Ca gluconate: 225 mmol/L Ca++
        
        **Osmolarity:**
        - Isotonic: 280-310 mOsm/L
        - Hypotonic: < 280 mOsm/L
        - Hypertonic: > 310 mOsm/L
        """)

