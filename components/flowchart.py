"""
Interactive Flowchart Component
Visual flowcharts for diagnostic algorithms and clinical decision trees
"""

import streamlit as st
import streamlit.components.v1 as components
from typing import List, Dict, Any, Optional, Tuple
from enum import Enum


class NodeType(Enum):
    """Node types in flowchart"""
    START = "start"
    DECISION = "decision"
    ACTION = "action"
    END = "end"
    TEST = "test"


class FlowchartNode:
    """Represents a node in the flowchart"""
    
    def __init__(
        self,
        id: str,
        label: str,
        node_type: NodeType = NodeType.ACTION,
        options: Optional[Dict[str, str]] = None,
        color: Optional[str] = None,
        icon: Optional[str] = None
    ):
        self.id = id
        self.label = label
        self.node_type = node_type
        self.options = options or {}
        self.color = color
        self.icon = icon
    
    def get_color(self) -> str:
        """Get color for node based on type"""
        if self.color:
            return self.color
        
        color_map = {
            NodeType.START: "#28a745",  # Green
            NodeType.DECISION: "#ffc107",  # Yellow
            NodeType.ACTION: "#17a2b8",  # Blue
            NodeType.TEST: "#6f42c1",  # Purple
            NodeType.END: "#dc3545"  # Red
        }
        return color_map.get(self.node_type, "#6c757d")
    
    def get_shape(self) -> str:
        """Get HTML shape for node"""
        shape_map = {
            NodeType.START: "ellipse",
            NodeType.DECISION: "diamond",
            NodeType.ACTION: "rect",
            NodeType.TEST: "rect",
            NodeType.END: "ellipse"
        }
        return shape_map.get(self.node_type, "rect")


class FlowchartEdge:
    """Represents an edge (connection) in the flowchart"""
    
    def __init__(
        self,
        from_node: str,
        to_node: str,
        label: Optional[str] = None,
        color: Optional[str] = None
    ):
        self.from_node = from_node
        self.to_node = to_node
        self.label = label
        self.color = color or "#495057"


def render_flowchart_node_html(node: FlowchartNode, x: float, y: float, width: float = 150, height: float = 60) -> str:
    """Render a single node as HTML"""
    color = node.get_color()
    shape = node.get_shape()
    icon = f"{node.icon} " if node.icon else ""
    
    # Node styling based on shape
    if shape == "ellipse":
        border_radius = "50%"
    elif shape == "diamond":
        # Diamond shape using CSS transform
        return f"""
        <div id="node-{node.id}" 
             style="
                 position: absolute;
                 left: {x}px;
                 top: {y}px;
                 width: {width}px;
                 height: {height}px;
                 background: {color}15;
                 border: 3px solid {color};
                 transform: rotate(45deg);
                 display: flex;
                 align-items: center;
                 justify-content: center;
                 cursor: pointer;
                 transition: all 0.3s;
                 z-index: 10;
             "
             onmouseover="this.style.transform='rotate(45deg) scale(1.1)'; this.style.zIndex='100';"
             onmouseout="this.style.transform='rotate(45deg) scale(1)'; this.style.zIndex='10';"
             title="{node.label}">
            <div style="
                transform: rotate(-45deg);
                font-size: 0.85rem;
                font-weight: bold;
                color: {color};
                text-align: center;
                padding: 8px;
            ">
                {icon}{node.label}
            </div>
        </div>
        """
    else:
        border_radius = "8px"
    
    return f"""
    <div id="node-{node.id}" 
         style="
             position: absolute;
             left: {x}px;
             top: {y}px;
             width: {width}px;
             height: {height}px;
             background: {color}15;
             border: 3px solid {color};
             border-radius: {border_radius};
             display: flex;
             align-items: center;
             justify-content: center;
             cursor: pointer;
             transition: all 0.3s;
             z-index: 10;
             box-shadow: 0 2px 4px rgba(0,0,0,0.1);
         "
         onmouseover="this.style.transform='scale(1.1)'; this.style.zIndex='100'; this.style.boxShadow='0 4px 8px rgba(0,0,0,0.2)';"
         onmouseout="this.style.transform='scale(1)'; this.style.zIndex='10'; this.style.boxShadow='0 2px 4px rgba(0,0,0,0.1)';"
         title="{node.label}">
        <div style="
            font-size: 0.9rem;
            font-weight: bold;
            color: {color};
            text-align: center;
            padding: 8px;
        ">
            {icon}{node.label}
        </div>
    </div>
    """


def render_flowchart_edge_html(edge: FlowchartEdge, nodes: Dict[str, Tuple[float, float]], node_width: float = 150, node_height: float = 60) -> str:
    """Render an edge (arrow) as SVG"""
    from_pos = nodes.get(edge.from_node, (0, 0))
    to_pos = nodes.get(edge.to_node, (0, 0))
    
    # Calculate arrow path
    from_x = from_pos[0] + node_width / 2
    from_y = from_pos[1] + node_height
    to_x = to_pos[0] + node_width / 2
    to_y = to_pos[1]
    
    # Arrow path
    mid_x = (from_x + to_x) / 2
    mid_y = (from_y + to_y) / 2
    
    # Label position
    label_x = mid_x
    label_y = mid_y - 10
    
    # Arrow SVG
    arrow_svg = f"""
    <svg style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1;">
        <defs>
            <marker id="arrowhead-{edge.from_node}-{edge.to_node}" 
                    markerWidth="10" markerHeight="10" 
                    refX="9" refY="3" 
                    orient="auto">
                <polygon points="0 0, 10 3, 0 6" fill="{edge.color}" />
            </marker>
        </defs>
        <line x1="{from_x}" y1="{from_y}" 
              x2="{to_x}" y2="{to_y}" 
              stroke="{edge.color}" 
              stroke-width="2" 
              marker-end="url(#arrowhead-{edge.from_node}-{edge.to_node})" />
        {f'<text x="{label_x}" y="{label_y}" fill="{edge.color}" font-size="12px" font-weight="bold" text-anchor="middle">{edge.label}</text>' if edge.label else ''}
    </svg>
    """
    
    return arrow_svg


def render_flowchart(
    nodes: List[FlowchartNode],
    edges: List[FlowchartEdge],
    title: str = "Clinical Algorithm",
    width: int = 800,
    height: int = 600,
    interactive: bool = True
) -> None:
    """
    Render an interactive flowchart
    
    Args:
        nodes: List of FlowchartNode objects
        edges: List of FlowchartEdge objects
        title: Flowchart title
        width: Canvas width
        height: Canvas height
        interactive: Whether to enable interactive features
    """
    st.markdown(f"### {title}")
    
    # Calculate node positions (simple layout)
    node_positions = {}
    node_width = 150
    node_height = 60
    spacing_x = 200
    spacing_y = 120
    
    # Simple grid layout
    cols = 3
    for idx, node in enumerate(nodes):
        row = idx // cols
        col = idx % cols
        x = col * spacing_x + 50
        y = row * spacing_y + 50
        node_positions[node.id] = (x, y)
    
    # Build HTML
    nodes_html = "\n".join([
        render_flowchart_node_html(node, *node_positions[node.id], node_width, node_height)
        for node in nodes
    ])
    
    edges_html = "\n".join([
        render_flowchart_edge_html(edge, node_positions, node_width, node_height)
        for edge in edges
    ])
    
    flowchart_html = f"""
    <div style="
        position: relative;
        width: {width}px;
        height: {height}px;
        margin: 2rem auto;
        background: #f8f9fa;
        border: 2px solid #dee2e6;
        border-radius: 8px;
        overflow: auto;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    ">
        {edges_html}
        {nodes_html}
    </div>
    """
    
    # Use components.html thay vì markdown để tránh Streamlit escape các thẻ SVG
    components.html(flowchart_html, height=height + 100, scrolling=True)
    
    # Legend
    legend_html = """
    <div style="
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin: 1rem 0;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
    ">
    """
    
    for node_type in NodeType:
        color_map = {
            NodeType.START: ("#28a745", "🟢 Start"),
            NodeType.DECISION: ("#ffc107", "🟡 Decision"),
            NodeType.ACTION: ("#17a2b8", "🔵 Action"),
            NodeType.TEST: ("#6f42c1", "🟣 Test"),
            NodeType.END: ("#dc3545", "🔴 End")
        }
        color, label = color_map.get(node_type, ("#6c757d", "Node"))
        legend_html += f"""
        <div style="display: flex; align-items: center; gap: 0.5rem;">
            <div style="
                width: 24px;
                height: 24px;
                background: {color}15;
                border: 2px solid {color};
                border-radius: 4px;
            "></div>
            <span style="font-size: 0.9rem;">{label}</span>
        </div>
        """
    
    legend_html += "</div>"
    st.markdown(legend_html, unsafe_allow_html=True)


def create_chest_pain_algorithm() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """Create chest pain diagnostic algorithm"""
    nodes = [
        FlowchartNode("start", "Chest Pain Present?", NodeType.START, icon="🚨"),
        FlowchartNode("ecg", "ECG", NodeType.TEST, icon="📊"),
        FlowchartNode("stemi", "STEMI", NodeType.ACTION, color="#dc3545", icon="🔴"),
        FlowchartNode("troponin", "Troponin", NodeType.TEST, icon="🧪"),
        FlowchartNode("positive", "Positive", NodeType.ACTION, color="#ffc107", icon="⚠️"),
        FlowchartNode("negative", "Negative", NodeType.ACTION, color="#28a745", icon="✅"),
        FlowchartNode("cath", "Cath Lab", NodeType.END, color="#dc3545", icon="🏥"),
        FlowchartNode("monitor", "Monitor & Reassess", NodeType.END, color="#17a2b8", icon="👁️"),
        FlowchartNode("discharge", "Consider Discharge", NodeType.END, color="#28a745", icon="🏠"),
    ]
    
    edges = [
        FlowchartEdge("start", "ecg", "Yes"),
        FlowchartEdge("ecg", "stemi", "STEMI"),
        FlowchartEdge("ecg", "troponin", "Not STEMI"),
        FlowchartEdge("stemi", "cath", ""),
        FlowchartEdge("troponin", "positive", "Elevated"),
        FlowchartEdge("troponin", "negative", "Normal"),
        FlowchartEdge("positive", "monitor", ""),
        FlowchartEdge("negative", "discharge", ""),
    ]
    
    return nodes, edges


def create_aki_algorithm() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """Create AKI diagnostic algorithm"""
    nodes = [
        FlowchartNode("start", "AKI Suspected?", NodeType.START, icon="🫘"),
        FlowchartNode("stage", "Stage AKI", NodeType.ACTION, icon="📊"),
        FlowchartNode("fena", "FENa", NodeType.TEST, icon="🧪"),
        FlowchartNode("prerenal", "Prerenal", NodeType.ACTION, color="#17a2b8", icon="💧"),
        FlowchartNode("intrinsic", "Intrinsic Renal", NodeType.ACTION, color="#ffc107", icon="⚠️"),
        FlowchartNode("postrenal", "Postrenal", NodeType.ACTION, color="#dc3545", icon="🔴"),
        FlowchartNode("treat", "Treat Cause", NodeType.END, color="#28a745", icon="💊"),
    ]
    
    edges = [
        FlowchartEdge("start", "stage", ""),
        FlowchartEdge("stage", "fena", ""),
        FlowchartEdge("fena", "prerenal", "< 1%"),
        FlowchartEdge("fena", "intrinsic", "> 2%"),
        FlowchartEdge("fena", "postrenal", "Check obstruction"),
        FlowchartEdge("prerenal", "treat", "Volume, BP"),
        FlowchartEdge("intrinsic", "treat", "Nephrotoxins, ATN"),
        FlowchartEdge("postrenal", "treat", "Relieve obstruction"),
    ]
    
    return nodes, edges


def render_algorithm_selector() -> Optional[str]:
    """Render algorithm selector"""
    algorithms = {
        "Chest Pain": "chest_pain",
        "Acute Kidney Injury": "aki",
        "Dyspnea Workup": "dyspnea",
        "Sepsis Protocol": "sepsis",
        "Anemia Workup": "anemia"
    }
    
    selected = st.selectbox(
        "Chọn Algorithm:",
        list(algorithms.keys()),
        key="algorithm_selector"
    )
    
    return algorithms.get(selected)


def render_interactive_algorithm(algorithm_name: str) -> None:
    """Render interactive algorithm based on name"""
    if algorithm_name == "chest_pain":
        nodes, edges = create_chest_pain_algorithm()
        render_flowchart(nodes, edges, "Chest Pain Diagnostic Algorithm", width=800, height=600)
    elif algorithm_name == "aki":
        nodes, edges = create_aki_algorithm()
        render_flowchart(nodes, edges, "Acute Kidney Injury (AKI) Diagnostic Algorithm", width=800, height=500)
    else:
        st.info(f"Algorithm '{algorithm_name}' chưa được implement. Đang phát triển...")

