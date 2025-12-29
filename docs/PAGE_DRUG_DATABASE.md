# 📋 Drug Database Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang thuốc để tránh sai sót.

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
Trang **Drug Database** là entry chính của nhóm **💊 Thuốc & Liều dùng**, cung cấp:
- Tra cứu toàn bộ thuốc (348+ thuốc)
- Tính liều theo chức năng thận (CrCl/eGFR) cho kháng sinh
- So sánh thuốc, lịch trình liều dùng
- Kiểm tra tương tác & tương thích IV

### Main Entry Point
- **File:** `pages/07_💊_Drug_Database.py`
- **URL Route:** `/pages/07_💊_Drug_Database`
- **Page Title:** "Cơ sở dữ liệu thuốc"

### Related Pages
- `pages/Drug_Detail.py` - Trang chi tiết từng thuốc
- `pages/02_💊_Antibiotics.py` - Kháng sinh chuyên sâu
- `pages/08_📊_TDM.py` - Theo dõi nồng độ thuốc

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/07_💊_Drug_Database.py
├── Sidebar menu với 6 công cụ
├── Routing logic
└── Import từ drugs module
```

### Core Module (`drugs/`)
```
drugs/
├── __init__.py                      # Main exports
├── drug_database.py                 # DRUG_DATABASE dictionary (merged từ drug_modules)
├── drug_info.py                     # Wrapper (imports từ drug_info_components)
│
├── drug_info_components/            # Main UI components
│   ├── __init__.py
│   ├── database_view.py            # Main drug database view (render_drug_database)
│   ├── detail_view.py              # Drug detail display (display_drug_info)
│   ├── card_components.py          # Drug card components
│   └── search.py                   # Search functions
│
├── drug_modules/                    # Drug data (organized by category)
│   ├── antimicrobial/              # Antibiotics, antivirals, antifungals
│   ├── cardiovascular/             # Cardiology drugs
│   ├── diabetes/                   # Diabetes medications
│   ├── gastrointestinal/           # GI drugs
│   └── ... (20+ categories)
│
├── interactions.py                  # Drug interaction checker
├── iv_compatibility.py             # IV compatibility checker
├── visual_comparison.py            # Drug comparison tool
├── dosing_schedule.py              # Dosing schedule generator
│
└── drug_utils/                     # Utilities
    ├── constants.py                # Constants
    ├── groups.py                   # Drug groups
    └── tdm_mapping.py              # TDM mapping
```

### Detail Page
```
pages/Drug_Detail.py                 # Dedicated drug detail page
├── Uses: display_drug_info từ detail_view.py
├── Mobile swipe gestures
├── Print functionality
└── Related drugs suggestions
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. 💊 Tra Cứu Thuốc (Tất Cả) - `render_drug_database()`
**File:** `drugs/drug_info_components/database_view.py`

**Features:**
- Search: Tên thuốc, Chỉ định, Tác dụng phụ, Chống chỉ định
- Filters: Nhóm thuốc, Pregnancy category, Black Box Warning, Monitoring Required
- Display: Drug cards với visual indicators
- Navigation: Click card → Navigate to `Drug_Detail.py`

**Components:**
- `search_drugs_with_filters()` - Search logic
- `render_compact_drug_card()` - Card display
- Quick filters UI

### 2. 🧮 Tính Liều Theo eGFR/CrCl (Kháng sinh) - `render_dosing_calculator()`
**File:** `antibiotics/dosing_calculator.py`

**Features:**
- Tính liều dựa trên CrCl/eGFR
- Hỗ trợ: HD, PD, béo phì, trẻ em
- Renal adjustments
- ICU adjustments

### 3. 📊 So Sánh Thuốc Trực Quan - `render_visual_comparison()`
**File:** `drugs/visual_comparison.py`

**Features:**
- So sánh 2-4 thuốc side-by-side
- Visual comparison table
- Key differences highlight

### 4. 📅 Tạo Lịch Trình Liều Dùng - `render_dosing_schedule_generator()`
**File:** `drugs/dosing_schedule.py`

**Features:**
- Tạo lịch trình liều dùng
- Customizable schedule
- Export/Print

### 5. 💉 Kiểm Tra Tương Thích IV - `render_iv_compatibility_checker()`
**File:** `drugs/iv_compatibility.py`

**Features:**
- Check IV compatibility
- Y-site compatibility
- Stability information

### 6. 🔍 Kiểm Tra Tương Tác Thuốc - `render_interaction_checker()`
**File:** `drugs/interactions.py`

**Features:**
- Multi-drug interaction checker
- Visual interaction matrix
- Severity levels (Major, Moderate, Minor)
- Mechanism và recommendations

---

## 📊 DATA STRUCTURE

### DRUG_DATABASE Dictionary
**Location:** `drugs/drug_database.py` (merged từ `drug_modules/`)

**Structure:**
```python
DRUG_DATABASE = {
    "Drug Name": {
        # Basic Info
        "vietnamese_name": str,
        "group": str,
        "class": str,
        
        # Indications & Dosing
        "indications": List[str],
        "dosage": {
            "adult_oral": str,
            "adult_iv": str,
            "pediatric": str,
            ...
        },
        
        # Safety
        "side_effects": Dict[str, List[str]] | List[str],  # Structured hoặc legacy
        "contraindications": Dict | List[str],
        "pregnancy": str,  # A, B, C, D, X
        "black_box_warnings": List[str],
        "requires_monitoring": List[str],
        
        # Adjustments
        "renal_adjustment": Dict[str, str],  # CrCl ranges
        "hepatic_adjustment": Dict[str, str],  # mild, moderate, severe, cirrhosis
        
        # Interactions
        "interactions": List[Dict],
        
        # Enhanced Fields (optional)
        "organ_toxicity": Dict,
        "drug_class_mechanism": str,
        ...
    },
    ...
}
```

### Side Effects Structure (Enhanced)
```python
# New structured format (recommended)
"side_effects": {
    "common": ["effect1", "effect2"],      # ≥1%
    "uncommon": ["effect3"],               # 0.1-1%
    "rare": ["effect4"],                   # <0.1%
    "serious": ["effect5", "effect6"]      # Nghiêm trọng
}

# Legacy format (still supported)
"side_effects": ["effect1", "effect2", ...]
```

### Renal Adjustment Structure
```python
"renal_adjustment": {
    "normal": str,        # CrCl ≥60
    "30_60": str,         # CrCl 30-60
    "15_30": str,         # CrCl 15-30
    "under_30": str,      # CrCl <30
    "under_15": str,      # CrCl <15
    "hemodialysis": str   # HD
}
```

### Hepatic Adjustment Structure
```python
"hepatic_adjustment": {
    "mild": str,          # Suy gan nhẹ
    "moderate": str,      # Suy gan trung bình
    "severe": str,        # Suy gan nặng
    "cirrhosis": str      # Xơ gan
}
```

---

## 🔗 COMPONENTS & DEPENDENCIES

### Main Components Flow

```
pages/07_💊_Drug_Database.py
    ↓
drugs/__init__.py (exports)
    ↓
drugs/drug_info_components/database_view.py
    ├── Uses: search.py (search functions)
    ├── Uses: card_components.py (card display)
    └── Calls: st.switch_page("Drug_Detail.py") on card click
        ↓
    pages/Drug_Detail.py
        ↓
    drugs/drug_info_components/detail_view.py (display_drug_info)
        ├── Uses: card_components.py (quick facts)
        └── Displays: Full drug information in tabs
```

### Key Dependencies
- **Streamlit:** UI framework
- **DRUG_DATABASE:** Main data source
- **Search functions:** `drugs/drug_info_components/search.py`
- **Card components:** `drugs/drug_info_components/card_components.py`
- **Detail view:** `drugs/drug_info_components/detail_view.py`
- **Interaction checker:** `drugs/interactions.py`
- **Antibiotics module:** `antibiotics/` (cho dosing calculator)

### External Integrations
- **Antibiotics module:** `render_dosing_calculator()` từ `antibiotics/`
- **TDM module:** Linked từ sidebar
- **Components:** Mobile navigation, breadcrumbs

---

## 🔄 WORKFLOW & USER JOURNEY

### User Journey 1: Tra Cứu Thuốc
```
1. User vào Drug Database page
2. Sidebar: Chọn "💊 Tra cứu thuốc (Tất cả)"
3. Main view: database_view.py renders
   - Search input với dropdown (Tên/Chỉ định/Tác dụng phụ/Chống chỉ định)
   - Quick filters (Nhóm, Pregnancy, BBW, Monitoring)
   - Drug cards display
4. User click vào một drug card
   → Navigate to Drug_Detail.py
5. Drug_Detail.py displays full information
   - Tabs: Overview, Dosing, Safety, Interactions, etc.
   - Related drugs section
   - Print button
6. User có thể:
   - Navigate back (swipe right trên mobile)
   - Print page
   - Click related drug để xem
```

### User Journey 2: Tính Liều
```
1. User vào Drug Database page
2. Sidebar: Chọn "🧮 Tính liều theo eGFR/CrCl"
3. Render: render_dosing_calculator() từ antibiotics/
4. User input: Patient data, antibiotic selection
5. Calculate: Renal-adjusted dosing
6. Display: Detailed dosing recommendations
```

### User Journey 3: Kiểm Tra Tương Tác
```
1. User vào Drug Database page
2. Sidebar: Chọn "🔍 Kiểm tra tương tác thuốc"
3. Render: render_interaction_checker()
4. User selects: 2-4 drugs
5. Check: Interaction logic
6. Display: Visual interaction matrix với severity levels
```

---

## ✨ RECENT CHANGES & IMPROVEMENTS

### Phase 1: Content & Search (2025-02-18)
**Changes:**
- ✅ Side Effects với frequency data (Common, Uncommon, Rare, Serious)
- ✅ Enhanced Search: 4 loại search (Tên, Chỉ định, Tác dụng phụ, Chống chỉ định)
- ✅ Visual Indicators trong cards (Pregnancy, Black Box, Monitoring, Renal)

**Files Modified:**
- `drugs/drug_info_components/detail_view.py` - Side effects display
- `drugs/drug_info_components/database_view.py` - Enhanced search UI
- `drugs/drug_info_components/card_components.py` - Visual indicators
- `drugs/search.py` - Search by indications, side effects, contraindications

### Phase 2: Print & Mobile (2025-02-18)
**Changes:**
- ✅ Print-friendly CSS format
- ✅ Print Button trong Drug_Detail.py
- ✅ Mobile Swipe Gestures (swipe right → back)

**Files Modified:**
- `static/styles.css` - Print styles
- `pages/Drug_Detail.py` - Print button, swipe gestures
- `static/drug_detail_mobile.css` - Mobile styles

### Phase 3: Advanced Features (2025-02-18)
**Changes:**
- ✅ Enhanced Related Drugs (Same Group + Alternative Drugs)
- ✅ Improved Visual Interaction Matrix (styling, dynamic height, sticky header)
- ✅ Enhanced Dosing Calculator Section (feature cards)
- ✅ Hepatic Adjustment Display (visual cards với color coding)
- ✅ Enhanced Offline Mode (indicators, cache status)

**Files Modified:**
- `pages/Drug_Detail.py` - Related drugs improvements
- `components/drug_interaction_matrix.py` - Enhanced styling
- `drugs/drug_info_components/detail_view.py` - Dosing calculator section, hepatic adjustment
- `components/offline.py` - Enhanced offline indicators
- `static/offline.html` - Drug database offline info

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Data Consistency
- ⚠️ **DRUG_DATABASE** được merge từ nhiều modules trong `drug_modules/`
- ⚠️ Khi thêm/sửa thuốc: Thêm vào đúng file trong `drug_modules/`, không sửa trực tiếp `drug_database.py`
- ⚠️ Đảm bảo backward compatibility: Side effects có thể là Dict (new) hoặc List (legacy)

### 2. Navigation Flow
- ⚠️ **Drug cards** phải navigate đến `Drug_Detail.py`, không hiển thị inline
- ⚠️ Sử dụng `st.switch_page("Drug_Detail.py")` để navigate
- ⚠️ Set `st.session_state['view_drug_name']` trước khi navigate

### 3. Search Implementation
- ⚠️ Search functions trong `drugs/search.py` hỗ trợ 4 loại search
- ⚠️ UI dropdown trong `database_view.py` phải match với search types
- ⚠️ Search phải case-insensitive và hỗ trợ Vietnamese characters

### 4. Visual Indicators
- ⚠️ Cards hiển thị badges: Pregnancy, Black Box, Monitoring, Renal
- ⚠️ Badges chỉ hiển thị khi có data tương ứng
- ⚠️ Color coding phải consistent

### 5. Side Effects Display
- ⚠️ Hỗ trợ cả structured format (Dict) và legacy format (List)
- ⚠️ Categories: Common (≥1%), Uncommon (0.1-1%), Rare (<0.1%), Serious
- ⚠️ Color coding: 🟡 Yellow, 🟠 Orange, ⚪ Gray, 🔴 Red

### 6. Renal & Hepatic Adjustments
- ⚠️ Renal: Display với CrCl ranges và color coding
- ⚠️ Hepatic: Display với severity levels và color coding
- ⚠️ Format phải match với data structure

### 7. Related Drugs
- ⚠️ Same Group: Tìm thuốc cùng `group`
- ⚠️ Alternative Drugs: Tìm thuốc cùng `indications` nhưng khác `group`
- ⚠️ Limit số lượng hiển thị (6 drugs mỗi section)

### 8. Mobile & Print
- ⚠️ Mobile: Swipe gestures chỉ hoạt động trên mobile (<768px)
- ⚠️ Print: CSS ẩn sidebar, buttons, và các elements không cần
- ⚠️ Print button trong Drug_Detail.py

### 9. Offline Mode
- ⚠️ Offline indicator hiển thị khi offline
- ⚠️ Drug database hoạt động với cached data
- ⚠️ Service worker handles caching

### 10. Testing
- ⚠️ Test với cả structured và legacy data formats
- ⚠️ Test navigation flow (card click → detail page)
- ⚠️ Test search với Vietnamese characters
- ⚠️ Test mobile swipe gestures
- ⚠️ Test print layout

---

## ✅ TESTING CHECKLIST

### Before Making Changes
- [ ] Đọc file này để hiểu cấu trúc
- [ ] Xem Recent Changes để tránh conflicts
- [ ] Review related files

### After Making Changes
- [ ] Test functionality đã thay đổi
- [ ] Test backward compatibility (legacy data formats)
- [ ] Test navigation flow
- [ ] Test mobile responsiveness
- [ ] Test print layout (nếu liên quan)
- [ ] Update Recent Changes section trong file này
- [ ] Update version/date ở đầu file

### Full Test Checklist
- [ ] Search hoạt động (4 loại)
- [ ] Filters hoạt động
- [ ] Drug cards hiển thị đúng
- [ ] Visual indicators hiển thị
- [ ] Navigation đến Drug_Detail.py
- [ ] Side effects display (structured & legacy)
- [ ] Renal adjustment display
- [ ] Hepatic adjustment display (nếu có)
- [ ] Related drugs hiển thị
- [ ] Interaction matrix hoạt động
- [ ] Mobile swipe gestures
- [ ] Print layout
- [ ] Offline mode

---

## 📝 CHANGELOG

### 2025-02-18 - Bug Fix
- Fixed: NameError trong Drug_Detail.py - drug_name được sử dụng trước khi định nghĩa
- Fix: Di chuyển việc get drug_name lên trước breadcrumbs

### 2025-02-18 - Phase 1, 2, 3 Improvements
- Added: Side effects frequency data
- Added: Enhanced search (4 types)
- Added: Visual indicators
- Added: Print functionality
- Added: Mobile swipe gestures
- Added: Enhanced related drugs
- Added: Hepatic adjustment display
- Added: Enhanced offline mode

---

## 🔗 RELATED DOCUMENTATION

- `FINAL_SUMMARY.md` - Tổng kết all improvements
- `TEST_GUIDE_ALL_PHASES.md` - Test guide
- `drugs/README_ENHANCED_FIELDS.md` - Enhanced fields documentation
- `drugs/DRUG_EXPANSION_PLAN.md` - Drug expansion plan

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18  
**Next Review:** When making significant changes

---

> **⚠️ REMEMBER:** Cập nhật file này mỗi khi có thay đổi quan trọng để giữ documentation luôn up-to-date!

