# UI/UX Mobile Optimization - Tối ưu cho Bác sĩ

## Tổng quan

Đã hoàn thành tối ưu UI/UX cho app chuyên môn dành cho bác sĩ, tập trung vào:
- **Mobile-first design**: Tối ưu cho điện thoại, mượt và nhanh
- **Navigation đơn giản**: Bottom nav 5 tab chính
- **Trang chủ tối ưu**: Search lớn, gần đây, shortcuts, đề xuất theo chuyên khoa
- **Design system**: Màu sắc, typography, spacing nhất quán

---

## Các thay đổi chính

### 1. Bottom Navigation (Mobile)

**File**: `components/mobile_navigation.py`

- **5 tab chính**:
  1. 🏠 **Trang chủ** - Trang chủ với search và shortcuts
  2. 💊 **Thuốc** - Tra cứu thuốc và liều dùng
  3. 📊 **Thang điểm** - Tính score và công cụ
  4. 📋 **Guideline** - Phác đồ điều trị
  5. ⭐ **Tủ cá nhân** - Yêu thích, ghi chú, cài đặt

- **Tính năng**:
  - Chỉ hiển thị trên màn hình < 768px
  - Active state rõ ràng với màu primary (#2D7DF6)
  - Icon scale khi active
  - Safe area support cho iPhone (notch)
  - Padding bottom cho content để không bị che

### 2. Trang chủ mới (Homepage)

**File**: `components/homepage_doctor.py`

**Layout**:
- **Header**: Chào hỏi + avatar placeholder
- **Search Hero**: Ô tìm kiếm lớn với gradient, nhấn Ctrl+K để focus
- **Gần đây**: Horizontal scroll list các công cụ vừa dùng
- **Shortcuts 2x2**: 
  - 💊 Thuốc
  - 📊 Thang điểm  
  - 📋 Guideline
  - ⚗️ Tương tác thuốc
- **Đề xuất theo chuyên khoa**: List các score/guideline hay dùng

**Tính năng**:
- Responsive cards với hover/active states
- Click để navigate trực tiếp
- Hiển thị icon, tên, category
- Tự động đề xuất dựa trên chuyên khoa (ICU, Tim mạch, Hô hấp, Nhi, Nội)

### 3. Design System (CSS)

**File**: `static/styles.css`

**Màu sắc mới**:
- **Primary**: #2D7DF6 (xanh tin cậy)
- **Success**: #17A56B
- **Warning**: #F5A524
- **Error**: #E74C3C
- **Background**: #F7F9FC (light), #0F172A (dark)
- **Text**: #1B2430 (light), #E5E7EB (dark)

**Typography**:
- Font: System fonts (-apple-system, Roboto, Inter)
- Body: 14-16pt (mobile)
- Heading: 18-22pt
- Line-height: 1.4-1.5

**Spacing**:
- Grid: 4pt/8pt
- Padding: 16-20pt
- Touch targets: ≥48px

**Components**:
- Cards: Border radius 12-16px, shadow nhẹ
- Buttons: 48px min height, rounded corners
- Inputs: 16px font (tránh zoom iOS), 48px min height

### 4. Mobile Optimizations

**File**: `components/mobile_inputs.py` (đã có sẵn)

**Tối ưu**:
- Input font 16px để tránh zoom trên iOS
- Touch targets ≥48px
- Numeric keyboard cho số
- Email/tel keyboard cho tương ứng
- Focus states rõ ràng

---

## User Flow

### Flow 1: Tra cứu thuốc nhanh
1. Mở app → Trang chủ
2. Gõ tên thuốc vào search bar lớn
3. Chọn thuốc từ kết quả
4. Xem chi tiết: chỉ định, liều, chỉnh liều, ADR, tương tác
5. 1 tap để thêm vào Yêu thích

### Flow 2: Tính thang điểm
1. Tap tab "Thang điểm" (bottom nav)
2. Chọn score từ "Yêu thích" hoặc "Gần đây"
3. Điền các tiêu chí (checkbox/stepper)
4. Xem kết quả: score + phân tầng nguy cơ + gợi ý xử trí
5. Link sang Guideline liên quan

### Flow 3: Xem phác đồ
1. Tap tab "Guideline"
2. Lọc theo chuyên khoa
3. Chọn bệnh lý (Sepsis, STEMI, COPD...)
4. Xem tóm tắt step-by-step
5. Link trực tiếp sang thuốc/score liên quan

---

## Responsive Breakpoints

- **Mobile**: < 768px
  - Bottom nav hiển thị
  - Single column layout
  - Cards stack vertically
  - Touch-friendly targets (48px)

- **Tablet**: 768px - 1024px
  - Bottom nav ẩn
  - 2-3 columns
  - Sidebar có thể mở

- **Desktop**: > 1024px
  - Sidebar mặc định mở
  - Multi-column layout
  - Hover effects

---

## Performance Optimizations

1. **Lazy loading**: Components chỉ load khi cần
2. **CSS variables**: Dễ maintain và switch theme
3. **Minimal animations**: 200-250ms, ease-out
4. **Touch optimizations**: Tap highlight, active states
5. **Font loading**: System fonts (không cần download)

---

## Dark Mode Support

- Tự động detect system preference
- Toggle button trong header
- Màu sắc được điều chỉnh cho contrast tốt
- Tất cả components hỗ trợ dark mode

---

## Accessibility

- **Touch targets**: ≥48px (WCAG AA)
- **Contrast**: ≥4.5:1 cho text (WCAG AA)
- **Focus states**: Rõ ràng cho keyboard navigation
- **Screen reader**: Semantic HTML, ARIA labels
- **Font scaling**: Hỗ trợ 120-140% zoom

---

## Files Changed

1. `components/mobile_navigation.py` - Bottom nav với 5 tab mới
2. `components/homepage_doctor.py` - Trang chủ mới cho bác sĩ
3. `static/styles.css` - Design system mới
4. `app.py` - Tích hợp homepage component

---

## Next Steps (Tùy chọn)

1. **Thêm chuyên khoa selector**: Cho phép bác sĩ chọn chuyên khoa để personalize đề xuất
2. **Offline support**: Cache nội dung chuyên môn để dùng offline
3. **Push notifications**: Nhắc nhở guideline mới, cập nhật thuốc
4. **Analytics**: Track usage để cải thiện UX
5. **A/B testing**: Test các layout khác nhau

---

## Testing Checklist

- [x] Bottom nav hiển thị đúng trên mobile
- [x] Trang chủ load nhanh và mượt
- [x] Search hoạt động tốt
- [x] Cards click được và navigate đúng
- [x] Dark mode hoạt động
- [x] Touch targets đủ lớn (≥48px)
- [x] Font không zoom trên iOS khi focus input
- [x] Responsive trên các kích thước màn hình

---

**Ngày hoàn thành**: 2025-02-18
**Version**: 2.4.0

