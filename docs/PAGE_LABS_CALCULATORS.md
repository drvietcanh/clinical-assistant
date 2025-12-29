# 📋 Labs & Calculators Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Labs & Calculators để tránh sai sót.

---

## 📑 MỤC LỤC

1. [Tổng Quan](#tổng-quan)
2. [Cấu Trúc Files](#cấu-trúc-files)
3. [Các Chức Năng Chính](#các-chức-năng-chính)
4. [Data Structure](#data-structure)
5. [Components & Dependencies](#components--dependencies)
6. [Workflow & User Journey](#workflow--user-journey)
7. [Recent Changes & Improvements](#recent-changes--improvements)
8. [Lưu Ý Khi Làm Việc](#lưu-ý-khi-làm-việc)
9. [Testing Checklist](#testing-checklist)

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **Labs & Calculators** cung cấp:
- Tra cứu giá trị xét nghiệm và giải thích kết quả
- Tính toán công thức lâm sàng (calculators)
- Phân tích xu hướng xét nghiệm (trend analysis)
- Chuyển đổi đơn vị y khoa

### Main Entry Point
- **File:** `pages/05_🔬_Labs_and_Calculators.py`
- **URL Route:** `/pages/05_🔬_Labs_and_Calculators`
- **Page Title:** "Xét nghiệm & Calculators"

### Related Pages
- `pages/01_📊_Scores.py` - Thang điểm lâm sàng
- `pages/08_📊_TDM.py` - Theo dõi nồng độ thuốc

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/05_🔬_Labs_and_Calculators.py
├── Sidebar với 4 categories:
│   ├── 🧮 Calculators
│   ├── 🔬 Lab Panels
│   ├── 📈 Lab Enhancement
│   └── 🔄 Unit Converter
├── Routing logic cho từng category
└── Imports từ labs/ và scores/
```

### Core Modules

#### Labs Module (`labs/`)
```
labs/
├── __init__.py                      # Main exports
├── cbc.py                          # Complete Blood Count
├── bmp.py                          # Basic Metabolic Panel
├── cmp.py                          # Comprehensive Metabolic Panel
├── lft.py                          # Liver Function Tests
├── lipid.py                        # Lipid Panel
├── cardiac.py                      # Cardiac Markers
├── coag.py                         # Coagulation Panel
├── thyroid.py                      # Thyroid Function Tests
├── abg.py                          # Arterial Blood Gas
├── trend_analysis.py               # Lab Trend Analysis
├── panel_calculator.py             # Lab Panel Calculator
└── normal_ranges.py                 # Reference ranges
```

#### Scores Module (Calculators) (`scores/`)
```
scores/
├── metabolism/
│   ├── bmi_ibw_bsa.py             # BMI, IBW, BSA
│   ├── osmolality.py              # Osmolality & Gap
│   ├── anion_gap.py               # Anion Gap
│   ├── corrected_calcium.py       # Corrected Calcium
│   ├── fena.py                    # FENa
│   ├── hba1c_eag.py               # HbA1c ↔ eAG
│   ├── winter_formula.py          # Winter Formula
│   └── free_t4_index.py           # Free T4 Index
└── nephrology/
    └── egfr.py                    # eGFR/GFR Calculator
```

#### Components
```
components/
└── unit_converter_enhanced.py     # Enhanced Unit Converter
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. 🧮 Calculators
**Category:** Calculators  
**Sub-options:** 10 calculators

**Available Calculators:**
1. **📏 BMI | IBW | BSA** - `render_bmi_ibw_bsa()`
2. **🧪 eGFR/GFR Calculator** - `render_egfr()`
3. **💧 Osmolality & Gap** - `render_osmolality()`
4. **⚖️ Anion Gap** - `render_anion_gap()`
5. **🦴 Corrected Calcium** - `render_corrected_calcium()`
6. **🧪 FENa** - `render_fena()`
7. **📊 HbA1c ↔ eAG** - `render_hba1c_eag()`
8. **🌡️ Winter Formula** - `render_winter_formula()`
9. **🔬 Free T4 Index** - `render_free_t4_index()`
10. **💊 Lipid Panel Calculator** - `render_lipid()`

**Routing Logic:**
- String matching trong `calculator_type`
- Case-insensitive matching
- Routes to appropriate render function

### 2. 🔬 Lab Panels
**Category:** Lab Panels  
**Sub-options:** 8 lab panels

**Available Panels:**
1. **🩸 CBC** - `render_cbc()`
2. **🧪 BMP** - `render_bmp()`
3. **🧪 CMP** - `render_cmp()`
4. **🫀 LFT** - `render_lft()`
5. **❤️ Cardiac Markers** - `render_cardiac_markers()`
6. **🩸 Coagulation Panel** - `render_coag()`
7. **🦋 Thyroid Function Tests** - `render_thyroid()`
8. **💨 ABG** - `render_abg()`

**Quick Actions:**
- BMP/CMP: eGFR, Anion Gap, Osmolality, Corrected Ca
- Thyroid: Free T4 Index
- Quick actions set `st.session_state.quick_action` và render calculator tương ứng

### 3. 📈 Lab Enhancement
**Category:** Lab Enhancement  
**Sub-options:** 2 features

**Available Features:**
1. **📈 Lab Trend Analysis** - `render_trend_analysis()`
2. **🧮 Lab Panel Calculator** - `render_panel_calculator()`

### 4. 🔄 Unit Converter
**Category:** Unit Converter  
**Component:** `components/unit_converter_enhanced.py`

**Features:**
- Auto-detection: Tự động phát hiện đơn vị từ input
- Context-aware: Chuyển đổi theo ngữ cảnh
- Hỗ trợ nhiều loại đơn vị y khoa

---

## 📊 DATA STRUCTURE

### Lab Panels Data
**Location:** `labs/normal_ranges.py` (reference ranges)

**Structure:**
- Reference ranges cho từng lab value
- Critical values
- Interpretation guidelines

### Calculator Data
**Location:** Individual calculator files trong `scores/`

**Structure:**
- Input validation
- Calculation logic
- Result display
- References

---

## 🔗 COMPONENTS & DEPENDENCIES

### Main Components Flow

```
pages/05_🔬_Labs_and_Calculators.py
    ↓
Category Selection (radio)
    ↓
Sub-option Selection (selectbox)
    ↓
Route to appropriate render function
    ├── labs/ (lab panels)
    ├── scores/ (calculators)
    └── components/ (unit converter)
```

### Key Dependencies
- **Streamlit:** UI framework
- **labs module:** Lab panels và enhancements
- **scores module:** Calculators (metabolism, nephrology)
- **components:** Unit converter

### External Integrations
- **Scores page:** Linked từ sidebar
- **TDM page:** Linked từ sidebar

---

## 🔄 WORKFLOW & USER JOURNEY

### User Journey 1: Calculator
```
1. User vào Labs & Calculators page
2. Sidebar: Chọn "🧮 Calculators"
3. Selectbox: Chọn calculator (ví dụ: "⚖️ Anion Gap")
4. Main view: Calculator form hiển thị
5. User input: Values
6. Calculate: Results hiển thị
7. Optional: Link to related lab panel
```

### User Journey 2: Lab Panel
```
1. User vào Labs & Calculators page
2. Sidebar: Chọn "🔬 Lab Panels"
3. Selectbox: Chọn panel (ví dụ: "🧪 BMP")
4. Main view: Lab panel hiển thị
   - Reference ranges
   - Input fields
   - Interpretation
5. Quick Actions: Click button để tính calculator liên quan
6. Calculator hiển thị với quick action
```

### User Journey 3: Quick Action
```
1. User đang xem Lab Panel (BMP/CMP)
2. Click Quick Action button (ví dụ: "⚖️ Tính Anion Gap")
3. Sets: st.session_state.quick_action = "anion_gap"
4. Rerun: Page reruns
5. Detects: quick_action trong session_state
6. Renders: Calculator tương ứng
7. Clears: quick_action sau khi render
```

---

## ✨ RECENT CHANGES & IMPROVEMENTS

### 2025-02-18 - Anion Gap Calculator Integration
**Changes:**
- ✅ Xóa option riêng "🧪 Anion Gap Calculator" khỏi radio button
- ✅ Anion Gap Calculator được di chuyển vào trong "🧮 Calculators" category
- ✅ Truy cập: Calculators → Anion Gap

**Files Modified:**
- `pages/05_🔬_Labs_and_Calculators.py` - Updated category options

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Category Structure
- ⚠️ **4 categories chính:** Calculators, Lab Panels, Lab Enhancement, Unit Converter
- ⚠️ Mỗi category có sub-options trong selectbox
- ⚠️ Routing dựa trên string matching (case-insensitive)

### 2. Calculator Routing
- ⚠️ Routing sử dụng string matching trong `calculator_type`
- ⚠️ Phải match chính xác với options trong selectbox
- ⚠️ Case-insensitive matching để tránh Unicode issues

### 3. Lab Panel Quick Actions
- ⚠️ Quick actions set `st.session_state.quick_action`
- ⚠️ Phải clear `quick_action` sau khi render
- ⚠️ Quick actions chỉ hiển thị cho panels phù hợp (BMP/CMP, Thyroid)

### 4. Unit Converter
- ⚠️ Import từ `components.unit_converter_enhanced`
- ⚠️ Có try-except để handle ImportError
- ⚠️ Hiển thị error message nếu không import được

### 5. Show Panel Request
- ⚠️ Handles `st.session_state.show_panel` để show related panel
- ⚠️ Supports: bmp, cmp, thyroid, lipid
- ⚠️ Phải clear sau khi render

### 6. Category Help Text
- ⚠️ Help text trong radio button mô tả từng category
- ⚠️ Updated khi có thay đổi (ví dụ: mention Anion Gap trong Calculators)

### 7. Lab Warning
- ⚠️ Footer có warning về reference ranges
- ⚠️ Important disclaimer về critical values

### 8. Testing
- ⚠️ Test tất cả 4 categories
- ⚠️ Test quick actions
- ⚠️ Test calculator routing
- ⚠️ Test unit converter import

---

## ✅ TESTING CHECKLIST

### Before Making Changes
- [ ] Đọc file này để hiểu cấu trúc
- [ ] Xem Recent Changes để tránh conflicts
- [ ] Review related files trong labs/ và scores/

### After Making Changes
- [ ] Test tất cả 4 categories
- [ ] Test calculator routing
- [ ] Test lab panel quick actions
- [ ] Test unit converter
- [ ] Update Recent Changes section
- [ ] Update version/date

### Full Test Checklist
- [ ] Calculators category hoạt động (10 calculators)
- [ ] Lab Panels category hoạt động (8 panels)
- [ ] Lab Enhancement category hoạt động (2 features)
- [ ] Unit Converter category hoạt động
- [ ] Quick actions hoạt động (BMP/CMP, Thyroid)
- [ ] Calculator routing chính xác
- [ ] Show panel request hoạt động
- [ ] Error handling cho unit converter

---

## 📝 CHANGELOG

### 2025-02-18 - Anion Gap Calculator Integration
- Changed: Xóa option riêng "🧪 Anion Gap Calculator" khỏi radio
- Changed: Anion Gap Calculator truy cập qua Calculators → Anion Gap
- Updated: Help text để mention Anion Gap trong Calculators

---

## 🔗 RELATED DOCUMENTATION

- `docs/PAGE_DRUG_DATABASE.md` - Drug Database documentation
- `docs/README.md` - Documentation index
- `labs/` - Lab panels documentation (nếu có)
- `scores/` - Calculators documentation (nếu có)

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18  
**Next Review:** When making significant changes

---

> **⚠️ REMEMBER:** Cập nhật file này mỗi khi có thay đổi quan trọng để giữ documentation luôn up-to-date!

