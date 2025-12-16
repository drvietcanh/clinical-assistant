"""
Dosing Schedule Generator
Generate dosing schedule timeline for drugs
Visual timeline: 24h, 48h, 7 days
"""

import streamlit as st
from datetime import datetime, timedelta

# Import drug database for dropdown list
try:
    from .drug_database import DRUG_DATABASE
    _DRUG_DB_AVAILABLE = True
except ImportError:
    try:
        from drugs.drug_database import DRUG_DATABASE
        _DRUG_DB_AVAILABLE = True
    except ImportError:
        _DRUG_DB_AVAILABLE = False
        DRUG_DATABASE = {}


def calculate_dosing_times(start_time_str, interval_hours, duration_days):
    """
    Calculate dosing times for a schedule
    
    Args:
        start_time_str: Start time string (HH:MM format)
        interval_hours: Dosing interval in hours
        duration_days: Duration in days
    
    Returns:
        list of datetime objects
    """
    try:
        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        start_datetime = datetime.combine(datetime.today(), start_time)
    except (ValueError, TypeError):
        # Default to 8:00 AM if invalid time format
        start_datetime = datetime.combine(datetime.today(), datetime.strptime("08:00", "%H:%M").time())
    
    doses = []
    current_time = start_datetime
    end_time = start_datetime + timedelta(days=duration_days)
    
    while current_time < end_time:
        doses.append(current_time)
        current_time += timedelta(hours=interval_hours)
    
    return doses


def render_dosing_schedule_generator():
    """Render dosing schedule generator interface"""
    
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #4CAF50 0%, #45A049 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.2em;'>📅 Tạo Lịch Trình Liều dùng</h1>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>
            Generate dosing schedule timeline • Visual timeline • Print schedule for nursing
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Công cụ này giúp:**
    - ✅ Tạo lịch trình liều dùng chi tiết
    - ✅ Visual timeline (24h, 48h, 7 ngày)
    - ✅ In lịch cho điều dưỡng
    - ✅ Nhắc nhở thời gian uống tiêm
    """)
    
    st.markdown("---")
    
    # Check for preset values from example buttons
    preset_drug = st.session_state.get('preset_schedule_drug_name', None)
    preset_dose = st.session_state.get('preset_schedule_dose', None)
    preset_interval = st.session_state.get('preset_schedule_interval', None)
    preset_duration = st.session_state.get('preset_schedule_duration', None)
    preset_route = st.session_state.get('preset_schedule_route', None)
    preset_start_time = st.session_state.get('preset_schedule_start_time', None)
    
    # Clear presets after using
    if preset_drug:
        st.session_state.pop('preset_schedule_drug_name', None)
    if preset_dose:
        st.session_state.pop('preset_schedule_dose', None)
    if preset_interval is not None:
        st.session_state.pop('preset_schedule_interval', None)
    if preset_duration is not None:
        st.session_state.pop('preset_schedule_duration', None)
    if preset_route:
        st.session_state.pop('preset_schedule_route', None)
    if preset_start_time:
        st.session_state.pop('preset_schedule_start_time', None)
    
    # Drug selection
    st.markdown("### 💊 Thông tin Thuốc")
    
    # Get drug list from database
    if _DRUG_DB_AVAILABLE and DRUG_DATABASE:
        # Get sorted list of drug names
        drug_list = sorted(list(DRUG_DATABASE.keys()))
        # Add "Khác..." option at the end
        drug_options = drug_list + ["Khác..."]
        
        # Handle preset drug from example buttons
        if preset_drug:
            if preset_drug in drug_list:
                # Set the selectbox to the preset drug
                if 'schedule_drug_select' not in st.session_state or st.session_state.get('schedule_drug_select') != preset_drug:
                    st.session_state['schedule_drug_select'] = preset_drug
            else:
                # Set to "Khác..." and fill custom input
                if 'schedule_drug_select' not in st.session_state or st.session_state.get('schedule_drug_select') != "Khác...":
                    st.session_state['schedule_drug_select'] = "Khác..."
                if 'schedule_drug_custom' not in st.session_state or st.session_state.get('schedule_drug_custom') != preset_drug:
                    st.session_state['schedule_drug_custom'] = preset_drug
        
        # Get current selection or default
        current_selection = st.session_state.get('schedule_drug_select', drug_options[0] if drug_options else "")
        
        # Drug selection dropdown
        selected_drug_option = st.selectbox(
            "Tên thuốc:",
            options=drug_options,
            index=drug_options.index(current_selection) if current_selection in drug_options else 0,
            key="schedule_drug_select"
        )
        
        # If "Khác..." is selected, show text input
        if selected_drug_option == "Khác...":
            custom_drug = st.text_input(
                "Nhập tên thuốc:",
                value=st.session_state.get('schedule_drug_custom', preset_drug if preset_drug and preset_drug not in drug_list else ""),
                placeholder="Ví dụ: Thuốc mới, Biệt dược...",
                key="schedule_drug_custom"
            )
            drug_name = custom_drug
        else:
            drug_name = selected_drug_option
            # Clear custom drug if a drug from list is selected
            if 'schedule_drug_custom' in st.session_state:
                st.session_state.pop('schedule_drug_custom', None)
    else:
        # Fallback to text input if database not available
        drug_name = st.text_input(
            "Tên thuốc:",
            value=preset_drug if preset_drug else "",
            placeholder="Ví dụ: Vancomycin, Metformin, Omeprazole...",
            key="schedule_drug_name"
        )
    
    # Dosing parameters
    st.markdown("### 📋 Thông số Liều dùng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        dose_amount = st.text_input(
            "Liều mỗi lần:",
            value=preset_dose if preset_dose else "1000mg",
            placeholder="Ví dụ: 1000mg, 500mg, 1 tablet...",
            key="schedule_dose"
        )
        
        start_time = st.text_input(
            "Giờ bắt đầu:",
            value=preset_start_time if preset_start_time else "08:00",
            placeholder="HH:MM (ví dụ: 08:00, 14:30)",
            key="schedule_start_time",
            help="Giờ uống/tiêm lần đầu tiên"
        )
    
    with col2:
        interval_hours = st.number_input(
            "Khoảng cách giữa các lần (giờ):",
            min_value=1,
            max_value=48,
            value=preset_interval if preset_interval is not None else 12,
            step=1,
            key="schedule_interval"
        )
        
        duration_days = st.number_input(
            "Thời gian điều trị (ngày):",
            min_value=1,
            max_value=30,
            value=preset_duration if preset_duration is not None else 7,
            step=1,
            key="schedule_duration"
        )
    
    # Route
    route_options = ["PO (Uống)", "IV (Tiêm tĩnh mạch)", "IM (Tiêm bắp)", "SC (Tiêm dưới da)", "Khác"]
    if preset_route and preset_route in route_options:
        route_index = route_options.index(preset_route)
    else:
        route_index = 0
    
    route = st.selectbox(
        "Đường dùng:",
        route_options,
        index=route_index,
        key="schedule_route"
    )
    
    # Patient info (optional)
    with st.expander("📋 Thông tin bệnh nhân (tùy chọn)"):
        patient_name = st.text_input("Tên bệnh nhân:", key="schedule_patient_name")
        patient_id = st.text_input("Mã bệnh nhân:", key="schedule_patient_id")
        doctor_name = st.text_input("Bác sĩ kê đơn:", key="schedule_doctor_name")
    
    st.markdown("---")
    
    # Quick examples
    st.markdown("### 💡 Ví dụ nhanh:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Vancomycin\n1000mg q12h x 7d", use_container_width=True, key="example_vanco"):
            # Lưu preset (giữ nguyên cơ chế cũ để tương thích)
            st.session_state['preset_schedule_drug_name'] = "Vancomycin"
            st.session_state['preset_schedule_dose'] = "1000mg"
            st.session_state['preset_schedule_interval'] = 12
            st.session_state['preset_schedule_duration'] = 7
            st.session_state['preset_schedule_route'] = "IV (Tiêm tĩnh mạch)"
            st.session_state['preset_schedule_start_time'] = "08:00"
            # Đồng bộ trực tiếp với các widget để Streamlit thực sự hiển thị giá trị
            st.session_state['schedule_drug_select'] = "Vancomycin"  # For dropdown
            st.session_state['schedule_dose'] = "1000mg"
            st.session_state['schedule_interval'] = 12
            st.session_state['schedule_duration'] = 7
            st.session_state['schedule_route'] = "IV (Tiêm tĩnh mạch)"
            st.session_state['schedule_start_time'] = "08:00"
            st.session_state['schedule_generated'] = False
            st.rerun()
    
    with col2:
        if st.button("📋 Metformin\n500mg q8h x 30d", use_container_width=True, key="example_metformin"):
            st.session_state['preset_schedule_drug_name'] = "Metformin"
            st.session_state['preset_schedule_dose'] = "500mg"
            st.session_state['preset_schedule_interval'] = 8
            st.session_state['preset_schedule_duration'] = 30
            st.session_state['preset_schedule_route'] = "PO (Uống)"
            st.session_state['preset_schedule_start_time'] = "08:00"
            st.session_state['schedule_drug_select'] = "Metformin"  # For dropdown
            st.session_state['schedule_dose'] = "500mg"
            st.session_state['schedule_interval'] = 8
            st.session_state['schedule_duration'] = 30
            st.session_state['schedule_route'] = "PO (Uống)"
            st.session_state['schedule_start_time'] = "08:00"
            st.session_state['schedule_generated'] = False
            st.rerun()
    
    with col3:
        if st.button("📋 Omeprazole\n20mg q24h x 14d", use_container_width=True, key="example_omeprazole"):
            st.session_state['preset_schedule_drug_name'] = "Omeprazole"
            st.session_state['preset_schedule_dose'] = "20mg"
            st.session_state['preset_schedule_interval'] = 24
            st.session_state['preset_schedule_duration'] = 14
            st.session_state['preset_schedule_route'] = "PO (Uống)"
            st.session_state['preset_schedule_start_time'] = "08:00"
            st.session_state['schedule_drug_select'] = "Omeprazole"  # For dropdown
            st.session_state['schedule_dose'] = "20mg"
            st.session_state['schedule_interval'] = 24
            st.session_state['schedule_duration'] = 14
            st.session_state['schedule_route'] = "PO (Uống)"
            st.session_state['schedule_start_time'] = "08:00"
            st.session_state['schedule_generated'] = False
            st.rerun()
    
    st.markdown("---")
    
    # Generate schedule
    if st.button("📅 Tạo Lịch Trình", type="primary", use_container_width=True):
        st.session_state['schedule_generated'] = True
        if not drug_name:
            st.error("Vui lòng nhập tên thuốc.")
            return
        
        if not dose_amount:
            st.error("Vui lòng nhập liều mỗi lần.")
            return
        
        # Calculate dosing times
        doses = calculate_dosing_times(start_time, interval_hours, duration_days)
        
        if not doses:
            st.error("Không thể tính lịch trình. Vui lòng kiểm tra lại thông tin.")
            st.session_state['schedule_generated'] = False
            return
        
        st.session_state['schedule_generated'] = True
        st.markdown("---")
        
        # Display schedule
        st.markdown("### 📅 Lịch Trình Liều dùng")
        
        # Header info
        schedule_info = f"""
        **Thuốc:** {drug_name}  
        **Liều:** {dose_amount}  
        **Khoảng cách:** Mỗi {interval_hours} giờ  
        **Đường dùng:** {route}  
        **Thời gian điều trị:** {duration_days} ngày  
        **Số lần dùng:** {len(doses)} lần
        """
        
        if patient_name:
            schedule_info += f"\n**Bệnh nhân:** {patient_name}"
        if patient_id:
            schedule_info += f"\n**Mã BN:** {patient_id}"
        if doctor_name:
            schedule_info += f"\n**Bác sĩ:** {doctor_name}"
        
        st.info(schedule_info)
        
        st.markdown("---")
        
        # Timeline by day
        current_date = datetime.today().date()
        doses_by_day = {}
        
        for dose_time in doses:
            day_key = dose_time.date()
            if day_key not in doses_by_day:
                doses_by_day[day_key] = []
            doses_by_day[day_key].append(dose_time)
        
        # Display schedule by day
        for day, day_doses in sorted(doses_by_day.items()):
            day_name = day.strftime("%A")  # Monday, Tuesday, etc.
            day_str = day.strftime("%d/%m/%Y")
            
            # Determine day label
            if day == current_date:
                day_label = f"**Hôm nay - {day_name}, {day_str}**"
                day_color = "#4CAF50"
            elif day == current_date + timedelta(days=1):
                day_label = f"**Ngày mai - {day_name}, {day_str}**"
                day_color = "#2196F3"
            else:
                day_label = f"**{day_name}, {day_str}**"
                day_color = "#666"
            
            st.markdown(f"""
            <div style='background-color: {day_color}20; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 4px solid {day_color};'>
                <h4 style='margin: 0; color: {day_color};'>{day_label}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            # Doses for this day
            for dose_time in sorted(day_doses):
                time_str = dose_time.strftime("%H:%M")
                
                # Icon based on route
                route_icons = {
                    "PO (Uống)": "💊",
                    "IV (Tiêm tĩnh mạch)": "💉",
                    "IM (Tiêm bắp)": "💉",
                    "SC (Tiêm dưới da)": "💉"
                }
                icon = route_icons.get(route, "💊")
                
                # Check if this dose has passed
                now = datetime.now()
                if dose_time < now:
                    status = "✅ Đã dùng"
                    status_color = "#4CAF50"
                elif dose_time <= now + timedelta(hours=1):
                    status = "⏰ Sắp đến"
                    status_color = "#FF9800"
                else:
                    status = "⏳ Chưa đến"
                    status_color = "#666"
                
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    st.markdown(f"**{time_str}**")
                with col2:
                    st.markdown(f"{icon} **{dose_amount}** ({route})")
                with col3:
                    st.markdown(f"<span style='color: {status_color};'>{status}</span>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Summary table
        st.markdown("### 📊 Tóm Tắt Lịch Trình")
        
        summary_data = []
        for i, dose_time in enumerate(doses, 1):
            summary_data.append({
                "Lần": f"#{i}",
                "Ngày": dose_time.strftime("%d/%m/%Y"),
                "Giờ": dose_time.strftime("%H:%M"),
                "Liều": dose_amount,
                "Đường dùng": route.split(" ")[0] if " " in route else route
            })
        
        import pandas as pd
        df_summary = pd.DataFrame(summary_data)
        st.dataframe(df_summary, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Instructions
        st.markdown("### 📝 Hướng dẫn:")
        st.info(f"""
        **Lưu ý quan trọng:**
        - ⏰ Dùng đúng giờ theo lịch trình
        - 📱 Có thể dùng ứng dụng nhắc nhở trên điện thoại
        - 💊 Tuân thủ đúng liều và đường dùng
        - 📞 Liên hệ bác sĩ nếu quên liều hoặc có tác dụng phụ
        
        **Cho điều dưỡng:**
        - Kiểm tra kỹ tên thuốc, liều, đường dùng trước khi cho bệnh nhân
        - Ghi chú lại thời gian dùng thuốc
        - Theo dõi phản ứng của bệnh nhân
        """)

