"""
Formulary Integration
Tích hợp với danh mục thuốc bệnh viện và kiểm tra tình trạng có sẵn
"""

import streamlit as st
from typing import Dict, List, Optional
from .antibiotics_data import ANTIBIOTICS_DATABASE

# Hospital list
VIETNAM_HOSPITALS = {
    "BACH_MAI": "Bệnh viện Bạch Mai",
    "CHO_RAY": "Bệnh viện Chợ Rẫy",
    "108": "Bệnh viện 108",
    "NHI_DONG": "Bệnh viện Nhi Đồng",
    "Y_DUOC_HCM": "Bệnh viện Đại học Y Dược TP.HCM",
    "GENERAL": "Bệnh viện đa khoa tỉnh/thành phố"
}

# Formulary database - Hospital formulary status
# Format: {antibiotic_name: {"available": bool, "formulary": bool, "notes": str, "cost_vnd": float, "hospitals": {hospital_id: status}}}
HOSPITAL_FORMULARY = {
    "Vancomycin": {
        "available": True,
        "formulary": True,
        "restricted": True,
        "restriction_level": "Restricted - ID approval",
        "notes": "Cần phê duyệt của khoa Nhiễm",
        "cost_vnd": 150000,  # Per 500mg vial (approximate)
        "hospitals": {
            "BACH_MAI": {"available": True, "restricted": True},
            "CHO_RAY": {"available": True, "restricted": True},
            "108": {"available": True, "restricted": True},
            "NHI_DONG": {"available": True, "restricted": True},
            "Y_DUOC_HCM": {"available": True, "restricted": True},
            "GENERAL": {"available": True, "restricted": True}
        }
    },
    "Ceftriaxone": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn, không hạn chế",
        "cost_vnd": 45000,  # Per 1g vial (approximate)
        "hospitals": {
            "BACH_MAI": {"available": True, "restricted": False},
            "CHO_RAY": {"available": True, "restricted": False},
            "108": {"available": True, "restricted": False},
            "NHI_DONG": {"available": True, "restricted": False},
            "Y_DUOC_HCM": {"available": True, "restricted": False},
            "GENERAL": {"available": True, "restricted": False}
        }
    },
    "Piperacillin-Tazobactam": {
        "available": True,
        "formulary": True,
        "restricted": True,
        "restriction_level": "Restricted - Severe infections",
        "notes": "Chỉ dùng cho nhiễm khuẩn nặng"
    },
    "Meropenem": {
        "available": True,
        "formulary": True,
        "restricted": True,
        "restriction_level": "Restricted - ID approval",
        "notes": "Cần phê duyệt khoa Nhiễm, chỉ dùng khi kháng đa thuốc"
    },
    "Imipenem-Cilastatin": {
        "available": True,
        "formulary": True,
        "restricted": True,
        "restriction_level": "Restricted - ID approval",
        "notes": "Cần phê duyệt khoa Nhiễm"
    },
    "Cefepime": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn"
    },
    "Ceftazidime": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn"
    },
    "Linezolid": {
        "available": True,
        "formulary": True,
        "restricted": True,
        "restriction_level": "Restricted - ID approval",
        "notes": "Cần phê duyệt khoa Nhiễm, giá cao"
    },
    "Daptomycin": {
        "available": False,
        "formulary": False,
        "restricted": True,
        "restriction_level": "Not available",
        "notes": "Không có trong formulary, cần đặt hàng đặc biệt"
    },
    "Colistin": {
        "available": True,
        "formulary": True,
        "restricted": True,
        "restriction_level": "Restricted - ID approval",
        "notes": "Cần phê duyệt khoa Nhiễm, chỉ dùng khi kháng đa thuốc"
    },
    "Gentamicin": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn"
    },
    "Amikacin": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn"
    },
    "Levofloxacin": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn"
    },
    "Ciprofloxacin": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn"
    },
    "Azithromycin": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn"
    },
    "Clindamycin": {
        "available": True,
        "formulary": True,
        "restricted": False,
        "notes": "Có sẵn"
    },
}

# Default status for antibiotics not in formulary
DEFAULT_FORMULARY_STATUS = {
    "available": True,
    "formulary": True,
    "restricted": False,
    "notes": "Kiểm tra với khoa Dược để xác nhận"
}


def get_formulary_status(antibiotic_name: str) -> Dict:
    """Get formulary status for an antibiotic"""
    return HOSPITAL_FORMULARY.get(antibiotic_name, DEFAULT_FORMULARY_STATUS.copy())


def check_availability(antibiotic_names: List[str]) -> Dict:
    """Check availability for multiple antibiotics"""
    results = {}
    
    for ab_name in antibiotic_names:
        status = get_formulary_status(ab_name)
        results[ab_name] = status
    
    return results


def get_restricted_antibiotics() -> List[str]:
    """Get list of restricted antibiotics"""
    restricted = []
    for ab_name, status in HOSPITAL_FORMULARY.items():
        if status.get("restricted", False):
            restricted.append(ab_name)
    return restricted


def get_alternative_if_unavailable(antibiotic_name: str) -> Optional[str]:
    """Suggest alternative if antibiotic is unavailable"""
    alternatives = {
        "Daptomycin": "Vancomycin",
        "Linezolid": "Vancomycin",
        "Meropenem": "Piperacillin-Tazobactam",
        "Imipenem-Cilastatin": "Meropenem",
    }
    
    return alternatives.get(antibiotic_name)


def render_formulary_checker():
    """Render Formulary Checker UI"""
    
    st.markdown("### 🏥 Kiểm tra Formulary & Tình trạng Có sẵn")
    st.caption("Kiểm tra kháng sinh có trong danh mục thuốc bệnh viện và tình trạng hạn chế")
    
    st.info("""
    **💡 Lưu ý:**
    - Dữ liệu formulary có thể khác nhau giữa các bệnh viện
    - Luôn kiểm tra với khoa Dược để xác nhận tình trạng thực tế
    - Các kháng sinh hạn chế cần phê duyệt trước khi sử dụng
    - Chi phí là ước tính, có thể thay đổi theo từng bệnh viện
    """)
    
    # Hospital selection
    selected_hospital = st.selectbox(
        "🏥 Chọn bệnh viện:",
        options=list(VIETNAM_HOSPITALS.keys()),
        format_func=lambda x: VIETNAM_HOSPITALS[x],
        key="formulary_hospital",
        help="Chọn bệnh viện để kiểm tra formulary cụ thể"
    )
    
    # Mode selection
    mode = st.radio(
        "Chế độ:",
        ["🔍 Kiểm tra đơn lẻ", "📋 Kiểm tra nhiều kháng sinh", "📊 Danh sách hạn chế", "💰 So sánh chi phí"],
        key="formulary_mode"
    )
    
    if mode == "🔍 Kiểm tra đơn lẻ":
        st.markdown("#### 🔍 Kiểm tra Đơn lẻ")
        
        antibiotic_name = st.selectbox(
            "Chọn kháng sinh:",
            options=sorted(list(ANTIBIOTICS_DATABASE.keys())),
            key="formulary_single_ab"
        )
        
        if st.button("🔍 Kiểm tra", type="primary", use_container_width=True):
            status = get_formulary_status(antibiotic_name)
            
            # Check hospital-specific status
            hospital_status = None
            if "hospitals" in status and selected_hospital in status["hospitals"]:
                hospital_status = status["hospitals"][selected_hospital]
            
            st.markdown("---")
            st.markdown("#### 📊 Kết Quả")
            
            # Status display
            if status["available"] and status["formulary"]:
                if status.get("restricted", False) or (hospital_status and hospital_status.get("restricted", False)):
                    color = "#ff9800"
                    icon = "⚠️"
                    message = "Có sẵn nhưng HẠN CHẾ"
                else:
                    color = "#4caf50"
                    icon = "✅"
                    message = "Có sẵn"
            elif not status["formulary"]:
                color = "#f44336"
                icon = "❌"
                message = "Không có trong formulary"
            else:
                color = "#757575"
                icon = "❓"
                message = "Không rõ"
            
            # Cost information
            cost_info = ""
            if "cost_vnd" in status and status["cost_vnd"]:
                cost_info = f'<p style="margin: 5px 0;"><strong>Chi phí (ước tính):</strong> {status["cost_vnd"]:,.0f} VNĐ</p>'
            
            st.markdown(f"""
            <div style='
                background: {color};
                color: white;
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 20px;
            '>
                <h2 style='margin: 0 0 10px 0; color: white;'>{icon} {message}</h2>
                <p style='margin: 5px 0;'><strong>Kháng sinh:</strong> {antibiotic_name}</p>
                <p style='margin: 5px 0;'><strong>Bệnh viện:</strong> {VIETNAM_HOSPITALS[selected_hospital]}</p>
                {f'<p style="margin: 5px 0;"><strong>Mức độ hạn chế:</strong> {status.get("restriction_level", "N/A")}</p>' if status.get("restricted") or (hospital_status and hospital_status.get("restricted")) else ""}
                {cost_info}
                {f'<p style="margin: 5px 0;"><strong>Ghi chú:</strong> {status.get("notes", "")}</p>' if status.get("notes") else ""}
            </div>
            """, unsafe_allow_html=True)
            
            # Alternative suggestion
            if not status["available"] or not status["formulary"]:
                alternative = get_alternative_if_unavailable(antibiotic_name)
                if alternative:
                    st.info(f"💡 **Gợi ý thay thế:** {alternative}")
            
            # Restrictions info
            if status.get("restricted", False):
                st.warning(f"""
                **⚠️ Kháng sinh hạn chế:**
                - {status.get("restriction_level", "Cần phê duyệt")}
                - {status.get("notes", "")}
                - Vui lòng liên hệ khoa Nhiễm hoặc khoa Dược để được phê duyệt
                """)
    
    elif mode == "📋 Kiểm tra nhiều kháng sinh":
        st.markdown("#### 📋 Kiểm tra Nhiều Kháng Sinh")
        
        antibiotic_names = st.multiselect(
            "Chọn kháng sinh (có thể chọn nhiều):",
            options=sorted(list(ANTIBIOTICS_DATABASE.keys())),
            key="formulary_multi_ab"
        )
        
        if st.button("🔍 Kiểm tra Tất cả", type="primary", use_container_width=True):
            if not antibiotic_names:
                st.warning("⚠️ Vui lòng chọn ít nhất một kháng sinh")
            else:
                results = check_availability(antibiotic_names)
                
                st.markdown("---")
                st.markdown("#### 📊 Kết Quả")
                
                # Group by status
                available = []
                restricted = []
                unavailable = []
                
                for ab_name, status in results.items():
                    if not status["available"] or not status["formulary"]:
                        unavailable.append((ab_name, status))
                    elif status.get("restricted", False):
                        restricted.append((ab_name, status))
                    else:
                        available.append((ab_name, status))
                
                # Display available
                if available:
                    st.success(f"✅ **Có sẵn ({len(available)}):**")
                    for ab_name, status in available:
                        st.markdown(f"- **{ab_name}**")
                
                # Display restricted
                if restricted:
                    st.warning(f"⚠️ **Hạn chế ({len(restricted)}):**")
                    for ab_name, status in restricted:
                        st.markdown(f"- **{ab_name}**: {status.get('restriction_level', 'Cần phê duyệt')}")
                
                # Display unavailable
                if unavailable:
                    st.error(f"❌ **Không có sẵn ({len(unavailable)}):**")
                    for ab_name, status in unavailable:
                        st.markdown(f"- **{ab_name}**: {status.get('notes', 'Không có trong formulary')}")
                        alternative = get_alternative_if_unavailable(ab_name)
                        if alternative:
                            st.caption(f"  💡 Gợi ý thay thế: {alternative}")
    
    elif mode == "💰 So sánh chi phí":
        st.markdown("#### 💰 So Sánh Chi Phí")
        
        antibiotic_names = st.multiselect(
            "Chọn kháng sinh để so sánh chi phí:",
            options=sorted(list(ANTIBIOTICS_DATABASE.keys())),
            key="formulary_cost_comparison"
        )
        
        if st.button("💰 So Sánh Chi Phí", type="primary", use_container_width=True):
            if not antibiotic_names:
                st.warning("⚠️ Vui lòng chọn ít nhất một kháng sinh")
            else:
                import pandas as pd
                
                cost_data = []
                for ab_name in antibiotic_names:
                    status = get_formulary_status(ab_name)
                    cost_data.append({
                        "Kháng sinh": ab_name,
                        "Chi phí (VNĐ)": status.get("cost_vnd", 0) if status.get("cost_vnd") else 0,
                        "Có sẵn": "✅" if status.get("available") and status.get("formulary") else "❌",
                        "Hạn chế": "⚠️" if status.get("restricted") else "✅",
                        "Ghi chú": status.get("notes", "")
                    })
                
                df_cost = pd.DataFrame(cost_data)
                df_cost = df_cost[df_cost["Chi phí (VNĐ)"] > 0]  # Only show drugs with cost data
                
                if not df_cost.empty:
                    st.dataframe(df_cost, use_container_width=True, hide_index=True)
                    
                    # Visual comparison
                    try:
                        import plotly.graph_objects as go
                        fig = go.Figure(data=[
                            go.Bar(
                                x=df_cost["Kháng sinh"],
                                y=df_cost["Chi phí (VNĐ)"],
                                marker_color='#4CAF50',
                                text=[f"{cost:,.0f} VNĐ" for cost in df_cost["Chi phí (VNĐ)"]],
                                textposition='outside'
                            )
                        ])
                        fig.update_layout(
                            title='So Sánh Chi Phí Kháng Sinh',
                            xaxis_title='Kháng sinh',
                            yaxis_title='Chi phí (VNĐ)',
                            height=400
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    except ImportError:
                        pass
                else:
                    st.info("💡 Chưa có dữ liệu chi phí cho các kháng sinh được chọn")
    
    else:  # Restricted list
        st.markdown("#### 📊 Danh sách Kháng Sinh Hạn Chế")
        
        restricted = get_restricted_antibiotics()
        
        if restricted:
            st.warning(f"⚠️ **{len(restricted)} kháng sinh hạn chế:**")
            
            for ab_name in sorted(restricted):
                status = get_formulary_status(ab_name)
                with st.expander(f"🔒 {ab_name}", expanded=False):
                    st.markdown(f"**Mức độ hạn chế:** {status.get('restriction_level', 'Cần phê duyệt')}")
                    if status.get("cost_vnd"):
                        st.markdown(f"**Chi phí (ước tính):** {status.get('cost_vnd'):,.0f} VNĐ")
                    st.markdown(f"**Ghi chú:** {status.get('notes', '')}")
                    st.info("💡 Liên hệ khoa Nhiễm hoặc khoa Dược để được phê duyệt")
        else:
            st.info("Không có kháng sinh nào trong danh sách hạn chế")
    
    # Information section
    with st.expander("📚 Thông tin về Formulary", expanded=False):
        st.markdown("""
        **Formulary là gì?**
        - Danh mục thuốc được phê duyệt sử dụng tại bệnh viện
        - Được quản lý bởi Hội đồng Thuốc và Điều trị
        
        **Kháng sinh hạn chế:**
        - Cần phê duyệt trước khi sử dụng
        - Thường là kháng sinh phổ rộng, giá cao, hoặc có nguy cơ kháng thuốc
        - Mục đích: Quản lý kháng sinh tốt hơn, giảm kháng thuốc
        
        **Quy trình phê duyệt:**
        1. Đánh giá lâm sàng
        2. Xác nhận chỉ định phù hợp
        3. Phê duyệt bởi khoa Nhiễm hoặc khoa Dược
        4. Theo dõi và đánh giá hiệu quả
        
        **Lưu ý:**
        - Dữ liệu formulary có thể khác nhau giữa các bệnh viện
        - Luôn kiểm tra với khoa Dược để xác nhận
        """)
