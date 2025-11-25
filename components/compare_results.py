"""
Compare Results Component
Compare calculation results side-by-side (before/after, different patients, etc.)
"""

import streamlit as st
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd


def render_compare_results(
    results_list: List[Dict[str, Any]],
    labels: Optional[List[str]] = None,
    show_differences: bool = True
):
    """
    Render comparison view for multiple calculation results
    
    Args:
        results_list: List of result dictionaries to compare
        labels: Optional labels for each result (e.g., ["Before", "After"])
        show_differences: Highlight differences between results
    """
    if not results_list:
        st.warning("Không có kết quả để so sánh")
        return
    
    if len(results_list) < 2:
        st.warning("Cần ít nhất 2 kết quả để so sánh")
        return
    
    st.subheader("🔀 So Sánh Kết Quả")
    
    # Default labels
    if not labels:
        labels = [f"Kết quả {i+1}" for i in range(len(results_list))]
    
    # Display results side-by-side
    num_cols = len(results_list)
    cols = st.columns(num_cols)
    
    for idx, (result, label) in enumerate(zip(results_list, labels)):
        with cols[idx]:
            st.markdown(f"### {label}")
            
            if isinstance(result, dict):
                # Display as key-value pairs
                for key, value in result.items():
                    st.markdown(f"**{key}:** {value}")
            else:
                st.write(result)
    
    # Differences table
    if show_differences and len(results_list) == 2:
        st.markdown("---")
        st.markdown("### 📊 Bảng So Sánh")
        
        # Extract all keys from both results
        if isinstance(results_list[0], dict) and isinstance(results_list[1], dict):
            all_keys = set(results_list[0].keys()) | set(results_list[1].keys())
            
            comparison_data = []
            for key in sorted(all_keys):
                val1 = results_list[0].get(key, "N/A")
                val2 = results_list[1].get(key, "N/A")
                
                # Calculate difference if numeric
                diff = None
                if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                    diff = val2 - val1
                
                comparison_data.append({
                    'Thông số': key,
                    labels[0]: val1,
                    labels[1]: val2,
                    'Chênh lệch': diff if diff is not None else "N/A"
                })
            
            df = pd.DataFrame(comparison_data)
            st.dataframe(df, use_container_width=True)
            
            # Highlight differences
            st.markdown("**💡 Ghi chú:**")
            for row in comparison_data:
                if row['Chênh lệch'] != "N/A" and row['Chênh lệch'] != 0:
                    st.caption(f"- {row['Thông số']}: {row['Chênh lệch']:+.2f}")


def render_compare_from_history(
    calculator_id: Optional[str] = None,
    max_selections: int = 5
):
    """
    Render UI to select and compare calculations from history
    
    Args:
        calculator_id: Optional filter by calculator
        max_selections: Maximum number of calculations to compare
    """
    from components.calculation_history import get_calculation_history
    
    st.subheader("🔀 So Sánh Từ Lịch Sử")
    
    # Get history
    history = get_calculation_history(calculator_id=calculator_id, limit=50)
    
    if not history:
        st.info("Chưa có lịch sử tính toán để so sánh")
        return
    
    # Selection UI
    st.markdown("**Chọn các tính toán để so sánh:**")
    
    selected_calcs = []
    for calc in history[:20]:  # Show last 20
        label = f"{calc['date']} {calc['time']} - {calc['calculator_name']}"
        if st.checkbox(
            label,
            key=f"compare_select_{calc['id']}",
            value=st.session_state.get(f"compare_selected_{calc['id']}", False)
        ):
            if len(selected_calcs) < max_selections:
                selected_calcs.append(calc)
                st.session_state[f"compare_selected_{calc['id']}"] = True
            else:
                st.warning(f"Tối đa {max_selections} tính toán")
                st.session_state[f"compare_selected_{calc['id']}"] = False
        else:
            st.session_state[f"compare_selected_{calc['id']}"] = False
    
    # Compare button
    if selected_calcs and len(selected_calcs) >= 2:
        if st.button("🔀 So sánh", key="compare_selected"):
            results_list = [calc['results'] for calc in selected_calcs]
            labels = [
                f"{calc['date']} {calc['time']}" for calc in selected_calcs
            ]
            
            render_compare_results(results_list, labels)
    
    # Quick compare: Before/After
    st.markdown("---")
    st.markdown("### ⚡ So Sánh Nhanh: Trước/Sau")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Trước:**")
        before_options = {
            f"{calc['date']} {calc['time']}": calc['id']
            for calc in history[:10]
        }
        before_selected = st.selectbox(
            "Chọn tính toán",
            options=list(before_options.keys()),
            key="compare_before"
        )
    
    with col2:
        st.markdown("**Sau:**")
        after_options = {
            f"{calc['date']} {calc['time']}": calc['id']
            for calc in history[:10]
        }
        after_selected = st.selectbox(
            "Chọn tính toán",
            options=list(after_options.keys()),
            key="compare_after"
        )
    
    if before_selected and after_selected:
        before_id = before_options[before_selected]
        after_id = after_options[after_selected]
        
        before_calc = next((c for c in history if c['id'] == before_id), None)
        after_calc = next((c for c in history if c['id'] == after_id), None)
        
        if before_calc and after_calc:
            if st.button("🔀 So sánh Trước/Sau", key="compare_before_after"):
                render_compare_results(
                    [before_calc['results'], after_calc['results']],
                    labels=["Trước", "Sau"]
                )


def render_compare_current_with_history(
    current_result: Dict[str, Any],
    calculator_id: str,
    calculator_name: str
):
    """
    Compare current calculation result with history
    
    Args:
        current_result: Current calculation result
        calculator_id: Calculator ID
        calculator_name: Calculator name
    """
    from components.calculation_history import get_calculation_history
    
    st.markdown("### 🔀 So Sánh Với Lịch Sử")
    
    # Get recent calculations for this calculator
    history = get_calculation_history(calculator_id=calculator_id, limit=5)
    
    if not history:
        st.info("Chưa có lịch sử để so sánh")
        return
    
    # Select calculation to compare
    compare_options = {
        f"{calc['date']} {calc['time']}": calc['id']
        for calc in history
    }
    
    selected = st.selectbox(
        "Chọn tính toán từ lịch sử để so sánh:",
        options=list(compare_options.keys()),
        key="compare_current_with_history"
    )
    
    if selected:
        selected_id = compare_options[selected]
        selected_calc = next((c for c in history if c['id'] == selected_id), None)
        
        if selected_calc:
            if st.button("🔀 So sánh", key="compare_current"):
                render_compare_results(
                    [selected_calc['results'], current_result],
                    labels=[f"{selected_calc['date']} {selected_calc['time']}", "Hiện tại"]
                )

