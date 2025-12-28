# 📋 KẾ HOẠCH CHI TIẾT PHASE 9-12
## ICU Scoring & Advanced Tools

**Ngày:** 2025-02-05  
**Ưu tiên:** Priority 1 & 2

---

## 🎯 PHASE 9: ICU SCORING SYSTEMS

### 9.1: GCS Calculator ⭐ Priority 1

**Files cần tạo:**
- `critical_care/gcs_calculator.py` - Core module
- `components/gcs_calculator.py` - UI component
- Tích hợp vào `pages/09_🫁_Critical_Care.py`

**Tính năng:**
- Input: Mắt (1-4), Lời nói (1-5), Vận động (1-6)
- Tính tổng điểm GCS (3-15)
- Phân loại: Nhẹ (13-15), Trung bình (9-12), Nặng (3-8)
- Lưu lịch sử
- Hiển thị chi tiết từng thành phần

**Công thức:**
```
GCS = Eye + Verbal + Motor
```

---

### 9.2: SOFA Score Calculator ⭐ Priority 2

**Files cần tạo:**
- `critical_care/sofa_score.py` - Core module
- `components/sofa_score_calculator.py` - UI component
- Tích hợp vào `pages/09_🫁_Critical_Care.py`

**Tính năng:**
- Input 6 hệ cơ quan:
  - Hô hấp (PaO2/FiO2)
  - Đông máu (Platelets)
  - Gan (Bilirubin)
  - Tim mạch (MAP, vasopressors)
  - Thần kinh (GCS)
  - Thận (Creatinine, Urine output)
- Tính tổng điểm SOFA (0-24)
- Đánh giá từng hệ
- Theo dõi diễn biến
- Cảnh báo khi điểm tăng

**Công thức:**
```
SOFA = Sum of 6 organ system scores (0-4 each)
```

---

## 🎯 PHASE 10: SEDATION & NEUROLOGICAL

### 10.1: RASS Calculator ⭐ Priority 1

**Files cần tạo:**
- `critical_care/rass_calculator.py` - Core module
- `components/rass_calculator.py` - UI component
- Tích hợp vào `pages/09_🫁_Critical_Care.py`

**Tính năng:**
- Đánh giá RASS (-5 đến +4)
- Hướng dẫn đánh giá từng mức
- Khuyến nghị điều chỉnh liều an thần
- Lưu lịch sử
- So sánh với mục tiêu

**Thang điểm:**
- +4: Kích động dữ dội
- +1: Kích động
- 0: Tỉnh táo, bình tĩnh
- -1: Buồn ngủ
- -5: Không đánh thức được

---

## 🎯 PHASE 11: ACID-BASE ADVANCED

### 11.1: Anion Gap Calculator ⭐ Priority 1

**Files cần tạo:**
- `critical_care/anion_gap.py` - Core module
- `components/anion_gap_calculator.py` - UI component
- Tích hợp vào `pages/05_🔬_Labs_and_Calculators.py`

**Tính năng:**
- Input: Na+, Cl-, HCO3-
- Tính anion gap: AG = Na+ - (Cl- + HCO3-)
- Phân loại: Bình thường (8-12), Tăng (>12), Giảm (<8)
- Chẩn đoán phân biệt:
  - AG tăng: Nhiễm toan lactic, ketoacidosis, ngộ độc
  - AG bình thường: Mất HCO3-, suy thận
- Delta gap
- Khuyến nghị điều trị

**Công thức:**
```
AG = Na+ - (Cl- + HCO3-)
Delta gap = (AG - 12) - (24 - HCO3-)
```

---

## 🎯 PHASE 12: CARDIOVASCULAR ADVANCED

### 12.1: QTc Calculator ⭐ Priority 1

**Files cần tạo:**
- `critical_care/qtc_calculator.py` - Core module
- `components/qtc_calculator.py` - UI component
- Tích hợp vào `pages/09_🫁_Critical_Care.py`

**Tính năng:**
- Input: QT interval (ms), RR interval (ms), Giới tính
- Tính QTc bằng 3 công thức:
  - Bazett: QTc = QT / √RR
  - Fridericia: QTc = QT / ∛RR
  - Framingham: QTc = QT + 0.154(1-RR)
- Phân loại:
  - Bình thường: <450ms (nam), <470ms (nữ)
  - Kéo dài: >450ms (nam), >470ms (nữ)
  - Rất kéo dài: >500ms
- Cảnh báo nguy cơ Torsades de Pointes
- Đánh giá tác dụng phụ thuốc

**Công thức:**
```
Bazett: QTc = QT / √(RR/1000)
Fridericia: QTc = QT / ∛(RR/1000)
Framingham: QTc = QT + 0.154(1-RR)
```

---

### 12.2: Shock Index Calculator ⭐ Priority 2

**Files cần tạo:**
- `critical_care/shock_index.py` - Core module
- `components/shock_index_calculator.py` - UI component
- Tích hợp vào `pages/09_🫁_Critical_Care.py`

**Tính năng:**
- Input: Heart rate (bpm), Systolic BP (mmHg)
- Tính shock index: SI = HR / SBP
- Phân loại:
  - Bình thường: <0.7
  - Tăng: 0.7-1.0
  - Cao: >1.0
- Cảnh báo sốc
- Khuyến nghị điều trị
- Lưu lịch sử

**Công thức:**
```
Shock Index = Heart Rate / Systolic BP
```

---

## 📊 TỔNG KẾT

### Phase 9: ICU Scoring
- 9.1: GCS Calculator ✅ Priority 1
- 9.2: SOFA Score ✅ Priority 2

### Phase 10: Sedation
- 10.1: RASS Calculator ✅ Priority 1

### Phase 11: Acid-Base
- 11.1: Anion Gap ✅ Priority 1

### Phase 12: Cardiovascular
- 12.1: QTc Calculator ✅ Priority 1
- 12.2: Shock Index ✅ Priority 2

**Tổng cộng:** 6 tính năng mới (4 Priority 1, 2 Priority 2)

---

## 🚀 THỨ TỰ THỰC HIỆN

1. **Phase 9.1: GCS Calculator** ⭐ Priority 1
2. **Phase 10.1: RASS Calculator** ⭐ Priority 1
3. **Phase 11.1: Anion Gap Calculator** ⭐ Priority 1
4. **Phase 12.1: QTc Calculator** ⭐ Priority 1
5. **Phase 9.2: SOFA Score** ⭐ Priority 2
6. **Phase 12.2: Shock Index** ⭐ Priority 2

---

*© 2025 - Kế hoạch Phase 9-12*

