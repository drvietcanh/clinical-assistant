# BÁO CÁO TIẾN TRÌNH BỔ SUNG THUỐC MỚI TỪ FDA 2021

## Tổng quan
- **Tổng số thuốc cần bổ sung**: 50 thuốc
- **Ngày bắt đầu**: 2025-02-18
- **Trạng thái**: Đang tiến hành bổ sung thông tin chi tiết

---

## PHẦN 1: THUỐC ĐÃ BỔ SUNG ĐẦY ĐỦ THÔNG TIN

### 1. Voxzogo (Vosoritide)
- **File**: `drugs/drug_modules/endocrinology_other/growth_hormone.py`
- **Trạng thái**: ✅ Đã bổ sung đầy đủ
- **Ngày hoàn thành**: 2025-02-18
- **Chi tiết**: 
  - Cơ chế tác dụng: CNP analog cho achondroplasia
  - Liều dùng: 15 mcg/kg SC x 1 lần/ngày
  - Tác dụng phụ: Phản ứng tại chỗ tiêm, hạ huyết áp thoáng qua
  - Monitoring: Tốc độ tăng trưởng, chiều cao, huyết áp

### 2. Skytrofa (Lonapegsomatropin)
- **File**: `drugs/drug_modules/endocrinology_other/growth_hormone.py`
- **Trạng thái**: ✅ Đã bổ sung đầy đủ
- **Ngày hoàn thành**: 2025-02-18
- **Chi tiết**:
  - Cơ chế tác dụng: Long-acting growth hormone
  - Liều dùng: 0.24 mg/kg SC x 1 lần/tuần
  - Tác dụng phụ: Phản ứng tại chỗ tiêm, tăng đường huyết
  - Monitoring: IGF-1, tốc độ tăng trưởng

### 3. Besremi (Ropeginterferon alfa-2b)
- **File**: `drugs/drug_modules/hematology/other_hematology.py`
- **Trạng thái**: ✅ Đã bổ sung đầy đủ
- **Ngày hoàn thành**: 2025-02-18
- **Chi tiết**:
  - Cơ chế tác dụng: Long-acting interferon alpha cho polycythemia vera
  - Liều dùng: 100-500 mcg SC x 1 lần/2 tuần
  - Tác dụng phụ: Cúm-like symptoms, giảm bạch cầu/tiểu cầu, rối loạn tâm thần
  - Black box warning: Rối loạn tâm thần, giảm bạch cầu/tiểu cầu, tăng men gan
  - Monitoring: CBC, chức năng gan, tâm thần, tuyến giáp

### 4. Rezurock (Belumosudil)
- **File**: `drugs/drug_modules/hematology/other_hematology.py`
- **Trạng thái**: ✅ Đã bổ sung đầy đủ
- **Ngày hoàn thành**: 2025-02-18
- **Chi tiết**:
  - Cơ chế tác dụng: ROCK2 inhibitor cho cGVHD
  - Liều dùng: 200-400mg PO x 1 lần/ngày
  - Tác dụng phụ: Tăng men gan, tiêu chảy, viêm phổi kẽ (ILD)
  - Black box warning: Tăng men gan, ILD, nhiễm trùng
  - Monitoring: Chức năng gan (mỗi 2 tuần trong 2 tháng đầu), dấu hiệu ILD

### 5. Empaveli (Pegcetacoplan)
- **File**: `drugs/drug_modules/hematology/other_hematology.py`
- **Trạng thái**: ✅ Đã bổ sung đầy đủ
- **Ngày hoàn thành**: 2025-02-18
- **Chi tiết**:
  - Cơ chế tác dụng: Complement C3 inhibitor cho PNH
  - Liều dùng: 1080mg SC x 2 lần/tuần
  - Tác dụng phụ: Phản ứng tại chỗ tiêm, nhiễm trùng
  - Black box warning: Nhiễm trùng Neisseria meningitidis
  - Monitoring: CBC, LDH, haptoglobin, dấu hiệu nhiễm trùng
  - **LƯU Ý**: CẦN TIÊM PHÒNG Neisseria meningitidis trước điều trị

---

## PHẦN 2: THUỐC ĐÃ THÊM VÀO HỆ THỐNG NHƯNG CHƯA BỔ SUNG ĐẦY ĐỦ

### 6. Livmarli (Maralixibat)
- **File**: `drugs/drug_modules/dermatology/other_topical.py`
- **Trạng thái**: ⚠️ Đã thêm vào hệ thống, CHƯA bổ sung đầy đủ
- **Cần bổ sung**:
  - [ ] Cơ chế tác dụng chi tiết (IBAT inhibitor)
  - [ ] Liều dùng chi tiết (pediatric dosing)
  - [ ] Tác dụng phụ đầy đủ
  - [ ] Monitoring guidelines
  - [ ] Precautions và black box warnings
  - [ ] Pharmacokinetics
  - [ ] Drug interactions
  - [ ] Overdose management

### 7. Korsuva (Difelikefalin)
- **File**: `drugs/drug_modules/dermatology/other_topical.py`
- **Trạng thái**: ⚠️ Đã thêm vào hệ thống, CHƯA bổ sung đầy đủ
- **Cần bổ sung**: Tương tự Livmarli

### 8. Bylvay (Odevixibat)
- **File**: `drugs/drug_modules/dermatology/other_topical.py`
- **Trạng thái**: ⚠️ Đã thêm vào hệ thống, CHƯA bổ sung đầy đủ
- **Cần bổ sung**: Tương tự Livmarli

---

## PHẦN 3: THUỐC ĐÃ TỰ ĐỘNG THÊM VÀO HỆ THỐNG (CẦN KIỂM TRA VÀ BỔ SUNG)

### Oncology
- **Scemblix** (asciminib) - `oncology/targeted_therapy_tkis.py`
- **Exkivity** (mobocertinib) - `oncology/targeted_therapy_tkis.py`
- **Truseltiq** (infigratinib) - `oncology/targeted_therapy_tkis.py`
- **Tepmetko** (tepotinib) - `oncology/targeted_therapy_tkis.py`
- **Rylaze** (asparaginase erwinia chrysanthemi) - `oncology/basic_oncology.py`
- **Pylarify** (piflufolastat F 18) - `oncology/basic_oncology.py`
- **Rybrevant** (amivantamab) - `oncology/basic_oncology.py`
- **Fotivda** (tivozanib) - `oncology/basic_oncology.py`
- **Pepaxto** (melphalan flufenamide) - `oncology/basic_oncology.py`
- **Cosela** (trilaciclib) - `oncology/basic_oncology.py`
- **Ukoniq** (umbralisib) - `oncology/basic_oncology.py`
- **Tivdak** (tisotumab vedotin) - `oncology/monoclonal_antibodies_adcs.py`
- **Zynlonta** (loncastuximab tesirine) - `oncology/monoclonal_antibodies_adcs.py`

### Psychiatry
- **Qelbree** (viloxazine) - `psychiatry_other/adhd_anxiolytics.py`
- **Azstarys** (serdexmethylphenidate/dexmethylphenidate) - `psychiatry_other/adhd_anxiolytics.py`

### Miscellaneous/Biological
- **Brexafemme** (ibrexafungerp) - `miscellaneous/biological/other_biological.py`
- **Lybalvi** (olanzapine/samidorphan) - `miscellaneous/biological/other_biological.py`
- **Welireg** (belzutifan) - `miscellaneous/biological/other_biological.py`
- **Nexviazyme** (avalglucosidase alfa) - `miscellaneous/biological/other_biological.py`
- **Nulibry** (fosdenopterin) - `miscellaneous/biological/other_biological.py`
- **Amondys 45** (casimersen) - `miscellaneous/biological/other_biological.py`
- **Pafolacianine** (Cytalux) - `miscellaneous/biological/other_biological.py`
- **Tavneos** (avacopan) - `miscellaneous/biological/monoclonal_antibodies.py`
- **Lupkynis** (voclosporin) - `miscellaneous/biological/monoclonal_antibodies.py`

### Other
- **Fexinidazole** - `infectious_other/anthelmintics.py`
- **Zegalogue** (dasiglucagon) - `emergency/electrolytes.py`
- **Nextstellis** (drospirenone/estetrol) - `obstetrics_gynecology/contraceptives.py`

---

## PHẦN 4: THUỐC ĐÃ THÊM THỦ CÔNG TRƯỚC ĐÓ

### Đã có đầy đủ thông tin:
- **Tralokinumab** (Adbry) - `miscellaneous/biological/monoclonal_antibodies.py`
- **Atogepant** (Qulipta) - `neurological/migraine_cgrp_drugs.py`
- **Ponesimod** (Ponvory) - `neurological/multiple_sclerosis_drugs.py`
- **Sotorasib** (Lumakras) - `oncology/targeted_therapy_tkis.py`
- **Maribavir** (Livtencity) - `antimicrobial/antivirals/cmv.py`

---

## HƯỚNG DẪN TIẾP TỤC

### Bước tiếp theo:
1. **Kiểm tra các thuốc đã tự động thêm** - Xem xét từng thuốc trong danh sách Phần 3
2. **Bổ sung thông tin đầy đủ** cho các thuốc còn thiếu:
   - Cơ chế tác dụng chi tiết
   - Liều dùng cụ thể
   - Tác dụng phụ đầy đủ
   - Monitoring guidelines
   - Precautions và black box warnings
   - Pharmacokinetics
   - Drug interactions
   - Overdose management
   - Administration instructions

### Ưu tiên:
1. **Cao**: Livmarli, Korsuva, Bylvay (đã có trong hệ thống, chỉ cần bổ sung)
2. **Trung bình**: Oncology drugs (nhiều thuốc quan trọng)
3. **Thấp**: Miscellaneous/biological (có thể bổ sung sau)

### Lưu ý:
- Tất cả các thuốc đã thêm vào hệ thống đều có cấu trúc cơ bản
- Cần bổ sung các field có giá trị "Cần bổ sung thông tin từ tài liệu FDA"
- Kiểm tra syntax errors sau mỗi lần chỉnh sửa
- Commit và push thường xuyên

---

## GHI CHÚ KỸ THUẬT

### Files đã chỉnh sửa:
- `drugs/drug_modules/endocrinology_other/growth_hormone.py` (Voxzogo, Skytrofa)
- `drugs/drug_modules/hematology/other_hematology.py` (Besremi, Rezurock, Empaveli)

### Files cần kiểm tra:
- `drugs/drug_modules/dermatology/other_topical.py` (Livmarli, Korsuva, Bylvay)
- `drugs/drug_modules/oncology/basic_oncology.py` (nhiều thuốc)
- `drugs/drug_modules/oncology/targeted_therapy_tkis.py` (nhiều thuốc)
- `drugs/drug_modules/oncology/monoclonal_antibodies_adcs.py` (Tivdak, Zynlonta)
- `drugs/drug_modules/psychiatry_other/adhd_anxiolytics.py` (Qelbree, Azstarys)
- `drugs/drug_modules/miscellaneous/biological/other_biological.py` (nhiều thuốc)
- `drugs/drug_modules/miscellaneous/biological/monoclonal_antibodies.py` (Tavneos, Lupkynis)

---

**Cập nhật lần cuối**: 2025-02-18
**Người thực hiện**: AI Assistant
**Trạng thái**: Đang tiến hành
