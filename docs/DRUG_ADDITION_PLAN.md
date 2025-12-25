# 📋 Kế Hoạch Thêm Thuốc Mới vào Database

**Ngày tạo:** 2025-02-18  
**Database hiện tại:** 460 thuốc  
**Mục tiêu:** Mở rộng database với các thuốc quan trọng còn thiếu

---

## 📊 PHÂN TÍCH HIỆN TRẠNG

### Số lượng thuốc theo nhóm hiện tại:
- **Cardiovascular:** 30 thuốc
- **Antimicrobial:** ~50+ thuốc (antibiotics, antifungals, antivirals)
- **Neurology/Psychiatry:** 16 thuốc
- **Diabetes:** 9 thuốc
- **Oncology:** 10 thuốc
- **Emergency:** 7 thuốc
- **Gastrointestinal:** 10 thuốc
- **Respiratory:** 7 thuốc
- **Hematology:** 9 thuốc
- **Endocrinology:** 10 thuốc
- **Analgesics:** 9 thuốc
- **Other:** ~300+ thuốc khác

---

## 🎯 CHIẾN LƯỢC THÊM THUỐC

### Nguyên tắc ưu tiên:
1. **Thuốc phổ biến tại Việt Nam** - ưu tiên cao nhất
2. **Thuốc thiết yếu WHO/VN** - thuốc trong danh sách thiết yếu
3. **Thuốc ICU/Cấp cứu** - thuốc quan trọng trong cấp cứu
4. **Thuốc mới/FDA approved gần đây** - cập nhật kiến thức mới
5. **Thuốc có tương tác phức tạp** - cần thông tin chi tiết

---

## 📝 DANH SÁCH THUỐC ĐỀ XUẤT THÊM

### 🔴 **ƯU TIÊN CAO - Nhóm 1: Thuốc Cấp Cứu/ICU (15-20 thuốc)**

#### Vasopressors/Inotropes:
1. **Dobutamine** ✅ (đã có)
2. **Dopamine** ✅ (đã có)
3. **Norepinephrine** ✅ (đã có)
4. **Vasopressin** ✅ (đã có)
5. **Phenylephrine** ❌ (thiếu)
6. **Milrinone** ❌ (thiếu)

#### Sedatives/Anesthetics:
7. **Propofol** ✅ (đã có)
8. **Midazolam** ✅ (đã có)
9. **Ketamine** ✅ (đã có)
10. **Dexmedetomidine** ✅ (đã có)
11. **Etomidate** ✅ (đã có)
12. **Thiopental** ❌ (thiếu)
13. **Sevoflurane** ❌ (thiếu - nếu cần)

#### Neuromuscular Blockers:
14. **Succinylcholine** ❌ (thiếu - quan trọng)
15. **Rocuronium** ❌ (thiếu)
16. **Vecuronium** ❌ (thiếu)
17. **Cisatracurium** ❌ (thiếu)

#### Other ICU:
18. **Phenytoin IV** ✅ (đã có Phenytoin)
19. **Levetiracetam IV** ✅ (đã có)
20. **Fosphenytoin** ❌ (thiếu)

---

### 🟠 **ƯU TIÊN TRUNG BÌNH - Nhóm 2: Kháng Sinh Bổ Sung (20-25 thuốc)**

#### Beta-lactams:
1. **Cefotaxime** ✅ (đã có)
2. **Ceftazidime** ✅ (đã có)
3. **Cefepime** ✅ (đã có)
4. **Aztreonam** ❌ (thiếu - quan trọng cho dị ứng penicillin)
5. **Cefiderocol** ❌ (thiếu - kháng sinh mới)

#### Carbapenems:
6. **Meropenem** ✅ (đã có)
7. **Imipenem-cilastatin** ✅ (đã có)
8. **Ertapenem** ✅ (đã có)
9. **Doripenem** ❌ (thiếu)

#### Glycopeptides/Lipopeptides:
10. **Vancomycin** ✅ (đã có)
11. **Teicoplanin** ❌ (thiếu - phổ biến ở VN)
12. **Daptomycin** ✅ (đã có)

#### Other Antibiotics:
13. **Tigecycline** ✅ (đã có)
14. **Colistin** ✅ (đã có)
15. **Polymyxin B** ❌ (thiếu)
16. **Fosfomycin** ❌ (thiếu - quan trọng)
17. **Nitrofurantoin** ❌ (thiếu - UTI)
18. **Fidaxomicin** ❌ (thiếu - C. diff)

---

### 🟡 **ƯU TIÊN TRUNG BÌNH - Nhóm 3: Thuốc Tim Mạch Bổ Sung (15-20 thuốc)**

#### Antiarrhythmics:
1. **Amiodarone** ✅ (đã có)
2. **Lidocaine** ✅ (đã có)
3. **Procainamide** ✅ (đã có)
4. **Flecainide** ✅ (đã có)
5. **Sotalol** ❌ (thiếu)
6. **Dofetilide** ❌ (thiếu)

#### Heart Failure:
7. **Sacubitril-valsartan** ✅ (đã có)
8. **Ivabradine** ✅ (đã có)
9. **Vericiguat** ✅ (đã có)
10. **Entresto** ✅ (đã có - tên khác của Sacubitril-valsartan)
11. **Nesiritide** ❌ (thiếu - cấp cứu)

#### Antihypertensives:
12. **Hydralazine** ✅ (đã có)
13. **Nitroprusside** ❌ (thiếu - cấp cứu)
14. **Enalaprilat** ✅ (đã có)
15. **Clevidipine** ❌ (thiếu - ICU)

---

### 🟢 **ƯU TIÊN THẤP - Nhóm 4: Thuốc Chuyên Khoa (30-40 thuốc)**

#### Obstetrics/Gynecology:
1. **Oxytocin** ✅ (đã có)
2. **Misoprostol** ✅ (đã có)
3. **Methylergonovine** ❌ (thiếu)
4. **Carboprost** ❌ (thiếu)
5. **Dinoprostone** ❌ (thiếu)

#### Dermatology:
6. **Hydrocortisone topical** ❌ (thiếu)
7. **Clobetasol** ❌ (thiếu)
8. **Tacrolimus topical** ❌ (thiếu)
9. **Pimecrolimus** ❌ (thiếu)

#### Ophthalmology:
10. **Timolol eye drops** ❌ (thiếu)
11. **Latanoprost** ❌ (thiếu)
12. **Brinzolamide** ❌ (thiếu)

#### Urology:
13. **Tamsulosin** ❌ (thiếu - BPH)
14. **Finasteride** ❌ (thiếu - BPH)
15. **Sildenafil** ❌ (thiếu - ED)
16. **Tadalafil** ❌ (thiếu - ED/BPH)

---

### 🔵 **ƯU TIÊN THẤP - Nhóm 5: Thuốc Mới/FDA Gần Đây (20-30 thuốc)**

#### Oncology - Immunotherapy:
1. **Pembrolizumab** ✅ (đã có)
2. **Nivolumab** ✅ (đã có)
3. **Atezolizumab** ✅ (đã có)
4. **Durvalumab** ✅ (đã có)
5. **Cemiplimab** ✅ (đã có)
6. **Dostarlimab** ❌ (thiếu - mới)

#### Diabetes - GLP-1/SGLT2:
7. **Semaglutide** ✅ (đã có)
8. **Dulaglutide** ✅ (đã có)
9. **Tirzepatide** ✅ (đã có)
10. **Empagliflozin** ✅ (đã có)
11. **Dapagliflozin** ✅ (đã có)

#### Neurology - Alzheimer:
12. **Donepezil** ✅ (đã có)
13. **Memantine** ✅ (đã có)
14. **Aducanumab** ✅ (đã có)
15. **Lecanemab** ✅ (đã có)
16. **Donanemab** ✅ (đã có)

---

## 📋 QUY TRÌNH THÊM THUỐC MỚI

### Bước 1: Chuẩn bị thông tin
- [ ] Thu thập thông tin từ nguồn đáng tin cậy:
  - FDA Drug Labels
  - UpToDate, Medscape
  - Goodman & Gilman, Katzung
  - Nhà sản xuất thuốc
  - Clinical guidelines

### Bước 2: Xác định module phù hợp
- [ ] Xác định nhóm thuốc (cardiovascular, antimicrobial, etc.)
- [ ] Xác định file module phù hợp
- [ ] Kiểm tra xem thuốc đã có chưa

### Bước 3: Tạo entry với đầy đủ fields
- [ ] Basic fields (group, vietnamese_name, administration, indications, etc.)
- [ ] Dosage information
- [ ] Side effects, interactions
- [ ] **6 Enhanced fields cơ bản:**
  - mechanism_of_action
  - monitoring
  - precautions
  - pharmacokinetics
  - storage
  - black_box_warnings
- [ ] **8 Enhanced fields bổ sung** (nếu có thông tin)

### Bước 4: Validation
- [ ] Chạy `validate_all_drugs_comprehensive.py`
- [ ] Kiểm tra không có lỗi structure
- [ ] Kiểm tra không có lỗi validation

### Bước 5: Testing
- [ ] Test trong ứng dụng Streamlit
- [ ] Kiểm tra hiển thị đúng
- [ ] Kiểm tra search/filter

---

## 🛠️ CÔNG CỤ HỖ TRỢ

### Scripts có sẵn:
1. **`validate_all_drugs_comprehensive.py`** - Kiểm tra toàn diện database
2. **`find_drugs_without_enhanced.py`** - Tìm thuốc thiếu enhanced fields
3. **`check_enhanced_fields.py`** - Kiểm tra enhanced fields
4. **`drugs/add_new_drug_template.py`** - Template thêm thuốc mới

### Template Enhanced Fields:
- Xem `drugs/enhanced_fields_schema.py` để có template đầy đủ
- Sử dụng `create_enhanced_fields_template()` function

---

## 📅 KẾ HOẠCH THỰC HIỆN

### Phase 1: ICU/Cấp Cứu (Ưu tiên cao nhất)
**Mục tiêu:** 15-20 thuốc  
**Thời gian:** 1-2 tuần  
**Thuốc:**
- Phenylephrine
- Milrinone
- Succinylcholine
- Rocuronium
- Vecuronium
- Cisatracurium
- Fosphenytoin
- Thiopental

### Phase 2: Kháng Sinh Bổ Sung
**Mục tiêu:** 20-25 thuốc  
**Thời gian:** 2-3 tuần  
**Thuốc:**
- Aztreonam
- Teicoplanin
- Polymyxin B
- Fosfomycin
- Nitrofurantoin
- Fidaxomicin
- Doripenem

### Phase 3: Tim Mạch Bổ Sung
**Mục tiêu:** 15-20 thuốc  
**Thời gian:** 1-2 tuần  
**Thuốc:**
- Sotalol
- Dofetilide
- Nesiritide
- Nitroprusside
- Clevidipine

### Phase 4: Chuyên Khoa
**Mục tiêu:** 30-40 thuốc  
**Thời gian:** 3-4 tuần  
**Thuốc:**
- Obstetrics/Gynecology
- Dermatology
- Ophthalmology
- Urology

### Phase 5: Thuốc Mới
**Mục tiêu:** 20-30 thuốc  
**Thời gian:** 2-3 tuần  
**Thuốc:**
- Dostarlimab
- Các thuốc mới khác

---

## 📊 MỤC TIÊU TỔNG THỂ

### Ngắn hạn (1-2 tháng):
- Thêm 50-70 thuốc mới
- Tập trung vào ICU/Cấp cứu và Kháng sinh
- Đạt 510-530 thuốc tổng cộng

### Trung hạn (3-6 tháng):
- Thêm 100-150 thuốc mới
- Bổ sung đầy đủ các nhóm chuyên khoa
- Đạt 560-610 thuốc tổng cộng

### Dài hạn (6-12 tháng):
- Thêm 200-300 thuốc mới
- Database đầy đủ cho thực hành lâm sàng tại VN
- Đạt 660-760 thuốc tổng cộng

---

## ✅ CHECKLIST KHI THÊM THUỐC MỚI

- [ ] Thuốc chưa có trong database
- [ ] Xác định đúng module/file
- [ ] Có đầy đủ basic fields
- [ ] Có đầy đủ 6 enhanced fields cơ bản
- [ ] Có ít nhất 2-3 enhanced fields bổ sung
- [ ] Validation pass (không có lỗi)
- [ ] Test trong ứng dụng
- [ ] Cập nhật documentation nếu cần

---

## 📚 TÀI LIỆU THAM KHẢO

1. **FDA Drug Labels:** https://www.fda.gov/drugs
2. **UpToDate:** Drug information sections
3. **Medscape:** Drug reference
4. **Goodman & Gilman's:** The Pharmacological Basis of Therapeutics
5. **Katzung & Trevor's:** Pharmacology
6. **WHO Essential Medicines List:** https://www.who.int/medicines
7. **Vietnam Essential Medicines List:** Bộ Y tế Việt Nam

---

## 🔄 CẬP NHẬT KẾ HOẠCH

Kế hoạch này sẽ được cập nhật định kỳ dựa trên:
- Nhu cầu thực tế sử dụng
- Phản hồi từ người dùng
- Thuốc mới được FDA phê duyệt
- Thay đổi trong guidelines

**Lần cập nhật cuối:** 2025-02-18

