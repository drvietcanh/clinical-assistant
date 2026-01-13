# Hướng Dẫn Sử Dụng Công Cụ Kiểm Tra và Bổ Sung Fields

## Tổng Quan

Bộ công cụ này giúp kiểm tra và bổ sung các field còn thiếu cho tất cả thuốc trong database.

## Các Script Có Sẵn

### 1. Kiểm Tra Fields (`check_all_drug_fields.py`)

**Mục đích:** Kiểm tra toàn diện tất cả thuốc và fields

```bash
python drugs/check_all_drug_fields.py
```

**Output:**
- Console report với thống kê tổng quan
- `drug_fields_analysis.json` - Dữ liệu phân tích chi tiết

**Kết quả:**
- Thống kê số thuốc thiếu/rỗng từng field
- Top 10 pattern thiếu field phổ biến
- Phân tích độ hoàn thiện

### 2. Bổ Sung Fields (`supplement_missing_fields.py`)

**Mục đích:** Bổ sung skeleton fields cho thuốc thiếu

```bash
# Xem trước (không thay đổi)
python drugs/supplement_missing_fields.py --dry-run

# Thực hiện (chỉ trong memory)
python drugs/supplement_missing_fields.py --execute

# Chỉ bổ sung field cụ thể
python drugs/supplement_missing_fields.py --execute --fields reversal_agents contraindications_detail
```

**Lưu ý:** Script này chỉ thay đổi DRUG_DATABASE trong memory, không lưu vào files nguồn.

**Output:**
- Console summary
- `supplement_report.json` - Chi tiết thay đổi

### 3. Tạo Báo Cáo Chi Tiết (`generate_field_report.py`)

**Mục đích:** Tạo báo cáo markdown chi tiết

```bash
python drugs/generate_field_report.py
```

**Output:**
- `drug_fields_detailed_report.md` - Báo cáo đầy đủ

**Nội dung:**
- Thống kê theo field
- Danh sách thuốc thiếu/rỗng từng field
- Phân loại thuốc theo độ hoàn thiện
- Ưu tiên hành động

### 4. Validation (`validate_all_drugs.py`)

**Mục đích:** Kiểm tra validation cho tất cả thuốc

```bash
python drugs/validate_all_drugs.py
```

**Output:**
- Console validation summary
- `validation_results.json` - Kết quả chi tiết

**Kiểm tra:**
- Format fields
- Type fields
- Thứ tự fields
- Lỗi và cảnh báo

### 5. Tạo Tổng Kết (`create_final_summary.py`)

**Mục đích:** Tạo báo cáo tổng kết cuối cùng

```bash
python drugs/create_final_summary.py
```

**Output:**
- `FINAL_FIELD_SUMMARY.md` - Báo cáo tổng kết
- `final_field_summary.json` - Dữ liệu JSON

## Quy Trình Sử Dụng

### Bước 1: Kiểm Tra Hiện Trạng
```bash
python drugs/check_all_drug_fields.py
```

Xem kết quả để biết:
- Field nào thiếu nhiều nhất
- Thuốc nào cần bổ sung
- Pattern thiếu field phổ biến

### Bước 2: Xem Trước Bổ Sung
```bash
python drugs/supplement_missing_fields.py --dry-run
```

Xem trước những gì sẽ được bổ sung mà không thay đổi database.

### Bước 3: Bổ Sung Fields (Nếu Cần)
```bash
python drugs/supplement_missing_fields.py --execute
```

**Lưu ý:** Chỉ thay đổi trong memory. Để lưu vào files nguồn, cần cập nhật các file Python trong `drugs/drug_modules/`.

### Bước 4: Validation
```bash
python drugs/validate_all_drugs.py
```

Kiểm tra xem có lỗi format, type không.

### Bước 5: Tạo Báo Cáo
```bash
python drugs/generate_field_report.py
python drugs/create_final_summary.py
```

Tạo báo cáo chi tiết và tổng kết.

## Tìm File Chứa Thuốc

Để cập nhật file nguồn cho một thuốc cụ thể:

```python
from drugs.drug_manager import find_drug_file

# Tìm file chứa thuốc
file_path = find_drug_file('DrugName')
print(f"File chứa thuốc: {file_path}")
```

## Cấu Trúc Fields

### STANDARD_14_FIELDS (Bắt buộc)
1. `group` - Nhóm thuốc
2. `vietnamese_name` - Tên tiếng Việt
3. `administration` - Đường dùng
4. `indications` - Chỉ định
5. `dosage` - Liều dùng
6. `side_effects` - Tác dụng phụ
7. `contraindications` - Chống chỉ định
8. `interactions` - Tương tác thuốc
9. `pregnancy` - Thai kỳ
10. `mechanism_of_action` - Cơ chế tác dụng
11. `monitoring` - Theo dõi
12. `precautions` - Thận trọng
13. `pharmacokinetics` - Dược động học
14. `storage` - Bảo quản

### ADDITIONAL_8_FIELDS (Bổ sung)
15. `black_box_warnings` - Cảnh báo đen
16. `drug_interactions` - Tương tác thuốc chi tiết
17. `pregnancy_lactation` - Thai kỳ và cho con bú
18. `hepatic_adjustment` - Điều chỉnh liều suy gan
19. `overdose_management` - Xử trí quá liều
20. `reversal_agents` - Thuốc đối kháng
21. `administration_instructions` - Hướng dẫn dùng thuốc
22. `references` - Tài liệu tham khảo

### ADDITIONAL_COMMON_FIELDS (Bổ sung quan trọng)
23. `renal_adjustment` - Điều chỉnh liều suy thận
24. `contraindications_detail` - Chống chỉ định chi tiết

## Tài Liệu Tham Khảo

- `IMPLEMENTATION_COMPLETE.md` - Tổng kết triển khai
- `FIELD_SUPPLEMENTATION_PLAN.md` - Kế hoạch chi tiết
- `FINAL_FIELD_SUMMARY.md` - Báo cáo tổng kết
- `drug_fields_detailed_report.md` - Báo cáo chi tiết

## Lưu Ý

1. **Backup:** Luôn backup trước khi thay đổi
2. **Dry-run:** Luôn chạy dry-run trước khi execute
3. **Validation:** Chạy validation sau mỗi lần thay đổi
4. **Incremental:** Bổ sung từng nhóm, kiểm tra sau mỗi nhóm

## Hỗ Trợ

Nếu gặp vấn đề, kiểm tra:
1. File có tồn tại không
2. Import paths có đúng không
3. Python version có tương thích không (Python 3.7+)
