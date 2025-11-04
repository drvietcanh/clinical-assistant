---

## Ưu Tiên Bổ Sung (Đề Xuất)

### Nhóm 1 - Thuốc Cấp Cứu & Thường Dùng (Ưu tiên cao)
- Paracetamol (thuốc giảm đau phổ biến nhất)
- Ibuprofen (NSAID thường dùng)
- Salbutamol (thuốc cấp cứu hen suyễn)
- Adenosine (cấp cứu tim mạch)
- Methylprednisolone (corticosteroid cấp cứu)
- Acyclovir, Valacyclovir (antiviral quan trọng)
- Fluconazole (antifungal thường dùng)
- Ciprofloxacin, Levofloxacin (kháng sinh phổ biến)

### Nhóm 2 - Thuốc Có Nguy Cơ Cao (Ưu tiên cao)
- Valproate (cần theo dõi chặt chẽ)
- Lamotrigine (hội chứng Stevens-Johnson)
- Amitriptyline (antidepressant, quá liều nguy hiểm)
- Cisplatin, Carboplatin (chemotherapy, độc tính cao)
- Cyclophosphamide (immunosuppressant, độc tính)

### Nhóm 3 - Thuốc Thường Dùng (Ưu tiên trung bình)
- Antidepressants: Fluoxetine, Sertraline, Citalopram, Escitalopram
- Antihistamines: Loratadine, Cetirizine, Fexofenadine
- Antidiabetics: Empagliflozin, Dapagliflozin, Sitagliptin
- Anticoagulants: Ticagrelor, Prasugrel

### Nhóm 4 - Thuốc Khác (Ưu tiên thấp)
- Vitamins & supplements
- Thuốc ít dùng hơn

---

# Tiến Trình Bổ Sung Enhanced Fields

## Tổng Quan

**Tổng số thuốc:** 141  
**Đã có enhanced fields (6 fields cơ bản):** 112 ✅ (+36 từ các phiên này)  
**Chưa có enhanced fields:** 29  
**Mục tiêu:** Bổ sung đầy đủ 14 fields cho tất cả 141 thuốc

### Tiến Trình Gần Đây (2024-12-19)
- ✅ **Nhóm 1 - Thuốc Cấp Cứu & Thường Dùng**: 10 thuốc
  - Adenosine, Acyclovir, Methylprednisolone, Valacyclovir, Fluconazole, Levofloxacin
  - **Paracetamol, Ibuprofen, Salbutamol, Ciprofloxacin** (mới bổ sung)
- ✅ **Nhóm 3 - Kháng sinh & Antiviral**: 3 thuốc
  - **Clarithromycin, Oseltamivir, Trimethoprim-sulfamethoxazole** (mới bổ sung)
- ✅ **Nhóm 4 - Respiratory & Neurology**: 7 thuốc
  - **Budesonide inhaled, Montelukast, Fluticasone inhaled** (respiratory)
  - **Gabapentin, Pregabalin, Glibenclamide** (neurology/diabetes)
  - **Venlafaxine** (psychiatry/SNRI)
- ✅ **Nhóm 5 - Antifungal & Antiviral & Cardiovascular**: 4 thuốc
  - **Itraconazole, Voriconazole** (antifungal)
  - **Ganciclovir** (antiviral)
  - **Isosorbide mononitrate** (cardiovascular) (mới bổ sung)
- ✅ **Nhóm 2 - Thuốc Có Nguy Cơ Cao**: 6 thuốc
  - Valproate, Lamotrigine, Amitriptyline, Cisplatin, Carboplatin, Cyclophosphamide
- ✅ **Nhóm 3 - Antidepressants**: 4 thuốc
  - Fluoxetine, Sertraline, Citalopram, Escitalopram

## Schema Enhanced Fields (14 Fields)

### 6 Fields Cơ Bản (Bắt Buộc)
1. ✅ `mechanism_of_action` - Cơ chế tác dụng
2. ✅ `monitoring` - Các thông số cần theo dõi
3. ✅ `precautions` - Lưu ý và thận trọng
4. ✅ `pharmacokinetics` - Thông tin dược động học
5. ✅ `storage` - Điều kiện bảo quản
6. ✅ `black_box_warnings` - Cảnh báo hộp đen

### 8 Fields Bổ Sung (Tùy Chọn)
7. `drug_interactions` - Tương tác thuốc chi tiết
8. `contraindications` - Chống chỉ định phân loại
9. `pregnancy_lactation` - Thai kỳ và cho con bú
10. `hepatic_adjustment` - Điều chỉnh liều suy gan
11. `overdose_management` - Xử trí quá liều
12. `reversal_agents` - Chất đối kháng
13. `administration_instructions` - Hướng dẫn dùng chi tiết
14. `references` - Tài liệu tham khảo

## Danh Sách Thuốc Đã Có Enhanced Fields (112 thuốc)

### ✅ Mới Bổ Sung (36 thuốc - 2024-12-19)
- **Emergency/Cấp Cứu**: Adenosine
- **Antiviral**: Acyclovir, Valacyclovir
- **Corticosteroid**: Methylprednisolone
- **Antifungal**: Fluconazole
- **Antibiotics**: Levofloxacin
- **Analgesics/Antipyretics**: **Paracetamol, Ibuprofen** (mới bổ sung)
- **Respiratory**: **Salbutamol** (mới bổ sung)
- **Antibiotics (Fluoroquinolone)**: **Ciprofloxacin** (mới bổ sung)
- **Antibiotics (Macrolide)**: **Clarithromycin** (mới bổ sung)
- **Antibiotics (Sulfonamide)**: **Trimethoprim-sulfamethoxazole** (mới bổ sung)
- **Antiviral**: **Oseltamivir** (mới bổ sung)
- **Respiratory**: **Budesonide inhaled, Montelukast, Fluticasone inhaled** (mới bổ sung)
- **Neurology**: **Gabapentin, Pregabalin** (mới bổ sung)
- **Diabetes**: **Glibenclamide** (mới bổ sung)
- **Psychiatry (SNRI)**: **Venlafaxine** (mới bổ sung)
- **Antifungal**: **Itraconazole, Voriconazole** (mới bổ sung)
- **Antiviral**: **Ganciclovir** (mới bổ sung)
- **Cardiovascular (Nitrate)**: **Isosorbide mononitrate** (mới bổ sung)
- **Neurology**: Valproate, Lamotrigine
- **Psychiatry**: Amitriptyline, Fluoxetine, Sertraline, Citalopram, Escitalopram
- **Oncology**: Cisplatin, Carboplatin, Cyclophosphamide

### ✅ Đã Có Sẵn (70 thuốc)

### Cardiovascular
- Captopril, Enalapril, Lisinopril
- Losartan
- Metoprolol, Propranolol, Atenolol, Bisoprolol, Carvedilol
- Amlodipine, Nifedipine
- Diltiazem, Verapamil
- Furosemide, Hydrochlorothiazide, Spironolactone
- Amiodarone, Digoxin
- Warfarin, Aspirin, Clopidogrel

### Metabolic
- Atorvastatin, Simvastatin, Rosuvastatin
- Metformin, Gliclazide
- Insulin

### GI
- Omeprazole, Pantoprazole, Lansoprazole, Esomeprazole
- Ranitidine
- Metoclopramide, Loperamide, Domperidone, Ondansetron
- Sucralfate

### Pain & Inflammation
- Tramadol, Morphine, Codeine
- Naproxen, Diclofenac

### Respiratory
- Salmeterol
- Ipratropium, Tiotropium
- Sumatriptan

### Neurological
- Carbamazepine, Phenytoin, Levetiracetam
- Prednisolone, Prednisone
- Dexamethasone, Hydrocortisone, Betamethasone

### Antimicrobial
- Azithromycin, Doxycycline, Metronidazole
- Amoxicillin-clavulanate, Ceftriaxone
- Piperacillin-tazobactam, Meropenem, Clindamycin

### Others
- Levothyroxine
- Methotrexate
- Allopurinol
- Epinephrine, Atropine, Lidocaine
- Naloxone, Flumazenil

---

## Danh Sách Thuốc CẦN Bổ Sung Enhanced Fields (71 thuốc)

### ✅ Hoàn thành (70/141 thuốc)
- Cardiovascular cơ bản
- GI cơ bản
- Pain & Inflammation cơ bản
- Antimicrobial cơ bản
- Corticosteroids cơ bản

### 🔄 Đang làm
- Chưa bắt đầu

### 📋 Kế hoạch
- Phase 1: Bổ sung 6 fields cơ bản cho 71 thuốc còn lại
- Phase 2: Bổ sung 8 fields tùy chọn cho tất cả 141 thuốc

---

## Cách Tiếp Tục

### Bước 1: Chọn thuốc cần bổ sung
```python
# Xem danh sách thuốc chưa có enhanced fields
python -c "from drugs.drug_database import DRUG_DATABASE; drugs_without = [name for name, data in DRUG_DATABASE.items() if 'mechanism_of_action' not in data and 'enhanced_fields' not in data]; print('\n'.join(drugs_without))"
```

### Bước 2: Tạo enhanced fields
1. Import template:
```python
from drugs.enhanced_fields_schema import create_enhanced_fields_template
template = create_enhanced_fields_template()
```

2. Điền thông tin cho từng field dựa trên:
   - FDA Drug Labels
   - UpToDate, Medscape
   - Goodman & Gilman, Katzung
   - Clinical guidelines

### Bước 3: Validate
```python
from drugs.enhanced_fields_schema import validate_enhanced_fields
is_valid, errors = validate_enhanced_fields("Tên thuốc", enhanced_fields)
```

### Bước 4: Thêm vào database
- Mở `drugs/drug_database.py`
- Tìm thuốc và thêm `"enhanced_fields": {...}`

### Bước 5: Kiểm tra lại
```bash
python check_enhanced_fields.py
```

---

## Files Tham Khảo

- **Schema:** `drugs/enhanced_fields_schema.py`
- **Template:** `create_enhanced_fields_template()`
- **Validation:** `validate_enhanced_fields()`
- **Examples:** `EXAMPLE_ENHANCED_FIELDS` trong schema file
- **Comparison:** `drugs/ENHANCED_FIELDS_COMPARISON.md`
- **Guidelines:** `drugs/ENHANCED_FIELDS_README.md`

---

## Ghi Chú

- Làm lần lượt từng thuốc, đảm bảo chất lượng
- Validate trước khi commit
- Cập nhật file này sau mỗi lần hoàn thành một nhóm thuốc
- Ưu tiên các thuốc thường dùng và quan trọng trước

---

**Cập nhật lần cuối:** 2024-12-19 (đã thêm Paracetamol, Ibuprofen, Salbutamol, Ciprofloxacin, Clarithromycin, Oseltamivir, Trimethoprim-sulfamethoxazole, Budesonide inhaled, Montelukast, Fluticasone inhaled, Gabapentin, Pregabalin, Glibenclamide, Venlafaxine, Itraconazole, Voriconazole, Ganciclovir, Isosorbide mononitrate)

---

## Ghi Chú Kỹ Thuật

### Vấn Đề File Size
- File `drug_database.py` hiện tại: ~8,500+ dòng, ~850KB
- ⚠️ File quá lớn, khó maintain
- 📋 Đã có kế hoạch tách module: Xem `MODULE_REFACTORING_PLAN.md`

### Tiếp Tục
- Còn 29 thuốc cần bổ sung enhanced fields
- Ưu tiên: Antihistamines (Loratadine, Cetirizine, Fexofenadine), Antidiabetics (Empagliflozin, Dapagliflozin, Sitagliptin), Anticoagulants (Ticagrelor, Prasugrel)
- Sau khi hoàn thành tất cả → tiến hành refactor module
