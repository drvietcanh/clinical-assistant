# Disease Encyclopedia Module System

## Cấu trúc Module

Hệ thống được chia thành các module theo chuyên khoa để dễ quản lý và mở rộng.

### Cấu trúc thư mục

```
diseases/
├── __init__.py              # Exports chính
├── data.py                  # Disease class + tổng hợp từ modules
├── search.py                # Tìm kiếm bệnh
├── management.py            # Quản lý & thống kê ✨
└── modules/                 # Các module chuyên khoa
    ├── __init__.py
    ├── infectious.py        ✅ 4 bệnh
    ├── cardiology.py        ✅ 9 bệnh
    ├── respiratory.py       ✅ 2 bệnh
    ├── gastroenterology.py  ✅ 4 bệnh
    ├── endocrinology.py     ✅ 3 bệnh
    ├── nephrology.py        ✅ 2 bệnh
    ├── neurology.py         ✅ 2 bệnh
    ├── rheumatology.py      ✅ 1 bệnh
    ├── hematology.py        ✅ 2 bệnh
    ├── dermatology.py       ✅ 2 bệnh
    ├── psychiatry.py        ✅ 2 bệnh
    ├── emergency.py         ✅ 2 bệnh
    ├── oncology.py          (stub)
    ├── obstetrics_gynecology.py (stub)
    ├── pediatrics.py        (stub)
    ├── urology.py           (stub)
    ├── ophthalmology.py     (stub)
    ├── ent.py               (stub)
    ├── orthopedics.py       (stub)
    ├── critical_care.py     (stub)
    └── allergy_immunology.py (stub)
```

## Cách sử dụng

### 1. Import và sử dụng cơ bản

```python
from diseases import (
    DISEASES_DATABASE,
    get_all_diseases,
    get_diseases_by_category,
    get_category_list,
    search_diseases,
    get_disease_info
)

# Lấy tất cả bệnh
all_diseases = get_all_diseases()

# Lọc theo chuyên khoa
cardio_diseases = get_diseases_by_category("Cardiology")

# Tìm kiếm
results = search_diseases("viêm phổi")
```

### 2. Hệ thống quản lý và thống kê

```python
from diseases.management import (
    get_specialty_statistics,
    get_disease_by_id,
    search_diseases_by_keyword,
    get_diseases_by_icd10,
    get_diseases_by_drug,
    get_specialty_summary,
    export_specialty_data
)

# Thống kê theo chuyên khoa
stats = get_specialty_statistics()
print(stats["Cardiology"]["total_diseases"])  # 9

# Tìm bệnh theo ID
disease = get_disease_by_id("pneumonia")

# Tìm kiếm đa tiêu chí
results = search_diseases_by_keyword("sốt", category="Infectious")

# Tìm theo mã ICD-10
diseases = get_diseases_by_icd10("J18.9")

# Tìm theo thuốc
diseases = get_diseases_by_drug("Metformin")

# Tóm tắt tổng quan
summary = get_specialty_summary()
print(summary)

# Export dữ liệu chuyên khoa
data = export_specialty_data("Cardiology")
```

## Thêm bệnh mới

### Cách 1: Thêm vào module hiện có

Mở file module tương ứng (ví dụ: `diseases/modules/cardiology.py`) và thêm Disease object vào list:

```python
Disease(
    id="new_disease",
    name="New Disease",
    name_vn="Bệnh mới",
    category="Cardiology",
    definition="...",
    causes=[...],
    symptoms=[...],
    # ... các trường khác
)
```

### Cách 2: Tạo module mới

1. Tạo file mới trong `diseases/modules/` (ví dụ: `new_specialty.py`)
2. Import Disease class và tạo list bệnh
3. Thêm import vào `diseases/data.py`:

```python
from diseases.modules.new_specialty import NEW_SPECIALTY_DISEASES
```

4. Thêm vào `DISEASES_DATABASE`:

```python
DISEASES_DATABASE: List[Disease] = (
    # ... các module khác
    NEW_SPECIALTY_DISEASES
)
```

## Cấu trúc Disease Object

```python
@dataclass
class Disease:
    id: str                    # ID duy nhất
    name: str                  # Tên tiếng Anh
    name_vn: str               # Tên tiếng Việt
    category: str              # Chuyên khoa
    definition: str            # Định nghĩa
    causes: List[str]          # Nguyên nhân
    symptoms: List[str]        # Triệu chứng
    diagnosis: dict            # Chẩn đoán {"criteria": [], "tests": [], "imaging": []}
    treatment: dict            # Điều trị {"general": "", "medications": [], "procedures": []}
    prevention: List[str]      # Phòng ngừa
    complications: List[str]   # Biến chứng
    related_scores: List[str]  # Thang điểm liên quan
    related_drugs: List[str]    # Thuốc liên quan
    related_protocols: List[str] # Protocol liên quan
    icd10_codes: List[str]     # Mã ICD-10
```

## Lợi ích của cấu trúc module

1. **Dễ quản lý**: Mỗi chuyên khoa một file riêng
2. **Dễ mở rộng**: Thêm bệnh mới không ảnh hưởng module khác
3. **Dễ tìm kiếm**: Tìm bệnh trong module cụ thể
4. **Tự động tổng hợp**: `data.py` tự động import và tổng hợp
5. **Tự động mapping**: `CATEGORY_MAPPING` được tạo tự động

## Thống kê hiện tại

- **Tổng số bệnh**: 35
- **Số chuyên khoa có dữ liệu**: 12/21
- **Chuyên khoa đã tạo**: 21

## Lưu ý

- Luôn đảm bảo `id` là duy nhất
- `category` phải khớp với tên module
- Cập nhật `__init__.py` nếu thêm function mới
- Chạy linter để kiểm tra lỗi

