# 📋 KẾ HOẠCH PHASE 6, 7, 8
## Pediatric, Renal, Titration & Safety Features

**Ngày bắt đầu:** Sau Phase 5  
**Mục tiêu:** Bổ sung các tính năng quan trọng còn thiếu

---

## 🎯 PHASE 6: PEDIATRIC & RENAL DOSING

### 6.1: Pediatric Dosing Calculator ⭐⭐⭐

**Thời gian:** 5-6 ngày

**Tính năng:**
- [ ] Input: Tuổi, cân nặng, tình trạng
- [ ] Tính liều theo công thức pediatric
- [ ] Cảnh báo liều tối đa theo tuổi
- [ ] Hướng dẫn pha cho trẻ em
- [ ] Database liều pediatric cho 7 thuốc

**Files:**
- `drugs/pediatric_dosing.py`
- `components/pediatric_dosing_calculator.py`
- `drugs/pediatric_dosing_database.json`

**Integration:**
- Cardiovascular Calculator (thêm mode "Pediatric")

---

### 6.2: Renal Dose Adjustment Calculator ⭐⭐⭐

**Thời gian:** 5-6 ngày

**Tính năng:**
- [ ] Input: eGFR/CrCl, thuốc
- [ ] Tính liều điều chỉnh
- [ ] Cảnh báo khi cần giảm liều
- [ ] Database điều chỉnh liều cho từng thuốc
- [ ] Hướng dẫn điều chỉnh

**Files:**
- `drugs/renal_dosing.py`
- `components/renal_dosing_calculator.py`
- `drugs/renal_dosing_database.json`

**Integration:**
- Cardiovascular Calculator (thêm tab "Renal Adjustment")
- TDM module

---

## 🎯 PHASE 7: TITRATION & SAFETY

### 7.1: Infusion Rate Titration Guide ⭐⭐⭐

**Thời gian:** 4-5 ngày

**Tính năng:**
- [ ] Input: Liều hiện tại, liều mới
- [ ] Tính tốc độ mới
- [ ] Hiển thị thay đổi
- [ ] Lưu lịch sử titration (session state)
- [ ] Hướng dẫn titration

**Files:**
- `critical_care/titration_guide.py`
- `components/titration_calculator.py`

**Integration:**
- Cardiovascular Calculator
- Multiple Infusions Calculator

---

### 7.2: Infusion Safety Checker ⭐⭐

**Thời gian:** 4-5 ngày

**Tính năng:**
- [ ] Kiểm tra liều vs max dose
- [ ] Kiểm tra tốc độ vs giới hạn
- [ ] Checklist an toàn
- [ ] Cảnh báo rõ ràng
- [ ] Safety score

**Files:**
- `critical_care/safety_checker.py`
- `components/safety_checker.py`

**Integration:**
- Tất cả infusion calculators
- Hiển thị trước khi tính toán

---

## 🎯 PHASE 8: QUICK REFERENCE & PRESETS

### 8.1: Quick Reference Tables ⭐⭐

**Thời gian:** 3-4 ngày

**Tính năng:**
- [ ] Bảng liều thường dùng
- [ ] Bảng nồng độ pha
- [ ] Bảng tốc độ tham khảo
- [ ] Quick lookup
- [ ] Printable reference

**Files:**
- `components/quick_reference.py`
- `data/quick_reference_data.json`

**Integration:**
- Cardiovascular Calculator (tab "Quick Reference")
- Hoặc tạo page riêng

---

### 8.2: Custom Drug Presets ⭐⭐

**Thời gian:** 3-4 ngày

**Tính năng:**
- [ ] UI thêm thuốc mới
- [ ] Lưu preset (local storage)
- [ ] Import/Export preset
- [ ] Sử dụng preset trong calculator
- [ ] Quản lý presets

**Files:**
- `drugs/custom_presets.py`
- `components/custom_presets_manager.py`

**Integration:**
- Cardiovascular Calculator
- Settings/Preferences

---

### 8.3: Time Remaining Calculator ⭐⭐

**Thời gian:** 2-3 ngày

**Tính năng:**
- [ ] Input: Thể tích ban đầu, đã truyền, tốc độ
- [ ] Tính thời gian còn lại
- [ ] Cảnh báo khi < 1 giờ
- [ ] Hiển thị % đã truyền
- [ ] Progress bar

**Files:**
- `critical_care/time_remaining.py`
- `components/time_remaining_calculator.py`

**Integration:**
- Enhanced Infusion Calculator
- Hoặc tạo tab riêng

---

## 📅 TIMELINE TỔNG HỢP

**Phase 6:** 10-12 ngày (2.5-3 tuần)
- 6.1: Pediatric (5-6 ngày)
- 6.2: Renal (5-6 ngày)

**Phase 7:** 8-10 ngày (2 tuần)
- 7.1: Titration (4-5 ngày)
- 7.2: Safety (4-5 ngày)

**Phase 8:** 8-11 ngày (2-2.5 tuần)
- 8.1: Quick Reference (3-4 ngày)
- 8.2: Custom Presets (3-4 ngày)
- 8.3: Time Remaining (2-3 ngày)

**Tổng:** 26-33 ngày (5-6.5 tuần)

---

## ✅ CHECKLIST

### Phase 6:
- [ ] Pediatric dosing calculator
- [ ] Renal dose adjustment calculator
- [ ] Integration
- [ ] Testing

### Phase 7:
- [ ] Titration guide
- [ ] Safety checker
- [ ] Integration
- [ ] Testing

### Phase 8:
- [ ] Quick reference
- [ ] Custom presets
- [ ] Time remaining
- [ ] Integration
- [ ] Testing

---

*© 2025 - Kế hoạch Phase 6, 7, 8*

