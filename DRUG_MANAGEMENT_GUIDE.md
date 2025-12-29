# HƯỚNG DẪN QUẢN LÝ VÀ TÌM KIẾM THUỐC

**Cập nhật**: 2025-02-18

## TỔNG QUAN

Hệ thống quản lý thuốc đã được cải thiện để:
- ✅ Nhận diện chính xác số lượng thuốc thực sự
- ✅ Dễ dàng tìm kiếm thuốc
- ✅ Kiểm tra field nhanh chóng
- ✅ Quản lý và thống kê hiệu quả

## SỐ LƯỢNG THUỐC

- **Tổng số thuốc thực sự**: 579-604 (tùy theo logic lọc)
- **Các entries không phải thuốc**: Đã được lọc bỏ tự động
- **Tiêu chí nhận diện thuốc**:
  - Phải có ít nhất 2 trong: `group`, `vietnamese_name`, `administration`, `indications`
  - Loại bỏ các field names (lowercase với nhiều dấu gạch dưới)
  - Loại bỏ các giá trị đặc biệt (oral, im, sc, etc.)

## CÁC SCRIPT CHÍNH

### 1. `drug_manager.py` - Hệ thống quản lý chính

Quản lý toàn bộ database thuốc, cung cấp các chức năng:
- Tìm kiếm thuốc
- Kiểm tra field
- Thống kê
- Xuất database

**Cách sử dụng**:
```bash
# Tìm kiếm thuốc
python drug_manager.py search Gentamicin

# Kiểm tra field của một thuốc
python drug_manager.py check Gentamicin

# Tìm các thuốc thiếu một field cụ thể
python drug_manager.py missing references

# Xem thống kê
python drug_manager.py stats

# Xuất database ra JSON
python drug_manager.py export drugs_database.json
```

### 2. `check_drug_field_simple.py` - Kiểm tra field đơn giản

Script đơn giản, dễ sử dụng để kiểm tra field.

**Cách sử dụng**:
```bash
# Kiểm tra một thuốc
python check_drug_field_simple.py Gentamicin

# Kiểm tra với tất cả kết quả tìm thấy
python check_drug_field_simple.py Gentamicin --all

# Liệt kê các thuốc thiếu một field
python check_drug_field_simple.py --list-missing references

# Xem thống kê
python check_drug_field_simple.py --stats
```

### 3. `analyze_drug_count.py` - Phân tích số lượng thuốc

Phân tích chi tiết để xác định số lượng thuốc thực sự.

**Cách sử dụng**:
```bash
python analyze_drug_count.py
```

**Kết quả**:
- Tổng số entries tìm thấy
- Số lượng thuốc thực sự
- Số lượng entries không phải thuốc
- Phân loại theo lý do
- Thống kê field
- Phân bố theo file
- Lưu danh sách vào file

## VÍ DỤ SỬ DỤNG

### Tìm kiếm thuốc
```bash
# Tìm theo tên (partial match, case-insensitive)
python drug_manager.py search gentamicin
python drug_manager.py search amikacin
python check_drug_field_simple.py Gentamicin
```

### Kiểm tra field
```bash
# Kiểm tra field của một thuốc
python check_drug_field_simple.py Gentamicin

# Kết quả sẽ hiển thị:
# - Tên thuốc
# - File chứa thuốc
# - Các field thiếu (nếu có)
# - Trạng thái đầy đủ field
```

### Tìm thuốc thiếu field
```bash
# Tìm các thuốc thiếu field 'references'
python check_drug_field_simple.py --list-missing references

# Tìm các thuốc thiếu field 'administration_instructions'
python drug_manager.py missing administration_instructions
```

### Xem thống kê
```bash
# Xem thống kê tổng quan
python check_drug_field_simple.py --stats
python drug_manager.py stats
```

## CẤU TRÚC DỮ LIỆU

### Drug Object
```python
{
    'name': 'Gentamicin',
    'file': 'drugs/drug_modules/.../aminoglycosides.py',
    'fields': {'group', 'vietnamese_name', 'administration', ...},
    'field_count': 25
}
```

### Field Check Result
```python
{
    'drug_name': 'Gentamicin',
    'file': 'drugs/drug_modules/.../aminoglycosides.py',
    'missing_core': [],
    'missing_extended': [],
    'missing_enhanced': ['references'],
    'has_all_fields': False,
    'total_missing': 1
}
```

## LOGIC NHẬN DIỆN THUỐC

### Tiêu chí để một entry được coi là thuốc:

1. **Phải có ít nhất 2 trong các field**:
   - `group`
   - `vietnamese_name`
   - `administration`
   - `indications`

2. **Loại bỏ field names**:
   - Lowercase với nhiều dấu gạch dưới (trừ các exception: iv, po, im, sc)
   - Các field names đã biết: risk_flags, organ_toxicity, etc.

3. **Loại bỏ giá trị đặc biệt**:
   - oral, im, sc, inhaled, inhalation, iv, po
   - normal, 30_60, under_30, mild, moderate, severe
   - major, minor, tuyệt_đối, tương_đối

### Ví dụ:
- ✅ **Là thuốc**: "Gentamicin" (có group, vietnamese_name, administration, indications)
- ❌ **Không phải thuốc**: "risk_flags" (field name)
- ❌ **Không phải thuốc**: "oral" (giá trị đặc biệt)

## FILES ĐÃ TẠO

### Scripts:
- `drug_manager.py` - Hệ thống quản lý chính ⭐
- `check_drug_field_simple.py` - Kiểm tra field đơn giản ⭐
- `analyze_drug_count.py` - Phân tích số lượng thuốc

### Output files:
- `real_drugs_list.txt` - Danh sách thuốc thực sự
- `non_drugs_list.txt` - Danh sách entries không phải thuốc
- `drugs_database.json` - Database dạng JSON (khi export)

## SO SÁNH VỚI SCRIPT CŨ

| Metric | Script cũ | Script mới | Cải thiện |
|--------|-----------|------------|-----------|
| Số lượng nhận diện | 749 | 579-604 | Chính xác hơn |
| Lọc field names | Một phần | Hoàn chỉnh | ✅ |
| Tìm kiếm | Không có | Có | ✅ |
| Kiểm tra field | Phức tạp | Đơn giản | ✅ |
| Thống kê | Cơ bản | Chi tiết | ✅ |

## LƯU Ý

1. **Số lượng thuốc có thể khác nhau**:
   - Tùy theo logic lọc, có thể từ 579-666 thuốc
   - Script `analyze_drug_count.py` tìm thấy 604 thuốc
   - Script `drug_manager.py` tìm thấy 579 thuốc (lọc chặt hơn)

2. **Luôn kiểm tra bằng nhiều cách**:
   - Sử dụng `check_drug_field_simple.py` để kiểm tra nhanh
   - Sử dụng `drug_manager.py` để tìm kiếm và quản lý
   - Sử dụng `analyze_drug_count.py` để phân tích chi tiết

3. **Database có thể thay đổi**:
   - Khi thêm/sửa/xóa thuốc, cần chạy lại script để cập nhật
   - Có thể export ra JSON để lưu trữ

---

**Xem thêm**: 
- `SESSION_NOTES_2025-02-18.md` - Ghi chú chi tiết
- `QUICK_REFERENCE.md` - Tham khảo nhanh

