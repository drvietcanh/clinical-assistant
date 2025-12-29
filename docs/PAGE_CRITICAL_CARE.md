# 📋 Critical Care Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang Critical Care để tránh sai sót.

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **Critical Care** cung cấp:
- Dashboard ICU
- Scoring systems
- Ventilator management
- ARDS/Sepsis protocols
- Shock management
- Fluid therapy
- Vasopressors
- Sedation & Analgesia
- Transfusion
- RRT Calculator
- Clinical scenarios

### Main Entry Point
- **File:** `pages/09_🫁_Critical_Care.py`
- **URL Route:** `/pages/09_🫁_Critical_Care.py`
- **Page Title:** "Hồi sức"

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/09_🫁_Critical_Care.py
├── Sidebar:
│   └── Tool selector (selectbox) - 20+ tools
├── Main content:
│   └── Routes to appropriate function
└── Imports từ critical_care/ và ventilator/
```

### Critical Care Module
```
critical_care/
├── __init__.py                    # Main exports
├── fluid_calculator.py            # Fluid therapy
├── vasopressor_guide.py           # Vasopressors
├── transfusion_calculator.py      # Transfusion
├── sedation_calculator.py         # Sedation
├── scoring_calculator.py          # Scoring systems
├── dashboard.py                   # Dashboard
├── ventilator/                    # Ventilator tools
├── ards_protocols.py              # ARDS
├── sepsis_protocols.py            # Sepsis
├── shock_management.py            # Shock
├── rrt_calculator.py              # RRT
└── scenarios_calculator.py       # Scenarios
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. 🏠 Dashboard
**Function:** `render_critical_care_dashboard()`

### 2. 📊 Scoring Systems
**Function:** `render_scoring_calculator()`

### 3. 🫁 Ventilator Management
**Functions:**
- Basic: `render_ventilator_calculator()`
- Advanced: `render_comprehensive_calculator()` (if available)
- Individual tools: IBW, Tidal Volume, PEEP, Plateau Pressure, Weaning

### 4. 🫁 ARDS Protocols
**Function:** `render_ards_protocols()`

### 5. 🦠 Sepsis Protocols
**Function:** `render_sepsis_protocols()`

### 6. 💉 Shock Management
**Function:** `render_shock_management()`

### 7. 🩺 RRT Calculator
**Function:** `render_rrt_calculator()`

### 8. 🎯 Clinical Scenarios
**Function:** `render_scenarios_calculator()`

### 9. 💧 Fluid Therapy
**Function:** `render_fluid_calculator()`

### 10. 💉 Vasopressors
**Function:** `render_vasopressor_guide()`

### 11. 💤 Sedation & Analgesia
**Function:** `render_sedation_calculator()`

### 12. 🩸 Transfusion
**Function:** `render_transfusion_calculator()`

### 13. 💉 Drug Infusion (DIRC)
**Function:** `render_dirc_calculator()`

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Ventilator Advanced
- ⚠️ Check `VENTILATOR_ADVANCED_AVAILABLE` flag
- ⚠️ Import advanced functions nếu available
- ⚠️ Fallback to basic nếu không available

### 2. Tool Options
- ⚠️ 20+ tool options trong selectbox
- ⚠️ Consistent naming
- ⚠️ Routing based on string matching

### 3. Module Organization
- ⚠️ Critical Care module separate từ Ventilator
- ⚠️ Ventilator có basic và advanced versions
- ⚠️ Individual tools trong ventilator/ folder

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18

