"""
TDM Module - Therapeutic Drug Monitoring
Main Router - Imports from drugs.tdm module
Dedicated module for TDM calculators - Optimized with category grouping
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from drugs.tdm.tdm_config import get_drugs_by_category, get_all_drugs, TDM_DRUGS

# Import existing TDM modules
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
    
    # Get drugs by category
    categories = get_drugs_by_category()
    
    # Build drug list grouped by category
    drug_options = []
    category_map = {}  # Map drug name to category
    
    # Category order and icons
    category_order = [
        ("Aminoglycoside", "💉"),
        ("Glycopeptide", "💊"),
        ("Antiepileptic", "🧠"),
        ("Cardiovascular", "❤️"),
        ("Respiratory", "🫁"),
        ("Psychiatry", "💊"),
        ("Immunosuppressant", "🩸"),
        ("Antifungal", "🦠"),
        ("Oncology/Rheumatology", "🎗️"),
        ("Antitubercular", "🦠")
    ]
    
    for category, icon in category_order:
        if category in categories:
            for drug_id, drug_info in categories[category]:
                display_name = f"{drug_info['icon']} {drug_info['name']} ({category})"
                drug_options.append(display_name)
                category_map[display_name] = drug_id
    
    # Add existing drugs that might not be in config yet
    existing_drugs = [
        "💚 TDM - Digoxin (Tim Mạch)",
        "🧠 TDM - Phenytoin (Thần Kinh)",
        "💊 TDM - Lithium (Tâm Thần)",
        "🫁 TDM - Theophylline (Hô Hấp)",
        "🩸 TDM - Tacrolimus/Cyclosporine (Miễn Dịch)"
    ]
    
    # Combine lists
    all_options = existing_drugs + [d for d in drug_options if d not in existing_drugs]
    
    tdm_drug = st.selectbox(
        "Thuốc:",
        all_options,
        help="Chọn thuốc cần theo dõi nồng độ"
    )
    
    st.markdown("---")
    
    # Show drug info if selected from config
    if tdm_drug in category_map:
        drug_id = category_map[tdm_drug]
        drug_info = TDM_DRUGS[drug_id]
        
        st.info(f"""
        **{drug_info['name']} TDM:**
        - **Khoảng điều trị:** {drug_info['therapeutic_range']}
        - **Thời điểm lấy mẫu:** {drug_info['sampling_time']}
        - **Half-life:** {drug_info.get('half_life_hours', 'N/A')} giờ
        """)
    else:
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
    
    # Statistics
    total_drugs = len(get_all_drugs()) + 5  # +5 for existing modules
    st.caption(f"**📊 Tổng số thuốc TDM:** {total_drugs}")
    st.caption(f"**📁 Số category:** {len(categories)}")
    
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

# Route to new drugs from config
elif tdm_drug in category_map:
    drug_id = category_map[tdm_drug]
    drug_info = TDM_DRUGS[drug_id]
    
    # For now, show placeholder - will implement full calculators later
    st.markdown(f"### {drug_info['icon']} {drug_info['name']} TDM Calculator")
    st.info(f"""
    **Khoảng điều trị:** {drug_info['therapeutic_range']}
    
    **Thời điểm lấy mẫu:** {drug_info['sampling_time']}
    
    **Half-life:** {drug_info.get('half_life_hours', 'N/A')} giờ
    
    **Đơn vị:** {drug_info['unit']}
    """)
    
    st.warning(f"🚧 **Đang phát triển:** Calculator chi tiết cho {drug_info['name']} sẽ sớm được thêm vào.")
    
    # Basic level interpretation
    st.markdown("---")
    st.markdown("### 📊 Giải Thích Nồng Độ Cơ Bản")
    
    col1, col2 = st.columns(2)
    
    with col1:
        level = st.number_input(
            f"Nồng độ {drug_info['name']} ({drug_info['unit']})",
            min_value=0.0,
            max_value=100.0,
            value=(drug_info['target_min'] + drug_info['target_max']) / 2,
            step=0.1,
            format="%.2f",
            key=f"{drug_id}_level"
        )
    
    with col2:
        st.metric("Mục tiêu điều trị", drug_info['therapeutic_range'])
    
    if st.button("📊 Giải Thích", type="primary"):
        if level < drug_info['target_min']:
            st.info(f"⬇️ **Dưới mục tiêu** ({level:.2f} {drug_info['unit']} < {drug_info['target_min']} {drug_info['unit']})")
        elif level <= drug_info['target_max']:
            st.success(f"✅ **Trong mục tiêu điều trị** ({drug_info['target_min']}-{drug_info['target_max']} {drug_info['unit']})")
        elif drug_info.get('toxic_threshold') and level <= drug_info['toxic_threshold']:
            st.warning(f"⚠️ **Trên mục tiêu** ({level:.2f} {drug_info['unit']} > {drug_info['target_max']} {drug_info['unit']})")
        else:
            st.error(f"🚨 **ĐỘC TÍNH** ({level:.2f} {drug_info['unit']} > {drug_info.get('toxic_threshold', drug_info['target_max'] * 1.5)} {drug_info['unit']})")

# ========== FOOTER ==========
render_standard_footer(disclaimer=True)

