# 🔗 AUTO LINK SCORES SCRIPT
## Script tự động phát hiện và gắn liên kết scores

**Ngày:** 2025-02-05

---

## ✅ TÍNH NĂNG

### Auto-detection:
- ✅ Tự động scan tất cả articles trong `content/articles/`
- ✅ Tự động scan tất cả protocols trong `PROTOCOL_ROUTING`
- ✅ Phát hiện scores dựa trên keywords và content
- ✅ Tự động generate mapping file

### Performance:
- ✅ Chạy nhanh (< 5 giây)
- ✅ Không cần streamlit
- ✅ Có thể chạy thường xuyên

---

## 🚀 CÁCH SỬ DỤNG

### Chạy script:
```bash
python scripts/auto_link_scores_to_content.py
```

### Output:
- File: `config/article_protocol_score_mapping.py`
- Format: Python dict với ARTICLE_TO_SCORES và PROTOCOL_TO_SCORES

---

## 📊 KẾT QUẢ

### Lần chạy gần nhất:
- **Articles**: 74 articles có scores
- **Protocols**: 9 protocols có scores
- **Total links**: 301 links

### Coverage:
- Tự động phát hiện scores từ keywords
- Tự động match với SCORES_BY_SPECIALTY
- Tự động generate reason

---

## 🔧 TECHNICAL DETAILS

### Keywords Detection:
- Score keywords mapping trong `SCORE_KEYWORDS`
- Case-insensitive matching
- Multiple keywords per score

### Article Scanning:
- Scan tất cả `.md` files trong `content/articles/`
- Extract content và tìm keywords
- Match với scores

### Protocol Scanning:
- Parse `PROTOCOL_ROUTING` từ file
- Extract keywords và render function
- Match với scores

---

## 📝 LƯU Ý

### Auto-generated:
- File mapping được auto-generate
- **KHÔNG EDIT MANUALLY**
- Chạy script để update

### Updates:
- Chạy sau khi:
  - Thêm articles mới
  - Thêm protocols mới
  - Thêm scores mới
  - Update content

---

## 🔄 WORKFLOW

1. **Thêm content mới** (articles/protocols)
2. **Chạy script**: `python scripts/auto_link_scores_to_content.py`
3. **Review mapping**: Kiểm tra `config/article_protocol_score_mapping.py`
4. **Commit changes**: Commit cả content và mapping

---

*© 2025 - Auto Link Scores Script*

