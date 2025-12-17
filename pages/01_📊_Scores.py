"""
Scores Module - Clinical Scoring Systems
Main Router - Organized by Specialty

Imports calculators from individual specialty modules
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from scores.config import SCORES_BY_SPECIALTY
from scores import cardiology, emergency, respiratory, neurology, gi, metabolism, hematology, nephrology, trauma, psychiatry, oncology, surgery, pediatrics, infectious, ent, obstetrics, dermatology, rheumatology, ophthalmology, pain, nursing

# Standard page setup
setup_page(
    page_title="Calculators & Thang điểm",
    page_icon="📊",
    description="Thang điểm và calculators lâm sàng, phân loại theo chuyên khoa"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("Chọn chuyên khoa")
    
    specialty = st.selectbox(
        "Chuyên khoa:",
        list(SCORES_BY_SPECIALTY.keys()),
        index=0  # Default: Emergency & Critical Care
    )
    
    st.markdown("---")
    
    st.subheader("Thang điểm có sẵn")
    
    # Display scores for selected specialty
    scores_in_specialty = SCORES_BY_SPECIALTY[specialty]

    # Tìm nhanh trong chuyên khoa hiện tại
    search_query = st.text_input(
        "Tìm nhanh thang điểm/calculator:",
        "",
        placeholder="Nhập tên hoặc viết tắt (ví dụ: Wells, CURB-65, CHA2DS2-VASc)...",
    ).strip()

    # Ưu tiên các calculator được đánh dấu "(DÙNG HÀNG NGÀY)" trong mô tả
    def is_daily_use(info: dict) -> bool:
        desc = info.get("desc", "") or ""
        return "DÙNG HÀNG NGÀY" in desc

    # Lọc theo từ khóa (nếu có)
    def matches_query(score_id: str, info: dict) -> bool:
        if not search_query:
            return True
        q = search_query.lower()
        return q in score_id.lower() or q in info.get("name", "").lower() or q in (info.get("desc", "") or "").lower()

    filtered_items = [(k, v) for k, v in scores_in_specialty.items() if matches_query(k, v)]

    # Nếu không có kết quả, hiển thị thông báo và dùng toàn bộ danh sách để tránh lỗi widget
    if not filtered_items and search_query:
        st.warning("Không tìm thấy thang điểm phù hợp với từ khóa. Hiển thị tất cả thang điểm trong chuyên khoa.")
        filtered_items = list(scores_in_specialty.items())

    sorted_items = sorted(
        filtered_items,
        key=lambda item: (not is_daily_use(item[1]), item[1]["name"]),
    )

    score_options = []
    for score_id, score_info in sorted_items:
        label = f"{score_info['status']} {score_info['name']}"
        if is_daily_use(score_info):
            label += " ⭐"
        score_options.append(label)
    
    selected_score_display = st.radio(
        "Calculator:",
        score_options,
        label_visibility="collapsed"
    )
    
    # Extract score_id from selection (dựa trên danh sách đã sắp xếp)
    selected_score_id = None
    for score_id, score_info in sorted_items:
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
    st.caption("**Dựa trên bằng chứng**")

# ========== MAIN CONTENT ==========

# Display specialty overview
current_name = SCORES_BY_SPECIALTY[specialty][selected_score_id]['name'] if selected_score_id else "Chọn calculator bên trái"
current_desc = SCORES_BY_SPECIALTY[specialty][selected_score_id].get('desc', '') if selected_score_id else ""

st.info(f"""
**Chuyên khoa:** {specialty}

**Số lượng calculators:** {len(scores_in_specialty)}

**Đang xem:** {current_name}

**Dùng khi:** {current_desc if current_desc else 'Chọn calculator để xem mô tả chi tiết.'}
""")

# ========== ROUTE TO APPROPRIATE MODULE ==========

# Emergency & Critical Care
if "Cấp cứu" in specialty:
    emergency.render_emergency_calculator(selected_score_id)

# Cardiology
elif "Tim mạch" in specialty:
    cardiology.render_cardiology_calculator(selected_score_id)

# Respiratory
elif "Hô hấp" in specialty:
    respiratory.render_respiratory_calculator(selected_score_id)

# Neurology
elif "Thần kinh" in specialty:
    neurology.render_neurology_calculator(selected_score_id)

# GI/Hepatology
elif "Tiêu Hóa" in specialty or "Gan" in specialty:
    gi.render_gi_calculator(selected_score_id)

# Metabolism/Endocrinology
elif "Nội tiết" in specialty or "Chuyển hóa" in specialty:
    metabolism.render_metabolism_calculator(selected_score_id)

# Hematology
elif "Huyết học" in specialty or "Đông máu" in specialty:
    hematology.render_hematology_calculator(selected_score_id)

# Nephrology
elif "Thận" in specialty or "Điện giải" in specialty:
    nephrology.render_nephrology_calculator(selected_score_id)

# Trauma
elif "Chấn Thương" in specialty or "Chỉnh Hình" in specialty:
    trauma.render_trauma_calculator(selected_score_id)

# Psychiatry
elif "Tâm Thần" in specialty or "Tâm Lý" in specialty:
    psychiatry.render_psychiatry_calculator(selected_score_id)

# Oncology
elif "Ung thư" in specialty:
    oncology.render_oncology_calculator(selected_score_id)

# Surgery
elif "Phẫu Thuật" in specialty or "Gây Mê" in specialty:
    surgery.render_surgery_calculator(selected_score_id)

# Pediatrics
elif "Nhi Khoa" in specialty:
    pediatrics.render_pediatrics_calculator(selected_score_id)

# Infectious Disease
elif "Nhiễm khuẩn" in specialty:
    infectious.render_infectious_calculator(selected_score_id)

# ENT
elif "Tai Mũi Họng" in specialty or "ENT" in specialty:
    ent.render_ent_calculator(selected_score_id)

# Obstetrics
elif "Sản khoa" in specialty or "Obstetrics" in specialty:
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

# Pain Assessment
elif "Đánh giá đau" in specialty or "Pain" in specialty:
    pain.render_pain_calculator(selected_score_id)

# Nursing Care
elif "Chăm sóc điều dưỡng" in specialty or "Nursing" in specialty:
    nursing.render_nursing_calculator(selected_score_id)

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
