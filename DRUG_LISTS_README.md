# HƯỚNG DẪN SỬ DỤNG DANH SÁCH THUỐC

**Ngày tạo**: 2025-02-18  
**Tổng số thuốc**: 721

---

## TỔNG QUAN

Đã tạo **7 file danh sách thuốc** ở nhiều định dạng khác nhau để:
- ✅ Dễ dàng truy cập
- ✅ Tìm kiếm nhanh
- ✅ Sửa chữa thuận tiện
- ✅ Import vào các công cụ khác

---

## CÁC FILE DANH SÁCH

### 1. `drugs_list_simple.txt` ⭐
**Danh sách đơn giản - Chỉ tên thuốc**

- **Mục đích**: Xem nhanh danh sách tất cả thuốc
- **Định dạng**: Text đơn giản, mỗi dòng một thuốc
- **Sử dụng**: 
  - Tìm kiếm nhanh bằng Ctrl+F
  - Đếm số lượng thuốc
  - Copy danh sách

**Ví dụ**:
```
5-Fluorouracil
Abaloparatide
Abiraterone
...
```

---

### 2. `drugs_list_detailed.txt` ⭐
**Danh sách chi tiết - Tên + File + Field**

- **Mục đích**: Xem thông tin chi tiết từng thuốc
- **Định dạng**: Text có cấu trúc
- **Thông tin**: 
  - Tên thuốc
  - File chứa thuốc
  - Số lượng field
  - Các field thiếu (nếu có)

**Ví dụ**:
```
✅ Gentamicin
   File: drug_modules\antimicrobial\antibiotics\aminoglycosides.py
   Fields: 25 (14/14)

⚠️ Ampicillin
   File: drug_modules\antimicrobial\antibiotics\penicillins.py
   Fields: 18 (11/14)
   Missing: interactions, monitoring, storage
```

---

### 3. `drugs_list.csv` ⭐
**Danh sách CSV - Import Excel**

- **Mục đích**: Import vào Excel để xử lý
- **Định dạng**: CSV (Comma Separated Values)
- **Cột**: 
  - Drug Name
  - File
  - Field Count
  - Has 14 Fields
  - Missing Fields
  - Status

**Sử dụng**:
- Mở bằng Excel, Google Sheets
- Lọc và sắp xếp dễ dàng
- Tạo biểu đồ, thống kê

---

### 4. `drugs_list.json` ⭐
**Danh sách JSON - Xử lý bằng code**

- **Mục đích**: Xử lý bằng Python, JavaScript, etc.
- **Định dạng**: JSON
- **Cấu trúc**: 
  ```json
  {
    "created_date": "...",
    "total_drugs": 721,
    "drugs": {
      "DrugName": {
        "file": "...",
        "field_count": 25,
        "has_14_fields": true,
        "missing_14_fields": [],
        "fields": [...]
      }
    }
  }
  ```

**Sử dụng**:
- Load vào Python: `json.load(open('drugs_list.json'))`
- Xử lý tự động
- Tích hợp vào hệ thống khác

---

### 5. `drugs_list_by_file.txt` ⭐
**Danh sách theo file - Tìm thuốc trong file**

- **Mục đích**: Tìm thuốc trong file cụ thể
- **Định dạng**: Text có cấu trúc theo file
- **Thông tin**: 
  - Tên file
  - Số lượng thuốc trong file
  - Danh sách thuốc trong file

**Sử dụng**:
- Tìm file chứa thuốc
- Xem tất cả thuốc trong một file
- Kiểm tra phân bố thuốc

**Ví dụ**:
```
======================================================================
FILE: drug_modules\antimicrobial\antibiotics\aminoglycosides.py
So luong: 4 thuoc
======================================================================
  1. ✅ Gentamicin (25 fields)
  2. ✅ Amikacin (25 fields)
  3. ✅ Tobramycin (25 fields)
  4. ✅ Plazomicin (25 fields)
```

---

### 6. `drugs_search_index.txt` ⭐
**Index tìm kiếm - Theo chữ cái đầu**

- **Mục đích**: Tìm kiếm nhanh theo chữ cái đầu
- **Định dạng**: Text có cấu trúc theo chữ cái
- **Thông tin**: 
  - Chữ cái đầu
  - Số lượng thuốc
  - Danh sách thuốc

**Sử dụng**:
- Tìm thuốc bắt đầu bằng chữ cái cụ thể
- Tra cứu nhanh
- Đếm thuốc theo chữ cái

**Ví dụ**:
```
======================================================================
CHU CAI: A
So luong: 45 thuoc
======================================================================
  1. ✅ Abaloparatide
  2. ✅ Abiraterone
  3. ✅ Acarbose
  ...
```

---

### 7. `drugs_missing_fields.txt` ⭐
**Danh sách thuốc thiếu field**

- **Mục đích**: Xem thuốc cần bổ sung field
- **Định dạng**: Text chi tiết
- **Thông tin**: 
  - Tên thuốc
  - File chứa
  - Field count
  - Các field thiếu

**Sử dụng**:
- Xem thuốc cần sửa
- Lập kế hoạch bổ sung field
- Kiểm tra tiến độ

---

## CÁCH SỬ DỤNG

### Tìm kiếm nhanh:
1. Mở `drugs_list_simple.txt`
2. Dùng Ctrl+F để tìm
3. Hoặc mở `drugs_search_index.txt` để tìm theo chữ cái

### Xem thông tin chi tiết:
1. Mở `drugs_list_detailed.txt`
2. Tìm thuốc bằng Ctrl+F
3. Xem file chứa và field count

### Tìm thuốc trong file:
1. Mở `drugs_list_by_file.txt`
2. Tìm tên file bằng Ctrl+F
3. Xem tất cả thuốc trong file đó

### Xử lý bằng Excel:
1. Mở `drugs_list.csv` bằng Excel
2. Lọc và sắp xếp
3. Tạo biểu đồ, thống kê

### Xử lý bằng code:
```python
import json

# Load danh sách
with open('drugs_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Truy cập thuốc
drug = data['drugs']['Gentamicin']
print(drug['file'])
print(drug['field_count'])
```

### Xem thuốc cần sửa:
1. Mở `drugs_missing_fields.txt`
2. Xem danh sách thuốc thiếu field
3. Lập kế hoạch bổ sung

---

## CẬP NHẬT DANH SÁCH

Để cập nhật danh sách sau khi thêm/sửa/xóa thuốc:

```bash
python create_drug_lists.py
```

Script sẽ tự động:
- Load tất cả thuốc từ database
- Tạo lại tất cả 7 file danh sách
- Cập nhật thông tin mới nhất

---

## LƯU Ý

1. **File được tạo tự động**: Chạy `create_drug_lists.py` để tạo lại
2. **Định dạng UTF-8**: Tất cả file đều dùng UTF-8 để hỗ trợ tiếng Việt
3. **Cập nhật thường xuyên**: Nên chạy lại script sau khi thay đổi thuốc
4. **Backup**: Nên backup các file này trước khi cập nhật

---

## FILES ĐÃ TẠO

- `drugs_list_simple.txt` - Danh sách đơn giản
- `drugs_list_detailed.txt` - Danh sách chi tiết
- `drugs_list.csv` - CSV cho Excel
- `drugs_list.json` - JSON cho code
- `drugs_list_by_file.txt` - Theo file
- `drugs_search_index.txt` - Index tìm kiếm
- `drugs_missing_fields.txt` - Thuốc thiếu field
- `create_drug_lists.py` - Script tạo danh sách
- `DRUG_LISTS_README.md` - File này

---

**Cập nhật lần cuối**: 2025-02-18  
**Tổng số thuốc**: 721  
**Trạng thái**: ✅ Sẵn sàng sử dụng

