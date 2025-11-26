# 🎯 Kế Hoạch Cải Tiến Critical Care Dashboard

**Ngày:** 2025-02-XX  
**Mục tiêu:** Tối ưu dashboard để truy cập nhanh, hiện đại, tiện dụng

---

## 📊 Phân Tích Hiện Trạng

### Vấn Đề Hiện Tại:
1. ❌ **Cards không click được** - Chỉ hiển thị, không có tương tác
2. ❌ **Phải dùng sidebar** - Mất thời gian chọn từ dropdown
3. ❌ **Không có visual feedback** - Không biết card nào đang được hover
4. ❌ **Không có quick actions** - Phải nhiều bước để truy cập

### Cấu Trúc Hiện Tại:
- Dashboard hiển thị 4 quick access cards (Fluid, Vasopressors, Transfusion, Sedation)
- Scoring systems section với 3 columns
- Clinical scenarios section với 4 cards
- Tất cả đều chỉ là HTML/CSS, không có JavaScript interaction

---

## 🔍 Nghiên Cứu Best Practices

### 1. **Epic MyChart / Cerner PowerChart**
- ✅ **Clickable cards** với hover effects
- ✅ **Quick actions** buttons trên mỗi card
- ✅ **Visual hierarchy** rõ ràng
- ✅ **One-click navigation** đến tools

### 2. **Google Analytics Dashboard**
- ✅ **Interactive widgets** với click-to-drill-down
- ✅ **Color coding** cho different categories
- ✅ **Responsive grid layout**
- ✅ **Quick filters** và shortcuts

### 3. **Notion / Airtable**
- ✅ **Card-based navigation** với click handlers
- ✅ **Hover states** với visual feedback
- ✅ **Keyboard shortcuts** cho power users
- ✅ **Recent items** quick access

### 4. **Medical Apps (UpToDate, MDCalc)**
- ✅ **Category-based navigation**
- ✅ **Search-first approach**
- ✅ **Favorites/Recent** quick access
- ✅ **One-tap access** to calculators

---

## 🎨 Thiết Kế Giải Pháp

### Phase 1: Clickable Cards với Navigation ⭐ **PRIORITY**

#### 1.1. Quick Access Cards (4 cards)
- **Fluid Therapy** → Navigate to "💧 Fluid Therapy" tool
- **Vasopressors** → Navigate to "💉 Vasopressors" tool  
- **Transfusion** → Navigate to "🩸 Transfusion" tool
- **Sedation** → Navigate to "💤 Sedation & Analgesia" tool

**Implementation:**
```python
# Sử dụng st.button() với container để tạo clickable card
with st.container():
    if st.button("Fluid Therapy", key="card_fluid", use_container_width=True):
        st.session_state['critical_care_tool_selection'] = "💧 Fluid Therapy"
        st.rerun()
```

#### 1.2. Scoring Systems Cards
- **Đánh giá độ nặng** → Navigate to "📊 Scoring Systems" với filter
- **Đánh giá thần kinh** → Navigate với pre-selected GCS/RASS/CAM-ICU
- **Đánh giá thận** → Navigate với pre-selected AKI/RIFLE

#### 1.3. Clinical Scenarios Cards
- **Sepsis** → Navigate to "🦠 Sepsis Protocols"
- **ARDS** → Navigate to "🫁 ARDS Protocols"
- **Shock** → Navigate to "💉 Shock Management"
- **Delirium** → Navigate to "🧠 Delirium" (nếu có) hoặc CAM-ICU

### Phase 2: Enhanced UX Features

#### 2.1. Visual Feedback
- ✅ **Hover effects** với CSS transitions
- ✅ **Active state** cho card đang được chọn
- ✅ **Loading state** khi navigate
- ✅ **Tooltips** với mô tả ngắn

#### 2.2. Quick Actions
- ✅ **Keyboard shortcuts** (1-4 cho quick access cards)
- ✅ **Recent tools** section với quick links
- ✅ **Favorites** integration
- ✅ **Search bar** trong dashboard

#### 2.3. Responsive Design
- ✅ **Mobile-friendly** card layout
- ✅ **Touch-friendly** button sizes
- ✅ **Adaptive columns** (4 → 2 → 1 based on screen size)

### Phase 3: Advanced Features (Future)

#### 3.1. Smart Recommendations
- Hiển thị tools dựa trên:
  - Time of day (morning rounds → scoring, afternoon → protocols)
  - User history (most used tools)
  - Context (if viewing patient → relevant tools)

#### 3.2. Dashboard Customization
- User có thể:
  - Reorder cards
  - Hide/show sections
  - Customize quick access

#### 3.3. Integration với Patient Data
- Quick access với patient context
- Pre-fill data từ patient record
- Track usage per patient

---

## 🛠️ Implementation Plan

### Step 1: Tạo Clickable Card Component
**File:** `components/ui/clickable_card.py`

```python
def render_clickable_card(
    title: str,
    description: str,
    icon: str,
    gradient: str,
    action_key: str,
    action_value: str,
    tooltip: str = None
):
    """Render clickable card với navigation"""
    # Implementation với st.button và navigation
```

### Step 2: Cập Nhật Dashboard
**File:** `critical_care/dashboard.py`

- Thay thế HTML cards bằng clickable cards
- Map mỗi card đến tool selection
- Thêm visual feedback

### Step 3: Navigation Logic
- Sử dụng `st.session_state['critical_care_tool_selection']`
- Trigger `st.rerun()` sau khi set selection
- Page sẽ tự động route đến tool tương ứng

### Step 4: Testing
- ✅ Test tất cả cards navigate đúng
- ✅ Test responsive trên mobile
- ✅ Test keyboard navigation
- ✅ Test với different screen sizes

---

## 📋 Mapping Cards → Tools

| Card | Tool Selection | Page Route |
|------|---------------|------------|
| Fluid Therapy | `💧 Fluid Therapy` | `render_fluid_calculator()` |
| Vasopressors | `💉 Vasopressors` | `render_vasopressor_guide()` |
| Transfusion | `🩸 Transfusion` | `render_transfusion_calculator()` |
| Sedation | `💤 Sedation & Analgesia` | `render_sedation_calculator()` |
| Đánh giá độ nặng | `📊 Scoring Systems` | `render_scoring_calculator()` |
| Đánh giá thần kinh | `📊 Scoring Systems` + filter | `render_scoring_calculator()` |
| Đánh giá thận | `📊 Scoring Systems` + filter | `render_scoring_calculator()` |
| Sepsis | `🦠 Sepsis Protocols` | `render_sepsis_protocols()` |
| ARDS | `🫁 ARDS Protocols` | `render_ards_protocols()` |
| Shock | `💉 Shock Management` | `render_shock_management()` |
| Delirium | `📊 Scoring Systems` (CAM-ICU) | `render_scoring_calculator()` |

---

## 🎯 Success Metrics

1. **Time to Access Tool:** Giảm từ 3-4 clicks → 1 click
2. **User Satisfaction:** Dashboard là entry point chính
3. **Usage Patterns:** Track which cards được click nhiều nhất
4. **Mobile Usage:** Tối ưu cho mobile users

---

## 📚 References

- Streamlit Navigation: `st.switch_page()`, `st.session_state`
- Best Practices: Epic MyChart, Cerner, UpToDate, MDCalc
- UI/UX: Material Design, Apple HIG, Medical App Guidelines

---

**Status:** 🟡 Planning → 🟢 Ready to Implement

