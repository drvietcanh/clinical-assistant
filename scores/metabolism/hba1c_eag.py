"""
HbA1c - eAG Converter (Hemoglobin A1c - Estimated Average Glucose)
Chuyển đổi giữa HbA1c và glucose trung bình ước tính
"""

import streamlit as st


def calculate_eag_from_hba1c(hba1c_percent):
    """
    Calculate eAG from HbA1c using ADAG formula
    eAG (mg/dL) = 28.7 × HbA1c - 46.7
    eAG (mmol/L) = 1.59 × HbA1c - 2.59
    
    Args:
        hba1c_percent: HbA1c in percentage (%)
    
    Returns:
        tuple: (eAG in mg/dL, eAG in mmol/L)
    """
    eag_mgdl = 28.7 * hba1c_percent - 46.7
    eag_mmol = 1.59 * hba1c_percent - 2.59
    
    return eag_mgdl, eag_mmol


def calculate_hba1c_from_eag(eag_mgdl):
    """
    Calculate HbA1c from average glucose
    HbA1c (%) = (eAG + 46.7) / 28.7
    
    Args:
        eag_mgdl: Average glucose in mg/dL
    
    Returns:
        float: HbA1c in percentage
    """
    hba1c = (eag_mgdl + 46.7) / 28.7
    return hba1c


def get_diabetes_status(hba1c_percent):
    """
    Determine diabetes status based on HbA1c
    
    Args:
        hba1c_percent: HbA1c in percentage
    
    Returns:
        dict: Status information
    """
    if hba1c_percent < 5.7:
        return {
            "status": "Bình thường",
            "color": "🟢",
            "risk": "Không có đái tháo đường",
            "recommendation": "Duy trì lối sống lành mạnh"
        }
    elif hba1c_percent < 6.5:
        return {
            "status": "Tiền đái tháo đường",
            "color": "🟡",
            "risk": "Nguy cơ cao tiến triển thành ĐTĐ type 2",
            "recommendation": "Can thiệp lối sống tích cực (ăn uống, vận động)"
        }
    elif hba1c_percent < 7.0:
        return {
            "status": "Đái tháo đường - Kiểm soát tốt",
            "color": "🟠",
            "risk": "ĐTĐ được kiểm soát",
            "recommendation": "Tiếp tục điều trị, theo dõi định kỳ"
        }
    elif hba1c_percent < 8.0:
        return {
            "status": "Đái tháo đường - Kiểm soát trung bình",
            "color": "🟠",
            "risk": "Cần cải thiện kiểm soát đường huyết",
            "recommendation": "Xem xét điều chỉnh phác đồ điều trị"
        }
    elif hba1c_percent < 9.0:
        return {
            "status": "Đái tháo đường - Kiểm soát kém",
            "color": "🔴",
            "risk": "Nguy cơ biến chứng cao",
            "recommendation": "Cần điều chỉnh điều trị tích cực"
        }
    else:
        return {
            "status": "Đái tháo đường - Không kiểm soát",
            "color": "🔴",
            "risk": "Nguy cơ biến chứng cấp và mạn rất cao",
            "recommendation": "Cần can thiệp điều trị khẩn cấp"
        }


def render():
    """Render the HbA1c - eAG Converter calculator"""
    
    st.title("🩺 HbA1c - eAG Converter")
    st.markdown("""
    ### Chuyển đổi HbA1c ↔ Glucose trung bình
    
    **HbA1c (Hemoglobin A1c):**
    - Phản ánh glucose máu trung bình trong 2-3 tháng qua
    - Tiêu chuẩn vàng để đánh giá kiểm soát đường huyết dài hạn
    
    **eAG (Estimated Average Glucose):**
    - Glucose trung bình ước tính từ HbA1c
    - Giúp bệnh nhân dễ hiểu hơn so với %HbA1c
    
    **Công thức ADAG (A1c-Derived Average Glucose Study):**
    - eAG (mg/dL) = 28.7 × HbA1c - 46.7
    - eAG (mmol/L) = 1.59 × HbA1c - 2.59
    """)
    
    st.markdown("---")
    
    # Conversion mode selection
    mode = st.radio(
        "**Chọn loại chuyển đổi:**",
        ["HbA1c → eAG (Glucose trung bình)", "eAG → HbA1c"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if mode == "HbA1c → eAG (Glucose trung bình)":
        # HbA1c to eAG conversion
        st.subheader("📊 Nhập HbA1c")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            hba1c = st.number_input(
                "**HbA1c (%)**",
                min_value=3.0,
                max_value=20.0,
                value=7.0,
                step=0.1,
                help="Nhập giá trị HbA1c từ 3% đến 20%"
            )
        
        if st.button("🔄 Chuyển đổi", type="primary", use_container_width=True):
            # Calculate eAG
            eag_mgdl, eag_mmol = calculate_eag_from_hba1c(hba1c)
            
            # Get diabetes status
            status_info = get_diabetes_status(hba1c)
            
            st.markdown("---")
            st.subheader("📈 Kết Quả Chuyển Đổi")
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "HbA1c",
                    f"{hba1c:.1f}%",
                    help="Giá trị HbA1c đầu vào"
                )
            
            with col2:
                st.metric(
                    "eAG (mg/dL)",
                    f"{eag_mgdl:.0f} mg/dL",
                    help="Glucose trung bình ước tính"
                )
            
            st.metric(
                "eAG (mmol/L)",
                f"{eag_mmol:.1f} mmol/L",
                help="Glucose trung bình ước tính (đơn vị SI)"
            )
            
            st.markdown("---")
            
            # Status interpretation
            st.subheader("🎯 Phân Loại & Đánh Giá")
            
            st.info(f"""
            **{status_info['color']} Tình trạng:** {status_info['status']}
            
            **Đánh giá:** {status_info['risk']}
            
            **Khuyến nghị:** {status_info['recommendation']}
            """)
            
            # Reference table
            st.markdown("---")
            st.subheader("📋 Bảng Tham Chiếu HbA1c - eAG")
            
            st.markdown("""
            | HbA1c (%) | eAG (mg/dL) | eAG (mmol/L) | Phân loại |
            |-----------|-------------|--------------|-----------|
            | 5.0 | 97 | 5.4 | Bình thường |
            | 5.5 | 111 | 6.2 | Bình thường |
            | 6.0 | 126 | 7.0 | Tiền ĐTĐ |
            | 6.5 | 140 | 7.8 | Ngưỡng chẩn đoán ĐTĐ |
            | 7.0 | 154 | 8.6 | Mục tiêu kiểm soát ĐTĐ |
            | 7.5 | 169 | 9.4 | Cần cải thiện |
            | 8.0 | 183 | 10.2 | Kiểm soát kém |
            | 8.5 | 197 | 10.9 | Kiểm soát kém |
            | 9.0 | 212 | 11.8 | Không kiểm soát |
            | 10.0 | 240 | 13.4 | Không kiểm soát |
            """)
    
    else:
        # eAG to HbA1c conversion
        st.subheader("📊 Nhập Glucose Trung Bình")
        
        unit = st.radio(
            "**Đơn vị:**",
            ["mg/dL", "mmol/L"],
            horizontal=True
        )
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            if unit == "mg/dL":
                eag_value = st.number_input(
                    "**Glucose trung bình (mg/dL)**",
                    min_value=50.0,
                    max_value=500.0,
                    value=154.0,
                    step=1.0,
                    help="Nhập glucose trung bình từ CGM hoặc SMBG"
                )
            else:
                eag_mmol_input = st.number_input(
                    "**Glucose trung bình (mmol/L)**",
                    min_value=2.8,
                    max_value=27.8,
                    value=8.6,
                    step=0.1,
                    help="Nhập glucose trung bình từ CGM hoặc SMBG"
                )
                eag_value = eag_mmol_input * 18.0  # Convert to mg/dL
        
        if st.button("🔄 Chuyển đổi", type="primary", use_container_width=True):
            # Calculate HbA1c
            hba1c = calculate_hba1c_from_eag(eag_value)
            
            # Get diabetes status
            status_info = get_diabetes_status(hba1c)
            
            st.markdown("---")
            st.subheader("📈 Kết Quả Chuyển Đổi")
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "eAG (mg/dL)",
                    f"{eag_value:.0f} mg/dL",
                    help="Glucose trung bình"
                )
            
            with col2:
                st.metric(
                    "HbA1c ước tính",
                    f"{hba1c:.1f}%",
                    help="HbA1c ước tính từ glucose trung bình"
                )
            
            st.metric(
                "eAG (mmol/L)",
                f"{eag_value/18.0:.1f} mmol/L",
                help="Glucose trung bình (đơn vị SI)"
            )
            
            st.markdown("---")
            
            # Status interpretation
            st.subheader("🎯 Phân Loại & Đánh Giá")
            
            st.info(f"""
            **{status_info['color']} Tình trạng:** {status_info['status']}
            
            **Đánh giá:** {status_info['risk']}
            
            **Khuyến nghị:** {status_info['recommendation']}
            """)
    
    # Clinical notes
    st.markdown("---")
    st.subheader("📚 Ghi Chú Lâm Sàng")
    
    with st.expander("🎯 Mục tiêu HbA1c theo ADA/EASD"):
        st.markdown("""
        ### Mục tiêu cá nhân hóa:
        
        **1. Mục tiêu chung:**
        - HbA1c < 7.0% cho hầu hết người trưởng thành
        - HbA1c < 6.5% nếu không hạ đường huyết
        
        **2. Mục tiêu linh hoạt hơn (< 8.0%):**
        - Người cao tuổi yếu
        - Bệnh kèm theo nhiều
        - Tiền sử hạ đường huyết nặng
        - Tuổi thọ hạn chế
        - Biến chứng mạch máu tiến triển
        
        **3. Mục tiêu chặt chẽ hơn (< 6.5%):**
        - Mới chẩn đoán
        - Trẻ tuổi
        - Không dùng thuốc gây hạ đường huyết
        - Tuổi thọ dự kiến dài
        """)
    
    with st.expander("⚠️ Giới hạn của HbA1c"):
        st.markdown("""
        ### HbA1c có thể không chính xác khi:
        
        **1. Rối loạn hồng cầu:**
        - Thiếu máu hemolytic → HbA1c giảm giả
        - Thiếu máu thiếu sắt → HbA1c tăng giả
        - Truyền máu gần đây → HbA1c không đáng tin
        - Hemoglobinopathy (HbS, HbC, HbE)
        
        **2. Tình trạng khác:**
        - Suy thận giai đoạn cuối
        - Phụ nữ mang thai
        - Tuổi trẻ em < 18 tuổi
        - Thay đổi glucose nhanh (DKA hồi phục)
        
        **3. Biến động glucose lớn:**
        - HbA1c bình thường nhưng có nhiều hypo/hyper
        - Cần thêm CGM hoặc SMBG để đánh giá
        """)
    
    with st.expander("🔬 Về Nghiên cứu ADAG"):
        st.markdown("""
        ### ADAG Study (2008):
        
        **Nghiên cứu đa trung tâm quốc tế:**
        - 507 bệnh nhân ĐTĐ type 1 và type 2
        - 268 người không ĐTĐ
        - 16 tuần theo dõi glucose liên tục + SMBG
        
        **Kết quả:**
        - Tương quan cao giữa HbA1c và glucose trung bình (r = 0.92)
        - Công thức: eAG (mg/dL) = 28.7 × HbA1c - 46.7
        - Độ chính xác: ±2 SD = ±30 mg/dL
        
        **Ý nghĩa lâm sàng:**
        - Giúp bệnh nhân hiểu HbA1c dễ hơn
        - Liên kết với kết quả tự đo glucose tại nhà
        - Không thay thế HbA1c trong chẩn đoán
        """)
    
    with st.expander("💡 Cách sử dụng eAG"):
        st.markdown("""
        ### Ứng dụng thực tế:
        
        **1. Tư vấn bệnh nhân:**
        - "HbA1c 7% tương đương glucose trung bình 154 mg/dL"
        - Dễ so sánh với kết quả đo glucose hàng ngày
        - Giúp đặt mục tiêu thực tế
        
        **2. Giải thích chênh lệch:**
        - Nếu glucose tự đo thường < 150 nhưng HbA1c cao
        - → Có thể bỏ sót đường huyết cao sau ăn
        - → Cần tăng tần suất đo, đặc biệt sau ăn
        
        **3. Động viên tuân thủ:**
        - Thấy cải thiện glucose hàng ngày
        - → Hiểu được sẽ cải thiện HbA1c
        - → Tăng motivation điều trị
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Nathan DM, et al. Translating the A1C assay into estimated average glucose values. Diabetes Care. 2008;31(8):1473-8
    - American Diabetes Association. Standards of Medical Care in Diabetes-2024
    - EASD/ADA Consensus Report 2023
    """)


if __name__ == "__main__":
    render()

