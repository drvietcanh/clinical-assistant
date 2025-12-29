# 📋 Articles Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Articles để tránh sai sót.

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **Articles** cung cấp:
- Bài viết chuyên sâu về các chủ đề lâm sàng
- Auto-discovery từ `content/articles/*.md`
- Deep linking với protocols và scores
- Related calculators integration

### Main Entry Point
- **File:** `pages/12_📚_In_Depth_Articles.py`
- **URL Route:** `/pages/12_📚_In_Depth_Articles.py`
- **Page Title:** "Bài viết chuyên sâu"

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/12_📚_In_Depth_Articles.py
├── Auto-discovery từ content/articles/*.md
├── Article display với markdown rendering
├── Deep linking support
└── Protocol & score links integration
```

### Content Structure
```
content/
└── articles/
    ├── *.md files (auto-discovered)
    └── Metadata trong frontmatter
```

### Config
```
config/
└── article_protocol_mapping.py    # Protocol mapping
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. Article Discovery
**Features:**
- Auto-discovery từ `content/articles/`
- Markdown rendering
- Frontmatter parsing

### 2. Deep Linking
**Features:**
- Link to protocols
- Link to scores/calculators
- Session state management

### 3. Related Content
**Features:**
- Related protocols
- Related calculators
- Related scores

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Article Format
- ⚠️ Markdown files trong `content/articles/`
- ⚠️ Frontmatter cho metadata
- ⚠️ Auto-discovery mechanism

### 2. Protocol Mapping
- ⚠️ Uses `article_protocol_mapping.py`
- ⚠️ Deep linking với protocols page
- ⚠️ Session state: `protocol_specialty`, `protocol_to_open`

### 3. Adding New Article
- ⚠️ Create .md file trong `content/articles/`
- ⚠️ Add frontmatter metadata
- ⚠️ Update protocol mapping nếu cần

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18

