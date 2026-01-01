"""
Drug Interaction Checker UI Components
Streamlit components for displaying drug interaction warnings
"""

import streamlit as st
from typing import List, Dict

try:
    from .interaction_checker import DrugInteractionChecker
    from .drug_interactions import SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR
except ImportError:
    from interaction_checker import DrugInteractionChecker
    from drug_interactions import SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR


def render_interaction_warning(interaction: Dict):
    """
    Render a single interaction warning
    
    Args:
        interaction: Interaction dict
    """
    severity = interaction['severity']
    
    # Choose color and icon based on severity
    if severity == SEVERITY_MAJOR:
        st.error(f"🚨 **MAJOR INTERACTION**: {interaction['drug1']} + {interaction['drug2']}")
        with st.expander("Chi tiết tương tác nghiêm trọng", expanded=True):
            st.markdown(f"**Tác dụng:** {interaction['effect']}")
            st.markdown(f"**Cơ chế:** {interaction['mechanism']}")
            st.markdown(f"**⚠️ Xử trí:** {interaction['management']}")
            st.caption(f"Tài liệu: {', '.join(interaction['references'])}")
    
    elif severity == SEVERITY_MODERATE:
        st.warning(f"⚠️ **MODERATE INTERACTION**: {interaction['drug1']} + {interaction['drug2']}")
        with st.expander("Chi tiết tương tác vừa phải"):
            st.markdown(f"**Tác dụng:** {interaction['effect']}")
            st.markdown(f"**Cơ chế:** {interaction['mechanism']}")
            st.markdown(f"**Xử trí:** {interaction['management']}")
            st.caption(f"Tài liệu: {', '.join(interaction['references'])}")
    
    else:  # MINOR
        st.info(f"ℹ️ **MINOR INTERACTION**: {interaction['drug1']} + {interaction['drug2']}")
        with st.expander("Chi tiết tương tác nhẹ"):
            st.markdown(f"**Tác dụng:** {interaction['effect']}")
            st.markdown(f"**Xử trí:** {interaction['management']}")


def render_interaction_summary(summary: Dict):
    """
    Render interaction summary with metrics
    
    Args:
        summary: Summary dict from DrugInteractionChecker
    """
    st.markdown("### 📊 Tổng Kết Tương Tác Thuốc")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Tổng tương tác",
            summary['total_interactions'],
            delta=None
        )
    
    with col2:
        st.metric(
            "🔴 Major",
            summary['major'],
            delta="Nguy hiểm" if summary['major'] > 0 else None,
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            "🟡 Moderate",
            summary['moderate'],
            delta="Theo dõi" if summary['moderate'] > 0 else None,
            delta_color="off"
        )
    
    with col4:
        st.metric(
            "🟢 Minor",
            summary['minor'],
            delta="Nhẹ" if summary['minor'] > 0 else None,
            delta_color="off"
        )
    
    # Risk level indicator
    risk_level = summary['risk_level']
    if risk_level == "HIGH":
        st.error(f"⚠️ **MỨC ĐỘ RỦI RO: {risk_level}** - Tránh dùng chung nếu có thể!")
    elif risk_level == "MODERATE":
        st.warning(f"⚠️ **MỨC ĐỘ RỦI RO: {risk_level}** - Theo dõi bệnh nhân sát")
    elif risk_level == "LOW":
        st.info(f"ℹ️ **MỨC ĐỘ RỦI RO: {risk_level}** - Ít quan trọng lâm sàng")
    else:
        st.success(f"✅ **MỨC ĐỘ RỦI RO: {risk_level}** - Không phát hiện tương tác")


def render_medication_list_with_checker():
    """
    Render medication list with real-time interaction checking
    """
    st.markdown("### 💊 Danh Sách Thuốc Hiện Tại")
    
    # Initialize session state
    if 'medication_list' not in st.session_state:
        st.session_state.medication_list = []
    
    # Add new medication
    col1, col2 = st.columns([3, 1])
    
    with col1:
        new_drug = st.text_input(
            "Thêm thuốc mới",
            placeholder="Nhập tên thuốc...",
            key="new_drug_input"
        )
    
    with col2:
        add_button = st.button("➕ Thêm", use_container_width=True)
    
    # Check for interactions when adding new drug
    if add_button and new_drug:
        checker = DrugInteractionChecker()
        
        if new_drug not in st.session_state.medication_list:
            # Check interactions with current drugs
            new_interactions = checker.check_new_drug(
                st.session_state.medication_list,
                new_drug
            )
            
            if new_interactions:
                st.warning(f"⚠️ Cảnh báo: Thêm {new_drug} sẽ gây {len(new_interactions)} tương tác!")
                
                for interaction in new_interactions:
                    if interaction['severity'] == SEVERITY_MAJOR:
                        st.error(
                            f"🚨 MAJOR: {interaction['drug1']} + {new_drug}\n\n"
                            f"{interaction['effect']}"
                        )
                
                # Ask for confirmation
                confirm = st.checkbox(
                    f"Tôi hiểu rủi ro và vẫn muốn thêm {new_drug}",
                    key=f"confirm_{new_drug}"
                )
                
                if confirm:
                    st.session_state.medication_list.append(new_drug)
                    st.success(f"✅ Đã thêm {new_drug}")
                    st.rerun()
            else:
                # No interactions - add directly
                st.session_state.medication_list.append(new_drug)
                st.success(f"✅ Đã thêm {new_drug} (Không có tương tác)")
                st.rerun()
        else:
            st.warning(f"{new_drug} đã có trong danh sách")
    
    # Display current medications
    if st.session_state.medication_list:
        st.markdown("**Thuốc hiện tại:**")
        
        for idx, drug in enumerate(st.session_state.medication_list):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"{idx + 1}. **{drug}**")
            
            with col2:
                if st.button("🗑️", key=f"remove_{idx}"):
                    st.session_state.medication_list.pop(idx)
                    st.rerun()
        
        # Check all interactions
        if len(st.session_state.medication_list) >= 2:
            st.markdown("---")
            checker = DrugInteractionChecker()
            summary = checker.get_summary(st.session_state.medication_list)
            
            # Show summary
            render_interaction_summary(summary)
            
            # Show detailed interactions
            if summary['interactions']:
                st.markdown("### 📋 Chi Tiết Tương Tác")
                for interaction in summary['interactions']:
                    render_interaction_warning(interaction)
            
            # Show recommendations
            st.markdown("### 💡 Khuyến Nghị Lâm Sàng")
            recommendations = checker.get_recommendations(st.session_state.medication_list)
            for rec in recommendations:
                st.markdown(f"- {rec}")
            
            # Generate report button
            if st.button("📄 Tạo Báo Cáo Chi Tiết"):
                report = checker.generate_report(st.session_state.medication_list)
                st.text_area("Báo cáo tương tác thuốc", report, height=400)
                
                # Download button
                st.download_button(
                    label="⬇️ Tải Báo Cáo",
                    data=report,
                    file_name="drug_interaction_report.txt",
                    mime="text/plain"
                )
    else:
        st.info("Chưa có thuốc nào. Thêm thuốc để kiểm tra tương tác.")
    
    # Clear all button
    if st.session_state.medication_list:
        if st.button("🗑️ Xóa Tất Cả", type="secondary"):
            st.session_state.medication_list = []
            st.rerun()


def render_quick_interaction_check():
    """
    Quick interaction checker for 2 drugs
    """
    st.markdown("### ⚡ Kiểm Tra Nhanh (2 Thuốc)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        drug1 = st.text_input("Thuốc 1", key="quick_drug1")
    
    with col2:
        drug2 = st.text_input("Thuốc 2", key="quick_drug2")
    
    if st.button("🔍 Kiểm Tra", use_container_width=True):
        if drug1 and drug2:
            checker = DrugInteractionChecker()
            interaction = checker.check_pair(drug1, drug2)
            
            if interaction:
                st.markdown(f"### Kết Quả: {drug1} + {drug2}")
                render_interaction_warning({
                    'drug1': drug1,
                    'drug2': drug2,
                    **interaction
                })
            else:
                st.success(f"✅ Không phát hiện tương tác giữa {drug1} và {drug2}")
        else:
            st.warning("Vui lòng nhập cả 2 thuốc")


def render_complete_interaction_checker():
    """
    Complete interaction checker page
    Main entry point
    """
    st.title("⚠️ Kiểm Tra Tương Tác Thuốc")
    
    st.markdown("""
    Công cụ kiểm tra tương tác thuốc giúp phát hiện các tương tác có ý nghĩa lâm sàng 
    giữa các thuốc để đảm bảo an toàn cho người bệnh.
    
    **Phân loại mức độ nghiêm trọng:**
    - 🔴 **MAJOR**: Tránh dùng chung - Có thể gây nguy hiểm tính mạng
    - 🟡 **MODERATE**: Theo dõi sát - Cần điều chỉnh liều hoặc theo dõi
    - 🟢 **MINOR**: Ít quan trọng lâm sàng
    """)
    
    # Tabs
    tab1, tab2 = st.tabs(["📋 Danh Sách Thuốc", "⚡ Kiểm Tra Nhanh"])
    
    with tab1:
        render_medication_list_with_checker()
    
    with tab2:
        render_quick_interaction_check()
    
    # Database info
    with st.expander("ℹ️ Thông Tin Database"):
        from drug_interactions import get_interaction_statistics
        stats = get_interaction_statistics()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Tổng tương tác", stats['total_interactions'])
        
        with col2:
            st.metric("Major", stats['major'])
        
        with col3:
            st.metric("Moderate", stats['moderate'])
        
        st.caption(f"Thuốc có tương tác: {', '.join(stats['drugs_with_interactions'][:10])}...")


# Export
__all__ = [
    'render_interaction_warning',
    'render_interaction_summary',
    'render_medication_list_with_checker',
    'render_quick_interaction_check',
    'render_complete_interaction_checker'
]


# Main
if __name__ == "__main__":
    render_complete_interaction_checker()
