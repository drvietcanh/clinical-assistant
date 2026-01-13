"""
Main Menu Category Browser Component
Visual category cards with icons, colors, descriptions, and stats
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS


def get_category_metadata():
    """Get category metadata with icons, colors, and descriptions"""
    categories_meta = {
        "drugs_dosing": {
            "icon": "💊",
            "title": "Thuốc & Liều dùng",
            "description": "Database thuốc, liều dùng, tương tác",
            "color": "#9C27B0",
            "page": "pages/07_💊_Drug_Database.py"
        },
        "calculators_scores": {
            "icon": "📊",
            "title": "Tính toán & Thang điểm",
            "description": "Scores, calculators lâm sàng",
            "color": "#2196F3",
            "page": "pages/01_📊_Scores.py"
        },
        "critical_care_protocols": {
            "icon": "🫁",
            "title": "Hồi sức & Phác đồ",
            "description": "Protocols ICU, bundles, hồi sức",
            "color": "#E91E63",
            "page": "pages/09_🫁_Critical_Care.py"
        },
        "diagnosis_reference": {
            "icon": "🩺",
            "title": "Chẩn đoán & Tham khảo",
            "description": "Chẩn đoán phân biệt, ICD-10",
            "color": "#4CAF50",
            "page": "pages/06_🩺_Diagnosis.py"
        },
        "support_tools": {
            "icon": "🧭",
            "title": "Hỗ trợ & Công cụ",
            "description": "Decision support, guidelines",
            "color": "#607D8B",
            "page": "pages/10_🧭_Decision_Support.py"
        },
        "labs_calculators": {
            "icon": "🔬",
            "title": "Xét nghiệm & Labs",
            "description": "Lab panels, calculators",
            "color": "#00BCD4",
            "page": "pages/05_🔬_Labs_and_Calculators.py"
        },
    }
    return categories_meta


def count_calculators_by_category():
    """Count calculators in each category"""
    category_counts = {}
    for calc_id, calc_info in ALL_CALCULATORS.items():
        category = calc_info.get('category', 'Khác')
        category_counts[category] = category_counts.get(category, 0) + 1
    return category_counts


def render_category_browser():
    """Render visual category browser with cards"""
    categories_meta = get_category_metadata()
    category_counts = count_calculators_by_category()
    
    st.markdown("### 📚 Duyệt theo nhóm chính")
    st.caption("Chọn nhóm để xem tất cả calculators và công cụ")
    
    # Responsive grid: 3 columns desktop, 2 tablet, 1 mobile
    num_cols = 3
    cols = st.columns(num_cols)
    
    for idx, (cat_id, cat_info) in enumerate(categories_meta.items()):
        with cols[idx % num_cols]:
            # Count calculators in this category (approximate)
            count = category_counts.get(cat_info['title'].split('&')[0].strip(), 0)
            if count == 0:
                # Fallback: estimate based on category
                if "Thuốc" in cat_info['title']:
                    count = "700+"
                elif "Tính toán" in cat_info['title']:
                    count = "50+"
                else:
                    count = "10+"
            
            # Create category card
            gradient_color = cat_info['color']
            
            st.markdown(
                f"""
                <div class="category-card" 
                     style="background: linear-gradient(135deg, {gradient_color}15 0%, {gradient_color}05 100%);
                            border: 2px solid {gradient_color}40;
                            padding: 24px;
                            border-radius: 12px;
                            text-align: center;
                            cursor: pointer;
                            transition: all 0.3s;
                            margin-bottom: 1rem;
                            min-height: 180px;
                            display: flex;
                            flex-direction: column;
                            justify-content: center;">
                    <div class="category-card-icon" style="font-size: 4rem; margin-bottom: 12px;">
                        {cat_info['icon']}
                    </div>
                    <div class="category-card-title" style="font-size: 1.2rem; font-weight: 600; margin-bottom: 8px; color: var(--text-primary);">
                        {cat_info['title']}
                    </div>
                    <div class="category-card-desc" style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 12px;">
                        {cat_info['description']}
                    </div>
                    <div class="category-card-stats" style="font-size: 0.85rem; color: {gradient_color}; font-weight: 600;">
                        {count} calculators
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            if st.button(
                f"Mở {cat_info['title']}",
                key=f"cat_browse_{cat_id}",
                use_container_width=True,
                type="primary"
            ):
                st.switch_page(cat_info['page'])


def render_category_browser_compact():
    """Render compact category browser for sidebar"""
    categories_meta = get_category_metadata()
    
    st.markdown("### 📚 Nhóm chính")
    
    for cat_id, cat_info in list(categories_meta.items())[:6]:
        if st.button(
            f"{cat_info['icon']} {cat_info['title']}",
            key=f"cat_compact_{cat_id}",
            use_container_width=True
        ):
            st.switch_page(cat_info['page'])
