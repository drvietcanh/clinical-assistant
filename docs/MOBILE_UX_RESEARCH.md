# Mobile UX Research - Medical Apps
## Nghiên cứu giao diện mobile từ các ứng dụng y học nổi tiếng

### 📱 Các ứng dụng được nghiên cứu:
1. **UpToDate** - Professional, clean, clear hierarchy
2. **Medscape** - Quick access, sticky navigation
3. **Epocrates** - Compact, information-dense
4. **WebMD** - User-friendly, accessible
5. **Mayo Clinic** - Trustworthy, clear typography

---

## 🎨 Design Patterns đã áp dụng

### 1. **Bottom Navigation Bar** (Medscape/Epocrates)
- **Mục đích**: Quick access đến các module chính
- **Đặc điểm**:
  - Fixed ở bottom, không scroll
  - Icons + labels rõ ràng
  - Active state highlight
  - Safe area support (notch/home indicator)

### 2. **Sticky Search Bar** (UpToDate/Medscape)
- **Mục đích**: Search luôn accessible khi scroll
- **Đặc điểm**:
  - Sticky ở top khi scroll
  - Rounded input với icon
  - Quick filters/chips bên dưới

### 3. **Quick Action Chips** (Epocrates)
- **Mục đích**: Filter/quick actions nhanh
- **Đặc điểm**:
  - Horizontal scroll
  - Active state rõ ràng
  - Touch-friendly (min 36px height)

### 4. **Card Layouts** (UpToDate/Mayo Clinic)
- **Mục đích**: Hiển thị thông tin có cấu trúc
- **Đặc điểm**:
  - Clean borders, subtle shadows
  - Active state feedback (scale down khi tap)
  - Icon + title + meta info
  - Badges cho status

### 5. **Expandable Sections** (UpToDate)
- **Mục đích**: Tiết kiệm không gian, progressive disclosure
- **Đặc điểm**:
  - Smooth animation
  - Clear indicator (chevron)
  - Touch-friendly header (min 56px)

### 6. **Information Density** (Epocrates)
- **Mục đích**: Hiển thị nhiều thông tin trong không gian nhỏ
- **Đặc điểm**:
  - Label:Value layout
  - Clear typography hierarchy
  - Compact spacing

### 7. **Quick Actions Grid** (Medscape)
- **Mục đích**: Quick access đến các tính năng chính
- **Đặc điểm**:
  - 2-column grid
  - Large icons
  - Clear labels
  - Active feedback

### 8. **Table Card View** (Mobile-friendly)
- **Mục đích**: Tables dễ đọc trên mobile
- **Đặc điểm**:
  - Convert table rows thành cards
  - Label:Value pairs
  - Horizontal scroll fallback

### 9. **Floating Action Button** (Material Design)
- **Mục đích**: Primary action luôn accessible
- **Đặc điểm**:
  - Fixed position
  - Above bottom nav
  - Safe area support

### 10. **Status Indicators** (Epocrates)
- **Mục đích**: Visual status at a glance
- **Đặc điểm**:
  - Color-coded badges
  - Dot indicators
  - Clear labels

---

## 📐 Technical Specifications

### Touch Targets
- **Minimum**: 44x44px (iOS/Android guideline)
- **Recommended**: 48x48px cho primary actions
- **Spacing**: 8px minimum giữa các targets

### Typography
- **Base font**: 16px (prevent iOS zoom)
- **Headings**: 1.75rem (h1), 1.5rem (h2), 1.25rem (h3)
- **Body**: 0.95rem với line-height 1.6-1.7
- **Labels**: 0.9rem với font-weight 500-600

### Spacing
- **Card padding**: 16px
- **Section spacing**: 12-16px
- **Element spacing**: 8-12px

### Colors & Contrast
- **WCAG AA**: Minimum 4.5:1 cho text
- **WCAG AAA**: 7:1 cho important text
- **Status colors**: Consistent across app

### Performance
- **Animation duration**: 0.2s trên mobile
- **Touch delay**: Removed với `touch-action: manipulation`
- **Scrolling**: `-webkit-overflow-scrolling: touch`

---

## ♿ Accessibility Features

### 1. **High Contrast Mode**
- Support `prefers-contrast: high`
- Thicker borders, clearer distinctions

### 2. **Reduced Motion**
- Support `prefers-reduced-motion: reduce`
- Disable animations cho users nhạy cảm

### 3. **Safe Areas**
- Support `env(safe-area-inset-*)` cho devices có notch
- Padding tự động điều chỉnh

### 4. **Focus States**
- Clear outline cho keyboard navigation
- Visible focus indicators

---

## 🚀 Implementation Status

### ✅ Đã implement:
- [x] Base mobile optimizations CSS
- [x] Medical app patterns CSS
- [x] Touch targets optimization
- [x] Typography scaling
- [x] Table horizontal scroll
- [x] Sidebar mobile optimization
- [x] Safe area support
- [x] Accessibility features

### 🔄 Cần implement (Components):
- [ ] Bottom navigation bar component
- [ ] Quick action chips component
- [ ] Medical card component với patterns
- [ ] Expandable section component
- [ ] Table card view component
- [ ] Floating action button component
- [ ] Status indicator component
- [ ] Empty state component
- [ ] Skeleton loader component

---

## 📝 Usage Examples

### Medical Card Pattern
```html
<div class="medical-card">
    <div class="medical-card-header">
        <span class="medical-card-icon">💊</span>
        <div class="medical-card-title">Drug Name</div>
        <span class="medical-card-badge success">Active</span>
    </div>
    <div class="medical-card-meta">Category • Last updated</div>
</div>
```

### Quick Action Chips
```html
<div class="medical-quick-chips">
    <button class="medical-chip active">All</button>
    <button class="medical-chip">Emergency</button>
    <button class="medical-chip">Critical Care</button>
</div>
```

### Information Row
```html
<div class="medical-info-row">
    <span class="medical-info-label">Dosage:</span>
    <span class="medical-info-value">500mg</span>
</div>
```

---

## 🔗 References
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Material Design Guidelines](https://material.io/design)
- [WCAG 2.1 Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [UpToDate Mobile App](https://www.uptodate.com/)
- [Medscape Mobile App](https://www.medscape.com/)
- [Epocrates Mobile App](https://www.epocrates.com/)

