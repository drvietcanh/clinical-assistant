# 📚 NGHIÊN CỨU VÀ SO SÁNH - PHASE 2
## Cardiovascular Drugs Calculator

**Ngày:** 2025-02-05  
**Mục tiêu:** Nghiên cứu code hiện có và thiết kế module mới

---

## 🔍 PHÂN TÍCH CODE HIỆN CÓ

### 1. Vasopressor Guide (`critical_care/vasopressors.py`)

**Điểm mạnh:**
- ✅ Có database VASOPRESSORS với 6 thuốc
- ✅ Có thông tin đầy đủ: chỉ định, liều dùng, tác dụng phụ
- ✅ Có function `calculate_dose_per_hour` (nhưng chưa đầy đủ)

**Điểm yếu:**
- ❌ Chưa tính ml/hr (chỉ tính mcg/min, mcg/h, mg/h)
- ❌ Chưa tính giọt/phút
- ❌ Chưa tính thời gian truyền
- ❌ Chưa tích hợp với vial management
- ❌ Chưa hỗ trợ bơm 50ml vs chai 500ml

**Cần cải thiện:**
- Tích hợp với DIRC calculator để tính ml/hr
- Thêm tính giọt/phút
- Thêm tính thời gian truyền
- Thêm vial management (tạm thời hardcode)

---

### 2. DIRC Calculator (`critical_care/dirc/`)

**Điểm mạnh:**
- ✅ Đã có công thức `mcg_kg_min_to_ml_hr` - ĐÚNG
- ✅ Đã có công thức `ml_hr_to_mcg_kg_min` - ĐÚNG
- ✅ Đã có drug presets với vial info
- ✅ Code structure tốt, có validation

**Có thể tái sử dụng:**
- Functions conversion từ `conversions.py`
- Drug presets từ `drug_presets.py` (có thể mở rộng)

---

### 3. So sánh với Medical Calculator

**Medical Calculator có:**
- ✅ Tính liều thuốc tim mạch với vial management
- ✅ Tính tốc độ truyền (ml/hr, gtt/min)
- ✅ Tính thời gian truyền
- ✅ Hỗ trợ bơm 50ml và chai 500ml
- ✅ Thông tin đầy đủ về thuốc

**Chúng ta cần:**
- Tạo module tương tự nhưng tích hợp với code hiện có
- Sử dụng lại DIRC calculator
- Mở rộng vasopressor guide hiện có

---

## 📋 THIẾT KẾ MODULE MỚI

### Cấu trúc đề xuất:

```
drugs/
├── cardiovascular_drugs.json          # Database mới (7 thuốc)
└── cardiovascular_calculator.py      # Core functions

components/
└── cardiovascular_calculator.py      # UI component

pages/
└── 09_🫁_Critical_Care.py            # Tích hợp vào đây
```

### Database structure:

```json
{
  "Adrenaline": {
    "name": "Adrenaline",
    "name_vn": "Adrenaline",
    "group": "Vasopressor",
    "dose_range": "0.01–0.5 mcg/kg/min",
    "initial_dose": "0.05–0.1 mcg/kg/min",
    "max_dose": "1–2 mcg/kg/min",
    "vials": [
      {
        "size": "1mg/1ml",
        "volume_ml": 1,
        "concentration_mg_ml": 1.0,
        "total_mg": 1.0
      },
      {
        "size": "1mg/10ml",
        "volume_ml": 10,
        "concentration_mg_ml": 0.1,
        "total_mg": 1.0
      }
    ],
    "infusion_methods": {
      "syringe_pump_50ml": {
        "standard_volume": 50,
        "standard_concentration_mcg_ml": 20,
        "preparation": "1mg pha trong 50ml NS = 20 mcg/ml"
      },
      "iv_bag_500ml": {
        "standard_volume": 500,
        "standard_concentration_mcg_ml": 4,
        "preparation": "2mg pha trong 500ml NS = 4 mcg/ml"
      }
    },
    "indication": "Sốc phản vệ, ngừng tim, sốc tim",
    "contraindication": "...",
    "side_effects": "...",
    "monitoring": "MAP, HR, ngón tay chân, lactate, glucose"
  }
}
```

---

## ✅ KẾT LUẬN

1. **Tái sử dụng code hiện có:**
   - DIRC calculator functions
   - Vasopressor guide structure
   - Drug presets (mở rộng)

2. **Tạo mới:**
   - Cardiovascular drugs database (JSON)
   - Calculator module với đầy đủ tính năng
   - UI component tích hợp

3. **Cải thiện:**
   - Mở rộng vasopressor guide
   - Thêm tính giọt/phút
   - Thêm tính thời gian truyền
   - Thêm vial management (tạm thời)

---

*© 2025 - Nghiên cứu Phase 2*

