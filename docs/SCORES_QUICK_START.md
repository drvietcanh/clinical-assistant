# 🚀 Quick Start Guide - Scores Components

**Ngày:** 2025-02-18  
**Mục đích:** Hướng dẫn nhanh sử dụng các components mới

---

## ⚡ 5 PHÚT BẮT ĐẦU

### 1. Color Coding (1 phút)

```python
from components.risk_color_coding import render_risk_badge

# Xác định risk level
if score <= 2:
    risk_level = 'low'
elif score <= 4:
    risk_level = 'moderate'
else:
    risk_level = 'high'

# Hiển thị
render_risk_badge(risk_level, label=f"Score: {score}", value=score)
```

### 2. Visual Chart (1 phút)

```python
from components.score_charts import render_risk_gauge_chart

render_risk_gauge_chart(
    value=score,
    min_value=0,
    max_value=10,
    title="Risk Score"
)
```

### 3. Export (1 phút)

```python
from components.scores_export import render_export_section

render_export_section(
    calculator_name="My Calculator",
    inputs={'Input 1': value1, 'Input 2': value2},
    results={'Result': result},
    specialty="My Specialty"
)
```

### 4. Related Calculators (Tự động)

Không cần làm gì! Tự động hiển thị sau mỗi calculator.

---

## 📋 TEMPLATE CƠ BẢN

```python
import streamlit as st
from components.risk_color_coding import render_risk_badge
from components.score_charts import render_risk_gauge_chart
from components.scores_export import render_export_section

def render():
    st.subheader("📊 My Calculator")
    
    # Inputs
    value = st.number_input("Enter value", min_value=0, max_value=100)
    
    # Calculate
    score = value * 2  # Your calculation
    
    # Determine risk
    if score < 50:
        risk_level = 'low'
    elif score < 80:
        risk_level = 'moderate'
    else:
        risk_level = 'high'
    
    # Display
    render_risk_badge(risk_level, label=f"Score: {score}")
    render_risk_gauge_chart(value=score, min_value=0, max_value=200)
    
    # Export
    render_export_section(
        calculator_name="My Calculator",
        inputs={'Value': value},
        results={'Score': score},
        specialty="My Specialty"
    )
```

---

## 🎨 COLOR LEVELS

| Level | Color | Use Case |
|-------|-------|----------|
| `very_low` | Green | Score 0-20% |
| `low` | Light Green | Score 21-40% |
| `moderate` | Yellow/Orange | Score 41-60% |
| `high` | Orange | Score 61-80% |
| `very_high` | Red | Score 81-100% |
| `critical` | Dark Red | Emergency |

---

## 📊 CHART TYPES

| Chart | Use Case | Example |
|-------|----------|---------|
| `render_risk_gauge_chart` | Single value với thresholds | Risk score |
| `render_risk_bar_chart` | Horizontal bar với markers | Score comparison |
| `render_risk_stratification_chart` | Risk distribution | Population risk |
| `render_risk_pie_chart` | Risk distribution (percentage) | Risk categories |
| `render_comparison_chart` | Compare multiple values | Multiple scores |
| `render_trend_line_chart` | Trends over time | Score trends |

---

## 💡 TIPS

1. **Color Coding:** Luôn sử dụng `get_risk_level()` để xác định level
2. **Charts:** Chọn chart phù hợp với data type
3. **Export:** Luôn include cả inputs và results
4. **Mobile:** Components tự động responsive

---

## 🔗 LINKS

- [Integration Guide](SCORES_INTEGRATION_GUIDE.md) - Chi tiết
- [Complete Summary](SCORES_COMPLETE_SUMMARY.md) - Tổng kết
- [API Reference](SCORES_IMPROVEMENTS_IMPLEMENTED.md) - API docs

---

**Happy Coding!** 🎉

