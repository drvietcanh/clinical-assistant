# KẾ HOẠCH TÁCH MODULE

**Ngày tạo:** 2025-11-04 14:05:57

## 📋 TỔNG QUAN

- **Số file cần tách:** 4
- **Ưu tiên:** Tách theo thứ tự từ file dài nhất

## 🎯 KẾ HOẠCH CHI TIẾT

### 1. drugs\drug_database_data.py

**Thông tin:**
- Dòng: 8735 (code: 8495)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

```
📦 TÁCH DATA:
  1. Tạo drug_database_data_data.py - Chứa data dictionary
  2. Giữ drug_database_data.py - Chứa logic và functions
  3. Import từ drug_database_data_data.py vào drug_database_data.py
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

### 2. antibiotics\antibiotics_data_data.py

**Thông tin:**
- Dòng: 3206 (code: 3077)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

```
📄 TÁCH THEO SECTION:
  - File quá dài (3206 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo antibiotics_data_data/ và chia nhỏ
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

### 3. diagnosis\ddx_data_data.py

**Thông tin:**
- Dòng: 1360 (code: 1328)
- Classes: 0
- Functions: 0
- Data dict: Có

**Phương án tách:**

```
📄 TÁCH THEO SECTION:
  - File quá dài (1360 dòng)
  - Tìm các comment section (# ==========)
  - Tách mỗi section thành file riêng
  - Tạo ddx_data_data/ và chia nhỏ
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

### 4. drugs\enhanced_fields_schema_data.py

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

## ✅ CHECKLIST TỔNG QUAN

- [ ] drugs\drug_database_data.py (8735 dòng)
- [ ] antibiotics\antibiotics_data_data.py (3206 dòng)
- [ ] diagnosis\ddx_data_data.py (1360 dòng)
- [ ] drugs\enhanced_fields_schema_data.py (887 dòng)
