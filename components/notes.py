"""
Personal Notes & Annotations Component
Allows users to add, save, and manage notes for calculators and results
"""

import streamlit as st
from typing import Dict, List, Optional, Any
from datetime import datetime
import json


def get_notes_storage_key(calculator_id: str, result_id: Optional[str] = None) -> str:
    """
    Get storage key for notes
    
    Args:
        calculator_id: ID of the calculator (e.g., "egfr", "fena")
        result_id: Optional result ID for specific calculation
    
    Returns:
        Storage key string
    """
    if result_id:
        return f"notes_{calculator_id}_{result_id}"
    return f"notes_{calculator_id}_general"


def save_note(
    calculator_id: str,
    note_text: str,
    result_id: Optional[str] = None,
    tags: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> bool:
    """
    Save a note for a calculator or specific result
    
    Args:
        calculator_id: ID of the calculator
        note_text: Note content
        result_id: Optional result ID
        tags: Optional tags for categorization
        metadata: Optional metadata (e.g., inputs, results)
    
    Returns:
        True if saved successfully
    """
    if not note_text or not note_text.strip():
        return False
    
    storage_key = get_notes_storage_key(calculator_id, result_id)
    
    if 'user_notes' not in st.session_state:
        st.session_state.user_notes = {}
    
    if storage_key not in st.session_state.user_notes:
        st.session_state.user_notes[storage_key] = []
    
    note_entry = {
        "id": len(st.session_state.user_notes[storage_key]),
        "text": note_text.strip(),
        "timestamp": datetime.now().isoformat(),
        "tags": tags or [],
        "metadata": metadata or {}
    }
    
    st.session_state.user_notes[storage_key].append(note_entry)
    
    return True


def get_notes(
    calculator_id: str,
    result_id: Optional[str] = None,
    limit: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    Get notes for a calculator or specific result
    
    Args:
        calculator_id: ID of the calculator
        result_id: Optional result ID
        limit: Optional limit on number of notes
    
    Returns:
        List of note dictionaries
    """
    storage_key = get_notes_storage_key(calculator_id, result_id)
    
    if 'user_notes' not in st.session_state:
        st.session_state.user_notes = {}
    
    notes = st.session_state.user_notes.get(storage_key, [])
    
    # Sort by timestamp (newest first)
    notes.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
    
    if limit:
        return notes[:limit]
    
    return notes


def delete_note(
    calculator_id: str,
    note_id: int,
    result_id: Optional[str] = None
) -> bool:
    """
    Delete a note by ID
    
    Args:
        calculator_id: ID of the calculator
        note_id: Note ID to delete
        result_id: Optional result ID
    
    Returns:
        True if deleted successfully
    """
    storage_key = get_notes_storage_key(calculator_id, result_id)
    
    if 'user_notes' not in st.session_state:
        return False
    
    if storage_key not in st.session_state.user_notes:
        return False
    
    notes = st.session_state.user_notes[storage_key]
    
    # Find and remove note
    for idx, note in enumerate(notes):
        if note.get("id") == note_id:
            notes.pop(idx)
            return True
    
    return False


def search_notes(query: str, calculator_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Search notes by query
    
    Args:
        query: Search query
        calculator_id: Optional calculator ID to limit search
    
    Returns:
        List of matching notes with calculator context
    """
    if 'user_notes' not in st.session_state:
        return []
    
    query_lower = query.lower()
    results = []
    
    for storage_key, notes in st.session_state.user_notes.items():
        # Extract calculator_id from storage_key
        if storage_key.startswith("notes_"):
            key_parts = storage_key.replace("notes_", "").split("_")
            note_calculator_id = key_parts[0] if key_parts else None
            
            # Filter by calculator if specified
            if calculator_id and note_calculator_id != calculator_id:
                continue
            
            # Search in notes
            for note in notes:
                if query_lower in note.get("text", "").lower():
                    results.append({
                        "calculator_id": note_calculator_id,
                        "note": note
                    })
    
    # Sort by timestamp
    results.sort(key=lambda x: x["note"].get("timestamp", ""), reverse=True)
    
    return results


def export_notes(calculator_id: Optional[str] = None) -> str:
    """
    Export notes as JSON string
    
    Args:
        calculator_id: Optional calculator ID to limit export
    
    Returns:
        JSON string of notes
    """
    if 'user_notes' not in st.session_state:
        return "{}"
    
    export_data = {}
    
    for storage_key, notes in st.session_state.user_notes.items():
        if storage_key.startswith("notes_"):
            key_parts = storage_key.replace("notes_", "").split("_")
            note_calculator_id = key_parts[0] if key_parts else None
            
            if calculator_id and note_calculator_id != calculator_id:
                continue
            
            export_data[storage_key] = notes
    
    return json.dumps(export_data, indent=2, ensure_ascii=False)


def render_notes_section(
    calculator_id: str,
    result_id: Optional[str] = None,
    show_add_form: bool = True,
    show_search: bool = True,
    show_export: bool = True,
    max_display: int = 10
) -> None:
    """
    Render notes section for a calculator
    
    Args:
        calculator_id: ID of the calculator
        result_id: Optional result ID
        show_add_form: Whether to show add note form
        show_search: Whether to show search
        show_export: Whether to show export button
        max_display: Maximum notes to display
    """
    st.markdown("---")
    st.markdown("### 📝 Personal Notes")
    
    # Get existing notes
    notes = get_notes(calculator_id, result_id, limit=max_display)
    
    # Add note form
    if show_add_form:
        with st.expander("➕ Thêm Ghi Chú", expanded=len(notes) == 0):
            note_text = st.text_area(
                "Ghi chú:",
                key=f"note_input_{calculator_id}_{result_id or 'general'}",
                placeholder="Nhập ghi chú của bạn... (ví dụ: Bệnh nhân có CKD, điều chỉnh liều)",
                height=100
            )
            
            col1, col2 = st.columns([3, 1])
            with col1:
                tags_input = st.text_input(
                    "Tags (phân cách bằng dấu phẩy):",
                    key=f"note_tags_{calculator_id}_{result_id or 'general'}",
                    placeholder="Ví dụ: CKD, liều dùng, theo dõi"
                )
            
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("💾 Lưu Ghi Chú", key=f"save_note_{calculator_id}_{result_id or 'general'}", use_container_width=True):
                    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else []
                    
                    if save_note(calculator_id, note_text, result_id, tags):
                        st.success("✅ Đã lưu ghi chú!")
                        st.rerun()
                    else:
                        st.warning("Vui lòng nhập ghi chú")
    
    # Display notes
    if notes:
        st.markdown(f"**📋 Ghi chú ({len(notes)}):**")
        
        for note in notes:
            with st.container():
                # Note header
                timestamp = note.get("timestamp", "")
                if timestamp:
                    try:
                        dt = datetime.fromisoformat(timestamp)
                        time_str = dt.strftime("%Y-%m-%d %H:%M")
                    except:
                        time_str = timestamp
                else:
                    time_str = "Unknown"
                
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.markdown(f"**{time_str}**")
                    if note.get("tags"):
                        tags_html = " ".join([
                            f'<span style="background: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; margin-right: 4px;">{tag}</span>'
                            for tag in note.get("tags", [])
                        ])
                        st.markdown(tags_html, unsafe_allow_html=True)
                
                with col2:
                    if st.button("🗑️", key=f"delete_note_{calculator_id}_{note.get('id')}", help="Xóa ghi chú"):
                        if delete_note(calculator_id, note.get("id"), result_id):
                            st.success("Đã xóa ghi chú")
                            st.rerun()
                
                # Note content
                st.info(note.get("text", ""))
                st.markdown("---")
    else:
        st.info("Chưa có ghi chú nào. Thêm ghi chú đầu tiên ở trên!")
    
    # Search notes
    if show_search and len(notes) > 0:
        with st.expander("🔍 Tìm Kiếm Ghi Chú"):
            search_query = st.text_input("Tìm kiếm:", key=f"search_notes_{calculator_id}")
            if search_query:
                search_results = search_notes(search_query, calculator_id)
                if search_results:
                    st.markdown(f"**Tìm thấy {len(search_results)} ghi chú phù hợp:**")
                    for result in search_results:
                        st.markdown(f"**{result['calculator_id']}:** {result['note'].get('text', '')}")
                else:
                    st.info("Không tìm thấy ghi chú phù hợp")
    
    # Export notes
    if show_export and len(notes) > 0:
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            notes_json = export_notes(calculator_id)
            st.download_button(
                label="📥 Xuất Ghi Chú (JSON)",
                data=notes_json,
                file_name=f"notes_{calculator_id}_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col2:
            if st.button("🗑️ Xóa Tất Cả Ghi Chú", key=f"clear_notes_{calculator_id}", use_container_width=True):
                storage_key = get_notes_storage_key(calculator_id, result_id)
                if 'user_notes' in st.session_state and storage_key in st.session_state.user_notes:
                    st.session_state.user_notes[storage_key] = []
                    st.success("Đã xóa tất cả ghi chú")
                    st.rerun()


def render_notes_badge(calculator_id: str, result_id: Optional[str] = None) -> None:
    """
    Render a small badge showing note count
    
    Args:
        calculator_id: ID of the calculator
        result_id: Optional result ID
    """
    notes = get_notes(calculator_id, result_id)
    if notes:
        st.caption(f"📝 {len(notes)} note(s)")

