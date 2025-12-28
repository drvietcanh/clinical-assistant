# 📋 KẾ HOẠCH BỔ SUNG TÍNH NĂNG INFUSION
## Multiple Infusions & Compatibility Checking

**Ngày bắt đầu:** Sau khi hoàn thành Phase 1-4  
**Mục tiêu:** Bổ sung tính năng multiple infusions và compatibility checking  
**Ưu tiên:** ⭐⭐⭐ Cao

---

## 🎯 TỔNG QUAN

### Tính năng cần bổ sung:

1. **Multiple Simultaneous Infusions** ⭐⭐⭐
   - Tính nhiều thuốc cùng lúc
   - Tổng hợp thể tích, tốc độ
   - Cảnh báo giới hạn

2. **Drug Compatibility Checker** ⭐⭐⭐
   - Database tương thích
   - Kiểm tra khi trộn
   - Cảnh báo và hướng dẫn

3. **Electrolyte Concentration Calculator** ⭐⭐
   - Tính nồng độ điện giải
   - Điều chỉnh Na+, K+, Ca++
   - Tính áp lực thẩm thấu

---

## 📚 NGHIÊN CỨU

### Multiple Infusions - Tính năng cần có:

1. **Add/Remove Drugs:**
   - Button "Thêm thuốc"
   - Dropdown chọn thuốc
   - Input liều, cân nặng
   - Button "Xóa" cho mỗi thuốc

2. **Summary View:**
   - Tổng thể tích (nếu cùng chai)
   - Tổng tốc độ truyền
   - Tổng giọt/phút
   - Danh sách từng thuốc

3. **Warnings:**
   - Cảnh báo khi tổng thể tích > 500ml
   - Cảnh báo khi tổng tốc độ > giới hạn
   - Cảnh báo compatibility

---

### Compatibility Database - Cấu trúc:

```json
{
  "compatibility": {
    "Adrenaline": {
      "compatible": ["Noradrenaline", "Dopamine"],
      "incompatible": ["Sodium bicarbonate", "Alkaline solutions"],
      "conditional": ["Dobutamine", "Milrinone"],
      "notes": "Không trộn với sodium bicarbonate"
    }
  }
}
```

---

## 📝 KẾ HOẠCH CHI TIẾT

### Phase 5.1: Multiple Infusions Calculator (5-6 ngày)

#### Task 1: Tạo module `critical_care/multiple_infusions.py`

**Functions:**
```python
def add_infusion(
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str
) -> dict:
    """Add an infusion to the list"""
    pass

def calculate_total_volume(infusions: list) -> dict:
    """Calculate total volume if same bag"""
    pass

def calculate_total_rate(infusions: list) -> dict:
    """Calculate total infusion rate"""
    pass

def validate_limits(total_volume: float, total_rate: float) -> dict:
    """Validate against safety limits"""
    pass
```

#### Task 2: Tạo UI component

**File:** `components/multiple_infusions_calculator.py`

**UI Elements:**
- [ ] Button "Thêm thuốc"
- [ ] List các thuốc đã thêm
- [ ] Summary view
- [ ] Warnings
- [ ] Export/Print

---

### Phase 5.2: Compatibility Checker (4-5 ngày)

#### Task 1: Tạo compatibility database

**File:** `drugs/compatibility_database.json`

**Cấu trúc:**
- Compatible drugs
- Incompatible drugs
- Conditional compatibility
- Notes và hướng dẫn

#### Task 2: Tạo compatibility checker

**File:** `drugs/compatibility_checker.py`

**Functions:**
```python
def check_compatibility(drug1: str, drug2: str) -> dict:
    """Check if two drugs are compatible"""
    pass

def check_multiple_compatibility(drugs: list) -> dict:
    """Check compatibility of multiple drugs"""
    pass
```

#### Task 3: Tích hợp vào Multiple Infusions

- [ ] Tự động kiểm tra khi thêm thuốc
- [ ] Cảnh báo rõ ràng
- [ ] Hướng dẫn cách pha an toàn

---

### Phase 5.3: Electrolyte Calculator (3-4 ngày)

#### Task 1: Tạo electrolyte calculator

**File:** `critical_care/electrolyte_calculator.py`

**Functions:**
```python
def calculate_electrolyte_addition(
    current_volume_ml: float,
    current_na_mmol_l: float,
    target_na_mmol_l: float
) -> dict:
    """Calculate Na+ addition needed"""
    pass

def calculate_osmolarity(
    na_mmol_l: float,
    glucose_mmol_l: float,
    bun_mmol_l: float
) -> float:
    """Calculate osmolarity"""
    pass
```

#### Task 2: Tích hợp vào Fluid Therapy

- [ ] Thêm tab "Electrolyte Calculator"
- [ ] Tính Na+, K+, Ca++
- [ ] Tính áp lực thẩm thấu

---

## ✅ CHECKLIST

### Phase 5.1: Multiple Infusions
- [ ] Core functions
- [ ] UI component
- [ ] Tích hợp vào Enhanced Infusion
- [ ] Testing

### Phase 5.2: Compatibility
- [ ] Compatibility database
- [ ] Compatibility checker
- [ ] Tích hợp vào Multiple Infusions
- [ ] Testing

### Phase 5.3: Electrolyte
- [ ] Electrolyte calculator
- [ ] Tích hợp vào Fluid Therapy
- [ ] Testing

---

## 📅 TIMELINE

**Phase 5.1:** 5-6 ngày  
**Phase 5.2:** 4-5 ngày  
**Phase 5.3:** 3-4 ngày  

**Tổng:** 12-15 ngày (2.5-3 tuần)

---

*© 2025 - Kế hoạch bổ sung tính năng Infusion*

