# 🛠️ Clinical Assistant Developer Guide

This guide documents the standardized UI/UX components, theming system, and best practices for developing medical calculators in the Clinical Assistant application.

---

## 🎨 Color System

Always use the centralized `COLORS` dictionary from `config.theme`. **Do not use hardcoded hex values.**

### Import
```python
from config.theme import COLORS
```

### Reference
| Key | Color | Usage |
|-----|-------|-------|
| `primary` | 🔵 Blue | Actions, main headers, information |
| `success` | 🟢 Green | Normal results, low risk, safe conditions |
| `warning` | 🟠 Orange | Borderline results, moderate risk, caution needed |
| `error` | 🔴 Red | Abnormal results, high risk, critical warnings |
| `info` | 💠 Light Blue | Neutral information, notes |
| `neutral` | ⚪ Grey | Disabled text, borders, subtle elements |

**Light Variants**: Append `_light` (e.g., `COLORS['success_light']`) for background fills.
**Dark Variants**: Append `_dark` (e.g., `COLORS['primary_dark']`) for text on light backgrounds.

---

## 📊 Score Presentation

Use the standardized components in `components.ui.scoring`.

### Import
```python
from components.ui.scoring import render_score_result, render_score_breakdown, render_recommendation_box
```

### 1. Main Score Result (`render_score_result`)
Displays the primary output of a calculator.

```python
render_score_result(
    title="Score Name",          # e.g., "MELD Score"
    score=15,                    # The calculated value (number or string)
    interpretation="Moderate Risk", # Clinical interpretation
    mortality="19.6%",           # Optional: associated mortality/risk %
    color=COLORS["warning"],     # Theme color based on result
    icon="⚠️",                   # Icon (✅, 🟢, ⚠️, 🔴, 🚨)
    size="large"                 # "small", "medium", "large"
)
```

### 2. Score Breakdown (`render_score_breakdown`)
Displays contributions of individual components to the total score.

```python
render_score_breakdown(
    components=[
        {"name": "Age", "value": "≥ 65", "points": 1},
        {"name": "Confusion", "value": "Yes", "points": 1},
        {"name": "Urea", "value": "> 7 mmol/L", "points": 1},
    ],
    total_score=3,
    max_score=5 # Optional
)
```

### 3. Recommendations (`render_recommendation_box`)
Displays clinical guidance based on the score.

```python
render_recommendation_box(
    title="Management Recommendations",
    content="Consider hospital admission...",
    type="warning", # "success", "info", "warning", "error"
    icon="🏥"
)
```

---

## ✅ Input Validation

Use the validation utilities in `scores.utils.validation` and `components.ui.validation`.

### Import
```python
from scores.utils.validation import validate_age, validate_range, validate_gcs
from components.ui.validation import render_validation_errors
```

### Usage Pattern
```python
# 1. Collect inputs
age = st.number_input("Age", value=0)

# 2. Validate inputs
validation_errors = []

is_valid_age, age_error = validate_age(age, min_val=18, max_val=120)
if not is_valid_age:
    validation_errors.append(age_error)

# 3. Render errors or proceed
if validation_errors:
    render_validation_errors(validation_errors)
else:
    # Calculate score
    pass
```

---

## 📝 Calculator Template

Standard structure for a new calculator file (`scores/specialty/new_score.py`):

```python
import streamlit as st
from config.theme import COLORS
from components.ui.scoring import render_score_result, render_score_breakdown
# Import validation if needed
# from scores.utils.validation import validate_range

def render():
    st.markdown(f"<h3 style='text-align: center; color: {COLORS['success']};'>Title</h3>", unsafe_allow_html=True)
    st.caption("Subtitle / Description")
    
    with st.expander("ℹ️ Info"):
        st.markdown("Details about the score...")
        
    st.divider()
    
    # --- PRO TIP: Use columns for layout ---
    col1, col2 = st.columns(2)
    with col1:
        param1 = st.radio("Parameter 1", ["Option A (0)", "Option B (1)"])
        
    # --- Calculation Logic ---
    if st.button("Calculate"):
        # Calculate score
        score = 0
        # ... logic ...
        
        # Determine styling
        if score < 1:
            color = COLORS["success"]
            icon = "✅"
            interpretation = "Low Risk"
        else:
            color = COLORS["error"]
            icon = "🚨"
            interpretation = "High Risk"
            
        # Display Results
        render_score_result(
            title="Score Name",
            score=score,
            interpretation=interpretation,
            color=color,
            icon=icon
        )
        
        # Optional: Breakdown
        # render_score_breakdown(...)
```
