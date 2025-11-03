# 🔍 Phân Tích Code Và Đề Xuất Refactoring

**Date:** 2025-02-03  
**Mục tiêu:** Kiểm tra các file dài và đề xuất cách chia nhỏ để cải thiện maintainability

---

## 📊 TỔNG QUAN CÁC FILE DÀI NHẤT

| File | Lines | Type | Cần Refactor? |
|------|-------|------|---------------|
| `drugs/drug_database.py` | 5754 | Data dictionary | ❌ **KHÔNG** - Chỉ là data |
| `antibiotics/antibiotics_data.py` | 3203 | Data dictionary | ❌ **KHÔNG** - Chỉ là data |
| `antibiotics/dosing_calculator.py` | 1198 | Code + Logic | ✅ **CÓ** - Render function quá dài |
| `antibiotics/database.py` | 1027 | Code + UI | ✅ **CÓ** - Render function quá dài |
| `scores/nephrology/egfr.py` | 938 | Code + Logic | ⚠️ **CÓ THỂ** - Nhiều functions nhỏ |

---

## ✅ FILE KHÔNG CẦN REFACTOR

### **1. drugs/drug_database.py (5754 lines)**
- **Loại:** Data dictionary thuần túy
- **Cấu trúc:** `DRUG_DATABASE = {...}` với 131 thuốc
- **Lý do không refactor:**
  - Chỉ chứa dữ liệu tĩnh
  - Dễ đọc và maintain
  - Không có logic phức tạp
- **Đề xuất:** Giữ nguyên

### **2. antibiotics/antibiotics_data.py (3203 lines)**
- **Loại:** Data dictionary thuần túy  
- **Cấu trúc:** `ANTIBIOTICS_DATABASE = {...}` với 63 kháng sinh
- **Lý do không refactor:**
  - Chỉ chứa dữ liệu tĩnh
  - Dễ đọc và maintain
  - Không có logic phức tạp
- **Đề xuất:** Giữ nguyên

---

## ✅ FILE CẦN REFACTOR

### **1. antibiotics/dosing_calculator.py (1198 lines)**

#### **Phân tích:**
- **11 functions** trong file
- **`render_dosing_calculator()`** function rất dài (~600 lines)
- Chứa nhiều UI rendering code và logic tính toán

#### **Cấu trúc hiện tại:**
```
calculate_ibw()
calculate_abw()
calculate_bmi()
get_renal_category()
parse_dosage_text()
calculate_infusion_details()
calculate_detailed_dose()
check_warnings()
calculate_icu_adjustment()
calculate_adjusted_dose()
render_dosing_calculator()  ← QUÁ DÀI (~600 lines)
```

#### **Vấn đề:**
1. `render_dosing_calculator()` quá dài, khó maintain
2. Trộn lẫn UI rendering và business logic
3. Khó test từng phần riêng biệt

#### **Đề xuất refactoring:**

```
antibiotics/
├── dosing_calculator.py (logic thuần túy - giữ lại)
│   ├── calculate_ibw()
│   ├── calculate_abw()
│   ├── calculate_bmi()
│   ├── get_renal_category()
│   ├── parse_dosage_text()
│   ├── calculate_infusion_details()
│   ├── calculate_detailed_dose()
│   ├── check_warnings()
│   ├── calculate_icu_adjustment()
│   └── calculate_adjusted_dose()
│
├── dosing_ui/ (NEW - UI rendering)
│   ├── __init__.py
│   ├── patient_inputs.py  ← Patient input forms
│   ├── dosage_display.py  ← Dosage result display
│   ├── warnings_display.py ← Warnings/alerts display
│   └── calculator_layout.py ← Main layout orchestrator
│
└── dosing_calculator_page.py (NEW - thin controller)
    └── render_dosing_calculator() ← Chỉ orchestrate, gọi UI components
```

**Chi tiết:**
1. **`dosing_ui/patient_inputs.py`** (~150 lines)
   - Age, weight, height inputs
   - Special conditions (ICU, dialysis, pregnancy)
   - Renal function inputs (CrCl/eGFR)

2. **`dosing_ui/dosage_display.py`** (~150 lines)
   - Display calculated doses
   - Infusion details
   - Renal adjustments

3. **`dosing_ui/warnings_display.py`** (~100 lines)
   - Warning messages
   - Contraindications
   - Drug interactions

4. **`dosing_ui/calculator_layout.py`** (~200 lines)
   - Main layout
   - Tab organization
   - Integration with other components

5. **`dosing_calculator_page.py`** (~50 lines)
   - Thin controller
   - Orchestrate UI components
   - Handle session state

---

### **2. antibiotics/database.py (1027 lines)**

#### **Phân tích:**
- **12 functions** trong file
- **`render_database()`** function dài (~250 lines)
- **`display_antibiotic_info()`** function dài (~170 lines)
- Chứa nhiều UI rendering code

#### **Cấu trúc hiện tại:**
```
search_antibiotics()
get_antibiotic_autocomplete_suggestions()
get_recent_searches()
add_to_recent_searches()
filter_antibiotics()
_escape_html()
render_compact_antibiotic_card()
render_quick_dosing_calculator()
display_antibiotic_info()  ← DÀI (~170 lines)
_render_antibiotic_export()
render_database()  ← DÀI (~250 lines)
render_antibiotic_lookup()
```

#### **Vấn đề:**
1. `render_database()` quá dài và phức tạp
2. `display_antibiotic_info()` có nhiều HTML/CSS inline
3. Trộn lẫn search logic và UI rendering

#### **Đề xuất refactoring:**

```
antibiotics/
├── database.py (giữ lại - core search/filter logic)
│   ├── search_antibiotics()
│   ├── get_antibiotic_autocomplete_suggestions()
│   ├── get_recent_searches()
│   ├── add_to_recent_searches()
│   └── filter_antibiotics()
│
├── database_ui/ (NEW - UI components)
│   ├── __init__.py
│   ├── search_ui.py  ← Search input + suggestions
│   ├── filters_ui.py ← Filter controls
│   ├── card_ui.py  ← Compact antibiotic cards
│   ├── detail_ui.py  ← Detailed antibiotic info display
│   ├── export_ui.py  ← Export functionality
│   └── layout_ui.py  ← Main database layout
│
└── database_page.py (NEW - thin controller)
    ├── render_database() ← Orchestrate
    └── render_antibiotic_lookup() ← Simple lookup
```

**Chi tiết:**
1. **`database_ui/search_ui.py`** (~100 lines)
   - Search input
   - Autocomplete suggestions
   - Recent searches

2. **`database_ui/filters_ui.py`** (~80 lines)
   - Group filter
   - Route filter
   - AWaRe filter

3. **`database_ui/card_ui.py`** (~120 lines)
   - `render_compact_antibiotic_card()`
   - Card styling and interactions

4. **`database_ui/detail_ui.py`** (~200 lines)
   - `display_antibiotic_info()`
   - Detailed information display
   - HTML/CSS rendering

5. **`database_ui/export_ui.py`** (~100 lines)
   - `_render_antibiotic_export()`
   - Export formatting

6. **`database_ui/layout_ui.py`** (~150 lines)
   - Main layout
   - Tabs (Info, Favorites, Recent)
   - Integration

7. **`database_page.py`** (~80 lines)
   - Thin controller
   - Orchestrate components

---

### **3. scores/nephrology/egfr.py (938 lines)**

#### **Phân tích:**
- **14 functions** trong file
- Functions tương đối ngắn (~50-100 lines mỗi function)
- **`render()`** function dài (~700 lines)

#### **Cấu trúc hiện tại:**
```
calculate_bsa_mosteller()
calculate_bsa_dubois()
calculate_bsa_haycock()
calculate_bsa_boyd()
calculate_bsa_shuter_aslani()
calculate_ckd_epi()
calculate_mdrd()
calculate_cockcroft_gault()
calculate_abw()
calculate_ibw()
convert_egfr_to_absolute_gfr()
interpret_egfr()
get_recommended_formula()
render()  ← DÀI (~700 lines)
```

#### **Vấn đề:**
1. `render()` function quá dài
2. Trộn lẫn calculation logic và UI rendering

#### **Đề xuất refactoring:**

```
scores/nephrology/
├── egfr_calculations.py (NEW - calculation logic)
│   ├── calculate_bsa_mosteller()
│   ├── calculate_bsa_dubois()
│   ├── calculate_bsa_haycock()
│   ├── calculate_bsa_boyd()
│   ├── calculate_bsa_shuter_aslani()
│   ├── calculate_ckd_epi()
│   ├── calculate_mdrd()
│   ├── calculate_cockcroft_gault()
│   ├── calculate_abw()
│   ├── calculate_ibw()
│   ├── convert_egfr_to_absolute_gfr()
│   ├── interpret_egfr()
│   └── get_recommended_formula()
│
├── egfr_ui.py (NEW - UI rendering)
│   ├── render_input_form()
│   ├── render_results()
│   ├── render_comparison()
│   └── render_interpretation()
│
└── egfr.py (REFACTORED - thin controller)
    └── render()  ← Chỉ orchestrate (~100 lines)
```

---

## 📋 KẾ HOẠCH REFACTORING ƯU TIÊN

### **Priority 1: High Impact, Low Risk**
1. ✅ **antibiotics/dosing_calculator.py**
   - Tách UI rendering ra khỏi logic
   - Tạo `dosing_ui/` module
   - **Thời gian:** 2-3 giờ
   - **Lợi ích:** Dễ maintain, test, reuse

### **Priority 2: High Impact, Medium Risk**
2. ✅ **antibiotics/database.py**
   - Tách UI components ra khỏi search logic
   - Tạo `database_ui/` module
   - **Thời gian:** 3-4 giờ
   - **Lợi ích:** Dễ maintain, test, extend

### **Priority 3: Medium Impact, Low Risk**
3. ⚠️ **scores/nephrology/egfr.py**
   - Tách calculations ra khỏi UI
   - Tạo `egfr_calculations.py`
   - **Thời gian:** 1-2 giờ
   - **Lợi ích:** Dễ test calculations, reuse

---

## 🎯 NGUYÊN TẮC REFACTORING

### **1. Separation of Concerns**
- **Logic** tách khỏi **UI rendering**
- **Data processing** tách khỏi **display**

### **2. Single Responsibility**
- Mỗi module/function chỉ làm một việc
- UI components chỉ render, không tính toán

### **3. Reusability**
- Calculation functions có thể reuse
- UI components có thể reuse

### **4. Testability**
- Logic functions dễ test unit test
- UI components có thể test riêng

### **5. Maintainability**
- Files nhỏ hơn, dễ đọc
- Dễ tìm và sửa bugs
- Dễ thêm features mới

---

## ✅ KẾT LUẬN

**Cần refactor:**
1. ✅ `antibiotics/dosing_calculator.py` - **PRIORITY 1**
2. ✅ `antibiotics/database.py` - **PRIORITY 2**
3. ⚠️ `scores/nephrology/egfr.py` - **PRIORITY 3**

**Không cần refactor:**
- ❌ `drugs/drug_database.py` (data only)
- ❌ `antibiotics/antibiotics_data.py` (data only)

**Lợi ích refactoring:**
- ✅ Code dễ maintain hơn
- ✅ Dễ test hơn
- ✅ Dễ extend features mới
- ✅ Tăng code reusability
- ✅ Giảm complexity

---

**Ready to start refactoring?** ✅

