# 📋 Diagnosis Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Diagnosis để tránh sai sót.

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **Diagnosis** cung cấp:
- Công cụ hỗ trợ tạo danh sách chẩn đoán phân biệt
- Gợi ý theo triệu chứng và hệ cơ quan
- Liên kết với calculators và phác đồ điều trị

### Main Entry Point
- **File:** `pages/06_🩺_Diagnosis.py`
- **URL Route:** `/pages/06_🩺_Diagnosis.py`
- **Page Title:** "Chẩn đoán phân biệt"

### Related Pages
- `pages/12_📚_In_Depth_Articles.py` - Bài viết chuyên sâu
- `pages/01_📊_Scores.py` - Thang điểm & Scores

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/06_🩺_Diagnosis.py
├── Sidebar:
│   └── Info về module
├── Main content:
│   └── render_ddx_interface() từ diagnosis module
└── Imports từ diagnosis/
```

### Diagnosis Module
```
diagnosis/
└── render_ddx_interface()        # Differential diagnosis interface
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. Differential Diagnosis Generator
**Function:** `render_ddx_interface()`

**Features:**
- Gợi ý danh sách chẩn đoán phân biệt
- Theo triệu chứng và hệ cơ quan
- Liên kết với calculators và protocols

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Disclaimer
- ⚠️ Công cụ chỉ hỗ trợ, **không thay thế đánh giá lâm sàng**
- ⚠️ Footer có disclaimer=True

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18

