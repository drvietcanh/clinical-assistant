# 📋 Danh Sách Công Việc Ưu Tiên

**Tổng số nhóm công việc:** 5

---

## 🔴 CRITICAL - Cần sửa ngay

### 1. Sửa các lỗi nghiêm trọng

**Mô tả:** Các lỗi này ảnh hưởng đến tính toàn vẹn dữ liệu

**Số lượng:** 14

**Chi tiết:**

- **Abaloparatide:**
  - ⚠️  Field rỗng: interactions
- **Alirocumab:**
  - ❌ overdose_management phải là dictionary
  - ❌ administration_instructions phải là dictionary
- **Amlodipine/Olmesartan:**
  - ⚠️  Field rỗng: interactions
- **Calcitonin:**
  - ⚠️  Field rỗng: interactions
- **Enalapril:**
  - ❌ Kiểu dữ liệu sai: guideline_tags (mong đợi list, nhận được dict)
- **Evolocumab:**
  - ❌ overdose_management phải là dictionary
  - ❌ administration_instructions phải là dictionary
- **Inclisiran:**
  - ❌ overdose_management phải là dictionary
  - ❌ administration_instructions phải là dictionary
- **Lisinopril:**
  - ❌ Kiểu dữ liệu sai: guideline_tags (mong đợi list, nhận được dict)
- **Losartan:**
  - ❌ Kiểu dữ liệu sai: guideline_tags (mong đợi list, nhận được dict)
- **Metformin:**
  - ❌ Kiểu dữ liệu sai: guideline_tags (mong đợi list, nhận được dict)

---

## 🟠 HIGH - Ưu tiên cao

### 1. Bổ sung contraindications_detail (346 thuốc)

**Mô tả:** Field quan trọng cho an toàn thuốc, thiếu nhiều nhất (52%)

**Số lượng:** 346

**Danh sách thuốc:**

- 5-Fluorouracil
- Abiraterone
- Acebutolol
- Aclidinium
- Acyclovir
- Acyclovir eye drops
- Acyclovir eye ointment
- Adalimumab
- Albendazole
- Alemtuzumab
- Alfuzosin
- Alteplase
- Anastrozole
- Anidulafungin
- Anifrolumab
- Aripiprazole
- Artemether-lumefantrine
- Artesunate
- Artificial tears (Carboxymethylcellulose)
- Aspirin

### 2. Bổ sung reversal_agents (175 thuốc)

**Mô tả:** Quan trọng cho các thuốc có antidote, đặc biệt ICU/emergency

**Số lượng:** 175

**Danh sách thuốc:**

- Abaloparatide
- Acyclovir
- Acyclovir eye drops
- Acyclovir eye ointment
- Alendronate
- Alfuzosin
- Alteplase
- Amikacin
- Amlodipine/Olmesartan
- Amlodipine/Valsartan
- Amphotericin B
- Andexanet alfa
- Anidulafungin
- Artificial tears (Carboxymethylcellulose)
- Azelaic acid topical
- Azelastine eye drops
- Bedaquiline
- Bempedoic acid
- Benzoyl peroxide topical
- Betamethasone

---

## 🟡 MEDIUM - Ưu tiên trung bình

### 1. Bổ sung black_box_warnings (138 thuốc)

**Mô tả:** Cảnh báo đặc biệt quan trọng cho an toàn

**Số lượng:** 138

**Danh sách thuốc:**

- Acarbose
- Acyclovir
- Acyclovir eye drops
- Acyclovir eye ointment
- Adenosine
- Alfuzosin
- Alogliptin
- Aluminum hydroxide/Magnesium hydroxide
- Amoxicillin suspension
- Anidulafungin
- Artificial tears (Carboxymethylcellulose)
- Atazanavir (boosted with ritonavir/cobicistat)
- Atropine
- Azelaic acid topical
- Azelastine eye drops
- Aztreonam
- Beclomethasone inhaled
- Benzoyl peroxide topical
- Betamethasone/Clotrimazole topical
- Bictegravir (BIC)

### 2. Bổ sung các enhanced fields còn lại

**Mô tả:** Các field còn thiếu để đạt >95%

**Số lượng:** 43

**Danh sách thuốc:**

- renal_adjustment: thiếu 43 thuốc (6.5%)

---
