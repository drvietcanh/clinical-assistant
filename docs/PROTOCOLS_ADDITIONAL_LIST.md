# 📋 Danh Sách Các Protocol Bổ Sung - Từ Các Nguồn Y Tế Uy Tín

**Ngày tạo:** 2025-02-05  
**Mục tiêu:** Bổ sung các protocol phổ biến từ UpToDate, Medscape, Epocrates, và các guideline quốc tế

---

## 📊 TỔNG QUAN

### ✅ **Protocols Hiện Có (17 protocols):**
- Emergency: 7 protocols
- Respiratory: 2 protocols
- Cardiology: 2 protocols
- Nephrology: 1 protocol
- Infectious: 3 protocols
- Endocrinology: 3 protocols
- Oncology: 3 protocols

### 🎯 **Protocols Cần Bổ Sung (Ưu Tiên Cao)**

---

## 🚨 PRIORITY 1: Emergency & Critical Care

### 1. **Anaphylaxis Management** ⭐⭐⭐
- **Guideline:** ACAAI/WAO 2020, NIAID 2017
- **Tần suất sử dụng:** Rất cao
- **Nguồn tham khảo:** UpToDate, Medscape, Epocrates
- **Nội dung:**
  - Recognition & diagnosis
  - Epinephrine dosing (IM vs IV)
  - Antihistamines (H1 & H2 blockers)
  - Corticosteroids
  - Fluid resuscitation
  - Biphasic reactions
- **File:** `protocols/emergency/anaphylaxis.py`

### 2. **Hypertensive Emergency/Urgency** ⭐⭐⭐
- **Guideline:** AHA/ACC 2017, JNC 8
- **Tần suất sử dụng:** Rất cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - Hypertensive emergency vs urgency
  - Target BP reduction
  - IV medications (labetalol, nicardipine, esmolol)
  - Oral medications
  - Organ-specific protocols (stroke, aortic dissection, preeclampsia)
- **File:** `protocols/emergency/hypertensive_emergency.py`

### 3. **Status Epilepticus** ⭐⭐⭐
- **Guideline:** AES 2016, Neurocritical Care Society
- **Tần suất sử dụng:** Cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - Definition & classification
  - First-line: Benzodiazepines (lorazepam, midazolam)
  - Second-line: Fosphenytoin, valproate, levetiracetam
  - Refractory: Midazolam/Propofol infusion
  - RSE: Ketamine, pentobarbital
- **File:** `protocols/emergency/status_epilepticus.py`

### 4. **Acute Alcohol Withdrawal** ⭐⭐
- **Guideline:** ASAM 2020, CIWA-Ar protocol
- **Tần suất sử dụng:** Cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - CIWA-Ar scoring
  - Benzodiazepine protocol (symptom-triggered vs fixed)
  - Thiamine, folate, multivitamin
  - Seizure prophylaxis
  - Delirium tremens management
- **File:** `protocols/emergency/alcohol_withdrawal.py`

### 5. **Opioid Overdose / Naloxone Protocol** ⭐⭐⭐
- **Guideline:** AHA 2020, SAMHSA
- **Tần suất sử dụng:** Rất cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - Recognition (respiratory depression, miosis)
  - Naloxone dosing (IV, IM, IN)
  - Titration protocol
  - Monitoring for re-narcotization
  - Supportive care
- **File:** `protocols/emergency/opioid_overdose.py`

---

## ❤️ PRIORITY 2: Cardiology

### 6. **Atrial Fibrillation Management** ⭐⭐⭐
- **Guideline:** AHA/ACC/HRS 2019, ESC 2020
- **Tần suất sử dụng:** Rất cao
- **Nguồn tham khảo:** UpToDate, Medscape, Epocrates
- **Nội dung:**
  - Rate vs rhythm control
  - Anticoagulation (CHADS2-VASc, HAS-BLED)
  - Rate control medications
  - Cardioversion (electrical vs chemical)
  - Acute AF with RVR
- **File:** `protocols/cardiology/atrial_fibrillation.py`

### 7. **DVT/PE Management** ⭐⭐⭐
- **Guideline:** ACCP 2016, ESC 2019
- **Tần suất sử dụng:** Rất cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - Risk stratification (Wells score, PERC)
  - Diagnostic algorithm
  - Anticoagulation (DOACs vs warfarin)
  - Thrombolysis indications
  - IVC filter indications
- **File:** `protocols/cardiology/dvt_pe.py`

---

## 🧪 PRIORITY 3: Gastroenterology

### 8. **Acute Pancreatitis** ⭐⭐
- **Guideline:** ACG 2013, AGA 2018
- **Tần suất sử dụng:** Cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - Diagnosis (lipase, imaging)
  - Severity scoring (Ranson, BISAP, APACHE II)
  - Fluid resuscitation
  - Pain management
  - ERCP indications
  - Nutrition (early enteral)
- **File:** `protocols/gastroenterology/acute_pancreatitis.py`

### 9. **Acute Liver Failure** ⭐
- **Guideline:** AASLD 2011, EASL 2017
- **Tần suất sử dụng:** Trung bình
- **Nguồn tham khảo:** UpToDate
- **Nội dung:**
  - Etiology-specific management
  - N-acetylcysteine (acetaminophen)
  - ICP monitoring
  - Liver transplant criteria
- **File:** `protocols/gastroenterology/acute_liver_failure.py`

---

## ⚕️ PRIORITY 4: Endocrinology

### 10. **Hyperglycemic Hyperosmolar State (HHS)** ⭐⭐
- **Guideline:** ADA 2023, Endocrine Society
- **Tần suất sử dụng:** Trung bình-Cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - Diagnostic criteria
  - Fluid resuscitation
  - Insulin therapy (lower rate than DKA)
  - Electrolyte management
  - Thrombosis prophylaxis
- **File:** `protocols/endocrinology/hhs.py`

---

## 🧠 PRIORITY 5: Neurology

### 11. **Acute Stroke - Thrombolysis Protocol** ⭐⭐
- **Guideline:** AHA/ASA 2019 (đã có stroke management, cần bổ sung thrombolysis chi tiết)
- **Tần suất sử dụng:** Cao
- **Nội dung:**
  - tPA eligibility (time window, contraindications)
  - Dosing protocol
  - Post-tPA monitoring
  - Mechanical thrombectomy
- **File:** `protocols/emergency/stroke_thrombolysis.py` (hoặc mở rộng stroke.py)

---

## 🩸 PRIORITY 6: Hematology

### 12. **Transfusion Protocols** ⭐⭐
- **Guideline:** AABB 2016, ASH 2018
- **Tần suất sử dụng:** Rất cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - RBC transfusion thresholds
  - Platelet transfusion
  - FFP transfusion
  - Cryoprecipitate
  - Massive transfusion protocol
- **File:** `protocols/hematology/transfusion.py`

### 13. **Anticoagulation Reversal** ⭐⭐
- **Guideline:** ACCP 2018, ASH 2018
- **Tần suất sử dụng:** Cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - Warfarin reversal (vitamin K, FFP, PCC)
  - DOAC reversal (andexanet, idarucizumab)
  - Heparin reversal (protamine)
  - LMWH reversal
- **File:** `protocols/hematology/anticoagulation_reversal.py`

---

## 💊 PRIORITY 7: Pain & Symptom Management

### 14. **Acute Pain Management** ⭐⭐
- **Guideline:** ASIPP 2017, WHO
- **Tần suất sử dụng:** Rất cao
- **Nguồn tham khảo:** UpToDate, Medscape
- **Nội dung:**
  - Pain assessment scales
  - Multimodal analgesia
  - Opioid dosing & titration
  - Non-opioid alternatives
  - Special populations
- **File:** `protocols/pain/acute_pain.py`

### 15. **Acute Gout Management** ⭐
- **Guideline:** ACR 2020, EULAR 2016
- **Tần suất sử dụng:** Trung bình
- **Nguồn tham khảo:** UpToDate
- **Nội dung:**
  - Diagnosis (clinical vs crystal)
  - NSAIDs, colchicine, steroids
  - Urate-lowering therapy initiation
- **File:** `protocols/rheumatology/acute_gout.py`

---

## 🧠 PRIORITY 8: Psychiatry/Critical Care

### 16. **Delirium Management** ⭐⭐
- **Guideline:** ICU Delirium Guidelines, NICE
- **Tần suất sử dụng:** Cao (ICU)
- **Nguồn tham khảo:** UpToDate
- **Nội dung:**
  - CAM-ICU assessment
  - Non-pharmacologic management
  - Pharmacologic treatment (haloperidol, quetiapine)
  - Prevention strategies
- **File:** `protocols/critical_care/delirium.py`

---

## 📊 TỔNG KẾT

### **Ưu Tiên Thực Hiện (Top 10):**

1. ✅ **Anaphylaxis Management** - Rất cao
2. ✅ **Hypertensive Emergency** - Rất cao
3. ✅ **Status Epilepticus** - Cao
4. ✅ **Atrial Fibrillation** - Rất cao
5. ✅ **DVT/PE Management** - Rất cao
6. ✅ **Opioid Overdose** - Rất cao
7. ✅ **Acute Pancreatitis** - Cao
8. ✅ **HHS** - Trung bình-Cao
9. ✅ **Transfusion Protocols** - Rất cao
10. ✅ **Acute Alcohol Withdrawal** - Cao

### **Thống Kê:**
- **Tổng protocols mới:** 16 protocols
- **Sau khi bổ sung:** 33 protocols (tăng 94%)
- **Chuyên khoa mới:** Gastroenterology, Hematology, Pain Management, Rheumatology

---

## 📚 NGUỒN THAM KHẢO

### **Websites & Apps:**
1. **UpToDate** - Clinical decision support
2. **Medscape** - Medical reference
3. **Epocrates** - Drug & clinical reference
4. **MDCalc** - Clinical calculators
5. **EMCrit** - Critical care protocols
6. **Life in the Fast Lane** - Emergency medicine

### **Guideline Organizations:**
- AHA/ACC (Cardiology)
- AHA/ASA (Stroke)
- IDSA (Infectious Disease)
- ACAAI/WAO (Allergy)
- AES (Epilepsy)
- ACG/AGA (Gastroenterology)
- AASLD (Liver)
- AABB (Blood Banking)
- ASH (Hematology)

---

**Last Updated:** 2025-02-05  
**Status:** 📋 Ready for Implementation

