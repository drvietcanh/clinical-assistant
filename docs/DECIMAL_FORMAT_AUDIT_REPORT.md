# 📊 Báo Cáo Rà Soát Định Dạng Số Thập Phân

**Ngày:** 2025-02-03  
**Tổng số files có vấn đề:** 109 files  
**Tổng số number_input thiếu format:** ~500+ fields

---

## 📋 PHÂN LOẠI ĐƠN VỊ

### **1. Số Nguyên (format="%d")**

**Các đơn vị cần số nguyên:**
- **Height:** cm
- **Age:** years
- **Vital Signs:**
  - BP (mmHg): Systolic, Diastolic, MAP
  - HR (bpm): Heart Rate
  - RR (/min): Respiratory Rate
  - SpO2 (%)
- **ABG:**
  - PaO2 (mmHg)
  - PaCO2 (mmHg)
  - FiO2 (%)
- **Ventilator:**
  - PEEP (cmH2O)
  - Plateau Pressure (cmH2O)
  - Peak Pressure (cmH2O)
  - Vt (mL)
  - RR (/min)
- **Lab Counts:**
  - Platelets (×10³/μL)
  - WBC (×10³/μL)
  - RBC counts
- **Scores:**
  - GCS (3-15)
  - Urine output (mL)
- **Other:**
  - Units (transfusion)
  - Duration (hours, days - nếu là số nguyên)

---

### **2. 1 Số Thập Phân (format="%.1f")**

**Các đơn vị cần 1 số thập phân:**
- **Weight:** kg
- **Lab Values:**
  - Creatinine (mg/dL, µmol/L)
  - Bilirubin (mg/dL)
  - Albumin (g/dL)
  - Sodium (mEq/L)
  - Potassium (mEq/L)
  - Chloride (mEq/L)
  - HCO3 (mEq/L)
  - BUN (mg/dL)
  - Glucose (mg/dL, mmol/L)
  - Total Protein (g/dL)
  - Calcium (mg/dL)
  - Phosphorus (mg/dL)
  - Magnesium (mg/dL)
- **Temperature:** °C
- **Lactate:** mmol/L
- **CVP:** cmH2O
- **Compliance:** mL/cmH2O
- **Dosing:**
  - Dose (mg/kg, µg/kg/min, etc.)
- **Other:**
  - BMI (kg/m²)
  - Duration (hours - nếu có 0.5 step)
  - Percentages (%)

---

### **3. 2 Số Thập Phân (format="%.2f")**

**Các đơn vị cần 2 số thập phân:**
- **pH:** 7.40
- **INR:** 1.00
- **Troponin:** ng/mL (một số lab)
- **TDM Levels:** Một số thuốc cần độ chính xác cao
- **Ratios:** Một số tỷ lệ đặc biệt

---

## 🔍 FILES CẦN FIX (Ưu Tiên)

### **Critical Care Module (Ưu tiên cao):**
1. `critical_care/ards.py` - 2 fields
2. `critical_care/fluids.py` - 9 fields
3. `critical_care/rrt.py` - 6 fields
4. `critical_care/scoring.py` - 6 fields
5. `critical_care/sedation.py` - 4 fields
6. `critical_care/sepsis.py` - 4 fields
7. `critical_care/shock.py` - 9 fields
8. `critical_care/transfusion.py` - 12 fields
9. `critical_care/vasopressors.py` - 2 fields
10. `critical_care/ventilator.py` - 8 fields

### **Ventilator Module (Ưu tiên cao):**
1. `ventilator/abg_integration.py` - 7 fields
2. `ventilator/calculators.py` - 3 fields
3. `ventilator/comprehensive_calculator.py` - 9 fields
4. `ventilator/weaning.py` - 13 fields

### **Scores Module (Ưu tiên trung bình):**
- Emergency scores: apache2, sofa, saps2, mods, news2, qsofa
- Cardiology scores: ascvd, framingham, grace, killip, qtc, score2
- Nephrology scores: akin, rifle, kdigo, egfr
- Other scores: ~50+ files

### **Labs Module (Ưu tiên trung bình):**
- `labs/abg.py` - 3 fields
- `labs/bmp.py` - 10 fields
- `labs/cbc.py` - 8 fields
- `labs/cardiac.py` - 3 fields
- `labs/coag.py` - 4 fields
- `labs/lft.py` - 6 fields
- `labs/lipid.py` - 6 fields
- `labs/thyroid.py` - 3 fields

### **Antibiotics Module (Ưu tiên trung bình):**
- ~10 files

### **Drugs/TDM Module (Ưu tiên thấp):**
- ~15 files

### **Protocols Module (Ưu tiên thấp):**
- ~5 files

---

## 🎯 KẾ HOẠCH FIX

### **Phase 1: Critical Care & Ventilator (Ưu tiên cao)**
- Fix tất cả files trong `critical_care/` và `ventilator/`
- Estimated: ~60 fields

### **Phase 2: Labs & Scores (Ưu tiên trung bình)**
- Fix labs module
- Fix emergency scores
- Estimated: ~150 fields

### **Phase 3: Other Modules (Ưu tiên thấp)**
- Fix antibiotics, drugs, protocols
- Estimated: ~300 fields

---

## 📝 QUY TẮC FIX

### **Pattern Matching:**

```python
# Height (cm) - Integer
height = st.number_input("Chiều cao (cm)", ..., format="%d")

# Weight (kg) - 1 decimal
weight = st.number_input("Cân nặng (kg)", ..., format="%.1f")

# Age (years) - Integer
age = st.number_input("Tuổi", ..., format="%d")

# BP, HR, MAP - Integer
sbp = st.number_input("SBP (mmHg)", ..., format="%d")
hr = st.number_input("HR (bpm)", ..., format="%d")

# Lab values - 1 decimal
creatinine = st.number_input("Creatinine (mg/dL)", ..., format="%.1f")

# pH - 2 decimals
ph = st.number_input("pH", ..., format="%.2f")

# Temperature - 1 decimal
temp = st.number_input("Nhiệt độ (°C)", ..., format="%.1f")
```

---

## ✅ CHECKLIST

- [ ] Phase 1: Critical Care & Ventilator
- [ ] Phase 2: Labs & Scores  
- [ ] Phase 3: Other Modules
- [ ] Test toàn bộ app
- [ ] Verify không có lỗi

