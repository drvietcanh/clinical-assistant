"""
Protocols Module - Clinical Treatment Protocols
Main Router - Imports from protocols module
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from protocols import (
    render_sepsis,
    render_shock,
    render_stroke,
    render_gi_bleeding,
    render_dka,
    render_electrolytes,
    render_copd,
    render_asthma,
    render_acs,
    render_hf,
    render_aki
)

# Standard page setup
setup_page(
    page_title="Phác Đồ Điều Trị",
    page_icon="📋",
    description="Các phác đồ điều trị chuẩn theo hướng dẫn quốc tế"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📂 Chọn Chuyên Khoa")
    
    specialty = st.selectbox(
        "Chuyên khoa:",
        [
            "🚨 Cấp Cứu (Emergency)",
            "🫁 Hô Hấp (Respiratory)",
            "❤️ Tim Mạch (Cardiology)",
            "🧪 Thận (Nephrology)"
        ]
    )
    
    st.markdown("---")
    
    # Display protocols based on specialty
    if "Cấp Cứu" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🦠 Sepsis 1-Hour Bundle",
                "💔 Quản Lý Sốc",
                "🧠 Stroke Management",
                "🩸 GI Bleeding",
                "🍭 DKA Protocol",
                "⚡ Electrolyte Emergency"
            ],
            label_visibility="collapsed"
        )
    elif "Hô Hấp" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🫁 COPD Exacerbation",
                "🫁 Cơn Hen Cấp"
            ],
            label_visibility="collapsed"
        )
    elif "Tim Mạch" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "💔 ACS - Hội Chứng Vành Cấp",
                "💔 Suy Tim Cấp"
            ],
            label_visibility="collapsed"
        )
    elif "Thận" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🧪 AKI Management"
            ],
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ:**
    - International Guidelines
    - Evidence-based protocols
    - Updated regularly
    """)

# ========== MAIN CONTENT ==========

st.info(f"""
**Chuyên khoa:** {specialty}

**Phác đồ đang xem:** {protocol.split(' ', 1)[1] if ' ' in protocol else protocol}
""")

st.markdown("---")

# Route to appropriate protocol
if "Sepsis" in protocol:
    render_sepsis()

elif "Sốc" in protocol:
    render_shock()

elif "COPD" in protocol:
    render_copd()

elif "Hen" in protocol:
    render_asthma()

elif "ACS" in protocol:
    render_acs()

elif "Suy Tim" in protocol:
    render_hf()

elif "Stroke" in protocol:
    render_stroke()

elif "GI Bleeding" in protocol or "GI" in protocol:
    render_gi_bleeding()

elif "DKA" in protocol:
    render_dka()

elif "Electrolyte" in protocol:
    render_electrolytes()

elif "AKI" in protocol:
    render_aki()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
