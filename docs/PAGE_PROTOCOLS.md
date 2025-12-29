# 📋 Protocols Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Protocols để tránh sai sót.

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **Protocols** cung cấp:
- Các phác đồ điều trị chuẩn theo hướng dẫn quốc tế
- Organized by specialty
- Deep linking từ articles
- Score links integration

### Main Entry Point
- **File:** `pages/04_📋_Protocols.py`
- **URL Route:** `/pages/04_📋_Protocols.py`
- **Page Title:** "Phác đồ điều trị"

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/04_📋_Protocols.py
├── Sidebar:
│   └── render_protocols_sidebar() - Specialty & protocol selection
├── Main content:
│   └── render_protocol_by_name() - Dictionary-based routing
└── Components:
    ├── protocols_sidebar.py
    ├── protocols_article_link.py
    └── score_links_from_content.py
```

### Protocols Structure
```
protocols/
├── emergency/                    # Emergency protocols
├── cardiology/                   # Cardiology
├── endocrinology/                # Endocrinology
├── ... (other specialties)
└── config/
    └── protocol_routing.py       # Routing dictionary
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. Protocol Selection
**Component:** `render_protocols_sidebar()`

**Features:**
- Specialty selection
- Protocol selection
- Deep linking support

### 2. Protocol Rendering
**Function:** `render_protocol_by_name()`

**Features:**
- Dictionary-based routing
- Article links integration
- Score links integration

### 3. Deep Linking
**Features:**
- Auto-open protocol từ articles
- Session state management
- Clear state after use

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Protocol Routing
- ⚠️ Uses dictionary-based routing từ `config/protocol_routing.py`
- ⚠️ Protocol name phải match dictionary key
- ⚠️ Error handling nếu protocol không found

### 2. Deep Linking
- ⚠️ Uses session_state: `protocol_specialty`, `protocol_to_open`, `protocol_function`
- ⚠️ Phải clear state sau khi sử dụng
- ⚠️ Prevents re-triggering on refresh

### 3. Adding New Protocol
- ⚠️ Create protocol file trong appropriate specialty folder
- ⚠️ Add entry vào routing dictionary
- ⚠️ Test rendering

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18

