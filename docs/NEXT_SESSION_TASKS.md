# 📋 Nhiệm Vụ Các Phiên Tiếp Theo

**Cập nhật:** 2025-01-31  
**Status:** Đang theo dõi

---

## ✅ Đã Hoàn Thành

### **Session 2 - 2025-01-31**
1. ✅ **Đăng ký tất cả calculators** - 67 calculators mới
2. ✅ **Bổ sung 6 kháng sinh** - Nafcillin, Ceftizoxime, Cefotetan, Cefoxitin, Tedizolid, Telavancin, Ceftobiprole
3. ✅ **So sánh & Lộ trình** - COMPREHENSIVE_ROADMAP_VN.md
4. ✅ **UI/UX cải thiện** - Modern design system, enhanced search, favorites

### **Session 3 - 2025-01-31**
1. ✅ **Chuẩn hóa đơn vị** - mmol/L/µmol/L đứng trước, mg/dL sau, format 1 số thập phân
2. ✅ **Việt hóa** - Dịch tất cả text tiếng Anh trong labs module
3. ✅ **Giải thích chi tiết** - Thêm giải thích chuyên sâu cho BMI, IBW, BSA, eGFR, CrCl, CKD
4. ✅ **Sửa lỗi** - Fix lỗi Killip class parsing trong grace.py

---

## 🔥 CẦN LÀM NGAY (P0 - Tuần Này)

### **1. NEWS2 Score** ⏱️ 3-4 giờ
**File:** `scores/emergency/news2.py`  
**Priority:** 🔥🔥🔥 CRITICAL - Dùng hàng ngày ở ward

**Tính năng:**
- National Early Warning Score 2
- Nhịp tim, huyết áp, nhiệt độ, nhịp thở, SpO2
- Alert, oxygen, consciousness
- Thresholds: Low (0-4), Low-Medium (5), Medium (6), High (7+), Very High (≥10)
- Category action plan

**Tham khảo:**
- RCP 2017 NEWS2 guideline
- Category-based response thresholds

---

### **2. ASCVD Risk Calculator (ACC/AHA)** ⏱️ 4-5 giờ
**File:** `scores/cardiology/ascvd.py`  
**Priority:** 🔥🔥🔥 CRITICAL - Thay thế Framingham (hiện đại hơn)

**Tính năng:**
- Pooled Cohort Equations (2013 ACC/AHA)
- 10-year ASCVD risk
- Variables: Age, gender, race, TC, HDL-C, SBP, diabetes, smoking, statin use
- Race categories: White, African American, Other
- Risk categories: <5%, 5-<7.5%, 7.5-<20%, ≥20%
- Recommendations based on risk

**Tham khảo:**
- ACC/AHA 2013 Risk Assessment Guideline
- 2019 ACC/AHA Primary Prevention Update

---

## 📋 CẦN LÀM SAU (P1 - Tháng 2)

### **3. Drug Interaction Checker** ⏱️ 1-2 tuần
**File:** `drugs/interactions.py`  
**Priority:** 🔥🔥🔥 HIGH

**Tính năng:**
- Nhập danh sách thuốc
- Kiểm tra tương tác (Major, Moderate, Minor)
- Cảnh báo và hướng xử trí
- Database: 50-100 thuốc phổ biến ban đầu

---

### **4. Drug Database (Không chỉ kháng sinh)** ⏱️ 1-2 tuần
**File:** `drugs/drug_database.py`  
**Priority:** 🔥🔥🔥 HIGH

**Tính năng:**
- 100-200 thuốc phổ biến ở VN
- Thông tin đầy đủ: liều, chỉ định, chống chỉ định, tác dụng phụ
- Tra cứu theo tên, nhóm, chỉ định

---

### **5. Multi-Scenario Dosing Calculator** ⏱️ 3-5 ngày
**File:** `antibiotics/scenario_dosing_calculator.py`  
**Priority:** 🔥🔥 HIGH

**Tính năng:**
- Tính liều cho nhiều CrCl scenarios cùng lúc
- So sánh trong bảng
- Tích hợp vào database page

---

### **6. Mở Rộng Protocols** ⏱️ 1 tuần
**Priority:** 🔥🔥 MEDIUM

**Thêm:**
- Stroke Management (AHA 2021)
- GI Bleeding Protocol
- Acute Kidney Injury (KDIGO)
- Diabetic Ketoacidosis (DKA)
- Hyperkalemia Emergency

---

## 🔧 CẢI TIẾN UI/UX (P1 - Đang làm)

### **Đã làm:**
- ✅ Modern CSS design system
- ✅ Enhanced search component
- ✅ Improved favorites display
- ✅ Module cards với gradients

### **Còn lại:**
- [ ] Recently Used component enhancement (giống favorites)
- [ ] Export functionality (copy, download text)
- [ ] Dark mode toggle
- [ ] Mobile responsive improvements
- [ ] Loading skeletons

---

## 📊 TÍNH NĂNG NÂNG CAO (P2 - Tháng 3)

### **7. DDx Generator** ⏱️ 2-3 tuần
**File:** `diagnosis/ddx_generator.py`  
**Priority:** 🔥🔥 HIGH

---

### **8. Mini EHR** ⏱️ 2-3 tuần
**File:** `patient/patient_manager.py`  
**Priority:** 🔥🔥 MEDIUM

---

### **9. Fluid Therapy Calculator** ⏱️ 1-2 tuần
**File:** `critical_care/fluids.py`  
**Priority:** 🔥🔥 HIGH

---

### **10. Vasopressor Dosing Guide** ⏱️ 1 tuần
**File:** `critical_care/vasopressors.py`  
**Priority:** 🔥🔥 HIGH

---

## 🎯 Kế Hoạch Tuần Tới

**Ngày 1-2:**
- ✅ NEWS2 Score implementation
- ✅ ASCVD Calculator implementation

**Ngày 3-4:**
- [ ] Testing & bug fixes
- [ ] Documentation

**Ngày 5:**
- [ ] Review và planning cho tuần sau

---

## 📝 Notes

- Tất cả files đã được commit và push
- UI/UX improvements đã hoàn thành
- Ready cho next session: NEWS2 + ASCVD

---

**Next Session Start:** Implement NEWS2 Score

