# Hướng Dẫn Sử Dụng Unified Components

## 📋 Tổng Quan

Các unified components giúp standardize UI/UX across toàn bộ app.

---

## 🎯 1. PAGINATION

**File:** `components/pagination.py`

### `render_pagination()`

Render pagination controls cho list views.

**Ví dụ:**
```python
from components.pagination import render_pagination

# List of items
items = list(range(100))

# Render với pagination
paginated_items, current_page, total_pages = render_pagination(
    items=items,
    items_per_page=10,
    page_key="drug_list_page",
    show_info=True,
    show_jump=True
)

# Display paginated items
for item in paginated_items:
    st.write(item)
```

### `render_simple_pagination()`

Simple pagination không có controls.

**Ví dụ:**
```python
from components.pagination import render_simple_pagination

paginated_items = render_simple_pagination(
    items=items,
    items_per_page=20,
    page_key="simple_page"
)
```

---

## 🎯 2. UNIFIED SIDEBAR

**File:** `components/unified_sidebar.py`

### `render_standard_page_sidebar()`

Standard sidebar cho tất cả pages.

**Ví dụ:**
```python
from components.unified_sidebar import render_standard_page_sidebar

render_standard_page_sidebar(
    title="Drug Database",
    icon="💊",
    description="Tra cứu thông tin thuốc",
    module_group="drug_database",
    quick_links=[
        {'label': 'Antibiotics', 'page': 'pages/02_💊_Antibiotics.py', 'icon': '💉'},
        {'label': 'Interactions', 'page': 'pages/07_💊_Drug_Database.py', 'icon': '⚠️'}
    ],
    filters={
        'category': {
            'type': 'selectbox',
            'label': 'Nhóm thuốc',
            'options': ['All', 'Cardiovascular', 'Antibiotics', 'Analgesics']
        }
    },
    info_text="Database bao gồm 666+ thuốc"
)
```

### `render_module_sidebar()`

Render sidebar từ module config.

**Ví dụ:**
```python
from components.unified_sidebar import render_module_sidebar

render_module_sidebar(
    module_id="drug_database",
    quick_links=[...],
    filters={...}
)
```

---

## 🎯 3. UNIFIED FILTERS

**File:** `components/unified_filters.py`

### `render_filter_panel()`

Standard filter panel.

**Ví dụ:**
```python
from components.unified_filters import render_filter_panel, apply_filters

# Define filters
filters_config = {
    'category': {
        'type': 'selectbox',
        'label': 'Danh mục',
        'options': ['All', 'A', 'B', 'C'],
        'default': 'All'
    },
    'price_range': {
        'type': 'slider',
        'label': 'Khoảng giá',
        'min': 0,
        'max': 1000,
        'default': (0, 1000)
    },
    'search': {
        'type': 'text_input',
        'label': 'Tìm kiếm',
        'placeholder': 'Nhập từ khóa...'
    }
}

# Render filters
filter_values = render_filter_panel(
    filters_config=filters_config,
    title="🔍 Lọc",
    collapsible=True
)

# Apply filters
def filter_func(item, filters):
    if filters.get('category') != 'All' and item.category != filters['category']:
        return False
    if item.price < filters['price_range'][0] or item.price > filters['price_range'][1]:
        return False
    if filters.get('search') and filters['search'].lower() not in item.name.lower():
        return False
    return True

filtered_items = apply_filters(items, filter_values, filter_func)
```

---

## 🎯 4. UNIFIED CARDS

**File:** `components/unified_cards.py`

### `render_info_card()`

Standard card component.

**Ví dụ:**
```python
from components.unified_cards import render_info_card

render_info_card(
    title="Drug Information",
    content="<p>Detailed drug information here...</p>",
    badges=[
        {'label': 'Generic', 'bg_color': '#e3f2fd', 'color': '#1976d2'},
        {'label': 'BHYT', 'bg_color': '#e8f5e9', 'color': '#388e3c'}
    ],
    actions=[
        {'label': 'View Details', 'icon': '👁️', 'action': lambda: st.switch_page(...)},
        {'label': 'Compare', 'icon': '📊', 'action': lambda: ...}
    ],
    style="default",  # or "gradient", "outlined"
    icon="💊"
)
```

### `render_card_grid()`

Render cards in grid layout.

**Ví dụ:**
```python
from components.unified_cards import render_card_grid

cards = [
    {
        'title': 'Card 1',
        'content': 'Content 1',
        'icon': '📊',
        'badges': [{'label': 'New', 'bg_color': '#ffebee', 'color': '#c62828'}]
    },
    {
        'title': 'Card 2',
        'content': 'Content 2',
        'icon': '💊'
    }
]

render_card_grid(cards, columns=3, card_style="default")
```

---

## 🎯 5. PAGE TEMPLATE

**File:** `utils/page_template.py`

### `render_page_template()`

Unified page template với slots.

**Ví dụ:**
```python
from utils.page_template import render_page_template

def sidebar_content():
    st.markdown("### Sidebar")
    st.selectbox("Filter", ["A", "B", "C"])

def main_content():
    st.markdown("## Main Content")
    st.write("Content here...")

render_page_template(
    title="Drug Database",
    icon="💊",
    description="Tra cứu thông tin thuốc",
    sidebar_content=sidebar_content,
    main_content=main_content,
    breadcrumbs=[
        ("Trang chủ", "/"),
        ("Drugs & Dosing", None),
        ("Drug Database", None)
    ],
    hero_section="""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; padding: 25px; border-radius: 15px;'>
        <h1>💊 Drug Database</h1>
    </div>
    """
)
```

### `render_simple_page()`

Simple page template.

**Ví dụ:**
```python
from utils.page_template import render_simple_page

def content():
    st.markdown("## Content")

def sidebar():
    st.markdown("### Sidebar")

render_simple_page(
    title="Simple Page",
    icon="📊",
    content=content,
    sidebar=sidebar
)
```

---

## 📝 Tích Hợp Vào Pages

### Example: Drug Database với Pagination & Filters

```python
import streamlit as st
from components.pagination import render_pagination
from components.unified_filters import render_filter_panel, apply_filters
from components.unified_sidebar import render_module_sidebar

# Setup
render_module_sidebar(
    module_id="drug_database",
    filters={
        'group': {
            'type': 'selectbox',
            'label': 'Nhóm thuốc',
            'options': ['All'] + list(DRUG_GROUPS.keys())
        }
    }
)

# Get all drugs
all_drugs = list(DRUG_DATABASE.items())

# Filters
filters_config = {
    'group': {
        'type': 'selectbox',
        'label': 'Nhóm thuốc',
        'options': ['All'] + list(DRUG_GROUPS.keys())
    }
}

filter_values = render_filter_panel(filters_config)

# Apply filters
def filter_func(item, filters):
    drug_name, drug_data = item
    if filters.get('group') and filters['group'] != 'All':
        return drug_data.get('group') == filters['group']
    return True

filtered_drugs = apply_filters(all_drugs, filter_values, filter_func)

# Pagination
paginated_drugs, page, total_pages = render_pagination(
    items=filtered_drugs,
    items_per_page=20,
    page_key="drug_list"
)

# Display
for drug_name, drug_data in paginated_drugs:
    st.markdown(f"### {drug_name}")
```

---

## ✅ Lợi Ích

1. **Consistency**: Tất cả pages có cùng UI/UX
2. **Maintainability**: Dễ maintain và update
3. **Code Reduction**: Giảm duplicate code
4. **User Experience**: Navigation và interaction nhất quán

---

*Tài liệu được tạo vào: 2025-01-30*

