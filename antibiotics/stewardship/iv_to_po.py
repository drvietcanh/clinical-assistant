"""
IV to PO Switch Criteria
Tiêu chí chuyển từ đường tiêm truyền sang đường uống
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class IVToPODrug:
    """Thông tin thuốc có thể chuyển IV → PO"""
    drug_name: str
    iv_dose: str
    po_dose: str
    bioavailability: str
    notes: Optional[str] = None


@dataclass
class IVToPOCriteria:
    """Tiêu chí chuyển IV → PO"""
    clinical_criteria: List[str]
    microbiological_criteria: List[str]
    general_criteria: List[str]


IV_TO_PO_CRITERIA = IVToPOCriteria(
    clinical_criteria=[
        "Bệnh nhân afebrile ≥ 24 giờ",
        "Cải thiện triệu chứng lâm sàng (giảm đau, giảm triệu chứng nhiễm trùng)",
        "Ổn định huyết động (không cần vasopressor)",
        "Có thể uống được (không nôn, không tắc ruột)",
        "Chức năng tiêu hóa bình thường"
    ],
    microbiological_criteria=[
        "Cấy máu/đờm/nước tiểu âm tính hoặc",
        "Vi khuẩn nhạy cảm với kháng sinh đường uống",
        "Không có nguy cơ nhiễm khuẩn đa kháng",
        "Đã có kết quả cấy và độ nhạy cảm"
    ],
    general_criteria=[
        "Bệnh nhân tuân thủ điều trị",
        "Không có chống chỉ định với đường uống",
        "Có thuốc tương đương đường uống với độ hấp thu tốt"
    ]
)


IV_TO_PO_DRUGS = [
    IVToPODrug(
        drug_name="Levofloxacin",
        iv_dose="500-750mg IV mỗi 24 giờ",
        po_dose="500-750mg PO mỗi 24 giờ",
        bioavailability="99%",
        notes="Bioavailability cao, có thể chuyển trực tiếp"
    ),
    IVToPODrug(
        drug_name="Moxifloxacin",
        iv_dose="400mg IV mỗi 24 giờ",
        po_dose="400mg PO mỗi 24 giờ",
        bioavailability="90%",
        notes="Bioavailability cao, chuyển trực tiếp"
    ),
    IVToPODrug(
        drug_name="Ciprofloxacin",
        iv_dose="400mg IV mỗi 12 giờ",
        po_dose="500-750mg PO mỗi 12 giờ",
        bioavailability="70-80%",
        notes="Có thể cần tăng liều PO một chút"
    ),
    IVToPODrug(
        drug_name="Amoxicillin-Clavulanate",
        iv_dose="1.2g IV mỗi 8 giờ",
        po_dose="875/125mg PO mỗi 12 giờ",
        bioavailability="75-85%",
        notes="Liều PO tương đương với IV"
    ),
    IVToPODrug(
        drug_name="Cefuroxime",
        iv_dose="750mg-1.5g IV mỗi 8 giờ",
        po_dose="500mg PO mỗi 12 giờ",
        bioavailability="50-60%",
        notes="Có thể chuyển khi nhiễm trùng nhẹ đến trung bình"
    ),
    IVToPODrug(
        drug_name="Clindamycin",
        iv_dose="600-900mg IV mỗi 8 giờ",
        po_dose="300-450mg PO mỗi 6-8 giờ",
        bioavailability="90%",
        notes="Bioavailability cao, chuyển trực tiếp"
    ),
    IVToPODrug(
        drug_name="Metronidazole",
        iv_dose="500mg IV mỗi 8 giờ",
        po_dose="500mg PO mỗi 8 giờ",
        bioavailability="95-100%",
        notes="Bioavailability rất cao, chuyển trực tiếp"
    ),
    IVToPODrug(
        drug_name="Linezolid",
        iv_dose="600mg IV mỗi 12 giờ",
        po_dose="600mg PO mỗi 12 giờ",
        bioavailability="100%",
        notes="Bioavailability 100%, chuyển trực tiếp"
    ),
    IVToPODrug(
        drug_name="Azithromycin",
        iv_dose="500mg IV mỗi 24 giờ",
        po_dose="500mg PO mỗi 24 giờ",
        bioavailability="38% (nhưng hiệu quả do phân bố tốt)",
        notes="Có thể chuyển, nhưng cần đảm bảo tuân thủ"
    ),
    IVToPODrug(
        drug_name="Doxycycline",
        iv_dose="100mg IV mỗi 12 giờ",
        po_dose="100mg PO mỗi 12 giờ",
        bioavailability="90-100%",
        notes="Bioavailability cao, chuyển trực tiếp"
    ),
]


# Drugs that CANNOT be switched IV → PO easily
CANNOT_SWITCH_DRUGS = [
    "Vancomycin",  # PO không hấp thu, chỉ dùng cho C. difficile
    "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",  # PO không hấp thu
    "Most Cephalosporins (Ceftriaxone, Ceftazidime, Cefepime)",  # PO không có hoặc bioavailability thấp
    "Carbapenems (Meropenem, Imipenem)",  # PO không có
    "Piperacillin-Tazobactam",  # PO không có
    "Colistin",  # PO không hấp thu tốt
]


def get_iv_to_po_criteria() -> IVToPOCriteria:
    """Lấy tiêu chí chuyển IV → PO"""
    return IV_TO_PO_CRITERIA


def get_iv_to_po_drugs() -> List[IVToPODrug]:
    """Lấy danh sách thuốc có thể chuyển IV → PO"""
    return IV_TO_PO_DRUGS


def render_iv_to_po_view():
    """Render UI cho IV → PO switch criteria"""
    import streamlit as st
    
    st.markdown("### 💊 Tiêu chí Chuyển IV → PO")
    st.caption("Chuyển từ đường tiêm truyền sang đường uống khi bệnh nhân đáp ứng tốt")
    
    criteria = get_iv_to_po_criteria()
    
    # Clinical criteria
    st.markdown("#### ✅ Tiêu chí lâm sàng")
    for criterion in criteria.clinical_criteria:
        st.markdown(f"- ✓ {criterion}")
    
    st.markdown("---")
    
    # Microbiological criteria
    st.markdown("#### 🦠 Tiêu chí vi sinh")
    for criterion in criteria.microbiological_criteria:
        st.markdown(f"- ✓ {criterion}")
    
    st.markdown("---")
    
    # General criteria
    st.markdown("#### 📋 Tiêu chí chung")
    for criterion in criteria.general_criteria:
        st.markdown(f"- ✓ {criterion}")
    
    st.markdown("---")
    
    # Drugs that can be switched
    st.markdown("#### 💊 Thuốc có thể chuyển IV → PO")
    
    drugs = get_iv_to_po_drugs()
    
    for drug in drugs:
        with st.expander(f"**{drug.drug_name}**", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**IV:** {drug.iv_dose}")
            with col2:
                st.markdown(f"**PO:** {drug.po_dose}")
            
            st.markdown(f"**Độ hấp thu:** {drug.bioavailability}")
            
            if drug.notes:
                st.caption(f"💡 {drug.notes}")
    
    st.markdown("---")
    
    # Drugs that cannot be switched
    st.markdown("#### ⚠️ Thuốc KHÔNG thể chuyển IV → PO")
    st.warning("Các thuốc sau đây không có dạng uống hoặc độ hấp thu kém, cần tiếp tục đường IV:")
    for drug in CANNOT_SWITCH_DRUGS:
        st.markdown(f"- ❌ {drug}")
    
    st.markdown("---")
    
    # Benefits
    st.markdown("#### 💡 Lợi ích của chuyển IV → PO")
    st.markdown("""
    - ✅ Giảm chi phí điều trị
    - ✅ Giảm nguy cơ nhiễm khuẩn liên quan catheter
    - ✅ Giảm thời gian nằm viện
    - ✅ Tăng chất lượng cuộc sống bệnh nhân
    - ✅ Giảm nguy cơ kháng thuốc do điều trị ngắn hơn
    """)
