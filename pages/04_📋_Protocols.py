"""
Protocols Module - Clinical Treatment Protocols
Main Router - Imports from protocols module
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from protocols import (
    render_sepsis,
    render_sepsis_3hour,
    render_shock,
    render_stroke,
    render_gi_bleeding,
    render_dka,
    render_electrolytes,
    render_copd,
    render_asthma,
    render_acs,
    render_hf,
    render_aki,
    render_cap,
    render_hap_vap,
    render_cdiff,
    render_thyrotoxic_crisis,
    render_myxedema_coma,
    render_adrenal_crisis,
    render_tls,
    render_febrile_neutropenia,
    render_hypercalcemia
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
            "🧪 Thận (Nephrology)",
            "🦠 Nhiễm Khuẩn (Infectious)",
            "⚕️ Nội Tiết (Endocrinology)",
            "🎗️ Ung Thư (Oncology)"
        ]
    )
    
    st.markdown("---")
    
    # Display protocols based on specialty
    if "Cấp Cứu" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🦠 Sepsis 1-Hour Bundle",
                "🦠 Sepsis 3-Hour Bundle",
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
    elif "Nhiễm Khuẩn" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🫁 CAP Management",
                "🏥 HAP/VAP Guidelines",
                "🦠 C. diff Treatment"
            ],
            label_visibility="collapsed"
        )
    elif "Nội Tiết" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "⚡ Thyrotoxic Crisis",
                "❄️ Myxedema Coma",
                "⚡ Adrenal Crisis"
            ],
            label_visibility="collapsed"
        )
    elif "Ung Thư" in specialty or "Oncology" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🎗️ Tumor Lysis Syndrome",
                "🌡️ Febrile Neutropenia",
                "📈 Hypercalcemia of Malignancy"
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
if "Sepsis 1-Hour" in protocol:
    render_sepsis()
elif "Sepsis 3-Hour" in protocol:
    render_sepsis_3hour()
elif "Sepsis" in protocol:
    render_sepsis()  # Fallback

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

elif "CAP" in protocol:
    render_cap()

elif "HAP" in protocol or "VAP" in protocol:
    render_hap_vap()

elif "C. diff" in protocol or "cdiff" in protocol.lower():
    render_cdiff()

elif "Thyrotoxic" in protocol or "thyrotoxic" in protocol.lower():
    render_thyrotoxic_crisis()

elif "Myxedema" in protocol or "myxedema" in protocol.lower():
    render_myxedema_coma()

elif "Adrenal" in protocol or "adrenal" in protocol.lower():
    render_adrenal_crisis()

elif "Tumor Lysis" in protocol or "TLS" in protocol or "tls" in protocol.lower():
    render_tls()

elif "Febrile Neutropenia" in protocol or "neutropenia" in protocol.lower():
    render_febrile_neutropenia()

elif "Hypercalcemia" in protocol or "hypercalcemia" in protocol.lower():
    render_hypercalcemia()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
