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
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🔍 Tra cứu vắc xin",
        "📅 Lịch tiêm chủng",
        "🛠️ Công cụ tính lịch",
        "⚖️ So sánh vắc xin",
        "💰 Giá cả",
        "📚 Thông tin chung"
    ])
    
    with tab1:
        render_vaccine_search()
    
    with tab2:
        render_schedule_viewer()
    
    with tab3:
        render_schedule_calculator()
    
    with tab4:
        render_vaccine_comparison()
    
    with tab5:
        render_price_comparison()
    
    with tab6:
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
    # Header with key info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"**🏭 Nhà sản xuất:**\n\n{vaccine.manufacturer}")
        st.markdown(f"**📋 Phân loại:**\n\n{vaccine.category}")
    
    with col2:
        st.markdown(f"**💰 Giá tham khảo:**\n\n{vaccine.price_range}")
        st.markdown(f"**👤 Đối tượng:**\n\n{vaccine.target_age}")
    
    with col3:
        st.markdown(f"**📝 Tên khác:**\n\n{vaccine.name}")
        if vaccine.notes:
            st.markdown(f"**📌 Ghi chú:**\n\n{vaccine.notes}")
    
    st.markdown("---")
    
    # Description
    st.markdown("#### 📖 Mô tả")
    st.info(vaccine.description)
    
    # Create tabs for detailed information
    detail_tab1, detail_tab2, detail_tab3, detail_tab4 = st.tabs([
        "✅ Chỉ định & Phác đồ",
        "❌ Chống chỉ định",
        "⚠️ Tác dụng phụ",
        "📋 Thông tin bổ sung"
    ])
    
    with detail_tab1:
        st.markdown("**✅ Chỉ định tiêm:**")
        for indication in vaccine.indications:
            st.markdown(f"• {indication}")
        
        st.markdown("---")
        st.markdown("**📅 Phác đồ tiêm chủng:**")
        
        # Display schedule in a more organized way
        schedule_data = []
        for age, schedule_desc in vaccine.schedule.items():
            schedule_data.append({
                "Độ tuổi/Điều kiện": age,
                "Phác đồ": schedule_desc
            })
        
        if schedule_data:
            st.table(schedule_data)
        
        # Additional schedule notes
        st.markdown("""
        **💡 Lưu ý về phác đồ:**
        - Phác đồ trên là khuyến nghị chung, có thể điều chỉnh theo tình trạng sức khỏe
        - Nếu trễ lịch, không cần bắt đầu lại, chỉ cần tiêm tiếp các mũi còn lại
        - Có thể tiêm nhiều vắc xin cùng ngày nếu cần
        - Nên tham khảo ý kiến bác sĩ để có lịch tiêm phù hợp nhất
        """)
    
    with detail_tab2:
        st.markdown("**❌ Chống chỉ định (Không nên tiêm):**")
        
        if vaccine.contraindications:
            for contraindication in vaccine.contraindications:
                st.markdown(f"• {contraindication}")
        else:
            st.info("Không có chống chỉ định tuyệt đối. Cần đánh giá từng trường hợp cụ thể.")
        
        st.markdown("---")
        st.markdown("""
        **⚠️ Các trường hợp cần thận trọng (Tham khảo ý kiến bác sĩ):**
        - Đang sốt cao (>38.5°C) hoặc bệnh cấp tính nặng
        - Đang dùng thuốc ức chế miễn dịch
        - Có tiền sử phản ứng nặng với vắc xin trước đó
        - Phụ nữ mang thai (đối với vắc xin sống giảm độc lực)
        - Suy giảm miễn dịch (đối với vắc xin sống)
        
        **💡 Lưu ý:** Chỉ có bác sĩ mới có thể quyết định có nên tiêm hay không dựa trên đánh giá toàn diện.
        """)
    
    with detail_tab3:
        st.markdown("**⚠️ Tác dụng phụ có thể gặp:**")
        
        if vaccine.side_effects:
            # Categorize side effects
            st.markdown("**🔴 Phản ứng tại chỗ tiêm (Thường gặp - 50-80%):**")
            local_effects = [e for e in vaccine.side_effects if any(word in e.lower() for word in ['chỗ', 'tại', 'sưng', 'đỏ', 'đau'])]
            if local_effects:
                for effect in local_effects:
                    st.markdown(f"• {effect}")
            else:
                st.markdown("• Đau, sưng, đỏ tại vị trí tiêm")
            
            st.markdown("**🟡 Phản ứng toàn thân (Thường gặp - 10-30%):**")
            systemic_effects = [e for e in vaccine.side_effects if any(word in e.lower() for word in ['sốt', 'mệt', 'đau đầu', 'quấy'])]
            if systemic_effects:
                for effect in systemic_effects:
                    st.markdown(f"• {effect}")
            else:
                st.markdown("• Sốt nhẹ, mệt mỏi, đau đầu")
            
            st.markdown("**🟢 Phản ứng khác:**")
            other_effects = [e for e in vaccine.side_effects if e not in local_effects + systemic_effects]
            if other_effects:
                for effect in other_effects:
                    st.markdown(f"• {effect}")
        else:
            st.info("Vắc xin này thường ít tác dụng phụ. Phản ứng thường gặp: đau tại chỗ tiêm, sốt nhẹ.")
        
        st.markdown("---")
        st.markdown("""
        **📋 Xử trí phản ứng sau tiêm:**
        
        1. **Phản ứng tại chỗ:**
           - Chườm lạnh nếu sưng đỏ
           - Không xoa bóp, không đắp lá thuốc
           - Tự khỏi sau 2-3 ngày
        
        2. **Sốt:**
           - Uống nhiều nước
           - Dùng paracetamol nếu sốt >38.5°C (10-15mg/kg/lần, cách 4-6 giờ)
           - Lau người bằng nước ấm
        
        3. **Khi nào cần đến cơ sở y tế:**
           - Sốt cao >39°C không hạ
           - Co giật
           - Khó thở, tím tái
           - Phát ban lan nhanh
           - Trẻ li bì, khó đánh thức
        """)
    
    with detail_tab4:
        # Additional information based on vaccine type
        st.markdown("**🔬 Thông tin kỹ thuật:**")
        
        # Determine vaccine type
        vaccine_type_info = {
            "BCG": "Vắc xin sống giảm độc lực (Live attenuated). Tiêm trong da.",
            "Hepatitis B": "Vắc xin tái tổ hợp (Recombinant). Tiêm bắp.",
            "DTP": "Vắc xin bất hoạt (Inactivated). Tiêm bắp.",
            "Polio": "Có thể là vắc xin sống (OPV - uống) hoặc bất hoạt (IPV - tiêm).",
            "MMR": "Vắc xin sống giảm độc lực (Live attenuated). Tiêm dưới da.",
            "Pneumococcal": "Vắc xin liên hợp (Conjugate - PCV13) hoặc polysaccharide (PPSV23). Tiêm bắp.",
            "Rotavirus": "Vắc xin sống giảm độc lực (Live attenuated). Uống, không tiêm.",
            "Hib": "Vắc xin liên hợp (Conjugate). Tiêm bắp.",
            "Varicella": "Vắc xin sống giảm độc lực (Live attenuated). Tiêm dưới da.",
            "Hepatitis A": "Vắc xin bất hoạt (Inactivated). Tiêm bắp.",
            "Meningococcal": "Vắc xin liên hợp (Conjugate) hoặc polysaccharide. Tiêm bắp.",
            "Influenza": "Vắc xin bất hoạt (Inactivated) hoặc sống giảm độc lực. Tiêm bắp hoặc xịt mũi.",
            "HPV": "Vắc xin tái tổ hợp (Recombinant). Tiêm bắp.",
            "Tdap/Td": "Vắc xin độc tố (Toxoid). Tiêm bắp.",
            "Shingles": "Vắc xin sống giảm độc lực (Zostavax) hoặc tái tổ hợp (Shingrix). Tiêm bắp.",
            "Typhoid": "Vắc xin bất hoạt (tiêm) hoặc sống giảm độc lực (uống).",
            "Rabies": "Vắc xin bất hoạt (Inactivated). Tiêm bắp."
        }
        
        vaccine_type = vaccine_type_info.get(vaccine.name, "Vắc xin bất hoạt hoặc tái tổ hợp. Tiêm bắp.")
        st.info(vaccine_type)
        
        st.markdown("---")
        st.markdown("**⏱️ Thời gian bảo vệ:**")
        
        protection_duration = {
            "BCG": "10-15 năm, có thể suốt đời",
            "Hepatitis B": "20+ năm, có thể suốt đời nếu đáp ứng tốt",
            "DTP": "10 năm, cần nhắc lại",
            "Polio": "Suốt đời sau khi hoàn thành phác đồ",
            "MMR": "Suốt đời sau 2 mũi",
            "Pneumococcal": "5-10 năm tùy loại",
            "Rotavirus": "Bảo vệ trong 2-3 năm đầu đời",
            "Hib": "5-10 năm",
            "Varicella": "10+ năm, có thể suốt đời",
            "Hepatitis A": "20+ năm",
            "Meningococcal": "3-5 năm, cần nhắc lại",
            "Influenza": "6-12 tháng, cần tiêm hàng năm",
            "HPV": "10+ năm, có thể suốt đời",
            "Tdap/Td": "10 năm, cần nhắc lại",
            "Shingles": "4-5 năm (Shingrix)",
            "Typhoid": "2-3 năm",
            "Rabies": "2-3 năm (tiêm phòng), cần tiêm ngay sau phơi nhiễm"
        }
        
        duration = protection_duration.get(vaccine.name, "Tùy thuộc vào đáp ứng miễn dịch cá nhân")
        st.info(duration)
        
        st.markdown("---")
        st.markdown("**📊 Hiệu quả bảo vệ:**")
        
        efficacy_info = {
            "BCG": "50-80% phòng lao nặng ở trẻ em",
            "Hepatitis B": "95% phòng viêm gan B mạn tính",
            "DTP": "80-95% phòng từng bệnh",
            "Polio": "99% phòng bại liệt",
            "MMR": "97% phòng sởi, 88% phòng quai bị, 97% phòng rubella",
            "Pneumococcal": "60-80% phòng viêm phổi, 90%+ phòng nhiễm trùng xâm lấn",
            "Rotavirus": "85-98% phòng tiêu chảy nặng",
            "Hib": "95%+ phòng nhiễm trùng xâm lấn",
            "Varicella": "90-95% phòng thủy đậu",
            "Hepatitis A": "95%+ phòng viêm gan A",
            "Meningococcal": "85-95% phòng viêm màng não",
            "Influenza": "40-60% phòng cúm (thay đổi theo mùa)",
            "HPV": "90%+ phòng ung thư cổ tử cung và các bệnh do HPV",
            "Tdap/Td": "95%+ phòng uốn ván, bạch hầu",
            "Shingles": "90%+ phòng zona (Shingrix)",
            "Typhoid": "50-80% phòng thương hàn",
            "Rabies": "100% phòng dại nếu tiêm đúng phác đồ"
        }
        
        efficacy = efficacy_info.get(vaccine.name, "Hiệu quả cao, tùy thuộc vào từng cá nhân")
        st.info(efficacy)
        
        st.markdown("---")
        st.markdown("**💉 Tên thương mại (Brand names):**")
        
        if vaccine.brands and len(vaccine.brands) > 0:
            # Create a table for brand information
            brand_data = []
            for brand in vaccine.brands:
                brand_data.append({
                    "Tên thương mại": brand.brand_name,
                    "Nước sản xuất": brand.country,
                    "Nhà sản xuất": brand.manufacturer,
                    "Giá (VNĐ)": brand.price,
                    "Ghi chú": brand.notes if brand.notes else "-"
                })
            
            st.dataframe(brand_data, use_container_width=True)
            
            st.markdown("""
            **💡 Lưu ý về giá:**
            - Giá trên chỉ mang tính chất tham khảo
            - Giá thực tế có thể khác nhau tùy theo:
              - Cơ sở tiêm chủng (bệnh viện, trung tâm y tế, phòng khám)
              - Thời điểm tiêm
              - Chương trình khuyến mãi (nếu có)
            - Nên liên hệ trực tiếp với cơ sở tiêm chủng để biết giá chính xác
            - Vắc xin trong chương trình TCMR được tiêm miễn phí
            """)
        else:
            st.info("Thông tin về các tên thương mại cụ thể đang được cập nhật. Vui lòng tham khảo thông tin từ cơ sở tiêm chủng.")
        
        st.markdown("---")
        st.markdown("**🔗 Tương tác với vắc xin khác:**")
        st.info("""
        - Có thể tiêm cùng ngày với các vắc xin khác
        - Vắc xin sống nên tiêm cùng ngày hoặc cách nhau ít nhất 4 tuần
        - Vắc xin bất hoạt có thể tiêm bất kỳ lúc nào
        - Nên tham khảo ý kiến bác sĩ khi tiêm nhiều vắc xin cùng lúc
        """)


def render_schedule_viewer():
    """Render vaccination schedule viewer"""
    st.markdown("### 📅 Lịch tiêm chủng")
    
    # View mode selector
    view_mode = st.radio(
        "Chế độ xem:",
        ["Theo nhóm tuổi", "Timeline đầy đủ"],
        horizontal=True,
        key="schedule_view_mode"
    )
    
    if view_mode == "Theo nhóm tuổi":
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
            st.markdown(f"#### 📋 Lịch tiêm chủng cho: {selected_age}")
            
            # Create a table with more details
            schedule_data = []
            for vaccine_name, schedule_desc in schedule.items():
                # Find vaccine info
                vaccine = get_vaccine_by_name(vaccine_name)
                if vaccine:
                    category = vaccine.category
                    price = vaccine.price_range
                    target_age = "Trẻ em" if vaccine.target_age == "children" else "Người lớn" if vaccine.target_age == "adults" else "Cả hai"
                else:
                    category = "N/A"
                    price = "N/A"
                    target_age = "N/A"
                
                schedule_data.append({
                    "Vắc xin": vaccine_name,
                    "Phác đồ": schedule_desc,
                    "Phân loại": category,
                    "Đối tượng": target_age,
                    "Giá tham khảo": price
                })
            
            st.dataframe(schedule_data, use_container_width=True)
            
            # Show vaccine details in expanders
            st.markdown("---")
            st.markdown("#### 💉 Chi tiết các vắc xin")
            
            for vaccine_name, schedule_desc in schedule.items():
                vaccine = get_vaccine_by_name(vaccine_name)
                if vaccine:
                    with st.expander(f"📌 {vaccine.name_vn} ({vaccine_name})"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"**Nhà sản xuất:** {vaccine.manufacturer}")
                            st.markdown(f"**Phân loại:** {vaccine.category}")
                            st.markdown(f"**Giá:** {vaccine.price_range}")
                        with col2:
                            st.markdown(f"**Mô tả:** {vaccine.description}")
                            if vaccine.notes:
                                st.markdown(f"**Ghi chú:** {vaccine.notes}")
            
            # Additional info
            st.markdown("---")
            st.info("""
            **💡 Lưu ý:**
            - Lịch tiêm có thể thay đổi tùy theo tình trạng sức khỏe và chỉ định của bác sĩ
            - Vắc xin bắt buộc (TCMR) được tiêm miễn phí tại các trạm y tế
            - Vắc xin khuyến nghị có thể tiêm tại các trung tâm tiêm chủng dịch vụ
            - Có thể tiêm nhiều vắc xin cùng ngày nếu cần
            - Nếu trễ lịch, không cần bắt đầu lại, chỉ cần tiêm tiếp các mũi còn lại
            """)
        else:
            st.warning(f"Không có lịch tiêm chủng cho nhóm tuổi: {selected_age}")
    
    else:
        # Timeline view
        st.markdown("#### 📊 Timeline lịch tiêm chủng đầy đủ")
        st.markdown("Lịch tiêm chủng từ sơ sinh đến người lớn")
        
        # Organize by chronological order
        timeline_order = [
            "Trẻ sơ sinh (0-1 tháng)",
            "Trẻ 2 tháng",
            "Trẻ 3 tháng",
            "Trẻ 4 tháng",
            "Trẻ 6 tháng",
            "Trẻ 9 tháng",
            "Trẻ 12 tháng",
            "Trẻ 18 tháng",
            "Trẻ 24 tháng",
            "Trẻ 4-6 tuổi",
            "Trẻ 9-14 tuổi",
            "Người lớn"
        ]
        
        for age_group in timeline_order:
            if age_group in VACCINE_SCHEDULES:
                schedule = VACCINE_SCHEDULES[age_group]
                if schedule:
                    with st.expander(f"📅 {age_group} - {len(schedule)} vắc xin", expanded=False):
                        for vaccine_name, schedule_desc in schedule.items():
                            vaccine = get_vaccine_by_name(vaccine_name)
                            if vaccine:
                                category_badge = "🟢 Bắt buộc" if vaccine.category == "Bắt buộc" else "🔵 Khuyến nghị"
                                st.markdown(f"**{vaccine.name_vn}** ({vaccine_name}) {category_badge}")
                                st.markdown(f"  → {schedule_desc}")
                                st.markdown(f"  💰 {vaccine.price_range}")
                            else:
                                st.markdown(f"**{vaccine_name}**")
                                st.markdown(f"  → {schedule_desc}")
                            st.markdown("")
        
        st.markdown("---")
        st.markdown("""
        **📌 Hướng dẫn đọc timeline:**
        - 🟢 Bắt buộc: Vắc xin trong chương trình TCMR, tiêm miễn phí
        - 🔵 Khuyến nghị: Vắc xin dịch vụ, nên tiêm để bảo vệ tốt hơn
        - Timeline này chỉ là khuyến nghị chung, lịch cụ thể cần được bác sĩ tư vấn
        """)


def render_vaccine_comparison():
    """Render vaccine comparison tool"""
    st.markdown("### ⚖️ So sánh vắc xin")
    st.markdown("So sánh các vắc xin để lựa chọn phù hợp nhất")
    
    # Select vaccines to compare
    vaccine_options = {f"{v.name_vn} ({v.name})": v for v in ALL_VACCINES}
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected_vaccine1 = st.selectbox(
            "Chọn vắc xin thứ nhất:",
            list(vaccine_options.keys()),
            key="compare_vaccine1"
        )
        vaccine1 = vaccine_options[selected_vaccine1]
    
    with col2:
        selected_vaccine2 = st.selectbox(
            "Chọn vắc xin thứ hai:",
            list(vaccine_options.keys()),
            key="compare_vaccine2"
        )
        vaccine2 = vaccine_options[selected_vaccine2]
    
    if vaccine1.name == vaccine2.name:
        st.warning("Vui lòng chọn 2 vắc xin khác nhau để so sánh.")
    else:
        st.markdown("---")
        st.markdown("### 📊 Bảng so sánh")
        
        # Create comparison table
        comparison_data = {
            "Tiêu chí": [
                "Tên vắc xin",
                "Phân loại",
                "Đối tượng",
                "Nhà sản xuất",
                "Giá tham khảo",
                "Số mũi tiêm",
                "Khoảng cách giữa các mũi",
                "Tác dụng phụ thường gặp"
            ],
            vaccine1.name_vn: [
                vaccine1.name_vn,
                vaccine1.category,
                vaccine1.target_age,
                vaccine1.manufacturer,
                vaccine1.price_range,
                len(vaccine1.schedule),
                "Xem phác đồ chi tiết",
                ", ".join(vaccine1.side_effects[:3]) if vaccine1.side_effects else "Ít tác dụng phụ"
            ],
            vaccine2.name_vn: [
                vaccine2.name_vn,
                vaccine2.category,
                vaccine2.target_age,
                vaccine2.manufacturer,
                vaccine2.price_range,
                len(vaccine2.schedule),
                "Xem phác đồ chi tiết",
                ", ".join(vaccine2.side_effects[:3]) if vaccine2.side_effects else "Ít tác dụng phụ"
            ]
        }
        
        st.dataframe(comparison_data, use_container_width=True)
        
        # Detailed comparison
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"#### {vaccine1.name_vn}")
            st.markdown(f"**Mô tả:** {vaccine1.description}")
            st.markdown("**Chỉ định:**")
            for ind in vaccine1.indications:
                st.markdown(f"- {ind}")
            if vaccine1.brands:
                st.markdown("**Tên thương mại:**")
                for brand in vaccine1.brands[:3]:
                    st.markdown(f"- {brand.brand_name} ({brand.country}) - {brand.price}")
        
        with col2:
            st.markdown(f"#### {vaccine2.name_vn}")
            st.markdown(f"**Mô tả:** {vaccine2.description}")
            st.markdown("**Chỉ định:**")
            for ind in vaccine2.indications:
                st.markdown(f"- {ind}")
            if vaccine2.brands:
                st.markdown("**Tên thương mại:**")
                for brand in vaccine2.brands[:3]:
                    st.markdown(f"- {brand.brand_name} ({brand.country}) - {brand.price}")
        
        st.markdown("---")
        st.info("""
        **💡 Lưu ý khi so sánh:**
        - So sánh trên chỉ mang tính chất tham khảo
        - Việc lựa chọn vắc xin nên dựa trên tư vấn của bác sĩ
        - Cần xem xét tình trạng sức khỏe, độ tuổi, và lịch tiêm chủng hiện tại
        - Giá cả có thể thay đổi tùy theo cơ sở tiêm chủng
        """)
    
    # Special comparison: 5-in-1 vs 6-in-1 vs DTP riêng lẻ
    st.markdown("---")
    st.markdown("### 💡 So sánh đặc biệt: Vắc xin kết hợp vs Vắc xin riêng lẻ")
    
    with st.expander("📋 Vắc xin 5-in-1 và 6-in-1"):
        st.markdown("""
        **Ưu điểm của vắc xin kết hợp (5-in-1, 6-in-1):**
        - ✅ Giảm số lần tiêm (từ 5-6 mũi xuống còn 1 mũi)
        - ✅ Giảm đau đớn cho trẻ
        - ✅ Tiết kiệm thời gian đi lại
        - ✅ Giảm nguy cơ quên mũi tiêm
        - ✅ Ho gà vô bào (trong một số loại) ít phản ứng phụ hơn
        
        **Nhược điểm:**
        - ❌ Giá cao hơn vắc xin riêng lẻ
        - ❌ Không có trong chương trình TCMR (phải trả phí)
        - ❌ Một số trẻ có thể phản ứng với nhiều kháng nguyên cùng lúc
        
        **Khi nào nên chọn vắc xin kết hợp:**
        - Gia đình có điều kiện kinh tế
        - Muốn giảm số lần tiêm cho trẻ
        - Trẻ khỏe mạnh, không có chống chỉ định
        - Muốn sử dụng vắc xin ho gà vô bào (ít phản ứng phụ)
        
        **Khi nào nên chọn vắc xin riêng lẻ:**
        - Muốn tiết kiệm chi phí
        - Trẻ có phản ứng với vắc xin kết hợp trước đó
        - Cần linh hoạt trong lịch tiêm
        """)
    
    with st.expander("📋 Vắc xin 5-in-1 vs 6-in-1"):
        st.markdown("""
        **Vắc xin 5-in-1:**
        - Phòng: Bạch hầu, Ho gà, Uốn ván, Bại liệt, Hib
        - Giá: 600.000 - 800.000 VNĐ/mũi
        - Phù hợp: Khi đã tiêm viêm gan B riêng hoặc muốn tiết kiệm hơn
        
        **Vắc xin 6-in-1:**
        - Phòng: Bạch hầu, Ho gà, Uốn ván, Bại liệt, Hib, Viêm gan B
        - Giá: 800.000 - 1.000.000 VNĐ/mũi
        - Phù hợp: Muốn tiêm đầy đủ nhất trong 1 mũi, tiện lợi tối đa
        
        **Khuyến nghị:**
        - Nếu chưa tiêm viêm gan B: Chọn 6-in-1
        - Nếu đã tiêm viêm gan B: Có thể chọn 5-in-1 để tiết kiệm
        - Nên tham khảo ý kiến bác sĩ để quyết định
        """)


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
    st.markdown("### 📚 Thông tin chung về tiêm chủng và vắc xin")
    
    # Create tabs for different topics
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "🎯 Tổng quan",
        "🔬 Cơ chế & Phân loại",
        "⚠️ Phản ứng & Xử trí",
        "📅 Lịch tiêm chi tiết",
        "👥 Nhóm đặc biệt",
        "✈️ Vắc xin du lịch",
        "❄️ Bảo quản vắc xin",
        "❓ Câu hỏi thường gặp",
        "📖 Nguồn thông tin"
    ])
    
    with tab1:
        st.markdown("""
        #### 🎯 Tầm quan trọng của tiêm chủng
        
        Tiêm chủng là biện pháp hiệu quả nhất để phòng ngừa các bệnh truyền nhiễm nguy hiểm. 
        Tiêm chủng đầy đủ và đúng lịch giúp:
        - **Bảo vệ cá nhân:** Giảm nguy cơ mắc bệnh và biến chứng nặng
        - **Miễn dịch cộng đồng (Herd Immunity):** Khi tỷ lệ tiêm chủng đạt 80-95%, bệnh khó lây lan, bảo vệ cả những người chưa thể tiêm
        - **Giảm tỷ lệ tử vong:** Nhiều bệnh đã được thanh toán hoặc giảm đáng kể nhờ tiêm chủng
        - **Tiết kiệm chi phí:** Chi phí tiêm chủng thấp hơn nhiều so với điều trị bệnh
        
        #### 📋 Chương trình Tiêm chủng mở rộng (TCMR) tại Việt Nam
        
        Chương trình TCMR của Việt Nam được triển khai từ năm 1985, cung cấp miễn phí các vắc xin bắt buộc cho trẻ em:
        
        **Vắc xin trong chương trình TCMR:**
        - **BCG:** Phòng lao, tiêm ngay sau sinh
        - **Viêm gan B:** Phòng viêm gan B, mũi đầu trong 24h sau sinh
        - **DTP:** Phòng bạch hầu, ho gà, uốn ván (3 trong 1)
        - **Bại liệt (OPV/IPV):** Phòng bại liệt, có thể uống hoặc tiêm
        - **Sởi - Quai bị - Rubella (MMR):** Phòng 3 bệnh
        - **Viêm não Nhật Bản:** Phòng viêm não do virus JEV
        
        **Đối tượng:** Trẻ em từ 0-5 tuổi tại tất cả các địa phương
        
        #### 💉 Vắc xin khuyến nghị (Dịch vụ)
        
        Ngoài các vắc xin bắt buộc, có nhiều vắc xin khuyến nghị giúp bảo vệ toàn diện hơn:
        
        **Cho trẻ em:**
        - Phế cầu khuẩn (Prevenar 13, Synflorix)
        - Rotavirus (Rotarix, Rotateq)
        - Thủy đậu (Varicella)
        - Viêm gan A
        - Não mô cầu (Meningococcal)
        - Cúm (Influenza)
        - HPV (từ 9 tuổi)
        
        **Cho người lớn:**
        - Cúm (hàng năm)
        - Phế cầu (≥65 tuổi)
        - Zona (≥50 tuổi)
        - Tdap/Td (nhắc lại mỗi 10 năm)
        - Viêm gan A, B (nếu chưa tiêm)
        - HPV (đến 26-45 tuổi tùy chỉ định)
        """)
    
    with tab2:
        st.markdown("""
        #### 🔬 Cơ chế hoạt động của vắc xin
        
        Vắc xin hoạt động bằng cách "dạy" hệ thống miễn dịch nhận biết và chống lại mầm bệnh:
        
        1. **Kích thích miễn dịch:** Vắc xin chứa kháng nguyên (mầm bệnh đã làm yếu hoặc bất hoạt) hoặc thành phần của mầm bệnh
        2. **Tạo kháng thể:** Cơ thể sản xuất kháng thể đặc hiệu chống lại mầm bệnh
        3. **Ghi nhớ miễn dịch:** Tế bào nhớ được tạo ra, giúp cơ thể phản ứng nhanh khi gặp mầm bệnh thật
        4. **Bảo vệ lâu dài:** Khi nhiễm bệnh thật, hệ miễn dịch đã sẵn sàng tiêu diệt mầm bệnh
        
        #### 📦 Phân loại vắc xin
        
        **1. Vắc xin sống giảm độc lực (Live attenuated vaccines)**
        - Chứa vi khuẩn/virus sống đã được làm yếu
        - Tạo miễn dịch mạnh và lâu dài
        - Thường chỉ cần 1-2 liều
        - Ví dụ: BCG, MMR, Thủy đậu, Rotavirus (uống)
        - Lưu ý: Không dùng cho người suy giảm miễn dịch nặng, phụ nữ mang thai
        
        **2. Vắc xin bất hoạt (Inactivated vaccines)**
        - Chứa vi khuẩn/virus đã chết hoàn toàn
        - An toàn hơn vắc xin sống
        - Thường cần nhiều liều và nhắc lại
        - Ví dụ: Bại liệt (IPV), Cúm, Viêm gan A, Ho gà (acellular)
        
        **3. Vắc xin tái tổ hợp (Recombinant vaccines)**
        - Chứa protein hoặc thành phần của mầm bệnh được sản xuất bằng công nghệ gen
        - An toàn, hiệu quả cao
        - Ví dụ: Viêm gan B, HPV
        
        **4. Vắc xin polysaccharide (Polysaccharide vaccines)**
        - Chứa đường (polysaccharide) từ vỏ vi khuẩn
        - Ví dụ: Phế cầu (PPSV23), Não mô cầu
        
        **5. Vắc xin liên hợp (Conjugate vaccines)**
        - Polysaccharide gắn với protein để tăng hiệu quả
        - Đặc biệt tốt cho trẻ nhỏ
        - Ví dụ: Phế cầu (PCV13), Hib, Não mô cầu
        
        **6. Vắc xin độc tố (Toxoid vaccines)**
        - Chứa độc tố đã được làm mất độc tính
        - Ví dụ: Uốn ván, Bạch hầu
        
        #### 🧪 Công nghệ vắc xin mới
        
        - **Vắc xin mRNA:** Sử dụng RNA thông tin để tạo protein kháng nguyên (ví dụ: COVID-19)
        - **Vắc xin vector virus:** Sử dụng virus vô hại làm "xe" mang gen kháng nguyên
        - **Vắc xin peptide:** Chứa các đoạn protein nhỏ của mầm bệnh
        """)
    
    with tab3:
        st.markdown("""
        #### ⚠️ Phản ứng sau tiêm chủng
        
        **1. Phản ứng tại chỗ tiêm (Thường gặp - 50-80%)**
        - Đau, sưng, đỏ tại vị trí tiêm
        - Xuất hiện trong 24-48 giờ đầu
        - Tự khỏi sau 2-3 ngày
        - **Xử trí:** Chườm lạnh, không xoa bóp, có thể dùng paracetamol nếu đau nhiều
        
        **2. Phản ứng toàn thân nhẹ (Thường gặp - 10-30%)**
        - Sốt nhẹ (<38.5°C)
        - Mệt mỏi, đau đầu
        - Quấy khóc (trẻ em)
        - Chán ăn tạm thời
        - **Xử trí:** Nghỉ ngơi, uống nhiều nước, dùng paracetamol nếu sốt >38.5°C
        
        **3. Phản ứng trung bình (Ít gặp - 1-5%)**
        - Sốt cao (38.5-39.5°C)
        - Sưng đỏ lan rộng (>5cm)
        - Nôn, tiêu chảy
        - Phát ban nhẹ
        - **Xử trí:** Dùng thuốc hạ sốt, theo dõi sát, liên hệ bác sĩ nếu không cải thiện
        
        **4. Phản ứng nặng (Rất hiếm - <0.1%)**
        - Sốt cao >39.5°C kéo dài
        - Co giật do sốt
        - Phản ứng dị ứng nặng (sốc phản vệ)
        - Khó thở, tím tái
        - **Xử trí:** Đến ngay cơ sở y tế gần nhất
        
        #### 🚨 Dấu hiệu cần đến cơ sở y tế ngay
        
        - Sốt cao >39°C không hạ sau dùng thuốc
        - Co giật
        - Khó thở, thở nhanh
        - Tím tái, da xanh
        - Phát ban lan nhanh, nổi mề đay
        - Sưng nề nhiều, đau dữ dội
        - Nôn nhiều, không uống được
        - Trẻ li bì, khó đánh thức
        - Quấy khóc kéo dài >3 giờ
        
        #### 📋 Quy trình an toàn khi tiêm
        
        **Trước khi tiêm:**
        1. Khám sàng lọc sức khỏe
        2. Đo nhiệt độ, huyết áp (nếu cần)
        3. Khai báo đầy đủ:
           - Tiền sử dị ứng (thuốc, thức ăn, vắc xin trước)
           - Bệnh mạn tính đang điều trị
           - Thuốc đang dùng (đặc biệt thuốc ức chế miễn dịch)
           - Tình trạng mang thai
           - Phản ứng với vắc xin trước đó
        
        **Trong khi tiêm:**
        - Kiểm tra tên vắc xin, hạn sử dụng, lô sản xuất
        - Tiêm đúng kỹ thuật, đúng vị trí
        - Bảo quản vắc xin đúng nhiệt độ (2-8°C)
        
        **Sau khi tiêm:**
        - Theo dõi tại cơ sở y tế tối thiểu 30 phút
        - Ghi nhận vào sổ tiêm chủng
        - Hướng dẫn chăm sóc tại nhà
        - Cung cấp số điện thoại hỗ trợ 24/7
        
        #### 🏠 Chăm sóc tại nhà sau tiêm
        
        1. **Vị trí tiêm:**
           - Không xoa bóp, không đắp lá thuốc
           - Có thể chườm lạnh nếu sưng đỏ
           - Giữ sạch, khô ráo
           - Mặc quần áo rộng rãi
        
        2. **Sốt:**
           - Uống nhiều nước
           - Dùng paracetamol theo liều khuyến nghị (10-15mg/kg/lần, cách 4-6 giờ)
           - Lau người bằng nước ấm
           - Không dùng aspirin cho trẻ <18 tuổi
        
        3. **Dinh dưỡng:**
           - Ăn uống bình thường, đủ chất
           - Cho trẻ bú mẹ nhiều hơn nếu đang bú
           - Tránh thức ăn dễ dị ứng trong 24h đầu
        
        4. **Vận động:**
           - Nghỉ ngơi, tránh vận động mạnh trong 24h đầu
           - Tắm rửa bình thường, tránh chà xát vị trí tiêm
        """)
    
    with tab4:
        st.markdown("""
        #### 📅 Lịch tiêm chủng chi tiết theo độ tuổi
        
        **TRẺ SƠ SINH (0-1 tháng)**
        - **BCG:** 1 mũi ngay sau sinh hoặc trong tháng đầu
        - **Viêm gan B:** Mũi 1 trong 24 giờ đầu sau sinh
        
        **TRẺ 2 THÁNG**
        - Viêm gan B: Mũi 2
        - DTP: Mũi 1
        - Bại liệt (OPV/IPV): Liều 1
        - Hib: Mũi 1 (nếu tiêm dịch vụ)
        - Phế cầu: Mũi 1 (nếu tiêm dịch vụ)
        - Rotavirus: Mũi 1 (nếu tiêm dịch vụ)
        
        **TRẺ 3 THÁNG**
        - DTP: Mũi 2
        - Bại liệt: Liều 2
        - Hib: Mũi 2 (nếu tiêm dịch vụ)
        - Phế cầu: Mũi 2 (nếu tiêm dịch vụ)
        - Rotavirus: Mũi 2 (nếu tiêm dịch vụ)
        
        **TRẺ 4 THÁNG**
        - DTP: Mũi 3
        - Bại liệt: Liều 3
        - Hib: Mũi 3 (nếu tiêm dịch vụ)
        - Phế cầu: Mũi 3 (nếu tiêm dịch vụ)
        - Rotavirus: Mũi 3 (nếu Rotateq)
        
        **TRẺ 6 THÁNG**
        - Viêm gan B: Mũi 3
        - Cúm: Mũi 1 (nếu mùa cúm, lần đầu tiêm cần 2 mũi cách 1 tháng)
        
        **TRẺ 9 THÁNG**
        - Sởi: Mũi 1 (hoặc MMR nếu tiêm dịch vụ)
        
        **TRẺ 12 THÁNG**
        - Viêm não Nhật Bản: Mũi 1
        - Viêm gan A: Mũi 1 (nếu tiêm dịch vụ)
        - Thủy đậu: Mũi 1 (nếu tiêm dịch vụ)
        - Não mô cầu: Mũi 1 (nếu có nguy cơ)
        
        **TRẺ 13 THÁNG**
        - Viêm não Nhật Bản: Mũi 2 (cách mũi 1: 1-2 tuần)
        
        **TRẺ 18 THÁNG**
        - DTP: Mũi 4 (nhắc lại)
        - Bại liệt: Liều 4 (nhắc lại)
        - MMR: Mũi 2
        - Hib: Mũi nhắc lại (nếu đã tiêm)
        - Phế cầu: Mũi nhắc lại (nếu đã tiêm)
        
        **TRẺ 24 THÁNG**
        - Viêm não Nhật Bản: Mũi 3 (nhắc lại)
        - Viêm gan A: Mũi 2 (nếu đã tiêm mũi 1)
        
        **TRẺ 4-6 TUỔI**
        - Thủy đậu: Mũi 2 (nếu đã tiêm mũi 1)
        - DTP: Mũi 5 (nhắc lại)
        - MMR: Mũi 3 (nhắc lại)
        
        **TRẺ 9-14 TUỔI**
        - HPV: 2 mũi (cách 6 tháng) - ưu tiên cho trẻ 9-14 tuổi
        
        **THANH THIẾU NIÊN 15-18 TUỔI**
        - HPV: 3 mũi (0, 2, 6 tháng) nếu chưa tiêm
        - Tdap: 1 mũi nhắc lại
        - Cúm: Hàng năm
        
        **NGƯỜI LỚN (≥19 TUỔI)**
        - **Cúm:** 1 mũi hàng năm (tốt nhất tháng 9-11)
        - **Tdap:** 1 mũi, sau đó Td mỗi 10 năm
        - **Phế cầu:** PCV13 + PPSV23 (nếu ≥65 tuổi hoặc có bệnh mạn tính)
        - **Zona:** 2 mũi (nếu ≥50 tuổi)
        - **Viêm gan A, B:** Nếu chưa tiêm hoặc chưa có kháng thể
        - **MMR:** Nếu chưa tiêm đủ hoặc không có miễn dịch
        - **Thủy đậu:** Nếu chưa mắc và chưa tiêm
        - **HPV:** Đến 26 tuổi (nữ), 21 tuổi (nam), hoặc đến 45 tuổi nếu có chỉ định
        
        #### ⏰ Nguyên tắc về khoảng cách giữa các mũi tiêm
        
        - **Vắc xin cùng loại:** Tuân thủ khoảng cách tối thiểu giữa các liều
        - **Vắc xin khác loại:** Có thể tiêm cùng ngày hoặc cách nhau bất kỳ
        - **Nếu trễ lịch:** Không cần bắt đầu lại từ đầu, chỉ cần tiêm tiếp các mũi còn lại
        - **Tiêm nhiều mũi cùng lúc:** An toàn và được khuyến nghị để giảm số lần đến cơ sở y tế
        """)
    
    with tab5:
        st.markdown("""
        #### 👥 Tiêm chủng cho các nhóm đặc biệt
        
        **🤰 PHỤ NỮ MANG THAI**
        
        **Vắc xin được khuyến nghị:**
        - **Cúm:** Tiêm bất kỳ giai đoạn nào của thai kỳ, tốt nhất trước mùa cúm
        - **Tdap:** Tiêm mỗi lần mang thai, tốt nhất tuần 27-36, để truyền kháng thể cho con
        - **Viêm gan B:** Nếu chưa có miễn dịch và có nguy cơ cao
        
        **Vắc xin chống chỉ định:**
        - Vắc xin sống giảm độc lực: MMR, Thủy đậu, BCG
        - HPV (chưa có dữ liệu đầy đủ)
        
        **Lưu ý:**
        - Tiêm vắc xin trong thai kỳ an toàn và bảo vệ cả mẹ và con
        - Kháng thể từ mẹ truyền qua nhau thai bảo vệ trẻ trong 6 tháng đầu
        
        **👴 NGƯỜI CAO TUỔI (≥65 TUỔI)**
        
        **Vắc xin được khuyến nghị:**
        - **Cúm:** Hàng năm (ưu tiên cao)
        - **Phế cầu:** PCV13 (nếu chưa tiêm) + PPSV23 sau 1 năm
        - **Zona:** 2 mũi Shingrix (≥50 tuổi)
        - **Tdap/Td:** Nhắc lại mỗi 10 năm
        
        **Lưu ý:**
        - Người già dễ mắc bệnh và biến chứng nặng hơn
        - Đáp ứng miễn dịch có thể kém hơn người trẻ nhưng vẫn có hiệu quả bảo vệ
        
        **🏥 NGƯỜI CÓ BỆNH MẠN TÍNH**
        
        **Bệnh tim mạch, phổi, thận, gan:**
        - Cúm: Hàng năm (ưu tiên cao)
        - Phế cầu: PCV13 + PPSV23
        - Viêm gan A, B: Nếu có nguy cơ
        
        **Đái tháo đường:**
        - Cúm: Hàng năm
        - Phế cầu: PCV13 + PPSV23
        - Viêm gan B: Nếu chưa tiêm
        
        **Suy giảm miễn dịch (HIV, ung thư, ghép tạng):**
        - Cần tư vấn bác sĩ chuyên khoa
        - Tránh vắc xin sống giảm độc lực
        - Có thể cần liều cao hơn hoặc lịch khác
        - Cúm, Phế cầu: Rất quan trọng
        
        **Bệnh tự miễn (Lupus, viêm khớp dạng thấp):**
        - Có thể tiêm vắc xin khi bệnh ổn định
        - Tránh tiêm khi đang dùng liều cao thuốc ức chế miễn dịch
        - Cúm, Phế cầu: Được khuyến nghị
        
        **👶 TRẺ SINH NON, NHẸ CÂN**
        
        - Tiêm đúng lịch theo tuổi thực (không tính tuổi điều chỉnh)
        - Viêm gan B: Tiêm ngay sau sinh bất kể cân nặng
        - BCG: Có thể hoãn nếu cân nặng <2kg
        - Rotavirus: Có thể tiêm từ 6 tuần tuổi nếu trẻ ổn định
        
        **🚫 NGƯỜI SUY GIẢM MIỄN DỊCH NẶNG**
        
        - **Tránh vắc xin sống:** MMR, Thủy đậu, BCG, Rotavirus (uống)
        - **Có thể dùng vắc xin bất hoạt:** Cúm, Phế cầu, Viêm gan A/B
        - Cần tư vấn bác sĩ chuyên khoa miễn dịch
        - Có thể cần xét nghiệm kháng thể sau tiêm
        
        **💊 NGƯỜI ĐANG DÙNG THUỐC**
        
        **Corticosteroid liều cao (>20mg/ngày prednisone >2 tuần):**
        - Tránh vắc xin sống
        - Có thể tiêm vắc xin bất hoạt
        
        **Thuốc ức chế miễn dịch (chemotherapy, rituximab, v.v.):**
        - Tránh vắc xin sống
        - Nên tiêm trước khi bắt đầu điều trị nếu có thể
        - Tiêm vắc xin bất hoạt khi bệnh ổn định
        
        **Kháng sinh:**
        - Không ảnh hưởng đến hiệu quả vắc xin (trừ vắc xin sống uống như Rotavirus, có thể cần cách 2 tuần)
        """)
    
    with tab6:
        st.markdown("""
        #### ✈️ Vắc xin cho người đi du lịch
        
        Việc tiêm vắc xin trước khi đi du lịch phụ thuộc vào:
        - Điểm đến
        - Thời gian lưu trú
        - Loại hình du lịch (thành phố, nông thôn, rừng núi)
        - Tình trạng sức khỏe cá nhân
        
        **🌍 Vắc xin theo khu vực địa lý**
        
        **Châu Á:**
        - Viêm gan A, B: Nếu chưa tiêm
        - Cúm: Hàng năm
        - Viêm não Nhật Bản: Vùng nông thôn, mùa mưa
        - Thương hàn: Vùng có dịch
        - Tả: Một số vùng (thường không bắt buộc)
        - Sốt vàng da: Không cần (chỉ cần ở châu Phi, Nam Mỹ)
        
        **Châu Phi:**
        - Sốt vàng da: **Bắt buộc** ở nhiều nước (cần giấy chứng nhận)
        - Viêm gan A, B
        - Thương hàn
        - Viêm màng não do não mô cầu: Vùng "vành đai viêm màng não" (Sahel)
        - Sốt rét: Dùng thuốc phòng (không có vắc xin)
        - Dại: Nếu ở lâu hoặc vùng sâu vùng xa
        
        **Nam Mỹ, Trung Mỹ:**
        - Sốt vàng da: Một số nước bắt buộc
        - Viêm gan A, B
        - Thương hàn
        - Dại: Vùng có nguy cơ
        
        **Châu Âu, Bắc Mỹ, Úc:**
        - Viêm gan A, B: Nếu chưa tiêm
        - Cúm: Theo mùa
        - Các vắc xin thông thường khác
        
        **📋 Vắc xin du lịch phổ biến**
        
        **1. Viêm gan A**
        - Chỉ định: Hầu hết các nước đang phát triển
        - Lịch: 2 mũi (cách 6-12 tháng)
        - Bảo vệ: >95%, kéo dài 20+ năm
        
        **2. Thương hàn**
        - Chỉ định: Vùng có dịch (Ấn Độ, Đông Nam Á, châu Phi, Nam Mỹ)
        - Loại: Tiêm (1 mũi) hoặc uống (4 viên)
        - Bảo vệ: 50-80%, nhắc lại sau 3 năm
        
        **3. Viêm màng não do não mô cầu**
        - Chỉ định: Vùng dịch (Sahel châu Phi, một số nước Ả Rập)
        - Lịch: 1 mũi, nhắc lại sau 3-5 năm
        - Bắt buộc: Một số nước yêu cầu giấy chứng nhận
        
        **4. Sốt vàng da**
        - Chỉ định: Châu Phi, Nam Mỹ
        - Lịch: 1 mũi, bảo vệ suốt đời
        - Bắt buộc: Cần giấy chứng nhận quốc tế (Yellow Card)
        - Chỉ tiêm tại trung tâm được WHO cấp phép
        
        **5. Dại**
        - Chỉ định: Vùng có nguy cơ cao, ở lâu, đi rừng
        - Lịch tiêm phòng: 3 mũi (0, 7, 21-28 ngày)
        - Lợi ích: Nếu bị cắn, chỉ cần 2 mũi nhắc lại thay vì 4-5 mũi + huyết thanh
        
        **6. Viêm não Nhật Bản**
        - Chỉ định: Vùng nông thôn châu Á, mùa mưa
        - Lịch: 2 mũi (cách 1-2 tuần), nhắc lại sau 1-2 năm
        
        **7. Tả**
        - Chỉ định: Vùng có dịch, nhân đạo
        - Lịch: 2 liều uống (cách 1-2 tuần)
        - Hiệu quả: 60-85%
        
        **⏰ Thời gian chuẩn bị**
        
        - **Tối thiểu 4-6 tuần** trước khi đi để hoàn thành các mũi tiêm
        - Một số vắc xin cần nhiều mũi cách nhau
        - Nên tư vấn tại phòng khám du lịch hoặc trung tâm y tế dự phòng
        
        **📄 Giấy tờ cần thiết**
        
        - Sổ tiêm chủng quốc tế (International Certificate of Vaccination)
        - Giấy chứng nhận sốt vàng da (Yellow Card) - bắt buộc ở một số nước
        - Giấy chứng nhận viêm màng não - một số nước yêu cầu
        
        **💡 Lưu ý khác**
        
        - Tiêm các vắc xin thông thường (Cúm, Tdap) trước khi đi
        - Mang theo thuốc phòng sốt rét nếu cần
        - Chuẩn bị bộ sơ cứu cá nhân
        - Mua bảo hiểm du lịch
        - Tìm hiểu về dịch vụ y tế tại điểm đến
        """)
    
    with tab7:
        st.markdown("""
        #### ❄️ Bảo quản vắc xin
        
        Bảo quản đúng cách là yếu tố quan trọng để đảm bảo hiệu quả và an toàn của vắc xin.
        
        **🌡️ Nhiệt độ bảo quản:**
        
        **Hầu hết vắc xin:**
        - Nhiệt độ: **2-8°C** (tủ lạnh)
        - Không được đông đá
        - Không được để ở nhiệt độ phòng quá lâu
        - Theo dõi nhiệt độ liên tục bằng nhiệt kế
        
        **Một số vắc xin đặc biệt:**
        - **Vắc xin sống (MMR, Thủy đậu):** 2-8°C, có thể bảo quản ở -20°C trước khi pha
        - **Vắc xin bại liệt uống (OPV):** -20°C (đông đá), sau khi rã đông dùng trong 6 tháng ở 2-8°C
        
        **📦 Dây chuyền lạnh (Cold Chain):**
        
        Vắc xin phải được bảo quản lạnh từ nhà sản xuất đến người tiêm:
        1. **Nhà sản xuất:** Bảo quản ở 2-8°C
        2. **Vận chuyển:** Sử dụng thùng lạnh, đá khô
        3. **Kho bảo quản:** Tủ lạnh chuyên dụng, có báo động nhiệt độ
        4. **Cơ sở tiêm chủng:** Tủ lạnh y tế, nhiệt kế theo dõi
        5. **Khi tiêm:** Lấy ra khỏi tủ lạnh ngay trước khi tiêm
        
        **⚠️ Dấu hiệu vắc xin bị hỏng:**
        
        - **Nhiệt độ:** Vượt quá 2-8°C (quá nóng hoặc đông đá)
        - **Màu sắc:** Thay đổi màu, có cặn, vẩn đục
        - **Bao bì:** Rách, nứt, phồng
        - **Hạn sử dụng:** Quá hạn
        - **Vắc xin đã pha:** Quá thời gian cho phép (thường 6-8 giờ)
        
        **❌ Không sử dụng vắc xin nếu:**
        - Đã bị đông đá (trừ một số loại đặc biệt)
        - Đã để ở nhiệt độ phòng >30 phút
        - Bao bì bị hỏng
        - Quá hạn sử dụng
        - Có dấu hiệu bất thường về màu sắc, mùi
        
        **🏥 Tại cơ sở tiêm chủng:**
        
        - Tủ lạnh chuyên dụng cho vắc xin
        - Nhiệt kế theo dõi liên tục
        - Báo động khi nhiệt độ vượt ngưỡng
        - Ghi chép nhiệt độ hàng ngày
        - Bảo quản riêng biệt với thực phẩm, thuốc khác
        - Không để vắc xin ở cánh cửa tủ lạnh (nhiệt độ không ổn định)
        
        **🚗 Khi vận chuyển:**
        
        - Sử dụng thùng lạnh chuyên dụng
        - Đá khô hoặc gel lạnh
        - Nhiệt kế theo dõi
        - Vận chuyển nhanh, tránh ánh nắng trực tiếp
        - Không để trong cốp xe, nơi nóng
        
        **🏠 Tại nhà (nếu mua về):**
        
        - **Không nên** mua vắc xin về nhà tự bảo quản
        - Vắc xin cần được bảo quản chuyên nghiệp
        - Nếu bắt buộc, chỉ vận chuyển trong thùng lạnh và tiêm ngay
        - Không để vắc xin trong tủ lạnh gia đình (nhiệt độ không ổn định)
        
        **📋 Kiểm tra trước khi tiêm:**
        
        Nhân viên y tế phải kiểm tra:
        - ✅ Nhiệt độ bảo quản (có ghi chép)
        - ✅ Hạn sử dụng
        - ✅ Tên vắc xin, lô sản xuất
        - ✅ Màu sắc, độ trong suốt
        - ✅ Bao bì nguyên vẹn
        - ✅ Điều kiện bảo quản đúng
        
        **💡 Lưu ý quan trọng:**
        
        - Vắc xin bị hỏng do bảo quản sai có thể:
          - Mất hiệu quả (không bảo vệ được)
          - Gây phản ứng phụ
          - Lãng phí chi phí
        
        - Luôn yêu cầu xem nhiệt kế và ghi chép nhiệt độ tại cơ sở tiêm chủng
        - Nếu nghi ngờ vắc xin bị hỏng, không nên tiêm
        - Báo cáo ngay nếu phát hiện vắc xin bất thường
        """)
    
    with tab8:
        st.markdown("""
        #### ❓ Câu hỏi thường gặp về tiêm chủng
        
        **Q1: Tiêm nhiều mũi cùng lúc có an toàn không?**
        - **A:** Có, rất an toàn. Tiêm nhiều vắc xin cùng lúc không làm tăng phản ứng phụ và giúp trẻ được bảo vệ sớm hơn. Hệ miễn dịch có thể xử lý hàng nghìn kháng nguyên cùng lúc.
        
        **Q2: Nếu trễ lịch tiêm, có cần bắt đầu lại từ đầu không?**
        - **A:** Không. Chỉ cần tiêm tiếp các mũi còn lại, không cần bắt đầu lại. Tuy nhiên, nên tiêm đúng lịch để được bảo vệ sớm nhất.
        
        **Q3: Trẻ bị sốt nhẹ, sổ mũi có tiêm được không?**
        - **A:** Có thể tiêm nếu sốt <38.5°C và trẻ vẫn ăn uống, chơi bình thường. Chỉ hoãn khi sốt cao >38.5°C hoặc bệnh nặng.
        
        **Q4: Vắc xin có gây tự kỷ không?**
        - **A:** Không. Nhiều nghiên cứu lớn đã chứng minh không có mối liên hệ giữa vắc xin và tự kỷ. Nghiên cứu ban đầu đề xuất mối liên hệ đã bị rút lại do gian lận khoa học.
        
        **Q5: Vắc xin có chứa thủy ngân (thimerosal) không?**
        - **A:** Hầu hết vắc xin hiện tại không chứa thimerosal. Nếu có, lượng rất nhỏ và an toàn. Thimerosal đã được loại bỏ khỏi hầu hết vắc xin trẻ em từ năm 2001.
        
        **Q6: Trẻ đã mắc bệnh (sởi, thủy đậu) có cần tiêm vắc xin không?**
        - **A:** Nếu đã mắc bệnh và xác nhận bằng xét nghiệm, thường không cần tiêm vắc xin đó nữa vì đã có miễn dịch tự nhiên. Tuy nhiên, một số bệnh có thể mắc lại nên vẫn nên tư vấn bác sĩ.
        
        **Q7: Tiêm vắc xin có làm suy yếu hệ miễn dịch không?**
        - **A:** Không. Ngược lại, vắc xin giúp hệ miễn dịch "học" cách chống lại bệnh một cách an toàn. Hệ miễn dịch vẫn hoạt động bình thường với các mầm bệnh khác.
        
        **Q8: Vắc xin có hiệu quả 100% không?**
        - **A:** Không, nhưng hiệu quả rất cao (80-99% tùy loại). Ngay cả khi không hoàn toàn bảo vệ, vắc xin vẫn giúp giảm mức độ nặng của bệnh nếu mắc phải.
        
        **Q9: Người lớn có cần tiêm nhắc lại không?**
        - **A:** Có. Một số vắc xin cần nhắc lại: Cúm (hàng năm), Tdap/Td (10 năm), Phế cầu (theo chỉ định). Nên kiểm tra sổ tiêm chủng định kỳ.
        
        **Q10: Tiêm vắc xin có đau không?**
        - **A:** Có thể đau nhẹ tại chỗ tiêm, nhưng chỉ trong vài giây. Đau này nhẹ hơn nhiều so với đau khi mắc bệnh. Có thể dùng thuốc giảm đau sau tiêm nếu cần.
        
        **Q11: Vắc xin có thể gây bệnh mà nó phòng ngừa không?**
        - **A:** Vắc xin bất hoạt không thể gây bệnh. Vắc xin sống giảm độc lực rất hiếm khi gây bệnh (tỷ lệ <1/1 triệu), và nếu có thường nhẹ hơn nhiều so với bệnh tự nhiên.
        
        **Q12: Trẻ sinh non có tiêm được vắc xin không?**
        - **A:** Có, tiêm theo tuổi thực (không tính tuổi điều chỉnh). Trẻ sinh non càng cần được bảo vệ bằng vắc xin vì dễ mắc bệnh hơn.
        
        **Q13: Có thể tiêm vắc xin khi đang cho con bú không?**
        - **A:** Có, hầu hết vắc xin an toàn khi cho con bú. Một số vắc xin (như Cúm, Tdap) còn khuyến khích tiêm để truyền kháng thể cho trẻ qua sữa mẹ.
        
        **Q14: Vắc xin có tác dụng phụ lâu dài không?**
        - **A:** Hầu hết phản ứng xảy ra trong vài ngày đến vài tuần. Phản ứng lâu dài rất hiếm và được theo dõi chặt chẽ qua hệ thống giám sát an toàn vắc xin.
        
        **Q15: Có thể tiêm vắc xin nếu đang dùng kháng sinh không?**
        - **A:** Có. Kháng sinh không ảnh hưởng đến hiệu quả vắc xin bất hoạt hoặc tiêm. Chỉ cần lưu ý với vắc xin sống uống (Rotavirus) - nên cách 2 tuần.
        """)
    
    with tab9:
        st.markdown("""
        #### 📖 Nguồn thông tin đáng tin cậy về tiêm chủng
        
        **🇻🇳 Tại Việt Nam:**
        
        - **Bộ Y tế Việt Nam:** Thông tin chính thức về chương trình TCMR và các khuyến nghị
        - **Viện Vệ sinh Dịch tễ Trung ương (NIHE):** Nghiên cứu và khuyến nghị về vắc xin
        - **Cục Y tế Dự phòng:** Quản lý chương trình tiêm chủng quốc gia
        - **Trung tâm Y tế Dự phòng các tỉnh/thành:** Tư vấn và tiêm chủng tại địa phương
        
        **🌍 Quốc tế:**
        
        - **Tổ chức Y tế Thế giới (WHO):** Khuyến nghị toàn cầu về tiêm chủng, thông tin về an toàn vắc xin
        - **Trung tâm Kiểm soát và Phòng ngừa Dịch bệnh Hoa Kỳ (CDC):** Hướng dẫn chi tiết về lịch tiêm, chỉ định, chống chỉ định
        - **Học viện Nhi khoa Hoa Kỳ (AAP):** Khuyến nghị về tiêm chủng cho trẻ em
        - **Hiệp hội Bác sĩ Gia đình Hoa Kỳ (AAFP):** Hướng dẫn cho người lớn
        - **Trung tâm Phòng ngừa và Kiểm soát Dịch bệnh Châu Âu (ECDC):** Khuyến nghị cho châu Âu
        
        **📚 Tài liệu tham khảo:**
        
        - **Sách giáo khoa:** Miễn dịch học, Nhi khoa, Y tế Công cộng
        - **Tạp chí y khoa:** Vaccine, Clinical Infectious Diseases, Pediatrics
        - **Cơ sở dữ liệu:** PubMed, Cochrane Library
        
        **⚠️ Cảnh báo về thông tin sai lệch:**
        
        - Tránh tin vào thông tin từ mạng xã hội không có nguồn khoa học
        - Không tin vào các trang web chống vắc xin không có bằng chứng
        - Luôn kiểm tra nguồn thông tin với bác sĩ hoặc cơ sở y tế
        - Thông tin y khoa luôn thay đổi, nên tham khảo nguồn cập nhật
        
        **🔍 Cách đánh giá thông tin:**
        
        1. Kiểm tra nguồn: Ai viết? Có phải chuyên gia y tế không?
        2. Kiểm tra ngày: Thông tin có cập nhật không?
        3. Kiểm tra bằng chứng: Có nghiên cứu khoa học hỗ trợ không?
        4. So sánh: Thông tin có nhất quán với các nguồn đáng tin cậy khác không?
        5. Tư vấn chuyên gia: Khi nghi ngờ, hỏi bác sĩ
        
        **📞 Kênh tư vấn:**
        
        - Bác sĩ gia đình hoặc bác sĩ nhi khoa
        - Phòng khám tiêm chủng
        - Trung tâm y tế dự phòng
        - Hotline tư vấn sức khỏe (nếu có)
        """)
    
    st.markdown("---")
    st.info("""
    **ℹ️ Lưu ý quan trọng:**
    
    Thông tin trên chỉ mang tính chất tham khảo và giáo dục. Mỗi cá nhân có tình trạng sức khỏe khác nhau, 
    nên việc quyết định tiêm chủng cần được tư vấn bởi bác sĩ hoặc nhân viên y tế có chuyên môn.
    
    - Lịch tiêm có thể thay đổi tùy theo tình trạng sức khỏe và chỉ định của bác sĩ
    - Phản ứng sau tiêm có thể khác nhau ở mỗi người
    - Thông tin về giá cả và địa điểm tiêm nên liên hệ trực tiếp với cơ sở y tế
    - Luôn mang theo sổ tiêm chủng khi đi tiêm
    """)


def render_schedule_calculator():
    """Render personalized vaccination schedule calculator"""
    st.markdown("### 🛠️ Công cụ tính lịch tiêm chủng cá nhân")
    st.markdown("Nhập thông tin để nhận lịch tiêm chủng được đề xuất")
    
    # Input form
    col1, col2 = st.columns(2)
    
    with col1:
        age_type = st.radio(
            "Đối tượng:",
            ["Trẻ em", "Người lớn"],
            key="age_type_calc"
        )
        
        if age_type == "Trẻ em":
            age_months = st.number_input(
                "Tuổi (tháng):",
                min_value=0,
                max_value=216,  # 18 years
                value=0,
                step=1,
                key="age_months"
            )
            age_display = f"{age_months} tháng"
            if age_months >= 12:
                age_years = age_months // 12
                remaining_months = age_months % 12
                if remaining_months > 0:
                    age_display = f"{age_years} tuổi {remaining_months} tháng"
                else:
                    age_display = f"{age_years} tuổi"
        else:
            age_years = st.number_input(
                "Tuổi (năm):",
                min_value=19,
                max_value=100,
                value=30,
                step=1,
                key="age_years"
            )
            age_display = f"{age_years} tuổi"
    
    with col2:
        st.markdown("**Tình trạng đặc biệt (nếu có):**")
        special_conditions = st.multiselect(
            "Chọn các điều kiện phù hợp:",
            [
                "Phụ nữ mang thai",
                "Người cao tuổi (≥65 tuổi)",
                "Bệnh tim mạch",
                "Bệnh phổi mạn tính",
                "Đái tháo đường",
                "Bệnh thận mạn tính",
                "Bệnh gan mạn tính",
                "Suy giảm miễn dịch",
                "Chuẩn bị đi du lịch",
                "Không có điều kiện đặc biệt"
            ],
            key="special_conditions"
        )
    
    st.markdown("---")
    
    # Calculate and display schedule
    if st.button("🔍 Tính lịch tiêm chủng", type="primary"):
        st.markdown(f"### 📅 Lịch tiêm chủng đề xuất cho: {age_display}")
        
        recommended_vaccines = []
        
        if age_type == "Trẻ em":
            # Children's schedule
            if age_months == 0:
                recommended_vaccines.append({
                    "Vắc xin": "BCG",
                    "Thời điểm": "Ngay sau sinh",
                    "Lý do": "Phòng lao, tiêm trong tháng đầu"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Viêm gan B",
                    "Thời điểm": "Trong 24 giờ đầu sau sinh",
                    "Lý do": "Mũi đầu tiên trong phác đồ 3-4 mũi"
                })
            elif age_months == 2:
                recommended_vaccines.append({
                    "Vắc xin": "Viêm gan B",
                    "Thời điểm": "2 tháng tuổi",
                    "Lý do": "Mũi 2"
                })
                recommended_vaccines.append({
                    "Vắc xin": "DTP",
                    "Thời điểm": "2 tháng tuổi",
                    "Lý do": "Mũi 1 (Bạch hầu - Ho gà - Uốn ván)"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Bại liệt",
                    "Thời điểm": "2 tháng tuổi",
                    "Lý do": "Liều 1"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Phế cầu (khuyến nghị)",
                    "Thời điểm": "2 tháng tuổi",
                    "Lý do": "Mũi 1 - Phòng viêm phổi, viêm màng não"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Rotavirus (khuyến nghị)",
                    "Thời điểm": "2 tháng tuổi",
                    "Lý do": "Mũi 1 - Phòng tiêu chảy"
                })
            elif age_months == 3:
                recommended_vaccines.append({
                    "Vắc xin": "DTP",
                    "Thời điểm": "3 tháng tuổi",
                    "Lý do": "Mũi 2"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Bại liệt",
                    "Thời điểm": "3 tháng tuổi",
                    "Lý do": "Liều 2"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Phế cầu (khuyến nghị)",
                    "Thời điểm": "3 tháng tuổi",
                    "Lý do": "Mũi 2"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Rotavirus (khuyến nghị)",
                    "Thời điểm": "3 tháng tuổi",
                    "Lý do": "Mũi 2"
                })
            elif age_months == 4:
                recommended_vaccines.append({
                    "Vắc xin": "DTP",
                    "Thời điểm": "4 tháng tuổi",
                    "Lý do": "Mũi 3"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Bại liệt",
                    "Thời điểm": "4 tháng tuổi",
                    "Lý do": "Liều 3"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Phế cầu (khuyến nghị)",
                    "Thời điểm": "4 tháng tuổi",
                    "Lý do": "Mũi 3"
                })
            elif age_months == 6:
                recommended_vaccines.append({
                    "Vắc xin": "Viêm gan B",
                    "Thời điểm": "6 tháng tuổi",
                    "Lý do": "Mũi 3"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Cúm (khuyến nghị)",
                    "Thời điểm": "6 tháng tuổi",
                    "Lý do": "Mũi 1 (lần đầu cần 2 mũi cách 1 tháng)"
                })
            elif age_months == 9:
                recommended_vaccines.append({
                    "Vắc xin": "Sởi",
                    "Thời điểm": "9 tháng tuổi",
                    "Lý do": "Mũi 1"
                })
            elif age_months == 12:
                recommended_vaccines.append({
                    "Vắc xin": "Viêm não Nhật Bản",
                    "Thời điểm": "12 tháng tuổi",
                    "Lý do": "Mũi 1"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Thủy đậu (khuyến nghị)",
                    "Thời điểm": "12-18 tháng tuổi",
                    "Lý do": "Mũi 1"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Viêm gan A (khuyến nghị)",
                    "Thời điểm": "12 tháng tuổi",
                    "Lý do": "Mũi 1"
                })
            elif age_months == 18:
                recommended_vaccines.append({
                    "Vắc xin": "DTP",
                    "Thời điểm": "18 tháng tuổi",
                    "Lý do": "Mũi 4 (nhắc lại)"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Bại liệt",
                    "Thời điểm": "18 tháng tuổi",
                    "Lý do": "Liều 4 (nhắc lại)"
                })
                recommended_vaccines.append({
                    "Vắc xin": "MMR",
                    "Thời điểm": "18 tháng tuổi",
                    "Lý do": "Mũi 2"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Phế cầu (khuyến nghị)",
                    "Thời điểm": "12-15 tháng tuổi",
                    "Lý do": "Mũi nhắc lại"
                })
            elif age_months >= 24:
                recommended_vaccines.append({
                    "Vắc xin": "Viêm não Nhật Bản",
                    "Thời điểm": "24 tháng tuổi",
                    "Lý do": "Mũi 3 (nhắc lại)"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Viêm gan A (khuyến nghị)",
                    "Thời điểm": "18-24 tháng tuổi",
                    "Lý do": "Mũi 2"
                })
            elif age_months >= 48 and age_months <= 72:
                recommended_vaccines.append({
                    "Vắc xin": "Thủy đậu (khuyến nghị)",
                    "Thời điểm": "4-6 tuổi",
                    "Lý do": "Mũi 2 (nhắc lại)"
                })
                recommended_vaccines.append({
                    "Vắc xin": "DTP",
                    "Thời điểm": "5-6 tuổi",
                    "Lý do": "Mũi 5 (nhắc lại)"
                })
                recommended_vaccines.append({
                    "Vắc xin": "MMR",
                    "Thời điểm": "5-6 tuổi",
                    "Lý do": "Mũi 3 (nhắc lại)"
                })
            elif age_months >= 108 and age_months <= 168:
                recommended_vaccines.append({
                    "Vắc xin": "HPV (khuyến nghị)",
                    "Thời điểm": "9-14 tuổi",
                    "Lý do": "2 mũi (cách 6 tháng) - Phòng ung thư cổ tử cung"
                })
        else:
            # Adults schedule
            recommended_vaccines.append({
                "Vắc xin": "Cúm",
                "Thời điểm": "Hàng năm",
                "Lý do": "Tốt nhất tiêm tháng 9-11, trước mùa cúm"
            })
            
            if age_years >= 65:
                recommended_vaccines.append({
                    "Vắc xin": "Phế cầu",
                    "Thời điểm": "≥65 tuổi",
                    "Lý do": "PCV13 trước, sau 1 năm tiêm PPSV23"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Zona",
                    "Thời điểm": "≥50 tuổi",
                    "Lý do": "2 mũi (cách 2-6 tháng)"
                })
            
            recommended_vaccines.append({
                "Vắc xin": "Tdap/Td",
                "Thời điểm": "Mỗi 10 năm",
                "Lý do": "Nhắc lại uốn ván, bạch hầu"
            })
            
            if "Phụ nữ mang thai" in special_conditions:
                recommended_vaccines.append({
                    "Vắc xin": "Tdap",
                    "Thời điểm": "Tuần 27-36 của thai kỳ",
                    "Lý do": "Mỗi lần mang thai, truyền kháng thể cho con"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Cúm",
                    "Thời điểm": "Bất kỳ giai đoạn nào của thai kỳ",
                    "Lý do": "An toàn và được khuyến nghị"
                })
            
            if "Chuẩn bị đi du lịch" in special_conditions:
                recommended_vaccines.append({
                    "Vắc xin": "Viêm gan A",
                    "Thời điểm": "Trước khi đi 2-4 tuần",
                    "Lý do": "2 mũi (cách 6-12 tháng)"
                })
                recommended_vaccines.append({
                    "Vắc xin": "Thương hàn",
                    "Thời điểm": "Trước khi đi 2 tuần",
                    "Lý do": "Nếu đi vùng có dịch"
                })
        
        # Add special condition recommendations
        if "Bệnh tim mạch" in special_conditions or "Bệnh phổi mạn tính" in special_conditions:
            recommended_vaccines.append({
                "Vắc xin": "Cúm",
                "Thời điểm": "Hàng năm",
                "Lý do": "Ưu tiên cao cho người có bệnh mạn tính"
            })
            recommended_vaccines.append({
                "Vắc xin": "Phế cầu",
                "Thời điểm": "Theo chỉ định bác sĩ",
                "Lý do": "Phòng viêm phổi"
            })
        
        if "Đái tháo đường" in special_conditions:
            recommended_vaccines.append({
                "Vắc xin": "Cúm",
                "Thời điểm": "Hàng năm",
                "Lý do": "Người đái tháo đường dễ biến chứng nặng"
            })
            recommended_vaccines.append({
                "Vắc xin": "Phế cầu",
                "Thời điểm": "Theo chỉ định bác sĩ",
                "Lý do": "Nguy cơ nhiễm trùng cao hơn"
            })
        
        if recommended_vaccines:
            st.dataframe(recommended_vaccines, use_container_width=True)
            
            st.markdown("---")
            st.markdown("### 📋 Checklist trước khi tiêm")
            
            checklist_items = [
                "✓ Kiểm tra sức khỏe tổng quát",
                "✓ Khai báo tiền sử dị ứng",
                "✓ Khai báo thuốc đang dùng",
                "✓ Không sốt cao (>38.5°C)",
                "✓ Mang theo sổ tiêm chủng",
                "✓ Ăn uống đầy đủ trước khi tiêm"
            ]
            
            for item in checklist_items:
                st.markdown(f"- {item}")
            
            st.markdown("---")
            st.warning("""
            **⚠️ Lưu ý quan trọng:**
            - Lịch trên chỉ mang tính chất tham khảo
            - Cần được bác sĩ đánh giá và chỉ định cụ thể
            - Lịch có thể thay đổi tùy theo tình trạng sức khỏe
            - Nếu đã tiêm một số vắc xin, chỉ cần tiêm tiếp các mũi còn lại
            """)
        else:
            st.info(f"Không có vắc xin cụ thể được đề xuất cho {age_display} tại thời điểm này. Vui lòng tham khảo tab 'Lịch tiêm chủng' để xem lịch đầy đủ.")

