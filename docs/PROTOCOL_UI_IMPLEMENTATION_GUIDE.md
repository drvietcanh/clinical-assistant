# 🚀 Hướng Dẫn Triển Khai Giao Diện Protocol Mới

## Tổng Quan

Tài liệu này hướng dẫn cách sử dụng các component và CSS mới để cải thiện giao diện trang Protocol.

---

## Bước 1: CSS Đã Được Tích Hợp

File `static/protocol_custom.css` đã được tự động load trong `pages/04_📋_Protocols.py`. Không cần thêm code gì.

**Các style đã có:**
- ✅ Color scheme chuyên nghiệp
- ✅ Typography tối ưu cho đọc
- ✅ Section headers với icons
- ✅ Card layouts
- ✅ Evidence badges
- ✅ Responsive mobile
- ✅ Print-friendly styles

---

## Bước 2: Sử Dụng Components Mới

### 2.1. Section Headers

**Thay vì:**
```python
st.markdown("### 📋 Diagnostic Criteria")
```

**Sử dụng:**
```python
from components.protocol_ui import render_section_header

render_section_header(
    title="Diagnostic Criteria",
    icon="📋",
    level=2,
    description="Tiêu chuẩn chẩn đoán theo guideline"
)
```

**Các level:**
- `level=1`: Header lớn nhất (cho page title)
- `level=2`: Section headers (mặc định)
- `level=3`: Subsection headers

### 2.2. Evidence Badges

**Thêm badge cho guideline:**
```python
from components.protocol_ui import render_evidence_badge

render_evidence_badge(
    level="A",
    source="SSC",
    year=2021,
    guideline="Surviving Sepsis Campaign"
)
```

**Levels:**
- `A`: Strong evidence (màu xanh)
- `B`: Moderate evidence (màu vàng)
- `C`: Weak evidence (màu đỏ)

### 2.3. Protocol Cards

**Wrap content trong card:**
```python
from components.protocol_ui import render_protocol_card

content = """
**Dosing:**
- Drug 1: 10mg/kg IV
- Drug 2: 5mg/kg PO
"""

render_protocol_card(
    content=content,
    card_type="dosing",  # dosing, monitoring, reference, default
    title="Dosing Information"
)
```

**Card types:**
- `default`: Card trắng thông thường
- `dosing`: Card vàng nhạt cho dosing info
- `monitoring`: Card xanh nhạt cho monitoring
- `reference`: Card xanh dương nhạt cho references

### 2.4. Protocol Dividers

**Thay vì:**
```python
st.markdown("---")
```

**Sử dụng:**
```python
from components.protocol_ui import render_protocol_divider

render_protocol_divider()
```

---

## Bước 3: Ví Dụ Protocol Mới

### Ví Dụ: Sepsis Protocol với UI Mới

```python
from components.protocol_ui import (
    render_section_header,
    render_evidence_badge,
    render_protocol_card,
    render_protocol_divider
)

def render():
    """Sepsis Protocol với UI mới"""
    
    # Header với evidence badge
    st.subheader("🦠 Sepsis 1-Hour Bundle")
    render_evidence_badge(
        level="A",
        source="SSC",
        year=2021,
        guideline="Surviving Sepsis Campaign"
    )
    
    render_protocol_divider()
    
    # Diagnostic Criteria Section
    render_section_header(
        title="Diagnostic Criteria",
        icon="🔍",
        level=2,
        description="Tiêu chuẩn chẩn đoán Sepsis"
    )
    
    render_protocol_card(
        content="""
        **Chẩn đoán Sepsis khi có:**
        - Nhiễm trùng (nghi ngờ hoặc xác định)
        - qSOFA ≥2 hoặc SOFA tăng ≥2 điểm
        - Rối loạn chức năng cơ quan
        """,
        card_type="default"
    )
    
    render_protocol_divider()
    
    # Treatment Section
    render_section_header(
        title="1-Hour Bundle",
        icon="⏱️",
        level=2
    )
    
    st.error("""
    **Thực hiện NGAY trong vòng 1 GIỜ:**
    1. ✅ Đo Lactate
    2. ✅ Cấy máu trước khi kháng sinh
    3. ✅ Kháng sinh phổ rộng
    4. ✅ Truyền dịch nhanh
    5. ✅ Vasopressor nếu hạ huyết áp
    """)
    
    render_protocol_divider()
    
    # Dosing Section
    render_section_header(
        title="Antibiotic Selection",
        icon="💊",
        level=2
    )
    
    render_protocol_card(
        content="""
        **Nhiễm trùng cộng đồng:**
        - Ceftriaxone 2g IV q24h
        + Azithromycin 500mg IV q24h
        
        **Nhiễm trùng bệnh viện:**
        - Meropenem 1g IV q8h
        + Vancomycin 15-20mg/kg IV
        """,
        card_type="dosing",
        title="Empiric Antibiotics"
    )
    
    render_protocol_divider()
    
    # Monitoring Section
    render_section_header(
        title="Monitoring",
        icon="📈",
        level=2
    )
    
    render_protocol_card(
        content="""
        **Resuscitation Goals:**
        - MAP ≥65 mmHg
        - Urine output ≥0.5 mL/kg/h
        - Lactate normalization
        
        **Frequency:**
        - Vital signs q15-30min
        - Lactate q2-4h
        """,
        card_type="monitoring"
    )
```

---

## Bước 4: Migration Guide

### Cách Migrate Protocol Cũ

1. **Import components:**
```python
from components.protocol_ui import (
    render_section_header,
    render_evidence_badge,
    render_protocol_card,
    render_protocol_divider
)
```

2. **Thay headers:**
```python
# Cũ
st.markdown("### 📋 Diagnostic Criteria")

# Mới
render_section_header("Diagnostic Criteria", icon="📋")
```

3. **Thay dividers:**
```python
# Cũ
st.markdown("---")

# Mới
render_protocol_divider()
```

4. **Wrap important content:**
```python
# Cũ
st.info("Dosing information...")

# Mới
render_protocol_card(
    content="Dosing information...",
    card_type="dosing"
)
```

5. **Thêm evidence badges:**
```python
# Thêm ở đầu protocol
render_evidence_badge("A", "SSC", 2021)
```

---

## Bước 5: Best Practices

### 5.1. Icon Selection

**Sử dụng icons nhất quán:**
- 📋 Diagnostic Criteria
- 💊 Treatment/Dosing
- 📈 Monitoring
- ⚠️ Warnings
- 🎯 Goals
- 📚 References
- 🔍 Assessment
- ⏱️ Time-sensitive

### 5.2. Card Usage

**Khi nào dùng card:**
- ✅ Dosing information → `card_type="dosing"`
- ✅ Monitoring parameters → `card_type="monitoring"`
- ✅ References → `card_type="reference"`
- ✅ Important notes → `card_type="default"`

**Khi nào không dùng card:**
- ❌ Short inline text
- ❌ Simple lists
- ❌ Already in expander

### 5.3. Section Organization

**Cấu trúc chuẩn:**
1. Protocol title + evidence badge
2. Diagnostic Criteria (level 2)
3. Risk Stratification (level 2)
4. Treatment Algorithm (level 2)
5. Dosing Information (level 2)
6. Monitoring (level 2)
7. Special Populations (level 2)
8. References (level 2)

---

## Bước 6: Testing

### Checklist

- [ ] CSS được load (kiểm tra browser DevTools)
- [ ] Section headers hiển thị đúng
- [ ] Cards có màu nền đúng
- [ ] Evidence badges hiển thị
- [ ] Mobile responsive
- [ ] Print styles hoạt động

### Browser Testing

Test trên:
- ✅ Chrome/Edge (desktop)
- ✅ Firefox (desktop)
- ✅ Safari (desktop)
- ✅ Chrome Mobile
- ✅ Safari Mobile

---

## Troubleshooting

### CSS không load

**Kiểm tra:**
1. File `static/protocol_custom.css` tồn tại
2. Path trong code đúng
3. Streamlit cache cleared (`Ctrl+F5`)

### Components không import được

**Kiểm tra:**
1. File `components/protocol_ui/__init__.py` tồn tại
2. Import path đúng
3. Python path includes project root

### Styles không apply

**Kiểm tra:**
1. CSS selectors đúng
2. Streamlit không override styles
3. Use `unsafe_allow_html=True`

---

## Next Steps

1. **Migrate protocols:** Bắt đầu với protocols quan trọng (Sepsis, Stroke, etc.)
2. **Gather feedback:** Thu thập feedback từ users
3. **Iterate:** Cải thiện dựa trên feedback
4. **Document:** Cập nhật documentation

---

## Resources

- **CSS File:** `static/protocol_custom.css`
- **Components:** `components/protocol_ui/`
- **Documentation:** `docs/PROTOCOL_PAGE_DOCUMENTATION.md`
- **Improvement Plan:** `docs/PROTOCOL_UI_IMPROVEMENT_PLAN.md`

---

*Hướng dẫn này sẽ được cập nhật khi có thêm features mới.*

