"""
Render functions for vaccination module
"""

import streamlit as st
from typing import List, Dict
from vaccination.vaccine_data import (
    ALL_VACCINES,
    VACCINES_CHILDREN,
    VACCINES_ADULTS,
    VACCINE_SCHEDULES,
    VACCINE_PRICES,
    get_vaccine_by_name,
    get_vaccines_by_category,
    get_schedule_by_age_group,
    Vaccine
)


def render_vaccination_home():
    """Render main vaccination home page"""
    st.markdown("## 💉 Tiêm chủng và Vắc xin")
    st.markdown("""
    **Thông tin toàn diện về tiêm chủng tại Việt Nam**
    
    - 📋 Lịch tiêm chủng cho trẻ em và người lớn
    - 💰 Giá cả các loại vắc xin
    - 📊 Phác đồ tiêm các loại vắc xin
    - 🔍 Tra cứu thông tin chi tiết
    """)
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔍 Tra cứu vắc xin",
        "📅 Lịch tiêm chủng",
        "💰 Giá cả",
        "📚 Thông tin chung"
    ])
    
    with tab1:
        render_vaccine_search()
    
    with tab2:
        render_schedule_viewer()
    
    with tab3:
        render_price_comparison()
    
    with tab4:
        render_general_info()


def render_vaccine_search():
    """Render vaccine search and detail view"""
    st.markdown("### 🔍 Tra cứu vắc xin")
    
    # Search and filter
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("🔎 Tìm kiếm", placeholder="Nhập tên vắc xin...")
    
    with col2:
        age_filter = st.selectbox(
            "👤 Đối tượng",
            ["Tất cả", "Trẻ em", "Người lớn", "Cả hai"]
        )
    
    with col3:
        category_filter = st.selectbox(
            "📋 Phân loại",
            ["Tất cả", "Bắt buộc", "Khuyến nghị"]
        )
    
    # Filter vaccines
    filtered_vaccines = ALL_VACCINES
    
    if search_term:
        filtered_vaccines = [
            v for v in filtered_vaccines
            if search_term.lower() in v.name.lower() or 
               search_term.lower() in v.name_vn.lower() or
               search_term.lower() in v.description.lower()
        ]
    
    if age_filter != "Tất cả":
        age_map = {"Trẻ em": "children", "Người lớn": "adults", "Cả hai": "both"}
        filtered_vaccines = [
            v for v in filtered_vaccines
            if v.target_age == age_map[age_filter] or v.target_age == "both"
        ]
    
    if category_filter != "Tất cả":
        filtered_vaccines = [
            v for v in filtered_vaccines
            if v.category == category_filter
        ]
    
    st.markdown(f"**Tìm thấy {len(filtered_vaccines)} vắc xin**")
    st.markdown("---")
    
    # Display vaccines
    if filtered_vaccines:
        for vaccine in filtered_vaccines:
            with st.expander(f"💉 **{vaccine.name_vn}** ({vaccine.name}) - {vaccine.category}"):
                render_vaccine_detail(vaccine)
    else:
        st.info("Không tìm thấy vắc xin nào phù hợp với tiêu chí tìm kiếm.")


def render_vaccine_detail(vaccine: Vaccine):
    """Render detailed vaccine information"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**🏭 Nhà sản xuất:** {vaccine.manufacturer}")
        st.markdown(f"**💰 Giá:** {vaccine.price_range}")
        st.markdown(f"**👤 Đối tượng:** {vaccine.target_age}")
        st.markdown(f"**📋 Phân loại:** {vaccine.category}")
    
    with col2:
        st.markdown(f"**📝 Mô tả:**")
        st.info(vaccine.description)
    
    st.markdown("---")
    
    # Indications
    st.markdown("**✅ Chỉ định:**")
    for indication in vaccine.indications:
        st.markdown(f"- {indication}")
    
    # Contraindications
    st.markdown("**❌ Chống chỉ định:**")
    for contraindication in vaccine.contraindications:
        st.markdown(f"- {contraindication}")
    
    # Side effects
    st.markdown("**⚠️ Tác dụng phụ:**")
    for side_effect in vaccine.side_effects:
        st.markdown(f"- {side_effect}")
    
    # Schedule
    st.markdown("**📅 Phác đồ tiêm:**")
    for age, schedule_desc in vaccine.schedule.items():
        st.markdown(f"- **{age}:** {schedule_desc}")
    
    if vaccine.notes:
        st.markdown(f"**📌 Lưu ý:** {vaccine.notes}")


def render_schedule_viewer():
    """Render vaccination schedule viewer"""
    st.markdown("### 📅 Lịch tiêm chủng")
    
    # Age group selector
    age_groups = list(VACCINE_SCHEDULES.keys())
    selected_age = st.selectbox(
        "Chọn nhóm tuổi:",
        age_groups,
        key="schedule_age_selector"
    )
    
    st.markdown("---")
    
    # Display schedule
    schedule = get_schedule_by_age_group(selected_age)
    
    if schedule:
        st.markdown(f"**Lịch tiêm chủng cho: {selected_age}**")
        
        # Create a table
        schedule_data = []
        for vaccine_name, schedule_desc in schedule.items():
            # Find vaccine info
            vaccine = get_vaccine_by_name(vaccine_name)
            category = vaccine.category if vaccine else "N/A"
            price = vaccine.price_range if vaccine else "N/A"
            
            schedule_data.append({
                "Vắc xin": vaccine_name,
                "Phác đồ": schedule_desc,
                "Phân loại": category,
                "Giá tham khảo": price
            })
        
        st.table(schedule_data)
        
        # Additional info
        st.info("""
        **Lưu ý:**
        - Lịch tiêm có thể thay đổi tùy theo tình trạng sức khỏe và chỉ định của bác sĩ
        - Vắc xin bắt buộc (TCMR) được tiêm miễn phí tại các trạm y tế
        - Vắc xin khuyến nghị có thể tiêm tại các trung tâm tiêm chủng dịch vụ
        """)
    else:
        st.warning(f"Không có lịch tiêm chủng cho nhóm tuổi: {selected_age}")
    
    # Full schedule overview
    st.markdown("---")
    st.markdown("### 📊 Tổng quan lịch tiêm chủng")
    
    with st.expander("Xem toàn bộ lịch tiêm chủng"):
        for age_group, vaccines in VACCINE_SCHEDULES.items():
            st.markdown(f"#### {age_group}")
            for vaccine_name, schedule_desc in vaccines.items():
                st.markdown(f"- **{vaccine_name}:** {schedule_desc}")
            st.markdown("---")


def render_price_comparison():
    """Render vaccine price comparison"""
    st.markdown("### 💰 Giá cả vắc xin (Tham khảo)")
    st.caption("Giá có thể thay đổi tùy theo cơ sở tiêm chủng và thời điểm")
    
    # Group by price range
    st.markdown("#### 📊 Bảng giá theo mức giá")
    
    price_data = []
    for price_range, vaccines in VACCINE_PRICES.items():
        for vaccine_name in vaccines:
            # Find vaccine info
            vaccine = get_vaccine_by_name(vaccine_name)
            if vaccine:
                price_data.append({
                    "Vắc xin": vaccine.name_vn,
                    "Mức giá": price_range,
                    "Đối tượng": vaccine.target_age,
                    "Phân loại": vaccine.category
                })
    
    if price_data:
        st.dataframe(price_data, use_container_width=True)
    
    # Price by category
    st.markdown("---")
    st.markdown("#### 💉 Vắc xin cho trẻ em")
    
    children_prices = {}
    for vaccine in VACCINES_CHILDREN:
        if vaccine.price_range not in children_prices:
            children_prices[vaccine.price_range] = []
        children_prices[vaccine.price_range].append(vaccine.name_vn)
    
    for price_range, vaccines in sorted(children_prices.items()):
        st.markdown(f"**{price_range}:**")
        for vaccine_name in vaccines:
            st.markdown(f"- {vaccine_name}")
        st.markdown("")
    
    st.markdown("---")
    st.markdown("#### 👨‍⚕️ Vắc xin cho người lớn")
    
    adults_prices = {}
    for vaccine in VACCINES_ADULTS:
        if vaccine.price_range not in adults_prices:
            adults_prices[vaccine.price_range] = []
        adults_prices[vaccine.price_range].append(vaccine.name_vn)
    
    for price_range, vaccines in sorted(adults_prices.items()):
        st.markdown(f"**{price_range}:**")
        for vaccine_name in vaccines:
            st.markdown(f"- {vaccine_name}")
        st.markdown("")
    
    # Important notes
    st.markdown("---")
    st.warning("""
    **⚠️ Lưu ý về giá:**
    - Giá trên chỉ mang tính chất tham khảo
    - Giá thực tế có thể khác nhau tùy theo:
      - Cơ sở tiêm chủng (bệnh viện, trung tâm y tế, phòng khám)
      - Nhà sản xuất và loại vắc xin
      - Thời điểm tiêm
      - Chương trình khuyến mãi (nếu có)
    - Vắc xin trong chương trình TCMR (Tiêm chủng mở rộng) được tiêm miễn phí
    - Nên liên hệ trực tiếp với cơ sở tiêm chủng để biết giá chính xác
    """)


def render_general_info():
    """Render general vaccination information"""
    st.markdown("### 📚 Thông tin chung về tiêm chủng")
    
    st.markdown("""
    #### 🎯 Tầm quan trọng của tiêm chủng
    
    Tiêm chủng là biện pháp hiệu quả nhất để phòng ngừa các bệnh truyền nhiễm nguy hiểm. 
    Tiêm chủng đầy đủ và đúng lịch giúp:
    - Bảo vệ cá nhân khỏi các bệnh truyền nhiễm
    - Tạo miễn dịch cộng đồng (herd immunity)
    - Giảm tỷ lệ mắc bệnh và tử vong
    - Tiết kiệm chi phí điều trị
    
    #### 📋 Chương trình Tiêm chủng mở rộng (TCMR)
    
    Chương trình TCMR của Việt Nam cung cấp miễn phí các vắc xin bắt buộc cho trẻ em:
    - BCG (Lao)
    - Viêm gan B
    - Bạch hầu - Ho gà - Uốn ván (DTP)
    - Bại liệt
    - Sởi - Quai bị - Rubella (MMR)
    - Viêm não Nhật Bản
    
    #### 💉 Vắc xin khuyến nghị
    
    Ngoài các vắc xin bắt buộc, có nhiều vắc xin khuyến nghị giúp bảo vệ tốt hơn:
    - Phế cầu khuẩn
    - Rotavirus
    - Thủy đậu
    - Viêm gan A
    - Não mô cầu
    - Cúm
    - HPV
    
    #### ⚠️ Lưu ý khi tiêm chủng
    
    1. **Trước khi tiêm:**
       - Kiểm tra sức khỏe tổng quát
       - Thông báo tiền sử dị ứng
       - Không tiêm khi sốt cao hoặc bệnh cấp tính
    
    2. **Sau khi tiêm:**
       - Theo dõi tại cơ sở y tế 30 phút
       - Chườm lạnh nếu sưng đỏ tại chỗ tiêm
       - Uống nhiều nước
       - Theo dõi các dấu hiệu bất thường
    
    3. **Phản ứng sau tiêm:**
       - Phản ứng thường gặp: sưng đỏ, sốt nhẹ, quấy khóc (trẻ em)
       - Phản ứng nặng: sốt cao, co giật, phản ứng dị ứng
       - Cần đến ngay cơ sở y tế nếu có dấu hiệu bất thường
    
    #### 📍 Địa điểm tiêm chủng
    
    - **Trạm y tế xã/phường:** Tiêm vắc xin TCMR miễn phí
    - **Trung tâm y tế dự phòng:** Tiêm cả TCMR và dịch vụ
    - **Bệnh viện:** Tiêm dịch vụ, đầy đủ các loại vắc xin
    - **Trung tâm tiêm chủng:** Dịch vụ tiêm chủng toàn diện
    
    #### 📞 Tư vấn
    
    Nếu có thắc mắc về tiêm chủng, vui lòng:
    - Liên hệ bác sĩ hoặc nhân viên y tế
    - Gọi hotline của trung tâm tiêm chủng
    - Tham khảo thông tin từ Bộ Y tế
    """)
    
    st.markdown("---")
    st.info("""
    **ℹ️ Thông tin này chỉ mang tính chất tham khảo.**
    Để có thông tin chính xác và cập nhật nhất, vui lòng liên hệ trực tiếp với cơ sở y tế hoặc bác sĩ.
    """)

