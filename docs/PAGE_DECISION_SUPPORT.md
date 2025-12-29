# 📋 Decision Support Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Decision Support để tránh sai sót.

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **Decision Support** cung cấp:
- Flowcharts quyết định lâm sàng
- An toàn thai kỳ & cho con bú
- Tính liều Nhi khoa

### Main Entry Point
- **File:** `pages/10_🧭_Decision_Support.py`
- **URL Route:** `/pages/10_🧭_Decision_Support.py`
- **Page Title:** "Hỗ trợ quyết định"

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/10_🧭_Decision_Support.py
├── Sidebar:
│   └── Feature selector (selectbox) - 3 features
├── Main content:
│   └── Routes to appropriate function
└── Imports từ components/ và scores/
```

### Components
```
components/
├── flowchart.py                   # Flowchart renderer
├── flowcharts/
│   └── clinical_rules.py         # Clinical flowcharts
├── pregnancy_lactation_display.py # Pregnancy & lactation
└── scores.pediatrics.pediatric_dosing.py # Pediatric dosing
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. 🔄 Flowcharts Quyết Định Lâm Sàng
**Function:** `render_flowchart()`

**Available Flowcharts:**
- Wells PE
- PERC
- CHA2DS2-VASc
- Sepsis
- Stroke
- AKI
- CURB-65

### 2. 🤰 Thai Kỳ & Cho Con Bú
**Function:** `render_pregnancy_lactation_section()`

**Features:**
- Safety information
- Drug compatibility
- Recommendations

### 3. 👶 Liều Nhi Khoa
**Function:** `render_pediatric_dosing_calculator()`

**Features:**
- Pediatric dosing calculations
- Age-based adjustments

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Feature Selection
- ⚠️ Uses session_state: `phase2_feature_selector`
- ⚠️ Remembers last selection
- ⚠️ Default: Flowcharts

### 2. Flowchart Creation
- ⚠️ Flowcharts created từ `create_*_flowchart()` functions
- ⚠️ Uses flowchart renderer component

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18

