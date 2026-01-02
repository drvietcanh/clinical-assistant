# 📊 TÓM TẮT FILE DÀI CẦN CHIA NHỎ

## 🚨 TOP 10 FILE DÀI NHẤT (>2000 dòng)

| # | File | Số dòng | Loại | Ưu tiên |
|---|------|---------|------|---------|
| 1 | `patient_education/patient_education_data/disease.py` | **14,738** | CODE | ⚠️⚠️⚠️ CAO |
| 2 | `drugs/enhanced_fields_overrides.py` | **7,726** | CODE | ⚠️⚠️ CAO |
| 3 | `drugs/drug_modules/miscellaneous/biological_drugs.py` | **5,958** | CODE | ⚠️⚠️ CAO |
| 4 | `drugs/drug_modules/ophthalmology.py` | **5,046** | CODE | ⚠️⚠️ CAO |
| 5 | `drugs/drug_modules/dermatology.py` | **4,946** | CODE | ⚠️⚠️ CAO |
| 6 | `protocols/references_config.py` | **3,909** | CODE | ⚠️ TRUNG BÌNH |
| 7 | `drugs/drug_modules/hematology.py` | **3,736** | CODE | ⚠️ TRUNG BÌNH |
| 8 | `scores/references_config.py` | **3,102** | CODE | ⚠️ TRUNG BÌNH |
| 9 | `drugs/drug_modules/urology.py` | **2,648** | CODE | ⚠️ THẤP |
| 10 | `drugs/drug_modules/antimicrobial/antivirals/hiv_arvs.py` | **2,419** | CODE | ⚠️ THẤP |

## 📋 CÁC FILE KHÁC 2000-3000 DÒNG

- `drugs/drug_modules/infectious_other/cephalosporins.py` - 2,306 dòng
- `drugs/drug_modules/cardiovascular/anticoagulants.py` - 2,291 dòng
- `drugs/drug_modules/neurological/anticonvulsants.py` - 2,243 dòng
- `drugs/drug_modules/cardiovascular/antiarrhythmics.py` - 2,174 dòng
- `drugs/drug_modules/psychiatry_other/antipsychotics.py` - 2,132 dòng
- `drugs/drug_modules/emergency/electrolytes.py` - 2,051 dòng

## 🎯 KẾ HOẠCH THỰC HIỆN

### Phase 1: Ưu tiên cao (Files > 5000 dòng)
1. ✅ `patient_education/patient_education_data/disease.py` → Chia theo chuyên khoa
2. ✅ `drugs/enhanced_fields_overrides.py` → Chia theo nhóm thuốc
3. ✅ `drugs/drug_modules/miscellaneous/biological_drugs.py` → Chia theo loại biological
4. ✅ `drugs/drug_modules/ophthalmology.py` → Chia theo công dụng
5. ✅ `drugs/drug_modules/dermatology.py` → Chia theo nhóm thuốc

### Phase 2: Ưu tiên trung bình (Files 3000-5000 dòng)
6. ✅ `protocols/references_config.py` → Chia theo chuyên khoa
7. ✅ `drugs/drug_modules/hematology.py` → Chia theo cơ chế
8. ✅ `scores/references_config.py` → Chia theo chuyên khoa

### Phase 3: Ưu tiên thấp (Files 2000-3000 dòng)
9. ✅ Các file còn lại → Chia khi cần thiết

## 📝 NGUYÊN TẮC

- **Mục tiêu:** Mỗi file < 1000 dòng (lý tưởng: 500-800 dòng)
- **Cách chia:** Theo chức năng/chuyên khoa/nhóm thuốc
- **Backward compatibility:** Giữ nguyên imports, tạo `__init__.py` merge tất cả

## 📖 Xem chi tiết: `KE_HOACH_CHIA_NHO_FILE.md`

