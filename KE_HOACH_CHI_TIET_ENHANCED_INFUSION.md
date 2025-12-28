# 📋 KẾ HOẠCH CHI TIẾT: ENHANCED INFUSION CALCULATOR
## Phase 3: Tính tốc độ truyền chi tiết nâng cao

**Ngày bắt đầu:** Sau khi hoàn thành Phase 2  
**Mục tiêu:** Bổ sung tính năng tính giọt/phút, thời gian truyền chi tiết  
**Ưu tiên:** ⭐⭐ Trung bình

---

## 🎯 TỔNG QUAN

### Mục tiêu
- Tạo calculator tính tốc độ truyền chi tiết
- Tính giọt/phút với nhiều drop factors
- Tính thời gian truyền
- Hỗ trợ nhiều phương pháp truyền (bơm, chai, túi)

### Tính năng cần có
1. **Infusion Rate Calculator**
   - Input: Liều, cân nặng, nồng độ
   - Output: ml/hr, gtt/min

2. **Time Calculator**
   - Input: Thể tích, tốc độ
   - Output: Thời gian truyền

3. **Volume Calculator**
   - Input: Liều, thời gian, nồng độ
   - Output: Thể tích cần pha

4. **Drop Factor Support**
   - Hỗ trợ: 10, 15, 20, 60 gtt/ml

---

## 📚 NGHIÊN CỨU

### Code hiện có
- ✅ DIRC calculator đã có `mcg_kg_min_to_ml_hr`
- ✅ Phase 2 đã có `calculate_drop_rate` và `calculate_infusion_time`
- ⚠️ Chưa có calculator tổng hợp cho tất cả scenarios

### So sánh với Medical Calculator
- ✅ Medical Calculator có tính giọt/phút
- ✅ Medical Calculator có tính thời gian truyền
- ✅ Medical Calculator hỗ trợ nhiều drop factors

---

## 📝 KẾ HOẠCH CHI TIẾT

### BƯỚC 1: Nghiên cứu và thiết kế (Ngày 1-2)

#### Task 1.1: Nghiên cứu code hiện có
- [ ] Đọc DIRC calculator
- [ ] Đọc Phase 2 calculator
- [ ] Xác định tính năng còn thiếu

**Deliverable:**
- Document: `docs/enhanced_infusion_research.md`

---

### BƯỚC 2: Tạo Enhanced Infusion Module (Ngày 3-5)

#### Task 2.1: Tạo module `critical_care/enhanced_infusion.py`

**Functions cần có:**
```python
def calculate_infusion_rate(
    dose_mcg_kg_min: float,
    weight_kg: float,
    concentration_mcg_ml: float,
    drop_factor: Optional[int] = None
) -> dict:
    """Calculate infusion rate with optional drop rate"""
    pass

def calculate_volume_needed(
    dose_mcg_kg_min: float,
    weight_kg: float,
    duration_hours: float,
    concentration_mcg_ml: float
) -> dict:
    """Calculate volume needed for given duration"""
    pass

def calculate_dose_from_rate(
    infusion_rate_ml_hour: float,
    weight_kg: float,
    concentration_mcg_ml: float
) -> dict:
    """Calculate dose from infusion rate (reverse calculation)"""
    pass
```

**Checklist:**
- [ ] Functions có docstring
- [ ] Type hints đầy đủ
- [ ] Error handling
- [ ] Unit tests

---

#### Task 2.2: Tích hợp với Phase 2
- [ ] Sử dụng lại functions từ Phase 2
- [ ] Mở rộng tính năng
- [ ] Không duplicate code

---

### BƯỚC 3: Tạo UI Component (Ngày 6-7)

#### Task 3.1: Tạo Streamlit component

**File:** `components/enhanced_infusion_calculator.py`

**UI Elements:**
- [ ] Tab 1: Tính tốc độ truyền
- [ ] Tab 2: Tính thời gian truyền
- [ ] Tab 3: Tính thể tích cần pha
- [ ] Tab 4: Tính liều từ tốc độ (reverse)

**Checklist:**
- [ ] UI rõ ràng
- [ ] Responsive
- [ ] Error handling

---

#### Task 3.2: Tích hợp vào Critical Care
- [ ] Thêm vào Critical Care page
- [ ] Link từ các calculators khác
- [ ] UI nhất quán

---

### BƯỚC 4: Testing (Ngày 8-9)

#### Task 4.1: Unit Tests
- [ ] Test tất cả functions
- [ ] Test edge cases
- [ ] Test với Medical Calculator

---

#### Task 4.2: Integration Tests
- [ ] Test với Phase 2
- [ ] Test với DIRC calculator
- [ ] Test UI

---

### BƯỚC 5: Documentation (Ngày 10)

#### Task 5.1: User Guide
- [ ] Hướng dẫn sử dụng
- [ ] Ví dụ tính toán
- [ ] FAQ

---

## ✅ CHECKLIST TỔNG HỢP

### Trước khi bắt đầu
- [ ] Phase 2 đã hoàn thành
- [ ] Đã nghiên cứu code hiện có
- [ ] Đã thiết kế module

### Trong quá trình
- [ ] Mỗi function có test
- [ ] So sánh với Medical Calculator
- [ ] Tích hợp mượt với Phase 2

### Trước khi release
- [ ] Tất cả tests pass
- [ ] So sánh với Medical Calculator khớp
- [ ] Documentation đầy đủ

---

## 📅 TIMELINE

| Bước | Ngày | Trạng thái |
|------|------|------------|
| Bước 1: Nghiên cứu | 1-2 | ⏳ Pending |
| Bước 2: Module | 3-5 | ⏳ Pending |
| Bước 3: UI | 6-7 | ⏳ Pending |
| Bước 4: Testing | 8-9 | ⏳ Pending |
| Bước 5: Documentation | 10 | ⏳ Pending |

**Tổng thời gian:** 10 ngày (2 tuần)

---

*© 2025 - Kế hoạch chi tiết Enhanced Infusion Calculator*

