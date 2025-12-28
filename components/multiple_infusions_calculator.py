"""
Multiple Infusions Calculator UI Component
Calculate multiple drugs infusing simultaneously
"""

import streamlit as st
from critical_care.multiple_infusions import (
    InfusionItem,
    add_infusion,
    remove_infusion,
    calculate_multiple_infusions_summary
)
from drugs.cardiovascular_calculator import get_drug_names, get_drug_info
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert


def render_multiple_infusions_calculator():
    """Render multiple infusions calculator interface."""
    
    st.markdown("## 💉 Multiple Infusions Calculator")
    st.markdown("""
    Tính toán nhiều thuốc truyền đồng thời.
    
    **Tính năng:**
    - Thêm/xóa nhiều thuốc
    - Tính tổng thể tích, tốc độ
    - Cảnh báo giới hạn
    - Kiểm tra tương thích (sắp có)
    """)
    
    st.markdown("---")
    
    # Initialize session state
    if "multiple_infusions" not in st.session_state:
        st.session_state.multiple_infusions = []
    
    if "same_bag" not in st.session_state:
        st.session_state.same_bag = False
    
    # Get available drugs
    drug_names = get_drug_names()
    
    # Settings
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "**Cân nặng (kg):**",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="multi_weight"
        )
    
    with col2:
        same_bag = st.checkbox(
            "**Tất cả thuốc trong cùng một chai/bơm**",
            value=st.session_state.same_bag,
            key="multi_same_bag",
            help="Nếu chọn, sẽ tính tổng thể tích trong cùng một chai/bơm"
        )
        st.session_state.same_bag = same_bag
    
    st.markdown("---")
    
    # Add new infusion
    st.markdown("### ➕ Thêm thuốc mới")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        new_drug = st.selectbox(
            "**Thuốc:**",
            drug_names,
            key="multi_new_drug"
        )
    
    with col2:
        new_dose = st.number_input(
            "**Liều (µg/kg/phút):**",
            min_value=0.01,
            max_value=100.0,
            value=0.1,
            step=0.01,
            format="%.2f",
            key="multi_new_dose"
        )
    
    with col3:
        new_method = st.radio(
            "**Phương pháp:**",
            ["syringe_pump_50ml", "iv_bag_500ml"],
            format_func=lambda x: "Bơm 50ml" if x == "syringe_pump_50ml" else "Chai 500ml",
            key="multi_new_method"
        )
    
    with col4:
        new_drop_factor = None
        if new_method == "iv_bag_500ml":
            new_drop_factor = st.selectbox(
                "**Drop factor:**",
                [10, 15, 20, 60],
                index=2,
                key="multi_new_drop"
            )
    
    if st.button("➕ Thêm thuốc", key="multi_add", type="primary"):
        try:
            new_item = add_infusion(
                st.session_state.multiple_infusions,
                new_drug,
                new_dose,
                weight_kg,
                new_method,
                new_drop_factor
            )
            st.success(f"Đã thêm {new_drug}")
            st.rerun()
        except Exception as e:
            st.error(f"Lỗi: {str(e)}")
    
    st.markdown("---")
    
    # Display current infusions
    if st.session_state.multiple_infusions:
        st.markdown("### 📋 Danh sách thuốc đang truyền")
        
        # Summary calculation
        summary = calculate_multiple_infusions_summary(
            st.session_state.multiple_infusions,
            same_bag
        )
        
        # Display each infusion
        for idx, item in enumerate(st.session_state.multiple_infusions):
            with st.expander(f"💉 {item.drug_name} - {item.dose_mcg_kg_min:.2f} µg/kg/phút", expanded=False):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    result = item.calculate()
                    
                    st.markdown(f"**Liều:** {item.dose_mcg_kg_min:.2f} µg/kg/phút")
                    st.markdown(f"**Tốc độ:** {result.get('infusion_rate_ml_hour', 0):.2f} ml/h")
                    if result.get('drop_rate_gtt_min'):
                        st.markdown(f"**Giọt/phút:** {result.get('drop_rate_gtt_min', 0):.1f} gtt/min")
                    st.markdown(f"**Tổng liều:** {result.get('total_dose_mcg_hour', 0):.2f} µg/h")
                
                with col2:
                    if st.button("✏️ Sửa", key=f"multi_edit_{idx}"):
                        st.info("Tính năng sửa sẽ có trong phiên bản sau")
                
                with col3:
                    if st.button("🗑️ Xóa", key=f"multi_delete_{idx}"):
                        remove_infusion(st.session_state.multiple_infusions, idx)
                        st.success("Đã xóa")
                        st.rerun()
        
        st.markdown("---")
        
        # Summary
        st.markdown("### 📊 Tổng hợp")
        
        # Total volume
        total_vol = summary["total_volume"]
        col1, col2 = st.columns(2)
        
        with col1:
            render_result_box(
                "Tổng thể tích",
                f"{total_vol['total_volume_ml']:.1f} ml",
                color="primary",
                icon="💧"
            )
        
        with col2:
            if same_bag:
                bag_info = f"{total_vol['bag_volume_ml']:.0f} ml/bag"
            else:
                bag_info = f"{len(st.session_state.multiple_infusions)} bags"
            render_result_box(
                "Cấu hình",
                bag_info,
                color="info",
                icon="📦"
            )
        
        # Total rate
        total_rate = summary["total_rate"]
        
        metrics = [
            {
                "label": "Tổng tốc độ",
                "value": f"{total_rate['total_rate_ml_hour']:.1f} ml/h",
                "icon": "💉"
            },
            {
                "label": "Tổng liều",
                "value": f"{total_rate['total_dose_mcg_hour']:.1f} µg/h",
                "icon": "💊"
            }
        ]
        
        if total_rate.get('total_drop_rate_gtt_min'):
            metrics.append({
                "label": "Tổng giọt/phút",
                "value": f"{total_rate['total_drop_rate_gtt_min']:.1f} gtt/min",
                "icon": "💧"
            })
        
        render_result_card("Tổng tốc độ truyền", metrics, color="success")
        
        # Validation warnings/errors
        validation = summary["validation"]
        
        if validation["errors"]:
            for error in validation["errors"]:
                render_error_alert(error, title="❌ Lỗi")
        
        if validation["warnings"]:
            for warning in validation["warnings"]:
                render_warning_alert(warning, title="⚠️ Cảnh báo")
        
        if validation["is_valid"] and not validation["warnings"]:
            render_info_alert("Tất cả thông số trong giới hạn an toàn", title="✅ An toàn")
        
        # Clear all button
        st.markdown("---")
        if st.button("🗑️ Xóa tất cả", key="multi_clear_all", type="secondary"):
            st.session_state.multiple_infusions = []
            st.success("Đã xóa tất cả")
            st.rerun()
    
    else:
        st.info("Chưa có thuốc nào. Hãy thêm thuốc ở trên.")
    
    # Compatibility checker
    if st.session_state.multiple_infusions and len(st.session_state.multiple_infusions) > 1:
        st.markdown("---")
        st.markdown("### 🔍 Kiểm tra tương thích")
        
        try:
            from drugs.compatibility_checker import check_multiple_compatibility
            
            # Get list of drug names
            drug_names = [item.drug_name for item in st.session_state.multiple_infusions]
            
            # Check compatibility
            compatibility_result = check_multiple_compatibility(drug_names)
            
            # Display results
            if compatibility_result["all_compatible"] and not compatibility_result["conditional_pairs"]:
                render_info_alert(
                    "✅ Tất cả thuốc tương thích. Có thể trộn an toàn.",
                    title="Tương thích"
                )
            elif compatibility_result["incompatible_pairs"]:
                error_msg = "❌ CÓ THUỐC KHÔNG TƯƠNG THÍCH:\n\n"
                for pair in compatibility_result["incompatible_pairs"]:
                    error_msg += f"  • {pair[0]} và {pair[1]} không tương thích\n"
                error_msg += "\n⚠️ KHÔNG NÊN TRỘN các thuốc này!"
                render_error_alert(error_msg, title="Không tương thích")
            elif compatibility_result["conditional_pairs"]:
                warning_msg = "⚠️ CÓ THUỐC CẦN THEO DÕI:\n\n"
                for pair in compatibility_result["conditional_pairs"]:
                    warning_msg += f"  • {pair[0]} và {pair[1]} cần theo dõi sát\n"
                warning_msg += "\n💡 Có thể trộn nhưng cần theo dõi kỹ."
                render_warning_alert(warning_msg, title="Cần theo dõi")
            
            # Show detailed matrix
            with st.expander("📋 Chi tiết tương thích từng cặp thuốc"):
                from drugs.compatibility_checker import check_compatibility
                
                for i, drug1 in enumerate(drug_names):
                    for j, drug2 in enumerate(drug_names):
                        if i < j:
                            result = check_compatibility(drug1, drug2)
                            
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                if result["status"] == "compatible":
                                    st.success(f"✅ {drug1} ↔ {drug2}: Tương thích")
                                elif result["status"] == "incompatible":
                                    st.error(f"❌ {drug1} ↔ {drug2}: Không tương thích")
                                elif result["status"] == "conditional":
                                    st.warning(f"⚠️ {drug1} ↔ {drug2}: Cần theo dõi")
                                else:
                                    st.info(f"❓ {drug1} ↔ {drug2}: Không rõ")
                            
                            with col2:
                                if result.get("y_site"):
                                    st.caption("Y-site: ✅")
                                else:
                                    st.caption("Y-site: ❌")
                            
                            if result.get("notes"):
                                st.caption(f"  {result['notes']}")
                            
                            if result.get("recommendations"):
                                with st.expander(f"💡 Khuyến nghị cho {drug1} ↔ {drug2}"):
                                    for rec in result["recommendations"]:
                                        st.markdown(f"  • {rec}")
                            
                            st.markdown("---")
        
        except ImportError as e:
            st.warning(f"Compatibility checker chưa sẵn sàng: {str(e)}")
        except Exception as e:
            st.error(f"Lỗi kiểm tra tương thích: {str(e)}")

