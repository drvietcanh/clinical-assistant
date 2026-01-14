# 📋 Kế Hoạch Bổ sung Thuốc Mới - Drug Database Expansion

**Ngày tạo:** 2025-02-04  
**Hiện trạng:** 74 thuốc  
**Mục tiêu:** 150-200 thuốc phổ biến tại Việt Nam  
**Version:** 2.17.0

---

## 📊 HIỆN TRẠNG

### **Số lượng thuốc hiện tại:**
- **Tổng số:** 74 thuốc
- **Đã có Enhanced Fields (6 fields cơ bản):** 74/74 (100%)
- **Đã có Enhanced Fields (14 fields đầy đủ):** ~70/74 (94.6%)

### **Phân bố theo nhóm:**
- Cardiovascular: 30 thuốc
- Diabetes: 9 thuốc
- Gastrointestinal: 10 thuốc
- Oncology: 10 thuốc
- Emergency: 7 thuốc
- Antibiotics: 9 thuốc
- Pediatric: 6 thuốc
- Analgesics: 8 thuốc
- Respiratory: 7 thuốc
- Neurology/Psychiatry: 13 thuốc
- Allergy: 5 thuốc
- Vitamins/Supplements: 5 thuốc
- Anti-infectives: 4 thuốc
- Endocrinology: 4 thuốc
- Other: 2 thuốc

---

## 🎯 MỤC TIÊU

### **Mục tiêu tổng thể:**
- **Giai đoạn 1:** 74 → 100 thuốc (+26 thuốc)
- **Giai đoạn 2:** 100 → 150 thuốc (+50 thuốc)
- **Giai đoạn 3:** 150 → 200 thuốc (+50 thuốc)

### **Ưu tiên:**
1. 🔥 **Cao nhất:** Thuốc cấp cứu, thường dùng, có nguy cơ cao
2. 🔥 **Cao:** Thuốc theo chuyên khoa quan trọng
3. ⚡ **Trung bình:** Thuốc bổ sung cho đầy đủ nhóm
4. 📋 **Thấp:** Thuốc ít dùng, bổ sung sau

---

## 📋 KẾ HOẠCH CHI TIẾT

### **GIAI ĐOẠN 1: Bổ sung 26 Thuốc (74 → 100)**

#### **Nhóm 1: Thuốc Cấp cứu & Thường Dùng (Ưu tiên cao nhất)** 🔥🔥🔥

**Mục tiêu:** 10 thuốc

1. ✅ **Paracetamol** (Acetaminophen)
   - **Lý do:** Thuốc giảm đau/hạ sốt phổ biến nhất
   - **Nhóm:** Analgesic/Antipyretic
   - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

2. ✅ **Ibuprofen**
   - **Lý do:** NSAID thường dùng
   - **Nhóm:** Analgesic/NSAID
   - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

3. ✅ **Salbutamol** (Albuterol)
   - **Lý do:** Thuốc cấp cứu hen suyễn
   - **Nhóm:** Respiratory/Bronchodilator
   - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

4. ✅ **Adenosine**
   - **Lý do:** Cấp cứu tim mạch (SVT)
   - **Nhóm:** Emergency/Antiarrhythmic
   - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

5. ✅ **Methylprednisolone**
   - **Lý do:** Corticosteroid cấp cứu
   - **Nhóm:** Emergency/Corticosteroid
   - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

6. ✅ **Acyclovir**
   - **Lý do:** Antiviral quan trọng
   - **Nhóm:** Antimicrobial/Antiviral
   - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

7. ✅ **Valacyclovir**
   - **Lý do:** Antiviral (prodrug của Acyclovir)
   - **Nhóm:** Antimicrobial/Antiviral
   - **Ưu tiên:** 🔥🔥 CAO

8. ✅ **Fluconazole**
   - **Lý do:** Antifungal thường dùng
   - **Nhóm:** Antimicrobial/Antifungal
   - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

9. ✅ **Ciprofloxacin**
   - **Lý do:** Kháng sinh phổ biến
   - **Nhóm:** Antimicrobial/Antibiotic
   - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

10. ✅ **Levofloxacin**
    - **Lý do:** Kháng sinh phổ biến
    - **Nhóm:** Antimicrobial/Antibiotic
    - **Ưu tiên:** 🔥🔥🔥 CAO NHẤT

**Trạng thái:** ✅ Đã có trong enhanced fields progress (có thể đã có trong DB)

---

#### **Nhóm 2: Thuốc Có Nguy cơ Cao (Ưu tiên cao)** 🔥🔥

**Mục tiêu:** 6 thuốc

1. ✅ **Valproate** (Valproic acid)
   - **Lý do:** Cần theo dõi chặt chẽ (độc tính gan, dị tật thai)
   - **Nhóm:** Neurology/Anticonvulsant
   - **Ưu tiên:** 🔥🔥 CAO

2. ✅ **Lamotrigine**
   - **Lý do:** Hội chứng Stevens-Johnson
   - **Nhóm:** Neurology/Anticonvulsant
   - **Ưu tiên:** 🔥🔥 CAO

3. ✅ **Amitriptyline**
   - **Lý do:** Antidepressant, quá liều nguy hiểm
   - **Nhóm:** Psychiatry/Antidepressant
   - **Ưu tiên:** 🔥🔥 CAO

4. ✅ **Cisplatin**
   - **Lý do:** Chemotherapy, độc tính cao
   - **Nhóm:** Oncology/Chemotherapy
   - **Ưu tiên:** 🔥🔥 CAO

5. ✅ **Carboplatin**
   - **Lý do:** Chemotherapy, độc tính cao
   - **Nhóm:** Oncology/Chemotherapy
   - **Ưu tiên:** 🔥🔥 CAO

6. ✅ **Cyclophosphamide**
   - **Lý do:** Immunosuppressant, độc tính
   - **Nhóm:** Oncology/Immunosuppressant
   - **Ưu tiên:** 🔥🔥 CAO

**Trạng thái:** ✅ Đã có trong enhanced fields progress

---

#### **Nhóm 3: Thuốc Thường Dùng - Antidepressants (Ưu tiên cao)** 🔥🔥

**Mục tiêu:** 4 thuốc

1. ✅ **Fluoxetine**
   - **Lý do:** SSRI phổ biến nhất
   - **Nhóm:** Psychiatry/SSRI
   - **Ưu tiên:** 🔥🔥 CAO

2. ✅ **Sertraline**
   - **Lý do:** SSRI phổ biến
   - **Nhóm:** Psychiatry/SSRI
   - **Ưu tiên:** 🔥🔥 CAO

3. ✅ **Citalopram**
   - **Lý do:** SSRI phổ biến
   - **Nhóm:** Psychiatry/SSRI
   - **Ưu tiên:** 🔥🔥 CAO

4. ✅ **Escitalopram**
   - **Lý do:** SSRI (enantiomer của Citalopram)
   - **Nhóm:** Psychiatry/SSRI
   - **Ưu tiên:** 🔥🔥 CAO

**Trạng thái:** ✅ Đã có trong enhanced fields progress

---

#### **Nhóm 4: Thuốc Thường Dùng - Antihistamines (Ưu tiên trung bình)** ⚡

**Mục tiêu:** 3 thuốc

1. ✅ **Loratadine**
   - **Lý do:** Antihistamine thế hệ 2
   - **Nhóm:** Allergy/Antihistamine
   - **Ưu tiên:** ⚡ TRUNG BÌNH

2. ✅ **Cetirizine**
   - **Lý do:** Antihistamine thế hệ 2
   - **Nhóm:** Allergy/Antihistamine
   - **Ưu tiên:** ⚡ TRUNG BÌNH

3. ✅ **Fexofenadine**
   - **Lý do:** Antihistamine thế hệ 2
   - **Nhóm:** Allergy/Antihistamine
   - **Ưu tiên:** ⚡ TRUNG BÌNH

**Trạng thái:** ✅ Đã có trong enhanced fields progress

---

#### **Nhóm 5: Thuốc Thường Dùng - Antidiabetics (Ưu tiên trung bình)** ⚡

**Mục tiêu:** 3 thuốc

1. ✅ **Empagliflozin**
   - **Lý do:** SGLT2 inhibitor
   - **Nhóm:** Diabetes/SGLT2 inhibitor
   - **Ưu tiên:** ⚡ TRUNG BÌNH

2. ✅ **Dapagliflozin**
   - **Lý do:** SGLT2 inhibitor
   - **Nhóm:** Diabetes/SGLT2 inhibitor
   - **Ưu tiên:** ⚡ TRUNG BÌNH

3. ✅ **Sitagliptin**
   - **Lý do:** DPP-4 inhibitor
   - **Nhóm:** Diabetes/DPP-4 inhibitor
   - **Ưu tiên:** ⚡ TRUNG BÌNH

**Trạng thái:** ✅ Đã có trong database (9 thuốc diabetes)

---

### **GIAI ĐOẠN 2: Bổ sung 50 Thuốc (100 → 150)**

#### **Nhóm 6: Kháng sinh Bổ sung (Ưu tiên cao)** 🔥🔥

**Mục tiêu:** 10 thuốc

1. **Clarithromycin**
   - **Lý do:** Macrolide phổ biến
   - **Nhóm:** Antimicrobial/Macrolide
   - **Ưu tiên:** 🔥🔥 CAO

2. **Azithromycin**
   - **Lý do:** Macrolide phổ biến
   - **Nhóm:** Antimicrobial/Macrolide
   - **Ưu tiên:** 🔥🔥 CAO

3. **Trimethoprim-sulfamethoxazole** (Co-trimoxazole)
   - **Lý do:** Kháng sinh phổ biến
   - **Nhóm:** Antimicrobial/Sulfonamide
   - **Ưu tiên:** 🔥🔥 CAO

4. **Oseltamivir**
   - **Lý do:** Antiviral (influenza)
   - **Nhóm:** Antimicrobial/Antiviral
   - **Ưu tiên:** 🔥🔥 CAO

5. **Ganciclovir**
   - **Lý do:** Antiviral (CMV)
   - **Nhóm:** Antimicrobial/Antiviral
   - **Ưu tiên:** 🔥 CAO

6. **Itraconazole**
   - **Lý do:** Antifungal
   - **Nhóm:** Antimicrobial/Antifungal
   - **Ưu tiên:** 🔥 CAO

7. **Voriconazole**
   - **Lý do:** Antifungal
   - **Nhóm:** Antimicrobial/Antifungal
   - **Ưu tiên:** 🔥 CAO

8. **Nystatin**
   - **Lý do:** Antifungal (topical)
   - **Nhóm:** Antimicrobial/Antifungal
   - **Ưu tiên:** ⚡ TRUNG BÌNH

9. **Ribavirin**
   - **Lý do:** Antiviral (HCV)
   - **Nhóm:** Antimicrobial/Antiviral
   - **Ưu tiên:** ⚡ TRUNG BÌNH

10. **Chloroquine / Artesunate**
    - **Lý do:** Antimalarial
    - **Nhóm:** Antimicrobial/Antimalarial
    - **Ưu tiên:** ⚡ TRUNG BÌNH

---

#### **Nhóm 7: Tim mạch Bổ sung (Ưu tiên trung bình)** ⚡

**Mục tiêu:** 5 thuốc

1. **Ticagrelor**
   - **Lý do:** Antiplatelet mới
   - **Nhóm:** Cardiovascular/Antiplatelet
   - **Ưu tiên:** ⚡ TRUNG BÌNH

2. **Prasugrel**
   - **Lý do:** Antiplatelet mới
   - **Nhóm:** Cardiovascular/Antiplatelet
   - **Ưu tiên:** ⚡ TRUNG BÌNH

3. **Ticlopidine**
   - **Lý do:** Antiplatelet
   - **Nhóm:** Cardiovascular/Antiplatelet
   - **Ưu tiên:** ⚡ TRUNG BÌNH

4. **Dipyridamole**
   - **Lý do:** Antiplatelet
   - **Nhóm:** Cardiovascular/Antiplatelet
   - **Ưu tiên:** ⚡ TRUNG BÌNH

5. **Isosorbide mononitrate**
   - **Lý do:** Nitrate
   - **Nhóm:** Cardiovascular/Nitrate
   - **Ưu tiên:** ⚡ TRUNG BÌNH

---

#### **Nhóm 8: Thần kinh & Tâm Thần Bổ sung (Ưu tiên trung bình)** ⚡

**Mục tiêu:** 8 thuốc

1. **Gabapentin**
   - **Lý do:** Anticonvulsant, neuropathic pain
   - **Nhóm:** Neurology/Anticonvulsant
   - **Ưu tiên:** ⚡ TRUNG BÌNH

2. **Pregabalin**
   - **Lý do:** Anticonvulsant, neuropathic pain
   - **Nhóm:** Neurology/Anticonvulsant
   - **Ưu tiên:** ⚡ TRUNG BÌNH

3. **Venlafaxine**
   - **Lý do:** SNRI
   - **Nhóm:** Psychiatry/SNRI
   - **Ưu tiên:** ⚡ TRUNG BÌNH

4. **Desloratadine**
   - **Lý do:** Antihistamine
   - **Nhóm:** Allergy/Antihistamine
   - **Ưu tiên:** ⚡ TRUNG BÌNH

5. **Levocetirizine**
   - **Lý do:** Antihistamine
   - **Nhóm:** Allergy/Antihistamine
   - **Ưu tiên:** ⚡ TRUNG BÌNH

6. **Phenytoin**
   - **Lý do:** Anticonvulsant cổ điển
   - **Nhóm:** Neurology/Anticonvulsant
   - **Ưu tiên:** ⚡ TRUNG BÌNH

7. **Levetiracetam**
   - **Lý do:** Anticonvulsant mới
   - **Nhóm:** Neurology/Anticonvulsant
   - **Ưu tiên:** ⚡ TRUNG BÌNH

8. **Carbamazepine**
   - **Lý do:** Anticonvulsant cổ điển
   - **Nhóm:** Neurology/Anticonvulsant
   - **Ưu tiên:** ⚡ TRUNG BÌNH

---

#### **Nhóm 9: Hô hấp Bổ sung (Ưu tiên trung bình)** ⚡

**Mục tiêu:** 5 thuốc

1. **Salmeterol**
   - **Lý do:** LABA
   - **Nhóm:** Respiratory/LABA
   - **Ưu tiên:** ⚡ TRUNG BÌNH

2. **Ipratropium**
   - **Lý do:** SAMA
   - **Nhóm:** Respiratory/Anticholinergic
   - **Ưu tiên:** ⚡ TRUNG BÌNH

3. **Tiotropium**
   - **Lý do:** LAMA
   - **Nhóm:** Respiratory/Anticholinergic
   - **Ưu tiên:** ⚡ TRUNG BÌNH

4. **Montelukast**
   - **Lý do:** Leukotriene receptor antagonist
   - **Nhóm:** Respiratory/Antileukotriene
   - **Ưu tiên:** ⚡ TRUNG BÌNH

5. **Budesonide inhaled / Fluticasone inhaled**
   - **Lý do:** Inhaled corticosteroid
   - **Nhóm:** Respiratory/ICS
   - **Ưu tiên:** ⚡ TRUNG BÌNH

---

#### **Nhóm 10: Tiêu hóa Bổ sung (Ưu tiên trung bình)** ⚡

**Mục tiêu:** 5 thuốc

1. **Lansoprazole**
   - **Lý do:** PPI
   - **Nhóm:** Gastrointestinal/PPI
   - **Ưu tiên:** ⚡ TRUNG BÌNH

2. **Esomeprazole**
   - **Lý do:** PPI
   - **Nhóm:** Gastrointestinal/PPI
   - **Ưu tiên:** ⚡ TRUNG BÌNH

3. **Ranitidine**
   - **Lý do:** H2 blocker
   - **Nhóm:** Gastrointestinal/H2 blocker
   - **Ưu tiên:** ⚡ TRUNG BÌNH

4. **Domperidone**
   - **Lý do:** Prokinetic
   - **Nhóm:** Gastrointestinal/Prokinetic
   - **Ưu tiên:** ⚡ TRUNG BÌNH

5. **Loperamide**
   - **Lý do:** Antidiarrheal
   - **Nhóm:** Gastrointestinal/Antidiarrheal
   - **Ưu tiên:** ⚡ TRUNG BÌNH

---

#### **Nhóm 11: Ung thư Bổ sung (Ưu tiên trung bình)** ⚡

**Mục tiêu:** 5 thuốc

1. **Oxaliplatin**
   - **Lý do:** Platinum compound
   - **Nhóm:** Oncology/Platinum
   - **Ưu tiên:** ⚡ TRUNG BÌNH

2. **5-Fluorouracil (5-FU)**
   - **Lý do:** Antimetabolite
   - **Nhóm:** Oncology/Antimetabolite
   - **Ưu tiên:** ⚡ TRUNG BÌNH

3. **Ifosfamide**
   - **Lý do:** Alkylating agent
   - **Nhóm:** Oncology/Alkylating
   - **Ưu tiên:** ⚡ TRUNG BÌNH

4. **Doxorubicin**
   - **Lý do:** Anthracycline
   - **Nhóm:** Oncology/Anthracycline
   - **Ưu tiên:** ⚡ TRUNG BÌNH

5. **Granisetron / Palonosetron**
   - **Lý do:** Antiemetic (5-HT3 antagonist)
   - **Nhóm:** Oncology/Antiemetic
   - **Ưu tiên:** ⚡ TRUNG BÌNH

---

#### **Nhóm 12: Nội tiết & Khác (Ưu tiên thấp)** 📋

**Mục tiêu:** 12 thuốc

1. **Levothyroxine**
   - **Lý do:** Thyroid hormone
   - **Nhóm:** Endocrinology/Thyroid
   - **Ưu tiên:** 📋 THẤP

2. **Methimazole**
   - **Lý do:** Antithyroid
   - **Nhóm:** Endocrinology/Antithyroid
   - **Ưu tiên:** 📋 THẤP

3. **Propylthiouracil**
   - **Lý do:** Antithyroid
   - **Nhóm:** Endocrinology/Antithyroid
   - **Ưu tiên:** 📋 THẤP

4. **Methotrexate**
   - **Lý do:** Immunosuppressant, chemotherapy
   - **Nhóm:** Rheumatology/Immunosuppressant
   - **Ưu tiên:** 📋 THẤP

5. **Allopurinol**
   - **Lý do:** Xanthine oxidase inhibitor (gout)
   - **Nhóm:** Metabolic/Gout
   - **Ưu tiên:** 📋 THẤP

6. **Atropine**
   - **Lý do:** Anticholinergic
   - **Nhóm:** Emergency/Anticholinergic
   - **Ưu tiên:** 📋 THẤP

7. **Enalaprilat**
   - **Lý do:** ACE inhibitor (IV)
   - **Nhóm:** Cardiovascular/ACE inhibitor
   - **Ưu tiên:** 📋 THẤP

8. **Amoxicillin suspension**
   - **Lý do:** Pediatric formulation
   - **Nhóm:** Pediatric/Antibiotic
   - **Ưu tiên:** 📋 THẤP

9. **Budesonide**
   - **Lý do:** Corticosteroid
   - **Nhóm:** Respiratory/Corticosteroid
   - **Ưu tiên:** 📋 THẤP

10. **Albendazole / Mebendazole**
    - **Lý do:** Anthelmintic
    - **Nhóm:** Antimicrobial/Anthelmintic
    - **Ưu tiên:** 📋 THẤP

11. **Calcium / Vitamin D / Vitamin B12 / Folic Acid / Iron**
    - **Lý do:** Vitamins & Supplements
    - **Nhóm:** Supportive/Vitamins
    - **Ưu tiên:** 📋 THẤP

12. **Sumatriptan**
    - **Lý do:** Antimigraine
    - **Nhóm:** Neurology/Antimigraine
    - **Ưu tiên:** 📋 THẤP

---

### **GIAI ĐOẠN 3: Bổ sung 50 Thuốc (150 → 200)**

#### **Nhóm 13-20: Các Nhóm Bổ sung**

**Mục tiêu:** 50 thuốc

- **Antibiotics bổ sung:** 10 thuốc
- **Cardiovascular bổ sung:** 8 thuốc
- **Neurology/Psychiatry bổ sung:** 8 thuốc
- **Respiratory bổ sung:** 5 thuốc
- **Gastrointestinal bổ sung:** 5 thuốc
- **Oncology bổ sung:** 5 thuốc
- **Emergency bổ sung:** 4 thuốc
- **Other:** 5 thuốc

---

## 📝 TEMPLATE THÊM THUỐC MỚI

### **Cấu trúc dữ liệu:**

```python
"Tên Thuốc": {
    "name": "Tên Thuốc",
    "generic_name": "Tên chung",
    "brand_names": ["Biệt dược 1", "Biệt dược 2"],
    "group": "Nhóm thuốc",
    "category": "Phân loại",
    "indications": ["Chỉ định 1", "Chỉ định 2"],
    "contraindications": ["Chống chỉ định 1"],
    "dosage": {
        "adult": {
            "oral": "Liều uống",
            "iv": "Liều tiêm tĩnh mạch",
            "im": "Liều tiêm bắp"
        },
        "pediatric": {
            "oral": "Liều uống trẻ em",
            "iv": "Liều tiêm tĩnh mạch trẻ em"
        }
    },
    "renal_adjustment": {
        "crcl_30_50": "Điều chỉnh CrCl 30-50",
        "crcl_10_30": "Điều chỉnh CrCl 10-30",
        "crcl_<10": "Điều chỉnh CrCl <10"
    },
    "side_effects": ["Tác dụng phụ 1", "Tác dụng phụ 2"],
    "interactions": ["Tương tác 1", "Tương tác 2"],
    "notes": "Ghi chú",
    "enhanced_fields": {
        "mechanism_of_action": "...",
        "monitoring": "...",
        "precautions": "...",
        "pharmacokinetics": "...",
        "storage": "...",
        "black_box_warnings": "...",
        # ... 8 fields tùy chọn
    }
}
```

---

## 🛠️ QUY TRÌNH THÊM THUỐC

### **Bước 1: Chuẩn bị thông tin**
1. Thu thập thông tin từ:
   - FDA Drug Labels
   - UpToDate, Medscape
   - Goodman & Gilman, Katzung
   - Clinical guidelines
   - Vietnamese drug database

### **Bước 2: Xác định file module**
- Xác định nhóm thuốc
- Tìm file module tương ứng trong `drugs/drug_modules/`
- Nếu chưa có, tạo file mới hoặc thêm vào `other.py`

### **Bước 3: Thêm dữ liệu**
1. Mở file module tương ứng
2. Thêm thuốc vào dictionary
3. Đảm bảo format đúng
4. Thêm enhanced_fields (6 fields cơ bản)

### **Bước 4: Cập nhật DRUG_GROUPS**
- Mở `drugs/drug_utils/groups.py`
- Thêm thuốc vào nhóm tương ứng

### **Bước 5: Validate**
```bash
python check_enhanced_fields.py
python -c "from drugs.drug_database import DRUG_DATABASE; print(len(DRUG_DATABASE))"
```

### **Bước 6: Test**
- Test search functionality
- Test display drug info
- Test enhanced fields display

---

## 📊 THEO DÕI TIẾN TRÌNH

### **Script theo dõi:**
```bash
# Kiểm tra số lượng thuốc
python -c "from drugs.drug_database import TOTAL_DRUGS; print(f'Total: {TOTAL_DRUGS}')"

# Kiểm tra enhanced fields
python check_enhanced_fields.py

# Kiểm tra theo nhóm
python -c "from drugs.drug_utils import DRUG_GROUPS; [print(f'{g}: {len(d)}') for g, d in DRUG_GROUPS.items()]"
```

### **File theo dõi:**
- `drugs/DRUG_EXPANSION_PLAN.md` - Kế hoạch này
- `drugs/ENHANCED_FIELDS_PROGRESS.md` - Tiến trình enhanced fields
- `drugs/PHASE2_PLAN.md` - Kế hoạch Phase 2

---

## ✅ CHECKLIST THÊM THUỐC MỚI

- [ ] Thu thập đầy đủ thông tin
- [ ] Xác định file module
- [ ] Thêm vào dictionary
- [ ] Thêm enhanced_fields (6 fields cơ bản)
- [ ] Cập nhật DRUG_GROUPS
- [ ] Validate format
- [ ] Test search
- [ ] Test display
- [ ] Cập nhật documentation
- [ ] Commit changes

---

## 🎯 KẾ HOẠCH THỰC HIỆN

### **Tuần 1-2: Giai đoạn 1 (26 thuốc)**
- Nhóm 1: 10 thuốc cấp cứu
- Nhóm 2: 6 thuốc nguy cơ cao
- Nhóm 3: 4 thuốc antidepressants
- Nhóm 4: 3 thuốc antihistamines
- Nhóm 5: 3 thuốc antidiabetics

### **Tuần 3-6: Giai đoạn 2 (50 thuốc)**
- Nhóm 6: 10 thuốc kháng sinh
- Nhóm 7: 5 thuốc tim mạch
- Nhóm 8: 8 thuốc thần kinh
- Nhóm 9: 5 thuốc hô hấp
- Nhóm 10: 5 thuốc tiêu hóa
- Nhóm 11: 5 thuốc ung thư
- Nhóm 12: 12 thuốc nội tiết & khác

### **Tuần 7-10: Giai đoạn 3 (50 thuốc)**
- Các nhóm bổ sung

---

## 📝 GHI CHÚ

- **Ưu tiên chất lượng hơn số lượng:** Đảm bảo thông tin chính xác
- **Làm từng nhóm:** Hoàn thành từng nhóm trước khi chuyển sang nhóm khác
- **Validate thường xuyên:** Chạy validation sau mỗi nhóm
- **Cập nhật documentation:** Cập nhật file này sau mỗi nhóm hoàn thành

---

**Cập nhật lần cuối:** 2025-02-04  
**Trạng thái:** 📋 Kế hoạch đã sẵn sàng  
**Bước tiếp theo:** Bắt đầu Giai đoạn 1 - Nhóm 1 (Thuốc cấp cứu)

