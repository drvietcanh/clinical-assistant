# 📐 Module Formatters - Hướng Dẫn Sử Dụng

**File:** `utils/formatters.py`  
**Mục đích:** Chuẩn hóa format các giá trị lâm sàng (tuổi, cân nặng, chiều cao, lab values, etc.)

---

## 🎯 Tổng Quan

Module này cung cấp các hàm để:
1. **Format giá trị** khi hiển thị (không có số thập phân thừa)
2. **Render input fields** với format chuẩn tự động

---

## 📋 Các Hàm Format

### **1. format_age(age)**
Format tuổi - **số nguyên** (không có số thập phân)

```python
from utils.formatters import format_age

age = 65.5
formatted = format_age(age)  # "65" (không phải "65.0")
```

### **2. format_weight(weight, decimals=1)**
Format cân nặng - **1 số thập phân** (nhưng nếu là số nguyên thì không hiển thị .0)

```python
from utils.formatters import format_weight

weight1 = 70.0
formatted1 = format_weight(weight1)  # "70" (không phải "70.0")

weight2 = 70.5
formatted2 = format_weight(weight2)  # "70.5"

weight3 = 70.25
formatted3 = format_weight(weight3, decimals=2)  # "70.25"
```

### **3. format_height(height)**
Format chiều cao - **số nguyên**

```python
from utils.formatters import format_height

height = 170.5
formatted = format_height(height)  # "170"
```

### **4. format_lab_value(value, decimals=1)**
Format giá trị lab - **1-2 số thập phân**

```python
from utils.formatters import format_lab_value

creatinine = 100.5
formatted = format_lab_value(creatinine)  # "100.5"

glucose = 100.25
formatted = format_lab_value(glucose, decimals=2)  # "100.25"
```

### **5. format_percentage(value, decimals=1)**
Format phần trăm

```python
from utils.formatters import format_percentage

percent = 95.5
formatted = format_percentage(percent)  # "95.5%"
```

### **6. format_dose(value, decimals=1)**
Format liều thuốc

```python
from utils.formatters import format_dose

dose1 = 1000.0
formatted1 = format_dose(dose1)  # "1000"

dose2 = 1000.5
formatted2 = format_dose(dose2)  # "1000.5"
```

---

## 🖥️ Các Hàm Render Input (Streamlit)

### **1. render_age_input()**
Render input cho tuổi - tự động format số nguyên

```python
from utils.formatters import render_age_input

age = render_age_input(
    label="Tuổi (năm)",
    min_value=18,
    max_value=120,
    value=50,
    key="patient_age"
)
# Tự động format: chỉ số nguyên, không có .0
```

### **2. render_weight_input()**
Render input cho cân nặng - format 1 số thập phân

```python
from utils.formatters import render_weight_input

weight = render_weight_input(
    label="Cân nặng (kg)",
    min_value=10.0,
    max_value=200.0,
    value=70.0,
    decimals=1,  # 1 số thập phân
    key="patient_weight"
)
```

### **3. render_height_input()**
Render input cho chiều cao - format số nguyên

```python
from utils.formatters import render_height_input

height = render_height_input(
    label="Chiều cao (cm)",
    min_value=100,
    max_value=220,
    value=170,
    key="patient_height"
)
```

### **4. render_lab_value_input()**
Render input cho giá trị lab - format với số thập phân

```python
from utils.formatters import render_lab_value_input

creatinine = render_lab_value_input(
    label="Creatinine (µmol/L)",
    min_value=10.0,
    max_value=2000.0,
    value=100.0,
    decimals=1,  # 1 số thập phân
    key="creatinine"
)

# Hoặc cho Hemoglobin (1 số thập phân)
hgb = render_lab_value_input(
    label="Hemoglobin (g/dL)",
    min_value=1.0,
    max_value=25.0,
    value=7.0,
    decimals=1,
    key="hemoglobin"
)
```

---

## 📝 Ví Dụ Sử Dụng

### **Ví dụ 1: Calculator với format chuẩn**

```python
import streamlit as st
from utils.formatters import (
    render_age_input,
    render_weight_input,
    render_height_input,
    format_weight,
    format_height
)

def render_calculator():
    st.header("BMI Calculator")
    
    # Sử dụng render functions (tự động format)
    age = render_age_input("Tuổi", min_value=18, max_value=120, value=50)
    weight = render_weight_input("Cân nặng (kg)", min_value=10.0, max_value=200.0)
    height = render_height_input("Chiều cao (cm)", min_value=100, max_value=220)
    
    # Tính toán
    bmi = weight / ((height / 100) ** 2)
    
    # Hiển thị kết quả với format chuẩn
    st.metric("BMI", f"{bmi:.1f}")
    st.caption(f"Cân nặng: {format_weight(weight)} kg")
    st.caption(f"Chiều cao: {format_height(height)} cm")
```

### **Ví dụ 2: Sửa format hiện có**

**Trước (có 2 số thập phân):**
```python
current_hgb = st.number_input(
    "Hemoglobin hiện tại (g/dL)",
    min_value=1.0,
    max_value=25.0,
    value=7.0,
    step=0.1,
    key="hgb_current"
)
# Hiển thị: 7.20 (2 số thập phân)
```

**Sau (chỉ 1 số thập phân):**
```python
# Cách 1: Thêm format parameter
current_hgb = st.number_input(
    "Hemoglobin hiện tại (g/dL)",
    min_value=1.0,
    max_value=25.0,
    value=7.0,
    step=0.1,
    format="%.1f",  # Chỉ 1 số thập phân
    key="hgb_current"
)
# Hiển thị: 7.2 (1 số thập phân)

# Cách 2: Sử dụng render_lab_value_input (khuyến nghị)
from utils.formatters import render_lab_value_input

current_hgb = render_lab_value_input(
    "Hemoglobin hiện tại (g/dL)",
    min_value=1.0,
    max_value=25.0,
    value=7.0,
    decimals=1,
    key="hgb_current"
)
```

### **Ví dụ 3: Format khi hiển thị kết quả**

```python
from utils.formatters import format_weight, format_lab_value, format_age

# Trong kết quả
st.write(f"Tuổi: {format_age(age)}")  # "65" không phải "65.0"
st.write(f"Cân nặng: {format_weight(weight)} kg")  # "70" hoặc "70.5"
st.write(f"Creatinine: {format_lab_value(creatinine)} µmol/L")  # "100.5"
```

---

## 🎨 Quy Tắc Format Chuẩn

| Loại Giá Trị | Format | Ví Dụ |
|-------------|--------|-------|
| **Tuổi** | Số nguyên | `65` (không phải `65.0`) |
| **Cân nặng** | 1 số thập phân (nếu cần) | `70` hoặc `70.5` |
| **Chiều cao** | Số nguyên | `170` (không phải `170.0`) |
| **Lab values** | 1-2 số thập phân | `100.5` hoặc `100.25` |
| **Hemoglobin** | 1 số thập phân | `7.2` (không phải `7.20`) |
| **Liều thuốc** | 1 số thập phân (nếu cần) | `1000` hoặc `1000.5` |
| **Phần trăm** | 1 số thập phân | `95.5%` |

---

## ✅ Checklist Khi Sử Dụng

- [ ] Tuổi: Dùng `render_age_input()` hoặc `format="%d"`
- [ ] Cân nặng: Dùng `render_weight_input()` hoặc `format="%.1f"`
- [ ] Chiều cao: Dùng `render_height_input()` hoặc `format="%d"`
- [ ] Lab values: Dùng `render_lab_value_input()` với `decimals=1` hoặc `decimals=2`
- [ ] Hemoglobin: **1 số thập phân** (`format="%.1f"`)
- [ ] Khi hiển thị: Dùng các hàm `format_*()` để loại bỏ số 0 thừa

---

## 🔧 Migration Guide

### **Tìm và thay thế các pattern cũ:**

1. **Tuổi:**
```python
# Trước
age = st.number_input("Tuổi", value=50.0, step=1.0)

# Sau
from utils.formatters import render_age_input
age = render_age_input("Tuổi", value=50)
```

2. **Cân nặng:**
```python
# Trước
weight = st.number_input("Cân nặng (kg)", value=70.0, step=1.0)

# Sau
from utils.formatters import render_weight_input
weight = render_weight_input("Cân nặng (kg)", value=70.0)
```

3. **Lab values (Hemoglobin, Creatinine, etc.):**
```python
# Trước
hgb = st.number_input("Hemoglobin (g/dL)", value=7.0, step=0.1)
# Hiển thị: 7.20 (2 số thập phân)

# Sau
from utils.formatters import render_lab_value_input
hgb = render_lab_value_input("Hemoglobin (g/dL)", value=7.0, decimals=1)
# Hiển thị: 7.2 (1 số thập phân)
```

---

## 📚 API Reference

Xem file `utils/formatters.py` để biết chi tiết đầy đủ về:
- Tất cả các hàm format
- Tất cả các hàm render input
- Các tham số và options
- Ví dụ sử dụng

---

**Created:** 2025-02-04  
**Version:** 1.0.0  
**Status:** ✅ Ready for use

