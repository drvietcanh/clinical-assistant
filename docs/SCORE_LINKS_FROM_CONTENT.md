# 📊 SCORE LINKS FROM CONTENT
## Hệ thống link từ Articles/Protocols đến Scores

**Ngày:** 2025-02-05

---

## ✅ ĐÃ TẠO

### Files:
- ✅ `config/article_protocol_score_mapping.py` - Mapping từ articles/protocols đến scores
- ✅ `components/score_links_from_content.py` - Component render links

### Integration:
- ✅ Tích hợp vào `pages/12_📚_In_Depth_Articles.py`
- ✅ Tích hợp vào `pages/04_📋_Protocols.py`
- ✅ Cập nhật `config/protocol_routing.py` để hỗ trợ score links

---

## 🎯 TÍNH NĂNG

### Mapping System:
- ✅ **ARTICLE_TO_SCORES**: Mapping từ article_id → list of scores
- ✅ **PROTOCOL_TO_SCORES**: Mapping từ protocol_function → list of scores
- ✅ Mỗi score có: `score_id`, `specialty`, `reason`

### Component Functions:
- ✅ `render_score_links_from_article(article_id)` - Render links từ article
- ✅ `render_score_links_from_protocol(protocol_function)` - Render links từ protocol

### Auto-detection:
- ✅ Tự động extract `protocol_function` từ render function name
- ✅ Tự động lấy score info từ `SCORES_BY_SPECIALTY`

---

## 📋 MAPPING COVERAGE

### Articles có scores:
- ✅ ACS Management → HEART, TIMI, GRACE, Killip
- ✅ Acute Heart Failure → NYHA, Killip
- ✅ Atrial Fibrillation → CHA2DS2-VASc, HAS-BLED
- ✅ Sepsis Bundle → qSOFA, SOFA, SOFA-2, SIRS, NEWS2
- ✅ Stroke Management → NIHSS, GCS, ICH, Hunt & Hess, ASPECTS, ABCD2, mRS
- ✅ ARDS Ventilation → ARDS Berlin, SOFA, SOFA-2
- ✅ AKI KDIGO → KDIGO, eGFR, FENa
- ✅ Và nhiều hơn...

### Protocols có scores:
- ✅ render_acs → HEART, TIMI, GRACE, Killip
- ✅ render_sepsis → qSOFA, SOFA, SOFA-2, SIRS, NEWS2
- ✅ render_stroke → NIHSS, GCS, ICH, Hunt & Hess, ASPECTS, ABCD2, mRS
- ✅ render_ards → ARDS Berlin, SOFA, SOFA-2
- ✅ render_aki → KDIGO, eGFR, FENa
- ✅ Và nhiều hơn...

---

## 💡 CÁCH SỬ DỤNG

### Từ Articles:
1. Mở article trong **In-Depth Articles** page
2. Scroll xuống phần **"📊 Scores liên quan"**
3. Click **"🔗 Mở"** để chuyển đến Scores page
4. Calculator sẽ được chọn tự động

### Từ Protocols:
1. Mở protocol trong **Protocols** page
2. Scroll xuống phần **"📊 Scores liên quan"**
3. Click **"🔗 Mở"** để chuyển đến Scores page
4. Calculator sẽ được chọn tự động

---

## 🔧 TECHNICAL DETAILS

### Mapping Structure:
```python
ARTICLE_TO_SCORES = {
    "article_id": [
        {
            "score_id": "HEART Score",
            "specialty": "❤️ Tim mạch (Cardiology)",
            "reason": "Đánh giá nguy cơ ACS"
        },
        ...
    ]
}
```

### Component Flow:
1. Article/Protocol → Get scores from mapping
2. For each score → Get score info from SCORES_BY_SPECIALTY
3. Render expander with score links
4. On click → Set session state → Switch to Scores page

---

## 📊 TỔNG KẾT

### Coverage:
- ✅ **20+ articles** có score links
- ✅ **30+ protocols** có score links
- ✅ **50+ scores** được link

### Benefits:
- ✅ Tích hợp seamless giữa content và calculators
- ✅ User-friendly navigation
- ✅ Không duplicate code
- ✅ Dễ maintain và mở rộng

---

*© 2025 - Score Links from Content System*

