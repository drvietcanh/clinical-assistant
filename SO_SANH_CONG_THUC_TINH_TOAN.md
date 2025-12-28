# 🔬 SO SÁNH CÔNG THỨC TÍNH TOÁN
## Kiểm tra và verify công thức với các nguồn uy tín

**Mục đích:** Đảm bảo tính chính xác của các công thức tính toán  
**Ngày tạo:** 2025-02-05

---

## 📚 CÔNG THỨC 1: TÍNH TỐC ĐỘ TRUYỀN (mcg/kg/min → ml/hr)

### Công thức của chúng ta:
```python
ml/hr = (mcg/kg/min × kg × 60) / (mg/ml × 1000)
```

**Hoặc viết rõ hơn:**
```
Tổng liều (mcg/min) = Liều (mcg/kg/min) × Cân nặng (kg)
Tổng liều (mcg/giờ) = Tổng liều (mcg/min) × 60
Tốc độ (ml/giờ) = Tổng liều (mcg/giờ) / Nồng độ pha (mcg/ml)
```

### So sánh với các nguồn:

#### ✅ DIRC Calculator (codebase hiện có)
**File:** `critical_care/dirc/conversions.py`
```python
def mcg_kg_min_to_ml_hr(dose_mcg_kg_min: float, weight_kg: float, concentration_mg_ml: float) -> float:
    return (dose_mcg_kg_min * weight_kg * 60) / (concentration_mg_ml * 1000)
```
**Kết luận:** ✅ Khớp 100%

#### ✅ Medical Calculator (tkinter app)
**Công thức tương tự:**
```
ml/hr = (dose_mcg_kg_min × weight_kg × 60) / (concentration_mg_ml × 1000)
```
**Kết luận:** ✅ Khớp 100%

#### ✅ UpToDate / Clinical Guidelines
**Công thức chuẩn:**
- Tổng liều/giờ = Liều/kg/phút × Cân nặng × 60
- Tốc độ = Tổng liều/giờ / Nồng độ
**Kết luận:** ✅ Khớp 100%

### Ví dụ tính toán:

**Input:**
- Liều: 0.1 mcg/kg/min
- Cân nặng: 70 kg
- Nồng độ pha: 4 mcg/ml (1mg/250ml NS)

**Tính toán:**
```
Tổng liều/phút = 0.1 × 70 = 7 mcg/min
Tổng liều/giờ = 7 × 60 = 420 mcg/h
Tốc độ = 420 / 4 = 105 ml/h
```

**Verify:**
- Medical Calculator: ✅ 105 ml/h
- Tính tay: ✅ 105 ml/h
- DIRC calculator: ✅ 105 ml/h

**Kết luận:** ✅ Công thức đúng

---

## 📚 CÔNG THỨC 2: TÍNH GIỌT/PHÚT (gtt/min)

### Công thức của chúng ta:
```python
gtt/min = (ml/hr × drop_factor) / 60
```

### So sánh với các nguồn:

#### ✅ Medical Calculator
**Công thức:**
```
gtt/min = (ml/hr × drop_factor) / 60
```
**Kết luận:** ✅ Khớp 100%

#### ✅ Nursing Textbooks
**Công thức chuẩn:**
```
gtt/min = (Volume × Drop factor) / Time (minutes)
```
Với Volume = ml/hr và Time = 60 phút:
```
gtt/min = (ml/hr × drop_factor) / 60
```
**Kết luận:** ✅ Khớp 100%

### Ví dụ tính toán:

**Input:**
- Tốc độ: 105 ml/h
- Drop factor: 20 gtt/ml

**Tính toán:**
```
gtt/min = (105 × 20) / 60 = 35 gtt/min
```

**Verify:**
- Medical Calculator: ✅ 35 gtt/min
- Tính tay: ✅ 35 gtt/min

**Kết luận:** ✅ Công thức đúng

---

## 📚 CÔNG THỨC 3: TÍNH THỜI GIAN TRUYỀN

### Công thức của chúng ta:
```python
time_hours = volume_ml / infusion_rate_ml_hour
time_minutes = time_hours × 60
```

### So sánh với các nguồn:

#### ✅ Medical Calculator
**Công thức:**
```
Thời gian (giờ) = Thể tích (ml) / Tốc độ (ml/giờ)
```
**Kết luận:** ✅ Khớp 100%

#### ✅ Basic Math
**Công thức vật lý:**
```
Time = Distance / Speed
→ Time = Volume / Rate
```
**Kết luận:** ✅ Khớp 100%

### Ví dụ tính toán:

**Input:**
- Thể tích: 50 ml (bơm tiêm điện)
- Tốc độ: 105 ml/h

**Tính toán:**
```
Thời gian = 50 / 105 = 0.476 giờ = 28.6 phút
```

**Verify:**
- Medical Calculator: ✅ 28.6 phút
- Tính tay: ✅ 28.6 phút

**Kết luận:** ✅ Công thức đúng

---

## 📚 CÔNG THỨC 4: TÍNH SỐ LƯỢNG ỐNG CẦN DÙNG

### Công thức của chúng ta:
```python
vials_needed = math.ceil(total_dose_mg / vial_size_mg)
```

### So sánh với các nguồn:

#### ✅ Medical Calculator
**Công thức:**
```
Số lượng ống = CEIL(Tổng liều / Liều mỗi ống)
```
**Kết luận:** ✅ Khớp 100%

#### ✅ Basic Logic
**Logic chuẩn:**
- Nếu cần 150 mg và ống có 100 mg → Cần 2 ống
- Nếu cần 100 mg và ống có 100 mg → Cần 1 ống
- Nếu cần 50 mg và ống có 100 mg → Cần 1 ống (không thể dùng 0.5 ống)
**Kết luận:** ✅ Logic đúng

### Ví dụ tính toán:

**Input:**
- Tổng liều: 150 mg
- Ống có: 100 mg

**Tính toán:**
```
Số lượng = CEIL(150 / 100) = CEIL(1.5) = 2 ống
```

**Verify:**
- Medical Calculator: ✅ 2 ống
- Logic: ✅ 2 ống

**Kết luận:** ✅ Công thức đúng

---

## 📚 CÔNG THỨC 5: TÍNH LƯỢNG THUỐC THỪA (WASTE)

### Công thức của chúng ta:
```python
waste_mg = (vials_needed × vial_size_mg) - total_dose_mg
waste_percent = (waste_mg / (vials_needed × vial_size_mg)) × 100
```

### So sánh với các nguồn:

#### ⚠️ Medical Calculator
**Chưa có tính waste trong code**
**Kết luận:** ⚠️ Cần verify logic

#### ✅ Basic Math
**Logic:**
- Tổng có: Số ống × Liều mỗi ống
- Cần dùng: Tổng liều
- Thừa: Tổng có - Cần dùng
**Kết luận:** ✅ Logic đúng

### Ví dụ tính toán:

**Input:**
- Số lượng ống: 2
- Liều mỗi ống: 100 mg
- Tổng liều cần: 150 mg

**Tính toán:**
```
Tổng có = 2 × 100 = 200 mg
Thừa = 200 - 150 = 50 mg
Phần trăm = (50 / 200) × 100 = 25%
```

**Verify:**
- Logic: ✅ 50 mg (25%)

**Kết luận:** ✅ Công thức đúng

---

## 📚 CÔNG THỨC 6: TÍNH NỒNG ĐỘ PHA

### Công thức của chúng ta:
```python
concentration_mg_ml = total_dose_mg / volume_ml
concentration_mcg_ml = concentration_mg_ml × 1000
```

### So sánh với các nguồn:

#### ✅ Medical Calculator
**Công thức:**
```
Nồng độ = Tổng liều / Thể tích
```
**Kết luận:** ✅ Khớp 100%

#### ✅ Chemistry
**Công thức chuẩn:**
```
Concentration = Mass / Volume
```
**Kết luận:** ✅ Khớp 100%

### Ví dụ tính toán:

**Input:**
- Tổng liều: 1 mg
- Thể tích: 250 ml

**Tính toán:**
```
Nồng độ = 1 / 250 = 0.004 mg/ml = 4 mcg/ml
```

**Verify:**
- Medical Calculator: ✅ 4 mcg/ml
- Tính tay: ✅ 4 mcg/ml

**Kết luận:** ✅ Công thức đúng

---

## ✅ TỔNG KẾT

| Công thức | Trạng thái | Nguồn verify |
|-----------|------------|--------------|
| mcg/kg/min → ml/hr | ✅ Đúng | DIRC, Medical Calculator, UpToDate |
| ml/hr → gtt/min | ✅ Đúng | Medical Calculator, Nursing textbooks |
| Tính thời gian | ✅ Đúng | Medical Calculator, Basic math |
| Tính số ống | ✅ Đúng | Medical Calculator, Logic |
| Tính waste | ✅ Đúng | Logic (Medical Calculator chưa có) |
| Tính nồng độ | ✅ Đúng | Medical Calculator, Chemistry |

**Kết luận:** Tất cả công thức đều đúng và đã được verify với nhiều nguồn.

---

## 📝 LƯU Ý KHI IMPLEMENT

1. **Rounding:**
   - Số ống: Luôn làm tròn lên (CEIL)
   - Tốc độ: Làm tròn đến 1 chữ số thập phân
   - Giọt/phút: Làm tròn đến số nguyên

2. **Validation:**
   - Liều > 0
   - Cân nặng > 0
   - Nồng độ > 0
   - Thể tích > 0

3. **Error handling:**
   - Kiểm tra division by zero
   - Kiểm tra giá trị âm
   - Thông báo lỗi rõ ràng

---

*© 2025 - So sánh công thức tính toán với các nguồn uy tín*

