# 📋 KẾ HOẠCH CHI TIẾT: TÍNH LIỀU THUỐC TIM MẠCH VỚI VIAL
## Phase 2: Triển khai từng bước với kiểm tra và so sánh

**Ngày bắt đầu:** Sau khi hoàn thành Phase 1  
**Mục tiêu:** Module tính liều thuốc tim mạch với vial management  
**Ưu tiên:** ⭐⭐⭐ Cao

---

## 🎯 TỔNG QUAN

### Mục tiêu
- Tạo module tính liều thuốc tim mạch cấp cứu
- Tích hợp với Vial Management System (Phase 1)
- Tính tốc độ truyền cho bơm 50ml và chai 500ml
- Tính giọt/phút với drop factor

### Thuốc cần hỗ trợ
1. Adrenaline (Epinephrine)
2. Noradrenaline (Norepinephrine)
3. Dopamine
4. Dobutamine
5. Vasopressin
6. Milrinone
7. Nitroglycerin

---

## 📚 NGHIÊN CỨU CÔNG THỨC

### 1. Công thức tính liều (mcg/kg/min → ml/hr)

#### Công thức cơ bản:
```
Tổng liều (mcg/min) = Liều (mcg/kg/min) × Cân nặng (kg)
Tổng liều (mcg/giờ) = Tổng liều (mcg/min) × 60
Tốc độ (ml/giờ) = Tổng liều (mcg/giờ) / Nồng độ pha (mcg/ml)
```

**Ví dụ:**
- Liều: 0.1 mcg/kg/min
- Cân nặng: 70 kg
- Nồng độ pha: 4 mcg/ml (1mg trong 250ml)
- Tính:
  - Tổng liều: 0.1 × 70 = 7 mcg/min
  - Tổng liều/giờ: 7 × 60 = 420 mcg/h
  - Tốc độ: 420 / 4 = 105 ml/h

#### Công thức gộp:
```
ml/hr = (mcg/kg/min × kg × 60) / (mg/ml × 1000)
```

**Verify với DIRC calculator hiện có:**
- File: `critical_care/dirc/conversions.py`
- Function: `mcg_kg_min_to_ml_hr()`
- ✅ Đã có sẵn, công thức đúng

---

### 2. Công thức tính giọt/phút

```
Giọt/phút = (Tốc độ ml/giờ × Drop factor) / 60
```

**Drop factors phổ biến:**
- Macro drip: 10, 15, 20 gtt/ml
- Micro drip: 60 gtt/ml

**Ví dụ:**
- Tốc độ: 105 ml/h
- Drop factor: 20 gtt/ml
- Giọt/phút: (105 × 20) / 60 = 35 gtt/min

---

### 3. Công thức tính thời gian truyền

```
Thời gian (giờ) = Thể tích (ml) / Tốc độ (ml/giờ)
Thời gian (phút) = Thời gian (giờ) × 60
```

**Ví dụ:**
- Thể tích: 50 ml (bơm tiêm điện)
- Tốc độ: 105 ml/h
- Thời gian: 50 / 105 = 0.476 giờ = 28.6 phút

---

### 4. So sánh với các nguồn

#### Medical Calculator (tkinter)
- ✅ Có tính ml/hr
- ✅ Có tính giọt/phút
- ✅ Có tính thời gian truyền
- ✅ Hỗ trợ bơm 50ml và chai 500ml

#### MDCalc
- ⚠️ Không có calculator riêng cho vasopressor infusion
- ✅ Có các calculator khác (verify công thức tương tự)

#### HSCC.vn
- ✅ Có tính liều vasopressor
- ⚠️ Chưa rõ có tính giọt/phút

#### UpToDate
- ✅ Có hướng dẫn liều dùng
- ✅ Có cách pha thuốc
- ⚠️ Không có calculator

---

## 📝 KẾ HOẠCH CHI TIẾT

### BƯỚC 1: Nghiên cứu và thiết kế (Ngày 1-2)

#### Task 1.1: Nghiên cửu thuốc tim mạch
- [ ] Đọc code Medical Calculator về thuốc tim mạch
- [ ] Nghiên cứu vasopressor guide hiện có (`critical_care/vasopressors.py`)
- [ ] So sánh với Surviving Sepsis Guidelines
- [ ] So sánh với ACCM Guidelines

**Deliverable:**
- Document: `docs/cardiovascular_drugs_research.md`
- Comparison table với Medical Calculator

**Checklist:**
- [ ] Liều dùng khớp với guidelines
- [ ] Cách pha khớp với hướng dẫn
- [ ] Nồng độ pha chuẩn

---

#### Task 1.2: Thiết kế module
- [ ] Thiết kế cấu trúc module
- [ ] Thiết kế UI/UX
- [ ] Thiết kế tích hợp với Vial Management

**Deliverable:**
- Design document
- UI mockup

---

### BƯỚC 2: Tạo Cardiovascular Drugs Database (Ngày 3-4)

#### Task 2.1: Tạo JSON database

**File:** `drugs/cardiovascular_drugs.json`

**Cấu trúc:**
```json
{
  "Adrenaline": {
    "name": "Adrenaline",
    "name_vn": "Adrenaline",
    "group": "Vận mạch",
    "dose_range": "0.01–0.5 mcg/kg/min",
    "initial_dose": "0.05–0.1 mcg/kg/min",
    "max_dose": "1–2 mcg/kg/min",
    "preparation": "1mg/1ml, 1mg/10ml",
    "standard_concentration": "4 mcg/ml (1mg/250ml NS)",
    "solvent": "NaCl 0.9%",
    "indication": "Sốc phản vệ, ngừng tim, sốc tim",
    "contraindication": "...",
    "side_effects": "...",
    "monitoring": "MAP, HR, ngón tay chân, lactate, glucose",
    "vials": [
      {
        "size": "1mg/1ml",
        "volume_ml": 1,
        "concentration_mg_ml": 1.0,
        "total_mg": 1.0
      }
    ],
    "infusion_methods": {
      "syringe_pump_50ml": {
        "standard_volume": 50,
        "standard_concentration_mg_ml": 0.02,
        "preparation": "1mg pha trong 50ml NS = 0.02 mg/ml = 20 mcg/ml"
      },
      "iv_bag_500ml": {
        "standard_volume": 500,
        "standard_concentration_mg_ml": 0.004,
        "preparation": "2mg pha trong 500ml NS = 0.004 mg/ml = 4 mcg/ml"
      }
    },
    "notes": "..."
  }
}
```

**Checklist:**
- [ ] Dữ liệu chính xác (verify với MIMS, UpToDate)
- [ ] Đầy đủ 7 thuốc
- [ ] Có thông tin vial
- [ ] Có thông tin cách pha

---

#### Task 2.2: Verify dữ liệu

**Nguồn tham khảo:**
- [ ] MIMS Vietnam
- [ ] UpToDate
- [ ] Surviving Sepsis 2021
- [ ] Medical Calculator
- [ ] Vasopressor guide hiện có

**Checklist:**
- [ ] Liều dùng khớp
- [ ] Cách pha khớp
- [ ] Nồng độ pha khớp

---

### BƯỚC 3: Implement Core Functions (Ngày 5-7)

#### Task 3.1: Tạo module `drugs/cardiovascular_calculator.py`

**Functions:**

```python
def calculate_vasopressor_infusion(
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str = "syringe_pump_50ml"
) -> dict:
    """
    Calculate vasopressor infusion details
    
    Args:
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        infusion_method: "syringe_pump_50ml" or "iv_bag_500ml"
    
    Returns:
        {
            "total_dose_mcg_min": float,
            "total_dose_mcg_hour": float,
            "infusion_rate_ml_hour": float,
            "concentration_mcg_ml": float,
            "drop_rate_gtt_min": float,  # If applicable
            "infusion_time_hours": float,
            "preparation_instructions": str
        }
    """
    pass

def calculate_drop_rate(
    infusion_rate_ml_hour: float,
    drop_factor: int = 20
) -> float:
    """
    Calculate drop rate in gtt/min
    
    Args:
        infusion_rate_ml_hour: Infusion rate in ml/hour
        drop_factor: Drop factor (10, 15, 20, or 60 gtt/ml)
    
    Returns:
        Drop rate in gtt/min
    """
    pass

def calculate_infusion_time(
    volume_ml: float,
    infusion_rate_ml_hour: float
) -> dict:
    """
    Calculate infusion time
    
    Returns:
        {
            "time_hours": float,
            "time_minutes": float,
            "time_formatted": str
        }
    """
    pass
```

**Checklist:**
- [ ] Functions có docstring đầy đủ
- [ ] Type hints
- [ ] Error handling
- [ ] Unit tests

---

#### Task 3.2: Verify công thức

**Test cases:**

```python
# Test 1: Adrenaline - Basic calculation
result = calculate_vasopressor_infusion(
    "Adrenaline", 0.1, 70, "iv_bag_500ml"
)
expected = {
    "total_dose_mcg_min": 7.0,
    "total_dose_mcg_hour": 420.0,
    "infusion_rate_ml_hour": 105.0,  # 420 / 4
    "concentration_mcg_ml": 4.0
}
assert abs(result["infusion_rate_ml_hour"] - expected["infusion_rate_ml_hour"]) < 0.1

# Test 2: Drop rate
drop_rate = calculate_drop_rate(105, 20)
expected = 35.0  # (105 * 20) / 60
assert abs(drop_rate - expected) < 0.1

# Test 3: Infusion time
time = calculate_infusion_time(50, 105)
expected_hours = 50 / 105
assert abs(time["time_hours"] - expected_hours) < 0.01
```

**So sánh với:**
- [ ] Medical Calculator
- [ ] DIRC calculator hiện có
- [ ] Tính tay

---

### BƯỚC 4: Tạo UI Component (Ngày 8-9)

#### Task 4.1: Tạo Streamlit component

**File:** `components/cardiovascular_calculator.py`

**UI Elements:**
- [ ] Dropdown chọn thuốc
- [ ] Input liều (mcg/kg/min)
- [ ] Input cân nặng
- [ ] Radio chọn phương pháp truyền (bơm 50ml / chai 500ml)
- [ ] Input drop factor (nếu chai truyền)
- [ ] Hiển thị kết quả:
  - Tốc độ ml/giờ
  - Giọt/phút (nếu có)
  - Thời gian truyền
  - Hướng dẫn pha
  - Vial management (từ Phase 1)

**Checklist:**
- [ ] UI rõ ràng
- [ ] Responsive
- [ ] Error handling
- [ ] Real-time calculation

---

#### Task 4.2: Tích hợp vào Critical Care

**File:** `pages/09_🫁_Critical_Care.py`

**Integration:**
- [ ] Thêm tab "Tính liều thuốc tim mạch"
- [ ] Link từ Vasopressor guide
- [ ] Hiển thị kết quả đẹp

---

### BƯỚC 5: Testing và Validation (Ngày 10-11)

#### Task 5.1: Unit Tests

**Test cases:**
- [ ] Test tính liều cho mỗi thuốc
- [ ] Test tính giọt/phút
- [ ] Test tính thời gian
- [ ] Test edge cases
- [ ] Test error handling

---

#### Task 5.2: So sánh với Medical Calculator

**Test scenarios:**
1. Adrenaline: 0.1 mcg/kg/min, 70kg
2. Noradrenaline: 0.1 mcg/kg/min, 70kg
3. Dopamine: 5 mcg/kg/min, 70kg
4. Dobutamine: 5 mcg/kg/min, 70kg

**Tolerance:** < 1% sai số

---

#### Task 5.3: Manual Testing

**Scenarios:**
- [ ] Test với các liều khác nhau
- [ ] Test với các cân nặng khác nhau
- [ ] Test với cả 2 phương pháp truyền
- [ ] Test drop factor khác nhau

---

### BƯỚC 6: Documentation (Ngày 12)

#### Task 6.1: User Guide
- [ ] Hướng dẫn sử dụng
- [ ] Ví dụ tính toán
- [ ] FAQ

---

## ✅ CHECKLIST TỔNG HỢP

### Trước khi bắt đầu
- [ ] Phase 1 (Vial Management) đã hoàn thành
- [ ] Đã nghiên cứu công thức
- [ ] Đã so sánh với Medical Calculator

### Trong quá trình
- [ ] Mỗi function có test
- [ ] So sánh kết quả với Medical Calculator
- [ ] Verify với guidelines

### Trước khi release
- [ ] Tất cả tests pass
- [ ] So sánh với Medical Calculator khớp
- [ ] Documentation đầy đủ

---

## 📅 TIMELINE

| Bước | Ngày | Trạng thái |
|------|------|------------|
| Bước 1: Nghiên cứu | 1-2 | ⏳ Pending |
| Bước 2: Database | 3-4 | ⏳ Pending |
| Bước 3: Core Functions | 5-7 | ⏳ Pending |
| Bước 4: UI | 8-9 | ⏳ Pending |
| Bước 5: Testing | 10-11 | ⏳ Pending |
| Bước 6: Documentation | 12 | ⏳ Pending |

**Tổng thời gian:** 12 ngày (2.5 tuần)

---

*© 2025 - Kế hoạch chi tiết Cardiovascular Drugs Calculator*

