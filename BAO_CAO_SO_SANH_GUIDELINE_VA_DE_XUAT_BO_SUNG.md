# BÁO CÁO SO SÁNH VỚI GUIDELINE VÀ ĐỀ XUẤT BỔ SUNG

**Ngày:** 2025-02-05  
**Mục đích:** So sánh các protocol với guideline quốc tế và đề xuất bổ sung

---

## 📋 TỔNG QUAN

Sau khi đọc kỹ và so sánh các protocol với các guideline quốc tế chính thức, đây là báo cáo chi tiết về những điểm có thể cần bổ sung hoặc cải thiện.

---

## 🦠 SEPSIS PROTOCOL

### ✅ Điểm mạnh hiện có:
- ✅ 1-Hour Bundle đầy đủ (lactate, cultures, antibiotics, fluids, vasopressor)
- ✅ 3-Hour Bundle mở rộng với source control
- ✅ Antibiotic selection theo community vs hospital acquired
- ✅ Vasopressor management (norepinephrine, vasopressin, epinephrine)
- ✅ Fluid resuscitation với calculator
- ✅ Monitoring parameters

### 🔍 Đề xuất bổ sung:

#### 1. **Corticosteroids trong Septic Shock**
**Guideline:** Surviving Sepsis Campaign 2021 khuyến nghị:
- **Hydrocortisone 200mg/day** nếu:
  - Septic shock với vasopressor không đáp ứng sau truyền dịch
  - Hoặc cần vasopressor >0.1 mcg/kg/min norepinephrine
- **Liều:** 50mg IV q6h hoặc 200mg/day continuous infusion
- **Thời gian:** 7 ngày hoặc đến khi không cần vasopressor

**Đề xuất:** Thêm section về corticosteroids trong sepsis_3hour.py

#### 2. **Renal Replacement Therapy (RRT)**
**Guideline:** Chỉ định RRT trong sepsis:
- AKI stage 2-3 với oliguria/anuria
- Uremia (BUN >100 mg/dL)
- Acidosis nặng (pH <7.15) không đáp ứng
- Quá tải dịch không đáp ứng lợi tiểu
- Hyperkalemia nặng (>6.5 mEq/L)

**Đề xuất:** Thêm section về RRT indications trong sepsis_3hour.py

#### 3. **Blood Glucose Management**
**Guideline:** 
- Mục tiêu: 140-180 mg/dL
- Tránh <110 mg/dL (tăng mortality)
- Insulin infusion nếu glucose >180 mg/dL

**Đề xuất:** Thêm section về glucose management

#### 4. **Venous Thromboembolism (VTE) Prophylaxis**
**Guideline:**
- LMWH hoặc UFH cho tất cả bệnh nhân sepsis không chống chỉ định
- Bắt đầu trong 24h đầu

**Đề xuất:** Thêm section về VTE prophylaxis

#### 5. **Stress Ulcer Prophylaxis**
**Guideline:**
- PPI hoặc H2 blocker cho bệnh nhân có nguy cơ
- Có sẵn trong stress_ulcer.py nhưng nên nhắc trong sepsis

**Đề xuất:** Thêm reference đến stress ulcer prophylaxis

---

## 🧠 STROKE PROTOCOL

### ✅ Điểm mạnh hiện có:
- ✅ BE FAST mnemonic
- ✅ Timeline goals (door-to-CT, door-to-needle, door-to-puncture)
- ✅ tPA eligibility checklist với interactive calculator
- ✅ Time windows (0-3h, 3-4.5h, wake-up stroke)
- ✅ Mechanical thrombectomy criteria
- ✅ Hemorrhagic stroke management

### 🔍 Đề xuất bổ sung:

#### 1. **Tenecteplase (TNK-tPA)**
**Guideline:** AHA/ASA 2023 đã cập nhật:
- **Tenecteplase** có thể thay thế alteplase trong một số trường hợp
- **Liều:** 0.25 mg/kg IV bolus (max 25mg)
- **Ưu điểm:** Single bolus, không cần infusion
- **Chỉ định:** Tương tự alteplase nhưng đang được nghiên cứu mở rộng

**Đề xuất:** Thêm section về tenecteplase như một lựa chọn

#### 2. **Mechanical Thrombectomy - Extended Window**
**Guideline:** AHA/ASA 2023:
- **DAWN Trial:** Up to 24h với clinical-imaging mismatch
- **DEFUSE-3 Trial:** Up to 16h với perfusion mismatch
- **CT Perfusion** hoặc **MRI DWI-FLAIR** để xác định salvageable tissue

**Đề xuất:** Mở rộng section về mechanical thrombectomy với extended windows

#### 3. **Blood Pressure Management trong Ischemic Stroke**
**Guideline:** AHA/ASA:
- **Trước tPA:** SBP <185/110 mmHg
- **Sau tPA:** SBP <180/105 mmHg trong 24h đầu
- **Nếu không tPA:** Có thể cho phép SBP cao hơn (permissive hypertension)
- **Thuốc:** Labetalol, nicardipine, clevidipine

**Đề xuất:** Thêm section chi tiết về BP management

#### 4. **Antiplatelet Therapy**
**Guideline:**
- **Aspirin 160-325mg** trong 24-48h sau stroke (nếu không tPA)
- **Dual antiplatelet (DAPT):** Aspirin + Clopidogrel trong 21 ngày cho minor stroke/TIA
- **Chống chỉ định:** Không dùng trong 24h sau tPA

**Đề xuất:** Thêm section về antiplatelet therapy timing

#### 5. **Dysphagia Screening**
**Guideline:**
- Screen tất cả bệnh nhân stroke trước khi cho ăn/uống
- NPO cho đến khi screen negative
- Formal swallow evaluation nếu screen positive

**Đề xuất:** Thêm section về dysphagia screening

#### 6. **Fever Management**
**Guideline:**
- Mục tiêu: Normothermia (<37.5°C)
- Acetaminophen hoặc cooling nếu sốt
- Sốt tăng mortality và poor outcomes

**Đề xuất:** Thêm section về fever management

---

## 💔 ACS PROTOCOL

### ✅ Điểm mạnh hiện có:
- ✅ STEMI vs NSTEMI/UA phân loại
- ✅ A-B-C-D-E approach
- ✅ Primary PCI vs Fibrinolysis
- ✅ DAPT (Aspirin + P2Y12 inhibitor)
- ✅ Anticoagulation
- ✅ Risk stratification (GRACE, TIMI)

### 🔍 Đề xuất bổ sung:

#### 1. **High-Sensitivity Troponin (hs-Tn)**
**Guideline:** ESC 2020, AHA 2021:
- **0/1h Algorithm:** Rule-out/rule-in nhanh
- **0/2h Algorithm:** Alternative
- **0/3h Algorithm:** Nếu không có hs-Tn
- **Delta change:** >20% hoặc >50% ngưỡng

**Đề xuất:** Thêm section về troponin algorithms và interpretation

#### 2. **Coronary CT Angiography (CCTA)**
**Guideline:** ESC 2020:
- **Chỉ định:** Low-intermediate risk NSTEMI/UA
- **Rule-out:** Nếu CCTA negative → discharge
- **Rule-in:** Nếu CCTA positive → invasive angiography

**Đề xuất:** Thêm section về CCTA trong NSTEMI workup

#### 3. **Early Invasive Strategy Timing**
**Guideline:** ESC 2020:
- **Immediate (<2h):** Refractory angina, hemodynamic instability, life-threatening arrhythmias
- **Early (<24h):** GRACE >140, dynamic ECG changes, elevated troponin
- **Delayed (24-72h):** Low risk, stable

**Đề xuất:** Thêm section chi tiết về timing của invasive strategy

#### 4. **Glycoprotein IIb/IIIa Inhibitors**
**Guideline:** 
- **Chỉ định:** High-risk PCI, thrombus burden cao
- **Thuốc:** Abciximab, eptifibatide, tirofiban
- **Không routine:** Chỉ khi cần thiết

**Đề xuất:** Thêm section về GP IIb/IIIa inhibitors (khi nào dùng)

#### 5. **Statin Therapy**
**Guideline:**
- **High-intensity statin:** Atorvastatin 80mg hoặc Rosuvastatin 20-40mg
- **Bắt đầu ngay:** Trong 24h đầu
- **Mục tiêu:** LDL <70 mg/dL hoặc giảm >50%

**Đề xuất:** Thêm section về statin therapy (hiện có nhưng có thể chi tiết hơn)

#### 6. **Beta-Blocker Timing**
**Guideline:**
- **NSTEMI:** Có thể bắt đầu sớm nếu không chống chỉ định
- **STEMI:** Có thể trì hoãn nếu Killip class III-IV (suy tim nặng)
- **Contraindications:** Shock, severe HF, HR <60, SBP <100

**Đề xuất:** Làm rõ timing và contraindications của beta-blocker

---

## 🍭 DKA PROTOCOL

### ✅ Điểm mạnh hiện có:
- ✅ Severity classification (mild/moderate/severe)
- ✅ Fluid deficit calculator
- ✅ Insulin rate calculator
- ✅ Potassium replacement
- ✅ Transition to SC insulin

### 🔍 Đề xuất bổ sung:

#### 1. **Bicarbonate Therapy**
**Guideline:** ADA, ISPAD:
- **Chỉ định:** pH <6.9 với hemodynamic instability
- **Liều:** 50-100 mEq NaHCO₃ trong 500ml D5W
- **Không routine:** Nếu pH >7.0 (không cải thiện outcomes)

**Đề xuất:** Thêm section về bicarbonate (khi nào dùng, khi nào không)

#### 2. **Phosphate Replacement**
**Guideline:**
- **Chỉ định:** Phosphate <1.0 mg/dL
- **Liều:** 20-30 mmol IV trong 6-12h
- **Cảnh báo:** Có thể gây hypocalcemia

**Đề xuất:** Thêm section về phosphate replacement

#### 3. **Cerebral Edema Prevention (Pediatric)**
**Guideline:** ISPAD:
- **Nguy cơ:** Trẻ em <5 tuổi
- **Phòng ngừa:** 
  - Tránh truyền dịch quá nhanh
  - Tránh giảm glucose quá nhanh (>100 mg/dL/h)
  - Tránh giảm Na quá nhanh
- **Dấu hiệu:** Headache, altered mental status, bradycardia

**Đề xuất:** Thêm section về cerebral edema (nếu có pediatric protocol)

#### 4. **DKA Precipitants**
**Guideline:**
- **Common causes:** Infection, missed insulin, new-onset diabetes, MI, stroke
- **Cần tìm:** Source of infection, cardiac events

**Đề xuất:** Thêm section về tìm nguyên nhân gây DKA

#### 5. **Transition to Subcutaneous Insulin**
**Guideline:**
- **Criteria:** pH >7.3, HCO₃⁻ >18, anion gap <12, eating
- **Timing:** Overlap IV và SC insulin 1-2h
- **Dosing:** Calculate total daily dose từ IV rate

**Đề xuất:** Thêm calculator cho SC insulin transition

---

## 🫁 ARDS PROTOCOL

### ✅ Điểm mạnh hiện có:
- ✅ Berlin Definition với interactive calculator
- ✅ Lung protective ventilation (6 ml/kg IBW)
- ✅ PEEP/FiO₂ table
- ✅ Prone positioning
- ✅ Fluid management

### 🔍 Đề xuất bổ sung:

#### 1. **Neuromuscular Blockade**
**Guideline:** SCCM 2017:
- **Chỉ định:** ARDS nặng (PaO₂/FiO₂ <150) trong 48h đầu
- **Thuốc:** Cisatracurium (ưu tiên) hoặc vecuronium
- **Liều:** Continuous infusion để đạt deep paralysis
- **Thời gian:** 48h

**Đề xuất:** Thêm section về neuromuscular blockade

#### 2. **ECMO (Extracorporeal Membrane Oxygenation)**
**Guideline:** ELSO, SCCM:
- **Chỉ định:** ARDS nặng không đáp ứng với conventional therapy
- **Criteria:** 
  - PaO₂/FiO₂ <80 với PEEP ≥10 trong >6h
  - Hoặc pH <7.15 với Pplat >30
- **Timing:** Early referral (<7 days)

**Đề xuất:** Thêm section về ECMO indications và referral

#### 3. **Corticosteroids trong ARDS**
**Guideline:** 
- **Chỉ định:** ARDS do COVID-19 (Dexamethasone 6mg/day × 10 days)
- **Không routine:** ARDS không do COVID-19 (không có bằng chứng rõ ràng)

**Đề xuất:** Thêm section về corticosteroids (khi nào dùng)

#### 4. **Inhaled Nitric Oxide (iNO)**
**Guideline:**
- **Không routine:** Không cải thiện mortality
- **Có thể thử:** Refractory hypoxemia như rescue therapy
- **Liều:** 5-40 ppm

**Đề xuất:** Thêm section về iNO (rescue therapy, không routine)

#### 5. **Fluid Management Strategy**
**Guideline:** FACTT Trial:
- **Conservative fluid:** Giảm ventilator days
- **Liberal fluid:** Nếu shock, cần volume
- **Mục tiêu:** CVP <4 mmHg (conservative) vs 10-14 mmHg (liberal)

**Đề xuất:** Làm rõ fluid strategy (conservative vs liberal)

---

## 🩸 GI BLEEDING PROTOCOL

### ✅ Điểm mạnh hiện có:
- ✅ Upper vs Lower GI bleeding
- ✅ GBS và Rockall calculators
- ✅ Resuscitation protocol
- ✅ Anticoagulation reversal
- ✅ Variceal vs non-variceal
- ✅ PPI dosing calculator

### 🔍 Đề xuất bổ sung:

#### 1. **Tranexamic Acid (TXA)**
**Guideline:** HALT-IT Trial:
- **Chỉ định:** Upper GI bleeding (có thể giảm mortality)
- **Liều:** 1g IV bolus, sau đó 3g trong 24h
- **Timing:** Trong 8h từ khi khởi phát

**Đề xuất:** Thêm section về TXA trong UGIB

#### 2. **Endoscopic Hemostasis Techniques**
**Guideline:**
- **Injection:** Epinephrine 1:10,000
- **Thermal:** Bipolar electrocoagulation, heater probe
- **Mechanical:** Clips, bands
- **Combination:** Injection + thermal/mechanical

**Đề xuất:** Thêm section về endoscopic techniques

#### 3. **Variceal Bleeding - TIPS**
**Guideline:**
- **Chỉ định:** Variceal bleeding không đáp ứng với endoscopic therapy
- **Timing:** Early TIPS (<72h) cho high-risk patients
- **Criteria:** Child-Pugh B với active bleeding hoặc Child-Pugh C

**Đề xuất:** Thêm section về TIPS indications

#### 4. **Lower GI Bleeding - Colonoscopy Timing**
**Guideline:**
- **Urgent (<24h):** Active bleeding, hemodynamic instability
- **Early (24-48h):** Stable với preparation
- **Delayed (>48h):** Low risk, elective

**Đề xuất:** Thêm section về colonoscopy timing trong LGIB

#### 5. **Angiography và Embolization**
**Guideline:**
- **Chỉ định:** Active bleeding không đáp ứng với endoscopy
- **Timing:** Sau khi endoscopy thất bại
- **Technique:** Selective embolization

**Đề xuất:** Thêm section về angiography/embolization

---

## 📊 TỔNG KẾT ĐỀ XUẤT BỔ SUNG

### Ưu tiên CAO (Quan trọng, ảnh hưởng outcomes):

1. **Sepsis:**
   - ✅ Corticosteroids trong septic shock
   - ✅ RRT indications
   - ✅ Glucose management

2. **Stroke:**
   - ✅ Tenecteplase option
   - ✅ Extended window mechanical thrombectomy
   - ✅ Blood pressure management chi tiết

3. **ACS:**
   - ✅ High-sensitivity troponin algorithms
   - ✅ Early invasive strategy timing

4. **DKA:**
   - ✅ Bicarbonate therapy (khi nào dùng)
   - ✅ Phosphate replacement

5. **ARDS:**
   - ✅ Neuromuscular blockade
   - ✅ ECMO indications

### Ưu tiên TRUNG BÌNH (Cải thiện care):

1. **Sepsis:**
   - VTE prophylaxis
   - Stress ulcer prophylaxis reference

2. **Stroke:**
   - Antiplatelet timing
   - Dysphagia screening
   - Fever management

3. **ACS:**
   - CCTA trong NSTEMI
   - GP IIb/IIIa inhibitors

4. **GI Bleeding:**
   - TXA
   - Endoscopic techniques
   - TIPS indications

### Ưu tiên THẤP (Nice to have):

1. **DKA:**
   - Cerebral edema prevention (nếu có pediatric)
   - DKA precipitants

2. **ARDS:**
   - iNO (rescue therapy)
   - Corticosteroids (COVID-19 specific)

---

## 🎯 KHUYẾN NGHỊ TRIỂN KHAI

### Bước 1: Bổ sung các điểm ưu tiên CAO
- Tập trung vào các điểm ảnh hưởng trực tiếp đến outcomes
- Cập nhật các protocol chính (sepsis, stroke, ACS, DKA, ARDS)

### Bước 2: Cải thiện các điểm ưu tiên TRUNG BÌNH
- Thêm các section hỗ trợ chẩn đoán và điều trị
- Cải thiện workflow và decision-making

### Bước 3: Hoàn thiện các điểm ưu tiên THẤP
- Thêm các chi tiết bổ sung
- Cải thiện completeness

---

## 📚 NGUỒN THAM KHẢO CHÍNH

1. **Sepsis:**
   - Surviving Sepsis Campaign 2021
   - IDSA Guidelines 2017

2. **Stroke:**
   - AHA/ASA Guidelines 2021, 2023
   - DAWN, DEFUSE-3 Trials

3. **ACS:**
   - ESC Guidelines 2020
   - AHA/ACC Guidelines 2021

4. **DKA:**
   - ADA Guidelines 2023
   - ISPAD Guidelines 2022

5. **ARDS:**
   - Berlin Definition 2012
   - SCCM Guidelines 2017
   - FACTT Trial

6. **GI Bleeding:**
   - ACG Guidelines 2021
   - BSG Guidelines 2021

---

## ✅ KẾT LUẬN

Các protocol hiện tại đã **rất đầy đủ và chất lượng cao**. Tuy nhiên, để đạt được **best practice** và **cập nhật với guideline mới nhất**, các điểm bổ sung trên sẽ giúp:

1. **Cải thiện outcomes** (ưu tiên cao)
2. **Tối ưu workflow** (ưu tiên trung bình)
3. **Hoàn thiện protocol** (ưu tiên thấp)

**Khuyến nghị:** Bắt đầu với các điểm ưu tiên CAO, sau đó tiếp tục với các điểm khác.

---

**Ngày hoàn thành:** 2025-02-05  
**Người phân tích:** Comprehensive Protocol Review  
**Phiên bản:** 1.0

