# 📋 Kế Hoạch Kiểm Tra Fields Cho Các Thuốc Còn Thiếu

**Ngày tạo:** 2025-02-05  
**Mục tiêu:** Kiểm tra và bổ sung đầy đủ 14 fields cho tất cả các thuốc còn thiếu trong Phase 1

---

## 📊 TỔNG QUAN

### **Các thuốc đã hoàn thành (26/30):**
✅ Salmeterol, Terbutaline, Bupropion, Mirtazapine, Trazodone  
✅ Donepezil, Rivastigmine, Memantine  
✅ Diphenhydramine, Chlorpheniramine, Hydroxyzine  
✅ Flecainide, Propafenone, Chlorthalidone, Indapamide  
✅ Mupirocin, Terbinafine, Nystatin, Tretinoin, Benzoyl Peroxide, Permethrin  
✅ Calcium Gluconate, Sodium Bicarbonate, Magnesium Sulfate, Vasopressin  
✅ Probenecid

### **Các thuốc còn thiếu (13 thuốc):**

#### **1. Neurology - Anticonvulsants (4 thuốc)**
- [ ] Primidone
- [ ] Zonisamide
- [ ] Lacosamide
- [ ] Perampanel

#### **2. Gastrointestinal (2 thuốc)**
- [ ] Sucralfate
- [ ] Misoprostol

#### **3. Cardiovascular (5 thuốc)**
- [ ] Nadolol
- [ ] Timolol
- [ ] Acebutolol
- [ ] Betaxolol
- [ ] Felodipine

#### **4. Antibiotics - Cephalosporins (2 thuốc)**
- [ ] Cefotetan
- [ ] Cefoxitin

---

## ✅ CHECKLIST 14 FIELDS CẦN KIỂM TRA

### **6 Required Fields (Bắt buộc):**
- [ ] `mechanism_of_action` - Cơ chế tác dụng (50-200 từ)
- [ ] `pharmacokinetics` - Dược động học (dict với half_life, onset, duration, protein_binding, clearance)
- [ ] `monitoring` - Theo dõi (list các thông số)
- [ ] `precautions` - Thận trọng (list các lưu ý)
- [ ] `storage` - Bảo quản (hướng dẫn chi tiết)
- [ ] `black_box_warnings` - Cảnh báo đặc biệt (string hoặc None)

### **8 Optional Fields (Tùy chọn nhưng nên có):**
- [ ] `drug_interactions` - Tương tác thuốc (dict với major, moderate, minor)
- [ ] `contraindications` - Chống chỉ định (dict với tuyệt_đối, tương_đối)
- [ ] `pregnancy_lactation` - Thai kỳ và cho con bú (dict với fda_category, pregnancy_details, lactation)
- [ ] `hepatic_adjustment` - Điều chỉnh liều suy gan (dict với mild, moderate, severe, notes)
- [ ] `overdose_management` - Xử trí quá liều (dict với symptoms, antidote, treatment, monitoring)
- [ ] `reversal_agents` - Thuốc giải độc (dict với available, agents)
- [ ] `administration_instructions` - Hướng dẫn dùng thuốc (dict với oral, iv, im, topical, etc.)
- [ ] `references` - Tài liệu tham khảo (dict với primary_sources, last_updated, evidence_level)

---

## 🎯 KẾ HOẠCH THỰC HIỆN

### **Bước 1: Bổ sung các thuốc còn thiếu (13 thuốc)**

#### **Session 1: Neurology - Anticonvulsants (4 thuốc)**
**File:** `drugs/drug_modules/neurological/anticonvulsants.py`

1. **Primidone**
   - Nhóm: Anticonvulsant (Barbiturate-like)
   - Chuyển hóa thành phenobarbital
   - Cần đầy đủ 14 fields

2. **Zonisamide**
   - Nhóm: Anticonvulsant (Sulfonamide)
   - Đa cơ chế, dùng 1 lần/ngày
   - Cần đầy đủ 14 fields

3. **Lacosamide**
   - Nhóm: Anticonvulsant (mới)
   - Tác dụng trên voltage-gated sodium channels
   - Cần đầy đủ 14 fields

4. **Perampanel**
   - Nhóm: Anticonvulsant (AMPA receptor antagonist)
   - Thuốc mới hơn
   - Cần đầy đủ 14 fields

#### **Session 2: Gastrointestinal (2 thuốc)**
**File:** `drugs/drug_modules/gastrointestinal/mucosal_protectants.py`

1. **Sucralfate**
   - Nhóm: Mucosal Protectant
   - Bảo vệ niêm mạc dạ dày
   - Cần đầy đủ 14 fields

2. **Misoprostol**
   - Nhóm: Prostaglandin E1 Analog
   - Phòng loét do NSAID
   - Cần đầy đủ 14 fields

#### **Session 3: Cardiovascular - Beta-blockers (4 thuốc)**
**Files:** 
- `drugs/drug_modules/cardiovascular/beta_blockers/non_selective.py` (Nadolol, Timolol)
- `drugs/drug_modules/cardiovascular/beta_blockers/selective.py` (Acebutolol, Betaxolol)

1. **Nadolol**
   - Nhóm: Beta-blocker (non-selective)
   - Half-life dài, dùng 1 lần/ngày
   - Cần đầy đủ 14 fields

2. **Timolol**
   - Nhóm: Beta-blocker (non-selective)
   - Dùng cho tăng nhãn áp, migraine
   - Cần đầy đủ 14 fields

3. **Acebutolol**
   - Nhóm: Beta-blocker (selective)
   - Ít dùng hơn
   - Cần đầy đủ 14 fields

4. **Betaxolol**
   - Nhóm: Beta-blocker (selective)
   - Ít dùng hơn
   - Cần đầy đủ 14 fields

#### **Session 4: Cardiovascular - CCB (1 thuốc)**
**File:** `drugs/drug_modules/cardiovascular/calcium_blockers/dihydropyridines.py`

1. **Felodipine**
   - Nhóm: CCB (Dihydropyridine)
   - Ít dùng hơn
   - Cần đầy đủ 14 fields

#### **Session 5: Antibiotics - Cephalosporins (2 thuốc)**
**File:** `drugs/drug_modules/infectious_other/cephalosporins.py`

1. **Cefotetan**
   - Nhóm: Cephalosporin (2nd gen)
   - Dùng trong phẫu thuật
   - Cần đầy đủ 14 fields

2. **Cefoxitin**
   - Nhóm: Cephalosporin (2nd gen)
   - Dùng trong phẫu thuật
   - Cần đầy đủ 14 fields

---

### **Bước 2: Kiểm tra fields sau khi bổ sung**

Sau mỗi session, kiểm tra:
1. ✅ Có đủ 6 required fields không?
2. ✅ Có đủ 8 optional fields không?
3. ✅ Format đúng với schema không?
4. ✅ Nội dung đầy đủ và chính xác không?

---

## 📝 TEMPLATE CHO MỖI THUỐC

```python
"Tên Thuốc": {
    # === CÁC TRƯỜNG CƠ BẢN ===
    "group": "...",
    "vietnamese_name": "...",
    "administration": [...],
    "indications": [...],
    "contraindications": [...],
    "dosage": {...},
    "renal_adjustment": {...},
    "side_effects": [...],
    "interactions": [...],
    "pregnancy": "...",
    
    # === 6 REQUIRED FIELDS ===
    "mechanism_of_action": "...",  # 50-200 từ
    "pharmacokinetics": {
        "half_life": "...",
        "onset": "...",
        "duration": "...",
        "protein_binding": "...",
        "clearance": "..."
    },
    "monitoring": [...],
    "precautions": [...],
    "storage": "...",
    "black_box_warnings": None hoặc "...",
    
    # === 8 OPTIONAL FIELDS ===
    "drug_interactions": {
        "major": [...],
        "moderate": [...],
        "minor": [...]
    },
    "contraindications": {
        "tuyệt_đối": [...],
        "tương_đối": [...]
    },
    "pregnancy_lactation": {
        "fda_category": "...",
        "pregnancy_details": "...",
        "lactation": {
            "safety": "...",
            "details": "...",
            "recommendation": "..."
        }
    },
    "hepatic_adjustment": {
        "mild": "...",
        "moderate": "...",
        "severe": "...",
        "notes": "..."
    },
    "overdose_management": {
        "symptoms": [...],
        "antidote": "...",
        "treatment": [...],
        "monitoring": "..."
    },
    "reversal_agents": {
        "available": True/False,
        "agents": [...]
    },
    "administration_instructions": {
        "oral": {...} hoặc None,
        "iv": {...} hoặc None,
        ...
    },
    "references": {
        "primary_sources": [...],
        "last_updated": "2025-02-05",
        "evidence_level": "..."
    }
}
```

---

## ✅ CHECKLIST TIẾN ĐỘ

### **Session 1: Neurology (4 thuốc)**
- [ ] Primidone
- [ ] Zonisamide
- [ ] Lacosamide
- [ ] Perampanel

### **Session 2: Gastrointestinal (2 thuốc)**
- [ ] Sucralfate
- [ ] Misoprostol

### **Session 3: Cardiovascular - Beta-blockers (4 thuốc)**
- [ ] Nadolol
- [ ] Timolol
- [ ] Acebutolol
- [ ] Betaxolol

### **Session 4: Cardiovascular - CCB (1 thuốc)**
- [ ] Felodipine

### **Session 5: Antibiotics (2 thuốc)**
- [ ] Cefotetan
- [ ] Cefoxitin

---

## 📊 TỔNG KẾT

**Tổng số thuốc cần bổ sung:** 13  
**Số session:** 5  
**Mục tiêu:** Hoàn thành Phase 1 (30/30 thuốc)

---

**Cập nhật lần cuối:** 2025-02-05  
**Trạng thái:** 📋 Kế hoạch đã được lập, sẵn sàng bắt đầu Session 1

