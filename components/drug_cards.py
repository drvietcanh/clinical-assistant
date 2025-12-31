"""
Drug Card Component
Phase 3 UI Modernization - Card-based layout for drug database
"""

import streamlit as st
from typing import Dict, List, Optional


def render_drug_card(drug_name: str, drug_data: Dict, compact: bool = False) -> None:
    """
    Render a single drug as a modern card
    
    Args:
        drug_name: Name of the drug
        drug_data: Dictionary containing drug information
        compact: If True, render compact version for list view
    """
    
    # Extract key information
    group = drug_data.get('group', 'Unknown')
    vietnamese_name = drug_data.get('vietnamese_name', '')
    indications = drug_data.get('indications', [])
    administration = drug_data.get('administration', [])
    
    # Determine card color based on group
    group_colors = {
        'Cardiovascular': '#00897B',
        'Antibiotic': '#1976D2',
        'Respiratory': '#66BB6A',
        'Neurological': '#9C27B0',
        'Oncology': '#EF5350',
        'Emergency': '#FF7043',
    }
    
    # Find matching color
    card_color = '#546E7A'  # Default gray
    for key, color in group_colors.items():
        if key.lower() in group.lower():
            card_color = color
            break
    
    if compact:
        # Compact card for list view
        card_html = f"""
        <div style="
            background: linear-gradient(135deg, {card_color}10 0%, {card_color}05 100%);
            border-left: 4px solid {card_color};
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 0.75rem;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        " onmouseover="this.style.transform='translateX(4px)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.15)';" 
           onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 1px 3px rgba(0,0,0,0.1)';">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div style="flex: 1;">
                    <div style="font-size: 1.1rem; font-weight: 600; color: #263238; margin-bottom: 0.25rem;">
                        {drug_name}
                    </div>
                    <div style="font-size: 0.85rem; color: #546E7A; margin-bottom: 0.5rem;">
                        {vietnamese_name}
                    </div>
                    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                        <span style="
                            background: {card_color}20;
                            color: {card_color};
                            padding: 0.25rem 0.75rem;
                            border-radius: 12px;
                            font-size: 0.75rem;
                            font-weight: 600;
                        ">{group}</span>
                        {f'<span style="background: #E3F2FD; color: #1976D2; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.75rem;">{", ".join(administration[:2])}</span>' if administration else ''}
                    </div>
                </div>
                <div style="color: {card_color}; font-size: 1.5rem;">→</div>
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
    else:
        # Full card for grid view
        indications_text = ", ".join(indications[:3]) if indications else "N/A"
        if len(indications) > 3:
            indications_text += f" (+{len(indications)-3} more)"
        
        card_html = f"""
        <div style="
            background: white;
            border: 2px solid {card_color}40;
            border-radius: 12px;
            padding: 1.5rem;
            height: 100%;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        " onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 24px rgba(0,0,0,0.15)'; this.style.borderColor='{card_color}';" 
           onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)'; this.style.borderColor='{card_color}40';">
            <div style="
                background: linear-gradient(135deg, {card_color} 0%, {card_color}dd 100%);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 8px;
                margin-bottom: 1rem;
                font-size: 0.75rem;
                font-weight: 600;
                text-align: center;
            ">{group}</div>
            
            <div style="font-size: 1.25rem; font-weight: 700; color: #263238; margin-bottom: 0.5rem;">
                {drug_name}
            </div>
            
            <div style="font-size: 0.9rem; color: #546E7A; margin-bottom: 1rem;">
                {vietnamese_name}
            </div>
            
            <div style="margin-bottom: 0.75rem;">
                <div style="font-size: 0.75rem; color: #90A4AE; font-weight: 600; margin-bottom: 0.25rem;">
                    ADMINISTRATION
                </div>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    {' '.join([f'<span style="background: #E3F2FD; color: #1976D2; padding: 0.25rem 0.5rem; border-radius: 6px; font-size: 0.75rem;">{route}</span>' for route in administration[:4]])}
                </div>
            </div>
            
            <div>
                <div style="font-size: 0.75rem; color: #90A4AE; font-weight: 600; margin-bottom: 0.25rem;">
                    INDICATIONS
                </div>
                <div style="font-size: 0.85rem; color: #546E7A; line-height: 1.4;">
                    {indications_text}
                </div>
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)


def render_drug_list_cards(drugs_dict: Dict, layout: str = "list", max_items: Optional[int] = None) -> None:
    """
    Render multiple drugs as cards
    
    Args:
        drugs_dict: Dictionary of drugs {drug_name: drug_data}
        layout: "list" (vertical) or "grid" (2-3 columns)
        max_items: Maximum number of drugs to display (None = all)
    """
    
    if not drugs_dict:
        st.info("Không tìm thấy thuốc nào")
        return
    
    # Limit items if specified
    items = list(drugs_dict.items())
    if max_items:
        items = items[:max_items]
    
    if layout == "grid":
        # Grid layout (3 columns on desktop, 1 on mobile)
        cols_per_row = 3
        for i in range(0, len(items), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                if i + j < len(items):
                    drug_name, drug_data = items[i + j]
                    with col:
                        render_drug_card(drug_name, drug_data, compact=False)
                        # Add clickable button
                        if st.button(f"Xem chi tiết", key=f"drug_detail_{drug_name}_{i}_{j}", use_container_width=True):
                            st.session_state.selected_drug = drug_name
                            st.switch_page("pages/_Drug_Detail.py")
    
    elif layout == "list":
        # List layout (vertical, compact cards)
        for drug_name, drug_data in items:
            render_drug_card(drug_name, drug_data, compact=True)
            # Add clickable button (visually hidden but functional)
            if st.button(f"→ {drug_name}", key=f"drug_list_{drug_name}", use_container_width=True):
                st.session_state.selected_drug = drug_name
                st.switch_page("pages/_Drug_Detail.py")


def render_drug_filters() -> Dict:
    """
    Render filter controls for drug database
    Returns dict with filter criteria
    """
    st.markdown("### 🔍 Bộ lọc")
    
    col1, col2 = st.columns(2)
    
    with col1:
        search_query = st.text_input(
            "Tìm kiếm thuốc",
            placeholder="Nhập tên thuốc...",
            help="Tìm theo tên tiếng Anh hoặc tiếng Việt"
        )
    
    with col2:
        group_filter = st.selectbox(
            "Nhóm thuốc",
            options=["Tất cả", "Cardiovascular", "Antibiotic", "Respiratory", "Neurological", "Oncology", "Emergency"],
            help="Lọc theo nhóm thuốc"
        )
    
    col3, col4 = st.columns(2)
    
    with col3:
        route_filter = st.selectbox(
            "Đường dùng",
            options=["Tất cả", "PO", "IV", "IM", "SC", "Inhalation"],
            help="Lọc theo đường dùng thuốc"
        )
    
    with col4:
        layout = st.radio(
            "Hiển thị",
            options=["list", "grid"],
            format_func=lambda x: "📋 Danh sách" if x == "list" else "🎴 Lưới",
            horizontal=True
        )
    
    return {
        "search": search_query,
        "group": None if group_filter == "Tất cả" else group_filter,
        "route": None if route_filter == "Tất cả" else route_filter,
        "layout": layout
    }
