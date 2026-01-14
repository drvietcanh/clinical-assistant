"""
Cost Comparison Tool
So sánh chi phí điều trị giữa các kháng sinh
Dữ liệu giá tham khảo tại Việt Nam (cập nhật định kỳ)
"""

import streamlit as st
from typing import Dict, List, Optional
import pandas as pd

# Drug cost database (reference prices in VND)
# Prices are approximate and should be updated regularly
# Based on hospital formulary and market prices in Vietnam
DRUG_COSTS_VN = {
    "Vancomycin": {
        "unit_cost": 50000,  # VND per 500mg vial
        "unit": "500mg vial",
        "route": "IV",
        "notes": "Giá tham khảo, có thể thay đổi theo bệnh viện"
    },
    "Ceftriaxone": {
        "unit_cost": 30000,  # VND per 1g vial
        "unit": "1g vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Piperacillin-Tazobactam": {
        "unit_cost": 120000,  # VND per 4.5g vial
        "unit": "4.5g vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Meropenem": {
        "unit_cost": 200000,  # VND per 1g vial
        "unit": "1g vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Imipenem-Cilastatin": {
        "unit_cost": 180000,  # VND per 500mg vial
        "unit": "500mg vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Cefepime": {
        "unit_cost": 80000,  # VND per 1g vial
        "unit": "1g vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Ceftazidime": {
        "unit_cost": 40000,  # VND per 1g vial
        "unit": "1g vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Cefazolin": {
        "unit_cost": 20000,  # VND per 1g vial
        "unit": "1g vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Gentamicin": {
        "unit_cost": 15000,  # VND per 80mg vial
        "unit": "80mg vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Amikacin": {
        "unit_cost": 25000,  # VND per 500mg vial
        "unit": "500mg vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Levofloxacin": {
        "unit_cost": 35000,  # VND per 500mg vial
        "unit": "500mg vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Ciprofloxacin": {
        "unit_cost": 30000,  # VND per 400mg vial
        "unit": "400mg vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Azithromycin": {
        "unit_cost": 40000,  # VND per 500mg vial
        "unit": "500mg vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Clindamycin": {
        "unit_cost": 25000,  # VND per 600mg vial
        "unit": "600mg vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
    "Linezolid": {
        "unit_cost": 500000,  # VND per 600mg vial
        "unit": "600mg vial",
        "route": "IV",
        "notes": "Giá cao, chỉ dùng khi cần thiết"
    },
    "Daptomycin": {
        "unit_cost": 800000,  # VND per 500mg vial
        "unit": "500mg vial",
        "route": "IV",
        "notes": "Giá rất cao, chỉ dùng khi cần thiết"
    },
    "Colistin": {
        "unit_cost": 150000,  # VND per 1 million IU vial
        "unit": "1 million IU vial",
        "route": "IV",
        "notes": "Giá tham khảo"
    },
}

# Typical dosing regimens for cost calculation
TYPICAL_REGIMENS = {
    "Vancomycin": {"dose_mg": 1000, "frequency": "q12h", "days": 7},
    "Ceftriaxone": {"dose_mg": 2000, "frequency": "q24h", "days": 7},
    "Piperacillin-Tazobactam": {"dose_mg": 4500, "frequency": "q6h", "days": 7},
    "Meropenem": {"dose_mg": 2000, "frequency": "q8h", "days": 7},
    "Imipenem-Cilastatin": {"dose_mg": 1000, "frequency": "q6h", "days": 7},
    "Cefepime": {"dose_mg": 2000, "frequency": "q8h", "days": 7},
    "Ceftazidime": {"dose_mg": 2000, "frequency": "q8h", "days": 7},
    "Cefazolin": {"dose_mg": 1000, "frequency": "q8h", "days": 7},
    "Gentamicin": {"dose_mg": 240, "frequency": "q24h", "days": 7},
    "Amikacin": {"dose_mg": 1000, "frequency": "q24h", "days": 7},
    "Levofloxacin": {"dose_mg": 750, "frequency": "q24h", "days": 7},
    "Ciprofloxacin": {"dose_mg": 400, "frequency": "q12h", "days": 7},
    "Azithromycin": {"dose_mg": 500, "frequency": "q24h", "days": 5},
    "Clindamycin": {"dose_mg": 600, "frequency": "q8h", "days": 7},
    "Linezolid": {"dose_mg": 600, "frequency": "q12h", "days": 10},
    "Daptomycin": {"dose_mg": 500, "frequency": "q24h", "days": 7},
    "Colistin": {"dose_mg": 300, "frequency": "q8h", "days": 7},  # 300 mg = ~9 million IU
}


def calculate_drug_cost(antibiotic_name: str, dose_mg: float, frequency: str, days: int) -> Dict:
    """
    Calculate total cost for antibiotic treatment
    
    Args:
        antibiotic_name: Name of antibiotic
        dose_mg: Dose per administration in mg
        frequency: Frequency (e.g., "q8h", "q12h", "q24h")
        days: Duration in days
    
    Returns:
        dict with cost calculation results
    """
    if antibiotic_name not in DRUG_COSTS_VN:
        return {"error": "Không có dữ liệu giá cho kháng sinh này"}
    
    cost_info = DRUG_COSTS_VN[antibiotic_name]
    unit_cost = cost_info["unit_cost"]
    unit_dose = _parse_unit_dose(cost_info["unit"])
    
    # Calculate doses per day
    doses_per_day = _parse_frequency(frequency)
    
    # Calculate units needed per dose
    units_per_dose = dose_mg / unit_dose
    if units_per_dose < 1:
        units_per_dose = 1  # Round up to at least 1 unit
    
    # Calculate total units for treatment
    total_units = units_per_dose * doses_per_day * days
    
    # Calculate total cost
    total_cost = total_units * unit_cost
    
    # Cost per day
    cost_per_day = (units_per_dose * doses_per_day) * unit_cost
    
    return {
        "antibiotic": antibiotic_name,
        "unit_cost": unit_cost,
        "unit": cost_info["unit"],
        "units_per_dose": units_per_dose,
        "doses_per_day": doses_per_day,
        "total_units": total_units,
        "total_cost": total_cost,
        "cost_per_day": cost_per_day,
        "days": days,
        "notes": cost_info.get("notes", "")
    }


def _parse_unit_dose(unit_str: str) -> float:
    """Parse unit dose from string like '500mg vial' or '1g vial'"""
    import re
    match = re.search(r'(\d+(?:\.\d+)?)\s*(mg|g)', unit_str, re.IGNORECASE)
    if match:
        value = float(match.group(1))
        unit = match.group(2).lower()
        if unit == "g":
            value *= 1000  # Convert to mg
        return value
    return 1.0


def _parse_frequency(frequency: str) -> int:
    """Parse frequency to doses per day"""
    frequency = frequency.lower().strip()
    
    if "q24h" in frequency or "once daily" in frequency or "qd" in frequency:
        return 1
    elif "q12h" in frequency or "bid" in frequency:
        return 2
    elif "q8h" in frequency or "tid" in frequency:
        return 3
    elif "q6h" in frequency:
        return 4
    elif "q4h" in frequency:
        return 6
    else:
        return 1  # Default


def compare_costs(antibiotic_regimens: List[Dict]) -> pd.DataFrame:
    """
    Compare costs of multiple antibiotic regimens
    
    Args:
        antibiotic_regimens: List of dicts with keys: antibiotic_name, dose_mg, frequency, days
    
    Returns:
        DataFrame with comparison results
    """
    results = []
    
    for regimen in antibiotic_regimens:
        result = calculate_drug_cost(
            regimen["antibiotic_name"],
            regimen.get("dose_mg", 1000),
            regimen.get("frequency", "q12h"),
            regimen.get("days", 7)
        )
        
        if "error" not in result:
            results.append({
                "Kháng sinh": result["antibiotic"],
                "Liều/ngày": f"{regimen.get('dose_mg', 1000)}mg × {result['doses_per_day']}",
                "Số ngày": result["days"],
                "Chi phí/ngày": f"{result['cost_per_day']:,.0f} VND",
                "Tổng chi phí": f"{result['total_cost']:,.0f} VND",
            })
    
    return pd.DataFrame(results)


def render_cost_comparison():
    """Render Cost Comparison Tool UI"""
    
    st.markdown("### 💰 So Sánh Chi Phí Điều Trị")
    st.caption("So sánh chi phí điều trị giữa các kháng sinh (giá tham khảo tại Việt Nam)")
    
    st.warning("""
    **⚠️ Lưu ý quan trọng:**
    - Giá thuốc chỉ mang tính tham khảo
    - Giá thực tế có thể khác nhau tùy theo:
      - Bệnh viện/phòng khám
      - Nhà cung cấp
      - Thời điểm
      - Bảo hiểm y tế
    - Luôn kiểm tra giá thực tế tại nơi điều trị
    - Chi phí điều trị còn bao gồm: dịch truyền, bơm tiêm, nhân lực, etc.
    """)
    
    # Mode selection
    mode = st.radio(
        "Chế độ:",
        ["🔍 So sánh nhiều kháng sinh", "📊 Tính chi phí đơn lẻ"],
        key="cost_mode"
    )
    
    if mode == "📊 Tính chi phí đơn lẻ":
        # Single drug cost calculation
        st.markdown("#### 📊 Tính Chi Phí Đơn Lẻ")
        
        antibiotic_name = st.selectbox(
            "Chọn kháng sinh:",
            options=sorted(list(DRUG_COSTS_VN.keys())),
            key="cost_single_ab"
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            dose_mg = st.number_input(
                "Liều mỗi lần (mg):",
                min_value=0.0,
                value=TYPICAL_REGIMENS.get(antibiotic_name, {}).get("dose_mg", 1000.0),
                step=100.0,
                key="cost_single_dose"
            )
        
        with col2:
            frequency = st.selectbox(
                "Tần suất:",
                options=["q24h", "q12h", "q8h", "q6h", "q4h"],
                index=1,
                key="cost_single_freq"
            )
        
        with col3:
            days = st.number_input(
                "Số ngày điều trị:",
                min_value=1,
                value=TYPICAL_REGIMENS.get(antibiotic_name, {}).get("days", 7),
                step=1,
                key="cost_single_days"
            )
        
        if st.button("💰 Tính Chi Phí", type="primary", use_container_width=True):
            result = calculate_drug_cost(antibiotic_name, dose_mg, frequency, days)
            
            if "error" not in result:
                st.markdown("---")
                st.markdown("#### 📊 Kết Quả")
                
                col_r1, col_r2, col_r3 = st.columns(3)
                with col_r1:
                    st.metric("Chi phí/ngày", f"{result['cost_per_day']:,.0f} VND")
                with col_r2:
                    st.metric("Tổng chi phí", f"{result['total_cost']:,.0f} VND")
                with col_r3:
                    st.metric("Số đơn vị cần", f"{result['total_units']:.0f} {result['unit']}")
                
                st.info(f"""
                **Chi tiết:**
                - Đơn giá: {result['unit_cost']:,.0f} VND / {result['unit']}
                - Số đơn vị mỗi liều: {result['units_per_dose']:.1f}
                - Số liều/ngày: {result['doses_per_day']}
                - Tổng số đơn vị: {result['total_units']:.0f}
                """)
                
                if result.get("notes"):
                    st.caption(f"💡 {result['notes']}")
    
    else:
        # Multi-drug comparison
        st.markdown("#### 🔍 So Sánh Nhiều Kháng Sinh")
        
        num_drugs = st.number_input(
            "Số kháng sinh muốn so sánh:",
            min_value=2,
            max_value=10,
            value=3,
            step=1,
            key="cost_num_drugs"
        )
        
        regimens = []
        for i in range(num_drugs):
            with st.expander(f"Kháng sinh {i+1}", expanded=(i == 0)):
                antibiotic_name = st.selectbox(
                    "Chọn kháng sinh:",
                    options=sorted(list(DRUG_COSTS_VN.keys())),
                    key=f"cost_ab_{i}"
                )
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    dose_mg = st.number_input(
                        "Liều (mg):",
                        min_value=0.0,
                        value=TYPICAL_REGIMENS.get(antibiotic_name, {}).get("dose_mg", 1000.0),
                        step=100.0,
                        key=f"cost_dose_{i}"
                    )
                
                with col2:
                    frequency = st.selectbox(
                        "Tần suất:",
                        options=["q24h", "q12h", "q8h", "q6h", "q4h"],
                        index=1,
                        key=f"cost_freq_{i}"
                    )
                
                with col3:
                    days = st.number_input(
                        "Số ngày:",
                        min_value=1,
                        value=TYPICAL_REGIMENS.get(antibiotic_name, {}).get("days", 7),
                        step=1,
                        key=f"cost_days_{i}"
                    )
                
                regimens.append({
                    "antibiotic_name": antibiotic_name,
                    "dose_mg": dose_mg,
                    "frequency": frequency,
                    "days": days
                })
        
        if st.button("💰 So Sánh Chi Phí", type="primary", use_container_width=True):
            df = compare_costs(regimens)
            
            if not df.empty:
                st.markdown("---")
                st.markdown("#### 📊 Bảng So Sánh")
                st.dataframe(df, use_container_width=True, hide_index=True)
                
                # Sort by total cost
                df_sorted = df.copy()
                df_sorted["Tổng chi phí_num"] = df_sorted["Tổng chi phí"].str.replace(" VND", "").str.replace(",", "").astype(float)
                df_sorted = df_sorted.sort_values("Tổng chi phí_num")
                
                st.markdown("#### 🏆 Xếp Hạng (Từ Rẻ Đến Đắt)")
                for idx, row in df_sorted.iterrows():
                    rank = list(df_sorted.index).index(idx) + 1
                    medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"{rank}."
                    st.markdown(f"{medal} **{row['Kháng sinh']}**: {row['Tổng chi phí']}")
    
    # Information section
    with st.expander("📚 Thông tin về Giá Thuốc", expanded=False):
        st.markdown("""
        **Nguồn dữ liệu:**
        - Giá tham khảo từ bệnh viện và thị trường Việt Nam
        - Cập nhật định kỳ (có thể không phản ánh giá thực tế tại thời điểm hiện tại)
        
        **Các yếu tố ảnh hưởng đến chi phí:**
        - Giá thuốc gốc vs generic
        - Nhà cung cấp
        - Bệnh viện/phòng khám
        - Bảo hiểm y tế
        - Chi phí phụ trợ (dịch truyền, bơm tiêm, nhân lực)
        
        **Lưu ý:**
        - Luôn kiểm tra giá thực tế tại nơi điều trị
        - Chi phí không phải là yếu tố duy nhất để chọn kháng sinh
        - Cần cân nhắc: hiệu quả, an toàn, kháng thuốc, etc.
        """)
