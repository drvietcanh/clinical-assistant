# Hướng dẫn bổ sung field đầy đủ cho các thuốc

## Tình trạng hiện tại

Đã bắt đầu bổ sung thông tin cho thuốc đầu tiên: **Amvuttra (vutrisiran)**

### Thuốc đã hoàn thành:
- ✅ **Amvuttra (vutrisiran)** - `miscellaneous/other.py`
  - Đã bổ sung: side_effects, interactions, mechanism_of_action, precautions, pharmacokinetics, black_box_warnings, monitoring, pregnancy_lactation, hepatic_adjustment, overdose_management, administration_instructions

### Thuốc cần tiếp tục:
- 185 thuốc còn lại cần bổ sung thông tin

## Quy trình bổ sung thông tin

### 1. Xác định thuốc cần bổ sung
- Xem file `MANUAL_UPDATE_TEMPLATE.md` để biết danh sách thuốc
- Hoặc chạy `check_missing_fields.py` để xem báo cáo

### 2. Tìm thông tin từ nguồn đáng tin cậy

**Nguồn chính:**
- FDA Drug Labels: https://www.accessdata.fda.gov/scripts/cder/daf/
- DrugBank: https://go.drugbank.com/
- UpToDate
- PubMed

**Các field cần bổ sung:**
1. **side_effects** - Tác dụng phụ (list)
2. **interactions** - Tương tác thuốc (list)
3. **mechanism_of_action** - Cơ chế tác dụng (string, chi tiết)
4. **precautions** - Cảnh báo và thận trọng (list)
5. **pharmacokinetics** - Dược động học (dict với các subfield)
6. **black_box_warnings** - Cảnh báo đen (string)
7. **monitoring** - Theo dõi (list)
8. **pregnancy_lactation** - Thai kỳ và cho con bú (dict)
9. **hepatic_adjustment** - Điều chỉnh liều suy gan (dict)
10. **overdose_management** - Xử trí quá liều (dict)
11. **administration_instructions** - Hướng dẫn dùng thuốc (dict)

### 3. Cập nhật vào file module

**Cách 1: Sử dụng script (khuyến nghị)**
```python
from update_drug_fields import update_drug_in_module

updates = {
    "side_effects": ["Tác dụng phụ 1", "Tác dụng phụ 2"],
    "mechanism_of_action": "Cơ chế tác dụng chi tiết...",
    # ... các field khác
}

update_drug_in_module("miscellaneous/other.py", "DrugName", updates)
```

**Cách 2: Chỉnh sửa trực tiếp**
1. Mở file module tương ứng
2. Tìm entry của thuốc
3. Cập nhật các field còn thiếu
4. Kiểm tra syntax: `python -m py_compile [file_path]`

### 4. Kiểm tra và validate

Sau khi cập nhật:
1. Kiểm tra syntax Python
2. Chạy lại `check_missing_fields.py` để xác nhận
3. Cập nhật `MANUAL_UPDATE_TEMPLATE.md` (đánh dấu checkbox)

## Template cho các field

### side_effects (list)
```python
"side_effects": [
    "Tác dụng phụ 1 - phổ biến",
    "Tác dụng phụ 2 - hiếm nhưng nghiêm trọng",
    # ...
],
```

### mechanism_of_action (string)
```python
"mechanism_of_action": "Mô tả chi tiết về cơ chế tác dụng ở mức phân tử, bao gồm: target, pathway, tác dụng cuối cùng...",
```

### pharmacokinetics (dict)
```python
"pharmacokinetics": {
    "half_life": "Thời gian bán hủy",
    "onset": "Thời gian bắt đầu tác dụng",
    "duration": "Thời gian tác dụng",
    "protein_binding": "Tỷ lệ gắn protein (%)",
    "metabolism": "Cơ chế chuyển hóa",
    "clearance": "Cơ chế thanh thải"
},
```

### black_box_warnings (string)
```python
"black_box_warnings": "Cảnh báo đen nếu có, hoặc 'Không có black box warning' nếu không có",
```

## Lưu ý quan trọng

1. **Độ chính xác**: Luôn kiểm tra thông tin từ nguồn đáng tin cậy
2. **Format**: Đảm bảo đúng format Python (dấu ngoặc, dấu phẩy)
3. **Encoding**: Luôn dùng UTF-8
4. **Backup**: Tạo backup trước khi chỉnh sửa
5. **Syntax check**: Luôn kiểm tra syntax sau khi cập nhật

## Tiến độ

- ✅ Amvuttra (vutrisiran) - Hoàn thành
- ⏳ 185 thuốc còn lại - Đang chờ bổ sung

## Script hỗ trợ

- `update_drug_fields.py` - Script hỗ trợ cập nhật field
- `check_missing_fields.py` - Kiểm tra field còn thiếu
- `MANUAL_UPDATE_TEMPLATE.md` - Template theo dõi
