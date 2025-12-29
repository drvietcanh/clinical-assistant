# 📋 TDM Page - Documentation Tổng Quát

**Last Updated:** 2025-02-18  
**Status:** ✅ Active  
**Version:** 1.0

> **⚠️ QUAN TRỌNG:** Đọc file này TRƯỚC KHI làm bất kỳ thay đổi nào trong trang TDM để tránh sai sót.

---

## 🎯 TỔNG QUAN

### Mô tả
Trang **TDM** (Therapeutic Drug Monitoring) cung cấp:
- Tính toán và theo dõi nồng độ thuốc
- Organized by category (Aminoglycoside, Glycopeptide, etc.)
- Integration với Drug Database
- Preset drug support

### Main Entry Point
- **File:** `pages/08_📊_TDM.py`
- **URL Route:** `/pages/08_📊_TDM.py`
- **Page Title:** "TDM - Theo dõi nồng độ thuốc"

---

## 📁 CẤU TRÚC FILES

### Main Router
```
pages/08_📊_TDM.py
├── Sidebar:
│   ├── Drug selection (grouped by category)
│   └── Preset drug support
├── Main content:
│   └── Routes to appropriate TDM render function
└── Imports từ drugs.tdm/
```

### TDM Module
```
drugs/tdm/
├── __init__.py                    # Main exports
├── tdm_config.py                  # TDM_DRUGS, categories
├── vancomycin_tdm.py              # Vancomycin TDM
├── aminoglycosides_tdm.py         # Aminoglycosides TDM
├── digoxin.py                     # Digoxin TDM
├── phenytoin_tdm.py               # Phenytoin TDM
├── lithium_tdm.py                 # Lithium TDM
├── theophylline_tdm.py            # Theophylline TDM
├── immunosuppressants.py          # Immunosuppressants TDM
├── carbamazepine_tdm.py           # Carbamazepine TDM
└── valproic_acid_tdm.py           # Valproic Acid TDM
```

---

## 🔧 CÁC CHỨC NĂNG CHÍNH

### 1. Drug Selection
**Component:** Selectbox với category grouping

**Categories:**
- Aminoglycoside (💉)
- Glycopeptide (💊)
- Antiepileptic (🧠)
- Cardiovascular (❤️)
- Respiratory (🫁)
- Psychiatry (💊)

### 2. Preset Drug Support
**Features:**
- Switch từ Drug Database với preset drug
- Session state: `switch_to_tdm`, `preset_tdm_drug`
- Auto-select preset drug

### 3. TDM Calculators
**Available:**
- Vancomycin TDM
- Aminoglycosides TDM
- Digoxin TDM
- Phenytoin TDM
- Lithium TDM
- Theophylline TDM
- Immunosuppressants TDM
- Carbamazepine TDM
- Valproic Acid TDM

---

## ⚠️ LƯU Ý KHI LÀM VIỆC

### 1. Category Grouping
- ⚠️ Drugs grouped by category từ `get_drugs_by_category()`
- ⚠️ Category icons và order defined
- ⚠️ Drug options formatted: "Icon Drug Name"

### 2. Preset Drug
- ⚠️ Check `st.session_state.switch_to_tdm`
- ⚠️ Get `preset_tdm_drug` từ session_state
- ⚠️ Clear preset sau khi sử dụng
- ⚠️ Auto-select preset drug trong selectbox

### 3. TDM Routing
- ⚠️ Routes based on drug name
- ⚠️ Calls appropriate TDM render function
- ⚠️ Error handling nếu drug không found

---

## 📝 CHANGELOG

### 2025-02-18 - Initial Documentation
- Created: Documentation structure

---

**Maintainer:** Development Team  
**Last Reviewed:** 2025-02-18

