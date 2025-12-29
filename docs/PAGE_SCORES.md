# 📋 Scores Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Scores để tránh sai sót.

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
Trang **Scores** cung cấp:
- Thang điểm và calculators lâm sàng
- Phân loại theo chuyên khoa (20+ specialties)
- Search functionality
- Daily use indicators

### Main Entry Point
- **File:** `pages/01_📊_Scores.py`
- **URL Route:** `/pages/01_📊_Scores.py`
- **Page Title:** "Calculators & Thang điểm"

### Related Pages
- `pages/05_🔬_Labs_and_Calculators.py` - Labs & Calculators
- `pages/08_📊_TDM.py` - TDM

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/01_📊_Scores.py
├── Sidebar:
│   ├── Specialty selector (selectbox)
│   ├── Search input
│   └── Score list (radio buttons)
├── Main content:
│   └── Routes to appropriate score render function
└── Imports từ scores/ modules
```

### Scores Module Structure
```
scores/
├── config.py                    # SCORES_BY_SPECIALTY dictionary
├── __init__.py                  # Main exports
│
├── cardiology/                  # Cardiology scores
├── emergency/                   # Emergency & Critical Care
├── respiratory/                 # Respiratory
├── neurology/                   # Neurology
├── gi/                          # Gastroenterology
├── metabolism/                  # Metabolism
├── hematology/                  # Hematology
├── nephrology/                  # Nephrology
├── trauma/                      # Trauma
├── psychiatry/                  # Psychiatry
├── oncology/                    # Oncology
├── surgery/                     # Surgery
├── pediatrics/                  # Pediatrics
├── infectious/                  # Infectious Disease
├── ent/                         # ENT
├── obstetrics/                  # Obstetrics
├── dermatology/                 # Dermatology
├── rheumatology/                # Rheumatology
├── ophthalmology/               # Ophthalmology
├── pain/                        # Pain Management
└── nursing/                     # Nursing
```

### Key Files
- `scores/config.py` - SCORES_BY_SPECIALTY dictionary, score metadata
- `scores/__init__.py` - Module exports
- Individual score files trong mỗi specialty folder

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. Specialty Selection
**Component:** Selectbox trong sidebar

**Available Specialties:**
- 20+ specialties từ SCORES_BY_SPECIALTY
- Default: Emergency & Critical Care

### 2. Search Functionality
**Component:** Text input trong sidebar

**Features:**
- Search by score name, abbreviation, description
- Case-insensitive
- Filters scores trong specialty hiện tại
- Shows all nếu không có kết quả

### 3. Score Selection
**Component:** Radio buttons trong sidebar

**Features:**
- Sorted by daily use indicator (⭐)
- Status indicators (✅, ⚠️, etc.)
- Filtered by search query
- Daily use scores shown first

### 4. Score Rendering
**Component:** Dynamic routing to score render functions

**Routing:**
- Uses SCORES_BY_SPECIALTY dictionary
- Routes to appropriate specialty module
- Calls score's render function

---

## 📊 DATA STRUCTURE

### SCORES_BY_SPECIALTY Dictionary
**Location:** `scores/config.py`

**Structure:**
```python
SCORES_BY_SPECIALTY = {
    "Specialty Name": {
        "score_id": {
            "name": "Score Name",
            "desc": "Description (may include 'DÙNG HÀNG NGÀY')",
            "status": "✅" | "⚠️" | "❌",
            "render": render_function
        },
        ...
    },
    ...
}
```

### Score Metadata
- **name:** Display name
- **desc:** Description (may include "DÙNG HÀNG NGÀY" for daily use)
- **status:** Status indicator
- **render:** Render function

---

## 🔗 COMPONENTS & DEPENDENCIES

### Main Components Flow

```
pages/01_📊_Scores.py
    ↓
Specialty Selection
    ↓
Search Filter (optional)
    ↓
Score Selection
    ↓
Route to score render function
    ↓
scores/{specialty}/{score_file}.py
```

### Key Dependencies
- **Streamlit:** UI framework
- **scores.config:** SCORES_BY_SPECIALTY dictionary
- **scores modules:** Individual specialty modules
- **components.mobile_page_wrapper:** Breadcrumbs

---

## 🔄 WORKFLOW & USER JOURNEY

### User Journey 1: Select Score
```
1. User vào Scores page
2. Sidebar: Chọn specialty (ví dụ: Emergency)
3. Search (optional): Gõ "Wells" để filter
4. Radio buttons: Chọn score (ví dụ: "✅ Wells Score ⭐")
5. Main view: Score calculator hiển thị
6. User input: Values
7. Calculate: Results hiển thị
```

### User Journey 2: Daily Use Score
```
1. User vào Scores page
2. Sidebar: Scores với ⭐ hiển thị đầu tiên
3. Select: Daily use score
4. Main view: Calculator hiển thị
```

---

## ✨ RECENT CHANGES & IMPROVEMENTS

### Current Version
- ✅ Organized by specialty
- ✅ Search functionality
- ✅ Daily use indicators
- ✅ Status indicators

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. SCORES_BY_SPECIALTY Dictionary
- ⚠️ **CRITICAL:** Phải update `scores/config.py` khi thêm score mới
- ⚠️ Dictionary structure phải match format
- ⚠️ Render function phải được import và available

### 2. Score Sorting
- ⚠️ Daily use scores (có "DÙNG HÀNG NGÀY" trong desc) được sort lên đầu
- ⚠️ Sorting logic: `(not is_daily_use, name)`
- ⚠️ Daily use indicator: ⭐ hiển thị trong label

### 3. Search Functionality
- ⚠️ Search trong specialty hiện tại
- ⚠️ Case-insensitive matching
- ⚠️ Shows all nếu không có kết quả (tránh widget error)

### 4. Score Rendering
- ⚠️ Routing dựa trên SCORES_BY_SPECIALTY dictionary
- ⚠️ Render function phải exist và callable
- ⚠️ Error handling nếu score không found

### 5. Adding New Score
- ⚠️ Create score file trong appropriate specialty folder
- ⚠️ Add entry vào SCORES_BY_SPECIALTY trong config.py
- ⚠️ Import render function trong specialty __init__.py
- ⚠️ Test score rendering

### 6. Daily Use Indicator
- ⚠️ Add "DÙNG HÀNG NGÀY" vào desc để mark daily use
- ⚠️ ⭐ sẽ tự động hiển thị trong label
- ⚠️ Score sẽ được sort lên đầu

---

## ✅ TESTING CHECKLIST

### Before Making Changes
- [ ] Đọc file này để hiểu cấu trúc
- [ ] Review SCORES_BY_SPECIALTY dictionary
- [ ] Check specialty module structure

### After Making Changes
- [ ] Test specialty selection
- [ ] Test search functionality
- [ ] Test score selection và rendering
- [ ] Test daily use sorting
- [ ] Update Recent Changes section
- [ ] Update version/date

### Full Test Checklist
- [ ] All specialties hiển thị
- [ ] Search hoạt động
- [ ] Score selection hoạt động
- [ ] Score rendering hoạt động
- [ ] Daily use sorting hoạt động
- [ ] Status indicators hiển thị
- [ ] Breadcrumbs hoạt động

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure
- Documented: Current functionality

---

## 🔗 RELATED DOCUMENTATION

- `docs/PAGE_LABS_CALCULATORS.md` - Labs & Calculators documentation
- `docs/README.md` - Documentation index
- `scores/config.py` - Score configuration

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18  
**Next Review:** When making significant changes

---

> **⚠️ REMEMBER:** Cập nhật file này mỗi khi có thay đổi quan trọng để giữ documentation luôn up-to-date!

