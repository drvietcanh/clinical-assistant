# Kế Hoạch Bổ Sung 8 Fields Tùy Chọn (Phase 2)

## Tổng Quan

**Mục tiêu:** Bổ sung đầy đủ 8 fields tùy chọn cho 140 thuốc còn lại (đã có Paracetamol)
**Tổng số:** 140 thuốc
**Thời gian ước tính:** Làm theo từng nhóm, mỗi nhóm 5-10 thuốc

## 8 Fields Cần Bổ Sung

1. `drug_interactions` - Tương tác thuốc chi tiết (major, moderate, minor)
2. `contraindications` - Chống chỉ định phân loại (absolute, relative) - **CHUYỂN ĐỔI TỪ LIST SANG DICT**
3. `pregnancy_lactation` - Thai kỳ và cho con bú
4. `hepatic_adjustment` - Điều chỉnh liều suy gan
5. `overdose_management` - Xử trí quá liều
6. `reversal_agents` - Chất đối kháng
7. `administration_instructions` - Hướng dẫn dùng chi tiết
8. `references` - Tài liệu tham khảo

## Kế Hoạch Phân Nhóm

### Nhóm 1 - Thuốc Cấp Cứu & Thường Dùng (Ưu tiên cao nhất) ✅ HOÀN THÀNH
**Số lượng:** 10 thuốc (100%)
- ✅ Paracetamol
- ✅ Ibuprofen
- ✅ Salbutamol
- ✅ Adenosine
- ✅ Acyclovir
- ✅ Valacyclovir
- ✅ Methylprednisolone
- ✅ Fluconazole
- ✅ Ciprofloxacin
- ✅ Levofloxacin

### Nhóm 2 - Thuốc Có Nguy Cơ Cao (Ưu tiên cao)
**Số lượng:** 6 thuốc
- ⏳ Valproate
- ⏳ Lamotrigine
- ⏳ Amitriptyline
- ⏳ Cisplatin
- ⏳ Carboplatin
- ⏳ Cyclophosphamide

### Nhóm 3 - Antidepressants & Antihistamines (Ưu tiên trung bình)
**Số lượng:** 7 thuốc
- ⏳ Fluoxetine
- ⏳ Sertraline
- ⏳ Citalopram
- ⏳ Escitalopram
- ⏳ Loratadine
- ⏳ Cetirizine
- ⏳ Fexofenadine

### Nhóm 4 - Antidiabetics & Anticoagulants (Ưu tiên trung bình)
**Số lượng:** 8 thuốc
- ⏳ Empagliflozin
- ⏳ Dapagliflozin
- ⏳ Sitagliptin
- ⏳ Metformin
- ⏳ Gliclazide
- ⏳ Glibenclamide
- ⏳ Ticagrelor
- ⏳ Prasugrel

### Nhóm 5 - Cardiovascular Cơ Bản (Ưu tiên trung bình)
**Số lượng:** 20 thuốc
- ⏳ Captopril, Enalapril, Lisinopril
- ⏳ Losartan
- ⏳ Metoprolol, Propranolol, Atenolol, Bisoprolol, Carvedilol
- ⏳ Amlodipine, Nifedipine
- ⏳ Diltiazem, Verapamil
- ⏳ Furosemide, Hydrochlorothiazide, Spironolactone
- ⏳ Amiodarone, Digoxin
- ⏳ Warfarin, Aspirin, Clopidogrel

### Nhóm 6 - Metabolic & GI (Ưu tiên trung bình)
**Số lượng:** 15 thuốc
- ⏳ Atorvastatin, Simvastatin, Rosuvastatin
- ⏳ Insulin
- ⏳ Omeprazole, Pantoprazole, Lansoprazole, Esomeprazole
- ⏳ Ranitidine
- ⏳ Metoclopramide, Loperamide, Domperidone, Ondansetron
- ⏳ Sucralfate

### Nhóm 7 - Pain & Inflammation (Ưu tiên thấp)
**Số lượng:** 5 thuốc
- ⏳ Tramadol, Morphine, Codeine
- ⏳ Naproxen, Diclofenac

### Nhóm 8 - Respiratory & Neurology (Ưu tiên thấp)
**Số lượng:** 15 thuốc
- ⏳ Salmeterol
- ⏳ Ipratropium, Tiotropium
- ⏳ Budesonide inhaled, Fluticasone inhaled
- ⏳ Montelukast
- ⏳ Sumatriptan
- ⏳ Carbamazepine, Phenytoin, Levetiracetam
- ⏳ Prednisolone, Prednisone
- ⏳ Dexamethasone, Hydrocortisone, Betamethasone
- ⏳ Gabapentin, Pregabalin
- ⏳ Venlafaxine

### Nhóm 9 - Antimicrobial (Ưu tiên thấp)
**Số lượng:** 20 thuốc
- ⏳ Azithromycin, Doxycycline, Metronidazole
- ⏳ Amoxicillin-clavulanate, Ceftriaxone
- ⏳ Piperacillin-tazobactam, Meropenem, Clindamycin
- ⏳ Clarithromycin, Oseltamivir
- ⏳ Trimethoprim-sulfamethoxazole
- ⏳ Itraconazole, Voriconazole, Nystatin
- ⏳ Ganciclovir, Ribavirin
- ⏳ Albendazole, Mebendazole

### Nhóm 10 - Emergency & Others (Ưu tiên thấp)
**Số lượng:** 15 thuốc
- ⏳ Epinephrine, Atropine, Lidocaine
- ⏳ Naloxone, Flumazenil
- ⏳ Levothyroxine
- ⏳ Methotrexate
- ⏳ Allopurinol
- ⏳ Ticlopidine, Dipyridamole
- ⏳ Isosorbide mononitrate
- ⏳ Enalaprilat
- ⏳ Amoxicillin suspension
- ⏳ Budesonide
- ⏳ Calcium, Vitamin D, Vitamin B12, Folic Acid, Iron

### Nhóm 11 - Các Thuốc Khác (Ưu tiên thấp nhất)
**Số lượng:** 19 thuốc
- Các thuốc còn lại

## Tiến Trình

### ✅ Hoàn thành
- **Nhóm 1 - HOÀN THÀNH 100% (10/10 thuốc):** Paracetamol, Ibuprofen, Salbutamol, Adenosine, Acyclovir, Valacyclovir, Methylprednisolone, Fluconazole, Ciprofloxacin, Levofloxacin
- **Tổng số:** 10/141 thuốc (7%)

### ⏳ Đang làm
- Tiếp theo: Nhóm 2 - Thuốc Có Nguy Cơ Cao

### 📋 Kế hoạch tiếp theo
1. ✅ Nhóm 1 (10/10 thuốc) - HOÀN THÀNH
2. ⏳ Nhóm 2 (6 thuốc): Valproate, Lamotrigine, Amitriptyline, Cisplatin, Carboplatin, Cyclophosphamide
3. Nhóm 3 (7 thuốc)
4. Nhóm 4 (8 thuốc)
5. Các nhóm tiếp theo...

## Lưu Ý Khi Bổ Sung

1. **contraindications**: Chuyển đổi từ list sang dict với `absolute` và `relative`
2. **drug_interactions**: Phân loại major, moderate, minor với đầy đủ mechanism, effect, management
3. **overdose_management**: Chỉ bổ sung cho thuốc có nguy cơ quá liều cao
4. **reversal_agents**: Chỉ bổ sung khi có antidote (N-acetylcysteine, naloxone, flumazenil, etc.)
5. **references**: Luôn cập nhật last_updated và evidence_level

## Template

Xem `drugs/enhanced_fields_schema.py` để lấy template và ví dụ từ Paracetamol.

