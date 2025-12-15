"""
Pediatric Dosing Calculator
Weight-based, BSA-based, and age-based dosing for children
"""

import streamlit as st
from typing import Dict, Optional, Tuple
from scores.metabolism.bmi_ibw_bsa import (
    calculate_bsa_mosteller,
    calculate_bsa_dubois
)


def calculate_weight_based_dose(
    weight_kg: float,
    dose_per_kg: float,
    max_dose: Optional[float] = None,
    min_dose: Optional[float] = None
) -> Dict:
    """
    Calculate weight-based dose
    
    Args:
        weight_kg: Weight in kg
        dose_per_kg: Dose per kg (mg/kg, mcg/kg, etc.)
        max_dose: Maximum dose (optional)
        min_dose: Minimum dose (optional)
    
    Returns:
        Dictionary with calculated dose and information
    """
    calculated_dose = weight_kg * dose_per_kg
    
    # Apply min/max constraints
    if min_dose is not None and calculated_dose <= min_dose:
        calculated_dose = min_dose
        adjusted = True
        reason = f"Áp dụng liều tối thiểu: {min_dose}"
    elif max_dose is not None and calculated_dose >= max_dose:
        calculated_dose = max_dose
        adjusted = True
        reason = f"Áp dụng liều tối đa: {max_dose}"
    else:
        adjusted = False
        reason = None
    
    return {
        "calculated_dose": calculated_dose,
        "weight_kg": weight_kg,
        "dose_per_kg": dose_per_kg,
        "max_dose": max_dose,
        "min_dose": min_dose,
        "adjusted": adjusted,
        "reason": reason
    }


def calculate_bsa_based_dose(
    weight_kg: float,
    height_cm: float,
    dose_per_m2: float,
    max_dose: Optional[float] = None
) -> Dict:
    """
    Calculate BSA-based dose
    
    Args:
        weight_kg: Weight in kg
        height_cm: Height in cm
        dose_per_m2: Dose per m²
        max_dose: Maximum dose (optional)
    
    Returns:
        Dictionary with calculated dose and information
    """
    # Calculate BSA using Mosteller formula
    bsa = calculate_bsa_mosteller(weight_kg, height_cm)
    
    calculated_dose = bsa * dose_per_m2
    
    # Apply max constraint
    if max_dose and calculated_dose > max_dose:
        calculated_dose = max_dose
        adjusted = True
        reason = f"Áp dụng liều tối đa: {max_dose}"
    else:
        adjusted = False
        reason = None
    
    return {
        "calculated_dose": calculated_dose,
        "bsa": bsa,
        "dose_per_m2": dose_per_m2,
        "max_dose": max_dose,
        "adjusted": adjusted,
        "reason": reason
    }


def calculate_age_based_dose(
    age_years: float,
    age_dose_map: Dict[Tuple[float, float], float],
    max_dose: Optional[float] = None
) -> Dict:
    """
    Calculate age-based dose
    
    Args:
        age_years: Age in years
        age_dose_map: Dictionary mapping (min_age, max_age) tuples to doses
        max_dose: Maximum dose (optional)
    
    Returns:
        Dictionary with calculated dose and information
    """
    # Find appropriate age range
    calculated_dose = None
    age_range = None
    
    for (min_age, max_age), dose in age_dose_map.items():
        if min_age <= age_years < max_age:
            calculated_dose = dose
            age_range = (min_age, max_age)
            break
    
    if calculated_dose is None:
        return {
            "calculated_dose": None,
            "error": f"Không có liều cho tuổi {age_years} tuổi"
        }
    
    # Apply max constraint
    if max_dose and calculated_dose > max_dose:
        calculated_dose = max_dose
        adjusted = True
        reason = f"Áp dụng liều tối đa: {max_dose}"
    else:
        adjusted = False
        reason = None
    
    return {
        "calculated_dose": calculated_dose,
        "age_years": age_years,
        "age_range": age_range,
        "max_dose": max_dose,
        "adjusted": adjusted,
        "reason": reason
    }


def get_pediatric_dosing_guidelines(drug_name: str) -> Optional[Dict]:
    """
    Get pediatric dosing guidelines for common drugs
    
    Args:
        drug_name: Name of the drug
    
    Returns:
        Dictionary with dosing guidelines or None
    """
    # Common pediatric dosing guidelines
    guidelines = {
        "Paracetamol": {
            "weight_based": {
                "dose_per_kg": 15,  # mg/kg
                "unit": "mg/kg",
                "frequency": "q4-6h",
                "max_dose_per_dose": 1000,  # mg
                "max_dose_per_day": 4000,  # mg/day
                "notes": "Không quá 4-5 lần/ngày"
            },
            "age_based": {
                "0-3 months": "10-15 mg/kg q4-6h",
                "3-12 months": "10-15 mg/kg q4-6h",
                "1-2 years": "120-240 mg q4-6h",
                "2-6 years": "240-360 mg q4-6h",
                "6-12 years": "360-500 mg q4-6h",
                ">12 years": "500-1000 mg q4-6h"
            }
        },
        "Ibuprofen": {
            "weight_based": {
                "dose_per_kg": 10,  # mg/kg
                "unit": "mg/kg",
                "frequency": "q6-8h",
                "max_dose_per_dose": 400,  # mg
                "max_dose_per_day": 40,  # mg/kg/day
                "notes": "Không dùng cho trẻ <6 tháng"
            }
        },
        "Amoxicillin": {
            "weight_based": {
                "dose_per_kg": 50,  # mg/kg/day
                "unit": "mg/kg/day",
                "frequency": "q8h hoặc q12h",
                "max_dose_per_day": 2000,  # mg/day
                "notes": "Chia 2-3 lần/ngày"
            }
        },
        "Amoxicillin-Clavulanate": {
            "weight_based": {
                "dose_per_kg": 45,  # mg/kg/day (amoxicillin component)
                "unit": "mg/kg/day",
                "frequency": "q12h",
                "max_dose_per_day": 2000,  # mg/day
                "notes": "Dựa trên amoxicillin component"
            }
        },
        "Azithromycin": {
            "weight_based": {
                "dose_per_kg": 10,  # mg/kg/day
                "unit": "mg/kg/day",
                "frequency": "q24h",
                "max_dose_per_day": 500,  # mg/day
                "notes": "Liều đầu tiên có thể gấp đôi"
            }
        },
        "Ceftriaxone": {
            "weight_based": {
                "dose_per_kg": 50,  # mg/kg/day
                "unit": "mg/kg/day",
                "frequency": "q12h hoặc q24h",
                "max_dose_per_day": 2000,  # mg/day
                "notes": "Có thể dùng q12h hoặc q24h"
            }
        },
        "Vancomycin": {
            "weight_based": {
                "dose_per_kg": 15,  # mg/kg/dose
                "unit": "mg/kg/dose",
                "frequency": "q6h",
                "max_dose_per_dose": 1000,  # mg
                "notes": "Cần TDM. Điều chỉnh theo CrCl nếu suy thận."
            }
        },
        "Gentamicin": {
            "weight_based": {
                "dose_per_kg": 7.5,  # mg/kg/dose
                "unit": "mg/kg/dose",
                "frequency": "q8h",
                "max_dose_per_dose": 240,  # mg
                "notes": "Cần TDM. Điều chỉnh theo CrCl."
            }
        },
    }
    
    return guidelines.get(drug_name)


def render_pediatric_dosing_calculator() -> None:
    """
    Render pediatric dosing calculator interface
    """
    st.subheader("👶 Pediatric Dosing Calculator")
    st.caption("Tính liều thuốc cho trẻ em")
    
    # Method selection
    method = st.radio(
        "Phương pháp tính liều:",
        ["Weight-based (mg/kg)", "BSA-based (mg/m²)", "Age-based", "Drug-specific Guidelines"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if method == "Weight-based (mg/kg)":
        st.markdown("### 📊 Weight-based Dosing")
        
        col1, col2 = st.columns(2)
        with col1:
            weight_kg = st.number_input(
                "Cân nặng (kg)",
                min_value=0.1,
                max_value=100.0,
                value=20.0,
                step=0.1,
                format="%.1f"
            )
        
        with col2:
            dose_per_kg = st.number_input(
                "Liều (mg/kg hoặc mcg/kg)",
                min_value=0.0,
                max_value=1000.0,
                value=10.0,
                step=0.1,
                format="%.2f"
            )
        
        col3, col4 = st.columns(2)
        with col3:
            max_dose = st.number_input(
                "Liều tối đa (optional)",
                min_value=0.0,
                value=0.0,
                step=1.0,
                format="%.0f",
                help="Để 0 nếu không giới hạn"
            )
            if max_dose == 0:
                max_dose = None
        
        with col4:
            min_dose = st.number_input(
                "Liều tối thiểu (optional)",
                min_value=0.0,
                value=0.0,
                step=1.0,
                format="%.0f",
                help="Để 0 nếu không giới hạn"
            )
            if min_dose == 0:
                min_dose = None
        
        if st.button("🧮 Tính liều", type="primary"):
            result = calculate_weight_based_dose(
                weight_kg=weight_kg,
                dose_per_kg=dose_per_kg,
                max_dose=max_dose,
                min_dose=min_dose
            )
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Liều tính được", f"{result['calculated_dose']:.2f} mg")
            with col2:
                st.metric("Cân nặng", f"{weight_kg:.1f} kg")
            
            st.markdown(f"**Liều:** {dose_per_kg:.2f} mg/kg × {weight_kg:.1f} kg = **{result['calculated_dose']:.2f} mg**")
            
            if result['adjusted']:
                st.warning(f"⚠️ {result['reason']}")
            
            if max_dose:
                st.info(f"💡 Liều tối đa: {max_dose} mg")
            if min_dose:
                st.info(f"💡 Liều tối thiểu: {min_dose} mg")
    
    elif method == "BSA-based (mg/m²)":
        st.markdown("### 📊 BSA-based Dosing")
        
        col1, col2 = st.columns(2)
        with col1:
            weight_kg = st.number_input(
                "Cân nặng (kg)",
                min_value=0.1,
                max_value=100.0,
                value=20.0,
                step=0.1,
                format="%.1f"
            )
        
        with col2:
            height_cm = st.number_input(
                "Chiều cao (cm)",
                min_value=10.0,
                max_value=200.0,
                value=100.0,
                step=0.5,
                format="%.1f"
            )
        
        dose_per_m2 = st.number_input(
            "Liều (mg/m²)",
            min_value=0.0,
            max_value=10000.0,
            value=100.0,
            step=1.0,
            format="%.0f"
        )
        
        max_dose = st.number_input(
            "Liều tối đa (optional)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            format="%.0f",
            help="Để 0 nếu không giới hạn"
        )
        if max_dose == 0:
            max_dose = None
        
        if st.button("🧮 Tính liều", type="primary"):
            result = calculate_bsa_based_dose(
                weight_kg=weight_kg,
                height_cm=height_cm,
                dose_per_m2=dose_per_m2,
                max_dose=max_dose
            )
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("BSA", f"{result['bsa']:.2f} m²")
            with col2:
                st.metric("Liều tính được", f"{result['calculated_dose']:.2f} mg")
            with col3:
                st.metric("Liều/m²", f"{dose_per_m2:.0f} mg/m²")
            
            st.markdown(f"**Liều:** {dose_per_m2:.0f} mg/m² × {result['bsa']:.2f} m² = **{result['calculated_dose']:.2f} mg**")
            
            if result['adjusted']:
                st.warning(f"⚠️ {result['reason']}")
    
    elif method == "Age-based":
        st.markdown("### 📊 Age-based Dosing")
        st.info("💡 Age-based dosing thường dùng cho một số thuốc đặc biệt. Vui lòng tham khảo guidelines cụ thể.")
        
        age_years = st.number_input(
            "Tuổi (năm)",
            min_value=0.0,
            max_value=18.0,
            value=5.0,
            step=0.5,
            format="%.1f"
        )
        
        st.markdown("**Ví dụ:** Paracetamol theo tuổi")
        st.markdown("""
        - 0-3 tháng: 10-15 mg/kg q4-6h
        - 3-12 tháng: 10-15 mg/kg q4-6h
        - 1-2 tuổi: 120-240 mg q4-6h
        - 2-6 tuổi: 240-360 mg q4-6h
        - 6-12 tuổi: 360-500 mg q4-6h
        - >12 tuổi: 500-1000 mg q4-6h
        """)
    
    elif method == "Drug-specific Guidelines":
        st.markdown("### 📊 Drug-specific Guidelines")
        
        # Common pediatric drugs
        common_drugs = [
            "Paracetamol",
            "Ibuprofen",
            "Amoxicillin",
            "Amoxicillin-Clavulanate",
            "Azithromycin",
            "Ceftriaxone",
            "Vancomycin",
            "Gentamicin"
        ]
        
        selected_drug = st.selectbox(
            "Chọn thuốc:",
            common_drugs
        )
        
        guidelines = get_pediatric_dosing_guidelines(selected_drug)
        
        if guidelines:
            st.markdown(f"#### 💊 {selected_drug}")
            
            # Weight-based guidelines
            if "weight_based" in guidelines:
                wb = guidelines["weight_based"]
                st.markdown("**Weight-based dosing:**")
                st.markdown(f"- Liều: **{wb['dose_per_kg']:.0f} {wb['unit']}**")
                st.markdown(f"- Tần suất: **{wb['frequency']}**")
                
                if "max_dose_per_dose" in wb:
                    st.markdown(f"- Liều tối đa mỗi lần: **{wb['max_dose_per_dose']:.0f} mg**")
                if "max_dose_per_day" in wb:
                    st.markdown(f"- Liều tối đa mỗi ngày: **{wb['max_dose_per_day']:.0f} mg/ngày**")
                
                if "notes" in wb:
                    st.info(f"💡 {wb['notes']}")
                
                # Interactive calculator
                st.markdown("---")
                st.markdown("**Tính liều:**")
                
                weight_kg = st.number_input(
                    "Cân nặng (kg)",
                    min_value=0.1,
                    max_value=100.0,
                    value=20.0,
                    step=0.1,
                    format="%.1f",
                    key=f"weight_{selected_drug}"
                )
                
                if st.button("🧮 Tính liều", key=f"calc_{selected_drug}"):
                    result = calculate_weight_based_dose(
                        weight_kg=weight_kg,
                        dose_per_kg=wb['dose_per_kg'],
                        max_dose=wb.get('max_dose_per_dose'),
                        min_dose=None
                    )
                    
                    st.success(f"**Liều tính được: {result['calculated_dose']:.2f} mg**")
                    
                    if result['adjusted']:
                        st.warning(f"⚠️ {result['reason']}")
            
            # Age-based guidelines
            if "age_based" in guidelines:
                st.markdown("**Age-based dosing:**")
                for age_range, dose in guidelines["age_based"].items():
                    st.markdown(f"- **{age_range}:** {dose}")
        else:
            st.info(f"Chưa có guidelines cho {selected_drug}. Đang cập nhật...")
    
    # Warning
    st.markdown("---")
    st.warning("""
    ⚠️ **Lưu ý quan trọng:**
    - Liều tính được chỉ mang tính tham khảo
    - Luôn kiểm tra lại với guidelines và tài liệu tham khảo
    - Điều chỉnh liều theo chức năng thận, gan nếu cần
    - Một số thuốc cần TDM (Therapeutic Drug Monitoring)
    - Cân nhắc tương tác thuốc và chống chỉ định
    """)

