"""
Renal Dosing Summary
Tóm tắt điều chỉnh liều theo chức năng thận
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class RenalDosingAdjustment:
    """Điều chỉnh liều theo chức năng thận"""
    drug_name: str
    normal_dose: str
    crcl_30_60: str
    crcl_15_30: str
    crcl_under_15: str
    notes: Optional[str] = None


RENAL_DOSING_ADJUSTMENTS = [
    RenalDosingAdjustment(
        drug_name="Vancomycin",
        normal_dose="15-20mg/kg IV mỗi 8-12 giờ",
        crcl_30_60="Giảm khoảng cách liều (mỗi 12-24 giờ)",
        crcl_15_30="Giảm khoảng cách liều (mỗi 24-48 giờ)",
        crcl_under_15="Giảm khoảng cách liều (mỗi 48-72 giờ) hoặc lọc máu",
        notes="⚠️ Cần theo dõi nồng độ (TDM) để đảm bảo hiệu quả và tránh độc tính"
    ),
    RenalDosingAdjustment(
        drug_name="Gentamicin",
        normal_dose="5-7mg/kg IV mỗi 24 giờ",
        crcl_30_60="Giảm liều hoặc khoảng cách liều",
        crcl_15_30="Giảm liều đáng kể hoặc tránh",
        crcl_under_15="Tránh hoặc chỉ dùng khi thực sự cần + lọc máu",
        notes="⚠️ Độc tính thận và thính giác. Cần TDM."
    ),
    RenalDosingAdjustment(
        drug_name="Amikacin",
        normal_dose="15-20mg/kg IV mỗi 24 giờ",
        crcl_30_60="Giảm liều hoặc khoảng cách liều",
        crcl_15_30="Giảm liều đáng kể",
        crcl_under_15="Tránh hoặc chỉ dùng khi thực sự cần + lọc máu",
        notes="⚠️ Độc tính thận và thính giác. Cần TDM."
    ),
    RenalDosingAdjustment(
        drug_name="Ciprofloxacin",
        normal_dose="400mg IV mỗi 12 giờ hoặc 500-750mg PO BID",
        crcl_30_60="Giảm liều 50%",
        crcl_15_30="200-400mg mỗi 12 giờ",
        crcl_under_15="200mg mỗi 12 giờ hoặc tránh",
        notes="Thải qua thận một phần"
    ),
    RenalDosingAdjustment(
        drug_name="Levofloxacin",
        normal_dose="500-750mg IV/PO mỗi 24 giờ",
        crcl_30_60="500mg mỗi 24 giờ",
        crcl_15_30="500mg mỗi 48 giờ",
        crcl_under_15="250-500mg mỗi 48 giờ",
        notes="Thải qua thận"
    ),
    RenalDosingAdjustment(
        drug_name="Piperacillin-Tazobactam",
        normal_dose="4.5g IV mỗi 6-8 giờ",
        crcl_30_60="4.5g mỗi 8 giờ",
        crcl_15_30="2.25g mỗi 8 giờ",
        crcl_under_15="2.25g mỗi 12 giờ",
        notes="Cả piperacillin và tazobactam đều thải qua thận"
    ),
    RenalDosingAdjustment(
        drug_name="Meropenem",
        normal_dose="1g IV mỗi 8 giờ",
        crcl_30_60="1g mỗi 8 giờ",
        crcl_15_30="500mg-1g mỗi 12 giờ",
        crcl_under_15="500mg mỗi 12 giờ",
        notes="Thải qua thận"
    ),
    RenalDosingAdjustment(
        drug_name="Ceftriaxone",
        normal_dose="1-2g IV/IM mỗi 24 giờ",
        crcl_30_60="Không đổi",
        crcl_15_30="Không đổi",
        crcl_under_15="Không đổi (thải qua gan và thận)",
        notes="Thải qua cả gan và thận, không cần điều chỉnh liều ở suy thận"
    ),
    RenalDosingAdjustment(
        drug_name="Azithromycin",
        normal_dose="500mg IV/PO mỗi 24 giờ",
        crcl_30_60="Không đổi",
        crcl_15_30="Không đổi",
        crcl_under_15="Không đổi (thải qua gan)",
        notes="Thải chủ yếu qua gan, không cần điều chỉnh liều ở suy thận"
    ),
    RenalDosingAdjustment(
        drug_name="Clindamycin",
        normal_dose="600-900mg IV mỗi 8 giờ hoặc 300-450mg PO QID",
        crcl_30_60="Không đổi",
        crcl_15_30="Không đổi",
        crcl_under_15="Không đổi (thải qua gan)",
        notes="Thải chủ yếu qua gan, không cần điều chỉnh liều ở suy thận"
    ),
]


def get_renal_dosing_summary() -> List[RenalDosingAdjustment]:
    """Lấy tóm tắt điều chỉnh liều theo thận"""
    return RENAL_DOSING_ADJUSTMENTS


def render_renal_dosing_view():
    """Render UI cho renal dosing summary"""
    import streamlit as st
    
    st.markdown("### 🫘 Tóm tắt Liều theo Thận")
    st.caption("Điều chỉnh liều kháng sinh theo chức năng thận (CrCl/eGFR)")
    
    st.info("💡 **Lưu ý:** Đây là hướng dẫn chung. Luôn tham khảo hướng dẫn cụ thể cho từng thuốc và tính toán CrCl/eGFR chính xác.")
    
    adjustments = get_renal_dosing_summary()
    
    # Create table
    st.markdown("#### 📊 Bảng Điều chỉnh Liều")
    
    for adj in adjustments:
        with st.expander(f"**{adj.drug_name}**", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Liều bình thường:**")
                st.markdown(f"{adj.normal_dose}")
                
                st.markdown("**CrCl 30-60 ml/min:**")
                st.markdown(f"{adj.crcl_30_60}")
            
            with col2:
                st.markdown("**CrCl 15-30 ml/min:**")
                st.markdown(f"{adj.crcl_15_30}")
                
                st.markdown("**CrCl < 15 ml/min:**")
                st.markdown(f"{adj.crcl_under_15}")
            
            if adj.notes:
                st.warning(f"⚠️ {adj.notes}")
    
    st.markdown("---")
    
    # Link to calculator
    st.markdown("#### 🧮 Tính toán CrCl/eGFR")
    col_calc1, col_calc2 = st.columns(2)
    with col_calc1:
        if st.button("📊 Mở Calculator CrCl", use_container_width=True):
            st.switch_page("pages/05_🔬_Labs_and_Calculators.py")
    with col_calc2:
        if st.button("💊 Mở Calculator Liều theo Thận", use_container_width=True):
            st.switch_page("pages/07_💊_Drug_Database.py")
    
    st.markdown("---")
    
    # General principles
    st.markdown("#### 📋 Nguyên tắc chung")
    st.markdown("""
    1. **Tính CrCl/eGFR chính xác**: Sử dụng công thức Cockcroft-Gault hoặc MDRD
    2. **Xem xét cả tuổi và cân nặng**: Đặc biệt ở người cao tuổi và béo phì
    3. **Theo dõi chức năng thận**: Đánh giá lại định kỳ trong quá trình điều trị
    4. **TDM khi cần**: Một số thuốc (vancomycin, aminoglycoside) cần theo dõi nồng độ
    5. **Lọc máu**: Cần điều chỉnh liều và thời gian dùng ở bệnh nhân lọc máu
    """)
