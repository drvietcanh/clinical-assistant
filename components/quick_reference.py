"""
Quick Reference Tables UI Component
Quick lookup tables for common doses, preparations, and rates
"""

import streamlit as st
import json
from pathlib import Path
import pandas as pd
from drugs.cardiovascular_calculator import get_drug_names, get_drug_info


def _load_quick_reference_data() -> dict:
    """Load quick reference data from JSON file."""
    db_path = Path(__file__).parent.parent / "data" / "quick_reference_data.json"
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def render_quick_reference():
    """Render quick reference tables interface."""
    
    st.markdown("## 📋 Quick Reference Tables")
    st.markdown("""
    Bảng tra cứu nhanh cho liều thường dùng, nồng độ pha, và tốc độ truyền.
    
    **Tính năng:**
    - Bảng liều thường dùng
    - Bảng nồng độ pha chuẩn
    - Bảng tốc độ tham khảo
    - Drop factor reference
    """)
    
    st.markdown("---")
    
    # Load data
    ref_data = _load_quick_reference_data()
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "💊 Liều thường dùng",
        "🧪 Nồng độ pha chuẩn",
        "💧 Tốc độ tham khảo",
        "📊 Drop Factor"
    ])
    
    # Tab 1: Common Doses
    with tab1:
        st.markdown("### 💊 Liều thường dùng")
        st.caption("Bảng tra cứu nhanh liều dùng cho các thuốc tim mạch")
        
        common_doses = ref_data.get("common_doses", {})
        drug_names = get_drug_names()
        
        # Create table
        doses_data = []
        for drug in drug_names:
            if drug in common_doses:
                info = common_doses[drug]
                doses_data.append({
                    "Thuốc": drug,
                    "Liều thấp": info.get("low_dose", "N/A"),
                    "Liều trung bình": info.get("medium_dose", "N/A"),
                    "Liều cao": info.get("high_dose", "N/A"),
                    "Liều tối đa": info.get("max_dose", "N/A"),
                    "Công dụng": info.get("typical_use", "N/A")
                })
        
        if doses_data:
            df = pd.DataFrame(doses_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Printable version
            with st.expander("🖨️ Phiên bản in"):
                st.markdown(df.to_markdown(index=False))
        else:
            st.info("Đang tải dữ liệu...")
    
    # Tab 2: Standard Preparations
    with tab2:
        st.markdown("### 🧪 Nồng độ pha chuẩn")
        st.caption("Bảng tra cứu nhanh cách pha chuẩn cho các thuốc")
        
        preparations = ref_data.get("standard_preparations", {})
        
        # Method selection
        method = st.radio(
            "**Phương pháp:**",
            ["syringe_pump_50ml", "syringe_pump_20ml", "iv_bag_500ml"],
            format_func=lambda x: {
                "syringe_pump_50ml": "Bơm 50ml",
                "syringe_pump_20ml": "Bơm 20ml",
                "iv_bag_500ml": "Chai 500ml"
            }.get(x, x),
            horizontal=True,
            key="ref_prep_method"
        )
        
        # Create table
        prep_data = []
        for drug in get_drug_names():
            if drug in preparations:
                prep_info = preparations[drug]
                prep_data.append({
                    "Thuốc": drug,
                    "Cách pha": prep_info.get(method, "N/A")
                })
        
        if prep_data:
            df = pd.DataFrame(prep_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Printable version
            with st.expander("🖨️ Phiên bản in"):
                st.markdown(df.to_markdown(index=False))
        else:
            st.info("Đang tải dữ liệu...")
    
    # Tab 3: Typical Rates
    with tab3:
        st.markdown("### 💧 Tốc độ tham khảo")
        st.caption("Tốc độ truyền tham khảo cho bệnh nhân 70kg")
        
        typical_rates = ref_data.get("typical_rates", {})
        
        # Weight input
        weight_kg = st.number_input(
            "**Cân nặng (kg):**",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=1.0,
            format="%.0f",
            key="ref_weight"
        )
        
        # Calculate rates for selected weight
        if typical_rates:
            st.markdown(f"#### Tốc độ cho bệnh nhân {weight_kg:.0f}kg")
            
            for drug, rates in typical_rates.items():
                if "70kg_patient" in rates:
                    st.markdown(f"**{drug}:**")
                    for dose_key, rate_70kg in rates["70kg_patient"].items():
                        # Scale to actual weight
                        rate_value = float(rate_70kg.split()[0])
                        scaled_rate = rate_value * (weight_kg / 70)
                        dose_str = dose_key.replace("_", " ").replace("mcg kg min", "mcg/kg/min")
                        st.markdown(f"  - {dose_str}: {scaled_rate:.1f} ml/h")
                    st.markdown("---")
        else:
            st.info("Đang tải dữ liệu...")
    
    # Tab 4: Drop Factor
    with tab4:
        st.markdown("### 📊 Drop Factor Reference")
        st.caption("Tham khảo drop factor cho các loại dịch truyền")
        
        drop_ref = ref_data.get("drop_rate_reference", {})
        
        if drop_ref:
            drop_data = []
            for key, info in drop_ref.items():
                drop_data.append({
                    "Drop Factor": key.replace("_", " ").replace("gtt ml", "gtt/ml"),
                    "Mô tả": info.get("description", ""),
                    "Sử dụng": info.get("use", "")
                })
            
            df = pd.DataFrame(drop_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Additional info
            st.markdown("---")
            st.markdown("#### 💡 Công thức tính giọt/phút")
            st.code("""
Giọt/phút = (Tốc độ truyền ml/h × Drop factor) / 60

Ví dụ:
- Tốc độ: 60 ml/h
- Drop factor: 20 gtt/ml
- Giọt/phút = (60 × 20) / 60 = 20 gtt/min
            """)
        else:
            st.info("Đang tải dữ liệu...")
    
    # Conversion factors
    with st.expander("🔄 Công thức chuyển đổi"):
        st.markdown("""
        **Chuyển đổi đơn vị:**
        - 1 mg = 1000 mcg
        - 1 mcg = 0.001 mg
        
        **Chuyển đổi liều:**
        - Từ mcg/kg/min → mg/h:
          ```
          mg/h = (mcg/kg/min × kg × 60) / 1000
          ```
        
        **Chuyển đổi tốc độ:**
        - Từ ml/h → giọt/phút:
          ```
          gtt/min = (ml/h × drop_factor) / 60
          ```
        
        **Chuyển đổi liều → tốc độ:**
        - Từ mcg/kg/min → ml/h:
          ```
          ml/h = (mcg/kg/min × kg × 60) / (concentration_mg/ml × 1000)
          ```
        """)

