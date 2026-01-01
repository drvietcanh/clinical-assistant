"""
Interactive Flowchart Engine
Renders a step-by-step wizard based on node-link data structure.
"""

import streamlit as st
from typing import Dict, Any, Optional

def render_flowchart(
    data: Dict[str, Any],
    flow_id: str
):
    """
    Render interactive flowchart
    
    Args:
        data: Flowchart definition (nodes, start_node_id)
        flow_id: Unique ID for this flowchart instance (for session state)
    """
    
    # Initialize session state for this flow
    state_key = f"flow_state_{flow_id}"
    history_key = f"flow_history_{flow_id}"
    
    if state_key not in st.session_state:
        st.session_state[state_key] = data.get("start_node_id")
        st.session_state[history_key] = []
        
    current_node_id = st.session_state[state_key]
    
    # Handle completion or invalid state
    if not current_node_id or current_node_id not in data["nodes"]:
        st.error(f"Lỗi: Không tìm thấy bước '{current_node_id}'")
        if st.button("Quay lại từ đầu"):
             st.session_state[state_key] = data.get("start_node_id")
             st.session_state[history_key] = []
             st.rerun()
        return

    node = data["nodes"][current_node_id]
    
    # Progress Bar (optional, simplistic)
    # Could be improved by calculating depth
    
    # Render Node UI
    with st.container():
        # Header / Title
        if "title" in node:
            st.subheader(node["title"])
            
        # Content / Description
        if "content" in node:
            st.info(node["content"]) if node.get("type") == "action" else st.markdown(node["content"])
            
        # Warning/Critical info
        if "warning" in node:
            st.error(f"⚠️ {node['warning']}")

        st.markdown("---")
        
        # Interaction Area
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if node.get("type") == "question":
                st.markdown("**Lựa chọn của bạn:**")
                options = node.get("options", [])
                
                # Render options as buttons (better for touch)
                for idx, opt in enumerate(options):
                    if st.button(
                        f"👉 {opt['label']}", 
                        key=f"btn_{flow_id}_{current_node_id}_{idx}",
                        use_container_width=True,
                        type="primary" if idx == 0 else "secondary" # Highlight first option usually Yes
                    ):
                        # Add to history
                        st.session_state[history_key].append(current_node_id)
                        # Move to next
                        st.session_state[state_key] = opt["next"]
                        st.rerun()
                        
            elif node.get("type") in ["action", "result"]:
                next_node = node.get("next")
                if next_node:
                    if st.button("Tiếp tục ➡️", key=f"next_{flow_id}", type="primary"):
                        st.session_state[history_key].append(current_node_id)
                        st.session_state[state_key] = next_node
                        st.rerun()
                else:
                    st.success("✅ Đã hoàn thành quy trình.")
                    if st.button("🔄 Làm lại từ đầu"):
                        st.session_state[state_key] = data.get("start_node_id")
                        st.session_state[history_key] = []
                        st.rerun()

        # Navigation Controls (Back / Reset)
        with col2:
            st.markdown("<br>", unsafe_allow_html=True) # Spacer
            if st.session_state[history_key]:
                if st.button("⬅️ Quay lại", key=f"back_{flow_id}"):
                    prev_node = st.session_state[history_key].pop()
                    st.session_state[state_key] = prev_node
                    st.rerun()
            
            if st.button("Reset", key=f"reset_{flow_id}"):
                st.session_state[state_key] = data.get("start_node_id")
                st.session_state[history_key] = []
                st.rerun()
