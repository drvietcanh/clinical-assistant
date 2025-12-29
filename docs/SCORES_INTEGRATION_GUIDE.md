# 📘 Hướng Dẫn Tích Hợp - Scores Components

**Ngày:** 2025-02-18  
**Mục đích:** Hướng dẫn tích hợp các components mới vào calculators

---

## 📋 MỤC LỤC

1. [Color Coding](#color-coding)
2. [Visual Charts](#visual-charts)
3. [Export/Print](#exportprint)
4. [Related Calculators](#related-calculators)
5. [Ví Dụ Hoàn Chỉnh](#ví-dụ-hoàn-chỉnh)

---

## 🎨 COLOR CODING

### Import
```python
from components.risk_color_coding import (
    render_risk_badge,
    render_risk_bar,
    render_risk_table,
    get_risk_color,
    get_risk_level
)
```

### Sử dụng Risk Badge
```python
# Xác định risk level
risk_level = get_risk_level(
    value=75.5,
    thresholds={
        'very_low_max': 20,
        'low_max': 40,
        'moderate_max': 60,
        'high_max': 80,
        'very_high_max': 100
    }
)

# Render badge
render_risk_badge(
    risk_level=risk_level,
    label='Nguy cơ đột quỵ',
    value=75.5
)
```

### Sử dụng Risk Bar
```python
render_risk_bar(
    value=65,
    max_value=100,
    thresholds={
        'Low': 30,
        'Moderate': 60,
        'High': 80
    },
    label='Risk Score'
)
```

### Sử dụng Risk Table
```python
risk_data = [
    {
        'label': 'Rất thấp',
        'value': '0-20%',
        'risk_level': 'very_low',
        'meaning': 'Nguy cơ thấp, không cần điều trị'
    },
    {
        'label': 'Thấp',
        'value': '21-40%',
        'risk_level': 'low',
        'meaning': 'Nguy cơ thấp, theo dõi'
    },
    {
        'label': 'Trung bình',
        'value': '41-60%',
        'risk_level': 'moderate',
        'meaning': 'Nguy cơ trung bình, cân nhắc điều trị'
    },
    {
        'label': 'Cao',
        'value': '61-80%',
        'risk_level': 'high',
        'meaning': 'Nguy cơ cao, nên điều trị'
    },
    {
        'label': 'Rất cao',
        'value': '81-100%',
        'risk_level': 'very_high',
        'meaning': 'Nguy cơ rất cao, điều trị ngay'
    }
]

render_risk_table(risk_data)
```

---

## 📊 VISUAL CHARTS

### Import
```python
from components.score_charts import (
    render_risk_bar_chart,
    render_risk_stratification_chart,
    render_risk_pie_chart,
    render_comparison_chart,
    render_trend_line_chart,
    render_risk_gauge_chart
)
```

### Sử dụng Risk Bar Chart
```python
render_risk_bar_chart(
    value=65,
    thresholds={'Low': 30, 'Moderate': 60, 'High': 80},
    max_value=100,
    title="CHA2DS2-VASc Score",
    show_value=True
)
```

### Sử dụng Risk Gauge Chart
```python
render_risk_gauge_chart(
    value=75,
    min_value=0,
    max_value=100,
    thresholds={'Low': 30, 'Moderate': 60, 'High': 80},
    title="Risk Level"
)
```

### Sử dụng Risk Stratification Chart
```python
risk_data = [
    {'level': 'very_low', 'value': 15, 'label': 'Rất thấp (0-20%)'},
    {'level': 'low', 'value': 25, 'label': 'Thấp (21-40%)'},
    {'level': 'moderate', 'value': 30, 'label': 'Trung bình (41-60%)'},
    {'level': 'high', 'value': 20, 'label': 'Cao (61-80%)'},
    {'level': 'very_high', 'value': 10, 'label': 'Rất cao (81-100%)'}
]

render_risk_stratification_chart(
    risk_data,
    title="Phân Bố Nguy Cơ",
    x_label="Mức Độ Nguy Cơ",
    y_label="Số Lượng Bệnh Nhân"
)
```

### Sử dụng Comparison Chart
```python
comparison_data = [
    {'label': 'CHA2DS2-VASc', 'value': 4, 'color': '#ef4444'},
    {'label': 'HAS-BLED', 'value': 2, 'color': '#f59e0b'},
    {'label': 'TIMI', 'value': 3, 'color': '#84cc16'}
]

render_comparison_chart(
    comparison_data,
    title="So Sánh Các Score",
    x_label="Score",
    y_label="Giá Trị"
)
```

---

## 📤 EXPORT/PRINT

### Import
```python
from components.scores_export import render_export_section
```

### Sử dụng Export Section
```python
# Sau khi tính toán
inputs = {
    'Tuổi': 75,
    'CHF': 'Có',
    'Tăng huyết áp': 'Có',
    'Đái tháo đường': 'Không',
    'Tiền sử đột quỵ': 'Có',
    'Bệnh mạch máu': 'Có',
    'Giới tính': 'Nữ'
}

results = {
    'CHA2DS2-VASc Score': 6,
    'Nguy cơ đột quỵ/năm': '9.7%',
    'Khuyến nghị': 'Nên dùng kháng đông (Warfarin hoặc DOAC)'
}

render_export_section(
    calculator_name="CHA2DS2-VASc Score",
    inputs=inputs,
    results=results,
    specialty="Tim mạch"
)
```

### Quick Export Button
```python
from components.scores_export import render_quick_export_button

render_quick_export_button(
    calculator_name="CHA2DS2-VASc Score",
    inputs=inputs,
    results=results,
    specialty="Tim mạch"
)
```

---

## 📋 RELATED CALCULATORS

### Tự động hiển thị
Related calculators tự động hiển thị sau mỗi calculator render trong `pages/01_📊_Scores.py`.

### Manual Integration
```python
from components.scores_related import render_related_calculators

# Trong calculator render function
def render():
    # ... calculator code ...
    
    # Hiển thị related calculators
    render_related_calculators(
        current_specialty="Tim mạch",
        current_score_id="CHA2DS2-VASc",
        title="📋 Calculators Liên Quan",
        max_display=5
    )
```

---

## 💡 VÍ DỤ HOÀN CHỈNH

### Example: CHA2DS2-VASc Calculator với tất cả tính năng

```python
"""
CHA2DS2-VASc Score Calculator với đầy đủ tính năng mới
"""

import streamlit as st
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section

def render():
    st.subheader("❤️ CHA₂DS₂-VASc Score")
    st.caption("Đánh giá nguy cơ đột quỵ Trong Rung Nhĩ")
    
    # Inputs
    col1, col2 = st.columns(2)
    
    with col1:
        chf = st.checkbox("C - Suy tim sung huyết")
        htn = st.checkbox("H - Tăng huyết áp")
        age_group = st.radio("A - Tuổi", ["< 65", "65-74", "≥ 75"])
        dm = st.checkbox("D - Đái tháo đường")
    
    with col2:
        stroke = st.checkbox("S - Tiền sử Đột quỵ/TIA")
        vasc = st.checkbox("V - Bệnh mạch máu")
        age_75 = 1 if age_group == "≥ 75" else 0
        age_65_74 = 1 if age_group == "65-74" else 0
        sex = st.radio("Sc - Giới tính", ["Nam", "Nữ"])
    
    # Calculate score
    score = 0
    if chf: score += 1
    if htn: score += 1
    if age_65_74: score += 1
    if age_75: score += 2
    if dm: score += 1
    if stroke: score += 2
    if vasc: score += 1
    if sex == "Nữ": score += 1
    
    # Risk interpretation
    if score == 0:
        risk_level = 'very_low'
        risk_text = "Rất thấp"
        recommendation = "Không cần kháng đông"
    elif score == 1:
        risk_level = 'low'
        risk_text = "Thấp"
        recommendation = "Cân nhắc kháng đông"
    elif score <= 4:
        risk_level = 'moderate'
        risk_text = "Trung bình"
        recommendation = "Nên dùng kháng đông"
    else:
        risk_level = 'high'
        risk_text = "Cao"
        recommendation = "Nên dùng kháng đông (Warfarin hoặc DOAC)"
    
    # Display results
    st.markdown("---")
    st.subheader("📊 Kết Quả")
    
    # Risk badge
    render_risk_badge(
        risk_level=risk_level,
        label=f"CHA2DS2-VASc Score: {score}",
        value=score
    )
    
    st.info(f"**Nguy cơ:** {risk_text} ({score} điểm)")
    st.success(f"**Khuyến nghị:** {recommendation}")
    
    # Visual charts
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        render_risk_bar_chart(
            value=score,
            thresholds={'Low': 1, 'Moderate': 2, 'High': 4},
            max_value=9,
            title="CHA2DS2-VASc Score"
        )
    
    with col_chart2:
        render_risk_gauge_chart(
            value=score,
            min_value=0,
            max_value=9,
            title="Risk Level"
        )
    
    # Export section
    inputs_dict = {
        'CHF': 'Có' if chf else 'Không',
        'Tăng huyết áp': 'Có' if htn else 'Không',
        'Tuổi': age_group,
        'Đái tháo đường': 'Có' if dm else 'Không',
        'Tiền sử đột quỵ/TIA': 'Có' if stroke else 'Không',
        'Bệnh mạch máu': 'Có' if vasc else 'Không',
        'Giới tính': sex
    }
    
    results_dict = {
        'CHA2DS2-VASc Score': score,
        'Nguy cơ': risk_text,
        'Khuyến nghị': recommendation
    }
    
    render_export_section(
        calculator_name="CHA2DS2-VASc Score",
        inputs=inputs_dict,
        results=results_dict,
        specialty="Tim mạch"
    )
```

---

## 🎯 BEST PRACTICES

### 1. Color Coding
- ✅ Sử dụng `get_risk_level()` để xác định risk level
- ✅ Sử dụng `render_risk_badge()` cho quick display
- ✅ Sử dụng `render_risk_bar()` cho progress visualization
- ✅ Sử dụng `render_risk_table()` cho detailed breakdown

### 2. Charts
- ✅ Chọn chart phù hợp với data type
- ✅ Gauge chart cho single value với thresholds
- ✅ Bar chart cho comparisons
- ✅ Pie chart cho distributions
- ✅ Line chart cho trends

### 3. Export
- ✅ Luôn include inputs và results
- ✅ Format rõ ràng, dễ đọc
- ✅ Include timestamp
- ✅ Include calculator name và specialty

### 4. Related Calculators
- ✅ Tự động hiển thị (không cần manual)
- ✅ Có thể customize `max_display` nếu cần

---

## 📝 CHECKLIST TÍCH HỢP

Khi tích hợp vào calculator mới:

- [ ] Import các components cần thiết
- [ ] Xác định risk levels và thresholds
- [ ] Thêm color coding (badge/bar/table)
- [ ] Thêm visual charts (nếu phù hợp)
- [ ] Thêm export section
- [ ] Test với các giá trị khác nhau
- [ ] Test mobile responsive
- [ ] Test dark mode
- [ ] Update documentation

---

## 🔗 RELATED DOCUMENTATION

- `docs/SCORES_COMPLETE_SUMMARY.md` - Tổng kết
- `docs/SCORES_IMPROVEMENTS_IMPLEMENTED.md` - Chi tiết implementation
- `components/risk_color_coding.py` - Color coding API
- `components/score_charts.py` - Charts API
- `components/scores_export.py` - Export API

---

**Maintainer:** Development Team  
**Last Updated:** 2025-02-18

