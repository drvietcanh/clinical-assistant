# 📋 Antibiotics Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Antibiotics để tránh sai sót.

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **Antibiotics** là module chuyên sâu về kháng sinh:
- Tra cứu & dữ liệu kháng sinh chi tiết
- So sánh nhiều kháng sinh
- So sánh Side-by-Side
- Phác đồ điều trị

### Main Entry Point
- **File:** `pages/02_💊_Antibiotics.py`
- **URL Route:** `/pages/02_💊_Antibiotics.py`
- **Page Title:** "Kháng sinh (chuyên sâu)"

### Related Pages
- `pages/07_💊_Drug_Database.py` - Cơ sở dữ liệu thuốc (entry chính)
- `pages/08_📊_TDM.py` - TDM kháng sinh

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/02_💊_Antibiotics.py
├── Sidebar:
│   ├── Function type selector (selectbox)
│   └── Info về module
├── Main content:
│   └── Routes to appropriate function
└── Imports từ antibiotics/ module
```

### Antibiotics Module
```
antibiotics/
├── __init__.py                    # Main exports
├── render_antibiotic_lookup()     # Tra cứu
├── render_database()              # Database view
├── render_multi_comparison()      # Multi comparison
├── comparison.py                  # Side-by-side comparison
└── treatment_algorithms.py       # Phác đồ điều trị
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. 🔍 Tra Cứu & Dữ Liệu Kháng Sinh
**Function:** `render_database()`

**Features:**
- Database view của kháng sinh
- Detailed information
- Search và filter

### 2. 🔬 So Sánh Nhiều Kháng Sinh
**Function:** `render_multi_comparison()`

**Features:**
- Compare multiple antibiotics
- Side-by-side comparison
- Key differences

### 3. 📊 So Sánh Side-by-Side
**Function:** `render_comparison()` từ `comparison.py`

**Features:**
- Detailed side-by-side comparison
- Visual comparison table

### 4. 🔄 Phác Đồ Điều Trị
**Function:** `render_algorithms_page()` từ `treatment_algorithms.py`

**Features:**
- Treatment algorithms
- Guidelines-based protocols

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Module Role
- ⚠️ Đây là **module chuyên sâu** về kháng sinh
- ⚠️ Tra cứu & tính liều cơ bản: dùng Drug Database (entry chính)
- ⚠️ TDM kháng sinh: dùng TDM module

### 2. Routing
- ⚠️ String matching (case-insensitive)
- ⚠️ Routes based on function_type

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18

