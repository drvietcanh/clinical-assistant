# 🌙 Dark Mode cho Trang Protocol

## Tổng Quan

Đã triển khai tính năng Dark Mode (Giao diện tối) cho trang Protocol, giúp giảm mỏi mắt khi đọc lâu và phù hợp với môi trường tối.

---

## ✅ Tính Năng

### 1. Theme Toggle
- **Nút toggle** trong sidebar
- **One-click** chuyển đổi giữa Light/Dark mode
- **Lưu preference** trong session state
- **Smooth transition** khi chuyển đổi

### 2. Dark Theme Colors
- **Background:** Dark (#121212) thay vì trắng
- **Text:** Light (#E8E8E8) thay vì đen
- **Primary Blue:** Sáng hơn (#4A9EFF) để dễ nhìn trên nền tối
- **Cards:** Dark background với borders
- **Status Colors:** Điều chỉnh cho dark theme

### 3. Component Styling
Tất cả components đã được style cho dark mode:
- ✅ Headers
- ✅ Text và paragraphs
- ✅ Cards (dosing, monitoring, reference)
- ✅ Evidence badges
- ✅ Tables
- ✅ Timeline
- ✅ Buttons
- ✅ Sidebar
- ✅ Streamlit components (alerts, expanders, inputs)

---

## 🎨 Color Scheme

### Light Mode (Mặc định)
- Background: #FFFFFF
- Text: #212529
- Primary Blue: #0066CC

### Dark Mode
- Background: #121212
- Text: #E8E8E8
- Primary Blue: #4A9EFF (sáng hơn)

### Status Colors (Dark Mode)
- **Urgent Red:** #FF6B6B (sáng hơn)
- **Warning Yellow:** #FFD93D
- **Success Green:** #6BCF7F
- **Info Blue:** #4ECDC4

---

## 📁 Files Đã Tạo

### 1. `static/protocol_dark_mode.css`
- Dark mode styles
- CSS variables cho dark theme
- Override cho tất cả components
- Print styles (luôn light khi in)

### 2. `components/protocol_dark_mode.py`
- Theme management functions
- Toggle functionality
- Session state handling
- CSS loading logic

---

## 🚀 Cách Sử Dụng

### Toggle Dark Mode
1. Mở trang Protocol
2. Vào sidebar
3. Tìm nút "🌙 Dark Mode" hoặc "☀️ Light Mode"
4. Click để chuyển đổi
5. Theme tự động apply ngay lập tức

### Theme Persistence
- Theme được lưu trong session state
- Giữ nguyên khi navigate giữa các protocols
- Reset về light mode khi refresh page (có thể cải thiện để lưu trong localStorage)

---

## 💡 Lợi Ích

### 1. Giảm Mỏi Mắt
- ✅ Dark background giảm strain cho mắt
- ✅ Đặc biệt hữu ích khi đọc lâu
- ✅ Phù hợp môi trường tối

### 2. Tiết Kiệm Pin
- ✅ Dark mode tiết kiệm pin trên OLED screens
- ✅ Giảm brightness cần thiết

### 3. User Preference
- ✅ Tùy chọn cá nhân
- ✅ Phù hợp với thói quen sử dụng

---

## 🎯 Technical Details

### Implementation
- **CSS Variables:** Sử dụng CSS custom properties để dễ switch
- **Data Attribute:** `data-theme="dark"` trên HTML element
- **Session State:** Lưu preference trong `st.session_state`
- **Smooth Transition:** CSS transitions cho smooth switching

### CSS Structure
```css
:root[data-theme="dark"] {
    --protocol-bg-main: #121212;
    --protocol-text-primary: #E8E8E8;
    /* ... */
}
```

### JavaScript Integration
- Script để set `data-theme` attribute
- Apply to document, body, và main container
- Load khi page init

---

## 📱 Mobile Support

- ✅ Dark mode hoạt động trên mobile
- ✅ Responsive design
- ✅ Touch-friendly toggle button

---

## 🖨️ Print Support

- ✅ Print styles luôn sử dụng light mode
- ✅ Đảm bảo in ra giấy rõ ràng
- ✅ Background trắng, text đen khi in

---

## 🔄 Future Enhancements

Có thể cải thiện thêm:
1. **localStorage:** Lưu preference trong browser
2. **System Preference:** Auto-detect system dark mode
3. **Scheduled Dark Mode:** Tự động chuyển theo thời gian
4. **Custom Colors:** Cho phép user chọn màu tùy chỉnh

---

## ✅ Checklist

- [x] Dark mode CSS styles
- [x] Theme toggle component
- [x] Session state management
- [x] All components styled
- [x] Smooth transitions
- [x] Print support (light mode)
- [x] Mobile responsive
- [x] Documentation

---

## 🎉 Kết Quả

### Trước
- ❌ Chỉ có light mode
- ❌ Mỏi mắt khi đọc lâu
- ❌ Không phù hợp môi trường tối

### Sau
- ✅ Light và Dark mode
- ✅ Giảm mỏi mắt
- ✅ Phù hợp mọi môi trường
- ✅ User preference

---

*Dark Mode đã sẵn sàng sử dụng! 🌙*

