# BÁO CÁO PHÂN TÍCH MODULE
**Ngày tạo:** D:\1app\medical
**Tổng số file:** 442

## 📊 TÓM TẮT

- ⚠️  **CRITICAL** (> 800 dòng): 9 files
- ⚠️  **Recommended** (> 500 dòng): 53 files
- ✅ **OK**: 380 files

## 🔴 CẦN TÁCH NGAY (CRITICAL)

### drugs\drug_modules\cardiovascular_other.py
- **Dòng:** 1071 (code: 1062)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~86 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (1071 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 1062 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~86 entries) - Nên tách data ra file riêng
  - 💡 Đề xuất: Tách data dictionary ra file riêng (.data.py)

**💡 Đề xuất tách:**
```
📄 TÁCH THEO SECTION:
  - File quá dài (1071 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo cardiovascular_other/ và chia nhỏ
```

### drugs\drug_modules\antimicrobial\antibiotics.py
- **Dòng:** 1067 (code: 1056)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~71 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (1067 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 1056 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~71 entries) - Nên tách data ra file riêng
  - 💡 Đề xuất: Tách data dictionary ra file riêng (.data.py)

**💡 Đề xuất tách:**
```
📄 TÁCH THEO SECTION:
  - File quá dài (1067 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo antibiotics/ và chia nhỏ
```

### drugs\drug_modules\cardiovascular\beta_blockers.py
- **Dòng:** 1048 (code: 1040)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~73 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (1048 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 1040 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~73 entries) - Nên tách data ra file riêng
  - 💡 Đề xuất: Tách data dictionary ra file riêng (.data.py)

**💡 Đề xuất tách:**
```
📄 TÁCH THEO SECTION:
  - File quá dài (1048 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo beta_blockers/ và chia nhỏ
```

### drugs\drug_modules\psychiatry_other.py
- **Dòng:** 934 (code: 926)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~69 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (934 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 926 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~69 entries) - Nên tách data ra file riêng

### drugs\drug_modules\antimicrobial\antivirals.py
- **Dòng:** 926 (code: 918)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~72 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (926 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 918 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~72 entries) - Nên tách data ra file riêng

### antibiotics\antibiotics_data\cephalosporins.py
- **Dòng:** 923 (code: 899)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~63 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (923 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 899 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~63 entries) - Nên tách data ra file riêng

### drugs\enhanced_fields_schema_data.py
- **Dòng:** 887 (code: 773)
- **Classes:** 0
- **Functions:** 3
- **Data dict:** Có (~52 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (887 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 773 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~52 entries) - Nên tách data ra file riêng

### drugs\drug_modules\cardiovascular\calcium_blockers.py
- **Dòng:** 867 (code: 860)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~59 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (867 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 860 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~59 entries) - Nên tách data ra file riêng

### drugs\drug_modules\endocrinology_other\corticosteroids.py
- **Dòng:** 854 (code: 849)
- **Classes:** 0
- **Functions:** 0
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (854 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 849 dòng (không tính comment)

## 🟡 NÊN XEM XÉT TÁCH

### drugs\drug_modules\metabolic.py (794 dòng)
- ⚠️  File dài (794 dòng) - Nên xem xét tách
- 📝 Code thực tế: 791 dòng (không tính comment)
- 📊 Có data dictionary lớn (~59 entries) - Nên tách data ra file riêng

### drugs\drug_modules\antimicrobial\antifungals.py (767 dòng)
- ⚠️  File dài (767 dòng) - Nên xem xét tách
- 📝 Code thực tế: 760 dòng (không tính comment)
- 📊 Có data dictionary lớn (~56 entries) - Nên tách data ra file riêng

### scores\metabolism\fena.py (701 dòng)
- ⚠️  File dài (701 dòng) - Nên xem xét tách
- 📝 Code thực tế: 566 dòng (không tính comment)

### scores\gi\child_pugh.py (699 dòng)
- ⚠️  File dài (699 dòng) - Nên xem xét tách
- 📝 Code thực tế: 549 dòng (không tính comment)

### scores\gi\meld.py (698 dòng)
- ⚠️  File dài (698 dòng) - Nên xem xét tách
- 📝 Code thực tế: 543 dòng (không tính comment)

### scores\gi\glasgow_blatchford.py (686 dòng)
- ⚠️  File dài (686 dòng) - Nên xem xét tách
- 📝 Code thực tế: 544 dòng (không tính comment)

### scores\nephrology\kdigo.py (686 dòng)
- ⚠️  File dài (686 dòng) - Nên xem xét tách
- 📝 Code thực tế: 530 dòng (không tính comment)

### drugs\drug_modules\neurological\anticonvulsants.py (668 dòng)
- ⚠️  File dài (668 dòng) - Nên xem xét tách
- 📝 Code thực tế: 663 dòng (không tính comment)

### drugs\drug_modules\cardiovascular\anticoagulants.py (653 dòng)
- ⚠️  File dài (653 dòng) - Nên xem xét tách
- 📝 Code thực tế: 647 dòng (không tính comment)

### scores\pediatrics\apgar.py (649 dòng)
- ⚠️  File dài (649 dòng) - Nên xem xét tách
- 📝 Code thực tế: 496 dòng (không tính comment)

### scores\respiratory\smartcop.py (649 dòng)
- ⚠️  File dài (649 dòng) - Nên xem xét tách
- 📝 Code thực tế: 512 dòng (không tính comment)

### critical_care\sedation.py (646 dòng)
- ⚠️  File dài (646 dòng) - Nên xem xét tách
- 📝 Code thực tế: 504 dòng (không tính comment)

### scores\gi\meld_na.py (645 dòng)
- ⚠️  File dài (645 dòng) - Nên xem xét tách
- 📝 Code thực tế: 499 dòng (không tính comment)

### scores\cardiology\qtc.py (639 dòng)
- ⚠️  File dài (639 dòng) - Nên xem xét tách
- 📝 Code thực tế: 501 dòng (không tính comment)

### drugs\drug_modules\cardiovascular\diuretics.py (630 dòng)
- ⚠️  File dài (630 dòng) - Nên xem xét tách
- 📝 Code thực tế: 623 dòng (không tính comment)

### scores\neurology\hunt_hess.py (628 dòng)
- ⚠️  File dài (628 dòng) - Nên xem xét tách
- 📝 Code thực tế: 484 dòng (không tính comment)

### scores\infectious\centor.py (625 dòng)
- ⚠️  File dài (625 dòng) - Nên xem xét tách
- 📝 Code thực tế: 471 dòng (không tính comment)

### scores\surgery\asa.py (624 dòng)
- ⚠️  File dài (624 dòng) - Nên xem xét tách
- 📝 Code thực tế: 489 dòng (không tính comment)

### scores\gi\bisap.py (622 dòng)
- ⚠️  File dài (622 dòng) - Nên xem xét tách
- 📝 Code thực tế: 474 dòng (không tính comment)

### scores\metabolism\bmi_ibw_bsa.py (622 dòng)
- ⚠️  File dài (622 dòng) - Nên xem xét tách
- 📝 Code thực tế: 463 dòng (không tính comment)

### antibiotics\treatment_algorithms.py (618 dòng)
- ⚠️  File dài (618 dòng) - Nên xem xét tách
- 📝 Code thực tế: 576 dòng (không tính comment)
- 📊 Có data dictionary lớn (~91 entries) - Nên tách data ra file riêng

### drugs\tdm\vancomycin_tdm.py (615 dòng)
- ⚠️  File dài (615 dòng) - Nên xem xét tách
- 📝 Code thực tế: 480 dòng (không tính comment)

### scores\obstetrics\bishop.py (611 dòng)
- ⚠️  File dài (611 dòng) - Nên xem xét tách
- 📝 Code thực tế: 463 dòng (không tính comment)

### critical_care\transfusion.py (603 dòng)
- ⚠️  File dài (603 dòng) - Nên xem xét tách
- 📝 Code thực tế: 457 dòng (không tính comment)

### scores\gi\ranson.py (602 dòng)
- ⚠️  File dài (602 dòng) - Nên xem xét tách
- 📝 Code thực tế: 435 dòng (không tính comment)

### scores\emergency\sofa.py (596 dòng)
- ⚠️  File dài (596 dòng) - Nên xem xét tách
- 📝 Code thực tế: 464 dòng (không tính comment)

### scores\trauma\nexus.py (587 dòng)
- ⚠️  File dài (587 dòng) - Nên xem xét tách
- 📝 Code thực tế: 425 dòng (không tính comment)

### drugs\tdm\phenytoin.py (579 dòng)
- ⚠️  File dài (579 dòng) - Nên xem xét tách
- 📝 Code thực tế: 444 dòng (không tính comment)

### scores\cardiology\ascvd.py (574 dòng)
- ⚠️  File dài (574 dòng) - Nên xem xét tách
- 📝 Code thực tế: 458 dòng (không tính comment)

### drugs\tdm\theophylline.py (566 dòng)
- ⚠️  File dài (566 dòng) - Nên xem xét tách
- 📝 Code thực tế: 435 dòng (không tính comment)

### scores\ent\epworth.py (563 dòng)
- ⚠️  File dài (563 dòng) - Nên xem xét tách
- 📝 Code thực tế: 438 dòng (không tính comment)

### antibiotics\database.py (561 dòng)
- ⚠️  File dài (561 dòng) - Nên xem xét tách
- 📝 Code thực tế: 448 dòng (không tính comment)

### drugs\drug_modules\cardiovascular\ace_inhibitors.py (558 dòng)
- ⚠️  File dài (558 dòng) - Nên xem xét tách
- 📝 Code thực tế: 552 dòng (không tính comment)

### antibiotics\antibiotics_data\others.py (555 dòng)
- ⚠️  File dài (555 dòng) - Nên xem xét tách
- 📝 Code thực tế: 540 dòng (không tính comment)

### antibiotics\database_display.py (552 dòng)
- ⚠️  File dài (552 dòng) - Nên xem xét tách

### scores\hematology\dic_score.py (552 dòng)
- ⚠️  File dài (552 dòng) - Nên xem xét tách

### scores\metabolism\corrected_calcium.py (550 dòng)
- ⚠️  File dài (550 dòng) - Nên xem xét tách
- 📝 Code thực tế: 425 dòng (không tính comment)

### scores\emergency\news2.py (545 dòng)
- ⚠️  File dài (545 dòng) - Nên xem xét tách
- 📝 Code thực tế: 446 dòng (không tính comment)

### drugs\tdm\immunosuppressants.py (543 dòng)
- ⚠️  File dài (543 dòng) - Nên xem xét tách
- 📝 Code thực tế: 443 dòng (không tính comment)

### antibiotics\scenario_dosing_calculator.py (539 dòng)
- ⚠️  File dài (539 dòng) - Nên xem xét tách
- 📝 Code thực tế: 417 dòng (không tính comment)

### scores\pediatrics\pelod2.py (539 dòng)
- ⚠️  File dài (539 dòng) - Nên xem xét tách
- 📝 Code thực tế: 409 dòng (không tính comment)

### scores\obstetrics\modified_bishop.py (534 dòng)
- ⚠️  File dài (534 dòng) - Nên xem xét tách
- 📝 Code thực tế: 409 dòng (không tính comment)

### scores\neurology\nihss.py (531 dòng)
- ⚠️  File dài (531 dòng) - Nên xem xét tách
- 📝 Code thực tế: 437 dòng (không tính comment)

### critical_care\fluids.py (527 dòng)
- ⚠️  File dài (527 dòng) - Nên xem xét tách
- 📝 Code thực tế: 407 dòng (không tính comment)

### scores\metabolism\crcl.py (525 dòng)
- ⚠️  File dài (525 dòng) - Nên xem xét tách

### drugs\drug_info.py (523 dòng)
- ⚠️  File dài (523 dòng) - Nên xem xét tách

### scores\emergency\sofa2.py (522 dòng)
- ⚠️  File dài (522 dòng) - Nên xem xét tách

### protocols\emergency\gi_bleeding.py (518 dòng)
- ⚠️  File dài (518 dòng) - Nên xem xét tách

### scores\psychiatry\phq9.py (517 dòng)
- ⚠️  File dài (517 dòng) - Nên xem xét tách

### ventilator\calculators.py (516 dòng)
- ⚠️  File dài (516 dòng) - Nên xem xét tách
- 📝 Code thực tế: 421 dòng (không tính comment)

### scores\metabolism\free_t4_index.py (508 dòng)
- ⚠️  File dài (508 dòng) - Nên xem xét tách

### scores\oncology\ecog.py (503 dòng)
- ⚠️  File dài (503 dòng) - Nên xem xét tách

### scores\psychiatry\gad7.py (503 dòng)
- ⚠️  File dài (503 dòng) - Nên xem xét tách

## 📋 TOP 20 FILE DÀI NHẤT

| File | Dòng | Code | Classes | Functions | Data Dict |
|------|------|------|---------|-----------|-----------|
| drugs\drug_modules\cardiovascular_other.py | 1071 | 1062 | 0 | 0 | ✅ (~86) |
| drugs\drug_modules\antimicrobial\antibiotics.py | 1067 | 1056 | 0 | 0 | ✅ (~71) |
| drugs\drug_modules\cardiovascular\beta_blockers.py | 1048 | 1040 | 0 | 0 | ✅ (~73) |
| drugs\drug_modules\psychiatry_other.py | 934 | 926 | 0 | 0 | ✅ (~69) |
| drugs\drug_modules\antimicrobial\antivirals.py | 926 | 918 | 0 | 0 | ✅ (~72) |
| antibiotics\antibiotics_data\cephalosporins.py | 923 | 899 | 0 | 0 | ✅ (~63) |
| drugs\enhanced_fields_schema_data.py | 887 | 773 | 0 | 3 | ✅ (~52) |
| drugs\drug_modules\cardiovascular\calcium_blockers.py | 867 | 860 | 0 | 0 | ✅ (~59) |
| drugs\drug_modules\endocrinology_other\corticosteroids.py | 854 | 849 | 0 | 0 | ❌ |
| drugs\drug_modules\metabolic.py | 794 | 791 | 0 | 0 | ✅ (~59) |
| drugs\drug_modules\antimicrobial\antifungals.py | 767 | 760 | 0 | 0 | ✅ (~56) |
| scores\metabolism\fena.py | 701 | 566 | 0 | 1 | ❌ |
| scores\gi\child_pugh.py | 699 | 549 | 0 | 1 | ❌ |
| scores\gi\meld.py | 698 | 543 | 0 | 2 | ❌ |
| scores\gi\glasgow_blatchford.py | 686 | 544 | 0 | 2 | ❌ |
| scores\nephrology\kdigo.py | 686 | 530 | 0 | 2 | ❌ |
| drugs\drug_modules\neurological\anticonvulsants.py | 668 | 663 | 0 | 0 | ❌ |
| drugs\drug_modules\cardiovascular\anticoagulants.py | 653 | 647 | 0 | 0 | ❌ |
| scores\pediatrics\apgar.py | 649 | 496 | 0 | 3 | ❌ |
| scores\respiratory\smartcop.py | 649 | 512 | 0 | 1 | ❌ |
