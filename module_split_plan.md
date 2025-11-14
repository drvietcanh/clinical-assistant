# KẾ HOẠCH TÁCH MODULE

**Ngày tạo:** 2025-11-14 23:17:23

## 📋 TỔNG QUAN

- **Số file cần tách:** 9
- **Ưu tiên:** Tách theo thứ tự từ file dài nhất

## 🎯 KẾ HOẠCH CHI TIẾT

### 1. drugs\drug_modules\cardiovascular_other.py

**Thông tin:**
- Dòng: 1071 (code: 1062)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

```
📄 TÁCH THEO SECTION:
  - File quá dài (1071 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo cardiovascular_other/ và chia nhỏ
```

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

### 2. drugs\drug_modules\antimicrobial\antibiotics.py

**Thông tin:**
- Dòng: 1067 (code: 1056)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

```
📄 TÁCH THEO SECTION:
  - File quá dài (1067 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo antibiotics/ và chia nhỏ
```

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

### 3. drugs\drug_modules\cardiovascular\beta_blockers.py

**Thông tin:**
- Dòng: 1048 (code: 1040)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

```
📄 TÁCH THEO SECTION:
  - File quá dài (1048 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo beta_blockers/ và chia nhỏ
```

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

### 4. drugs\drug_modules\psychiatry_other.py

**Thông tin:**
- Dòng: 934 (code: 926)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

1. Tách data dictionary ra file riêng (`.data.py`)
2. Giữ logic và functions trong file gốc
3. Import data từ file mới

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

### 5. drugs\drug_modules\antimicrobial\antivirals.py

**Thông tin:**
- Dòng: 926 (code: 918)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

1. Tách data dictionary ra file riêng (`.data.py`)
2. Giữ logic và functions trong file gốc
3. Import data từ file mới

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

### 6. antibiotics\antibiotics_data\cephalosporins.py

**Thông tin:**
- Dòng: 923 (code: 899)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

1. Tách data dictionary ra file riêng (`.data.py`)
2. Giữ logic và functions trong file gốc
3. Import data từ file mới

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

### 7. drugs\enhanced_fields_schema_data.py

**Thông tin:**
- Dòng: 887 (code: 773)
- Classes: 0
- Functions: 3
- Data dict: Có

**Phương án tách:**

1. Tách data dictionary ra file riêng (`.data.py`)
2. Giữ logic và functions trong file gốc
3. Import data từ file mới

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

### 8. drugs\drug_modules\cardiovascular\calcium_blockers.py

**Thông tin:**
- Dòng: 867 (code: 860)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

1. Tách data dictionary ra file riêng (`.data.py`)
2. Giữ logic và functions trong file gốc
3. Import data từ file mới

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

### 9. drugs\drug_modules\endocrinology_other\corticosteroids.py

**Thông tin:**
- Dòng: 854 (code: 849)
- Classes: 0
- Functions: 0
- Data dict: Không

**Phương án tách:**

1. Phân tích các nhóm functions
2. Tách theo chức năng (utils, calculators, helpers...)

**Bước thực hiện:**

```
# TODO: Thêm các bước cụ thể
1. [ ] Bước 1
2. [ ] Bước 2
3. [ ] Bước 3
4. [ ] Test sau khi tách
```

---

## ✅ CHECKLIST TỔNG QUAN

- [ ] drugs\drug_modules\cardiovascular_other.py (1071 dòng)
- [ ] drugs\drug_modules\antimicrobial\antibiotics.py (1067 dòng)
- [ ] drugs\drug_modules\cardiovascular\beta_blockers.py (1048 dòng)
- [ ] drugs\drug_modules\psychiatry_other.py (934 dòng)
- [ ] drugs\drug_modules\antimicrobial\antivirals.py (926 dòng)
- [ ] antibiotics\antibiotics_data\cephalosporins.py (923 dòng)
- [ ] drugs\enhanced_fields_schema_data.py (887 dòng)
- [ ] drugs\drug_modules\cardiovascular\calcium_blockers.py (867 dòng)
- [ ] drugs\drug_modules\endocrinology_other\corticosteroids.py (854 dòng)
