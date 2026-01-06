"""
STOPP/START Criteria
Screening Tool of Older Persons' Prescriptions / Screening Tool to Alert to Right Treatment
European alternative to Beers Criteria
"""

import streamlit as st

def render_stopp_start(score_id: str = "STOPP/START"):
    """Render STOPP/START Criteria checker"""
    
    st.markdown("### STOPP/START Criteria")
    st.markdown("**Screening Tool of Older Persons' Prescriptions**")
    st.info("""
    **STOPP/START Criteria** là công cụ châu Âu để đánh giá:
    - **STOPP**: Thuốc nên ngừng (potentially inappropriate)
    - **START**: Thuốc nên bắt đầu (omitted but indicated)
    
    **Ưu điểm:** Cả hai chiều - không chỉ tránh PIMs mà còn đảm bảo không thiếu thuốc cần thiết.
    """)
    
    st.markdown("---")
    
    # STOPP examples
    st.markdown("#### STOPP - Thuốc nên ngừng")
    
    stopp_examples = {
        "Cardiovascular": {
            "items": [
                "Digoxin >125 mcg/day (nếu không có AF)",
                "Thiazide diuretics với gout",
                "Beta-blockers với COPD/astma nặng",
                "Diltiazem/verapamil với heart failure",
            ]
        },
        "Central Nervous System": {
            "items": [
                "Tricyclic antidepressants với glaucoma, urinary retention, constipation",
                "Benzodiazepines >1 tháng",
                "Antipsychotics với parkinsonism",
                "Anticholinergics với dementia, chronic constipation",
            ]
        },
        "Gastrointestinal": {
            "items": [
                "Proton pump inhibitors >8 tuần (nếu không có chỉ định)",
                "Metoclopramide >12 tuần",
            ]
        },
        "Pain & Inflammation": {
            "items": [
                "NSAIDs với heart failure, CKD, peptic ulcer",
                "NSAIDs với warfarin",
                "Opioids với constipation không được điều trị",
            ]
        }
    }
    
    for system, data in stopp_examples.items():
        with st.expander(f"🛑 {system}", expanded=False):
            for item in data["items"]:
                st.markdown(f"• {item}")
    
    st.markdown("---")
    
    # START examples
    st.markdown("#### START - Thuốc nên bắt đầu")
    
    start_examples = {
        "Cardiovascular": {
            "items": [
                "Aspirin/clopidogrel với CVD history",
                "Statin với diabetes + ≥1 risk factor",
                "ACE inhibitor với heart failure, IHD, diabetes + proteinuria",
                "Beta-blocker với IHD sau MI",
            ]
        },
        "Endocrine": {
            "items": [
                "Metformin với type 2 diabetes (nếu không chống chỉ định)",
                "Bisphosphonate với osteoporosis, previous fracture",
            ]
        },
        "Respiratory": {
            "items": [
                "Regular inhaled beta-2 agonist hoặc anticholinergic với COPD",
                "Inhaled corticosteroid với asthma/COPD với recurrent exacerbations",
            ]
        },
        "Musculoskeletal": {
            "items": [
                "Calcium + Vitamin D với osteoporosis",
                "DMARD với active rheumatoid arthritis",
            ]
        }
    }
    
    for system, data in start_examples.items():
        with st.expander(f"✅ {system}", expanded=False):
            for item in data["items"]:
                st.markdown(f"• {item}")
    
    st.markdown("---")
    
    # Comparison with Beers
    with st.expander("📊 So sánh STOPP/START vs Beers Criteria"):
        st.markdown("""
        | Tiêu chí | STOPP/START | Beers |
        |----------|-------------|-------|
        | **Phạm vi** | EU-based | US-based |
        | **STOPP** | ✅ Có (PIMs) | ✅ Có (PIMs) |
        | **START** | ✅ Có (omissions) | ❌ Không |
        | **Bệnh cụ thể** | ✅ Chi tiết hơn | ⚠️ Ít chi tiết |
        | **Áp dụng** | Clinical review | Drug selection |
        
        **Khuyến nghị:**
        - **STOPP/START**: Tốt hơn cho medication review toàn diện
        - **Beers**: Tốt hơn cho quick reference khi kê đơn mới
        - Nên dùng cả hai để đảm bảo tối ưu
        """)
    
    st.markdown("---")
    
    # Key principles
    st.markdown("#### Nguyên tắc sử dụng")
    st.markdown("""
    1. **STOPP Review**: Kiểm tra từng thuốc đang dùng
       - Có thuốc nào không cần thiết?
       - Có thuốc nào không phù hợp với bệnh lý?
       - Có tương tác thuốc nguy hiểm?
    
    2. **START Review**: Kiểm tra các chỉ định
       - Có bệnh lý nào chưa được điều trị?
       - Có chỉ định phòng ngừa (prevention) nào cần thiết?
       - Có guideline nào chưa được tuân thủ?
    
    3. **Thảo luận với bệnh nhân**: 
       - Giải thích lý do ngừng/thêm thuốc
       - Xem xét goals of care
       - Đảm bảo compliance
    """)
    
    st.markdown("---")
    
    # References
    st.markdown("#### References")
    st.markdown("""
    - O'Mahony D, et al. STOPP/START criteria for potentially inappropriate prescribing in older people: version 2. Age Ageing. 2015;44(2):213-218.
    - O'Mahony D, et al. STOPP/START criteria for potentially inappropriate medications/potentially prescribing omissions in older people: origin and progress. Expert Rev Clin Pharmacol. 2020;13(1):15-22.
    """)
