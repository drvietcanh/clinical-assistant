# 🏗️ Clinical Assistant - Modular Architecture

## 📂 Cấu Trúc Tổng Thể

```
medical/
├── app.py                          # Main entry point
├── pages/                          # Streamlit pages (routers)
│   ├── 01_📊_Scores.py            # Router cho Scores
│   ├── 02_💊_Antibiotics.py       # Router cho Antibiotics
│   ├── 03_🫁_Ventilator.py        # Router cho Ventilator
│   └── 04_📋_Protocols.py         # Router cho Protocols
│
├── scores/                         # Scores module
│   ├── __init__.py
│   ├── config.py                  # SCORES_BY_SPECIALTY
│   ├── cardiology.py              # 8 calculators tim mạch
│   ├── emergency.py               # 5 calculators cấp cứu
│   ├── respiratory.py             # 5 calculators hô hấp
│   └── neurology.py               # 5 calculators thần kinh
│
├── antibiotics/                    # Antibiotics module
│   ├── __init__.py
│   ├── calculators.py             # CrCl, Vancomycin, Aminoglycoside
│   └── database.py                # Antibiotic lookup
│
├── ventilator/                     # Ventilator module
│   ├── __init__.py
│   ├── calculators.py             # ARDSNet, Initial settings
│   └── tables.py                  # PEEP/FiO2 table
│
└── protocols/                      # Protocols module
    ├── __init__.py
    ├── emergency.py               # Sepsis, Shock
    ├── respiratory.py             # COPD, Asthma
    └── cardiology.py              # ACS, Heart Failure
```

---

## 🎯 Nguyên Tắc Thiết Kế

### 1. **Separation of Concerns**
- Mỗi module xử lý 1 chức năng riêng biệt
- Mỗi calculator là 1 function độc lập
- Router files chỉ làm routing, không chứa logic

### 2. **Modular Structure**
- Easy to find: Mỗi specialty 1 file
- Easy to modify: Sửa 1 calculator không ảnh hưởng các calculator khác
- Easy to test: Test từng function độc lập
- Easy to expand: Thêm calculator = thêm 1 function

### 3. **Consistent Naming**
- Module folders: lowercase (scores, antibiotics, ventilator, protocols)
- Page files: Numbered with emoji (01_📊_Scores.py)
- Function names: render_xxx() format
- Config files: config.py for central configuration

---

## 📊 Module: Scores

### Cấu trúc:
```python
scores/
├── config.py          # SCORES_BY_SPECIALTY dictionary
├── cardiology.py      # Cardiac risk calculators
├── emergency.py       # Emergency & ICU calculators
├── respiratory.py     # Respiratory calculators
└── neurology.py       # Neurological assessment
```

### Pattern:
```python
# Mỗi calculator là 1 function
def render_calculator_name():
    """Calculator description"""
    st.subheader("Title")
    # Implementation
    ...

# Router function
def render_specialty_calculator(calculator_id):
    """Route to correct calculator"""
    calculators = {
        "ID": render_calculator_name,
        ...
    }
    calculators[calculator_id]()
```

### Thêm calculator mới:
1. Thêm function `render_xxx()` vào file specialty tương ứng
2. Thêm vào router dictionary
3. Cập nhật `config.py` để thêm vào menu

---

## 💊 Module: Antibiotics

### Cấu trúc:
```python
antibiotics/
├── calculators.py     # Dosing calculators (CrCl, Vanco, AG)
└── database.py        # Antibiotic database & lookup
```

### Tính năng:
- ✅ CrCl calculator với unit conversion (mg/dL ↔ µmol/L)
- 🚧 Vancomycin dosing & TDM
- 🚧 Aminoglycoside dosing
- 🚧 Antibiotic lookup database

---

## 🫁 Module: Ventilator

### Cấu trúc:
```python
ventilator/
├── calculators.py     # ARDSNet, Initial settings
└── tables.py          # Reference tables (PEEP/FiO2)
```

### Tính năng:
- ✅ ARDSNet tidal volume calculator
- ✅ PEEP/FiO2 table (Lower PEEP strategy)
- 🚧 Initial ventilator settings by pathology

---

## 📋 Module: Protocols

### Cấu trúc:
```python
protocols/
├── emergency.py       # Sepsis, Shock
├── respiratory.py     # COPD, Asthma
└── cardiology.py      # ACS, Heart Failure
```

### Tính năng:
- ✅ Sepsis 1-hour bundle (SSC 2021)
- 🚧 Shock management
- 🚧 COPD exacerbation
- 🚧 Acute asthma
- 🚧 ACS protocol
- 🚧 Acute heart failure

---

## 🔧 Cách Thêm Tính Năng Mới

### Ví dụ: Thêm TIMI Risk Score vào Cardiology

**Bước 1:** Thêm function vào `scores/cardiology.py`
```python
def render_timi_risk():
    """TIMI Risk Score Calculator"""
    st.subheader("💔 TIMI Risk Score")
    # Implementation here
    ...
```

**Bước 2:** Cập nhật router trong cùng file
```python
def render_cardiology_calculator(calculator_id):
    calculators = {
        ...
        "TIMI Risk": render_timi_risk,  # Thêm dòng này
        ...
    }
```

**Bước 3:** Cập nhật status trong `scores/config.py`
```python
"TIMI Risk": {"name": "TIMI Risk Score", "desc": "...", "status": "✅"},
```

**Chỉ 3 bước! Không cần sửa file khác!**

---

## 🧪 Testing Strategy

### Unit Testing (Tương lai)
```python
# tests/scores/test_cardiology.py
def test_cha2ds2vasc():
    # Test individual calculator
    ...

# tests/antibiotics/test_crcl.py
def test_crcl_calculation():
    # Test CrCl calculation
    ...
```

### Manual Testing
- Test từng calculator qua UI
- Verify calculations với reference values
- Check unit conversions

---

## 📈 Metrics

### Current Status (2025-10-29)

**Modules:** 4 modules ✅
- Scores ✅
- Antibiotics ✅
- Ventilator ✅
- Protocols ✅

**Calculators:**
- Total defined: 100+
- Completed (✅): 12
  - qSOFA
  - CHA₂DS₂-VASc
  - HAS-BLED
  - SCORE2
  - SCORE2-OP
  - CURB-65
  - GCS
  - CrCl
  - ARDSNet
  - PEEP/FiO2 Table
  - Sepsis Bundle
- In development (🚧): 8
- Planned (📋): 80+

**Files:**
- Total: 25 files
- Average lines per file: ~200
- Largest file: ~650 lines (cardiology.py)
- Smallest file: ~50 lines (__init__.py)

---

## 🚀 Next Steps

### Priority 1 (Week 1-2)
- [ ] Complete SCORE2/SCORE2-OP with full unit conversion
- [ ] Add HEART Score
- [ ] Add TIMI Risk Score
- [ ] Add Vancomycin dosing
- [ ] Add COPD exacerbation protocol

### Priority 2 (Week 3-4)
- [ ] Add GRACE Score
- [ ] Add Framingham Risk Score
- [ ] Add Aminoglycoside dosing
- [ ] Add GI/Hepatology calculators
- [ ] Add Nephrology calculators

### Priority 3 (Month 2)
- [ ] Add remaining specialties
- [ ] Unit tests for all calculators
- [ ] Antibiotic database
- [ ] More protocols

---

## 💡 Best Practices

### Code Organization
✅ **DO:**
- One calculator per function
- Clear, descriptive function names
- Docstrings for all functions
- Consistent UI patterns
- Unit conversions where needed

❌ **DON'T:**
- Mix multiple calculators in one function
- Duplicate code across calculators
- Hard-code values (use constants)
- Skip input validation

### UI/UX Patterns
✅ **Consistent Layout:**
```python
col1, col2 = st.columns([2, 1])

with col1:
    # Input parameters
    ...
    if st.button("🧮 Calculate"):
        # Calculate
        with col2:
            # Display result
            ...
        
        # Interpretation
        ...
        
        # Recommendations
        ...
        
        with st.expander("📚 References"):
            # Documentation
            ...
```

---

## 🤝 Contributing

### Adding a New Calculator
1. Create function in appropriate module file
2. Add to router dictionary
3. Update config.py status
4. Test thoroughly
5. Add references/documentation
6. Update this ARCHITECTURE.md

### File Naming
- Modules: lowercase, no spaces (scores, antibiotics)
- Pages: Numbered, emoji, title case (01_📊_Scores.py)
- Functions: lowercase, underscore (render_calculator_name)

### Commit Messages
```
feat: Add TIMI Risk Score calculator
fix: Correct CrCl formula for females
refactor: Simplify GCS calculation
docs: Update ARCHITECTURE.md
```

---

## 📚 Documentation

- **ARCHITECTURE.md** (this file): Overall structure
- **README.md**: User-facing documentation
- **QUICKSTART_STREAMLIT.md**: Quick start guide
- Individual module READMEs: Detailed module docs

---

## 🎓 Learning Resources

### Streamlit
- https://docs.streamlit.io
- Multi-page apps: https://docs.streamlit.io/library/get-started/multipage-apps

### Clinical Guidelines
- ESC Guidelines (Cardiology)
- Surviving Sepsis Campaign
- ARDSNet Protocol
- GOLD Guidelines (COPD)
- GINA Guidelines (Asthma)

---

**Last Updated:** 2025-10-29
**Version:** 2.0.0 (Modular Architecture)

