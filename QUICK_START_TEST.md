# Quick Start Test Guide - 5 Phút Test

**Mục đích:** Test nhanh các tính năng chính trong 5 phút

---

## 🚀 BƯỚC 1: Chạy App (1 phút)

```bash
streamlit run app.py
```

Mở browser: `http://localhost:8501`

---

## ✅ BƯỚC 2: Test Nhanh (4 phút)

### Test 1: Enhanced Search (1 phút)
1. Vào: **Drug Database**
2. Dropdown "Tìm theo:" → Chọn **"Chỉ định"**
3. Gõ: `tăng huyết áp`
4. ✅ **Kiểm tra:** Có kết quả? (Amlodipine, Losartan, etc.)

### Test 2: Drug Detail với Side Effects (1 phút)
1. Click vào một thuốc (ví dụ: **Metformin**)
2. Tab **"⚠️ Safety"** → **"⚠️ Tác dụng phụ"**
3. ✅ **Kiểm tra:** Có categories? (Phổ biến, Ít gặp, Hiếm gặp, Nghiêm trọng)

### Test 3: Related Drugs (1 phút)
1. Scroll xuống trang drug detail
2. ✅ **Kiểm tra:** Có section **"💊 Thuốc cùng nhóm"**?
3. ✅ **Kiểm tra:** Có section **"🔄 Thuốc thay thế"**? (nếu có indication)

### Test 4: Print & Visual (1 phút)
1. Click nút **"🖨️ In"** (hoặc Ctrl+P)
2. ✅ **Kiểm tra:** Print preview đẹp? (Sidebar, buttons ẩn)
3. Quay lại → Kiểm tra Visual Indicators trên cards (Pregnancy, Black Box, etc.)

---

## 🎯 QUICK CHECKLIST

- [ ] Enhanced Search hoạt động (Chỉ định)
- [ ] Side Effects có categories
- [ ] Related Drugs hiển thị
- [ ] Print preview đẹp
- [ ] Visual Indicators hiển thị trên cards

**Nếu tất cả ✅ → Các tính năng chính hoạt động tốt!**

**Nếu có ❌ → Xem `TEST_GUIDE_ALL_PHASES.md` để test chi tiết hơn**

---

**Thời gian:** ~5 phút  
**Version:** 1.0

