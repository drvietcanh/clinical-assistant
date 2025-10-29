"""
Module Kháng Sinh - Tính Liều, Điều Chỉnh Thận, TDM
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Kháng Sinh - Clinical Assistant", page_icon="💊", layout="wide")

# ========== HEADER ==========
st.title("💊 Kháng Sinh - Tính Liều & TDM")
st.markdown("Hướng dẫn liều dùng, điều chỉnh thận, theo dõi nồng độ thuốc")
st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Công Cụ")
    
    function_type = st.selectbox(
        "Công cụ:",
        [
            "🧮 Tính CrCl (Cockcroft-Gault)",
            "💉 Vancomycin - Tính Liều",
            "🔍 Tra Cứu Kháng Sinh",
            "💊 Aminoglycoside - Tính Liều",
            "📊 Cơ Sở Dữ Liệu"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ khoa học:**
    - FDA Drug Labels (Mỹ)
    - IDSA/ATS Guidelines
    - ASHP/IDSA TDM 2020
    - WHO AWaRe Classification
    """)

# ========== MAIN CONTENT ==========

# ===== CrCl Calculator =====
if "CrCl" in function_type:
    st.subheader("🧮 Tính Độ Lọc Cầu Thận (CrCl)")
    st.caption("Công thức Cockcroft-Gault")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Số Bệnh Nhân")
        
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=65,
            step=1
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.5,
            help="Cân nặng thực tế"
        )
        
        scr = st.number_input(
            "Creatinine máu (mg/dL)",
            min_value=0.1,
            max_value=15.0,
            value=1.0,
            step=0.1,
            help="Bình thường: 0.7-1.2 mg/dL"
        )
        
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True
        )
        
        if st.button("🧮 Tính CrCl", type="primary"):
            # Cockcroft-Gault Formula
            crcl = ((140 - age) * weight) / (72 * scr)
            if sex == "Nữ":
                crcl *= 0.85
            
            crcl = round(crcl, 1)
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                # Display CrCl
                if crcl >= 90:
                    st.success(f"## {crcl} mL/phút")
                    st.success("✅ Chức năng thận bình thường")
                    stage = "Bình thường (G1)"
                elif crcl >= 60:
                    st.success(f"## {crcl} mL/phút")
                    st.info("Giảm nhẹ")
                    stage = "CKD Giai đoạn 2 (G2)"
                elif crcl >= 30:
                    st.warning(f"## {crcl} mL/phút")
                    st.warning("⚠️ Giảm trung bình")
                    stage = "CKD Giai đoạn 3 (G3)"
                elif crcl >= 15:
                    st.error(f"## {crcl} mL/phút")
                    st.error("❗ Giảm nặng")
                    stage = "CKD Giai đoạn 4 (G4)"
                else:
                    st.error(f"## {crcl} mL/phút")
                    st.error("🚨 Suy thận")
                    stage = "CKD Giai đoạn 5 (G5)"
            
            # Detailed interpretation
            st.markdown("### 💡 Giải Thích")
            st.write(f"**Giai đoạn CKD:** {stage}")
            
            st.markdown("""
            **Ý nghĩa điều chỉnh liều:**
            - Nhiều kháng sinh cần điều chỉnh liều
            - Tham khảo hướng dẫn của bệnh viện
            - Hội chẩn dược sĩ lâm sàng nếu cần
            """)
            
            # Formula
            with st.expander("📐 Formula & Reference"):
                st.markdown("""
                **Cockcroft-Gault Formula:**
                
                ```
                CrCl (mL/min) = [(140 - Age) × Weight] / (72 × SCr)
                
                × 0.85 if Female
                ```
                
                **Parameters:**
                - Age: years
                - Weight: kg (actual body weight)
                - SCr: mg/dL
                
                **Limitations:**
                - Not accurate in extremes (obesity, elderly)
                - Consider eGFR (MDRD or CKD-EPI) alternatively
                - Use ideal body weight in obesity
                
                **Reference:**
                Cockcroft DW, Gault MH. Prediction of creatinine clearance 
                from serum creatinine. Nephron. 1976;16(1):31-41.
                """)

# ===== Vancomycin Calculator =====
elif "Vancomycin" in function_type:
    st.subheader("💉 Vancomycin Dosing Calculator")
    st.caption("AUC-Guided Dosing (ASHP/IDSA 2020)")
    
    st.info("""
    🚧 **Advanced Feature - Under Development**
    
    Full Vancomycin AUC calculator coming in Week 2.
    
    **Will include:**
    - Loading dose calculation
    - Maintenance dose based on CrCl
    - AUC/MIC target (400-600)
    - Trough-based dosing (legacy method)
    - Dose adjustment recommendations
    """)
    
    st.markdown("### Quick Reference")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Initial Dosing (Empiric):**
        - **Loading Dose:** 25-30 mg/kg IV × 1
        - **Maintenance:** 15-20 mg/kg/dose IV q8-12h
        
        **Target Levels:**
        - **AUC₂₄:** 400-600 mg•h/L (serious infections)
        - **Trough:** 10-20 mcg/mL (trough-based, less accurate)
        
        **Timing:**
        - Check trough before 4th dose (steady state)
        - Recheck after dose adjustment
        """)
    
    with col2:
        st.markdown("""
        **Renal Dosing:**
        - **CrCl >50:** q12h
        - **CrCl 30-50:** q24h
        - **CrCl 15-30:** q48h
        - **CrCl <15:** Loading dose, then consult nephrology
        
        **Special Populations:**
        - Obesity: Use actual body weight
        - Elderly: Lower doses, careful monitoring
        - Dialysis: Post-HD dosing
        """)
    
    with st.expander("📚 Full Guidelines"):
        st.markdown("""
        **Vancomycin Therapeutic Monitoring Guidelines**
        
        **Reference:**
        Rybak MJ, et al. Therapeutic monitoring of vancomycin for serious 
        methicillin-resistant Staphylococcus aureus infections: A revised 
        consensus guideline and review of the American Society of 
        Health-System Pharmacists, the Infectious Diseases Society of 
        America, the Pediatric Infectious Diseases Society, and the Society 
        of Infectious Diseases Pharmacists. Am J Health Syst Pharm. 
        2020;77(11):835-864.
        
        **Key Points:**
        1. AUC-guided dosing preferred over trough-only
        2. Target AUC₂₄/MIC 400-600
        3. Bayesian software recommended
        4. Consult pharmacist for complex cases
        """)

# ===== Database Lookup =====
elif "Database" in function_type:
    st.subheader("📊 Antibiotic Database Lookup")
    
    # Load data
    try:
        df = pd.read_csv("data-csv/Antibiotics.csv")
        
        st.markdown("### Search Antibiotics")
        search = st.text_input("🔍 Search by drug name or indication:", "")
        
        if search:
            # Filter dataframe
            mask = df.astype(str).apply(lambda x: x.str.contains(search, case=False, na=False)).any(axis=1)
            result = df[mask]
            
            if len(result) > 0:
                st.success(f"Found {len(result)} result(s)")
                st.dataframe(result, use_container_width=True)
            else:
                st.warning("No results found. Try another search term.")
        else:
            st.info("Enter a search term (drug name, class, or indication)")
            
            # Show sample
            with st.expander("📋 View All Antibiotics"):
                st.dataframe(df, use_container_width=True)
        
    except FileNotFoundError:
        st.error("""
        ❌ **Data file not found**
        
        Please ensure `data-csv/Antibiotics.csv` exists in the repository.
        """)

# ===== Tra cứu liều =====
else:  # "Tra cứu liều"
    st.subheader("🔍 Tra Cứu Liều Kháng Sinh")
    
    # Common antibiotics quick reference
    st.markdown("### Kháng Sinh Thường Dùng")
    
    antibiotic = st.selectbox(
        "Chọn kháng sinh:",
        [
            "Cefepime",
            "Piperacillin/Tazobactam",
            "Meropenem",
            "Vancomycin",
            "Levofloxacin",
            "Ceftriaxone",
            "Amoxicillin/Clavulanate"
        ]
    )
    
    if antibiotic == "Cefepime":
        st.markdown("""
        ### Cefepime
        
        **Class:** 4th generation cephalosporin
        
        **Indications:**
        - Severe infections (nosocomial pneumonia, febrile neutropenia)
        - Pseudomonas coverage
        
        **Dosing:**
        - **Moderate infections:** 1-2 g IV q12h
        - **Severe infections:** 2 g IV q8h
        - **Febrile neutropenia:** 2 g IV q8h
        
        **Renal Adjustment:**
        - CrCl 30-60: 2 g q12h → 2 g q24h
        - CrCl 11-29: 2 g q12h → 2 g q24h
        - CrCl <11: 2 g q12h → 1 g q24h
        
        **Notes:**
        - Good CNS penetration
        - Risk of neurotoxicity in renal failure
        - Extended infusion for difficult infections
        
        **Reference:** FDA Label Rev 07/2025
        """)
    
    elif antibiotic == "Piperacillin/Tazobactam":
        st.markdown("""
        ### Piperacillin/Tazobactam (Pip/Tazo)
        
        **Class:** Extended-spectrum penicillin + beta-lactamase inhibitor
        
        **Indications:**
        - Intra-abdominal infections
        - Nosocomial pneumonia
        - Febrile neutropenia
        
        **Dosing:**
        - **Standard:** 3.375 g IV q6h OR 4.5 g IV q6h
        - **Extended infusion:** 4.5 g IV over 4 hours q8h
        - **Nosocomial pneumonia:** 4.5 g IV q6h + aminoglycoside
        
        **Renal Adjustment:**
        - CrCl 20-40: 2.25 g q6h
        - CrCl <20: 2.25 g q8h
        
        **Notes:**
        - Extended infusion for better PK/PD
        - Higher doses for Pseudomonas
        
        **Reference:** FDA Label Rev 12/2024
        """)
    
    elif antibiotic == "Meropenem":
        st.markdown("""
        ### Meropenem
        
        **Class:** Carbapenem
        
        **Indications:**
        - Severe infections (MDR organisms)
        - Meningitis
        - Febrile neutropenia
        
        **Dosing:**
        - **Standard:** 1 g IV q8h
        - **Severe/CNS:** 2 g IV q8h
        - **Extended infusion:** 2 g IV over 3h q8h (preferred)
        
        **Renal Adjustment:**
        - CrCl 26-50: 1 g q12h
        - CrCl 10-25: 500 mg q12h
        - CrCl <10: 500 mg q24h
        
        **Notes:**
        - Extended infusion improves outcomes
        - Excellent CNS penetration
        - Reserve for MDR pathogens (stewardship)
        
        **Reference:** FDA Label, IDSA Guidelines
        """)
    
    else:
        st.info(f"Detailed information for **{antibiotic}** coming soon...")

# ========== FOOTER ==========
st.markdown("---")

st.warning("""
**⚠️ Important Reminders:**
- Always check local antibiogram
- Verify drug interactions
- Adjust for organ dysfunction
- Consult clinical pharmacist for complex cases
- Follow hospital formulary guidelines
""")

st.caption("📚 Based on FDA labels, IDSA/ATS guidelines, and institutional protocols")
st.caption("⚠️ Always verify with current hospital formulary")

