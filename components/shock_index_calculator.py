"""
Shock Index Calculator UI Component
Calculate shock index for early shock detection
"""

import streamlit as st
from critical_care.shock_index import (
    calculate_shock_index,
    add_shock_index_to_history,
    get_shock_index_trend,
    get_shock_index_reference
)
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert


def render_shock_index_calculator():
    """Render shock index calculator interface."""
    
    st.markdown("## ⚡ Shock Index Calculator")
    st.markdown("""
    Tính shock index để phát hiện sốc sớm.
    
    **Tính năng:**
    - Tính shock index (HR/SBP)
    - Phân loại mức độ (Bình thường/Tăng/Cao)
    - Cảnh báo sốc
    - Khuyến nghị điều trị
    - Lưu lịch sử đánh giá
    """)
    
    st.markdown("---")
    
    # Initialize session state
    if "shock_index_history" not in st.session_state:
        st.session_state.shock_index_history = []
    
    # Shock Index Assessment
    st.markdown("### 📊 Thông số lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        heart_rate = st.number_input(
            "**Nhịp tim (bpm):**",
            min_value=30.0,
            max_value=250.0,
            value=80.0,
            step=1.0,
            format="%.0f",
            key="si_hr"
        )
    
    with col2:
        systolic_bp = st.number_input(
            "**Huyết áp tâm thu (mmHg):**",
            min_value=40.0,
            max_value=250.0,
            value=120.0,
            step=1.0,
            format="%.0f",
            key="si_sbp"
        )
    
    # Calculate MAP if needed
    if systolic_bp > 0:
        # Estimate MAP (rough approximation: MAP ≈ SBP - 1/3(SBP-DBP))
        # Assuming DBP ≈ 2/3 of SBP for normal
        estimated_map = systolic_bp * 0.67
        st.caption(f"**MAP ước tính:** ~{estimated_map:.0f} mmHg (nếu DBP = {systolic_bp*0.67:.0f} mmHg)")
    
    notes = st.text_area(
        "**Ghi chú (tùy chọn):**",
        value="",
        key="si_notes",
        placeholder="Ví dụ: Bệnh nhân sốc nhiễm khuẩn, đã truyền dịch"
    )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🧮 Tính Shock Index", key="si_calculate", type="primary", use_container_width=True):
        try:
            result = calculate_shock_index(heart_rate, systolic_bp)
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả Shock Index")
            
            # Shock index
            si = result["shock_index"]
            classification = result["classification"]
            severity = result["severity"]
            risk_level = result["risk_level"]
            
            # Color based on risk
            if risk_level == "Thấp":
                color = "success"
                icon = "✅"
            elif risk_level == "Trung bình":
                color = "warning"
                icon = "⚠️"
            else:
                color = "error"
                icon = "❌"
            
            render_result_box(
                "Shock Index",
                f"{icon} {si} - {classification}",
                color=color,
                icon="⚡"
            )
            
            # Formula
            st.markdown("---")
            st.markdown("### 📐 Công thức")
            st.code(f"""
Shock Index = Heart Rate / Systolic BP
            = {heart_rate} / {systolic_bp}
            = {si}
            """)
            
            # Severity and risk
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                render_result_box(
                    "Mức độ",
                    severity,
                    color=color
                )
            with col2:
                render_result_box(
                    "Nguy cơ",
                    risk_level,
                    color=color
                )
            
            # Interpretation
            if result.get("interpretation"):
                st.markdown("---")
                st.markdown("### 💡 Đánh giá")
                for item in result["interpretation"]:
                    if "❌" in item:
                        render_error_alert(item.replace("❌ ", ""), title="❌ Cảnh báo")
                    elif "⚠️" in item:
                        render_warning_alert(item.replace("⚠️ ", ""), title="⚠️ Lưu ý")
                    else:
                        st.markdown(f"  • {item}")
            
            # Clinical context
            if result.get("clinical_context"):
                st.markdown("---")
                st.markdown("### 🔍 Bối cảnh lâm sàng")
                for item in result["clinical_context"]:
                    if "⚠️" in item:
                        render_warning_alert(item.replace("⚠️ ", ""), title="⚠️")
                    else:
                        st.markdown(f"  • {item}")
            
            # Recommendations
            if result.get("recommendations"):
                st.markdown("---")
                st.markdown("### 💡 Khuyến nghị")
                for rec in result["recommendations"]:
                    if "🔴" in rec:
                        st.markdown(f"**{rec}**")
                    elif "⚠️" in rec:
                        render_warning_alert(rec.replace("⚠️ ", ""), title="⚠️")
                    else:
                        st.markdown(f"  {rec}")
            
            # Add to history button
            st.markdown("---")
            if st.button("➕ Thêm vào lịch sử", key="si_add_history", type="secondary"):
                score_dict = add_shock_index_to_history(
                    st.session_state.shock_index_history,
                    heart_rate,
                    systolic_bp,
                    notes if notes else None
                )
                st.success("Đã thêm vào lịch sử!")
                st.rerun()
            
        except ValueError as e:
            st.error(f"Lỗi: {str(e)}")
        except Exception as e:
            st.error(f"Lỗi không xác định: {str(e)}")
    
    # Shock Index History
    if st.session_state.shock_index_history:
        st.markdown("---")
        st.markdown("### 📋 Lịch sử đánh giá")
        
        # Trend analysis
        trend = get_shock_index_trend(st.session_state.shock_index_history)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            render_result_box(
                "Số lần đánh giá",
                f"{trend['total_assessments']} lần",
                color="primary"
            )
        with col2:
            render_result_box(
                "Shock Index đầu tiên",
                f"{trend['first_index']}",
                color="info"
            )
        with col3:
            render_result_box(
                "Shock Index gần nhất",
                f"{trend['last_index']}",
                color="success" if trend.get("worsening") == False else "error" if trend.get("worsening") == True else "info"
            )
        
        # Trend
        if trend["change"] != 0:
            st.markdown("---")
            trend_color = "success" if trend.get("worsening") == False else "error"
            render_result_box(
                "Diễn biến",
                f"{trend['trend']} ({trend['change']:+.2f})",
                color=trend_color
            )
        
        # History table
        st.markdown("---")
        with st.expander("📊 Chi tiết lịch sử"):
            import pandas as pd
            
            history_data = []
            for idx, score in enumerate(st.session_state.shock_index_history, 1):
                history_data.append({
                    "Lần": idx,
                    "Thời gian": score.get("timestamp", "N/A")[:19] if score.get("timestamp") else "N/A",
                    "Nhịp tim": f"{score.get('heart_rate', 0):.0f} bpm",
                    "Huyết áp": f"{score.get('systolic_bp', 0):.0f} mmHg",
                    "Shock Index": f"{score.get('shock_index', 0):.2f}",
                    "Phân loại": score.get("classification", "N/A"),
                    "Ghi chú": score.get("notes", "-")
                })
            
            if history_data:
                df = pd.DataFrame(history_data)
                st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Clear history
        if st.button("🗑️ Xóa lịch sử", key="si_clear_history", type="secondary"):
            st.session_state.shock_index_history = []
            st.success("Đã xóa lịch sử!")
            st.rerun()
    
    # Reference guide
    with st.expander("📖 Hướng dẫn Shock Index"):
        reference = get_shock_index_reference()
        
        st.markdown("### Công thức:")
        st.code(reference["formula"])
        
        st.markdown("### Phân loại:")
        st.markdown(f"  • **Bình thường:** {reference['normal']}")
        st.markdown(f"  • **Tăng:** {reference['elevated']}")
        st.markdown(f"  • **Cao:** {reference['high']}")
        
        st.markdown("---")
        st.markdown("### Ý nghĩa lâm sàng:")
        for key, value in reference["clinical_significance"].items():
            st.markdown(f"  • **{key.capitalize()}:** {value}")
        
        st.markdown("---")
        st.markdown("### Lưu ý:")
        for note in reference["notes"]:
            st.markdown(f"  • {note}")
        
        st.markdown("---")
        st.markdown("### Ví dụ:")
        st.markdown("""
        - **HR = 100 bpm, SBP = 100 mmHg:** SI = 1.0 (Tăng)
        - **HR = 120 bpm, SBP = 90 mmHg:** SI = 1.33 (Cao - Sốc)
        - **HR = 80 bpm, SBP = 120 mmHg:** SI = 0.67 (Bình thường)
        """)

