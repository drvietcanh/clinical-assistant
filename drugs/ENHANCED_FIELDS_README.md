# Enhanced Fields Schema - Hướng dẫn sử dụng

## Tổng Quan

File `enhanced_fields_schema.py` chứa cấu trúc chuẩn và các công cụ hỗ trợ để thêm enhanced fields cho các thuốc trong database.

## Cấu Trúc Enhanced Fields

Enhanced fields bao gồm **14 trường** (6 cơ bản + 8 bổ sung):

### 6 Fields Cơ Bản (Bắt buộc)

1. **mechanism_of_action** (string) - Cơ chế tác dụng
2. **monitoring** (list of strings) - Các thông số cần theo dõi
3. **precautions** (list of strings) - Các lưu ý và thận trọng
4. **pharmacokinetics** (dict) - Thông tin dược động học
5. **storage** (string) - Điều kiện bảo quản
6. **black_box_warnings** (string or None) - Cảnh báo hộp đen

### 8 Fields Bổ sung (Tùy chọn)

7. **drug_interactions** (dict) - Tương tác thuốc chi tiết
8. **contraindications** (dict) - Chống chỉ định phân loại
9. **pregnancy_lactation** (dict) - Thai kỳ và cho con bú
10. **hepatic_adjustment** (dict) - Điều chỉnh liều suy gan
11. **overdose_management** (dict) - Xử trí quá liều
12. **reversal_agents** (dict or None) - Chất đối kháng
13. **administration_instructions** (dict) - Hướng dẫn dùng chi tiết
14. **references** (dict) - Tài liệu tham khảo
