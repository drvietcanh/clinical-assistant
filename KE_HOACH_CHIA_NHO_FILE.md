# 📋 KẾ HOẠCH CHIA NHỎ FILE - PHÂN TÍCH VÀ ĐỀ XUẤT

**Ngày phân tích:** 2025-02-18

---

## 📊 TỔNG QUAN

Sau khi phân tích toàn bộ codebase, phát hiện **nhiều file quá dài** (>2000 dòng) cần được chia nhỏ để:
- Dễ maintain và debug
- Tăng tốc độ load
- Cải thiện code organization
- Giảm conflict khi làm việc nhóm

---

## 🚨 TOP 10 FILE DÀI NHẤT CẦN ƯU TIÊN

### 1. **patient_education/patient_education_data/disease.py** - **14,738 dòng** ⚠️⚠️⚠️
- **Loại:** CODE FILE (10,806 dòng code)
- **Vấn đề:** File quá lớn, chứa tất cả dữ liệu giáo dục bệnh nhân về các bệnh
- **Đề xuất chia nhỏ:**
  ```
  patient_education/patient_education_data/
  ├── diseases/
  │   ├── cardiovascular.py      (tim mạch)
  │   ├── respiratory.py          (hô hấp)
  │   ├── diabetes.py             (đái tháo đường)
  │   ├── infectious.py           (nhiễm trùng)
  │   ├── neurological.py         (thần kinh)
  │   ├── gastrointestinal.py     (tiêu hóa)
  │   ├── renal.py                (thận)
  │   ├── hematology.py           (huyết học)
  │   └── other.py                (khác)
  └── __init__.py                 (import và merge tất cả)
  ```
- **Lợi ích:** Mỗi file ~1500-2000 dòng, dễ quản lý theo chuyên khoa

### 2. **drugs/enhanced_fields_overrides.py** - **7,726 dòng** ⚠️⚠️
- **Loại:** CODE FILE (7,573 dòng code, 2,513 dòng data)
- **Vấn đề:** Chứa tất cả enhanced fields overrides cho tất cả thuốc
- **Đề xuất chia nhỏ:**
  ```
  drugs/enhanced_fields/
  ├── cardiovascular.py
  ├── antimicrobial.py
  ├── neurological.py
  ├── diabetes.py
  ├── respiratory.py
  ├── gastrointestinal.py
  ├── hematology.py
  ├── supportive.py
  └── __init__.py                 (merge tất cả)
  ```
- **Lợi ích:** Chia theo nhóm thuốc, mỗi file ~800-1200 dòng

### 3. **drugs/drug_modules/miscellaneous/biological_drugs.py** - **5,958 dòng** ⚠️⚠️
- **Loại:** CODE FILE (5,921 dòng code)
- **Vấn đề:** Chứa tất cả biological drugs (monoclonal antibodies, etc.)
- **Đề xuất chia nhỏ:**
  ```
  drugs/drug_modules/miscellaneous/biological/
  ├── monoclonal_antibodies.py    (rituximab, trastuzumab, etc.)
  ├── cytokines.py               (interferon, interleukins)
  ├── vaccines.py                (vaccines)
  ├── enzymes.py                 (enzymes)
  └── __init__.py
  ```
- **Lợi ích:** Chia theo loại biological drug

### 4. **drugs/drug_modules/ophthalmology.py** - **5,046 dòng** ⚠️⚠️
- **Loại:** CODE FILE (5,014 dòng code)
- **Vấn đề:** File quá lớn, chứa tất cả thuốc nhãn khoa
- **Đề xuất chia nhỏ:**
  ```
  drugs/drug_modules/ophthalmology/
  ├── anti_glaucoma.py           (thuốc điều trị glaucom)
  ├── anti_infective.py          (kháng sinh, kháng virus mắt)
  ├── anti_inflammatory.py        (corticosteroid, NSAID mắt)
  ├── mydriatics.py              (giãn đồng tử)
  ├── lubricants.py              (nước mắt nhân tạo)
  └── __init__.py
  ```
- **Lợi ích:** Chia theo công dụng, mỗi file ~800-1000 dòng

### 5. **drugs/drug_modules/dermatology.py** - **4,946 dòng** ⚠️⚠️
- **Loại:** CODE FILE (4,907 dòng code)
- **Vấn đề:** File quá lớn, chứa tất cả thuốc da liễu
- **Đề xuất chia nhỏ:**
  ```
  drugs/drug_modules/dermatology/
  ├── topical_corticosteroids.py
  ├── topical_antifungals.py
  ├── topical_antibiotics.py
  ├── retinoids.py
  ├── immunosuppressants.py
  └── __init__.py
  ```
- **Lợi ích:** Chia theo nhóm thuốc, mỗi file ~800-1000 dòng

### 6. **protocols/references_config.py** - **3,909 dòng** ⚠️
- **Loại:** CODE FILE (3,797 dòng code)
- **Vấn đề:** Chứa tất cả references cho protocols
- **Đề xuất chia nhỏ:**
  ```
  protocols/references/
  ├── emergency.py               (cấp cứu)
  ├── critical_care.py           (hồi sức)
  ├── infectious.py              (nhiễm trùng)
  ├── cardiovascular.py          (tim mạch)
  └── __init__.py
  ```
- **Lợi ích:** Chia theo chuyên khoa protocol

### 7. **drugs/drug_modules/hematology.py** - **3,736 dòng** ⚠️
- **Loại:** CODE FILE (3,709 dòng code)
- **Vấn đề:** File lớn, chứa nhiều thuốc huyết học
- **Đề xuất chia nhỏ:**
  ```
  drugs/drug_modules/hematology/
  ├── anticoagulants.py         (chống đông)
  ├── antiplatelets.py           (chống kết tập tiểu cầu)
  ├── thrombolytics.py           (tiêu sợi huyết)
  ├── hemostatics.py             (cầm máu)
  └── __init__.py
  ```
- **Lợi ích:** Chia theo cơ chế tác dụng

### 8. **scores/references_config.py** - **3,102 dòng** ⚠️
- **Loại:** CODE FILE (2,938 dòng code)
- **Vấn đề:** Chứa tất cả references cho scores
- **Đề xuất chia nhỏ:**
  ```
  scores/references/
  ├── cardiology.py
  ├── emergency.py
  ├── respiratory.py
  ├── neurology.py
  ├── gi.py
  └── __init__.py
  ```
- **Lợi ích:** Chia theo chuyên khoa score

### 9. **drugs/drug_modules/urology.py** - **2,648 dòng** ⚠️
- **Loại:** CODE FILE (2,631 dòng code)
- **Vấn đề:** File lớn, có thể chia nhỏ
- **Đề xuất:** Có thể giữ nguyên hoặc chia theo nhóm nhỏ:
  ```
  drugs/drug_modules/urology/
  ├── bph.py                     (phì đại tuyến tiền liệt)
  ├── ed.py                      (rối loạn cương dương)
  ├── incontinence.py            (tiểu không tự chủ)
  └── __init__.py
  ```

### 10. **drugs/drug_modules/antimicrobial/antivirals/hiv_arvs.py** - **2,419 dòng** ⚠️
- **Loại:** CODE FILE (2,400 dòng code)
- **Vấn đề:** File lớn, chứa tất cả ARV
- **Đề xuất chia nhỏ:**
  ```
  drugs/drug_modules/antimicrobial/antivirals/hiv/
  ├── nrti.py                    (NRTI: tenofovir, lamivudine, etc.)
  ├── nnrti.py                   (NNRTI: efavirenz, nevirapine, etc.)
  ├── pi.py                      (Protease inhibitors)
  ├── integrase.py               (Integrase inhibitors)
  └── __init__.py
  ```

---

## 📋 KẾ HOẠCH THỰC HIỆN

### **Phase 1: Ưu tiên cao (Files > 5000 dòng)**
1. ✅ `patient_education/patient_education_data/disease.py` (14,738 dòng)
2. ✅ `drugs/enhanced_fields_overrides.py` (7,726 dòng)
3. ✅ `drugs/drug_modules/miscellaneous/biological_drugs.py` (5,958 dòng)
4. ✅ `drugs/drug_modules/ophthalmology.py` (5,046 dòng)
5. ✅ `drugs/drug_modules/dermatology.py` (4,946 dòng)

### **Phase 2: Ưu tiên trung bình (Files 3000-5000 dòng)**
6. ✅ `protocols/references_config.py` (3,909 dòng)
7. ✅ `drugs/drug_modules/hematology.py` (3,736 dòng)
8. ✅ `scores/references_config.py` (3,102 dòng)

### **Phase 3: Ưu tiên thấp (Files 2000-3000 dòng)**
9. ✅ `drugs/drug_modules/urology.py` (2,648 dòng)
10. ✅ `drugs/drug_modules/antimicrobial/antivirals/hiv_arvs.py` (2,419 dòng)
11. ✅ Các file khác 2000-3000 dòng

---

## 🎯 NGUYÊN TẮC CHIA NHỎ

### 1. **Chia theo chức năng/chuyên khoa**
- Mỗi file tập trung vào một nhóm thuốc/bệnh cụ thể
- Dễ tìm và maintain

### 2. **Giữ backward compatibility**
- Tạo `__init__.py` import và merge tất cả
- Code cũ vẫn hoạt động không cần sửa

### 3. **Kích thước mục tiêu**
- **Code files:** < 1000 dòng (lý tưởng: 500-800 dòng)
- **Data files:** < 2000 dòng (có thể lớn hơn nếu chỉ là data)

### 4. **Cấu trúc thư mục**
```
module_name/
├── __init__.py          (import và export tất cả)
├── submodule1.py
├── submodule2.py
└── submodule3.py
```

---

## 📝 CHECKLIST THỰC HIỆN

### Cho mỗi file cần chia:

- [ ] **Phân tích cấu trúc hiện tại**
  - [ ] Xác định các nhóm logic
  - [ ] Đếm số lượng items mỗi nhóm
  - [ ] Xác định cách chia hợp lý

- [ ] **Tạo cấu trúc mới**
  - [ ] Tạo thư mục con (nếu cần)
  - [ ] Tạo các file mới
  - [ ] Di chuyển code/data vào file mới

- [ ] **Tạo __init__.py**
  - [ ] Import tất cả từ các file con
  - [ ] Export các constants/functions chính
  - [ ] Đảm bảo backward compatibility

- [ ] **Kiểm tra**
  - [ ] Test import thành công
  - [ ] Test functionality không đổi
  - [ ] Kiểm tra không có lỗi syntax
  - [ ] Chạy app và test thực tế

- [ ] **Cleanup**
  - [ ] Xóa file cũ (sau khi đã test kỹ)
  - [ ] Update imports trong các file khác (nếu cần)
  - [ ] Commit và push

---

## ⚠️ LƯU Ý QUAN TRỌNG

1. **Backup trước khi chia:**
   ```bash
   git commit -am "Backup before refactoring"
   ```

2. **Test kỹ sau mỗi lần chia:**
   - Import test
   - Functionality test
   - Integration test

3. **Giữ nguyên tên biến/function:**
   - Đảm bảo code khác không bị ảnh hưởng

4. **Chia từng file một:**
   - Không chia nhiều file cùng lúc
   - Test kỹ trước khi chuyển sang file tiếp theo

---

## 📊 KẾT QUẢ MONG ĐỢI

Sau khi hoàn thành:
- ✅ Không còn file nào > 5000 dòng
- ✅ Hầu hết files < 2000 dòng
- ✅ Code dễ maintain hơn
- ✅ Tốc độ load nhanh hơn
- ✅ Dễ làm việc nhóm hơn

---

**Báo cáo được tạo tự động**  
**Ngày:** 2025-02-18

