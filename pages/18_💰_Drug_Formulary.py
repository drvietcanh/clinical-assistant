"""
Drug Formulary Information Module
Information about drugs covered by insurance (BHYT) and formularies
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from formulary.search import (
    search_formulary,
    get_drug_formulary_info,
    check_drug_coverage
)
from formulary.data import (
    get_all_formulary_drugs,
    get_drugs_by_category,
    get_category_list
)

# Standard page setup
setup_page(
    page_title="Danh mục Thuốc BHYT",
    page_icon="💰",
    description="Thông tin về thuốc trong danh mục BHYT và bảo hiểm"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("💰 Danh mục Thuốc BHYT")
    st.caption("Module **Danh mục Thuốc BHYT** – thông tin về thuốc được bảo hiểm chi trả.")
    
    view_mode = st.radio(
        "Chế độ xem:",
        ["Tìm kiếm", "Theo nhóm thuốc", "Tất cả"],
        key="formulary_view_mode"
    )
    
    if view_mode == "Theo nhóm thuốc":
        category_filter = st.selectbox(
            "Chọn nhóm thuốc:",
            ["Tất cả"] + get_category_list(),
            key="formulary_category_filter"
        )
    
    insurance_filter = st.selectbox(
        "Loại bảo hiểm:",
        ["Tất cả", "BHYT", "Private"],
        key="formulary_insurance_filter"
    )
    
    st.markdown("---")
    st.info("""
    **💰 Drug Formulary:**
    - Thông tin về thuốc trong **danh mục BHYT**
    - **Giá tham khảo** và coverage
    - **Generic alternatives**
    - **Prior authorization** requirements
    
    **💡 Lưu ý:**
    - Giá chỉ mang tính **tham khảo**
    - Danh mục có thể thay đổi
    - Cần xác nhận với cơ sở y tế
    """)

# ========== MAIN CONTENT ==========

st.markdown("## 💰 Danh mục Thuốc BHYT")
st.markdown("""
**Thông tin về thuốc trong danh mục BHYT và bảo hiểm**

Tra cứu thuốc được bảo hiểm chi trả, giá tham khảo, và thuốc thay thế.
""")

# Display based on view mode
if view_mode == "Tìm kiếm":
    st.markdown("### 🔍 Tìm kiếm Thuốc")
    
    search_query = st.text_input(
        "Nhập tên thuốc (generic hoặc brand name):",
        placeholder="Ví dụ: Metformin, Amoxicillin, Lipitor...",
        key="formulary_search_query"
    )
    
    insurance_type = None if insurance_filter == "Tất cả" else insurance_filter
    
    if search_query:
        results = search_formulary(search_query, insurance_type=insurance_type)
        
        if results:
            st.success(f"✅ Tìm thấy {len(results)} thuốc")
            
            for drug in results:
                render_drug_formulary_info(drug)
        else:
            st.warning("Không tìm thấy thuốc. Vui lòng thử lại với tên khác.")

elif view_mode == "Theo nhóm thuốc":
    st.markdown("### 📚 Thuốc theo Nhóm")
    
    category = None if category_filter == "Tất cả" else category_filter
    insurance_type = None if insurance_filter == "Tất cả" else insurance_filter
    
    drugs = get_drugs_by_category(category) if category else get_all_formulary_drugs()
    if insurance_type:
        drugs = [d for d in drugs if insurance_type in d.insurance_coverage]
    
    if drugs:
        st.success(f"✅ Tìm thấy {len(drugs)} thuốc")
        
        for drug in drugs:
            render_drug_formulary_info(drug)
    else:
        st.warning("Không tìm thấy thuốc trong nhóm này.")

else:  # Tất cả
    st.markdown("### 📋 Tất cả Thuốc trong Formulary")
    
    insurance_type = None if insurance_filter == "Tất cả" else insurance_filter
    drugs = get_all_formulary_drugs()
    if insurance_type:
        drugs = [d for d in drugs if insurance_type in d.insurance_coverage]
    
    if drugs:
        st.success(f"✅ Tìm thấy {len(drugs)} thuốc")
        
        for drug in drugs:
            render_drug_formulary_info(drug)
    else:
        st.warning("Không tìm thấy thuốc.")


def render_drug_formulary_info(drug):
    """Render formulary drug information"""
    with st.expander(f"**{drug.drug_name}** ({drug.generic_name})", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**Tên thuốc:** {drug.drug_name}")
            st.markdown(f"**Tên generic:** {drug.generic_name}")
            if drug.brand_names:
                st.markdown(f"**Brand names:** {', '.join(drug.brand_names)}")
            st.markdown(f"**Nhóm thuốc:** {drug.category}")
        
        with col2:
            # Insurance coverage
            if "BHYT" in drug.insurance_coverage:
                st.success(f"✅ **BHYT:** {drug.coverage_type}")
            else:
                st.warning(f"⚠️ **BHYT:** Không có trong danh mục")
            
            if "Private" in drug.insurance_coverage:
                st.info(f"💼 **Private:** {drug.coverage_type}")
            
            if drug.generic_available:
                st.success("✅ Generic có sẵn")
            else:
                st.warning("⚠️ Chỉ có brand name")
        
        # Price
        if drug.price_range:
            st.markdown(f"**💰 Giá tham khảo:** {drug.price_range}")
        
        # Notes
        if drug.notes:
            st.markdown(f"**📝 Ghi chú:** {drug.notes}")
        
        # Alternatives
        if drug.alternatives:
            st.markdown("**💡 Thuốc thay thế:**")
            for alt in drug.alternatives:
                st.markdown(f"- {alt}")
        
        # Link to Drug Database
        st.markdown("---")
        st.markdown(f"💡 Xem thêm thông tin về **{drug.drug_name}** trong [Cơ sở dữ liệu thuốc](?page=07_💊_Drug_Database)")


# Coverage checker
st.markdown("---")
st.markdown("### ✅ Kiểm tra Coverage")

check_drug = st.text_input(
    "Nhập tên thuốc để kiểm tra coverage:",
    placeholder="Ví dụ: Metformin, Warfarin...",
    key="formulary_coverage_check"
)

if check_drug:
    coverage_info = check_drug_coverage(check_drug, "BHYT")
    
    if coverage_info:
        st.markdown("---")
        if coverage_info['is_covered']:
            st.success(f"✅ **{coverage_info['drug_name']}** có trong danh mục BHYT")
            st.markdown(f"**Loại coverage:** {coverage_info['coverage_type']}")
            st.markdown(f"**Generic có sẵn:** {'Có' if coverage_info['generic_available'] else 'Không'}")
            if coverage_info['price_range']:
                st.markdown(f"**Giá tham khảo:** {coverage_info['price_range']}")
        else:
            st.warning(f"⚠️ **{coverage_info['drug_name']}** không có trong danh mục BHYT")
            if coverage_info['alternatives']:
                st.markdown("**Thuốc thay thế:**")
                for alt in coverage_info['alternatives']:
                    st.markdown(f"- {alt}")
        
        if coverage_info['notes']:
            st.info(f"**Ghi chú:** {coverage_info['notes']}")
    else:
        st.warning(f"Không tìm thấy thông tin về {check_drug} trong database.")

# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về Formulary")
st.markdown("""
**Danh mục BHYT:**

- **Full coverage:** Thuốc được BHYT chi trả hoàn toàn
- **Partial coverage:** Thuốc được BHYT chi trả một phần
- **Prior authorization required:** Cần xác nhận trước khi kê đơn
- **Not covered:** Không có trong danh mục BHYT

**Lưu ý:**
- Database này chỉ mang tính tham khảo
- Danh mục BHYT có thể thay đổi theo quy định
- Giá chỉ mang tính tham khảo, có thể khác nhau giữa các cơ sở
- Luôn xác nhận với cơ sở y tế về coverage và giá chính xác
- Một số thuốc có thể cần prior authorization hoặc giấy tờ đặc biệt

**Generic vs Brand:**
- Generic drugs thường rẻ hơn và có trong danh mục BHYT
- Brand name drugs có thể không có trong danh mục hoặc cần prior authorization
- Luôn ưu tiên generic khi có thể
""")

# Footer
render_standard_footer(disclaimer=True)

