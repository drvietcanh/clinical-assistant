# 📋 Tài Liệu Trang Protocol (Phác Đồ Điều Trị)

## Tổng Quan

Trang Protocol là module chính để hiển thị các phác đồ điều trị lâm sàng theo hướng dẫn quốc tế. Trang này cung cấp giao diện để bác sĩ tra cứu và áp dụng các protocol điều trị chuẩn.

**File chính:** `pages/04_📋_Protocols.py`

---

## Cấu Trúc Hiện Tại

### 1. Kiến Trúc Tổng Quan

```
pages/04_📋_Protocols.py (Main Router)
├── components/protocols_sidebar.py (Sidebar Navigation)
├── components/protocols_article_link.py (Article Links)
├── config/protocol_routing.py (Routing Dictionary)
└── protocols/ (Protocol Implementations)
    ├── emergency/
    ├── cardiology/
    ├── respiratory/
    ├── nephrology/
    └── ... (các chuyên khoa khác)
```

### 2. Luồng Hoạt Động

1. **Khởi tạo trang:** `setup_page()` với mobile optimizations
2. **Render breadcrumbs:** Điều hướng phân cấp
3. **Sidebar:** Chọn chuyên khoa → Chọn protocol
4. **Main content:** Hiển thị protocol được chọn
5. **Deep linking:** Hỗ trợ mở protocol từ Articles page

### 3. Các Component Chính

#### 3.1. Sidebar (`components/protocols_sidebar.py`)

**Chức năng:**
- Hiển thị danh sách chuyên khoa
- Cho phép chọn protocol theo chuyên khoa
- Hỗ trợ deep link từ Articles page
- Liên kết nhanh tới module Hồi sức

**Cấu trúc:**
```python
render_protocols_sidebar() -> (specialty, protocol, use_deep_link)
```

**Tính năng:**
- Selectbox chuyên khoa từ `SPECIALTY_LIST`
- Radio buttons cho danh sách protocol
- Auto-select khi có deep link
- Expander cho liên kết tới ICU Tools

#### 3.2. Protocol Routing (`config/protocol_routing.py`)

**Hệ thống routing dictionary-based:**
- Thay thế if-elif chains dài
- Hỗ trợ priority matching
- Keywords matching linh hoạt
- Exclude keywords cho trường hợp đặc biệt

**Cấu trúc routing:**
```python
PROTOCOL_ROUTING = {
    "protocol_id": {
        "keywords": [list],
        "render": render_function,
        "has_article": bool,
        "article_function": "render_xxx",
        "priority": int,
        "exclude_keywords": [list],
        "require_all": bool
    }
}
```

**Ví dụ:**
```python
"sepsis": {
    "keywords": ["Sepsis"],
    "render": render_sepsis,
    "has_article": True,
    "article_function": "render_sepsis",
    "priority": 8
}
```

#### 3.3. Protocol Template (`protocols/TEMPLATE_PROTOCOL.py`)

**Cấu trúc chuẩn của một protocol:**
1. Header với tên và guideline source
2. Key Points (info box)
3. Diagnostic Criteria
4. Risk Stratification
5. Treatment Algorithm
6. Dosing Information
7. Monitoring
8. Special Populations
9. References

---

## Tính Năng Hiện Tại

### ✅ Đã Có

1. **Navigation:**
   - Sidebar với chuyên khoa và protocol
   - Breadcrumbs
   - Deep linking từ Articles

2. **Content Display:**
   - Info boxes (st.info, st.warning, st.error)
   - Expanders cho nội dung dài
   - Columns layout
   - Tables cho dosing

3. **Integration:**
   - Liên kết tới Articles (bài viết chuyên sâu)
   - Liên kết tới Scores (công cụ tính điểm)
   - Liên kết tới ICU Tools

4. **Mobile Support:**
   - Mobile header
   - Responsive layout
   - Mobile optimizations

### ⚠️ Hạn Chế Hiện Tại

1. **Giao diện:**
   - Chưa có visual hierarchy rõ ràng
   - Màu sắc chưa nhất quán
   - Typography chưa tối ưu cho đọc lâu
   - Thiếu icons/visual cues cho các bước quan trọng

2. **UX:**
   - Sidebar có thể quá dài với nhiều protocol
   - Chưa có search/filter
   - Chưa có quick access cho protocol thường dùng
   - Chưa có progress indicators cho multi-step protocols

3. **Content Organization:**
   - Chưa có tabs cho các section lớn
   - Chưa có sticky headers
   - Chưa có print-friendly view
   - Chưa có download PDF option

---

## Cấu Trúc Dữ Liệu

### Protocol List (`config/protocol_lists.py`)

```python
SPECIALTY_LIST = [
    "Cấp cứu",
    "Hô hấp",
    "Tim mạch",
    # ...
]

def get_protocol_list(specialty: str) -> List[str]:
    # Returns list of protocol names for specialty
```

### Article Mapping (`config/article_protocol_mapping.py`)

```python
def get_article_deep_link(protocol_function: str) -> Tuple[str, str]:
    # Returns (page_path, article_id) if article exists
```

---

## Deep Linking

### Cơ Chế

1. **Từ Articles page:**
   - Set `st.session_state['protocol_specialty']`
   - Set `st.session_state['protocol_to_open']`
   - Set `st.session_state['protocol_function']`

2. **Trên Protocol page:**
   - Check session state
   - Auto-select specialty và protocol
   - Clear state sau khi sử dụng

### Ví Dụ

```python
# Từ Articles page
st.session_state['protocol_specialty'] = "Cấp cứu"
st.session_state['protocol_to_open'] = "Sepsis"
st.session_state['protocol_function'] = "render_sepsis"
st.switch_page("pages/04_📋_Protocols.py")
```

---

## Thống Kê

- **Tổng số protocol:** ~150+ protocols
- **Số chuyên khoa:** 15+ specialties
- **Protocols có article:** ~30+ protocols
- **Protocols có scores:** Nhiều protocols có liên kết tới scoring tools

---

## Best Practices Khi Tạo Protocol Mới

1. **Sử dụng template:** Copy từ `TEMPLATE_PROTOCOL.py`
2. **Follow structure:** Diagnostic → Risk → Treatment → Monitoring
3. **Add references:** Sử dụng `get_references()` và `render_references_section()`
4. **Register routing:** Thêm vào `PROTOCOL_ROUTING` dictionary
5. **Test deep linking:** Đảm bảo hoạt động với Articles

---

## Tích Hợp Với Các Module Khác

### Articles Module
- Deep link từ protocol → article
- Hiển thị link "Đọc thêm kiến thức chuyên sâu"

### Scores Module
- Auto-detect scores trong protocol content
- Render links tới scoring tools

### ICU Tools Module
- Quick link từ sidebar
- Shared protocols (ARDS, Ventilator Weaning, etc.)

### Drug Database
- Protocols có thể reference drugs
- Có thể tích hợp drug lookup trong tương lai

---

## Mobile Considerations

1. **Sidebar:** Collapsible trên mobile
2. **Content:** Responsive columns
3. **Tables:** Horizontal scroll nếu cần
4. **Expanders:** Mặc định collapsed để tiết kiệm space

---

## Tài Liệu Tham Khảo

- Streamlit Documentation: https://docs.streamlit.io
- Surviving Sepsis Campaign Guidelines
- UpToDate Clinical Decision Support
- Evidence-based Medicine Protocols

---

## Lịch Sử Cập Nhật

- **2024:** Initial implementation với routing dictionary
- **2024:** Added deep linking support
- **2024:** Added article integration
- **2024:** Added score links integration

---

## Ghi Chú Kỹ Thuật

### Performance
- Routing dictionary được load một lần
- Protocol functions được import lazy
- Session state được clear sau deep link

### Maintainability
- Dictionary-based routing dễ maintain hơn if-elif chains
- Template protocol đảm bảo consistency
- Modular components dễ test và update

---

*Tài liệu này được tạo để hỗ trợ development và maintenance của Protocol module.*

