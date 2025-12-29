"""
Symptom Checker Module
Advanced symptom analysis and diagnosis suggestion
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from symptom_checker.algorithm import (
    analyze_symptoms,
    calculate_severity,
    check_urgency
)
from symptom_checker.data import (
    get_all_symptoms,
    get_symptoms_by_category,
    get_urgent_symptoms
)

# Standard page setup
setup_page(
    page_title="Kiểm tra Triệu chứng",
    page_icon="🩺",
    description="Công cụ phân tích triệu chứng và gợi ý chẩn đoán"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("🩺 Kiểm tra Triệu chứng")
    st.caption("Module **Kiểm tra Triệu chứng** – phân tích triệu chứng và gợi ý chẩn đoán.")
    
    st.markdown("---")
    st.info("""
    **🩺 Symptom Checker:**
    - Nhập **nhiều triệu chứng** cùng lúc
    - Phân tích và **gợi ý chẩn đoán** có thể
    - Đánh giá **mức độ nghiêm trọng**
    - Cảnh báo **cấp cứu** nếu cần
    
    **💡 Lưu ý:**
    - Công cụ chỉ **hỗ trợ**, không thay thế đánh giá lâm sàng
    - Luôn tham khảo bác sĩ trước khi quyết định
    - Kết quả chỉ mang tính tham khảo
    """)

# ========== MAIN CONTENT ==========

st.markdown("## 🩺 Kiểm tra Triệu chứng")
st.markdown("""
**Công cụ phân tích triệu chứng và gợi ý chẩn đoán có thể**

Nhập các triệu chứng để nhận gợi ý về chẩn đoán có thể, mức độ nghiêm trọng, và khuyến nghị xử trí.
""")

# Symptom input
st.markdown("### 📝 Nhập Triệu chứng")

# Get all symptoms for selection
all_symptoms = get_all_symptoms()
symptom_options = {f"{s.name_vn} ({s.name})": s.name for s in all_symptoms}

# Multi-select symptoms
selected_symptoms = st.multiselect(
    "Chọn các triệu chứng (có thể chọn nhiều):",
    options=list(symptom_options.keys()),
    key="symptom_checker_selection",
    help="Chọn tất cả các triệu chứng mà bệnh nhân đang gặp phải"
)

# Manual input option
st.markdown("**Hoặc nhập triệu chứng thủ công:**")
manual_input = st.text_input(
    "Nhập triệu chứng (phân cách bằng dấu phẩy):",
    placeholder="Ví dụ: Sốt, Ho, Khó thở, Đau ngực...",
    key="symptom_checker_manual"
)

# Combine selected and manual symptoms
symptom_list = []
if selected_symptoms:
    symptom_list.extend([symptom_options[s] for s in selected_symptoms])
if manual_input:
    manual_symptoms = [s.strip() for s in manual_input.split(',') if s.strip()]
    symptom_list.extend(manual_symptoms)

# Remove duplicates
symptom_list = list(set(symptom_list))

# Analyze button
if st.button("🔍 Phân tích Triệu chứng", type="primary", use_container_width=True):
    if symptom_list:
        st.session_state['symptom_checker_results'] = {
            'symptoms': symptom_list,
            'diagnoses': analyze_symptoms(symptom_list),
            'severity': calculate_severity(symptom_list),
            'urgency': check_urgency(symptom_list)
        }
        st.rerun()
    else:
        st.warning("Vui lòng nhập ít nhất một triệu chứng.")

# Display results
if 'symptom_checker_results' in st.session_state:
    results = st.session_state['symptom_checker_results']
    symptoms = results['symptoms']
    diagnoses = results['diagnoses']
    severity = results['severity']
    is_urgent, urgency_msg = results['urgency']
    
    st.markdown("---")
    st.markdown("### 📊 Kết quả Phân tích")
    
    # Display symptoms
    st.markdown(f"**Triệu chứng đã nhập:** {', '.join(symptoms)}")
    
    # Urgency warning
    if is_urgent:
        st.error(f"🚨 **{urgency_msg}**")
    else:
        st.info(f"ℹ️ {urgency_msg}")
    
    # Severity
    severity_colors = {
        'critical': '🔴',
        'severe': '🟠',
        'moderate': '🟡',
        'mild': '🟢'
    }
    severity_icons = {
        'critical': '🔴',
        'severe': '🟠',
        'moderate': '🟡',
        'mild': '🟢'
    }
    st.markdown(f"**Mức độ nghiêm trọng:** {severity_icons.get(severity, '⚪')} {severity.upper()}")
    
    # Diagnosis suggestions
    if diagnoses:
        st.markdown("---")
        st.markdown("### 🎯 Gợi ý Chẩn đoán")
        st.info(f"Tìm thấy {len(diagnoses)} chẩn đoán có thể. Sắp xếp theo xác suất:")
        
        for i, diagnosis in enumerate(diagnoses, 1):
            prob = diagnosis['probability']
            prob_percent = int(prob * 100)
            
            # Color code by probability
            if prob >= 0.7:
                color = "🔴"
                expanded = True
            elif prob >= 0.5:
                color = "🟠"
                expanded = False
            elif prob >= 0.3:
                color = "🟡"
                expanded = False
            else:
                color = "🟢"
                expanded = False
            
            with st.expander(
                f"{color} **{i}. {diagnosis['diagnosis']}** - Xác suất: {prob_percent}%",
                expanded=expanded
            ):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Xác suất:** {prob_percent}%")
                    st.markdown(f"**Triệu chứng bắt buộc khớp:** {diagnosis['required_matched']}/{diagnosis['total_required']}")
                    st.markdown(f"**Triệu chứng hỗ trợ khớp:** {diagnosis['supporting_matched']}/{diagnosis['total_supporting']}")
                
                with col2:
                    dx_data = diagnosis.get('data', {})
                    urgency = dx_data.get('urgency', 'unknown')
                    st.markdown(f"**Mức độ cấp cứu:** {urgency}")
                    
                    if dx_data.get('rule_out_first'):
                        st.warning("⚠️ Cần loại trừ trước")
                
                # Workup recommendations
                if dx_data.get('workup'):
                    st.markdown("**🔬 Xét nghiệm/Cận lâm sàng được khuyến nghị:**")
                    workup = dx_data['workup']
                    if workup.get('immediate'):
                        st.markdown("**Ngay lập tức:**")
                        for test in workup['immediate']:
                            st.markdown(f"- {test}")
                    if workup.get('within_6h'):
                        st.markdown("**Trong 6 giờ:**")
                        for test in workup['within_6h']:
                            st.markdown(f"- {test}")
                    if workup.get('optional'):
                        st.markdown("**Tùy chọn:**")
                        for test in workup['optional']:
                            st.markdown(f"- {test}")
                
                # Management hints
                if dx_data.get('management_hints'):
                    st.markdown("**💡 Gợi ý xử trí:**")
                    st.info(dx_data['management_hints'])
                
                # Link to Disease Encyclopedia
                st.markdown("---")
                st.markdown(f"💡 Xem thêm thông tin về **{diagnosis['diagnosis']}** trong [Bách khoa Bệnh lý](?page=16_📖_Disease_Encyclopedia)")
    else:
        st.warning("Không tìm thấy chẩn đoán phù hợp. Vui lòng thử với các triệu chứng khác hoặc tham khảo bác sĩ.")
    
    # Clear button
    if st.button("🗑️ Xóa kết quả", use_container_width=True):
        if 'symptom_checker_results' in st.session_state:
            del st.session_state['symptom_checker_results']
        st.rerun()

# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về Symptom Checker")
st.markdown("""
**Cách sử dụng:**
1. Chọn các triệu chứng từ danh sách hoặc nhập thủ công
2. Click "Phân tích Triệu chứng"
3. Xem kết quả: mức độ nghiêm trọng, gợi ý chẩn đoán, xét nghiệm được khuyến nghị

**Lưu ý quan trọng:**
- ⚠️ Công cụ này **CHỈ mục đích hỗ trợ** quyết định lâm sàng
- ⚠️ **KHÔNG thay thế** đánh giá lâm sàng và kinh nghiệm của bác sĩ
- ⚠️ Kết quả chỉ mang tính **tham khảo**
- ⚠️ Luôn **tham khảo bác sĩ** trước khi quyết định điều trị
- ⚠️ Nếu có triệu chứng nghiêm trọng, **đến cấp cứu ngay lập tức**

**Triệu chứng cần cấp cứu:**
- Đau ngực đè ép
- Khó thở nặng
- Ngất
- Co giật
- Thay đổi ý thức
- Yếu chi cấp
""")

# Footer
render_standard_footer(disclaimer=True)

