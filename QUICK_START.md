# Quick Start Guide

## 🚀 Tích Hợp Nhanh

Hướng dẫn nhanh để tích hợp các tính năng mới vào pages.

---

## 📋 One-Line Integration

### 1. Print Button

```python
from utils.quick_integration import add_print_button

# Thêm vào đầu page
add_print_button(position="top")  # or "bottom"
```

### 2. Evidence Badge

```python
from utils.quick_integration import add_evidence_badge

# Trong protocol
add_evidence_badge(
    level="A",
    citation="Rhodes A, et al. Surviving Sepsis Campaign 2021..."
)
```

### 3. Score Chart

```python
from utils.quick_integration import add_score_chart

# Sau khi tính score
add_score_chart(
    score=result['total_score'],
    score_name="SOFA Score",
    max_score=24
)
```

### 4. Accessibility Toggle

```python
from utils.quick_integration import add_accessibility_toggle

# Trong sidebar
add_accessibility_toggle()
```

### 5. Dashboard Widgets

```python
from utils.quick_integration import add_dashboard_widgets

# Trong page
add_dashboard_widgets()
```

---

## 📝 Ví Dụ Đầy Đủ

### Score Page với Visuals

```python
import streamlit as st
from utils.quick_integration import add_print_button, add_score_chart

# Setup
add_print_button(position="top")

# Calculate score
result = calculate_score(...)

# Display with chart
add_score_chart(
    score=result['total_score'],
    score_name="Score Name",
    max_score=100
)

# Show interpretation
st.info(result['interpretation'])
```

### Protocol Page với Evidence

```python
import streamlit as st
from utils.quick_integration import add_print_button, add_evidence_badge

# Setup
add_print_button()

# Show recommendation
st.markdown("### Recommendation")
st.markdown("Administer antibiotics within 1 hour")

# Add evidence
add_evidence_badge(
    level="A",
    citation="SSC 2021 Guidelines",
    doi="10.1007/s00134-021-06506-y"
)
```

---

## 🎯 Advanced Integration

Xem `HELPER_FUNCTIONS_GUIDE.md` và `INTEGRATION_GUIDE.md` để biết cách tích hợp nâng cao.

---

## ✅ Checklist

- [ ] Import quick_integration
- [ ] Thêm print button (nếu cần)
- [ ] Thêm score chart (nếu là score page)
- [ ] Thêm evidence badge (nếu là protocol)
- [ ] Test và verify

---

*Tài liệu được tạo vào: 2025-01-30*

