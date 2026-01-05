# Cấu Trúc Module Thuốc

## Tổng Quan

Hệ thống thuốc được tổ chức theo module trong thư mục `drugs/drug_modules/`. Mỗi module đại diện cho một chuyên khoa hoặc nhóm thuốc.

## Cấu Trúc Thư Mục

```
drugs/drug_modules/
├── __init__.py                    # Export tất cả modules
├── cardiovascular/                # Module có subfolder
│   ├── __init__.py
│   ├── ace_arb.py
│   ├── beta_blockers/
│   └── ...
├── diabetes/                      # Module có subfolder
├── antimicrobial/                 # Module có subfolder
├── hematology/                    # Module có subfolder
│   ├── __init__.py
│   ├── anticoagulants.py
│   ├── antiplatelets.py
│   └── ...
├── dermatology/                   # Module có subfolder
├── ophthalmology/                 # Module có subfolder
├── urology/                       # Module có subfolder
└── other_module.py                # Module là file đơn (nếu nhỏ)
```

## Quy Tắc Tổ Chức

### 1. Module Có Subfolder

**Khi nào dùng:**
- Module có nhiều thuốc (>20 thuốc)
- Module có nhiều nhóm con rõ ràng
- File lớn hơn 100KB

**Cấu trúc:**
```
module_name/
├── __init__.py              # Combine tất cả submodules
├── category1.py             # Nhóm thuốc 1
├── category2.py             # Nhóm thuốc 2
└── other_module.py          # Thuốc khác
```

**Ví dụ:**
- `cardiovascular/` - có nhiều nhóm: ACE/ARB, beta blockers, calcium channel blockers, etc.
- `hematology/` - có nhiều nhóm: anticoagulants, antiplatelets, hemostatics, etc.

### 2. Module Là File Đơn

**Khi nào dùng:**
- Module có ít thuốc (<20 thuốc)
- Module không có nhóm con rõ ràng
- File nhỏ (<100KB)

**Ví dụ:**
- `ent_oral_nasal_combinations.py` - chỉ có 4 thuốc

## Quy Tắc Đặt Tên

### Tên Module

- Sử dụng lowercase với underscore: `cardiovascular`, `obstetrics_gynecology`
- Tên ngắn gọn, mô tả rõ chuyên khoa
- Tránh viết tắt không rõ ràng

### Tên File Trong Module

- Sử dụng lowercase với underscore: `ace_arb.py`, `topical_corticosteroids.py`
- Tên mô tả nhóm thuốc
- File `__init__.py` luôn có để combine các submodules

### Tên Biến

- Sử dụng UPPERCASE với underscore: `ACE_ARB_DRUGS`, `HEMATOLOGY_DRUGS`
- Format: `{CATEGORY}_DRUGS` hoặc `{MODULE}_DRUGS`

## Cấu Trúc File

### File __init__.py

```python
"""
Module Name Drugs
Combines all drugs from category-specific files
"""
from typing import Dict, Any

from .category1 import CATEGORY1_DRUGS
from .category2 import CATEGORY2_DRUGS

# Combine all drugs
MODULE_DRUGS: Dict[str, Dict[str, Any]] = {
    **CATEGORY1_DRUGS,
    **CATEGORY2_DRUGS,
}

__all__ = ['MODULE_DRUGS']
```

### File Category

```python
"""
Category Description
"""
from typing import Dict, Any

CATEGORY_DRUGS: Dict[str, Dict[str, Any]] = {
    "Drug Name": {
        # Drug data here
    },
}

__all__ = ['CATEGORY_DRUGS']
```

## Các Module Hiện Có

### Modules Có Subfolder

1. **cardiovascular/** - Tim mạch
2. **diabetes/** - Đái tháo đường
3. **antimicrobial/** - Kháng sinh/Kháng khuẩn
4. **hematology/** - Huyết học
5. **dermatology/** - Da liễu
6. **ophthalmology/** - Mắt
7. **urology/** - Tiết niệu
8. **gastrointestinal/** - Tiêu hóa
9. **respiratory/** - Hô hấp
10. **neurological/** - Thần kinh
11. **oncology/** - Ung thư
12. **emergency/** - Cấp cứu
13. **supportive/** - Hỗ trợ
14. **miscellaneous/** - Khác

### Modules Là File Đơn

- `ent_oral_nasal_combinations.py`
- Các module nhỏ khác

## Thêm Module Mới

1. Tạo thư mục hoặc file mới trong `drugs/drug_modules/`
2. Tạo file `__init__.py` nếu là thư mục
3. Thêm import vào `drugs/drug_modules/__init__.py`
4. Thêm vào `ALL_DRUGS` trong `drug_modules/__init__.py`

## Best Practices

1. **Tổ chức theo chuyên khoa**: Mỗi module đại diện một chuyên khoa
2. **Tách file lớn**: Nếu file >100KB, nên tách thành subfolder
3. **Đặt tên rõ ràng**: Tên file và biến phải mô tả rõ nội dung
4. **Consistent structure**: Giữ cấu trúc nhất quán giữa các module
5. **Documentation**: Thêm docstring cho mỗi module

## Ví Dụ

Xem các module hiện có để tham khảo:
- `drugs/drug_modules/cardiovascular/` - Module lớn với subfolder
- `drugs/drug_modules/hematology/` - Module đã được tách thành subfolder
- `drugs/drug_modules/ent_oral_nasal_combinations.py` - Module nhỏ là file đơn

