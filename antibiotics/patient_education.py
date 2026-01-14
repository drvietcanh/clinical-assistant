"""
Patient Education Materials
Tài liệu giáo dục bệnh nhân về kháng sinh
"""

import streamlit as st
from typing import Dict, List, Optional
from .antibiotics_data import ANTIBIOTICS_DATABASE


# Patient education templates for common antibiotics
PATIENT_EDUCATION_TEMPLATES = {
    "Vancomycin": {
        "title": "Hướng dẫn sử dụng Vancomycin",
        "how_to_take": """
        **Cách dùng:**
        - Vancomycin được truyền qua đường tĩnh mạch (IV) tại bệnh viện
        - Thời gian truyền: Thường từ 60-120 phút
        - Không tự ý ngừng thuốc khi chưa có chỉ định của bác sĩ
        """,
        "side_effects": """
        **Tác dụng phụ thường gặp:**
        - Đỏ da, ngứa (hội chứng đỏ người - Red Man Syndrome)
        - Buồn nôn, nôn
        - Đau tại vị trí tiêm truyền
        - Giảm thính lực (hiếm gặp)
        - Độc thận (hiếm gặp)
        
        **Khi nào cần báo bác sĩ ngay:**
        - Phát ban, ngứa nhiều
        - Khó thở, sưng mặt/lưỡi
        - Giảm thính lực, ù tai
        - Giảm lượng nước tiểu
        """,
        "warnings": """
        **Cảnh báo quan trọng:**
        - Cần theo dõi chức năng thận và thính lực trong quá trình điều trị
        - Báo bác sĩ nếu đang dùng thuốc khác
        - Uống đủ nước để tránh độc thận
        """,
        "interactions": """
        **Tương tác thuốc cần tránh:**
        - Các thuốc độc thận (aminoglycosides)
        - Thuốc lợi tiểu
        - Một số thuốc gây mê
        """
    },
    "Ceftriaxone": {
        "title": "Hướng dẫn sử dụng Ceftriaxone",
        "how_to_take": """
        **Cách dùng:**
        - Ceftriaxone được tiêm hoặc truyền qua đường tĩnh mạch/tiêm bắp
        - Thường dùng 1-2 lần/ngày
        - Có thể dùng tại bệnh viện hoặc tại nhà (nếu được hướng dẫn)
        """,
        "side_effects": """
        **Tác dụng phụ thường gặp:**
        - Tiêu chảy
        - Buồn nôn, nôn
        - Phát ban da
        - Đau tại vị trí tiêm
        
        **Khi nào cần báo bác sĩ ngay:**
        - Tiêu chảy nặng hoặc có máu
        - Phát ban, ngứa nhiều
        - Khó thở
        - Sưng mặt/lưỡi
        """,
        "warnings": """
        **Cảnh báo quan trọng:**
        - Không dùng nếu dị ứng với penicillin hoặc cephalosporin
        - Có thể gây tiêu chảy do C. difficile
        - Báo bác sĩ nếu đang mang thai hoặc cho con bú
        """,
        "interactions": """
        **Tương tác thuốc cần tránh:**
        - Thuốc chống đông máu (warfarin)
        - Thuốc tránh thai (có thể giảm hiệu quả)
        """
    },
    "Amoxicillin": {
        "title": "Hướng dẫn sử dụng Amoxicillin",
        "how_to_take": """
        **Cách dùng:**
        - Uống với hoặc không với thức ăn
        - Uống đủ nước khi dùng thuốc
        - Uống đều đặn theo chỉ định (thường 2-3 lần/ngày)
        - Không tự ý ngừng thuốc khi chưa hết liệu trình
        """,
        "side_effects": """
        **Tác dụng phụ thường gặp:**
        - Tiêu chảy nhẹ
        - Buồn nôn
        - Phát ban da nhẹ
        
        **Khi nào cần báo bác sĩ ngay:**
        - Tiêu chảy nặng hoặc có máu
        - Phát ban nặng, ngứa nhiều
        - Khó thở, sưng mặt/lưỡi
        - Sốt, đau họng
        """,
        "warnings": """
        **Cảnh báo quan trọng:**
        - Không dùng nếu dị ứng với penicillin
        - Uống đủ nước
        - Hoàn thành đủ liệu trình điều trị
        """,
        "interactions": """
        **Tương tác thuốc cần tránh:**
        - Thuốc tránh thai (có thể giảm hiệu quả)
        - Methotrexate
        - Allopurinol (có thể tăng nguy cơ phát ban)
        """
    },
    "Azithromycin": {
        "title": "Hướng dẫn sử dụng Azithromycin",
        "how_to_take": """
        **Cách dùng:**
        - Uống 1 giờ trước hoặc 2 giờ sau bữa ăn
        - Uống đủ nước
        - Thường dùng 1 lần/ngày
        - Hoàn thành đủ liệu trình (thường 3-5 ngày)
        """,
        "side_effects": """
        **Tác dụng phụ thường gặp:**
        - Buồn nôn, nôn
        - Tiêu chảy
        - Đau bụng
        - Đau đầu
        
        **Khi nào cần báo bác sĩ ngay:**
        - Tiêu chảy nặng
        - Đau ngực, nhịp tim không đều
        - Vàng da, vàng mắt
        - Giảm thính lực
        """,
        "warnings": """
        **Cảnh báo quan trọng:**
        - Có thể gây QT kéo dài (nguy cơ rối loạn nhịp tim)
        - Không dùng nếu có bệnh tim nặng
        - Báo bác sĩ nếu đang dùng thuốc tim mạch
        """,
        "interactions": """
        **Tương tác thuốc cần tránh:**
        - Thuốc chống loạn nhịp tim
        - Một số thuốc chống nấm
        - Thuốc chống đông máu
        """
    },
    "Ciprofloxacin": {
        "title": "Hướng dẫn sử dụng Ciprofloxacin",
        "how_to_take": """
        **Cách dùng:**
        - Uống với nhiều nước (ít nhất 1 cốc nước đầy)
        - Có thể uống với hoặc không với thức ăn
        - Tránh sữa, sản phẩm từ sữa, nước ép cam quýt trong vòng 2 giờ
        - Uống đều đặn theo chỉ định
        """,
        "side_effects": """
        **Tác dụng phụ thường gặp:**
        - Buồn nôn, nôn
        - Tiêu chảy
        - Đau đầu
        - Chóng mặt
        
        **Khi nào cần báo bác sĩ ngay:**
        - Đau gân, sưng gân (đặc biệt gân Achilles)
        - Đau ngực, nhịp tim không đều
        - Co giật
        - Tâm thần bất thường (lo âu, hoang tưởng)
        """,
        "warnings": """
        **Cảnh báo quan trọng:**
        - ⚠️ Có thể gây đứt gân (đặc biệt ở người cao tuổi)
        - Tránh ánh nắng mặt trời (dễ bị cháy nắng)
        - Có thể gây QT kéo dài
        - Không dùng cho trẻ em và phụ nữ mang thai
        """,
        "interactions": """
        **Tương tác thuốc cần tránh:**
        - Thuốc kháng acid, sắt, kẽm (giảm hấp thu)
        - Theophylline, caffeine
        - Thuốc chống đông máu
        - Một số thuốc chống loạn nhịp tim
        """
    }
}


def get_patient_education(antibiotic_name: str) -> Optional[Dict]:
    """Get patient education material for an antibiotic"""
    return PATIENT_EDUCATION_TEMPLATES.get(antibiotic_name)


def generate_patient_education_text(antibiotic_name: str) -> str:
    """Generate patient education text for printing"""
    edu = get_patient_education(antibiotic_name)
    if not edu:
        return f"Chưa có tài liệu giáo dục cho {antibiotic_name}"
    
    text = f"""
{edu['title']}

{edu['how_to_take']}

{edu['side_effects']}

{edu['warnings']}

{edu['interactions']}

---
⚠️ Lưu ý: Đây chỉ là thông tin tham khảo. Luôn tuân theo chỉ định của bác sĩ.
"""
    return text


def render_patient_education(antibiotic_name: str):
    """Render patient education UI"""
    
    st.markdown("---")
    st.markdown("### 📚 Hướng Dẫn Cho Bệnh Nhân")
    
    edu = get_patient_education(antibiotic_name)
    
    if not edu:
        st.info(f"💡 Tài liệu giáo dục cho {antibiotic_name} đang được cập nhật. Vui lòng tham khảo hướng dẫn từ bác sĩ.")
        return
    
    # Display sections
    st.markdown(f"#### {edu['title']}")
    
    with st.expander("💊 Cách dùng thuốc", expanded=True):
        st.markdown(edu['how_to_take'])
    
    with st.expander("⚠️ Tác dụng phụ", expanded=False):
        st.markdown(edu['side_effects'])
    
    with st.expander("🚨 Cảnh báo quan trọng", expanded=False):
        st.markdown(edu['warnings'])
    
    with st.expander("💊 Tương tác thuốc", expanded=False):
        st.markdown(edu['interactions'])
    
    # Print/Export button
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 In tài liệu", key=f"print_edu_{antibiotic_name}", use_container_width=True):
            st.info("💡 Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in")
    
    with col2:
        try:
            from .export import copy_to_clipboard
            edu_text = generate_patient_education_text(antibiotic_name)
            copy_to_clipboard(edu_text, "📋 Copy", key=f"copy_edu_{antibiotic_name}")
        except ImportError:
            pass
    
    st.markdown("---")
    st.caption("⚠️ **Lưu ý:** Đây chỉ là thông tin tham khảo. Luôn tuân theo chỉ định và hướng dẫn của bác sĩ điều trị.")


def render_patient_education_checker():
    """Render Patient Education Checker UI"""
    
    st.markdown("### 📚 Tài Liệu Giáo Dục Bệnh Nhân")
    st.caption("Tạo tài liệu hướng dẫn dùng thuốc cho bệnh nhân")
    
    # Antibiotic selection
    antibiotic_name = st.selectbox(
        "Chọn kháng sinh:",
        options=sorted(list(ANTIBIOTICS_DATABASE.keys())),
        key="patient_edu_ab"
    )
    
    if st.button("📚 Xem Tài Liệu", type="primary", use_container_width=True):
        render_patient_education(antibiotic_name)


__all__ = [
    'get_patient_education',
    'generate_patient_education_text',
    'render_patient_education',
    'render_patient_education_checker',
]
