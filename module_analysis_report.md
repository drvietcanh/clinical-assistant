# BÁO CÁO PHÂN TÍCH MODULE
**Ngày tạo:** D:\1app\medical
**Tổng số file:** 251

## 📊 TÓM TẮT

- ⚠️  **CRITICAL** (> 800 dòng): 4 files
- ⚠️  **Recommended** (> 500 dòng): 40 files
- ✅ **OK**: 207 files

## 🔴 CẦN TÁCH NGAY (CRITICAL)

### drugs\drug_database_data.py
- **Dòng:** 8735 (code: 8495)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~479 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (8735 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 8495 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~479 entries) - Nên tách data ra file riêng
  - 💡 Đề xuất: Tách data dictionary ra file riêng (.data.py)

**💡 Đề xuất tách:**
```
📦 TÁCH DATA:
  1. Tạo drug_database_data_data.py - Chứa data dictionary
  2. Giữ drug_database_data.py - Chứa logic và functions
  3. Import từ drug_database_data_data.py vào drug_database_data.py
```

### antibiotics\antibiotics_data_data.py
- **Dòng:** 3206 (code: 3077)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~210 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (3206 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 3077 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~210 entries) - Nên tách data ra file riêng
  - 💡 Đề xuất: Tách data dictionary ra file riêng (.data.py)

**💡 Đề xuất tách:**
```
📄 TÁCH THEO SECTION:
  - File quá dài (3206 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo antibiotics_data_data/ và chia nhỏ
```

### diagnosis\ddx_data_data.py
- **Dòng:** 1360 (code: 1328)
- **Classes:** 0
- **Functions:** 0
- **Data dict:** Có (~360 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (1360 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 1328 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~360 entries) - Nên tách data ra file riêng
  - 💡 Đề xuất: Tách data dictionary ra file riêng (.data.py)

**💡 Đề xuất tách:**
```
📄 TÁCH THEO SECTION:
  - File quá dài (1360 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo ddx_data_data/ và chia nhỏ
```

### drugs\enhanced_fields_schema_data.py
- **Dòng:** 887 (code: 773)
- **Classes:** 0
- **Functions:** 3
- **Data dict:** Có (~52 entries)
- **Gợi ý:**
  - ⚠️  CRITICAL: File quá dài (887 dòng) - Nên tách ngay!
  - 📝 Code thực tế: 773 dòng (không tính comment)
  - 📊 Có data dictionary lớn (~52 entries) - Nên tách data ra file riêng

## 🟡 NÊN XEM XÉT TÁCH

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

### scores\obstetrics\bishop.py (611 dòng)
- ⚠️  File dài (611 dòng) - Nên xem xét tách
- 📝 Code thực tế: 463 dòng (không tính comment)

### scores\gi\ranson.py (602 dòng)
- ⚠️  File dài (602 dòng) - Nên xem xét tách
- 📝 Code thực tế: 435 dòng (không tính comment)

### critical_care\transfusion.py (601 dòng)
- ⚠️  File dài (601 dòng) - Nên xem xét tách
- 📝 Code thực tế: 455 dòng (không tính comment)

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
| drugs\drug_database_data.py | 8735 | 8495 | 0 | 0 | ✅ (~479) |
| antibiotics\antibiotics_data_data.py | 3206 | 3077 | 0 | 0 | ✅ (~210) |
| diagnosis\ddx_data_data.py | 1360 | 1328 | 0 | 0 | ✅ (~360) |
| drugs\enhanced_fields_schema_data.py | 887 | 773 | 0 | 3 | ✅ (~52) |
| scores\metabolism\fena.py | 701 | 566 | 0 | 1 | ❌ |
| scores\gi\child_pugh.py | 699 | 549 | 0 | 1 | ❌ |
| scores\gi\meld.py | 698 | 543 | 0 | 2 | ❌ |
| scores\gi\glasgow_blatchford.py | 686 | 544 | 0 | 2 | ❌ |
| scores\nephrology\kdigo.py | 686 | 530 | 0 | 2 | ❌ |
| scores\pediatrics\apgar.py | 649 | 496 | 0 | 3 | ❌ |
| scores\respiratory\smartcop.py | 649 | 512 | 0 | 1 | ❌ |
| critical_care\sedation.py | 646 | 504 | 0 | 10 | ❌ |
| scores\gi\meld_na.py | 645 | 499 | 0 | 3 | ❌ |
| scores\cardiology\qtc.py | 639 | 501 | 0 | 8 | ❌ |
| scores\neurology\hunt_hess.py | 628 | 484 | 0 | 1 | ❌ |
| scores\infectious\centor.py | 625 | 471 | 0 | 4 | ❌ |
| scores\surgery\asa.py | 624 | 489 | 0 | 3 | ❌ |
| scores\gi\bisap.py | 622 | 474 | 0 | 1 | ❌ |
| scores\metabolism\bmi_ibw_bsa.py | 622 | 463 | 0 | 6 | ❌ |
| scores\obstetrics\bishop.py | 611 | 463 | 0 | 3 | ❌ |
