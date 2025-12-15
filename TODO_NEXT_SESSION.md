# 📋 TODO - Next Session

**Ngày:** 2025-02-05  
**Status:** Ready to Continue

---

## ✅ Đã Hoàn Thành (53 Calculators)

### **Validation System:**
- ✅ Component validation UI (`components/ui/validation.py`)
- ✅ 11 validation functions (`scores/utils/validation.py`)
- ✅ 53 calculators có validation đầy đủ (36 + 17 mới)

### **Result Display Components:**
- ✅ `components/ui/results.py` - Sẵn có
- ✅ `components/ui/scoring.py` - Sẵn có

---

## 🎯 Công Việc Tiếp Theo

### **1. Thêm Validation (Ưu Tiên Cao)** 🔴

#### **Nhi khoa (Quan trọng):**
- [x] **PRISM3** - ✅ ĐÃ CÓ VALIDATION
- [ ] **PEWS** - Vital signs cần validation
- [ ] **Pediatric GCS** - Tương tự GCS
- [x] **PELOD2** - ✅ ĐÃ CÓ VALIDATION

#### **Tiêu hóa:**
- [x] **MELD-Na** - ✅ ĐÃ CÓ VALIDATION
- [x] **Ranson** - ✅ Chỉ có checkboxes, không cần validation

#### **Huyết học:**
- [ ] **Four T's (HIT)** - Platelet count validation
- [ ] **Wells DVT** - Kiểm tra inputs
- [x] **Padua Score** - ✅ ĐÃ CÓ VALIDATION

#### **Hô hấp:**
- [x] **SMART-COP** - ✅ ĐÃ CÓ VALIDATION
- [x] **BODE Index** - ✅ ĐÃ CÓ VALIDATION

#### **Tim mạch:**
- [x] **SCORE2** - ✅ ĐÃ CÓ VALIDATION
- [x] **SCORE2-OP** - ✅ ĐÃ CÓ VALIDATION
- [ ] **HEART Score** - Age, Troponin validation

#### **Thần kinh:**
- [ ] **ICH Score** - Age, GCS, Volume validation

#### **Da liễu:**
- [x] **Parkland Formula** - ✅ ĐÃ CÓ VALIDATION
- [x] **Burn TBSA** - ✅ ĐÃ CÓ VALIDATION
- [x] **SCORAD** - ✅ ĐÃ CÓ VALIDATION
- [x] **PASI** - ✅ ĐÃ CÓ VALIDATION
- [ ] **Burn TBSA** - Percentages validation
- [ ] **SCORAD** - Scores validation
- [ ] **PASI** - Scores validation

#### **Thấp khớp:**
- [x] **DAS28** - ✅ ĐÃ CÓ VALIDATION
- [x] **CDAI** - ✅ ĐÃ CÓ VALIDATION
- [x] **SDAI** - ✅ ĐÃ CÓ VALIDATION

#### **Nhiễm khuẩn:**
- [ ] **MASCC** - Age validation
- [ ] **Pitt Bacteremia** - Temp validation

#### **Chuyển hóa:**
- [x] **Free T4 Index** - ✅ ĐÃ CÓ VALIDATION
- [x] **FENa** - ✅ ĐÃ CÓ VALIDATION

### **2. Cải Thiện UI/UX (Ưu Tiên Trung Bình)** 🟡

#### **Sử dụng Result Display Components:**

**✅ Đã hoàn thành:**
- [x] **PEWS** - `render_score_result()` + `render_score_breakdown()`
- [x] **Pediatric GCS** - `render_score_result()` + `render_score_breakdown()`
- [x] **HEART Score** - `render_score_result()` + `render_score_breakdown()`
- [x] **ICH Score** - `render_score_result()` + `render_score_breakdown()`
- [x] **GCS** - `render_score_result()` + `render_score_breakdown()`
- [x] **MELD** - `render_score_result()`
- [x] **CURB-65** - `render_score_result()` + `render_score_breakdown()`
- [x] **SOFA** - Đã có sẵn từ trước
- [x] **APACHE II** - Đã có sẵn từ trước
- [x] **Child-Pugh** - `render_score_result()` + `render_score_breakdown()`
- [x] **NEWS2** - `render_score_result()` + `render_score_breakdown()`
- [x] **GRACE** - `render_score_result()` + `render_score_breakdown()`
- [x] **MEWS** - `render_score_result()` + `render_score_breakdown()`
- [x] **qSOFA** - `render_score_result()` + `render_score_breakdown()`
- [x] **Wells PE** - `render_score_result()` + `render_score_breakdown()`
- [x] **PESI** - `render_score_result()` + `render_score_breakdown()`
- [x] **Glasgow-Blatchford** - `render_score_result()`
- [x] **ASCVD** - `render_result_box()`
- [x] **Framingham** - `render_result_box()`
- [x] **AIMS65** - `render_score_result()` + `render_score_breakdown()`
- [x] **BISAP** - `render_score_result()` + `render_score_breakdown()`
- [x] **FOUR Score** - `render_score_result()` + `render_score_breakdown()`
- [x] **Rockall** - `render_score_result()`

**✅ Đã hoàn thành (tiếp):**
- [x] **Four T's (HIT)** - `render_score_result()` + `render_score_breakdown()`
- [x] **Wells DVT** - `render_score_result()`
- [x] **MASCC** - `render_score_result()` + `render_score_breakdown()`
- [x] **Pitt Bacteremia** - `render_score_result()` + `render_score_breakdown()`

**Cấp cứu & Hồi sức (10):**
- [ ] APACHE II, III - `render_score_result()` + `render_score_breakdown()`
- [ ] SAPS II, III - `render_score_result()`
- [ ] SOFA, MODS, LODS - `render_score_result()` + `render_score_breakdown()`
- [ ] NEWS2, MEWS, qSOFA - `render_score_result()`

**Tim mạch (4):**
- [ ] GRACE - `render_score_result()` với color coding
- [ ] ASCVD - `render_result_card()` với risk metrics
- [ ] QTc - `render_result_box()` với interpretation
- [ ] Framingham - `render_result_card()` với risk metrics

**Hô hấp (4):**
- [ ] CURB-65, Wells PE, PESI, PSI/PORT - `render_score_result()`

**Tiêu hóa (6):**
- [ ] MELD, Child-Pugh, GBS, AIMS65, BISAP, Rockall - `render_score_result()`

**Chuyển hóa (6):**
- [ ] BMI/IBW/BSA - `render_result_card()` với multiple metrics
- [ ] Corrected Calcium, Anion Gap, Winter, Osmolality, CrCl - `render_result_box()`

**Khác:**
- [ ] GCS, FOUR Score - `render_score_result()` + breakdown
- [ ] RTS, ISS, TRISS - `render_score_result()`
- [ ] PIM2, DIC Score - `render_score_result()`

### **3. Chuẩn Hóa Format** 🟢

- [ ] Tạo template cho score display
- [ ] Chuẩn hóa color coding
- [ ] Chuẩn hóa format cho mortality/risk
- [ ] Chuẩn hóa breakdown tables

### **4. Testing & Documentation** 🔵

- [ ] Test validation functions
- [ ] Test result display components
- [ ] Document usage examples
- [ ] Performance check

---

## 📝 Quick Reference

### **Thêm Validation:**
```python
from scores.utils.validation import validate_age, validate_blood_pressure
from components.ui.validation import render_validation_errors

if st.button("🧮 Tính ..."):
    validation_errors = []
    is_valid_age, age_error = validate_age(age, 0, 120)
    if not is_valid_age:
        validation_errors.append(age_error)
    # ... more validations
    if validation_errors:
        render_validation_errors(validation_errors)
    # ... calculation
```

### **Sử dụng Result Components:**
```python
from components.ui.scoring import render_score_result, render_score_breakdown

render_score_result(
    title="Score Name",
    score=score,
    interpretation="Text",
    mortality="X%",
    color="error",
    icon="🚨"
)
```

---

**File chi tiết:** `TIEN_TRINH_VALIDATION_VA_UI_UX.md`

