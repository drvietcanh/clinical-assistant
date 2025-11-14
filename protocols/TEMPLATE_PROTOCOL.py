"""
[Protocol Name] Protocol
[Guideline Source] [Year]
[Brief Description]

Template file for creating new protocols
Copy this file and modify for your new protocol
"""

import streamlit as st


def render():
    """
    [Protocol Name] Protocol
    
    Main render function - this is what gets called from the main page
    """
    # Header
    st.subheader("🦠 [Protocol Name] Protocol")
    st.caption("[Guideline Source] [Year] - [Brief Description]")
    
    # Overview/Key Points
    st.info("""
    **Key Points:**
    - Point 1: Important information
    - Point 2: Critical consideration
    - Point 3: Key warning
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Diagnostic Criteria")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Chẩn đoán [Condition] khi có:**
        1. Criterion 1
        2. Criterion 2
        3. Criterion 3
        
        **Phân loại mức độ:**
        - **Nhẹ:** Criteria...
        - **Trung bình:** Criteria...
        - **Nặng:** Criteria...
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: RISK STRATIFICATION ==========
    st.markdown("### 📊 Risk Stratification")
    
    # Example: Risk calculator or scoring system
    risk_score = st.number_input(
        "Risk Score:",
        min_value=0,
        max_value=100,
        value=0,
        help="Enter risk score if applicable"
    )
    
    if risk_score > 0:
        if risk_score < 30:
            st.success("✅ **Nguy cơ thấp** - Có thể điều trị ngoại trú")
        elif risk_score < 70:
            st.warning("⚠️ **Nguy cơ trung bình** - Cần theo dõi sát")
        else:
            st.error("🚨 **Nguy cơ cao** - Cần nhập viện/ICU")
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ALGORITHM ==========
    st.markdown("### 💊 Treatment Algorithm")
    
    # Treatment selection
    severity = st.radio(
        "**Mức độ:**",
        ["Nhẹ", "Trung bình", "Nặng"],
        key="protocol_severity"
    )
    
    st.markdown("---")
    
    # Display treatment based on severity
    if severity == "Nhẹ":
        render_mild_protocol()
    elif severity == "Trung bình":
        render_moderate_protocol()
    else:
        render_severe_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 4: DOSING INFORMATION ==========
    st.markdown("### 💉 Dosing Information")
    
    with st.expander("📋 Xem liều thuốc", expanded=False):
        # Example dosing table
        dosing_data = {
            "Thuốc": ["Drug 1", "Drug 2", "Drug 3"],
            "Liều": ["Dose 1", "Dose 2", "Dose 3"],
            "Đường dùng": ["IV", "PO", "IV"],
            "Ghi chú": ["Note 1", "Note 2", "Note 3"]
        }
        
        import pandas as pd
        st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Monitoring")
    
    st.markdown("""
    **Cần theo dõi:**
    - Parameter 1: Frequency
    - Parameter 2: Frequency
    - Parameter 3: Frequency
    
    **Dấu hiệu cảnh báo:**
    - ⚠️ Warning sign 1
    - ⚠️ Warning sign 2
    - 🚨 Emergency sign
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Consideration 1
        - Consideration 2
        
        **Suy thận:**
        - Adjustment needed
        """)
    
    with col2:
        st.markdown("""
        **Có thai:**
        - Safety consideration
        - Alternative if needed
        
        **Trẻ em:**
        - Pediatric dosing
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: REFERENCES ==========
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **[Primary Guideline]** - [Organization] [Year]
       - Link: [URL if available]
    
    2. **[Supporting Study]** - [Authors] [Year]
       - DOI: [DOI if available]
    
    3. **UpToDate:** [Topic Name] - Last updated [Date]
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_protocol():
    """Mild severity protocol"""
    st.success("## ⚠️ MILD [CONDITION] PROTOCOL")
    
    st.markdown("""
    **Initial Management:**
    1. Step 1
    2. Step 2
    3. Step 3
    
    **Treatment:**
    - Drug 1: Dose
    - Drug 2: Dose
    
    **Follow-up:**
    - When to reassess
    - When to escalate
    """)


def render_moderate_protocol():
    """Moderate severity protocol"""
    st.warning("## 🚨 MODERATE [CONDITION] PROTOCOL")
    
    st.markdown("""
    **Initial Management:**
    1. Step 1
    2. Step 2
    3. Step 3
    
    **Treatment:**
    - Drug 1: Dose
    - Drug 2: Dose
    
    **Monitoring:**
    - Frequency
    - Parameters
    """)


def render_severe_protocol():
    """Severe severity protocol"""
    st.error("## 🚨🚨 SEVERE [CONDITION] PROTOCOL - ICU")
    
    st.markdown("""
    **Immediate Actions:**
    1. Critical step 1
    2. Critical step 2
    3. Critical step 3
    
    **Treatment:**
    - Drug 1: High dose
    - Drug 2: Loading dose
    
    **ICU Monitoring:**
    - Continuous monitoring
    - Frequent labs
    - Consider consultation
    """)


# Example: If you need helper functions
def calculate_dose(weight: float, severity: str) -> dict:
    """
    Calculate dosing based on weight and severity
    
    Args:
        weight: Patient weight in kg
        severity: Severity level (mild/moderate/severe)
    
    Returns:
        dict with dosing information
    """
    # Example calculation
    base_dose = 10  # mg/kg
    
    if severity == "severe":
        multiplier = 1.5
    elif severity == "moderate":
        multiplier = 1.2
    else:
        multiplier = 1.0
    
    total_dose = weight * base_dose * multiplier
    
    return {
        "dose_mg": total_dose,
        "dose_per_kg": base_dose * multiplier,
        "frequency": "q8h" if severity == "severe" else "q12h"
    }

