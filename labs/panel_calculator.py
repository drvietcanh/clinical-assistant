"""
Lab Panel Calculator Module
Calculate và interpret multiple labs cùng lúc với auto-interpretation
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Optional, Tuple
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES, CBC_RANGES, BMP_RANGES, CMP_RANGES, LFT_RANGES, COAG_RANGES, CARDIAC_RANGES, THYROID_RANGES


# Panel definitions
PANELS = {
    "CBC": {
        "name": "CBC - Complete Blood Count",
        "tests": ["WBC", "RBC", "Hemoglobin", "Hematocrit", "MCV", "MCH", "MCHC", "Platelet"],
        "ranges": CBC_RANGES
    },
    "BMP": {
        "name": "BMP - Basic Metabolic Panel",
        "tests": ["Sodium", "Potassium", "Chloride", "Bicarbonate", "BUN", "Creatinine", "Glucose"],
        "ranges": BMP_RANGES
    },
    "CMP": {
        "name": "CMP - Comprehensive Metabolic Panel",
        "tests": ["Sodium", "Potassium", "Chloride", "Bicarbonate", "BUN", "Creatinine", "Glucose", 
                  "Total Protein", "Albumin", "Bilirubin Total", "ALT", "AST", "Alkaline Phosphatase"],
        "ranges": CMP_RANGES
    },
    "LFT": {
        "name": "LFT - Liver Function Tests",
        "tests": ["Bilirubin Total", "Bilirubin Direct", "ALT", "AST", "Alkaline Phosphatase", 
                  "Total Protein", "Albumin"],
        "ranges": LFT_RANGES
    },
    "Coagulation": {
        "name": "Coagulation Panel",
        "tests": ["PT", "INR", "aPTT", "D-dimer"],
        "ranges": COAG_RANGES
    },
    "Cardiac": {
        "name": "Cardiac Markers",
        "tests": ["Troponin I", "CK-MB", "BNP", "NT-proBNP"],
        "ranges": CARDIAC_RANGES
    },
    "Thyroid": {
        "name": "Thyroid Function Tests",
        "tests": ["TSH", "Free T4", "Free T3"],
        "ranges": THYROID_RANGES
    }
}


def detect_patterns(panel_data: Dict[str, float], panel_name: str, gender: str = "male", age: Optional[int] = None) -> List[str]:
    """
    Detect clinical patterns from lab panel
    
    Args:
        panel_data: Dict of {test_name: value}
        panel_name: Name of panel
        gender: Gender for normal ranges
        age: Age for normal ranges
    
    Returns:
        List of detected patterns
    """
    patterns = []
    
    if panel_name == "CBC":
        # Anemia pattern
        hgb = panel_data.get("Hemoglobin")
        mcv = panel_data.get("MCV")
        if hgb and mcv:
            normal_hgb = get_normal_range("Hemoglobin", gender, age)
            if normal_hgb and hgb < normal_hgb.get("min", 12):
                if mcv < 80:
                    patterns.append("🔴 **Thiếu máu hồng cầu nhỏ** (Microcytic anemia) - Gợi ý thiếu sắt, thalassemia")
                elif mcv > 100:
                    patterns.append("🔴 **Thiếu máu hồng cầu to** (Macrocytic anemia) - Gợi ý thiếu B12/folate")
                else:
                    patterns.append("🔴 **Thiếu máu hồng cầu bình thường** (Normocytic anemia) - Gợi ý mất máu cấp, bệnh mạn tính")
        
        # Thrombocytopenia
        plt = panel_data.get("Platelet")
        if plt and plt < 150:
            if plt < 50:
                patterns.append("⚠️ **Giảm tiểu cầu nặng** - Nguy cơ xuất huyết cao")
            else:
                patterns.append("⚠️ **Giảm tiểu cầu** - Cần theo dõi")
        
        # Leukocytosis/Leukopenia
        wbc = panel_data.get("WBC")
        if wbc:
            if wbc > 11:
                patterns.append("⬆️ **Tăng bạch cầu** - Gợi ý nhiễm trùng, viêm")
            elif wbc < 4:
                patterns.append("⬇️ **Giảm bạch cầu** - Gợi ý nhiễm trùng, thuốc, bệnh tủy xương")
    
    elif panel_name == "BMP" or panel_name == "CMP":
        # AKI pattern
        cr = panel_data.get("Creatinine")
        bun = panel_data.get("BUN")
        if cr and bun:
            normal_cr = get_normal_range("Creatinine", gender, age)
            if normal_cr and cr > normal_cr.get("max", 1.2):
                bun_cr_ratio = bun / cr if cr > 0 else 0
                if bun_cr_ratio > 20:
                    patterns.append("🔴 **Suy thận cấp - Prerenal** - BUN/Cr > 20, gợi ý giảm thể tích")
                elif bun_cr_ratio < 15:
                    patterns.append("🔴 **Suy thận cấp - Intrinsic** - BUN/Cr < 15, gợi ý tổn thương thận")
                else:
                    patterns.append("🔴 **Suy thận cấp** - Cần đánh giá thêm")
        
        # Electrolyte imbalances
        na = panel_data.get("Sodium")
        k = panel_data.get("Potassium")
        if na:
            if na < 135:
                patterns.append("⚠️ **Hạ natri máu** - Cần đánh giá thể tích, ADH")
            elif na > 145:
                patterns.append("⚠️ **Tăng natri máu** - Cần đánh giá tình trạng nước")
        if k:
            if k < 3.5:
                patterns.append("⚠️ **Hạ kali máu** - Nguy cơ rối loạn nhịp tim")
            elif k > 5.0:
                patterns.append("⚠️ **Tăng kali máu** - Nguy cơ rối loạn nhịp tim, cần xử trí ngay")
        
        # Metabolic acidosis/alkalosis
        bicarb = panel_data.get("Bicarbonate")
        if bicarb:
            if bicarb < 22:
                patterns.append("🔴 **Nhiễm toan chuyển hóa** - Cần đánh giá anion gap")
            elif bicarb > 28:
                patterns.append("🔴 **Nhiễm kiềm chuyển hóa** - Gợi ý nôn, dùng thuốc")
    
    elif panel_name == "LFT":
        # Hepatocellular pattern
        alt = panel_data.get("ALT")
        ast = panel_data.get("AST")
        if alt and ast:
            if alt > 3 * (get_normal_range("ALT", gender, age) or {}).get("max", 40):
                if ast / alt > 2:
                    patterns.append("🔴 **Tổn thương gan - Alcoholic** - AST/ALT > 2")
                else:
                    patterns.append("🔴 **Tổn thương gan - Viral/Medication** - ALT tăng cao")
        
        # Cholestatic pattern
        alkphos = panel_data.get("Alkaline Phosphatase")
        bili = panel_data.get("Bilirubin Total")
        if alkphos and bili:
            normal_alkphos = get_normal_range("Alkaline Phosphatase", gender, age)
            if normal_alkphos and alkphos > 2 * normal_alkphos.get("max", 120):
                patterns.append("🔴 **Ứ mật** - Alkaline phosphatase tăng cao")
    
    elif panel_name == "Coagulation":
        # Bleeding risk
        inr = panel_data.get("INR")
        aptt = panel_data.get("aPTT")
        if inr and inr > 3.0:
            patterns.append("⚠️ **INR cao** - Nguy cơ xuất huyết, cần điều chỉnh warfarin")
        if aptt:
            normal_aptt = get_normal_range("aPTT", gender, age)
            if normal_aptt and aptt > 1.5 * normal_aptt.get("max", 35):
                patterns.append("⚠️ **aPTT kéo dài** - Cần đánh giá nguyên nhân")
    
    elif panel_name == "Cardiac":
        # ACS pattern
        trop = panel_data.get("Troponin I")
        ckmb = panel_data.get("CK-MB")
        if trop and trop > 0.04:
            patterns.append("🔴 **Troponin tăng** - Gợi ý nhồi máu cơ tim, cần đánh giá ngay")
        if ckmb and ckmb > (get_normal_range("CK-MB", gender, age) or {}).get("max", 5):
            patterns.append("🔴 **CK-MB tăng** - Gợi ý tổn thương cơ tim")
        
        # Heart failure
        bnp = panel_data.get("BNP")
        if bnp and bnp > 400:
            patterns.append("🔴 **BNP tăng cao** - Gợi ý suy tim")
    
    elif panel_name == "Thyroid":
        # Hyperthyroidism
        tsh = panel_data.get("TSH")
        ft4 = panel_data.get("Free T4")
        if tsh and ft4:
            normal_tsh = get_normal_range("TSH", gender, age)
            if normal_tsh and tsh < normal_tsh.get("min", 0.4):
                if ft4 > (get_normal_range("Free T4", gender, age) or {}).get("max", 1.8):
                    patterns.append("🔴 **Cường giáp** - TSH thấp, Free T4 cao")
        
        # Hypothyroidism
        if tsh and ft4:
            normal_tsh = get_normal_range("TSH", gender, age)
            if normal_tsh and tsh > normal_tsh.get("max", 4.0):
                if ft4 < (get_normal_range("Free T4", gender, age) or {}).get("min", 0.8):
                    patterns.append("🔴 **Suy giáp** - TSH cao, Free T4 thấp")
    
    return patterns


def render():
    """Render Lab Panel Calculator UI"""
    st.subheader("🧮 Lab Panel Calculator")
    st.caption("Tính toán và giải thích nhiều xét nghiệm cùng lúc - Auto-interpretation")
    
    # Instructions
    with st.expander("ℹ️ Hướng dẫn sử dụng"):
        st.markdown("""
        **Lab Panel Calculator** cho phép bạn:
        
        1. **Nhập toàn bộ panel** (CBC, CMP, LFT, etc.)
        2. **Tự động giải thích** tất cả giá trị
        3. **Nhận diện pattern** lâm sàng
        4. **Cảnh báo giá trị nguy hiểm**
        5. **Xuất kết quả** dạng bảng
        
        **Cách sử dụng:**
        - Chọn panel cần tính
        - Nhập các giá trị xét nghiệm
        - Xem kết quả tự động với giải thích và pattern recognition
        """)
    
    # Gender and age
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("Giới tính:", ["Nam", "Nữ"], key="panel_gender")
        gender_key = "male" if gender == "Nam" else "female"
    
    with col2:
        age = st.number_input("Tuổi (nếu cần):", min_value=0, max_value=120, value=None, key="panel_age")
    
    st.markdown("---")
    
    # Panel selection
    st.markdown("#### 📋 Chọn Panel")
    
    panel_name = st.selectbox(
        "Panel:",
        list(PANELS.keys()),
        format_func=lambda x: PANELS[x]["name"],
        key="panel_select"
    )
    
    if not panel_name:
        st.info("Vui lòng chọn panel")
        return
    
    panel_info = PANELS[panel_name]
    st.caption(f"Panel: {panel_info['name']}")
    
    st.markdown("---")
    
    # Data entry
    st.markdown("#### 📝 Nhập Giá trị")
    
    panel_data = {}
    
    # Get test info for this panel
    test_list = panel_info["tests"]
    ranges = panel_info["ranges"]
    
    # Organize into columns
    num_cols = 2
    cols = st.columns(num_cols)
    
    for idx, test_name in enumerate(test_list):
        col = cols[idx % num_cols]
        
        with col:
            test_info = ranges.get(test_name, {})
            test_label = test_info.get("label", test_name)
            unit = test_info.get("unit", "")
            normal = test_info.get("normal", {})
            
            # Default value
            default_val = None
            if normal:
                if "min" in normal and "max" in normal:
                    default_val = (normal["min"] + normal["max"]) / 2
                elif "max" in normal:
                    default_val = normal["max"] * 0.8
            
            value = st.number_input(
                f"{test_label} ({unit})",
                min_value=0.0,
                value=default_val,
                step=0.1,
                format="%.2f",
                key=f"panel_{test_name}"
            )
            
            panel_data[test_name] = value
    
    st.markdown("---")
    
    # Analysis
    st.markdown("#### 📊 Kết quả Phân tích")
    
    # Create results table
    results = []
    critical_count = 0
    
    for test_name in test_list:
        value = panel_data.get(test_name)
        if value is None:
            continue
        
        test_info = ranges.get(test_name, {})
        test_label = test_info.get("label", test_name)
        unit = test_info.get("unit", "")
        
        # Get normal range
        normal_range = get_normal_range(test_name, gender_key, age)
        min_val = normal_range.get("min") if normal_range else None
        max_val = normal_range.get("max") if normal_range else None
        
        # Interpretation
        interpretation = interpret_value(test_name, value, gender_key, age)
        
        # Check critical
        is_crit = is_critical(test_name, value)
        if is_crit:
            critical_count += 1
        
        # Normal range string
        range_str = ""
        if min_val is not None and max_val is not None:
            range_str = f"{min_val:.2f} - {max_val:.2f}"
        elif max_val is not None:
            range_str = f"< {max_val:.2f}"
        elif min_val is not None:
            range_str = f"> {min_val:.2f}"
        
        results.append({
            "Xét nghiệm": test_label,
            "Giá trị": f"{value:.2f} {unit}",
            "Giới hạn bình thường": range_str,
            "Giải thích": interpretation
        })
    
    # Display table
    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Critical alerts
    if critical_count > 0:
        st.error(f"⚠️ **CẢNH BÁO:** Có {critical_count} giá trị ở mức nguy hiểm!")
    
    st.markdown("---")
    
    # Pattern recognition
    st.markdown("#### 🔍 Pattern Recognition")
    
    patterns = detect_patterns(panel_data, panel_name, gender_key, age)
    
    if patterns:
        for pattern in patterns:
            st.markdown(f"- {pattern}")
    else:
        st.info("Không phát hiện pattern bất thường đặc biệt")
    
    st.markdown("---")
    
    # Summary
    st.markdown("#### 📋 Tóm Tắt")
    
    col1, col2, col3 = st.columns(3)
    
    total_tests = len([v for v in panel_data.values() if v is not None])
    abnormal_tests = len([test for test in test_list 
                          if panel_data.get(test) is not None 
                          and interpret_value(test, panel_data[test], gender_key, age) != "Normal ✓"])
    
    with col1:
        st.metric("Tổng số xét nghiệm", total_tests)
    
    with col2:
        st.metric("Giá trị bất thường", abnormal_tests)
    
    with col3:
        st.metric("Giá trị nguy hiểm", critical_count)
    
    # Export option
    with st.expander("💾 Xuất Kết quả"):
        csv = df.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="📥 Tải xuống CSV",
            data=csv,
            file_name=f"{panel_name}_results.csv",
            mime="text/csv"
        )

