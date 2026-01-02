"""
Interactive Flowchart Engine
Renders a step-by-step wizard based on node-link data structure.
"""

import streamlit as st
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
from enum import Enum


class NodeType(Enum):
    """Node types for flowcharts"""
    START = "start"
    DECISION = "decision"
    ACTION = "action"
    TEST = "test"
    RESULT = "result"
    END = "end"


@dataclass
class FlowchartNode:
    """Flowchart node definition"""
    id: str
    label: str
    node_type: NodeType
    icon: str = ""
    color: str = ""
    
    def __post_init__(self):
        if isinstance(self.node_type, str):
            self.node_type = NodeType(self.node_type)


@dataclass
class FlowchartEdge:
    """Flowchart edge definition"""
    from_node: str
    to_node: str
    label: str = ""

def render_flowchart(
    data: Dict[str, Any] = None,
    flow_id: str = None,
    # Alternative signature for node-edge style
    nodes: List[FlowchartNode] = None,
    edges: List[FlowchartEdge] = None,
    title: str = None,
    width: int = 800,
    height: int = 600,
    interactive: bool = True
):
    """
    Render interactive flowchart
    
    Args:
        data: Flowchart definition (nodes, start_node_id) - legacy format
        flow_id: Unique ID for this flowchart instance (for session state)
        nodes: List of FlowchartNode objects - new format
        edges: List of FlowchartEdge objects - new format
        title: Chart title
        width: Chart width
        height: Chart height
        interactive: Whether to show interactive controls
    """
    # Handle new format (nodes/edges)
    if nodes is not None and edges is not None:
        # Convert to legacy format
        nodes_dict = {}
        start_node_id = None
        
        for node in nodes:
            nodes_dict[node.id] = {
                "title": node.label,
                "type": node.node_type.value,
                "icon": node.icon,
                "color": node.color
            }
            if node.node_type == NodeType.START:
                start_node_id = node.id
        
        # Build options from edges
        for edge in edges:
            from_node = nodes_dict.get(edge.from_node, {})
            if "options" not in from_node:
                from_node["options"] = []
            from_node["options"].append({
                "label": edge.label or "Tiếp tục",
                "next": edge.to_node
            })
        
        data = {
            "nodes": nodes_dict,
            "start_node_id": start_node_id or (nodes[0].id if nodes else None)
        }
        flow_id = flow_id or title or "flowchart"
    
    if not data:
        st.error("No flowchart data provided")
        return
    
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
