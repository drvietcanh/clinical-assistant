# 📋 Hướng Dẫn Kiểm Tra Dữ Liệu Thuốc

## Tổng Quan

Script `comprehensive_drug_validation.py` được thiết kế để kiểm tra sâu toàn bộ dữ liệu các thuốc trong database, phát hiện các lỗi và thiếu sót.

## Chức Năng

### 1. Kiểm Tra Field Cơ Bản (Required Fields)
Script kiểm tra các field bắt buộc sau:
- `group`: Nhóm thuốc
- `vietnamese_name`: Tên tiếng Việt
- `administration`: Đường dùng
- `indications`: Chỉ định
- `contraindications`: Chống chỉ định
- `dosage`: Liều dùng
- `side_effects`: Tác dụng phụ
- `interactions`: Tương tác thuốc
- `pregnancy`: Phân loại thai kỳ

### 2. Kiểm Tra Enhanced Fields (14 fields)
Script kiểm tra 14 enhanced fields:
1. `mechanism_of_action`: Cơ chế tác dụng
2. `monitoring`: Theo dõi
3. `precautions`: Thận trọng
4. `pharmacokinetics`: Dược động học
5. `storage`: Bảo quản
6. `black_box_warnings`: Cảnh báo đặc biệt
7. `drug_interactions`: Tương tác thuốc chi tiết
8. `contraindications_detail`: Chống chỉ định chi tiết
9. `pregnancy_lactation`: Thai kỳ và cho con bú
10. `hepatic_adjustment`: Điều chỉnh liều suy gan
11. `renal_adjustment`: Điều chỉnh liều suy thận
12. `overdose_management`: Xử trí quá liều
13. `reversal_agents`: Thuốc giải độc
14. `administration_instructions`: Hướng dẫn dùng thuốc

### 3. Kiểm Tra Kiểu Dữ Liệu
Script kiểm tra kiểu dữ liệu của từng field:
- String fields phải là `str`
- List fields phải là `list`
- Dict fields phải là `dict`
- Phát hiện các trường hợp sai kiểu dữ liệu

### 4. Kiểm Tra Cấu Trúc Dữ Liệu
Script kiểm tra cấu trúc của các field phức tạp:
- `dosage`: Phải là dictionary không rỗng
- `risk_flags`: Phải có các key: `high_alert`, `narrow_therapeutic_index`, `icu_critical_care_only`
- `drug_interactions`: Phải là dict với keys `major`, `moderate`, `minor` hoặc list
- `contraindications_detail`: Phải có keys `tuyệt_đối`, `tương_đối`
- `pregnancy_lactation`: Phải có `fda_category`
- `hepatic_adjustment`: Phải có keys `mild`, `moderate`, `severe`
- `renal_adjustment`: Phải có keys `normal`, `30_60`, `under_30`
- `overdose_management`: Phải là dictionary
- `administration_instructions`: Phải là dictionary
- `pharmacokinetics`: Phải là dictionary

### 5. Kiểm Tra Dữ Liệu Rỗng
Script phát hiện các field:
- Không tồn tại
- Có giá trị `None`
- String rỗng hoặc chỉ có khoảng trắng
- List hoặc dict rỗng

### 6. Kiểm Tra Trùng Lặp
Script kiểm tra tên thuốc trùng lặp (case-insensitive)

## Cách Sử Dụng

### Chạy Script

```bash
python comprehensive_drug_validation.py
```

### Kết Quả

Script sẽ:
1. Hiển thị báo cáo trên console với:
   - Thống kê tổng quan
   - Tỷ lệ hoàn thành từng enhanced field
   - Danh sách thuốc có lỗi
   - Danh sách thuốc có cảnh báo

2. Tạo file báo cáo:
   - `drug_validation_report.json`: Báo cáo chi tiết dạng JSON
   - `drug_validation_report.txt`: Báo cáo dạng text

## Đọc Báo Cáo

### Thống Kê Tổng Quan
- **Tổng số thuốc**: Tổng số thuốc trong database
- **Thuốc hoàn chỉnh**: Số thuốc có đầy đủ tất cả fields
- **Thuốc chưa hoàn chỉnh**: Số thuốc thiếu một số fields
- **Tổng số lỗi**: Số lỗi nghiêm trọng (thiếu field bắt buộc, sai kiểu dữ liệu)
- **Tổng số cảnh báo**: Số cảnh báo (thiếu enhanced field, field rỗng)

### Hoàn Thành Enhanced Fields
Bảng hiển thị tỷ lệ hoàn thành của từng enhanced field:
- ✅: 100% hoàn thành
- ⚠️: Chưa đầy đủ

### Thuốc Có Lỗi
Danh sách các thuốc có lỗi nghiêm trọng cần sửa ngay:
- ❌ Thiếu field bắt buộc
- ❌ Sai kiểu dữ liệu
- ❌ Cấu trúc dữ liệu sai

### Thuốc Có Cảnh Báo
Danh sách các thuốc có cảnh báo (có thể cải thiện):
- ⚠️ Thiếu enhanced field
- ⚠️ Enhanced field rỗng
- ⚠️ Thiếu key trong dictionary

## Ví Dụ Kết Quả

```
📊 THỐNG KÊ TỔNG QUAN:
   Tổng số thuốc: 666
   ✅ Thuốc hoàn chỉnh: 160 (24.0%)
   ⚠️  Thuốc chưa hoàn chỉnh: 506 (76.0%)
   ❌ Tổng số lỗi: 19
   ⚠️  Tổng số cảnh báo: 970

📋 HOÀN THÀNH CÁC ENHANCED FIELDS:
   ✅ mechanism_of_action                 | 666/666 (100.0%) | Thiếu:   0
   ✅ monitoring                          | 666/666 (100.0%) | Thiếu:   0
   ⚠️  black_box_warnings                  | 528/666 ( 79.3%) | Thiếu: 138
   ⚠️  contraindications_detail            | 320/666 ( 48.0%) | Thiếu: 346
```

## Sửa Lỗi

### Lỗi Kiểu Dữ Liệu
Nếu field có kiểu dữ liệu sai, cần sửa trong file module tương ứng:
- `guideline_tags` phải là `list`, không phải `dict`
- `overdose_management` phải là `dict`, không phải `str`

### Field Rỗng
Nếu field bắt buộc bị rỗng, cần bổ sung dữ liệu.

### Thiếu Enhanced Field
Nếu thiếu enhanced field, có thể:
1. Bổ sung trực tiếp trong file module
2. Sử dụng `enhanced_fields_overrides.py` để bổ sung

## Lưu Ý

- Script chỉ kiểm tra cấu trúc và kiểu dữ liệu, không kiểm tra nội dung
- Một số field có thể là `None` hợp lệ (như `black_box_warnings`)
- Enhanced fields là tùy chọn nhưng nên có đầy đủ để cải thiện chất lượng dữ liệu

## Tích Hợp Vào Workflow

Có thể chạy script này:
- Trước khi commit code
- Sau khi thêm/sửa thuốc mới
- Định kỳ để kiểm tra chất lượng dữ liệu
- Trong CI/CD pipeline

## Tùy Chỉnh

Có thể chỉnh sửa script để:
- Thêm các validation rules mới
- Thay đổi danh sách required fields
- Thêm các kiểm tra custom
- Tích hợp với hệ thống báo cáo khác

