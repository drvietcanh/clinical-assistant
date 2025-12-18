# 📐 TEMPLATE KỸ THUẬT - DIRC CALCULATOR
## Drug Infusion Rate Conversion Calculator

**Ngày tạo:** 2025-01-30  
**Version:** 1.0  
**Status:** Planning

---

## 📋 TỔNG QUAN

### Mục Đích
DIRC (Drug Infusion Rate Conversion) calculator là công cụ chuyển đổi liều truyền thuốc giữa các đơn vị khác nhau, đặc biệt quan trọng trong ICU/ED.

### Yêu Cầu Chức Năng

1. **Chuyển đổi cơ bản:**
   - (mcg/kg/phút) ↔ (mL/giờ)
   - (mcg/phút) ↔ (mL/giờ)
   - (mg/phút) ↔ (mL/giờ)
   - (g/phút) ↔ (mL/giờ)

2. **Hỗ trợ bơm tiêm điện 50ml:**
   - Tính toán cho bơm tiêm điện 50ml
   - Hiển thị tốc độ truyền phù hợp

3. **Tính toán dịch truyền:**
   - Tính thời gian truyền dịch
   - Tính thể tích dịch còn lại

4. **Tính năng bổ sung:**
   - Lưu lịch sử tính toán
   - Export kết quả
   - In kết quả

---

## 🧮 CÔNG THỨC TÍNH TOÁN

### 1. Chuyển đổi (mcg/kg/phút) → (mL/giờ)

**Công thức:**
```
mL/giờ = (mcg/kg/phút × kg × 60) / (nồng độ thuốc trong mg/mL × 1000)
```

**Ví dụ:**
- Liều: 5 mcg/kg/phút
- Cân nặng: 70 kg
- Nồng độ: 1 mg/mL (1000 mcg/mL)
- Tính: (5 × 70 × 60) / (1000) = 21 mL/giờ

### 2. Chuyển đổi (mL/giờ) → (mcg/kg/phút)

**Công thức:**
```
mcg/kg/phút = (mL/giờ × nồng độ thuốc trong mg/mL × 1000) / (kg × 60)
```

**Ví dụ:**
- Tốc độ: 21 mL/giờ
- Nồng độ: 1 mg/mL (1000 mcg/mL)
- Cân nặng: 70 kg
- Tính: (21 × 1000) / (70 × 60) = 5 mcg/kg/phút

### 3. Chuyển đổi (mcg/phút) → (mL/giờ)

**Công thức:**
```
mL/giờ = (mcg/phút × 60) / (nồng độ thuốc trong mg/mL × 1000)
```

### 4. Chuyển đổi (mg/phút) → (mL/giờ)

**Công thức:**
```
mL/giờ = (mg/phút × 60) / (nồng độ thuốc trong mg/mL)
```

### 5. Chuyển đổi (g/phút) → (mL/giờ)

**Công thức:**
```
mL/giờ = (g/phút × 60 × 1000) / (nồng độ thuốc trong mg/mL)
```

### 6. Tính thời gian truyền dịch

**Công thức:**
```
Thời gian (giờ) = Thể tích (mL) / Tốc độ (mL/giờ)
Thời gian (phút) = Thời gian (giờ) × 60
```

### 7. Tính thể tích dịch còn lại

**Công thức:**
```
Thể tích còn lại (mL) = Thể tích ban đầu (mL) - (Tốc độ (mL/giờ) × Thời gian đã truyền (giờ))
```

---

## 🎨 THIẾT KẾ UI/UX

### Layout

```
┌─────────────────────────────────────────┐
│  DIRC Calculator                        │
├─────────────────────────────────────────┤
│                                         │
│  [Chọn loại chuyển đổi]                │
│  ┌─────────────────────────────────┐  │
│  │ ○ (mcg/kg/phút) ↔ (mL/giờ)      │  │
│  │ ○ (mcg/phút) ↔ (mL/giờ)         │  │
│  │ ○ (mg/phút) ↔ (mL/giờ)          │  │
│  │ ○ (g/phút) ↔ (mL/giờ)           │  │
│  │ ○ Tính thời gian truyền          │  │
│  │ ○ Tính thể tích còn lại          │  │
│  └─────────────────────────────────┘  │
│                                         │
│  [Input Section]                        │
│  ┌─────────────────────────────────┐  │
│  │ Liều: [____] mcg/kg/phút        │  │
│  │ Cân nặng: [____] kg             │  │
│  │ Nồng độ: [____] mg/mL           │  │
│  │ Thể tích: [____] mL              │  │
│  └─────────────────────────────────┘  │
│                                         │
│  [Results Section]                     │
│  ┌─────────────────────────────────┐  │
│  │ Kết quả: 21 mL/giờ              │  │
│  │ Bơm tiêm điện 50ml: Có thể      │  │
│  └─────────────────────────────────┘  │
│                                         │
│  [Actions]                              │
│  [Tính toán] [Xóa] [Lưu] [Export]      │
└─────────────────────────────────────────┘
```

### Components

1. **Conversion Type Selector**
   - Radio buttons hoặc dropdown
   - 6 options

2. **Input Fields**
   - Liều (dose)
   - Cân nặng (weight)
   - Nồng độ (concentration)
   - Thể tích (volume)
   - Tốc độ (rate)
   - Thời gian (time)

3. **Results Display**
   - Kết quả chính
   - Kết quả phụ (nếu có)
   - Cảnh báo (nếu có)

4. **Action Buttons**
   - Tính toán
   - Xóa
   - Lưu
   - Export

---

## 💻 CẤU TRÚC CODE

### File Structure

```
critical_care/
├── dirc/
│   ├── __init__.py
│   ├── calculator.py          # Main calculator logic
│   ├── conversions.py         # Conversion functions
│   ├── ui.py                  # UI components
│   ├── validation.py          # Input validation
│   └── utils.py               # Utility functions
```

### Class Structure

```python
class DIRCCalculator:
    """Main DIRC Calculator class"""
    
    def __init__(self):
        self.conversion_type = None
        self.inputs = {}
        self.results = {}
    
    def set_conversion_type(self, type: str):
        """Set conversion type"""
        pass
    
    def set_input(self, key: str, value: float):
        """Set input value"""
        pass
    
    def calculate(self) -> dict:
        """Perform calculation"""
        pass
    
    def validate_inputs(self) -> tuple[bool, str]:
        """Validate inputs"""
        pass
```

### Conversion Functions

```python
def mcg_kg_min_to_ml_hr(dose_mcg_kg_min: float, 
                        weight_kg: float, 
                        concentration_mg_ml: float) -> float:
    """
    Convert mcg/kg/min to mL/hr
    
    Formula: mL/hr = (mcg/kg/min × kg × 60) / (mg/mL × 1000)
    """
    if concentration_mg_ml <= 0:
        raise ValueError("Concentration must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    
    ml_per_hr = (dose_mcg_kg_min * weight_kg * 60) / (concentration_mg_ml * 1000)
    return round(ml_per_hr, 2)

def ml_hr_to_mcg_kg_min(ml_per_hr: float,
                        weight_kg: float,
                        concentration_mg_ml: float) -> float:
    """
    Convert mL/hr to mcg/kg/min
    
    Formula: mcg/kg/min = (mL/hr × mg/mL × 1000) / (kg × 60)
    """
    if concentration_mg_ml <= 0:
        raise ValueError("Concentration must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    
    mcg_kg_min = (ml_per_hr * concentration_mg_ml * 1000) / (weight_kg * 60)
    return round(mcg_kg_min, 2)
```

---

## ✅ VALIDATION RULES

### Input Validation

1. **Liều (Dose):**
   - Required: Yes
   - Type: Float
   - Range: > 0
   - Unit: mcg/kg/phút, mcg/phút, mg/phút, g/phút

2. **Cân nặng (Weight):**
   - Required: Yes (for weight-based calculations)
   - Type: Float
   - Range: > 0, typically 1-300 kg
   - Unit: kg

3. **Nồng độ (Concentration):**
   - Required: Yes
   - Type: Float
   - Range: > 0
   - Unit: mg/mL

4. **Thể tích (Volume):**
   - Required: Yes (for time/volume calculations)
   - Type: Float
   - Range: > 0
   - Unit: mL

5. **Tốc độ (Rate):**
   - Required: Yes (for reverse calculations)
   - Type: Float
   - Range: > 0
   - Unit: mL/giờ

6. **Thời gian (Time):**
   - Required: Yes (for volume remaining)
   - Type: Float
   - Range: >= 0
   - Unit: giờ hoặc phút

### Error Messages

- "Liều phải lớn hơn 0"
- "Cân nặng phải lớn hơn 0"
- "Nồng độ phải lớn hơn 0"
- "Thể tích phải lớn hơn 0"
- "Tốc độ phải lớn hơn 0"
- "Thời gian phải >= 0"
- "Vui lòng nhập đầy đủ thông tin"

---

## 🧪 TEST CASES

### Test Case 1: mcg/kg/phút → mL/giờ

**Input:**
- Liều: 5 mcg/kg/phút
- Cân nặng: 70 kg
- Nồng độ: 1 mg/mL

**Expected Output:**
- Kết quả: 21.00 mL/giờ

**Calculation:**
```
(5 × 70 × 60) / (1 × 1000) = 21 mL/giờ
```

### Test Case 2: mL/giờ → mcg/kg/phút

**Input:**
- Tốc độ: 21 mL/giờ
- Cân nặng: 70 kg
- Nồng độ: 1 mg/mL

**Expected Output:**
- Kết quả: 5.00 mcg/kg/phút

**Calculation:**
```
(21 × 1 × 1000) / (70 × 60) = 5 mcg/kg/phút
```

### Test Case 3: Tính thời gian truyền

**Input:**
- Thể tích: 500 mL
- Tốc độ: 100 mL/giờ

**Expected Output:**
- Thời gian: 5.00 giờ (300 phút)

**Calculation:**
```
500 / 100 = 5 giờ
```

### Test Case 4: Tính thể tích còn lại

**Input:**
- Thể tích ban đầu: 500 mL
- Tốc độ: 100 mL/giờ
- Thời gian đã truyền: 2 giờ

**Expected Output:**
- Thể tích còn lại: 300 mL

**Calculation:**
```
500 - (100 × 2) = 300 mL
```

### Edge Cases

1. **Zero values:**
   - Input: 0 → Error message

2. **Negative values:**
   - Input: -5 → Error message

3. **Very large values:**
   - Input: 1000000 → Should handle gracefully

4. **Very small values:**
   - Input: 0.0001 → Should handle gracefully

5. **Missing inputs:**
   - Missing required field → Error message

---

## 📱 MOBILE OPTIMIZATION

### Touch Targets
- All buttons: Minimum 44x44px
- Input fields: Minimum 44px height
- Spacing between elements: Minimum 8px

### Keyboard
- Numeric keyboard for number inputs
- Done button to dismiss keyboard
- Auto-scroll to input when keyboard appears

### Layout
- Stack inputs vertically on mobile
- Full-width buttons on mobile
- Larger font sizes on mobile

---

## 🚀 IMPLEMENTATION PLAN

### Phase 1: Basic Conversion (Week 1)
- [ ] Create file structure
- [ ] Implement basic conversion functions
- [ ] Create basic UI
- [ ] Add validation
- [ ] Test basic functionality

### Phase 2: Advanced Features (Week 2)
- [ ] Add all conversion types
- [ ] Add time/volume calculations
- [ ] Add 50ml syringe pump support
- [ ] Improve UI/UX
- [ ] Add error handling

### Phase 3: Polish (Week 3)
- [ ] Add history
- [ ] Add export
- [ ] Add help section
- [ ] User testing
- [ ] Final polish

---

## 📚 REFERENCES

1. **HSCC.vn DIRC Calculator**
   - Reference implementation
   - URL: https://hscc.vn/tools.asp

2. **Medical Guidelines**
   - ICU medication dosing guidelines
   - Drug infusion protocols

3. **Formulas**
   - Standard conversion formulas
   - Medical calculation references

---

## 🔄 VERSION HISTORY

- **v1.0 (2025-01-30):** Initial template created

---

**Template này sẽ được cập nhật khi implementation tiến triển.**

