"""
Undo/Redo System for Calculations
Track input changes and allow undo/redo
"""

import streamlit as st
from typing import Dict, Any, Optional, List
from datetime import datetime


def init_undo_redo_state(calculator_id: str):
    """Initialize undo/redo state for a calculator"""
    state_key = f"undo_redo_{calculator_id}"
    
    if state_key not in st.session_state:
        st.session_state[state_key] = {
            'history': [],
            'current_index': -1,
            'max_history': 20
        }


def save_state(calculator_id: str, inputs: Dict[str, Any], description: Optional[str] = None):
    """
    Save current state to undo/redo history
    
    Args:
        calculator_id: Calculator ID
        inputs: Current input values
        description: Optional description of the change
    """
    init_undo_redo_state(calculator_id)
    state_key = f"undo_redo_{calculator_id}"
    state = st.session_state[state_key]
    
    # Create state snapshot
    snapshot = {
        'inputs': inputs.copy(),
        'timestamp': datetime.now().isoformat(),
        'description': description or "Input change"
    }
    
    # Remove any states after current index (if we're in the middle of history)
    if state['current_index'] < len(state['history']) - 1:
        state['history'] = state['history'][:state['current_index'] + 1]
    
    # Add new state
    state['history'].append(snapshot)
    state['current_index'] = len(state['history']) - 1
    
    # Limit history size
    if len(state['history']) > state['max_history']:
        state['history'] = state['history'][-state['max_history']:]
        state['current_index'] = len(state['history']) - 1


def undo(calculator_id: str) -> Optional[Dict[str, Any]]:
    """
    Undo to previous state
    
    Args:
        calculator_id: Calculator ID
    
    Returns:
        Previous state inputs or None
    """
    init_undo_redo_state(calculator_id)
    state_key = f"undo_redo_{calculator_id}"
    state = st.session_state[state_key]
    
    if state['current_index'] > 0:
        state['current_index'] -= 1
        return state['history'][state['current_index']]['inputs']
    
    return None


def redo(calculator_id: str) -> Optional[Dict[str, Any]]:
    """
    Redo to next state
    
    Args:
        calculator_id: Calculator ID
    
    Returns:
        Next state inputs or None
    """
    init_undo_redo_state(calculator_id)
    state_key = f"undo_redo_{calculator_id}"
    state = st.session_state[state_key]
    
    if state['current_index'] < len(state['history']) - 1:
        state['current_index'] += 1
        return state['history'][state['current_index']]['inputs']
    
    return None


def can_undo(calculator_id: str) -> bool:
    """Check if undo is possible"""
    init_undo_redo_state(calculator_id)
    state_key = f"undo_redo_{calculator_id}"
    state = st.session_state[state_key]
    return state['current_index'] > 0


def can_redo(calculator_id: str) -> bool:
    """Check if redo is possible"""
    init_undo_redo_state(calculator_id)
    state_key = f"undo_redo_{calculator_id}"
    state = st.session_state[state_key]
    return state['current_index'] < len(state['history']) - 1


def get_current_state(calculator_id: str) -> Optional[Dict[str, Any]]:
    """Get current state from history"""
    init_undo_redo_state(calculator_id)
    state_key = f"undo_redo_{calculator_id}"
    state = st.session_state[state_key]
    
    if state['history'] and 0 <= state['current_index'] < len(state['history']):
        return state['history'][state['current_index']]['inputs']
    
    return None


def clear_history(calculator_id: str):
    """Clear undo/redo history"""
    state_key = f"undo_redo_{calculator_id}"
    if state_key in st.session_state:
        st.session_state[state_key] = {
            'history': [],
            'current_index': -1,
            'max_history': 20
        }


def render_undo_redo_ui(calculator_id: str, on_undo: callable, on_redo: callable):
    """
    Render undo/redo UI buttons
    
    Args:
        calculator_id: Calculator ID
        on_undo: Callback function when undo is clicked (receives inputs dict)
        on_redo: Callback function when redo is clicked (receives inputs dict)
    """
    init_undo_redo_state(calculator_id)
    
    col1, col2, col3 = st.columns([1, 1, 4])
    
    with col1:
        undo_disabled = not can_undo(calculator_id)
        if st.button("↶ Undo", disabled=undo_disabled, key=f"undo_{calculator_id}"):
            inputs = undo(calculator_id)
            if inputs:
                on_undo(inputs)
                st.rerun()
    
    with col2:
        redo_disabled = not can_redo(calculator_id)
        if st.button("↷ Redo", disabled=redo_disabled, key=f"redo_{calculator_id}"):
            inputs = redo(calculator_id)
            if inputs:
                on_redo(inputs)
                st.rerun()
    
    with col3:
        # Show history info
        state_key = f"undo_redo_{calculator_id}"
        if state_key in st.session_state:
            state = st.session_state[state_key]
            if state['history']:
                current_pos = state['current_index'] + 1
                total = len(state['history'])
                st.caption(f"History: {current_pos}/{total}")
                
                # History dropdown
                with st.expander("📜 Xem lịch sử", expanded=False):
                    for idx, snapshot in enumerate(state['history']):
                        is_current = idx == state['current_index']
                        marker = "👉" if is_current else "  "
                        st.caption(f"{marker} {snapshot['description']} - {snapshot['timestamp'][:19]}")
                        
                        if st.button("📥 Load", key=f"load_history_{calculator_id}_{idx}"):
                            state['current_index'] = idx
                            on_undo(snapshot['inputs'])
                            st.rerun()


def auto_save_on_change(calculator_id: str, input_key: str, value: Any):
    """
    Automatically save state when input changes
    Call this when an input value changes
    
    Args:
        calculator_id: Calculator ID
        input_key: Input field key
        value: New value
    """
    # Get all current inputs for this calculator
    current_inputs = {}
    for key in st.session_state.keys():
        if key.startswith(f"input_{calculator_id}_"):
            field_name = key.replace(f"input_{calculator_id}_", "")
            current_inputs[field_name] = st.session_state[key]
    
    # Update the changed input
    field_name = input_key.replace(f"input_{calculator_id}_", "")
    current_inputs[field_name] = value
    
    # Save state
    save_state(calculator_id, current_inputs, f"Changed {field_name}")

