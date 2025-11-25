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
    render_anaphylaxis,
    render_hypertensive_emergency,
    render_status_epilepticus,
    render_opioid_overdose,
    render_alcohol_withdrawal,
    render_acute_pain,
    render_copd,
    render_asthma,
    render_acs,
    render_hf,
    render_atrial_fibrillation,
    render_dvt_pe,
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
    page_title="Phác đồ điều trị",
    page_icon="📋",
    description="Các phác đồ điều trị chuẩn theo hướng dẫn quốc tế"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📂 Chọn chuyên khoa")
    
    specialty = st.selectbox(
        "Chuyên khoa:",
        [
            "🚨 Cấp cứu (Emergency)",
            "🫁 Hô hấp (Respiratory)",
            "❤️ Tim mạch (Cardiology)",
            "🧪 Thận (Nephrology)",
            "🦠 Nhiễm khuẩn (Infectious)",
            "⚕️ Nội tiết (Endocrinology)",
            "🎗️ Ung thư (Oncology)",
            "💊 Đau (Pain Management)"
        ]
    )
    
    st.markdown("---")
    
    # Display protocols based on specialty
    if "Cấp cứu" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🦠 Sepsis 1-Hour Bundle",
                "🦠 Sepsis 3-Hour Bundle",
                "💔 Quản lý sốc",
                "🧠 Stroke Management",
                "🩸 GI Bleeding",
                "🍭 DKA Protocol",
                "⚡ Electrolyte Emergency",
                "🚨 Anaphylaxis",
                "⚡ Cơn Tăng Huyết Áp Cấp Cứu",
                "🧠 Status Epilepticus",
                "💉 Ngộ Độc Opioid / Naloxone",
                "🍺 Cai Rượu Cấp"
            ],
            label_visibility="collapsed"
        )
    elif "Hô hấp" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🫁 COPD Exacerbation",
                "🫁 Cơn hen cấp"
            ],
            label_visibility="collapsed"
        )
    elif "Tim mạch" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "💔 ACS - Hội chứng vành cấp",
                "💔 Suy Tim Cấp",
                "💓 Rung Nhĩ (Atrial Fibrillation)",
                "🩸 DVT/PE Management"
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
    elif "Nhiễm khuẩn" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🫁 CAP Management",
                "🏥 HAP/VAP Guidelines",
                "🦠 C. diff Treatment"
            ],
            label_visibility="collapsed"
        )
    elif "Nội tiết" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "⚡ Thyrotoxic Crisis",
                "❄️ Myxedema Coma",
                "⚡ Adrenal Crisis"
            ],
            label_visibility="collapsed"
        )
    elif "Ung thư" in specialty or "Oncology" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🎗️ Tumor Lysis Syndrome",
                "🌡️ Febrile Neutropenia",
                "📈 Hypercalcemia of Malignancy"
            ],
            label_visibility="collapsed"
        )
    elif "Đau" in specialty or "Pain" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "💊 Quản Lý Đau Cấp"
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

elif "Anaphylaxis" in protocol or "anaphylaxis" in protocol.lower():
    render_anaphylaxis()

elif "Tăng Huyết Áp" in protocol or "Hypertensive" in protocol or "hypertensive" in protocol.lower():
    render_hypertensive_emergency()

elif "Status Epilepticus" in protocol or "status epilepticus" in protocol.lower() or "Epilepticus" in protocol:
    render_status_epilepticus()

elif "Opioid" in protocol or "opioid" in protocol.lower() or "Naloxone" in protocol or "naloxone" in protocol.lower() or "Ngộ Độc" in protocol:
    render_opioid_overdose()

elif "Alcohol" in protocol or "alcohol" in protocol.lower() or "Cai Rượu" in protocol or "Rượu" in protocol:
    render_alcohol_withdrawal()

elif "Rung Nhĩ" in protocol or "Atrial Fibrillation" in protocol or "atrial fibrillation" in protocol.lower() or "AF" in protocol:
    render_atrial_fibrillation()

elif "DVT" in protocol or "PE" in protocol or "dvt" in protocol.lower() or "pe" in protocol.lower() or "Huyết Khối" in protocol or "Thuyên Tắc" in protocol:
    render_dvt_pe()

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

elif "Đau" in protocol or "Pain" in protocol or "pain" in protocol.lower():
    render_acute_pain()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
