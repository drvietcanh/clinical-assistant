# 🚀 Advanced Calculator Features - Hướng Dẫn

**Ngày:** 2025-01-30  
**Version:** 1.0.0  
**Status:** ✅ Hoàn thành

---

## 📋 Tổng Quan

Hệ thống Advanced Calculator Features cung cấp các tính năng nâng cao cho calculators:
- **History:** Lưu và quản lý lịch sử tính toán
- **Batch:** Tính toán cho nhiều patients cùng lúc
- **Compare:** So sánh kết quả before/after
- **Templates:** Lưu và load input presets
- **Undo/Redo:** Hoàn tác/thực hiện lại thay đổi

---

## 🚀 Tính Năng

### 1. **Calculation History** 📜

Lưu và quản lý lịch sử tính toán (last 50).

**Features:**
- Auto-save calculations
- Search và filter
- Export JSON/CSV
- Delete individual hoặc clear all
- View details

**Usage:**
```python
from components.calculation_history import (
    save_calculation_to_history,
    get_calculation_history,
    render_history_ui
)

# Save calculation
save_calculation_to_history(
    calculator_id="egfr",
    calculator_name="eGFR Calculator",
    inputs={"age": 45, "creatinine": 1.2, "sex": "M"},
    results={"egfr": 65.5}
)

# Get history
history = get_calculation_history(calculator_id="egfr", limit=10)

# Render UI
render_history_ui(calculator_id="egfr")
```

**Location:** `components/calculation_history.py`

---

### 2. **Batch Calculator** 📊

Tính toán cho nhiều patients cùng lúc.

**Features:**
- Add/remove patients (max 10)
- Batch input form
- Calculate all button
- Results table
- Export CSV

**Usage:**
```python
from components.batch_calculator import render_batch_calculator

def calculate_egfr(age, creatinine, sex):
    # Your calculation logic
    return {"egfr": 65.5}

input_fields = [
    {'name': 'age', 'label': 'Age', 'type': 'number', 'min': 0, 'max': 120},
    {'name': 'creatinine', 'label': 'Creatinine', 'type': 'number', 'min': 0},
    {'name': 'sex', 'label': 'Sex', 'type': 'select', 'options': ['M', 'F']}
]

render_batch_calculator(
    calculator_function=calculate_egfr,
    input_fields=input_fields,
    calculator_name="eGFR Calculator"
)
```

**Location:** `components/batch_calculator.py`

---

### 3. **Compare Results** 🔀

So sánh kết quả tính toán.

**Features:**
- Side-by-side comparison
- Before/After comparison
- Compare with history
- Differences table
- Visual highlighting

**Usage:**
```python
from components.compare_results import (
    render_compare_results,
    render_compare_from_history,
    render_compare_current_with_history
)

# Compare two results
render_compare_results(
    results_list=[
        {"egfr": 65.5, "stage": "Stage 2"},
        {"egfr": 45.2, "stage": "Stage 3a"}
    ],
    labels=["Before", "After"]
)

# Compare from history
render_compare_from_history(calculator_id="egfr")

# Compare current with history
render_compare_current_with_history(
    current_result={"egfr": 65.5},
    calculator_id="egfr",
    calculator_name="eGFR Calculator"
)
```

**Location:** `components/compare_results.py`

---

### 4. **Templates Manager** 📋

Lưu và load calculation templates (input presets).

**Features:**
- Save templates from current inputs
- Load templates
- Tags và organization
- Export/Import templates
- Search và filter

**Usage:**
```python
from components.calculation_templates import (
    save_template,
    get_templates,
    load_template_inputs,
    render_templates_ui
)

# Save template
save_template(
    calculator_id="egfr",
    template_name="Standard Male",
    inputs={"age": 50, "creatinine": 1.0, "sex": "M"},
    tags=["standard", "male"]
)

# Get templates
templates = get_templates(calculator_id="egfr", tag_filter="standard")

# Load template
inputs = load_template_inputs(calculator_id="egfr", template_id="template_123")

# Render UI
render_templates_ui(calculator_id="egfr", calculator_name="eGFR Calculator")
```

**Location:** `components/calculation_templates.py`

---

### 5. **Undo/Redo System** ↶↷

Hoàn tác/thực hiện lại thay đổi inputs.

**Features:**
- Track input changes
- Undo/Redo buttons
- History view
- Auto-save on change
- Max 20 states

**Usage:**
```python
from components.undo_redo import (
    save_state,
    undo,
    redo,
    render_undo_redo_ui
)

# Save state
save_state(calculator_id="egfr", inputs={"age": 45, "creatinine": 1.2})

# Undo
previous_inputs = undo(calculator_id="egfr")

# Redo
next_inputs = redo(calculator_id="egfr")

# Render UI
def on_undo(inputs):
    # Load inputs into session state
    for key, value in inputs.items():
        st.session_state[f"input_egfr_{key}"] = value

def on_redo(inputs):
    for key, value in inputs.items():
        st.session_state[f"input_egfr_{key}"] = value

render_undo_redo_ui(calculator_id="egfr", on_undo=on_undo, on_redo=on_redo)
```

**Location:** `components/undo_redo.py`

---

## 🔧 Integration

### **Quick Integration với Wrapper Component:**

```python
from components.advanced_calculator_features import render_advanced_features_tabs

# In your calculator page
render_advanced_features_tabs(
    calculator_id="egfr",
    calculator_name="eGFR Calculator",
    calculator_function=calculate_egfr,
    input_fields=input_fields,
    current_inputs=current_inputs,
    current_result=current_result
)
```

### **Quick Actions:**

```python
from components.advanced_calculator_features import render_quick_actions

# Quick action buttons
render_quick_actions(
    calculator_id="egfr",
    calculator_name="eGFR Calculator",
    current_inputs=current_inputs,
    current_result=current_result
)
```

---

## 📁 Cấu Trúc Files

```
components/
├── calculation_history.py      # History manager
├── batch_calculator.py          # Batch calculator
├── compare_results.py            # Compare results
├── calculation_templates.py     # Templates manager
├── undo_redo.py                 # Undo/Redo system
└── advanced_calculator_features.py  # Wrapper component
```

---

## 💾 Data Storage

Tất cả data được lưu trong `st.session_state`:

- `calculation_history`: List of calculations
- `calculation_templates`: Dict by calculator_id
- `undo_redo_{calculator_id}`: Undo/redo state

**Note:** Data chỉ tồn tại trong session. Để persist, cần integrate với database hoặc file storage.

---

## 🎨 UI Examples

### **History Tab:**
- List of calculations với timestamps
- Search và filter
- View details
- Delete và export

### **Batch Tab:**
- Add patients
- Input form cho mỗi patient
- Calculate all button
- Results table

### **Compare Tab:**
- Select calculations from history
- Side-by-side view
- Differences table

### **Templates Tab:**
- Save template from current inputs
- List of templates
- Load template
- Export/Import

### **Undo/Redo Tab:**
- Undo/Redo buttons
- History view
- Current position indicator

---

## ⚠️ Limitations

1. **Session-only:** Data không persist sau khi close browser
2. **Memory:** Large history có thể tốn memory
3. **Performance:** Batch calculator với nhiều patients có thể chậm

---

## 🔮 Future Improvements

### **Priority 1:**
- [ ] Persist data to database/file
- [ ] Cloud sync
- [ ] Share templates
- [ ] Advanced batch operations

### **Priority 2:**
- [ ] Calculation groups
- [ ] Scheduled calculations
- [ ] Calculation alerts
- [ ] Integration với EMR

---

## 📚 References

- [Streamlit Session State](https://docs.streamlit.io/library/advanced-features/session-state)
- [State Management Patterns](https://docs.streamlit.io/library/advanced-features/session-state#advanced-usage)

---

## ✅ Checklist Implementation

- [x] Calculation History Manager
- [x] Batch Calculator
- [x] Compare Results
- [x] Templates Manager
- [x] Undo/Redo System
- [x] Wrapper Component
- [x] Documentation

---

**Last Updated:** 2025-01-30  
**Maintained by:** Clinical IT Team

