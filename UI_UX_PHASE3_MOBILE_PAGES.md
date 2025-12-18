# UI/UX Phase 3 - Mobile Page Optimizations

## Tổng quan

Tối ưu các trang con (Drug Database, Scores, Protocols) cho mobile với:
- **Mobile page wrapper**: Header, breadcrumbs, mobile-friendly sidebar
- **Consistent design**: Nhất quán với homepage design
- **Better navigation**: Back button, breadcrumbs
- **Optimized layouts**: Cards, tabs, empty states

---

## Components mới

### 1. Mobile Page Wrapper

**File**: `components/mobile_page_wrapper.py`

**Tính năng**:
- `render_mobile_page_header()`: Header sticky trên mobile với back button
- `render_breadcrumbs()`: Breadcrumb navigation
- `render_mobile_optimized_sidebar()`: Sidebar tối ưu cho mobile
- `render_mobile_friendly_tabs()`: Tabs responsive
- `render_mobile_card()`: Card component tối ưu mobile
- `render_empty_state()`: Empty state đẹp

**Sử dụng**:
```python
from components.mobile_page_wrapper import render_mobile_page_header, render_breadcrumbs

# In page file
render_mobile_page_header(
    title="Cơ sở dữ liệu thuốc",
    icon="💊",
    subtitle="Tra cứu thuốc và liều dùng",
    show_back_button=True,
    back_url="/"
)

render_breadcrumbs([
    ("Trang chủ", "/"),
    ("Thuốc", None)  # Current page
])
```

### 2. Page Helper Cải tiến

**File**: `utils/page_helper.py`

**Cải tiến**:
- Thêm parameter `mobile_header` (default: True)
- Tự động render mobile header nếu component available
- Ẩn standard title trên mobile khi có mobile header
- Backward compatible với code cũ

**Sử dụng**:
```python
from utils.page_helper import setup_page

setup_page(
    page_title="Scores",
    page_icon="📊",
    description="Clinical scoring systems",
    mobile_header=True  # Enable mobile header
)
```

---

## Mobile Optimizations

### 1. Sticky Header
- Header cố định ở top khi scroll
- Back button để quay về trang chủ
- Icon + title + subtitle
- Chỉ hiển thị trên mobile (< 768px)

### 2. Breadcrumbs
- Navigation path rõ ràng
- Click để quay lại trang trước
- Responsive font size
- Color coding (primary cho links, dark cho current)

### 3. Sidebar Optimization
- Full width trên mobile
- Toggle button floating (bottom right, above bottom nav)
- Collapsible để tiết kiệm không gian
- Touch-friendly controls

### 4. Mobile Cards
- Left border accent color
- Padding tối ưu cho mobile
- Hover/active states
- Clickable với cursor pointer

### 5. Empty States
- Large icon (4rem)
- Clear title và message
- Optional action button
- Centered layout

---

## Responsive Breakpoints

### Mobile (< 768px)
- Sticky mobile header hiển thị
- Standard title ẩn
- Sidebar full width, collapsible
- Cards stack vertically
- Tabs wrap, 2 columns

### Tablet (768px - 1024px)
- Standard title hiển thị
- Mobile header ẩn
- Sidebar normal width
- 2-3 column layouts

### Desktop (> 1024px)
- Standard title
- Sidebar expanded
- Multi-column layouts
- Hover effects

---

## Integration với Pages Hiện Tại

### Drug Database Page
- Mobile header với back button
- Breadcrumbs: Trang chủ > Thuốc
- Sidebar với function selector
- Mobile-friendly tabs cho các tools

### Scores Page
- Mobile header
- Breadcrumbs: Trang chủ > Thang điểm
- Specialty selector trong sidebar
- Score cards tối ưu mobile

### Protocols Page
- Mobile header
- Breadcrumbs: Trang chủ > Guideline
- Protocol selector trong sidebar
- Protocol cards với mobile layout

---

## CSS Additions

### Mobile Header
```css
.mobile-page-header {
    background: var(--card-bg);
    border-bottom: 1px solid var(--border);
    padding: 1rem;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 4px var(--shadow);
}
```

### Mobile Cards
```css
.mobile-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-left: 4px solid var(--primary);
    border-radius: 12px;
    padding: 1rem;
    transition: all 0.2s ease;
}
```

---

## Testing Checklist

- [x] Mobile header hiển thị đúng trên mobile
- [x] Back button navigate về trang chủ
- [x] Breadcrumbs hoạt động
- [x] Sidebar toggle hoạt động
- [x] Cards responsive
- [x] Empty states hiển thị đẹp
- [x] Tabs wrap đúng trên mobile
- [x] Không conflict với bottom nav

---

## Files Changed/Created

1. **components/mobile_page_wrapper.py** - NEW: Mobile page wrapper components
2. **utils/page_helper.py** - UPDATED: Thêm mobile header support

---

## Next Steps (Tùy chọn)

1. **Apply to all pages**: Tích hợp vào tất cả pages
2. **Loading states**: Skeleton screens cho loading
3. **Pull to refresh**: Swipe down để refresh
4. **Page transitions**: Smooth transitions giữa các pages
5. **Deep linking**: Support URL parameters cho deep links

---

**Ngày hoàn thành**: 2025-02-18
**Version**: 2.4.2

