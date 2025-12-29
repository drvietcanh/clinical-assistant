# 📝 Integration Examples - Scores Components

**Ngày:** 2025-02-18  
**Mục đích:** Ví dụ tích hợp components vào calculators

---

## ✅ CALCULATORS ĐÃ TÍCH HỢP (4 calculators)

### 1. CHA2DS2-VASc Score ✅
**File:** `scores/cardiology/cha2ds2vasc.py`

**Components đã tích hợp:**
- ✅ Color Coding (risk badges)
- ✅ Visual Charts (gauge, bar chart)
- ✅ Export (scores_export component)

**Features:**
- Risk level color coding (very_low, low, moderate, high, very_high)
- Gauge chart hiển thị score
- Bar chart với thresholds
- Export to TXT, CSV, Print

---

### 2. qSOFA Score ✅
**File:** `scores/emergency/qsofa.py`

**Components đã tích hợp:**
- ✅ Color Coding (risk badges)
- ✅ Visual Charts (gauge, bar chart)
- ✅ Export (scores_export component)

**Features:**
- Risk level color coding (low, moderate, very_high)
- Gauge chart hiển thị score
- Bar chart với thresholds
- Export to TXT, CSV, Print

---

## 📋 CODE EXAMPLES

### Example 1: CHA2DS2-VASc Integration

```python
# Import new components
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section as render_scores_export

# Determine risk level
if score == 0:
    risk_level = 'very_low'
elif score == 1:
    risk_level = 'low'
elif score == 2:
    risk_level = 'moderate'
elif score <= 4:
    risk_level = 'high'
else:
    risk_level = 'very_high'

# Display with color coding
render_risk_badge(
    risk_level=risk_level,
    label=f"Nguy cơ: {risk_text}",
    value=score
)

# Visual charts
col_chart1, col_chart2 = st.columns(2)
with col_chart1:
    render_risk_gauge_chart(
        value=score,
        min_value=0,
        max_value=9,
        thresholds={'Low': 1, 'Moderate': 2, 'High': 4},
        title="CHA₂DS₂-VASc Score"
    )
with col_chart2:
    render_risk_bar_chart(
        value=score,
        thresholds={'Low': 1, 'Moderate': 2, 'High': 4},
        max_value=9,
        title="Risk Level"
    )

# Export
render_scores_export(
    calculator_name="CHA₂DS₂-VASc Score",
    inputs=inputs_dict,
    results=results_dict,
    specialty="Tim mạch"
)
```

### Example 2: qSOFA Integration

```python
# Determine risk level
if score >= 2:
    risk_level_code = "very_high"
elif score == 1:
    risk_level_code = "moderate"
else:
    risk_level_code = "low"

# Display badge
render_risk_badge(
    risk_level=risk_level_code,
    label=risk_level,
    value=score
)

# Charts
render_risk_gauge_chart(
    value=score,
    min_value=0,
    max_value=3,
    thresholds={'Low': 0, 'Moderate': 1, 'High': 2},
    title="qSOFA Score"
)
```

---

## 🎯 INTEGRATION CHECKLIST

Khi tích hợp vào calculator mới:

### Color Coding
- [ ] Import `render_risk_badge` hoặc `get_risk_level`
- [ ] Xác định risk level từ score
- [ ] Render risk badge
- [ ] Test với các score khác nhau

### Visual Charts
- [ ] Import chart functions
- [ ] Chọn chart phù hợp (gauge/bar/pie)
- [ ] Set thresholds đúng
- [ ] Test responsive

### Export
- [ ] Import `render_scores_export`
- [ ] Prepare inputs dict
- [ ] Prepare results dict
- [ ] Call render_scores_export
- [ ] Test export formats

---

## 📊 RISK LEVEL MAPPING

### Common Risk Levels
- **very_low** (Green): Score 0-20% range
- **low** (Light Green): Score 21-40% range
- **moderate** (Yellow/Orange): Score 41-60% range
- **high** (Orange): Score 61-80% range
- **very_high** (Red): Score 81-100% range
- **critical** (Dark Red): Emergency cases

### Calculator-Specific Mappings

#### CHA2DS2-VASc (0-9 scale)
- 0: very_low
- 1: low
- 2: moderate
- 3-4: high
- 5-9: very_high

#### qSOFA (0-3 scale)
- 0: low
- 1: moderate
- 2-3: very_high

---

## 🔧 TROUBLESHOOTING

### Issue: Risk badge không hiển thị
**Solution:** Kiểm tra risk_level có đúng format không (very_low, low, moderate, high, very_high, critical)

### Issue: Charts không render
**Solution:** 
- Kiểm tra plotly đã install
- Kiểm tra value trong range min-max
- Kiểm tra thresholds format

### Issue: Export không hoạt động
**Solution:**
- Kiểm tra inputs và results là dict
- Kiểm tra calculator_name và specialty đã set
- Kiểm tra import đúng

---

## 📝 NEXT CALCULATORS TO INTEGRATE

### Priority High
1. ⏳ Wells DVT Score
2. ⏳ HAS-BLED Score
3. ⏳ SOFA Score
4. ⏳ APACHE II/III/IV
5. ⏳ GCS Score

### Priority Medium
6. ⏳ TIMI Risk Score
7. ⏳ GRACE Score
8. ⏳ CURB-65 Score
9. ⏳ NEWS2 Score
10. ⏳ MEWS Score

---

## 🔗 RELATED DOCUMENTATION

- [Integration Guide](SCORES_INTEGRATION_GUIDE.md) - Chi tiết
- [Quick Start](SCORES_QUICK_START.md) - Quick start
- [Testing Guide](SCORES_TESTING_GUIDE.md) - Testing

---

**Maintainer:** Development Team  
**Last Updated:** 2025-02-18

