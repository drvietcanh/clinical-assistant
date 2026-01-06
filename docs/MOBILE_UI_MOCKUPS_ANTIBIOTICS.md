# 📱 Mobile UI Mockups & Implementation Details

**Ngày:** 2025-02-18  
**Mục đích:** Visual mockups và implementation details cho mobile UI

---

## 🎨 Mobile Layout Mockups

### 1. Home Screen (By Infection Tab)

```
┌─────────────────────────────────┐
│ 🔍 [Tìm kiếm phác đồ...]      │ ← Sticky Search
├─────────────────────────────────┤
│ [CAP] [UTI] [Sepsis] [MRSA]    │ ← Quick Filter Chips
├─────────────────────────────────┤
│ 💊 Kháng sinh (Chuyên sâu)     │ ← Compact Hero
│ Phác đồ • So sánh • Dữ liệu    │
├─────────────────────────────────┤
│ [🧙 Bắt đầu Trợ lý Chọn KS]    │ ← Prominent FAB/Wizard
├─────────────────────────────────┤
│ ▼ 🦠 Viêm phổi cộng đồng       │ ← Accordion
│   ┌─────────────────────────┐  │
│   │ 🟢 Tuyến đầu            │  │
│   │ CAP Non-severe          │  │
│   │ Ceftriaxone 2g IV q24h  │  │
│   │ [📖] [📊] [⭐]          │  │
│   └─────────────────────────┘  │
│   ┌─────────────────────────┐  │
│   │ 🟡 Thay thế             │  │
│   │ Alternative regimen     │  │
│   └─────────────────────────┘  │
├─────────────────────────────────┤
│ ▼ 🦠 Nhiễm trùng đường tiểu   │
│   ...                           │
├─────────────────────────────────┤
│                                 │
│         [🦠] [💊] [🔄] [🔍]    │ ← Bottom Nav
└─────────────────────────────────┘
```

### 2. Filters Bottom Sheet

```
┌─────────────────────────────────┐
│ ═══════════════════════════════ │ ← Drag Handle
│ 🔍 Bộ lọc                       │
├─────────────────────────────────┤
│ Vị trí nhiễm trùng:            │
│ ☑ Viêm phổi cộng đồng          │
│ ☑ Nhiễm trùng đường tiểu       │
│ ☐ Nhiễm trùng huyết            │
├─────────────────────────────────┤
│ Mức độ nặng:                    │
│ ☑ Nhẹ                          │
│ ☑ Trung bình                   │
│ ☑ Nặng                         │
├─────────────────────────────────┤
│ Môi trường điều trị:            │
│ ☑ Ngoại trú                     │
│ ☑ Nội trú                      │
├─────────────────────────────────┤
│ [Áp dụng] [Xóa bộ lọc]         │ ← Action Buttons
└─────────────────────────────────┘
```

### 3. Regimen Card (Mobile-Optimized)

```
┌─────────────────────────────────┐
│ 🟢 Tuyến đầu  [Mạnh]           │ ← Badges
├─────────────────────────────────┤
│ Chỉ định: CAP non-severe       │
├─────────────────────────────────┤
│ Thuốc:                          │
│ • Ceftriaxone 2g IV q24h × 7d  │
│   [📖 Chi tiết] [📊 TDM]      │ ← Action Buttons
│                                 │
│ • Azithromycin 500mg PO qd × 3d│
│   [📖 Chi tiết]                │
├─────────────────────────────────┤
│ Lý do: Covers typical + atypical│
├─────────────────────────────────┤
│ ▼ 🔬 Độ nhạy cảm (Việt Nam)   │ ← Expandable
│   E. coli: S (55-65%)          │
│   K. pneumoniae: S (50-60%)   │
├─────────────────────────────────┤
│ ▼ 💊 Tùy chọn Giảm liều       │ ← Expandable
│   Cefuroxime 500mg PO BID      │
├─────────────────────────────────┤
│ [🔍] [🫁] [💊] [📄]           │ ← Quick Actions
└─────────────────────────────────┘
```

### 4. Wizard Screen (Mobile)

```
┌─────────────────────────────────┐
│ ← Quay lại Phác đồ              │ ← Back Button
├─────────────────────────────────┤
│ 🧙 Trợ lý Chọn Kháng Sinh      │
├─────────────────────────────────┤
│ Vị trí nhiễm trùng:             │
│ [Viêm phổi cộng đồng ▼]        │ ← Large Select
├─────────────────────────────────┤
│ Mức độ nặng:                    │
│ [Nhẹ ▼]                        │
├─────────────────────────────────┤
│ Môi trường điều trị:            │
│ [Ngoại trú ▼]                  │
├─────────────────────────────────┤
│ Bệnh kèm theo:                  │
│ ☐ Bệnh thận mạn                │ ← Large Checkboxes
│ ☐ Suy giảm miễn dịch           │
│ ☐ Mang thai                    │
├─────────────────────────────────┤
│ Yếu tố nguy cơ:                 │
│ ☐ Nguy cơ MRSA                 │
│ ☐ Nguy cơ Pseudomonas          │
│ ☐ Dị ứng beta-lactam           │
├─────────────────────────────────┤
│ [🔍 Nhận Đề xuất]               │ ← Primary Button
└─────────────────────────────────┘
```

---

## 💻 Implementation Code Examples

### 1. Bottom Navigation Component

```python
# antibiotics/mobile_ui.py

def render_mobile_bottom_nav(current_tab="infection"):
    """Render bottom navigation bar for mobile"""
    
    nav_items = [
        {"icon": "🦠", "label": "Nhiễm trùng", "key": "infection", "page": None},
        {"icon": "💊", "label": "Thuốc", "key": "drugs", "page": None},
        {"icon": "🔄", "label": "Quản lý", "key": "stewardship", "page": None},
        {"icon": "🔍", "label": "Tìm kiếm", "key": "search", "page": None},
    ]
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        #mobile-bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            border-top: 1px solid #e0e0e0;
            box-shadow: 0 -2px 8px rgba(0,0,0,0.1);
            z-index: 9999;
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 8px 0 max(8px, env(safe-area-inset-bottom)) 0;
            height: 60px;
        }
        
        .mobile-nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex: 1;
            padding: 4px;
            text-decoration: none;
            color: #666;
            min-height: 48px;
            transition: all 0.2s;
            -webkit-tap-highlight-color: transparent;
        }
        
        .mobile-nav-item.active {
            color: #1976D2;
            font-weight: 600;
        }
        
        .mobile-nav-icon {
            font-size: 22px;
            margin-bottom: 2px;
        }
        
        .mobile-nav-label {
            font-size: 10px;
            font-weight: 500;
        }
        
        /* Add padding to prevent content overlap */
        .main .block-container {
            padding-bottom: 80px !important;
        }
    }
    
    @media (min-width: 769px) {
        #mobile-bottom-nav {
            display: none;
        }
    }
    </style>
    
    <div id="mobile-bottom-nav">
    """, unsafe_allow_html=True)
    
    for item in nav_items:
        active_class = "active" if item["key"] == current_tab else ""
        st.markdown(f"""
        <a href="#{item['key']}" class="mobile-nav-item {active_class}" onclick="setActiveTab('{item['key']}')">
            <div class="mobile-nav-icon">{item['icon']}</div>
            <div class="mobile-nav-label">{item['label']}</div>
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
```

### 2. Bottom Sheet Filters

```python
def render_mobile_filters_sheet(protocols_collection):
    """Render filters in bottom sheet for mobile"""
    
    # Trigger button
    col_filter1, col_filter2 = st.columns([3, 1])
    with col_filter1:
        search_query = st.text_input(
            "🔍 Tìm kiếm phác đồ",
            key="mobile_search",
            placeholder="Tìm theo nhiễm trùng, thuốc..."
        )
    with col_filter2:
        if st.button("🔍", key="mobile_filter_btn", use_container_width=True):
            st.session_state.show_mobile_filters = not st.session_state.get("show_mobile_filters", False)
    
    # Bottom sheet
    if st.session_state.get("show_mobile_filters", False):
        st.markdown("""
        <style>
        @media (max-width: 768px) {
            .mobile-filter-sheet {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background: white;
                border-radius: 20px 20px 0 0;
                box-shadow: 0 -4px 20px rgba(0,0,0,0.2);
                z-index: 10000;
                max-height: 80vh;
                overflow-y: auto;
                padding: 20px;
            }
            
            .mobile-filter-overlay {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0,0,0,0.5);
                z-index: 9999;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="mobile-filter-overlay"></div>', unsafe_allow_html=True)
        st.markdown('<div class="mobile-filter-sheet">', unsafe_allow_html=True)
        
        st.markdown("### 🔍 Bộ lọc")
        st.markdown("---")
        
        # Filters content
        filters = render_filters_sidebar(protocols_collection)
        
        col_apply1, col_apply2 = st.columns(2)
        with col_apply1:
            if st.button("Áp dụng", type="primary", use_container_width=True):
                st.session_state.show_mobile_filters = False
                st.rerun()
        with col_apply2:
            if st.button("Xóa bộ lọc", use_container_width=True):
                st.session_state.show_mobile_filters = False
                # Clear filters logic
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    return filters if st.session_state.get("show_mobile_filters", False) else None
```

### 3. Mobile-Optimized Cards

```python
def render_mobile_regimen_card(regimen, key_prefix: str = ""):
    """Mobile-optimized regimen card"""
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .mobile-regimen-card {
            background: white;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            width: 100%;
        }
        
        .mobile-regimen-card .badge {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 16px;
            font-size: 0.85em;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 8px;
        }
        
        .mobile-regimen-card .drug-item {
            padding: 12px;
            background: #f8f9fa;
            border-radius: 8px;
            margin-bottom: 8px;
        }
        
        .mobile-regimen-card .action-buttons {
            display: flex;
            gap: 8px;
            margin-top: 12px;
        }
        
        .mobile-regimen-card .action-buttons button {
            flex: 1;
            min-height: 44px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Card content với mobile-optimized layout
    ...
```

### 4. Floating Action Button

```python
def render_mobile_fab():
    """Render Floating Action Button for mobile"""
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .mobile-fab {
            position: fixed;
            bottom: 80px;
            right: 20px;
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1976D2 0%, #1565C0 100%);
            color: white;
            box-shadow: 0 4px 12px rgba(25,118,210,0.4);
            z-index: 9998;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: none;
        }
        
        .mobile-fab:active {
            transform: scale(0.9);
            box-shadow: 0 2px 8px rgba(25,118,210,0.3);
        }
        
        .mobile-fab:hover {
            transform: scale(1.05);
        }
    }
    
    @media (min-width: 769px) {
        .mobile-fab {
            display: none;
        }
    }
    </style>
    
    <button class="mobile-fab" onclick="openWizard()" title="Bắt đầu Trợ lý Chọn Kháng Sinh">
        🧙
    </button>
    
    <script>
    function openWizard() {
        // Trigger wizard open
        window.parent.postMessage({type: 'openWizard'}, '*');
    }
    </script>
    """, unsafe_allow_html=True)
```

---

## 📐 Responsive Breakpoints Strategy

### Mobile First Approach

```css
/* Base styles (Mobile) */
.protocol-card {
    width: 100%;
    padding: 16px;
    margin-bottom: 16px;
}

/* Tablet (768px+) */
@media (min-width: 768px) {
    .protocol-card {
        padding: 20px;
        margin-bottom: 20px;
    }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
    .protocol-card {
        max-width: 800px;
        margin: 0 auto 20px;
    }
}
```

---

## 🎯 Key Mobile UX Principles

### 1. Thumb Zone Optimization
- **Primary actions**: Bottom-center (easy thumb reach)
- **Secondary actions**: Top hoặc sides
- **FAB**: Bottom-right (thumb-friendly)

### 2. One-Handed Use
- **Content width**: Max 100% trên mobile
- **Action buttons**: Bottom hoặc easily reachable
- **Navigation**: Bottom nav (thumb-friendly)

### 3. Visual Hierarchy
- **Larger fonts**: Dễ đọc trên small screens
- **More spacing**: Giảm clutter
- **Clear CTAs**: Prominent action buttons

### 4. Performance
- **Lazy load**: Load content khi cần
- **Optimize images**: Compress và lazy load
- **Minimize JS**: Reduce JavaScript overhead

---

## 📋 Implementation Priority

### Phase 1 (Critical - Week 1)
1. ✅ Bottom navigation bar
2. ✅ Mobile-optimized hero section
3. ✅ Full-width cards
4. ✅ Bottom sheet filters
5. ✅ Mobile-optimized buttons

### Phase 2 (Important - Week 2)
6. ✅ Sticky search bar
7. ✅ Quick filter chips
8. ✅ FAB button
9. ✅ Improved spacing
10. ✅ Touch feedback

### Phase 3 (Enhancement - Week 3)
11. Swipe gestures
12. Pull-to-refresh
13. Card swipe actions
14. Quick actions menu

---

**Status:** 📋 Ready for Implementation
