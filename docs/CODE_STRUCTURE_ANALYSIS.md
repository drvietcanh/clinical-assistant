# 🔍 Phân Tích Cấu Trúc Code - Các Điểm Cần Cải Thiện

## 📊 Phân Tích Chi Tiết

### ❌ Vấn Đề 1: Code Duplication - Protocol Selection Pattern

**Vấn đề:**
Mỗi specialty lặp lại pattern giống nhau:
```python
protocol_list = [...]
default_idx = get_default_protocol_index(protocol_list, deep_link_protocol) if use_deep_link else 0
protocol = st.radio("Phác đồ:", protocol_list, index=default_idx, label_visibility="collapsed")
```

**Impact:**
- Code dài và lặp lại
- Khó maintain khi cần thay đổi pattern
- Dễ miss khi thêm specialty mới

**Giải pháp đề xuất:**
Tạo helper function:
```python
def render_protocol_selector(protocol_list: list, deep_link_protocol: str = None, use_deep_link: bool = False):
    default_idx = get_default_protocol_index(protocol_list, deep_link_protocol) if use_deep_link else 0
    return st.radio("Phác đồ:", protocol_list, index=default_idx, label_visibility="collapsed")
```

---

### ❌ Vấn Đề 2: Routing Logic Quá Dài và Lặp Lại

**Vấn đề:**
- 100+ dòng elif statements
- Pattern lặp lại: `elif "X" in protocol or "x" in protocol.lower():`
- Khó maintain và dễ miss cases

**Impact:**
- Code khó đọc
- Performance: Check nhiều điều kiện tuần tự
- Khó thêm protocol mới

**Giải pháp đề xuất:**
Tạo mapping dictionary:
```python
PROTOCOL_ROUTING = {
    "cardiac_arrest": {
        "keywords": ["Cardiac Arrest", "ACLS", "cardiac arrest", "acls"],
        "render": render_cardiac_arrest,
        "has_article": False
    },
    "acs": {
        "keywords": ["ACS"],
        "render": render_acs,
        "has_article": True,
        "article_function": "render_acs"
    },
    # ...
}
```

---

### ❌ Vấn Đề 3: Inconsistent render_article_link Calls

**Vấn đề:**
- Một số protocols có article nhưng chưa gọi `render_article_link`
- Pattern không nhất quán:
  - `render_article_link("render_acs")` → `render_acs()`
  - `render_hf()` (thiếu render_article_link)
  - `render_acute_decompensated_hf()` (thiếu render_article_link)

**Impact:**
- User experience không nhất quán
- Một số protocols không có link về articles

**Giải pháp đề xuất:**
- Tự động gọi `render_article_link` dựa trên mapping
- Hoặc thêm vào routing dictionary

---

### ❌ Vấn Đề 4: Hard-coded Protocol Names

**Vấn đề:**
- Protocol names được hard-code ở nhiều nơi:
  - Trong protocol_list
  - Trong routing logic
  - Trong mapping

**Impact:**
- Khó maintain khi đổi tên
- Dễ inconsistent

**Giải pháp đề xuất:**
- Centralize protocol names trong config
- Use constants hoặc config file

---

### ❌ Vấn Đề 5: Missing Error Handling

**Vấn đề:**
- Routing logic không có error handling
- Nếu protocol không match → không render gì (silent failure)

**Impact:**
- User không biết tại sao không có content
- Debug khó

**Giải pháp đề xuất:**
- Default case với warning message
- Logging cho debugging

---

### ❌ Vấn Đề 6: Performance - Sequential String Matching

**Vấn đề:**
- 100+ string comparisons tuần tự
- Mỗi request phải check tất cả conditions

**Impact:**
- Performance không tối ưu (tuy không nghiêm trọng với số lượng này)

**Giải pháp đề xuất:**
- Use dictionary lookup thay vì sequential if-elif
- Pre-process protocol name để normalize

---

### ❌ Vấn Đề 7: Deep Link State Management

**Vấn đề:**
- State được clear sau khi render, nhưng nếu user refresh → mất deep link
- Không persist deep link info

**Impact:**
- User experience: Refresh page → mất context

**Giải pháp đề xuất:**
- Use query parameters thay vì session_state
- Hoặc persist trong URL

---

## 🎯 Ưu Tiên Cải Thiện

### Priority 1 (High Impact, Low Effort):
1. ✅ **Helper function cho protocol selector** - Giảm duplication
2. ✅ **Consistent render_article_link** - Fix missing links
3. ✅ **Default case với warning** - Better error handling

### Priority 2 (High Impact, Medium Effort):
4. ✅ **Routing dictionary** - Cleaner code, better maintainability
5. ✅ **Centralize protocol names** - Single source of truth

### Priority 3 (Medium Impact, High Effort):
6. ✅ **Query parameters cho deep linking** - Better UX
7. ✅ **Performance optimization** - Dictionary lookup

---

## 📝 Refactoring Plan

### Phase 1: Quick Wins
- [ ] Tạo helper function cho protocol selector
- [ ] Fix missing render_article_link calls
- [ ] Add default case với warning

### Phase 2: Structure Improvement
- [ ] Tạo routing dictionary
- [ ] Refactor routing logic
- [ ] Centralize protocol names

### Phase 3: Advanced
- [ ] Query parameters cho deep linking
- [ ] Performance optimization
- [ ] Better error handling và logging

---

*Phân tích hoàn tất: 2025-02-18*

