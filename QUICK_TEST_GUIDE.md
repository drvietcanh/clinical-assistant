# Hướng Dẫn Test Nhanh Phase 1 & 2

## ✅ KẾT QUẢ TEST TỰ ĐỘNG

**Tests đã pass:**
- ✅ Print CSS: Tìm thấy và có @media print
- ✅ Mobile CSS: Tìm thấy và có swipe styles

**Tests cần test manual (cần Streamlit app):**
- ⚠️ Side Effects Frequency
- ⚠️ Search Functions  
- ⚠️ Visual Indicators
- ⚠️ Search trong Side Effects

---

## 🚀 CÁCH TEST NHANH

### Bước 1: Chạy ứng dụng
```bash
streamlit run app.py
```

Hoặc nếu dùng virtual environment:
```bash
# Activate venv
# Then:
streamlit run app.py
```

### Bước 2: Test Phase 1

#### Test 1: Side Effects với Frequency
1. Vào: `http://localhost:8501/pages/07_💊_Drug_Database.py`
2. Tìm: "Metformin" hoặc "Aspirin"
3. Click "📖 Xem chi tiết"
4. Tab "⚠️ Safety" → Xem "⚠️ Tác dụng phụ"
5. **Kiểm tra:** Có categories (Phổ biến, Ít gặp, Hiếm gặp, Nghiêm trọng)?

#### Test 2: Enhanced Search
1. Trong trang Drug Database
2. Dropdown "Tìm theo:" → Chọn "Chỉ định"
3. Nhập: "tăng huyết áp"
4. Click "🔍 Tìm"
5. **Kiểm tra:** Có kết quả? (Amlodipine, Losartan, etc.)

#### Test 3: Visual Indicators
1. Duyệt danh sách thuốc
2. **Kiểm tra:** Cards có badges?
   - Pregnancy: 🟢 A, 🟡 B, etc.
   - Black Box: ⚠️ BBW
   - Monitoring: 📊 Monitor
   - Renal: 🫘 Renal

### Bước 3: Test Phase 2

#### Test 4: Print Function
1. Mở trang chi tiết thuốc
2. Click nút "🖨️ In"
3. **Kiểm tra:** Print dialog mở? Layout đẹp?

#### Test 5: Mobile Swipe (nếu có mobile)
1. Mở trên mobile hoặc Chrome DevTools (F12 → Toggle device)
2. Mở trang chi tiết thuốc
3. Swipe right (vuốt sang phải)
4. **Kiểm tra:** Quay lại được?

---

## 📋 CHECKLIST NHANH

- [ ] Side Effects có frequency categories
- [ ] Search by Indication hoạt động
- [ ] Search by Side Effect hoạt động
- [ ] Search by Contraindication hoạt động
- [ ] Visual indicators hiển thị trên cards
- [ ] Print button hoạt động
- [ ] Print layout đẹp
- [ ] Mobile swipe gestures hoạt động (nếu test trên mobile)

---

## 🐛 NẾU CÓ LỖI

**Lỗi thường gặp:**
1. **Search không tìm thấy:** Kiểm tra xem có thuốc nào có data không
2. **Visual indicators không hiển thị:** Kiểm tra drug data có đủ fields không
3. **Print không đẹp:** Kiểm tra browser print settings

**Debug:**
- Mở browser console (F12)
- Kiểm tra errors
- Kiểm tra network requests

---

**Tác giả:** AI Assistant  
**Ngày:** 2025-02-18

