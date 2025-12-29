# 📋 Vaccination Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Vaccination để tránh sai sót.

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **Vaccination** cung cấp:
- Thông tin toàn diện về tiêm chủng
- Lịch tiêm chủng & phác đồ tiêm
- Giá tham khảo, so sánh giữa các cơ sở
- Vắc xin cho trẻ em và người lớn

### Main Entry Point
- **File:** `pages/11_💉_Vaccination.py`
- **URL Route:** `/pages/11_💉_Vaccination.py`
- **Page Title:** "Tiêm chủng và Vắc xin"

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/11_💉_Vaccination.py
├── Sidebar:
│   └── Function selector (selectbox) - 5 functions
├── Main content:
│   └── Routes to appropriate function
└── Imports từ vaccination/
```

### Vaccination Module
```
vaccination/
├── render_vaccination_home()      # Home page
├── render_vaccine_search()        # Vaccine search
├── render_vaccine_detail()        # Vaccine detail
├── render_schedule_viewer()        # Schedule viewer
├── render_price_comparison()       # Price comparison
└── render_general_info()          # General info
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. 🏠 Trang Chủ
**Function:** `render_vaccination_home()`

### 2. 🔍 Tra Cứu Vắc Xin
**Function:** `render_vaccine_search()`

### 3. 📅 Lịch Tiêm Chủng
**Function:** `render_schedule_viewer()`

### 4. 💰 Giá Cả Vắc Xin
**Function:** `render_price_comparison()`

### 5. 📚 Thông Tin Chung
**Function:** `render_general_info()`

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Function Selection
- ⚠️ Uses session_state: `vaccination_function_selector`
- ⚠️ 5 function options

### 2. Vaccine Classification
- ⚠️ TCMR (bắt buộc)
- ⚠️ TCMR mở rộng
- ⚠️ Dịch vụ

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18

