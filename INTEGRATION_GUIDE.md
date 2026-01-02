# Hướng Dẫn Tích Hợp Components Mới

## 📋 Tổng Quan

Tài liệu này hướng dẫn cách tích hợp các components mới đã được tạo vào các pages hiện có.

---

## 🎯 1. EVIDENCE BADGES TRONG PROTOCOLS

### Cách sử dụng:

```python
# Trong protocol file (ví dụ: protocols/emergency/sepsis.py)

from components.evidence_badge import render_evidence_badge
from utils.evidence_levels import create_evidence_metadata

# Tạo evidence metadata
evidence = create_evidence_metadata(
    level="A",
    citation="Rhodes A, et al. Surviving Sepsis Campaign 2021...",
    doi="10.1007/s00134-021-06506-y",
    last_reviewed="2024-12-01"
)

# Render badge
render_evidence_badge(evidence, show_description=True, show_citation=True)
```

### Hoặc sử dụng helper:

```python
from components.protocol_evidence_integration import render_protocol_evidence

# Render evidence cho protocol
render_protocol_evidence("sepsis", "3_hour_bundle")
```

---

## 🎯 2. CDS ALERTS TRONG DRUG DATABASE

### Cách sử dụng:

```python
# Trong pages/07_💊_Drug_Database.py

from components.cds_alerts import (
    check_drug_interactions,
    check_contraindications,
    render_cds_alerts_panel
)

# Check interactions
drugs = ["Warfarin", "Aspirin"]
interaction_alerts = check_drug_interactions(drugs)

# Check contraindications
conditions = ["Pregnancy", "Active bleeding"]
contra_alerts = check_contraindications("Warfarin", conditions)

# Render all alerts
all_alerts = interaction_alerts + contra_alerts
render_cds_alerts_panel(all_alerts)
```

---

## 🎯 3. DRUG PRICING & FORMULARY

### Cách sử dụng:

```python
# Trong drug detail view

from drugs.pricing import get_drug_price, format_price
from drugs.formulary import get_formulary_info, get_formulary_status_badge

# Get pricing
pricing = get_drug_price("Paracetamol")
if pricing:
    st.markdown(f"**Giá:** {format_price(pricing['price_vnd'], show_usd=True)}")

# Get formulary info
formulary = get_formulary_info("Paracetamol")
if formulary:
    st.markdown(get_formulary_status_badge(formulary.status), unsafe_allow_html=True)
```

---

## 🎯 4. CALCULATOR VISUALS

### Cách sử dụng:

```python
# Trong calculator page

from components.calculator_visuals import render_score_chart

# Render risk score chart
render_score_chart(
    score=15,
    min_score=0,
    max_score=30,
    risk_levels=[
        (0, 10, "Low Risk", "#4caf50"),
        (10, 20, "Moderate Risk", "#ff9800"),
        (20, 30, "High Risk", "#f44336")
    ],
    title="Risk Score"
)
```

---

## 🎯 5. CALCULATOR COMPARISON

### Cách sử dụng:

```python
from components.calculator_comparison import render_calculator_comparison

calculators = [
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

render_calculator_comparison(calculators)
```

---

## 🎯 6. DASHBOARD WIDGETS

### Cách sử dụng:

```python
# Trong pages/17_🎯_Unified_Dashboard.py hoặc app.py

from components.dashboard_widgets import render_dashboard_layout

render_dashboard_layout(
    show_quick_access=True,
    show_activity=True,
    show_recommendations=True,
    show_stats=True
)
```

---

## 🎯 7. PDF EXPORT

### Cách sử dụng:

```python
from components.export_pdf import render_pdf_export_button

content = """
<h2>Kết quả tính toán</h2>
<p>Score: 15</p>
<p>Interpretation: Moderate risk</p>
"""

render_pdf_export_button(
    title="Kết quả SOFA Score",
    content=content,
    filename="sofa_result.pdf"
)
```

---

## 🎯 8. PRINT-FRIENDLY

### Cách sử dụng:

```python
from components.print_friendly import render_print_button, inject_print_styles

# Inject print styles (once per page)
inject_print_styles()

# Add print button
render_print_button("🖨️ In trang này")
```

---

## 🎯 9. ACCESSIBILITY

### Cách sử dụng:

```python
from components.accessibility import (
    render_accessibility_toggle,
    render_skip_to_content_link
)

# Add skip link (at top of page)
render_skip_to_content_link()

# Add accessibility toggle (in sidebar or settings)
render_accessibility_toggle()
```

---

## 🎯 10. BREADCRUMBS ENHANCED

### Cách sử dụng:

```python
from components.breadcrumbs_enhanced import render_breadcrumbs_enhanced, get_breadcrumbs_for_module

# Auto-generate breadcrumbs for module
breadcrumbs = get_breadcrumbs_for_module("scores")
render_breadcrumbs_enhanced(breadcrumbs, current_module_id="scores")

# Or manual
render_breadcrumbs_enhanced([
    ("Trang chủ", "/"),
    ("Calculators & Scores", None),
    ("SOFA Score", None)
], current_module_id="scores")
```

---

## 📝 LƯU Ý

1. **Import errors**: Tất cả components đã được test và import thành công
2. **Backward compatibility**: Các components mới không ảnh hưởng đến code cũ
3. **Optional imports**: Sử dụng try/except cho optional components
4. **Session state**: Một số components sử dụng session state, đảm bảo initialize trước

---

## 🚀 NEXT STEPS

1. Tích hợp evidence badges vào một số protocols mẫu
2. Thêm CDS alerts vào drug database page
3. Thêm pricing/formulary vào drug detail view
4. Thêm calculator visuals vào một số scores
5. Test và refine

---

*Tài liệu này được tạo vào: 2025-01-30*

