"""
Calculation History Manager
Manages calculation history with metadata, search, and export
"""

import streamlit as st
from datetime import datetime
from typing import Dict, List, Optional, Any
import json


def init_history_state():
    """Initialize calculation history in session state"""
    if 'calculation_history' not in st.session_state:
        st.session_state.calculation_history = []
    
    if 'history_max_size' not in st.session_state:
        st.session_state.history_max_size = 50  # Last 50 calculations


def save_calculation_to_history(
    calculator_id: str,
    calculator_name: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Save a calculation to history
    
    Args:
        calculator_id: ID of the calculator
        calculator_name: Name of the calculator
        inputs: Input values used
        results: Calculation results
        metadata: Optional metadata (patient_id, notes, etc.)
    
    Returns:
        Calculation ID
    """
    init_history_state()
    
    calculation_id = f"calc_{len(st.session_state.calculation_history)}_{datetime.now().timestamp()}"
    
    calculation_record = {
        'id': calculation_id,
        'calculator_id': calculator_id,
        'calculator_name': calculator_name,
        'inputs': inputs,
        'results': results,
        'metadata': metadata or {},
        'timestamp': datetime.now().isoformat(),
        'date': datetime.now().strftime('%Y-%m-%d'),
        'time': datetime.now().strftime('%H:%M:%S')
    }
    
    # Add to beginning
    st.session_state.calculation_history.insert(0, calculation_record)
    
    # Limit to max size
    if len(st.session_state.calculation_history) > st.session_state.history_max_size:
        st.session_state.calculation_history = st.session_state.calculation_history[:st.session_state.history_max_size]
    
    return calculation_id


def get_calculation_history(
    calculator_id: Optional[str] = None,
    limit: Optional[int] = None,
    date_filter: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get calculation history with optional filters
    
    Args:
        calculator_id: Filter by calculator ID
        limit: Maximum number of results
        date_filter: Filter by date (YYYY-MM-DD)
    
    Returns:
        List of calculation records
    """
    init_history_state()
    
    history = st.session_state.calculation_history
    
    # Filter by calculator
    if calculator_id:
        history = [calc for calc in history if calc['calculator_id'] == calculator_id]
    
    # Filter by date
    if date_filter:
        history = [calc for calc in history if calc['date'] == date_filter]
    
    # Apply limit
    if limit:
        history = history[:limit]
    
    return history


def get_calculation_by_id(calculation_id: str) -> Optional[Dict[str, Any]]:
    """Get a specific calculation by ID"""
    init_history_state()
    
    for calc in st.session_state.calculation_history:
        if calc['id'] == calculation_id:
            return calc
    
    return None


def delete_calculation(calculation_id: str) -> bool:
    """Delete a calculation from history"""
    init_history_state()
    
    initial_count = len(st.session_state.calculation_history)
    st.session_state.calculation_history = [
        calc for calc in st.session_state.calculation_history
        if calc['id'] != calculation_id
    ]
    
    return len(st.session_state.calculation_history) < initial_count


def clear_history(calculator_id: Optional[str] = None) -> int:
    """
    Clear calculation history
    
    Args:
        calculator_id: If provided, only clear history for this calculator
    
    Returns:
        Number of calculations cleared
    """
    init_history_state()
    
    if calculator_id:
        initial_count = len(st.session_state.calculation_history)
        st.session_state.calculation_history = [
            calc for calc in st.session_state.calculation_history
            if calc['calculator_id'] != calculator_id
        ]
        return initial_count - len(st.session_state.calculation_history)
    else:
        count = len(st.session_state.calculation_history)
        st.session_state.calculation_history = []
        return count


def search_history(query: str, calculator_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Search calculation history
    
    Args:
        query: Search query (searches in calculator name, inputs, results)
        calculator_id: Optional filter by calculator
    
    Returns:
        List of matching calculations
    """
    init_history_state()
    
    history = get_calculation_history(calculator_id=calculator_id)
    query_lower = query.lower()
    
    results = []
    for calc in history:
        # Search in calculator name
        if query_lower in calc['calculator_name'].lower():
            results.append(calc)
            continue
        
        # Search in inputs
        inputs_str = json.dumps(calc['inputs'], default=str).lower()
        if query_lower in inputs_str:
            results.append(calc)
            continue
        
        # Search in results
        results_str = json.dumps(calc['results'], default=str).lower()
        if query_lower in results_str:
            results.append(calc)
            continue
        
        # Search in metadata
        if calc.get('metadata'):
            metadata_str = json.dumps(calc['metadata'], default=str).lower()
            if query_lower in metadata_str:
                results.append(calc)
    
    return results


def export_history(format: str = 'json', calculator_id: Optional[str] = None) -> str:
    """
    Export calculation history
    
    Args:
        format: Export format ('json' or 'csv')
        calculator_id: Optional filter by calculator
    
    Returns:
        Exported data as string
    """
    history = get_calculation_history(calculator_id=calculator_id)
    
    if format == 'json':
        return json.dumps(history, indent=2, default=str)
    
    elif format == 'csv':
        import csv
        from io import StringIO
        
        if not history:
            return ""
        
        output = StringIO()
        writer = csv.writer(output)
        
        # Header
        writer.writerow([
            'ID', 'Calculator', 'Date', 'Time', 'Inputs', 'Results', 'Metadata'
        ])
        
        # Rows
        for calc in history:
            writer.writerow([
                calc['id'],
                calc['calculator_name'],
                calc['date'],
                calc['time'],
                json.dumps(calc['inputs'], default=str),
                json.dumps(calc['results'], default=str),
                json.dumps(calc.get('metadata', {}), default=str)
            ])
        
        return output.getvalue()
    
    return ""


def render_history_ui(calculator_id: Optional[str] = None, show_actions: bool = True):
    """
    Render calculation history UI
    
    Args:
        calculator_id: Optional filter by calculator
        show_actions: Show action buttons (delete, export, etc.)
    """
    init_history_state()
    
    history = get_calculation_history(calculator_id=calculator_id, limit=20)
    
    if not history:
        st.info("📝 Chưa có lịch sử tính toán. Thực hiện tính toán để lưu vào lịch sử.")
        return
    
    st.subheader(f"📊 Lịch Sử Tính Toán ({len(history)}/{st.session_state.history_max_size})")
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    with col1:
        search_query = st.text_input("🔍 Tìm kiếm", key=f"history_search_{calculator_id or 'all'}")
    with col2:
        if st.button("🗑️ Xóa tất cả", key=f"clear_history_{calculator_id or 'all'}"):
            cleared = clear_history(calculator_id)
            st.success(f"Đã xóa {cleared} tính toán")
            st.rerun()
    
    # Filter by search
    if search_query:
        history = search_history(search_query, calculator_id)
    
    # Display history
    for idx, calc in enumerate(history):
        with st.expander(
            f"📅 {calc['date']} {calc['time']} - {calc['calculator_name']}",
            expanded=False
        ):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Calculator:** {calc['calculator_name']}")
                st.markdown(f"**Thời gian:** {calc['date']} {calc['time']}")
                
                if calc.get('metadata'):
                    st.markdown("**Metadata:**")
                    st.json(calc['metadata'])
            
            with col2:
                if show_actions:
                    if st.button("📋 Xem chi tiết", key=f"view_{calc['id']}"):
                        st.session_state[f"view_calc_{calc['id']}"] = True
                    
                    if st.button("🗑️ Xóa", key=f"delete_{calc['id']}"):
                        if delete_calculation(calc['id']):
                            st.success("Đã xóa")
                            st.rerun()
            
            # Show details if requested
            if st.session_state.get(f"view_calc_{calc['id']}", False):
                st.markdown("---")
                st.markdown("**Inputs:**")
                st.json(calc['inputs'])
                st.markdown("**Results:**")
                st.json(calc['results'])
                
                if st.button("❌ Đóng", key=f"close_{calc['id']}"):
                    st.session_state[f"view_calc_{calc['id']}"] = False
                    st.rerun()
    
    # Export button
    if show_actions and history:
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📥 Xuất JSON", key=f"export_json_{calculator_id or 'all'}"):
                export_data = export_history('json', calculator_id)
                st.download_button(
                    "⬇️ Tải xuống",
                    export_data,
                    file_name=f"calculation_history_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json"
                )
        with col2:
            if st.button("📥 Xuất CSV", key=f"export_csv_{calculator_id or 'all'}"):
                export_data = export_history('csv', calculator_id)
                st.download_button(
                    "⬇️ Tải xuống",
                    export_data,
                    file_name=f"calculation_history_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )

