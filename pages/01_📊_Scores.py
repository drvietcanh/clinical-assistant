"""
Scores Module - Clinical Scoring Systems
Main Router - Organized by Specialty

Imports calculators from individual specialty modules
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path to import scores module
sys.path.insert(0, str(Path(__file__).parent.parent))

from scores.config import SCORES_BY_SPECIALTY
from scores import cardiology, emergency

st.set_page_config(page_title="Scores - Clinical Assistant", page_icon="📊", layout="wide")

# ========== HEADER ==========
st.title("📊 Thang Điểm Lâm Sàng")
st.markdown("Calculators phân loại theo chuyên khoa")
st.markdown("---")

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
st.markdown("---")
st.caption("📚 All scores based on international guidelines and peer-reviewed literature")
st.caption("⚠️ For reference only - Always use clinical judgment")
st.caption("🗂️ Modular architecture for easy maintenance and expansion")
