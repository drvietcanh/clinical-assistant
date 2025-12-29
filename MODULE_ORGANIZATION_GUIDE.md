# Hướng Dẫn Tổ Chức Module Thuốc

## Mục Tiêu
Tổ chức module thuốc để:
- ✅ **Dễ tìm kiếm**: Tìm thuốc nhanh chóng
- ✅ **Dễ sắp xếp**: Sắp xếp theo nhiều tiêu chí
- ✅ **Dễ sửa chữa**: Tìm và sửa file dễ dàng

## Cấu Trúc Hiện Tại

### 19 Modules Chính

1. **Cardiovascular** (CV) - Tim mạch
   - File: `drugs/drug_modules/cardiovascular/`
   - Subcategories: ACE inhibitors, ARBs, Beta-blockers, Statins, etc.

2. **Diabetes** (DM) - Đái tháo đường
   - File: `drugs/drug_modules/diabetes/`
   - Subcategories: Insulins, Biguanides, GLP-1, SGLT2, etc.

3. **Antimicrobial** (AM) - Kháng sinh/Kháng khuẩn
   - File: `drugs/drug_modules/antimicrobial/`
   - Subcategories: Antibiotics, Antivirals, Antifungals, Antituberculars

4. **Neurological** (NEURO) - Thần kinh/Tâm thần
   - File: `drugs/drug_modules/neurological/`
   - Subcategories: Anticonvulsants, Antidepressants, Antipsychotics

5. **Gastrointestinal** (GI) - Tiêu hóa
6. **Analgesics** (ANAL) - Giảm đau
7. **Respiratory** (RESP) - Hô hấp
8. **Oncology** (ONC) - Ung thư
9. **Emergency** (EMER) - Cấp cứu
10. **Hematology** (HEM) - Huyết học
11. **Endocrinology** (ENDO) - Nội tiết
12. **Metabolic** (MET) - Chuyển hóa
13. **Supportive** (SUP) - Hỗ trợ
14. **Urology** (URO) - Tiết niệu
15. **Dermatology** (DERM) - Da liễu
16. **Ophthalmology** (OPH) - Mắt
17. **Obstetrics/Gynecology** (OBGYN) - Sản phụ khoa
18. **ENT/Oral/Nasal** (ENT) - Tai mũi họng
19. **Miscellaneous** (MISC) - Khác

## Công Cụ Quản Lý

### 1. Drug Index (`drugs/drug_index.py`)

Hệ thống chỉ mục để tìm kiếm nhanh:

```python
from drugs.drug_index import search_drugs, find_drug_location

# Tìm kiếm thuốc
results = search_drugs("metformin", search_by="all")

# Tìm vị trí file
locations = find_drug_location("Metformin")
```

**Tính năng:**
- Tìm kiếm theo tên, từ khóa, nhóm, chỉ định
- Index tự động xây dựng
- Sắp xếp theo độ ưu tiên module

### 2. Drug Manager (`drugs/drug_manager.py`)

Công cụ quản lý và sửa chữa:

```python
from drugs.drug_manager import (
    find_drug_file,
    suggest_drug_placement,
    list_duplicate_drugs,
    export_module_structure
)

# Tìm file chứa thuốc
file_path = find_drug_file("Metformin")

# Gợi ý nơi đặt thuốc mới
suggestion = suggest_drug_placement("New Drug", drug_data)

# Tìm thuốc trùng lặp
duplicates = list_duplicate_drugs()
```

### 3. CLI Tool (`drugs/drug_cli.py`)

Command line interface:

```bash
# Tìm kiếm thuốc
python -m drugs.drug_cli search metformin

# Tìm file chứa thuốc
python -m drugs.drug_cli find Metformin

# Liệt kê modules
python -m drugs.drug_cli list --sort count

# Thông tin module
python -m drugs.drug_cli info Cardiovascular --show-drugs

# Tìm thuốc trùng lặp
python -m drugs.drug_cli duplicates

# Thống kê
python -m drugs.drug_cli stats

# Xuất cấu trúc
python -m drugs.drug_cli export --output structure.json
```

## Quy Tắc Tổ Chức

### 1. Đặt Thuốc Vào Module Đúng

**Nguyên tắc:**
- Dựa trên **nhóm điều trị chính** (group)
- Dựa trên **chỉ định chính** (indications)
- Sử dụng `suggest_drug_placement()` để gợi ý

**Ví dụ:**
- Metformin → Diabetes (nhóm: Biguanides)
- Amlodipine → Cardiovascular (nhóm: Calcium blockers)
- Omeprazole → Gastrointestinal (nhóm: PPIs)

### 2. Đặt Tên File Rõ Ràng

**Quy ước:**
- File module chính: `__init__.py`
- File subcategory: `{subcategory}.py` (snake_case)
- Ví dụ: `ace_inhibitors.py`, `beta_blockers.py`

### 3. Cấu Trúc Thư Mục

```
drug_modules/
├── cardiovascular/
│   ├── __init__.py          # Merge tất cả
│   ├── ace_inhibitors.py
│   ├── beta_blockers/
│   │   ├── __init__.py
│   │   ├── selective.py
│   │   └── non_selective.py
│   └── ...
├── diabetes/
│   ├── __init__.py
│   ├── insulins.py
│   └── ...
```

### 4. Metadata Module

Mỗi module có metadata trong `MODULE_METADATA`:
- `code`: Mã ngắn gọn (CV, DM, etc.)
- `description`: Mô tả module
- `keywords`: Từ khóa tìm kiếm
- `subcategories`: Danh mục con
- `file_path`: Đường dẫn file
- `priority`: Độ ưu tiên (1-4)

## Workflow Sửa Chữa

### 1. Tìm Thuốc Cần Sửa

```python
from drugs.drug_manager import find_drug_file

file_path = find_drug_file("Metformin")
print(f"File: {file_path}")
```

Hoặc dùng CLI:
```bash
python -m drugs.drug_cli find Metformin
```

### 2. Thêm Thuốc Mới

1. Xác định module phù hợp:
```python
from drugs.drug_manager import suggest_drug_placement

suggestion = suggest_drug_placement("New Drug", drug_data)
print(f"Đặt vào: {suggestion['module']}")
print(f"File: {suggestion['file_path']}")
```

2. Thêm vào file phù hợp
3. Kiểm tra trùng lặp:
```python
duplicates = list_duplicate_drugs()
```

### 3. Sửa Thuốc

1. Tìm file: `find_drug_file(drug_name)`
2. Sửa trong file
3. Kiểm tra syntax: `python -m py_compile {file}`

### 4. Xóa Thuốc

1. Tìm file: `find_drug_file(drug_name)`
2. Xóa entry trong dictionary
3. Kiểm tra không còn reference

## Tìm Kiếm Nâng Cao

### Tìm Theo Nhiều Tiêu Chí

```python
from drugs.drug_index import search_drugs

# Tìm theo tên
results = search_drugs("met", search_by="name")

# Tìm theo nhóm
results = search_drugs("beta blocker", search_by="group")

# Tìm theo chỉ định
results = search_drugs("tăng huyết áp", search_by="indication")

# Tìm tất cả
results = search_drugs("tim", search_by="all")
```

### Tìm Trong Module Cụ Thể

```python
results = search_drugs("metformin", module="Diabetes")
```

## Sắp Xếp

### Sắp Xếp Modules

```python
from drugs.drug_index import list_all_modules

# Theo tên
modules = list_all_modules(sort_by="name")

# Theo độ ưu tiên
modules = list_all_modules(sort_by="priority")

# Theo số lượng
modules = list_all_modules(sort_by="count")
```

### Sắp Xếp Thuốc Trong Module

```python
from drugs.drug_index import get_drugs_by_module

# Theo tên
drugs = get_drugs_by_module("Cardiovascular", sort_by="name")

# Theo nhóm
drugs = get_drugs_by_module("Cardiovascular", sort_by="group")
```

## Best Practices

1. **Luôn kiểm tra trùng lặp** trước khi thêm thuốc mới
2. **Sử dụng suggest_drug_placement()** để đặt đúng module
3. **Cập nhật metadata** nếu thêm subcategory mới
4. **Export structure** định kỳ để backup
5. **Sử dụng CLI** cho các thao tác thường xuyên

## Troubleshooting

### Thuốc không tìm thấy
- Kiểm tra tên chính xác (case-sensitive)
- Tìm trong tất cả modules: `search_drugs(name, search_by="all")`

### Không biết đặt thuốc vào module nào
- Dùng `suggest_drug_placement()`
- Xem metadata của các module
- Nếu không chắc, đặt vào "Miscellaneous"

### File quá lớn
- Chia nhỏ thành subcategories
- Tạo thư mục con với `__init__.py` merge lại

## Tài Liệu Tham Khảo

- `drugs/drug_index.py` - Hệ thống chỉ mục
- `drugs/drug_manager.py` - Công cụ quản lý
- `drugs/drug_cli.py` - CLI tool
- `drugs/drug_statistics.py` - Thống kê

