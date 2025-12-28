"""
Infusion Safety Checker UI Component
Comprehensive safety checks for infusions
"""

import streamlit as st
from critical_care.safety_checker import (
    check_complete_infusion_safety,
    get_safety_checklist
)
from drugs.cardiovascular_calculator import get_drug_names
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert


def render_safety_checker():
    """Render safety checker interface."""
    
    st.markdown("## ✅ Infusion Safety Checker")
    st.markdown("""
    Kiểm tra an toàn trước khi truyền dịch.
    
    **Tính năng:**
    - Kiểm tra liều vs max dose
    - Kiểm tra tốc độ vs giới hạn
    - Safety checklist
    - Safety score
    """)
    
    st.markdown("---")
    
    # Get available drugs
    drug_names = get_drug_names()
    
    # Input form
    st.markdown("### 💊 Thông tin truyền dịch")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_drug = st.selectbox(
            "**Thuốc:**",
            drug_names,
            key="safety_drug"
        )
    
    with col2:
        dose_mcg_kg_min = st.number_input(
            "**Liều (µg/kg/phút):**",
            min_value=0.01,
            max_value=100.0,
            value=0.1,
            step=0.01,
            format="%.2f",
            key="safety_dose"
        )
    
    with col3:
        weight_kg = st.number_input(
            "**Cân nặng (kg):**",
            min_value=0.1,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="safety_weight"
        )
    
    # Infusion method
    infusion_method = st.radio(
        "**Phương pháp truyền:**",
        ["syringe_pump_50ml", "iv_bag_500ml"],
        format_func=lambda x: "Bơm tiêm điện (50ml)" if x == "syringe_pump_50ml" else "Chai truyền (500ml)",
        key="safety_method"
    )
    
    drop_factor = None
    if infusion_method == "iv_bag_500ml":
        drop_factor = st.selectbox(
            "**Drop factor (gtt/ml):**",
            [10, 15, 20, 60],
            index=2,
            key="safety_drop_factor"
        )
    
    st.markdown("---")
    
    # Check button
    if st.button("🔍 Kiểm tra an toàn", key="safety_check", type="primary", use_container_width=True):
        try:
            # Perform safety check
            result = check_complete_infusion_safety(
                selected_drug,
                dose_mcg_kg_min,
                weight_kg,
                infusion_method,
                drop_factor
            )
            
            result_dict = result.to_dict()
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả kiểm tra an toàn")
            
            # Safety score
            score = result_dict["score"]
            if score >= 90:
                score_color = "success"
                score_icon = "✅"
                score_text = "An toàn"
            elif score >= 70:
                score_color = "warning"
                score_icon = "⚠️"
                score_text = "Cần lưu ý"
            else:
                score_color = "error"
                score_icon = "❌"
                score_text = "Không an toàn"
            
            render_result_box(
                "Safety Score",
                f"{score_icon} {score}/100 - {score_text}",
                color=score_color,
                icon="🛡️"
            )
            
            # Errors
            if result_dict["errors"]:
                st.markdown("---")
                st.markdown("### ❌ Lỗi (Cần sửa ngay)")
                for error in result_dict["errors"]:
                    render_error_alert(error, title="❌ Lỗi")
            
            # Warnings
            if result_dict["warnings"]:
                st.markdown("---")
                st.markdown("### ⚠️ Cảnh báo")
                for warning in result_dict["warnings"]:
                    render_warning_alert(warning, title="⚠️ Cảnh báo")
            
            # Info
            if result_dict["info"]:
                st.markdown("---")
                st.markdown("### ℹ️ Thông tin")
                for info in result_dict["info"]:
                    st.markdown(f"  • {info}")
            
            # Safety status
            if result_dict["is_safe"]:
                st.markdown("---")
                if not result_dict["has_warnings"]:
                    render_info_alert(
                        "✅ Tất cả kiểm tra an toàn đều pass. Có thể tiến hành truyền dịch.",
                        title="An toàn"
                    )
                else:
                    render_warning_alert(
                        "⚠️ Có một số cảnh báo. Vui lòng xem xét kỹ trước khi truyền.",
                        title="Cần lưu ý"
                    )
            else:
                st.markdown("---")
                render_error_alert(
                    "❌ CÓ LỖI AN TOÀN. KHÔNG NÊN TRUYỀN DỊCH cho đến khi sửa các lỗi.",
                    title="Không an toàn"
                )
            
        except Exception as e:
            st.error(f"Lỗi kiểm tra an toàn: {str(e)}")
    
    # Safety checklist
    st.markdown("---")
    st.markdown("### ✅ Safety Checklist")
    st.caption("Checklist an toàn trước khi truyền dịch")
    
    checklist = get_safety_checklist()
    
    for idx, item in enumerate(checklist):
        critical_icon = "🔴" if item["critical"] else "🟡"
        st.checkbox(
            f"{critical_icon} **{item['item']}**: {item['description']}",
            key=f"safety_checklist_{idx}",
            help="Critical" if item["critical"] else "Recommended"
        )
    
    # Safety tips
    with st.expander("💡 Mẹo an toàn"):
        st.markdown("""
        **Trước khi truyền:**
        1. Kiểm tra lại tất cả thông tin
        2. Xác nhận đúng thuốc, đúng bệnh nhân, đúng liều
        3. Kiểm tra tương thích nếu trộn thuốc
        4. Kiểm tra nồng độ pha đã đúng
        
        **Trong khi truyền:**
        1. Theo dõi sát huyết áp, nhịp tim
        2. Kiểm tra tưới máu ngoại vi
        3. Theo dõi tác dụng phụ
        4. Ghi chép lại liều và thời gian
        
        **Sau khi truyền:**
        1. Đánh giá đáp ứng
        2. Điều chỉnh liều nếu cần
        3. Ghi chép vào hồ sơ
        """)

