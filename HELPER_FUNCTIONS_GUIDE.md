# Helper Functions Guide

## 📋 Tổng Quan

Các helper functions giúp tích hợp các tính năng mới vào pages một cách dễ dàng.

---

## 🎯 1. Calculator Visuals Helper

**File:** `components/calculator_visuals_helper.py`

### `render_score_with_visual()`

Render score với visual chart và interpretation.

**Ví dụ:**
```python
from components.calculator_visuals_helper import render_score_with_visual

# Trong score calculator
result = calculate_score(...)

render_score_with_visual(
    score=result['total_score'],
    score_name="SOFA Score",
    min_score=0,
    max_score=24,
    risk_levels=[
        (0, 6, "Low Risk", "#4caf50"),
        (6, 12, "Moderate Risk", "#ff9800"),
        (12, 24, "High Risk", "#f44336")
    ],
    interpretation="Suy đa cơ quan vừa, cần theo dõi sát"
)
```

### `get_default_risk_levels()`

Lấy default risk levels cho các score types phổ biến.

**Ví dụ:**
```python
from components.calculator_visuals_helper import get_default_risk_levels

risk_levels = get_default_risk_levels("sofa")
# Returns: [(0, 6, "Low Risk", "#4caf50"), ...]
```

### `render_comparison_for_scores()`

Render comparison cho multiple scores.

**Ví dụ:**
```python
from components.calculator_visuals_helper import render_comparison_for_scores

scores = [
    {
        'name': 'SOFA',
        'result': 8,
        'interpretation': 'Moderate severity',
        'risk_level': 'Moderate'
    },
    {
        'name': 'APACHE II',
        'result': 18,
        'interpretation': 'Moderate risk',
        'risk_level': 'Moderate'
    }
]

render_comparison_for_scores(scores, title="So sánh Scores ICU")
```

---

## 🎯 2. Print-Friendly Helper

**File:** `components/print_friendly_helper.py`

### `setup_print_friendly_page()`

Setup print-friendly styles và button cho một page.

**Ví dụ:**
```python
from components.print_friendly_helper import setup_print_friendly_page

# Ở đầu page
setup_print_friendly_page(
    page_title="SOFA Score Calculator",
    show_button=True,
    button_position="top"  # or "bottom"
)
```

### `add_print_metadata()`

Thêm print metadata vào page.

**Ví dụ:**
```python
from components.print_friendly_helper import add_print_metadata

add_print_metadata(
    title="SOFA Score Calculator",
    author="Clinical Assistant",
    description="Sequential Organ Failure Assessment"
)
```

---

## 🎯 3. Evidence Helper

**File:** `utils/evidence_helper.py`

### `quick_evidence_badge()`

Cách nhanh để render evidence badge.

**Ví dụ:**
```python
from utils.evidence_helper import quick_evidence_badge

# Trong protocol
quick_evidence_badge(
    level="A",
    citation="Rhodes A, et al. Surviving Sepsis Campaign 2021...",
    doi="10.1007/s00134-021-06506-y",
    last_reviewed="2024-12-01",
    synopsis="High-quality evidence from systematic review"
)
```

### `evidence_for_recommendation()`

Thêm evidence badge vào recommendation text.

**Ví dụ:**
```python
from utils.evidence_helper import evidence_for_recommendation

recommendation = "Administer antibiotics within 1 hour"
recommendation_with_evidence = evidence_for_recommendation(
    recommendation,
    level="A",
    citation="SSC 2021 Guidelines",
    inline=True
)

st.markdown(recommendation_with_evidence, unsafe_allow_html=True)
```

---

## 📝 Tích Hợp Vào Pages

### Scores Pages

```python
# Thêm vào đầu file
from components.calculator_visuals_helper import render_score_with_visual, get_default_risk_levels
from components.print_friendly_helper import setup_print_friendly_page

# Setup print-friendly
setup_print_friendly_page(show_button=True)

# Trong render function, sau khi calculate
result = calculate_score(...)

# Render với visual
render_score_with_visual(
    score=result['total_score'],
    score_name="Score Name",
    min_score=0,
    max_score=100,
    risk_levels=get_default_risk_levels("score_type"),
    interpretation=result['interpretation']
)
```

### Protocol Pages

```python
# Thêm vào đầu file
from utils.evidence_helper import quick_evidence_badge

# Trong protocol, khi có recommendation
st.markdown("### Recommendation")
st.markdown("Administer antibiotics within 1 hour")
quick_evidence_badge(
    level="A",
    citation="SSC 2021 Guidelines",
    doi="10.1007/s00134-021-06506-y"
)
```

---

## ✅ Lợi Ích

1. **Dễ sử dụng**: Chỉ cần 1-2 dòng code
2. **Consistent**: Tất cả pages sử dụng cùng style
3. **Optional**: Có thể bỏ qua nếu không cần
4. **Backward compatible**: Không ảnh hưởng code cũ

---

*Tài liệu được tạo vào: 2025-01-30*

