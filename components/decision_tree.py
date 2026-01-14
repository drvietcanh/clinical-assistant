"""
Clinical Decision Tree Component
Visualize clinical decision trees and flowcharts for guidelines
"""

import streamlit as st
from typing import List, Dict, Optional

# Optional import for graphviz (not currently used, but may be needed in future)
try:
    import graphviz
    GRAPHVIZ_AVAILABLE = True
except ImportError:
    GRAPHVIZ_AVAILABLE = False
    graphviz = None


class DecisionNode:
    """Node in a decision tree"""
    def __init__(
        self,
        id: str,
        label: str,
        node_type: str = "decision",  # "decision", "action", "outcome"
        children: Optional[List] = None
    ):
        self.id = id
        self.label = label
        self.node_type = node_type
        self.children = children or []


def render_decision_tree_mermaid(nodes: List[Dict], title: str = "Clinical Decision Tree"):
    """
    Render decision tree using Mermaid diagram
    
    Args:
        nodes: List of node dictionaries with structure:
            {
                "id": str,
                "label": str,
                "type": "decision" | "action" | "outcome",
                "children": [{"id": str, "condition": str}]
            }
        title: Title of the decision tree
    """
    st.markdown(f"### {title}")
    
    # Build Mermaid diagram
    mermaid_code = "graph TD\n"
    
    # Add nodes
    for node in nodes:
        node_id = node["id"]
        label = node["label"].replace('"', "'")
        node_type = node.get("type", "decision")
        
        # Shape based on type
        if node_type == "decision":
            shape = f"{node_id}[\"{label}\"]"
        elif node_type == "action":
            shape = f"{node_id}((\"{label}\"))"
        else:  # outcome
            shape = f"{node_id}[\"{label}\"]"
        
        mermaid_code += f"    {shape}\n"
    
    # Add edges
    for node in nodes:
        node_id = node["id"]
        children = node.get("children", [])
        for child in children:
            child_id = child["id"]
            condition = child.get("condition", "")
            if condition:
                mermaid_code += f"    {node_id} -->|\"{condition}\"| {child_id}\n"
            else:
                mermaid_code += f"    {node_id} --> {child_id}\n"
    
    # Render Mermaid diagram
    st.markdown(f"```mermaid\n{mermaid_code}\n```")


def render_decision_tree_simple(
    steps: List[Dict],
    title: str = "Clinical Decision Tree"
):
    """
    Render simple decision tree as a step-by-step flowchart
    
    Args:
        steps: List of step dictionaries with structure:
            {
                "step": int,
                "question": str,
                "options": [
                    {"label": str, "next_step": int, "action": str}
                ]
            }
        title: Title of the decision tree
    """
    st.markdown(f"### {title}")
    
    for step_data in steps:
        step_num = step_data.get("step", 0)
        question = step_data.get("question", "")
        options = step_data.get("options", [])
        
        with st.container():
            st.markdown(f"**Bước {step_num}: {question}**")
            
            if options:
                for option in options:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"→ {option.get('label', '')}")
                    with col2:
                        if option.get('action'):
                            st.markdown(f"**{option['action']}**")
                    
                    if option.get('next_step'):
                        st.caption(f"→ Tiếp tục bước {option['next_step']}")
            
            st.markdown("---")


def create_heart_failure_tree():
    """Example: Heart failure decision tree"""
    return [
        {
            "id": "start",
            "label": "Bệnh nhân suy tim?",
            "type": "decision",
            "children": [
                {"id": "hfref", "condition": "LVEF ≤40%"},
                {"id": "hfmref", "condition": "LVEF 41-49%"},
                {"id": "hfpef", "condition": "LVEF ≥50%"}
            ]
        },
        {
            "id": "hfref",
            "label": "HFrEF - Điều trị ARNI/ACEi/ARB + Beta-blocker + MRA + SGLT2i",
            "type": "action",
            "children": []
        },
        {
            "id": "hfmref",
            "label": "HFmrEF - Điều trị tương tự HFrEF",
            "type": "action",
            "children": []
        },
        {
            "id": "hfpef",
            "label": "HFpEF - Điều trị triệu chứng + SGLT2i",
            "type": "action",
            "children": []
        }
    ]


def render_guideline_decision_tree(guideline_id: str):
    """
    Render decision tree for a specific guideline
    
    Args:
        guideline_id: ID of the guideline
    """
    # This would be loaded from a decision tree database
    # For now, use example trees based on guideline ID
    
    if "heart_failure" in guideline_id.lower():
        nodes = create_heart_failure_tree()
        render_decision_tree_mermaid(nodes, "Heart Failure Management Decision Tree")
    else:
        st.info("Decision tree chưa có sẵn cho guideline này.")


def render_interactive_decision_tree(steps: List[Dict]):
    """
    Render interactive decision tree where user can navigate
    
    Args:
        steps: List of step dictionaries
    """
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
    
    current_step = st.session_state.current_step
    
    if current_step < len(steps):
        step_data = steps[current_step]
        question = step_data.get("question", "")
        options = step_data.get("options", [])
        
        st.markdown(f"### {question}")
        
        for idx, option in enumerate(options):
            if st.button(
                option.get("label", ""),
                key=f"option_{current_step}_{idx}",
                use_container_width=True
            ):
                # Navigate to next step
                next_step = option.get("next_step", current_step + 1)
                st.session_state.current_step = next_step
                st.rerun()
        
        # Reset button
        if st.button("🔄 Bắt đầu lại", key="reset_tree"):
            st.session_state.current_step = 0
            st.rerun()
    else:
        st.success("✅ Hoàn thành quy trình quyết định!")
        if st.button("🔄 Bắt đầu lại"):
            st.session_state.current_step = 0
            st.rerun()
