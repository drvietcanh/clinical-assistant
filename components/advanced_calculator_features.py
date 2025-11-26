"""
Advanced Calculator Features - Wrapper Component
Integrates all advanced features: History, Batch, Compare, Templates, Undo/Redo
"""

import streamlit as st
from typing import Dict, List, Any, Optional, Callable


def render_advanced_features_tabs(
    calculator_id: str,
    calculator_name: str,
    calculator_function: Optional[Callable] = None,
    input_fields: Optional[List[Dict[str, Any]]] = None,
    current_inputs: Optional[Dict[str, Any]] = None,
    current_result: Optional[Dict[str, Any]] = None
):
    """
    Render tabs for all advanced calculator features
    
    Args:
        calculator_id: Calculator ID
        calculator_name: Calculator name
        calculator_function: Optional function for batch calculator
        input_fields: Optional input field definitions for batch calculator
        current_inputs: Optional current input values
        current_result: Optional current calculation result
    """
    from components.calculation_history import render_history_ui, save_calculation_to_history
    from components.batch_calculator import render_batch_calculator
    from components.compare_results import render_compare_from_history, render_compare_current_with_history
    from components.calculation_templates import render_templates_ui
    from components.undo_redo import render_undo_redo_ui, save_state, get_current_state
    
    # Auto-save current calculation to history if result exists
    if current_result and current_inputs:
        # Check if already saved (avoid duplicates)
        save_key = f"history_saved_{calculator_id}_{hash(str(current_inputs))}"
        if not st.session_state.get(save_key, False):
            save_calculation_to_history(
                calculator_id,
                calculator_name,
                current_inputs,
                current_result
            )
            st.session_state[save_key] = True
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📜 Lịch Sử",
        "📊 Batch",
        "🔀 So sánh",
        "📋 Templates",
        "↶ Undo/Redo"
    ])
    
    with tab1:
        render_history_ui(calculator_id=calculator_id, show_actions=True)
    
    with tab2:
        if calculator_function and input_fields:
            render_batch_calculator(
                calculator_function,
                input_fields,
                calculator_name
            )
        else:
            st.info("Batch calculator cần calculator_function và input_fields")
    
    with tab3:
        if current_result:
            render_compare_current_with_history(
                current_result,
                calculator_id,
                calculator_name
            )
            st.markdown("---")
        render_compare_from_history(calculator_id=calculator_id)
    
    with tab4:
        render_templates_ui(calculator_id, calculator_name)
    
    with tab5:
        if current_inputs:
            # Save current state
            save_state(calculator_id, current_inputs)
            
            # Undo/Redo callbacks
            def on_undo(inputs: Dict[str, Any]):
                """Load inputs from undo"""
                for key, value in inputs.items():
                    st.session_state[f"input_{calculator_id}_{key}"] = value
            
            def on_redo(inputs: Dict[str, Any]):
                """Load inputs from redo"""
                for key, value in inputs.items():
                    st.session_state[f"input_{calculator_id}_{key}"] = value
            
            render_undo_redo_ui(calculator_id, on_undo, on_redo)
        else:
            st.info("Nhập giá trị để sử dụng Undo/Redo")


def render_quick_actions(
    calculator_id: str,
    calculator_name: str,
    current_inputs: Optional[Dict[str, Any]] = None,
    current_result: Optional[Dict[str, Any]] = None
):
    """
    Render quick action buttons for advanced features
    
    Args:
        calculator_id: Calculator ID
        calculator_name: Calculator name
        current_inputs: Optional current input values
        current_result: Optional current calculation result
    """
    from components.calculation_history import save_calculation_to_history
    from components.calculation_templates import save_template
    
    st.markdown("### ⚡ Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if current_result and current_inputs:
            if st.button("💾 Lưu vào lịch sử", key=f"quick_save_history_{calculator_id}"):
                save_calculation_to_history(
                    calculator_id,
                    calculator_name,
                    current_inputs,
                    current_result
                )
                st.success("✅ Đã lưu vào lịch sử")
                st.rerun()
    
    with col2:
        if current_inputs:
            template_name = st.text_input(
                "Tên template",
                key=f"quick_template_name_{calculator_id}",
                placeholder="Nhập tên..."
            )
            if template_name and st.button("📋 Lưu template", key=f"quick_save_template_{calculator_id}"):
                save_template(
                    calculator_id,
                    template_name,
                    current_inputs
                )
                st.success(f"✅ Đã lưu template: {template_name}")
                st.rerun()
    
    with col3:
        if st.button("📊 Xem lịch sử", key=f"quick_view_history_{calculator_id}"):
            st.session_state[f"show_history_{calculator_id}"] = True
    
    with col4:
        if st.button("📋 Xem templates", key=f"quick_view_templates_{calculator_id}"):
            st.session_state[f"show_templates_{calculator_id}"] = True
    
    # Show history if requested
    if st.session_state.get(f"show_history_{calculator_id}", False):
        from components.calculation_history import render_history_ui
        st.markdown("---")
        render_history_ui(calculator_id=calculator_id)
        if st.button("❌ Đóng", key=f"close_history_{calculator_id}"):
            st.session_state[f"show_history_{calculator_id}"] = False
            st.rerun()
    
    # Show templates if requested
    if st.session_state.get(f"show_templates_{calculator_id}", False):
        from components.calculation_templates import render_templates_ui
        st.markdown("---")
        render_templates_ui(calculator_id, calculator_name)
        if st.button("❌ Đóng", key=f"close_templates_{calculator_id}"):
            st.session_state[f"show_templates_{calculator_id}"] = False
            st.rerun()

