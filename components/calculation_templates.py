"""
Calculation Templates Manager
Save and load calculation templates (input presets)
"""

import streamlit as st
from typing import Dict, List, Any, Optional
from datetime import datetime
import json


def init_templates_state():
    """Initialize templates in session state"""
    if 'calculation_templates' not in st.session_state:
        st.session_state.calculation_templates = {}


def save_template(
    calculator_id: str,
    template_name: str,
    inputs: Dict[str, Any],
    description: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> str:
    """
    Save a calculation template
    
    Args:
        calculator_id: ID of the calculator
        template_name: Name of the template
        inputs: Input values to save
        description: Optional description
        tags: Optional tags for organization
    
    Returns:
        Template ID
    """
    init_templates_state()
    
    template_id = f"template_{calculator_id}_{len(st.session_state.calculation_templates.get(calculator_id, []))}_{datetime.now().timestamp()}"
    
    template = {
        'id': template_id,
        'calculator_id': calculator_id,
        'name': template_name,
        'inputs': inputs,
        'description': description or "",
        'tags': tags or [],
        'created_at': datetime.now().isoformat(),
        'created_date': datetime.now().strftime('%Y-%m-%d')
    }
    
    # Initialize calculator templates if needed
    if calculator_id not in st.session_state.calculation_templates:
        st.session_state.calculation_templates[calculator_id] = []
    
    # Add template
    st.session_state.calculation_templates[calculator_id].append(template)
    
    return template_id


def get_templates(
    calculator_id: str,
    tag_filter: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get templates for a calculator
    
    Args:
        calculator_id: Calculator ID
        tag_filter: Optional filter by tag
    
    Returns:
        List of templates
    """
    init_templates_state()
    
    templates = st.session_state.calculation_templates.get(calculator_id, [])
    
    if tag_filter:
        templates = [
            t for t in templates
            if tag_filter in t.get('tags', [])
        ]
    
    return templates


def get_template_by_id(calculator_id: str, template_id: str) -> Optional[Dict[str, Any]]:
    """Get a specific template by ID"""
    templates = get_templates(calculator_id)
    
    for template in templates:
        if template['id'] == template_id:
            return template
    
    return None


def delete_template(calculator_id: str, template_id: str) -> bool:
    """Delete a template"""
    init_templates_state()
    
    if calculator_id not in st.session_state.calculation_templates:
        return False
    
    initial_count = len(st.session_state.calculation_templates[calculator_id])
    st.session_state.calculation_templates[calculator_id] = [
        t for t in st.session_state.calculation_templates[calculator_id]
        if t['id'] != template_id
    ]
    
    return len(st.session_state.calculation_templates[calculator_id]) < initial_count


def load_template_inputs(calculator_id: str, template_id: str) -> Optional[Dict[str, Any]]:
    """
    Load template inputs
    
    Args:
        calculator_id: Calculator ID
        template_id: Template ID
    
    Returns:
        Input values dictionary or None
    """
    template = get_template_by_id(calculator_id, template_id)
    
    if template:
        return template['inputs']
    
    return None


def render_templates_ui(calculator_id: str, calculator_name: str):
    """
    Render templates management UI
    
    Args:
        calculator_id: Calculator ID
        calculator_name: Calculator name
    """
    init_templates_state()
    
    st.subheader(f"📋 Templates: {calculator_name}")
    
    # Save current inputs as template
    with st.expander("💾 Lưu Template Từ Inputs Hiện Tại", expanded=False):
        template_name = st.text_input("Tên template", key=f"template_name_{calculator_id}")
        template_desc = st.text_area("Mô tả (tùy chọn)", key=f"template_desc_{calculator_id}")
        template_tags = st.text_input("Tags (phân cách bằng dấu phẩy)", key=f"template_tags_{calculator_id}")
        
        # Get current inputs from session state
        current_inputs = {}
        for key in st.session_state.keys():
            if key.startswith(f"input_{calculator_id}_"):
                field_name = key.replace(f"input_{calculator_id}_", "")
                current_inputs[field_name] = st.session_state[key]
        
        if template_name and current_inputs:
            if st.button("💾 Lưu Template", key=f"save_template_{calculator_id}"):
                tags_list = [t.strip() for t in template_tags.split(",")] if template_tags else []
                template_id = save_template(
                    calculator_id,
                    template_name,
                    current_inputs,
                    template_desc,
                    tags_list
                )
                st.success(f"✅ Đã lưu template: {template_name}")
                st.rerun()
        elif not current_inputs:
            st.info("Nhập giá trị vào calculator trước khi lưu template")
    
    # List templates
    templates = get_templates(calculator_id)
    
    if not templates:
        st.info("Chưa có template nào. Lưu template từ inputs hiện tại để bắt đầu.")
        return
    
    st.markdown(f"### 📚 Templates ({len(templates)})")
    
    # Filter by tag
    all_tags = set()
    for template in templates:
        all_tags.update(template.get('tags', []))
    
    if all_tags:
        selected_tag = st.selectbox(
            "Lọc theo tag",
            options=["Tất cả"] + sorted(list(all_tags)),
            key=f"filter_tag_{calculator_id}"
        )
        
        if selected_tag != "Tất cả":
            templates = [t for t in templates if selected_tag in t.get('tags', [])]
    
    # Display templates
    for template in templates:
        with st.expander(
            f"📋 {template['name']} ({template['created_date']})",
            expanded=False
        ):
            if template.get('description'):
                st.markdown(f"**Mô tả:** {template['description']}")
            
            if template.get('tags'):
                tags_str = ", ".join([f"`{tag}`" for tag in template['tags']])
                st.markdown(f"**Tags:** {tags_str}")
            
            st.markdown("**Inputs:**")
            st.json(template['inputs'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("📥 Tải", key=f"load_template_{template['id']}"):
                    # Load template inputs into session state
                    for key, value in template['inputs'].items():
                        st.session_state[f"input_{calculator_id}_{key}"] = value
                    st.success(f"✅ Đã load template: {template['name']}")
                    st.rerun()
            
            with col2:
                if st.button("🗑️ Xóa", key=f"delete_template_{template['id']}"):
                    if delete_template(calculator_id, template['id']):
                        st.success("✅ Đã xóa template")
                        st.rerun()
    
    # Export/Import
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📥 Xuất Templates", key=f"export_templates_{calculator_id}"):
            export_data = json.dumps(templates, indent=2, default=str)
            st.download_button(
                "⬇️ Tải xuống JSON",
                export_data,
                file_name=f"templates_{calculator_id}_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
    
    with col2:
        uploaded_file = st.file_uploader(
            "📤 Import Templates",
            type=['json'],
            key=f"import_templates_{calculator_id}"
        )
        
        if uploaded_file:
            try:
                import_data = json.load(uploaded_file)
                if isinstance(import_data, list):
                    for template in import_data:
                        template['calculator_id'] = calculator_id
                        if calculator_id not in st.session_state.calculation_templates:
                            st.session_state.calculation_templates[calculator_id] = []
                        st.session_state.calculation_templates[calculator_id].append(template)
                    st.success(f"✅ Đã import {len(import_data)} templates")
                    st.rerun()
            except Exception as e:
                st.error(f"❌ Lỗi import: {str(e)}")

