# Hướng Dẫn Toàn Diện Quản Lý Dữ Liệu Thuốc

## 🎯 Tổng Quan

Hệ thống quản lý dữ liệu thuốc toàn diện với các tính năng:
- ✅ **Kiểm tra chất lượng** - Phát hiện lỗi tự động
- ✅ **Kiểm tra tính toàn vẹn** - Đảm bảo tính nhất quán
- ✅ **Tìm kiếm nâng cao** - Fuzzy search, đa tiêu chí
- ✅ **Backup/Restore** - An toàn dữ liệu
- ✅ **Auto-fix** - Tự động sửa lỗi phổ biến
- ✅ **Theo dõi thay đổi** - Change tracking

## 📦 Các Module Chính

### 1. Data Quality Manager
**File:** `drugs/data_quality_manager.py`

**Chức năng:**
- Kiểm tra fields bắt buộc
- Kiểm tra kiểu dữ liệu
- Kiểm tra ràng buộc giá trị
- Phát hiện trùng lặp
- Kiểm tra tính nhất quán
- Kiểm tra format
- Tính toán chỉ số chất lượng

**Sử dụng:**
```python
from drugs.data_quality_manager import check_all_quality, calculate_quality_metrics

# Kiểm tra tất cả
errors = check_all_quality()

# Kiểm tra một thuốc
errors = check_all_quality(drug_name="Metformin")

# Chỉ số chất lượng
metrics = calculate_quality_metrics()
```

### 2. Data Integrity Checker
**File:** `drugs/data_integrity_checker.py`

**Chức năng:**
- Kiểm tra tham chiếu chéo
- Kiểm tra tính nhất quán dosage
- Kiểm tra tính nhất quán administration
- Kiểm tra cấu trúc contraindications

**Sử dụng:**
```python
from drugs.data_integrity_checker import check_all_integrity

result = check_all_integrity()
```

### 3. Data Search Enhancer
**File:** `drugs/data_search_enhancer.py`

**Chức năng:**
- Fuzzy search
- Tìm kiếm đa tiêu chí
- Gợi ý tìm kiếm
- Sửa lỗi chính tả

**Sử dụng:**
```python
from drugs.data_search_enhancer import fuzzy_search_drugs

results = fuzzy_search_drugs("metformim", threshold=0.6)
```

### 4. Data Backup Manager
**File:** `drugs/data_backup_manager.py`

**Chức năng:**
- Tạo backup
- Liệt kê backups
- Khôi phục từ backup
- Theo dõi thay đổi

**Sử dụng:**
```python
from drugs.data_backup_manager import create_backup

backup_file = create_backup()
```

### 5. Auto-Fix Manager
**File:** `drugs/auto_fix_manager.py`

**Chức năng:**
- Tự động sửa lỗi phổ biến
- Batch fix
- Preview trước khi fix

**Sử dụng:**
```python
from drugs.auto_fix_manager import auto_fix_drug

result = auto_fix_drug("Metformin", dry_run=True)
```

## 🛠️ CLI Commands

### Quality Management

```bash
# Kiểm tra chất lượng
python -m drugs.data_management_cli quality
python -m drugs.data_management_cli quality --drug Metformin

# Chỉ số chất lượng
python -m drugs.data_management_cli metrics
```

### Integrity Checking

```bash
# Kiểm tra tính toàn vẹn
python -m drugs.data_management_cli integrity
python -m drugs.data_management_cli integrity --show-issues
```

### Advanced Search

```bash
# Fuzzy search
python -m drugs.data_management_cli search "metformim" --fuzzy

# Tìm kiếm đa tiêu chí
python -m drugs.data_management_cli search --indication "đái tháo đường"
python -m drugs.data_management_cli search --administration PO

# Gợi ý tìm kiếm
python -m drugs.data_management_cli suggest "metform"
```

### Backup & Restore

```bash
# Tạo backup
python -m drugs.data_management_cli backup

# Liệt kê backups
python -m drugs.data_management_cli list-backups
```

### Data Issues

```bash
# Tìm trùng lặp
python -m drugs.data_management_cli duplicates

# Tìm thiếu fields
python -m drugs.data_management_cli missing-fields --fields drug_interactions
```

## 🔄 Workflow Quản Lý

### 1. Daily Maintenance

```bash
# 1. Kiểm tra chất lượng
python -m drugs.data_management_cli quality

# 2. Kiểm tra tính toàn vẹn
python -m drugs.data_management_cli integrity

# 3. Tìm trùng lặp
python -m drugs.data_management_cli duplicates
```

### 2. Before Making Changes

```bash
# 1. Tạo backup
python -m drugs.data_management_cli backup

# 2. Kiểm tra hiện trạng
python -m drugs.data_management_cli metrics
```

### 3. After Making Changes

```bash
# 1. Validate
python -m drugs.data_management_cli quality --drug [DrugName]

# 2. Kiểm tra lại
python -m drugs.data_management_cli integrity
```

## 📊 Quality Metrics

### Chỉ Số Chất Lượng

- **Quality Score**: 0-100 (mục tiêu > 90)
- **Error Rate**: % thuốc có lỗi (mục tiêu < 5%)
- **Field Coverage**: % fields đầy đủ (mục tiêu > 95%)

### Phân Loại Lỗi

- **Error**: Lỗi nghiêm trọng (thiếu field bắt buộc, sai type)
- **Warning**: Cảnh báo (format không chuẩn, thiếu field tùy chọn)
- **Info**: Thông tin (có thể cải thiện)

## 🔍 Tính Năng Tìm Kiếm

### 1. Fuzzy Search
Tìm kiếm mờ, chấp nhận lỗi chính tả:
```bash
python -m drugs.data_management_cli search "metformim" --fuzzy
```

### 2. Multi-Criteria Search
Tìm kiếm theo nhiều tiêu chí:
```python
from drugs.data_search_enhancer import search_by_multiple_criteria

results = search_by_multiple_criteria(
    name="metformin",
    indication="đái tháo đường",
    administration="PO"
)
```

### 3. Field Content Search
Tìm trong nội dung field:
```python
from drugs.data_search_enhancer import search_by_field_content

results = search_by_field_content("precautions", "tăng kali")
```

## 🛡️ Tránh Sai Sót

### 1. Validation Rules
- Fields bắt buộc phải có
- Kiểu dữ liệu phải đúng
- Giá trị phải hợp lệ
- Format phải chuẩn

### 2. Consistency Checks
- Đồng bộ giữa các fields liên quan
- Tham chiếu chéo phải hợp lệ
- Cấu trúc phải nhất quán

### 3. Auto-Fix
- Tự động sửa lỗi phổ biến
- Preview trước khi áp dụng
- Batch fix cho nhiều thuốc

## 🔧 Sửa Chữa Dễ Dàng

### 1. Tìm File
```bash
python -m drugs.drug_cli find Metformin
```

### 2. Kiểm Tra Trạng Thái
```bash
python -m drugs.enhanced_fields_cli status Metformin
```

### 3. Gợi ý Sửa
```bash
python -m drugs.enhanced_fields_cli suggest Metformin hepatic_adjustment
```

### 4. Auto-Fix
```python
from drugs.auto_fix_manager import auto_fix_drug

result = auto_fix_drug("Metformin", dry_run=True)
print(result["fix_code"])  # Copy vào file
```

## 📈 Best Practices

1. **Backup định kỳ** - Trước mỗi thay đổi lớn
2. **Quality check** - Sau mỗi thay đổi
3. **Integrity check** - Định kỳ hàng tuần
4. **Review duplicates** - Định kỳ hàng tháng
5. **Track changes** - Ghi log mọi thay đổi
6. **Validate** - Luôn validate trước khi commit
7. **Use fuzzy search** - Khi không chắc tên thuốc
8. **Check suggestions** - Xem gợi ý trước khi thêm mới

## 🚀 Quick Start

### Setup
```bash
# Không cần setup, chỉ cần import
```

### Basic Usage
```python
# 1. Kiểm tra chất lượng
from drugs.data_quality_manager import check_all_quality
errors = check_all_quality()

# 2. Tìm kiếm
from drugs.data_search_enhancer import fuzzy_search_drugs
results = fuzzy_search_drugs("metformin")

# 3. Backup
from drugs.data_backup_manager import create_backup
backup_file = create_backup()
```

### CLI Usage
```bash
# Quick check
python -m drugs.data_management_cli quality
python -m drugs.data_management_cli metrics

# Search
python -m drugs.data_management_cli search "metformin" --fuzzy

# Backup
python -m drugs.data_management_cli backup
```

## 📚 Tài Liệu Tham Khảo

- `drugs/data_quality_manager.py` - Quality checking
- `drugs/data_integrity_checker.py` - Integrity checking  
- `drugs/data_search_enhancer.py` - Enhanced search
- `drugs/data_backup_manager.py` - Backup/restore
- `drugs/auto_fix_manager.py` - Auto-fix
- `drugs/data_management_cli.py` - CLI tool
- `DRUG_DATA_MANAGEMENT_FEATURES.md` - Chi tiết tính năng

## 🎯 Roadmap

### Đã Hoàn Thành ✅
- Quality checking
- Integrity checking
- Enhanced search
- Backup/restore
- Auto-fix basics
- CLI tools

### Đề Xuất Phát Triển ⏳
- Data migration tools
- Comparison tool
- Export/import (Excel, CSV)
- Analytics dashboard
- Collaborative editing
- AI-powered suggestions

