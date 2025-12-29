# Hướng Dẫn Hệ Thống Chỉ Mục Enhanced Fields

## Mục Tiêu
Tạo hệ thống chỉ mục thống nhất cho **14 Enhanced Fields** để:
- ✅ **Dễ tìm kiếm**: Tìm thuốc theo field, tìm nội dung trong fields
- ✅ **Dễ sửa chữa**: Tìm thuốc thiếu field, gợi ý nội dung
- ✅ **Dễ bổ sung**: Template, validation, code generation

## 14 Enhanced Fields

### 6 Fields Cơ Bản (Bắt buộc)
1. **mechanism_of_action** - Cơ chế tác dụng
2. **monitoring** - Các thông số cần theo dõi
3. **precautions** - Lưu ý và thận trọng
4. **pharmacokinetics** - Dược động học
5. **storage** - Điều kiện bảo quản
6. **black_box_warnings** - Cảnh báo hộp đen

### 8 Fields Bổ Sung (Khuyến nghị)
7. **drug_interactions** - Tương tác thuốc chi tiết
8. **contraindications** - Chống chỉ định chi tiết
9. **pregnancy_lactation** - Thai kỳ và cho con bú
10. **hepatic_adjustment** - Điều chỉnh liều suy gan
11. **overdose_management** - Xử trí quá liều
12. **reversal_agents** - Thuốc đối kháng
13. **administration_instructions** - Hướng dẫn dùng thuốc
14. **references** - Nguồn tham khảo

### Meta Fields (Bổ sung)
- **risk_flags** - Cờ cảnh báo rủi ro
- **guideline_tags** - Thẻ hướng dẫn lâm sàng
- **availability_vietnam** - Tình trạng có sẵn tại VN

## Công Cụ

### 1. Enhanced Fields Index (`drugs/enhanced_fields_index.py`)

Hệ thống chỉ mục để tìm kiếm:

```python
from drugs.enhanced_fields_index import (
    find_drugs_with_field,
    find_drugs_missing_fields,
    get_drug_field_status,
    search_fields_by_content,
    get_field_statistics,
)

# Tìm thuốc có field
drugs_with_field = find_drugs_with_field("drug_interactions", has_field=True)

# Tìm thuốc thiếu field
drugs_missing = find_drugs_with_field("drug_interactions", has_field=False)

# Tìm thuốc thiếu nhiều fields
missing = find_drugs_missing_fields(["drug_interactions", "pregnancy_lactation"])

# Trạng thái fields của thuốc
status = get_drug_field_status("Metformin")

# Tìm kiếm trong nội dung
results = search_fields_by_content("tăng kali", field_name="precautions")

# Thống kê
stats = get_field_statistics()
```

### 2. Enhanced Fields Manager (`drugs/enhanced_fields_manager.py`)

Công cụ quản lý và sửa chữa:

```python
from drugs.enhanced_fields_manager import (
    find_drugs_needing_fields,
    suggest_field_content,
    generate_field_code,
    validate_drug_fields,
)

# Tìm thuốc cần bổ sung fields (có kèm file path)
needing = find_drugs_needing_fields(["drug_interactions", "pregnancy_lactation"])

# Gợi ý nội dung cho field
suggestion = suggest_field_content("Metformin", "hepatic_adjustment")

# Tạo code để thêm vào enhanced_fields_overrides.py
code = generate_field_code("Metformin", "drug_interactions", field_value)

# Validate fields
is_valid, errors = validate_drug_fields("Metformin")
```

### 3. CLI Tool (`drugs/enhanced_fields_cli.py`)

Command line interface:

```bash
# Thống kê
python -m drugs.enhanced_fields_cli stats

# Tìm thuốc thiếu fields
python -m drugs.enhanced_fields_cli missing --fields drug_interactions pregnancy_lactation

# Trạng thái fields của thuốc
python -m drugs.enhanced_fields_cli status Metformin

# Tìm kiếm trong nội dung
python -m drugs.enhanced_fields_cli search "tăng kali" --field precautions

# Gợi ý nội dung
python -m drugs.enhanced_fields_cli suggest Metformin hepatic_adjustment

# Validate
python -m drugs.enhanced_fields_cli validate Metformin

# Thuốc đủ fields
python -m drugs.enhanced_fields_cli complete --count 14

# Xuất báo cáo
python -m drugs.enhanced_fields_cli report --output report.json
```

## Workflow Sửa Chữa

### 1. Tìm Thuốc Cần Bổ Sung Field

```bash
# Tìm thuốc thiếu drug_interactions
python -m drugs.enhanced_fields_cli missing --fields drug_interactions

# Tìm thuốc thiếu nhiều fields
python -m drugs.enhanced_fields_cli missing --fields drug_interactions pregnancy_lactation
```

### 2. Kiểm Tra Trạng Thái

```bash
python -m drugs.enhanced_fields_cli status Metformin
```

### 3. Lấy Gợi Ý Nội Dung

```python
from drugs.enhanced_fields_manager import suggest_field_content

suggestion = suggest_field_content("Metformin", "hepatic_adjustment")
print(suggestion["suggestions"])
```

### 4. Tạo Code và Thêm Vào File

```python
from drugs.enhanced_fields_manager import generate_field_code

field_value = {
    "mild": "Không đổi",
    "moderate": "Thận trọng",
    "severe": "Giảm liều",
    "notes": "..."
}

code = generate_field_code("Metformin", "hepatic_adjustment", field_value)
print(code)  # Copy vào enhanced_fields_overrides.py
```

### 5. Validate

```bash
python -m drugs.enhanced_fields_cli validate Metformin
```

## Tìm Kiếm Nâng Cao

### Tìm Theo Field

```python
# Thuốc có field
drugs = find_drugs_with_field("drug_interactions", has_field=True)

# Thuốc thiếu field
drugs = find_drugs_with_field("drug_interactions", has_field=False)
```

### Tìm Trong Nội Dung

```python
# Tìm trong tất cả fields
results = search_fields_by_content("tăng kali")

# Tìm trong field cụ thể
results = search_fields_by_content("tăng kali", field_name="precautions")
```

### Tìm Thuốc Đủ Fields

```python
# Đủ 14 fields
complete = find_drugs_with_complete_fields(count=14)

# Đủ ít nhất 12 fields
almost_complete = find_drugs_with_complete_fields(count=12)
```

## Thống Kê

### Thống Kê Tổng Quan

```bash
python -m drugs.enhanced_fields_cli stats
```

### Báo Cáo Chi Tiết

```python
from drugs.enhanced_fields_manager import get_field_completion_report

report = get_field_completion_report()
print(f"Complete: {report['summary']['complete_drugs']}")
print(f"Incomplete: {report['summary']['incomplete_drugs']}")

# Xem coverage từng field
for field, data in report["by_field"].items():
    print(f"{field}: {data['coverage']:.1f}%")
```

## Best Practices

1. **Luôn validate** sau khi thêm/sửa field
2. **Sử dụng gợi ý** để bắt đầu, sau đó tra cứu thêm
3. **Kiểm tra trùng lặp** với fields hiện có
4. **Export báo cáo** định kỳ để theo dõi tiến độ
5. **Ưu tiên core fields** trước extended fields

## Field Templates

Lấy template cho field:

```python
from drugs.enhanced_fields_index import get_field_template

template = get_field_template("drug_interactions")
print(template)
```

## Troubleshooting

### Field không tìm thấy
- Kiểm tra tên field chính xác (xem `ALL_ENHANCED_FIELDS`)
- Kiểm tra aliases (`contraindications_detail` → `contraindications`)

### Validation lỗi
- Chạy `validate` để xem lỗi chi tiết
- Kiểm tra type và structure của field
- Xem `FIELD_METADATA` để biết yêu cầu

### Gợi ý không có
- Field có thể không có thông tin để gợi ý
- Cần tra cứu thủ công từ nguồn

## Tài Liệu Tham Khảo

- `drugs/enhanced_fields_index.py` - Hệ thống chỉ mục
- `drugs/enhanced_fields_manager.py` - Công cụ quản lý
- `drugs/enhanced_fields_cli.py` - CLI tool
- `drugs/enhanced_fields_schema.py` - Schema và validation
- `drugs/README_ENHANCED_FIELDS.md` - Hướng dẫn bổ sung fields

