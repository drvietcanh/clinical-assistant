"""
Scores Module - Clinical Scoring Systems
Main Router - Organized by Specialty

Imports calculators from individual specialty modules
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from scores.config import SCORES_BY_SPECIALTY
from scores import cardiology, emergency, respiratory, neurology, gi, metabolism, hematology, nephrology, trauma, psychiatry, oncology, surgery, pediatrics, infectious, ent, obstetrics, dermatology, rheumatology, ophthalmology

# Standard page setup
setup_page(
    page_title="Thang Điểm Lâm Sàng",
    page_icon="📊",
    description="Calculators phân loại theo chuyên khoa"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("Chọn Chuyên Khoa")
    
    specialty = st.selectbox(
        "Chuyên khoa:",
        list(SCORES_BY_SPECIALTY.keys()),
        index=0  # Default: Emergency & Critical Care
    )
    
    st.markdown("---")
    
    st.subheader("Thang Điểm Có Sẵn")
    
    # Display scores for selected specialty
    scores_in_specialty = SCORES_BY_SPECIALTY[specialty]
    
    score_options = []
    for score_id, score_info in scores_in_specialty.items():
        score_options.append(f"{score_info['status']} {score_info['name']}")
    
    selected_score_display = st.radio(
        "Calculator:",
        score_options,
        label_visibility="collapsed"
    )
    
    # Extract score_id from selection
    selected_score_id = None
    for score_id, score_info in scores_in_specialty.items():
        if score_info['name'] in selected_score_display:
            selected_score_id = score_id
            break
    
    st.markdown("---")
    st.info("""
    **Chú thích:**
    - ✅ Hoàn thành
    - 🚧 Đang phát triển
    - 📋 Kế hoạch
    """)
    
    st.markdown("---")
    st.caption(f"**{len([s for specialty_scores in SCORES_BY_SPECIALTY.values() for s in specialty_scores])}** calculators")
    st.caption("**Evidence-based**")

# ========== MAIN CONTENT ==========

# Display specialty overview
st.info(f"""
**Chuyên khoa:** {specialty}

**Số lượng calculators:** {len(scores_in_specialty)}

**Đang xem:** {SCORES_BY_SPECIALTY[specialty][selected_score_id]['name'] if selected_score_id else 'Chọn calculator bên trái'}
""")

# ========== ROUTE TO APPROPRIATE MODULE ==========

# Emergency & Critical Care
if "Cấp Cứu" in specialty:
    emergency.render_emergency_calculator(selected_score_id)

# Cardiology
elif "Tim Mạch" in specialty:
    cardiology.render_cardiology_calculator(selected_score_id)

# Respiratory
elif "Hô Hấp" in specialty:
    respiratory.render_respiratory_calculator(selected_score_id)

# Neurology
elif "Thần Kinh" in specialty:
    neurology.render_neurology_calculator(selected_score_id)

# GI/Hepatology
elif "Tiêu Hóa" in specialty or "Gan" in specialty:
    gi.render_gi_calculator(selected_score_id)

# Metabolism/Endocrinology
elif "Nội Tiết" in specialty or "Chuyển Hóa" in specialty:
    metabolism.render_metabolism_calculator(selected_score_id)

# Hematology
elif "Huyết Học" in specialty or "Đông Máu" in specialty:
    hematology.render_hematology_calculator(selected_score_id)

# Nephrology
elif "Thận" in specialty or "Điện Giải" in specialty:
    nephrology.render_nephrology_calculator(selected_score_id)

# Trauma
elif "Chấn Thương" in specialty or "Chỉnh Hình" in specialty:
    trauma.render_trauma_calculator(selected_score_id)

# Psychiatry
elif "Tâm Thần" in specialty or "Tâm Lý" in specialty:
    psychiatry.render_psychiatry_calculator(selected_score_id)

# Oncology
elif "Ung Thư" in specialty:
    oncology.render_oncology_calculator(selected_score_id)

# Surgery
elif "Phẫu Thuật" in specialty or "Gây Mê" in specialty:
    surgery.render_surgery_calculator(selected_score_id)

# Pediatrics
elif "Nhi Khoa" in specialty:
    pediatrics.render_pediatrics_calculator(selected_score_id)

# Infectious Disease
elif "Nhiễm Khuẩn" in specialty:
    infectious.render_infectious_calculator(selected_score_id)

# ENT
elif "Tai Mũi Họng" in specialty or "ENT" in specialty:
    ent.render_ent_calculator(selected_score_id)

# Obstetrics
elif "Sản Khoa" in specialty or "Obstetrics" in specialty:
    obstetrics.render_obstetrics_calculator(selected_score_id)

# Dermatology
elif "Da Liễu" in specialty or "Dermatology" in specialty:
    dermatology.render_dermatology_calculator(selected_score_id)

# Rheumatology
elif "Thấp Khớp" in specialty or "Miễn Dịch" in specialty:
    rheumatology.render_rheumatology_calculator(selected_score_id)

# Ophthalmology
elif "Mắt" in specialty or "Ophthalmology" in specialty:
    ophthalmology.render_ophthalmology_calculator(selected_score_id)

# Other specialties - show placeholder for now
else:
    score_info = scores_in_specialty[selected_score_id]
    st.subheader(f"📋 {score_info['name']}")
    st.caption(score_info['desc'])
    
    if score_info['status'] == "✅":
        st.success("✅ Đã hoàn thành - Đang trong module riêng")
    elif score_info['status'] == "🚧":
        st.warning("🚧 Đang phát triển - Sắp ra mắt")
    else:
        st.info("📋 Trong kế hoạch phát triển")
    
    st.markdown("---")
    st.markdown(f"""
    **Mô tả:** {score_info['desc']}
    
    Calculator này sẽ sớm được triển khai trong module chuyên khoa tương ứng.
    """)

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
