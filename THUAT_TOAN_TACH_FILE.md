# Thuật Toán Tách File An Toàn

## Tổng Quan

Thuật toán này được thiết kế để tách file `obstetrics_gynecology.py` (và các file lớn khác) thành subfolder với các file con một cách an toàn, không mất dữ liệu và không gây lỗi.

## Nguyên Tắc Thiết Kế

### 1. An Toàn Tối Đa
- **Load từ module trực tiếp**: Thay vì parse file (có thể lỗi), load từ module Python đã được import
- **Backup tự động**: Tự động backup file gốc trước khi thay đổi
- **Rollback tự động**: Nếu có lỗi, tự động khôi phục file gốc
- **Test import**: Kiểm tra import sau khi tách để đảm bảo không có lỗi

### 2. Phân Loại Thông Minh
- Phân loại dựa trên field `group` của thuốc
- Sử dụng keywords để xác định category
- Fallback về `other_obgyn` nếu không phân loại được

### 3. Format Đúng Python Syntax
- Đảm bảo `True`/`False`/`None` (không phải `true`/`false`/`null`)
- Xử lý đúng string, list, dict, tuple
- Giữ nguyên format và indentation

## Các Bước Thực Hiện

### Bước 1: Load Thuốc Từ Module
```python
from drugs.drug_modules.obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DRUGS
all_drugs = dict(OBSTETRICS_GYNECOLOGY_DRUGS)
```

**Ưu điểm:**
- Không cần parse file (tránh lỗi syntax)
- Đảm bảo dữ liệu đúng như trong Python
- Tự động xử lý các edge cases

### Bước 2: Phân Loại Thuốc
```python
def categorize_drug_by_group(drug_name: str, drug_data: Dict) -> str:
    group = drug_data.get('group', '').lower()
    
    # Kiểm tra keywords
    if 'contraceptive' in group:
        return 'contraceptives'
    elif 'hormone' in group or 'estrogen' in group:
        return 'hormone_replacement'
    # ...
```

**Categories:**
- `contraceptives` - Thuốc tránh thai
- `hormone_replacement` - Hormone replacement therapy
- `fertility_drugs` - Thuốc hỗ trợ sinh sản
- `vaginal_medications` - Thuốc đặt âm đạo
- `uterotonics` - Thuốc co tử cung
- `other_obgyn` - Khác

### Bước 3: Tạo Thư Mục
```python
target_dir = Path("drugs/drug_modules/obstetrics_gynecology")
target_dir.mkdir(exist_ok=True)
```

### Bước 4: Tạo File Cho Từng Category

**Format file:**
```python
"""
Obstetrics and Gynecology Medications
{category_description}
"""
from typing import Dict, Any

CATEGORY_DRUGS: Dict[str, Dict[str, Any]] = {
    "Drug Name": {
        # Drug data here
    },
}

__all__ = ['CATEGORY_DRUGS']
```

**Quan trọng:**
- Sử dụng `format_drug_dict()` để format đúng Python syntax
- Đảm bảo `True`/`False`/`None` (không phải JSON `true`/`false`/`null`)
- Giữ nguyên indentation và structure

### Bước 5: Tạo __init__.py
```python
from .contraceptives import CONTRACEPTIVES_DRUGS
from .hormone_replacement import HORMONE_REPLACEMENT_DRUGS
# ...

OBSTETRICS_GYNECOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {
    **CONTRACEPTIVES_DRUGS,
    **HORMONE_REPLACEMENT_DRUGS,
    # ...
}
```

### Bước 6: Backup File Cũ
```python
backup_file = source_file.with_suffix('.py.backup')
shutil.copy2(source_file, backup_file)
```

### Bước 7: Tạo Wrapper File
```python
"""
Backward compatibility: imports from obstetrics_gynecology module
"""

from .obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DRUGS

__all__ = ['OBSTETRICS_GYNECOLOGY_DRUGS']
```

**Mục đích:** Giữ backward compatibility, code cũ vẫn import được.

### Bước 8: Test Import
```python
# Clear cache
import importlib
if 'drugs.drug_modules.obstetrics_gynecology' in sys.modules:
    del sys.modules['drugs.drug_modules.obstetrics_gynecology']

# Test import
from drugs.drug_modules.obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DRUGS

# Verify
assert len(OBSTETRICS_GYNECOLOGY_DRUGS) == len(all_drugs)
```

**Nếu lỗi:** Tự động khôi phục từ backup.

## Xử Lý Edge Cases

### 1. Boolean Values
```python
elif isinstance(value, bool):
    lines.append(f'{indent}{key_str}: {str(value)},')  # True/False
```

### 2. None Values
```python
elif value is None:
    lines.append(f'{indent}{key_str}: None,')
```

### 3. Tuples
```python
elif isinstance(value, tuple):
    if all(isinstance(item, str) for item in value):
        items = ', '.join(json.dumps(item) for item in value)
        lines.append(f'{indent}{key_str}: ({items}),')
```

### 4. Multi-line Strings
```python
if '\n' in value or len(value) > 100:
    escaped = value.replace('"""', '\\"\\"\\"')
    lines.append(f'{indent}{key_str}: """{escaped}""",')
```

### 5. Nested Dicts
```python
if isinstance(value, dict):
    value_str = format_drug_dict(value, indent_level + 4)
    lines.append(f'{indent}{key_str}: {value_str},')
```

## Kiểm Tra An Toàn

### 1. Kiểm Tra Số Lượng
```python
assert len(OBSTETRICS_GYNECOLOGY_DRUGS) == len(all_drugs)
```

### 2. Kiểm Tra Field
```python
for drug_name in sample_drugs:
    drug_data = OBSTETRICS_GYNECOLOGY_DRUGS[drug_name]
    assert 'group' in drug_data
```

### 3. Kiểm Tra Import
```python
from drugs.drug_modules.obstetrics_gynecology.contraceptives import CONTRACEPTIVES_DRUGS
assert len(CONTRACEPTIVES_DRUGS) > 0
```

## Rollback Mechanism

Nếu có lỗi trong bước 8 (test import):
```python
except Exception as e:
    # Restore backup
    shutil.copy2(backup_file, source_file)
    return False
```

## Kết Quả

Sau khi tách thành công:
- ✅ File gốc được backup
- ✅ Subfolder được tạo với các file con
- ✅ `__init__.py` combine tất cả
- ✅ Wrapper file giữ backward compatibility
- ✅ Import hoạt động đúng
- ✅ Số lượng thuốc khớp

## Sử Dụng

```bash
python split_obstetrics_gynecology_safe.py
```

Script sẽ:
1. Load thuốc từ module
2. Phân loại và tách file
3. Test import
4. Báo cáo kết quả

## Lưu Ý

1. **Backup**: File gốc được backup tự động
2. **Rollback**: Nếu lỗi, file gốc được khôi phục
3. **Test**: Luôn test import sau khi tách
4. **Format**: Đảm bảo Python syntax đúng (True/False/None)
5. **Compatibility**: Wrapper file giữ backward compatibility

## Mở Rộng

Thuật toán này có thể áp dụng cho các file lớn khác:
- Tương tự cho các module khác
- Chỉ cần thay đổi logic phân loại
- Giữ nguyên cơ chế an toàn

