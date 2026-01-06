# Hướng Dẫn Workflow Quản Lý Thuốc

## Tổng Quan

Hướng dẫn này mô tả quy trình làm việc khi thêm, sửa, và quản lý thuốc trong hệ thống.

## Thêm Thuốc Mới

### Bước 1: Kiểm Tra Thuốc Đã Tồn Tại

```bash
python -m drugs.drug_cli search "Drug Name"
```

Hoặc sử dụng Python:
```python
from drugs.drug_manager_tool import get_drug_manager

manager = get_drug_manager()
if manager.check_drug_exists("Drug Name"):
    print("Drug already exists!")
```

### Bước 2: Xác Định Module và File

Sử dụng `DrugManager` để gợi ý:
```python
from drugs.drug_manager_tool import get_drug_manager

manager = get_drug_manager()
new_drug = {
    "group": "Cardiovascular - ACE Inhibitor",
    "indications": ["Hypertension", "Heart failure"]
}
suggestion = manager.suggest_placement(new_drug)
print(f"Suggested file: {suggestion['file']}")
print(f"Module: {suggestion['module']}")
print(f"Confidence: {suggestion['confidence']}")
```

### Bước 3: Validate Cấu Trúc

```python
from drugs.drug_manager_tool import get_drug_manager

manager = get_drug_manager()
validation = manager.validate_drug_structure(new_drug)
if not validation['valid']:
    print("Errors:", validation['errors'])
```

### Bước 4: Chuẩn Hóa Field

```python
from drugs.field_standardizer import get_field_standardizer

standardizer = get_field_standardizer()
standardized_drug = standardizer.standardize_drug(
    new_drug,
    include_additional=True,
    fix_format=True,
    reorder=True
)
```

### Bước 5: Thêm Vào File

1. Mở file được gợi ý (ví dụ: `drugs/drug_modules/cardiovascular/ace_arb.py`)
2. Thêm thuốc vào dictionary:
```python
ACE_ARB_DRUGS: Dict[str, Dict[str, Any]] = {
    "Existing Drug": {...},
    "New Drug Name": standardized_drug["New Drug Name"],
}
```

### Bước 6: Kiểm Tra Lại

```bash
# Kiểm tra field
python -m drugs.drug_cli check-fields "New Drug Name"

# Kiểm tra import
python -c "from drugs.drug_modules.cardiovascular.ace_arb import ACE_ARB_DRUGS; print('OK')"
```

## Sửa Thuốc

### Bước 1: Tìm File Chứa Thuốc

```bash
python -m drugs.drug_cli find "Drug Name"
```

Hoặc:
```python
from drugs.drug_manager_tool import get_drug_manager

manager = get_drug_manager()
files = manager.find_drug_file("Drug Name")
print(files)
```

### Bước 2: Sửa Dữ Liệu

1. Mở file chứa thuốc
2. Sửa dữ liệu thuốc
3. Chuẩn hóa lại nếu cần:
```python
from drugs.field_standardizer import get_field_standardizer

standardizer = get_field_standardizer()
updated_drug = standardizer.standardize_drug(edited_drug)
```

### Bước 3: Validate

```python
from drugs.field_validator import get_field_validator

validator = get_field_validator()
result = validator.validate_all_fields(updated_drug)
if not result['valid']:
    print("Errors:", result['errors'])
```

## Kiểm Tra Field

### Sử dụng CLI

```bash
# Kiểm tra một thuốc
python -m drugs.drug_cli check-fields "Metformin"

# Tìm thuốc thiếu field
python -m drugs.drug_cli missing-fields --module diabetes

# Tìm tất cả thuốc thiếu field
python -m drugs.drug_cli missing-fields
```

### Sử dụng Python

```python
from drugs.field_validator import get_field_validator
from drugs.drug_database import DRUG_DATABASE

validator = get_field_validator()
result = validator.validate_all_fields(DRUG_DATABASE["Metformin"])
print(result)
```

## Tìm Kiếm Thuốc

### Sử dụng CLI

```bash
# Tìm kiếm đơn giản
python -m drugs.drug_cli search "metformin"

# Tìm kiếm fuzzy
python -m drugs.drug_cli search "metform" --fuzzy

# Tìm theo module
python -m drugs.drug_cli stats --module diabetes
```

### Sử dụng Python

```python
from drugs.drug_index_system import get_drug_index

index = get_drug_index()

# Tìm kiếm
results = index.search("metformin", fuzzy=True)
print(results)

# Tìm theo module
results = index.search_by_module("diabetes")
print(results)

# Tìm theo group
results = index.search_by_group("ACE Inhibitor")
print(results)

# Tìm theo chỉ định
results = index.search_by_indication("hypertension")
print(results)
```

## Chuẩn Hóa Hàng Loạt

### Chuẩn Hóa Tất Cả Thuốc

```python
from drugs.field_standardizer import get_field_standardizer
from drugs.drug_database import DRUG_DATABASE

standardizer = get_field_standardizer()
standardized = standardizer.standardize_multiple_drugs(
    DRUG_DATABASE,
    include_additional=True,
    fix_format=True,
    reorder=True
)

# Lưu lại (cần cẩn thận!)
# for drug_name, drug_data in standardized.items():
#     # Update trong file tương ứng
```

## Kiểm Tra Trùng Lặp

```python
from drugs.drug_manager_tool import get_drug_manager

manager = get_drug_manager()
duplicates = manager.find_duplicates()
for drug_name, files in duplicates.items():
    print(f"{drug_name}: {files}")
```

## Export/Import

### Export

```bash
# Export một thuốc
python -m drugs.drug_cli export --drug "Metformin" --output metformin.json

# Export một module
python -m drugs.drug_cli export --module diabetes --output diabetes.json

# Export tất cả
python -m drugs.drug_cli export --output all_drugs.json
```

### Import (Gợi ý)

```python
from drugs.drug_manager_tool import get_drug_manager
import json

manager = get_drug_manager()

# Load từ JSON
with open('new_drug.json', 'r', encoding='utf-8') as f:
    drug_data = json.load(f)

# Validate và gợi ý
result = manager.import_drug(drug_data)
print(f"Suggested file: {result['suggested_file']}")
print(f"Validation: {result['validation']}")
```

## Phân tích Hệ Thống

### Chạy Phân tích Toàn Diện

```bash
python analyze_drug_system_structure.py
```

Kết quả:
- `drug_system_analysis_report.json` - Báo cáo chi tiết
- `drug_system_analysis_report.md` - Báo cáo markdown
- `missing_fields_report.json` - Thuốc thiếu field
- `duplicate_drugs_report.json` - Thuốc trùng lặp

### Kiểm Tra Field Toàn Diện

```bash
python check_all_drug_fields_comprehensive.py
```

Kết quả:
- `comprehensive_field_check_report.json` - Báo cáo chi tiết
- `comprehensive_field_check_report.md` - Báo cáo markdown
- `field_priority_list.json` - Danh sách ưu tiên sửa

## Best Practices

1. **Luôn validate trước khi thêm/sửa**: Sử dụng `FieldValidator`
2. **Chuẩn hóa field**: Sử dụng `FieldStandardizer` để đảm bảo cấu trúc đúng
3. **Kiểm tra trùng lặp**: Trước khi thêm thuốc mới
4. **Sử dụng gợi ý**: `DrugManager.suggest_placement()` để tìm đúng module
5. **Test import**: Luôn test import sau khi thêm/sửa
6. **Commit từng bước**: Commit sau mỗi thay đổi lớn
7. **Backup**: Backup file trước khi sửa lớn

## Troubleshooting

### Lỗi Import

```bash
# Kiểm tra syntax
python -m py_compile drugs/drug_modules/module/file.py

# Kiểm tra import
python -c "from drugs.drug_modules.module.file import DRUGS"
```

### Thuốc Không Tìm Thấy

```python
# Rebuild index
from drugs.drug_index_system import get_drug_index
index = get_drug_index()
index._build_indexes()
```

### Field Không Đúng Format

```python
# Sửa format
from drugs.field_standardizer import get_field_standardizer
standardizer = get_field_standardizer()
fixed = standardizer.fix_field_format(drug_data)
```

## Scripts Hữu Ích

1. `analyze_drug_system_structure.py` - Phân tích cấu trúc
2. `check_all_drug_fields_comprehensive.py` - Kiểm tra field
3. `drugs/drug_cli.py` - CLI tool
4. `drugs/drug_index_system.py` - Index system
5. `drugs/drug_manager_tool.py` - Manager tool
6. `drugs/field_validator.py` - Field validator
7. `drugs/field_standardizer.py` - Field standardizer

## Tài liệu tham khảo

- `MODULE_STRUCTURE.md` - Cấu trúc module
- `FIELD_STRUCTURE.md` - Cấu trúc field
- `drugs/drug_modules/` - Ví dụ thực tế

