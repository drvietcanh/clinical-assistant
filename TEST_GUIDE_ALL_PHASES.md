# Hướng Dẫn Test Tất Cả Phases

**Ngày:** 2025-02-18  
**Mục đích:** Test tất cả các cải thiện đã làm trong Phase 1, 2, và 3

---

## 🚀 CÁCH CHẠY TEST

### Test Tự Động:
```bash
# Test Phase 1 & 2
python test_phase_1_2.py

# Test Phase 3
python test_phase_3.py
```

### Test Manual trong App:
```bash
streamlit run app.py
```

---

## 📋 CHECKLIST TEST NHANH

### Phase 1 Tests:

#### ✅ Test 1: Side Effects với Frequency
1. Vào: Drug Database → Tìm "Metformin" hoặc "Aspirin"
2. Click "📖 Xem chi tiết"
3. Tab "⚠️ Safety" → "⚠️ Tác dụng phụ"
4. **Kiểm tra:** Có categories (Phổ biến, Ít gặp, Hiếm gặp, Nghiêm trọng)?

#### ✅ Test 2: Enhanced Search
1. Drug Database → Dropdown "Tìm theo:"
2. Test 4 options:
   - **Chỉ định:** "tăng huyết áp" → Có kết quả?
   - **Tác dụng phụ:** "buồn nôn" → Có kết quả?
   - **Chống chỉ định:** "suy thận" → Có kết quả?
   - **Tên thuốc:** "Metformin" → Có kết quả?

#### ✅ Test 3: Visual Indicators
1. Duyệt danh sách thuốc
2. **Kiểm tra:** Cards có badges?
   - Pregnancy: 🟢 A, 🟡 B, etc.
   - Black Box: ⚠️ BBW
   - Monitoring: 📊 Monitor
   - Renal: 🫘 Renal

---

### Phase 2 Tests:

#### ✅ Test 4: Print Function
1. Mở trang chi tiết thuốc
2. Click nút "🖨️ In"
3. **Kiểm tra:** Print dialog mở? Layout đẹp?

#### ✅ Test 5: Mobile Swipe (nếu có mobile)
1. Mở trên mobile hoặc Chrome DevTools (F12 → Toggle device)
2. Mở trang chi tiết thuốc
3. Swipe right (vuốt sang phải)
4. **Kiểm tra:** Quay lại được?

---

### Phase 3 Tests:

#### ✅ Test 6: Related Drugs - Same Group
1. Mở trang chi tiết một thuốc (ví dụ: Metformin)
2. Scroll xuống phần "💊 Thuốc cùng nhóm"
3. **Kiểm tra:**
   - Có hiển thị thuốc cùng nhóm?
   - Cards có gradient backgrounds?
   - Cards có visual indicators?
   - Hover effects hoạt động?

#### ✅ Test 7: Related Drugs - Alternative Drugs
1. Mở trang chi tiết một thuốc có indication (ví dụ: Metformin)
2. Scroll xuống phần "🔄 Thuốc thay thế (cùng chỉ định)"
3. **Kiểm tra:**
   - Có hiển thị thuốc cùng indication nhưng khác group?
   - Cards có yellow gradient?
   - Click vào có thể xem thuốc đó?

#### ✅ Test 8: Interaction Matrix
1. Vào: Drug Database → "🔍 Kiểm tra tương tác thuốc"
2. Chọn 3-4 thuốc (ví dụ: Warfarin, Aspirin, Metformin)
3. Click "Kiểm tra"
4. **Kiểm tra:**
   - Ma trận hiển thị?
   - Color coding đúng (🔴 Major, 🟡 Moderate, 🔵 Minor)?
   - Hover để xem tooltip?
   - Styling đẹp?

---

## 🎯 QUICK TEST SCENARIOS

### Scenario 1: Tìm thuốc và xem chi tiết
1. Search "tăng huyết áp" (Chỉ định)
2. Chọn một thuốc (ví dụ: Amlodipine)
3. Xem chi tiết
4. Kiểm tra:
   - Side effects với frequency
   - Visual indicators
   - Related drugs (same group)
   - Alternative drugs
   - Print button

### Scenario 2: Kiểm tra tương tác
1. Vào Interaction Checker
2. Chọn: Warfarin + Aspirin
3. Xem ma trận tương tác
4. Kiểm tra:
   - Ma trận hiển thị đúng
   - Color coding
   - Chi tiết interaction

### Scenario 3: Mobile experience
1. Mở trên mobile/Chrome DevTools mobile mode
2. Tìm thuốc
3. Xem chi tiết
4. Test swipe gestures
5. Test touch targets

---

## 📊 EXPECTED RESULTS

### Phase 1:
- ✅ Side Effects có 4 categories với color coding
- ✅ Search hoạt động với 4 loại tìm kiếm
- ✅ Cards có visual indicators

### Phase 2:
- ✅ Print layout đẹp, ẩn elements không cần
- ✅ Mobile swipe hoạt động smooth
- ✅ Touch targets đủ lớn (44px+)

### Phase 3:
- ✅ Related drugs hiển thị 2 sections (same group + alternatives)
- ✅ Cards có gradient và indicators
- ✅ Interaction matrix có enhanced styling

---

## 🐛 KNOWN ISSUES

**Nếu có lỗi:**
1. Check browser console (F12)
2. Check Streamlit logs
3. Verify data có trong database
4. Check network requests

---

## ✅ TEST CHECKLIST

### Phase 1:
- [ ] Side Effects frequency categories
- [ ] Search by Indication
- [ ] Search by Side Effect
- [ ] Search by Contraindication
- [ ] Visual indicators trong cards

### Phase 2:
- [ ] Print-friendly CSS
- [ ] Print Button
- [ ] Mobile Swipe Gestures
- [ ] Mobile Touch Targets

### Phase 3:
- [ ] Related Drugs - Same Group
- [ ] Related Drugs - Alternative Drugs
- [ ] Enhanced Interaction Matrix
- [ ] Improved styling

---

**Tác giả:** AI Assistant  
**Ngày:** 2025-02-18  
**Version:** 1.0

