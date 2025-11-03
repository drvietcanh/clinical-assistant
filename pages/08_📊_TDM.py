"""
TDM Module - Therapeutic Drug Monitoring
Main Router - Imports from drugs.tdm module
Dedicated module for TDM calculators
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from drugs.tdm import (
    render_digoxin_tdm,
    render_phenytoin_tdm,
    render_lithium_tdm,
    render_theophylline_tdm,
    render_immunosuppressants_tdm
)

# Standard page setup
setup_page(
    page_title="TDM - Theo Dõi Nồng Độ Thuốc",
    page_icon="📊",
    description="Tính toán và theo dõi nồng độ thuốc trong điều trị"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Công Cụ TDM")
    
    tdm_drug = st.selectbox(
        "Thuốc:",
        [
            "💚 TDM - Digoxin (Tim Mạch)",
            "🧠 TDM - Phenytoin (Thần Kinh)",
            "💊 TDM - Lithium (Tâm Thần)",
            "🫁 TDM - Theophylline (Hô Hấp)",
            "🩸 TDM - Tacrolimus/Cyclosporine (Miễn Dịch)"
        ]
    )
    
    st.markdown("---")
    
    st.info("""
    **📚 Về TDM:**
    
    **Therapeutic Drug Monitoring (TDM)** là việc đo nồng độ thuốc trong máu để:
    - Đảm bảo nồng độ trong khoảng điều trị
    - Tránh độc tính
    - Điều chỉnh liều chính xác
    
    **Chỉ định TDM:**
    - Thuốc có phạm vi điều trị hẹp
    - Độc tính cao nếu quá liều
    - Thay đổi dược động học lớn giữa các cá nhân
    """)
    
    st.markdown("---")
    
    st.caption("""
    **💡 Lưu ý:**
    - TDM chỉ là công cụ hỗ trợ
    - Luôn kết hợp với đánh giá lâm sàng
    - Nồng độ có thể thay đổi theo thời điểm lấy mẫu
    """)

# ========== MAIN CONTENT ==========

# Route to appropriate TDM calculator
if "Digoxin" in tdm_drug:
    render_digoxin_tdm()
    
elif "Phenytoin" in tdm_drug:
    render_phenytoin_tdm()
    
elif "Lithium" in tdm_drug:
    render_lithium_tdm()
    
elif "Theophylline" in tdm_drug:
    render_theophylline_tdm()
    
elif "Tacrolimus" in tdm_drug or "Cyclosporine" in tdm_drug:
    render_immunosuppressants_tdm()

# ========== FOOTER ==========
render_standard_footer(disclaimer=True)

