# 🛠️ Clinical Assistant Developer Guide

This guide documents the standardized UI/UX components, theming system, and best practices for developing medical calculators in the Clinical Assistant application.

---

## 🏗️ Architecture Overview - Scores Module Pattern

The Scores module serves as the **reference architecture** for all domain modules. This pattern should be replicated for Drugs, Critical Care, Diagnosis, and Guidelines.

### Architecture Layers

```
┌─────────────────────────────────────────────────────────────┐
│  UI Layer (Streamlit Pages)                                 │
│  pages/01_📊_Scores.py                                      │
│  - View mode toggle (Classic/Modern)                        │
│  - Tabs (Clinical Scores, Labs & Calculators)               │
│  - Sidebar (filters, search, specialty selection)          │
│  - Session state management                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │ calls
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Domain Router Layer                                         │
│  scores/cardiology/__init__.py                              │
│  scores/emergency/__init__.py                               │
│  ... (one per specialty)                                    │
│  - render_*_calculator(calculator_id) function              │
│  - Routes to individual calculator files                    │
└──────────────────────┬──────────────────────────────────────┘
                       │ uses
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Config Layer                                                │
│  scores/config.py                                            │
│  - SCORES_BY_SPECIALTY dict (registry of all calculators)   │
│  scores/specialty_groups.py                                  │
│  - SPECIALTY_GROUPS (organization for UI)                   │
│  scores/references_config.py                                 │
│  - References for each calculator                           │
└──────────────────────┬──────────────────────────────────────┘
                       │ referenced by
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Calculator Implementation Layer                              │
│  scores/cardiology/score2.py                                │
│  scores/cardiology/score2_op.py                             │
│  ... (one file per calculator)                              │
│  - render() function with full calculator logic             │
│  - Uses components/ui.scoring for display                   │
└──────────────────────┬──────────────────────────────────────┘
                       │ uses
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  UI Components Layer                                         │
│  components/scores_*.py                                      │
│  components/ui/scoring.py                                    │
│  scores/ui_scores_view.py                                    │
│  - Reusable UI components                                    │
│  - Cards, filters, search, favorites                        │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow Example: User selects SCORE2

1. **User Action**: Selects "Tim mạch" → "SCORE2" in sidebar
2. **Page Router** (`pages/01_📊_Scores.py`):
   - Reads `selected_score_id = "SCORE2"` from sidebar
   - Calls `_render_calculator_by_specialty("Tim mạch", "SCORE2")`
3. **Domain Router** (`scores/cardiology/__init__.py`):
   - `render_cardiology_calculator("SCORE2")` looks up in `calculators` dict
   - Calls `render_score2()` from `scores/cardiology/score2.py`
4. **Calculator** (`scores/cardiology/score2.py`):
   - `render()` function collects inputs, validates, calculates
   - Uses `components/ui/scoring.py` to display results
   - Uses `scores/references_config.py` for references

### Key Principles

- **Separation of Concerns**: UI (page) → Routing (domain) → Logic (calculator) → Components (reusable)
- **Config-Driven**: All calculators registered in `scores/config.py`, not hardcoded if/elif chains
- **Single Responsibility**: Each calculator is one file with one `render()` function
- **Reusability**: UI components (`components/scores_*`) shared across all calculators

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

## ➕ Adding a New Calculator - Step-by-Step Checklist

Follow this checklist to add a new calculator to the Scores module:

### Step 1: Register in Config
- [ ] Open `scores/config.py`
- [ ] Find the appropriate specialty section (e.g., `"❤️ Tim mạch (Cardiology)"`)
- [ ] Add entry: `"CALCULATOR_ID": {"name": "Display Name", "desc": "Description", "status": "✅"}`
- [ ] Ensure `CALCULATOR_ID` matches the filename (without `.py`)

### Step 2: Create Calculator File
- [ ] Create file: `scores/<specialty>/<calculator_id>.py`
- [ ] Copy template from below
- [ ] Implement `render()` function with:
  - Input collection (use `st.number_input`, `st.radio`, etc.)
  - Validation (use `scores.utils.validation`)
  - Calculation logic
  - Result display (use `components.ui.scoring`)

### Step 3: Register in Domain Router
- [ ] Open `scores/<specialty>/__init__.py`
- [ ] Add import: `from .<calculator_id> import render as render_<calculator_id>`
- [ ] Add to `calculators` dict: `"CALCULATOR_ID": render_<calculator_id>`
- [ ] Add to `__all__` list if needed

### Step 4: Add References (Optional)
- [ ] Open `scores/references_config.py`
- [ ] Add entry: `"CALCULATOR_ID": [{"title": "...", "authors": "...", "journal": "...", "year": ..., "url": "..."}]`

### Step 5: Test
- [ ] Run `streamlit run pages/01_📊_Scores.py`
- [ ] Navigate to specialty → select calculator
- [ ] Verify inputs, calculation, and display work correctly
- [ ] Check references appear (if added)

### Example: Adding "New Score" to Cardiology

**1. Config** (`scores/config.py`):
```python
"❤️ Tim mạch (Cardiology)": {
    # ... existing entries ...
    "New Score": {"name": "New Score", "desc": "Description here", "status": "✅"},
}
```

**2. File** (`scores/cardiology/new_score.py`):
```python
def render():
    # ... calculator implementation ...
```

**3. Router** (`scores/cardiology/__init__.py`):
```python
from .new_score import render as render_new_score

calculators = {
    # ... existing entries ...
    "New Score": render_new_score,
}
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
