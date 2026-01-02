"""
CDS Decision Trees Component
Clinical decision trees integrated into protocols
"""

import streamlit as st
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class DecisionNode:
    """Decision tree node"""
    id: str
    question: str
    options: List[Dict[str, str]]  # [{'label': 'Yes', 'next': 'node_id', 'action': '...'}]
    default_action: Optional[str] = None


class DecisionTree:
    """Decision tree structure"""
    
    def __init__(self, name: str, nodes: List[DecisionNode], start_node: str):
        self.name = name
        self.nodes = {node.id: node for node in nodes}
        self.start_node = start_node
    
    def get_node(self, node_id: str) -> Optional[DecisionNode]:
        """Get node by ID"""
        return self.nodes.get(node_id)
    
    def render(self, current_node_id: Optional[str] = None) -> Optional[str]:
        """
        Render decision tree interactively
        
        Args:
            current_node_id: Current node ID (from session state)
        
        Returns:
            Next node ID or None if complete
        """
        if current_node_id is None:
            current_node_id = self.start_node
        
        node = self.get_node(current_node_id)
        if not node:
            return None
        
        # Store current node in session state
        tree_key = f"decision_tree_{self.name}"
        if tree_key not in st.session_state:
            st.session_state[tree_key] = {'current_node': current_node_id, 'path': []}
        
        st.session_state[tree_key]['current_node'] = current_node_id
        st.session_state[tree_key]['path'].append(current_node_id)
        
        # Render question
        st.markdown(f"### {node.question}")
        
        # Render options
        selected_option = None
        for idx, option in enumerate(node.options):
            if st.button(
                option['label'],
                key=f"{tree_key}_option_{current_node_id}_{idx}",
                use_container_width=True
            ):
                selected_option = option
                break
        
        # Handle selection
        if selected_option:
            next_node_id = selected_option.get('next')
            action = selected_option.get('action')
            
            if action:
                st.info(f"**Hành động:** {action}")
            
            if next_node_id:
                st.session_state[tree_key]['current_node'] = next_node_id
                st.rerun()
            else:
                # End of tree
                st.success("✅ Hoàn thành quy trình quyết định")
                return None
        
        return current_node_id


# Predefined decision trees
SEPSIS_DECISION_TREE = DecisionTree(
    name="sepsis",
    nodes=[
        DecisionNode(
            id="start",
            question="Bệnh nhân có nghi ngờ nhiễm trùng không?",
            options=[
                {
                    'label': 'Có - Có dấu hiệu nhiễm trùng',
                    'next': 'check_lactate',
                    'action': 'Tiến hành đánh giá sepsis'
                },
                {
                    'label': 'Không - Không có dấu hiệu nhiễm trùng',
                    'next': None,
                    'action': 'Theo dõi, không cần sepsis bundle'
                }
            ]
        ),
        DecisionNode(
            id="check_lactate",
            question="Lactate >2 mmol/L hoặc tụt huyết áp?",
            options=[
                {
                    'label': 'Có - Lactate >2 hoặc tụt HA',
                    'next': 'sepsis_confirmed',
                    'action': 'SOFA ≥2 = Sepsis. Bắt đầu 1-hour bundle'
                },
                {
                    'label': 'Không - Lactate ≤2 và HA ổn',
                    'next': None,
                    'action': 'Theo dõi, chưa đủ tiêu chuẩn sepsis'
                }
            ]
        ),
        DecisionNode(
            id="sepsis_confirmed",
            question="Bắt đầu 1-hour bundle:",
            options=[
                {
                    'label': 'Đã hoàn thành',
                    'next': None,
                    'action': 'Tiếp tục theo dõi và điều chỉnh theo đáp ứng'
                }
            ],
            default_action="1. Đo Lactate\n2. Cấy máu\n3. Kháng sinh IV trong 1 giờ\n4. Bù dịch 30ml/kg nếu tụt HA\n5. Vasopressor nếu MAP <65"
        )
    ],
    start_node="start"
)

STROKE_DECISION_TREE = DecisionTree(
    name="stroke",
    nodes=[
        DecisionNode(
            id="start",
            question="Bệnh nhân có triệu chứng stroke (BE FAST)?",
            options=[
                {
                    'label': 'Có - Có triệu chứng stroke',
                    'next': 'check_time',
                    'action': 'Gọi code stroke, chuẩn bị CT não'
                },
                {
                    'label': 'Không - Không có triệu chứng rõ ràng',
                    'next': None,
                    'action': 'Đánh giá lại, có thể không phải stroke'
                }
            ]
        ),
        DecisionNode(
            id="check_time",
            question="Thời gian từ khi khởi phát đến hiện tại?",
            options=[
                {
                    'label': '< 3 giờ',
                    'next': 'tpa_eligible',
                    'action': 'Có thể xem xét tPA nếu đủ điều kiện'
                },
                {
                    'label': '3-4.5 giờ',
                    'next': 'tpa_eligible_extended',
                    'action': 'Có thể xem xét tPA extended window'
                },
                {
                    'label': '> 4.5 giờ',
                    'next': 'mechanical_thrombectomy',
                    'action': 'Xem xét mechanical thrombectomy nếu đủ điều kiện'
                }
            ]
        ),
        DecisionNode(
            id="tpa_eligible",
            question="Đủ điều kiện tPA?",
            options=[
                {
                    'label': 'Có - Đủ điều kiện',
                    'next': None,
                    'action': 'Truyền tPA 0.9mg/kg (max 90mg), 10% bolus, 90% trong 1h'
                },
                {
                    'label': 'Không - Có chống chỉ định',
                    'next': 'mechanical_thrombectomy',
                    'action': 'Xem xét mechanical thrombectomy'
                }
            ]
        ),
        DecisionNode(
            id="tpa_eligible_extended",
            question="Đủ điều kiện tPA extended window?",
            options=[
                {
                    'label': 'Có - Đủ điều kiện',
                    'next': None,
                    'action': 'Truyền tPA với extended window criteria'
                },
                {
                    'label': 'Không',
                    'next': 'mechanical_thrombectomy',
                    'action': 'Xem xét mechanical thrombectomy'
                }
            ]
        ),
        DecisionNode(
            id="mechanical_thrombectomy",
            question="Đủ điều kiện mechanical thrombectomy?",
            options=[
                {
                    'label': 'Có - LVO, <24h, NIHSS ≥6',
                    'next': None,
                    'action': 'Chuyển đến cath lab cho mechanical thrombectomy'
                },
                {
                    'label': 'Không',
                    'next': None,
                    'action': 'Điều trị hỗ trợ, dự phòng biến chứng'
                }
            ]
        )
    ],
    start_node="start"
)


def render_decision_tree(tree: DecisionTree, title: str = None) -> None:
    """
    Render decision tree in protocol
    
    Args:
        tree: DecisionTree object
        title: Optional title
    """
    if title:
        st.markdown(f"### {title}")
    
    tree_key = f"decision_tree_{tree.name}"
    current_node_id = st.session_state.get(tree_key, {}).get('current_node', tree.start_node)
    
    # Reset button
    if st.button("🔄 Bắt đầu lại", key=f"{tree_key}_reset"):
        if tree_key in st.session_state:
            del st.session_state[tree_key]
        st.rerun()
    
    st.markdown("---")
    
    # Render tree
    next_node = tree.render(current_node_id)
    
    # Show path
    path = st.session_state.get(tree_key, {}).get('path', [])
    if len(path) > 1:
        with st.expander("📋 Lịch sử quyết định", expanded=False):
            for node_id in path:
                node = tree.get_node(node_id)
                if node:
                    st.markdown(f"- {node.question}")


def get_decision_tree(tree_name: str) -> Optional[DecisionTree]:
    """
    Get predefined decision tree
    
    Args:
        tree_name: Tree name ("sepsis", "stroke", etc.)
    
    Returns:
        DecisionTree or None
    """
    trees = {
        "sepsis": SEPSIS_DECISION_TREE,
        "stroke": STROKE_DECISION_TREE,
    }
    return trees.get(tree_name.lower())


__all__ = [
    'DecisionNode',
    'DecisionTree',
    'render_decision_tree',
    'get_decision_tree',
    'SEPSIS_DECISION_TREE',
    'STROKE_DECISION_TREE',
]

