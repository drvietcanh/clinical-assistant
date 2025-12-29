# Checklist Test Phase 1 & 2 - Drug Database Improvements

**Ngày:** 2025-02-18  
**Mục đích:** Test các cải thiện đã triển khai trong Phase 1 và Phase 2

---

## 🧪 PHASE 1 - CONTENT & SEARCH IMPROVEMENTS

### ✅ Test 1: Side Effects với Frequency Data

**Cách test:**
1. Mở trang Drug Database: `pages/07_💊_Drug_Database.py`
2. Tìm một thuốc bất kỳ (ví dụ: Metformin, Omeprazole, Aspirin)
3. Click "📖 Xem chi tiết"
4. Vào tab "⚠️ Safety"
5. Kiểm tra phần "⚠️ Tác dụng phụ"

**Kết quả mong đợi:**
- ✅ Side effects được phân loại thành:
  - 🟡 Phổ biến (≥1%) - Yellow background
  - 🟠 Ít gặp (0.1-1%) - Orange background
  - ⚪ Hiếm gặp (<0.1%) - Gray background
  - 🔴 Nghiêm trọng - Red background
- ✅ Mỗi category có icon và color coding rõ ràng
- ✅ Layout đẹp, dễ đọc

**Thuốc để test:**
- Metformin (có nhiều side effects)
- Aspirin (có serious effects)
- Warfarin (có monitoring requirements)

---

### ✅ Test 2: Enhanced Search - Tìm theo Indication

**Cách test:**
1. Mở trang Drug Database
2. Trong phần "🔍 Tìm kiếm thuốc"
3. Chọn "Tìm theo: Chỉ định"
4. Nhập: "tăng huyết áp"
5. Click "🔍 Tìm"

**Kết quả mong đợi:**
- ✅ Hiển thị danh sách thuốc có chỉ định "tăng huyết áp"
- ✅ Placeholder text thay đổi: "Ví dụ: tăng huyết áp, đái tháo đường..."
- ✅ Kết quả chính xác (ACE inhibitors, ARBs, Beta-blockers, etc.)

**Test cases:**
- "tăng huyết áp" → Nên có: Amlodipine, Losartan, Metoprolol
- "đái tháo đường" → Nên có: Metformin, Glipizide
- "loét dạ dày" → Nên có: Omeprazole, Pantoprazole

---

### ✅ Test 3: Enhanced Search - Tìm theo Side Effect

**Cách test:**
1. Chọn "Tìm theo: Tác dụng phụ"
2. Nhập: "buồn nôn"
3. Click "🔍 Tìm"

**Kết quả mong đợi:**
- ✅ Hiển thị danh sách thuốc có tác dụng phụ "buồn nôn"
- ✅ Kết quả chính xác

**Test cases:**
- "buồn nôn" → Nên có nhiều thuốc
- "chóng mặt" → Nên có: Metoprolol, Amlodipine
- "táo bón" → Nên có: Opioids, Calcium channel blockers

---

### ✅ Test 4: Enhanced Search - Tìm theo Contraindication

**Cách test:**
1. Chọn "Tìm theo: Chống chỉ định"
2. Nhập: "suy thận"
3. Click "🔍 Tìm"

**Kết quả mong đợi:**
- ✅ Hiển thị danh sách thuốc có chống chỉ định "suy thận"
- ✅ Kết quả chính xác

**Test cases:**
- "suy thận" → Nên có: Metformin (trong một số trường hợp)
- "mang thai" → Nên có: Warfarin, ACE inhibitors
- "suy gan" → Nên có: Paracetamol (liều cao)

---

### ✅ Test 5: Visual Indicators trong Drug Cards

**Cách test:**
1. Mở trang Drug Database
2. Tìm kiếm hoặc duyệt danh sách thuốc
3. Quan sát các drug cards

**Kết quả mong đợi:**
- ✅ Cards hiển thị visual badges:
  - **Pregnancy category:** 🟢 A, 🟡 B, 🟠 C, 🔴 D, ⚫ X
  - **Black Box Warning:** ⚠️ BBW (red badge)
  - **Monitoring Required:** 📊 Monitor (purple badge)
  - **Renal Adjustment:** 🫘 Renal (blue badge)
- ✅ Badges có màu sắc rõ ràng
- ✅ Hover tooltip hiển thị thông tin chi tiết

**Thuốc để test:**
- Warfarin → Nên có: ⚠️ BBW, 📊 Monitor
- Metformin → Nên có: 🫘 Renal
- Aspirin → Nên có: Pregnancy category

---

## 🧪 PHASE 2 - PRINT & MOBILE EXPERIENCE

### ✅ Test 6: Print-Friendly CSS

**Cách test:**
1. Mở trang chi tiết một thuốc bất kỳ
2. Click "🖨️ In" hoặc Ctrl+P (Windows) / Cmd+P (Mac)
3. Xem Print Preview

**Kết quả mong đợi:**
- ✅ Sidebar, buttons, navigation ẩn đi
- ✅ Layout clean, dễ đọc
- ✅ Headers có borders rõ ràng
- ✅ Tables có borders
- ✅ Page breaks hợp lý (không cắt giữa sections)
- ✅ Print header: "Trợ lý lâm sàng - Thông tin thuốc"
- ✅ Print footer: Page numbers
- ✅ Màu sắc: Black text on white background
- ✅ Badges chuyển thành text với borders

**Test cases:**
- Print trang chi tiết thuốc
- Print danh sách thuốc (nếu có)
- Kiểm tra page breaks

---

### ✅ Test 7: Print Button

**Cách test:**
1. Mở trang chi tiết thuốc
2. Tìm nút "🖨️ In" trong action buttons row
3. Click nút

**Kết quả mong đợi:**
- ✅ Nút hiển thị rõ ràng
- ✅ Click nút → Mở print dialog
- ✅ Print preview hiển thị đúng

---

### ✅ Test 8: Mobile Swipe Gestures

**Cách test:**
1. Mở ứng dụng trên mobile device hoặc Chrome DevTools (mobile mode)
2. Mở trang chi tiết một thuốc
3. Swipe từ trái sang phải (swipe right)

**Kết quả mong đợi:**
- ✅ Swipe right → Quay lại trang trước
- ✅ Visual feedback khi swipe:
  - Indicator text hiển thị: "← Quay lại"
  - Smooth animation
- ✅ Swipe hint hiển thị lần đầu: "👆 Vuốt sang phải để quay lại"
- ✅ Hint chỉ hiển thị 1 lần per session

**Test trên:**
- Mobile device (iOS/Android)
- Chrome DevTools mobile mode (F12 → Toggle device toolbar)
- Responsive design mode

---

### ✅ Test 9: Mobile Touch Targets

**Cách test:**
1. Mở ứng dụng trên mobile
2. Kiểm tra các buttons và cards

**Kết quả mong đợi:**
- ✅ Buttons có min-height 44px (Apple HIG standard)
- ✅ Cards có min-height 60px
- ✅ Dễ click/touch
- ✅ Không bị miss-click

**Test cases:**
- Click "📖 Xem chi tiết" button
- Click "🔄 So sánh" button
- Click drug cards
- Click action buttons trong trang chi tiết

---

### ✅ Test 10: Mobile Layout & Spacing

**Cách test:**
1. Mở ứng dụng trên mobile
2. Kiểm tra layout và spacing

**Kết quả mong đợi:**
- ✅ Layout responsive
- ✅ Text dễ đọc (font size ≥ 16px cho inputs)
- ✅ Spacing hợp lý
- ✅ Không bị overflow
- ✅ Bottom navigation hiển thị đúng

---

## 📋 QUICK TEST SCENARIOS

### Scenario 1: Tìm thuốc cho bệnh nhân tăng huyết áp
1. Search "tăng huyết áp" (Chỉ định)
2. Xem danh sách thuốc
3. Click vào một thuốc (ví dụ: Amlodipine)
4. Kiểm tra visual indicators
5. Xem side effects với frequency
6. In thông tin (nếu cần)

### Scenario 2: Kiểm tra tác dụng phụ của thuốc
1. Search "buồn nôn" (Tác dụng phụ)
2. Xem danh sách thuốc có tác dụng phụ này
3. Click vào một thuốc
4. Xem chi tiết side effects với frequency categories

### Scenario 3: Mobile usage
1. Mở trên mobile
2. Tìm thuốc
3. Xem chi tiết
4. Swipe right để quay lại
5. Test touch targets

---

## 🐛 BUGS CẦN KIỂM TRA

### Potential Issues:
- [ ] Search không tìm thấy kết quả khi nên có
- [ ] Side effects không hiển thị đúng categories
- [ ] Visual indicators không hiển thị
- [ ] Print layout bị lỗi
- [ ] Swipe gestures không hoạt động
- [ ] Mobile layout bị vỡ
- [ ] Touch targets quá nhỏ

---

## ✅ CHECKLIST TỔNG HỢP

### Phase 1:
- [ ] Side Effects với frequency data
- [ ] Search by Indication
- [ ] Search by Side Effect
- [ ] Search by Contraindication
- [ ] Visual Indicators trong cards

### Phase 2:
- [ ] Print-friendly CSS
- [ ] Print Button
- [ ] Mobile Swipe Gestures
- [ ] Mobile Touch Targets
- [ ] Mobile Layout

---

## 📝 GHI CHÚ TEST

**Test Date:** _______________

**Tester:** _______________

**Environment:**
- Browser: _______________
- Device: _______________
- Screen Size: _______________

**Issues Found:**
1. 
2. 
3. 

**Notes:**
- 

---

**Tác giả:** AI Assistant  
**Ngày:** 2025-02-18  
**Version:** 1.0

