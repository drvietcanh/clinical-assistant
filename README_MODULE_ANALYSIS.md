# 🔍 HƯỚNG DẪN KIỂM TRA MODULE

## Mục đích

Script tự động phân tích độ dài các module Python và đề xuất phương án tách hợp lý.

## Cách sử dụng

### 1. Chạy kiểm tra nhanh

```bash
python check_modules.py
```

Script sẽ:
- ✅ Quét tất cả file `.py` trong project
- ✅ Phân tích độ dài, số classes, functions
- ✅ Phát hiện data dictionaries lớn
- ✅ Đề xuất cách tách hợp lý
- ✅ Tạo báo cáo chi tiết: `module_analysis_report.md`

### 2. Chạy tự động (không hỏi)

```bash
python check_modules.py --auto
```

### 3. Sử dụng trực tiếp analyzer

```python
from utils.module_analyzer import ModuleAnalyzer

analyzer = ModuleAnalyzer(".")
results = analyzer.analyze_all()
report = analyzer.generate_report("my_report.md")
```

## Tiêu chí đánh giá

### 🔴 CRITICAL (>800 dòng)
- **Hành động:** Nên tách ngay
- **Lý do:** File quá dài, khó maintain, khó test

### 🟡 WARNING (500-800 dòng)
- **Hành động:** Nên xem xét tách
- **Lý do:** File đang dài, có thể tách để dễ quản lý

### ✅ OK (≤500 dòng)
- **Hành động:** Không cần tách
- **Lý do:** Độ dài hợp lý

## Các pattern tách module

### 1. Tách Data Dictionary
**Khi nào:** File có data dictionary lớn (>50 entries)

**Cách làm:**
```
drug_database.py (8000 dòng)
  ↓
drug_database_data.py (chứa DRUG_DATABASE dict)
drug_database.py (chứa logic và functions)
```

### 2. Tách theo Class
**Khi nào:** File có nhiều classes (>3)

**Cách làm:**
```
calculator.py (có 5 classes)
  ↓
calculator/
  ├── __init__.py
  ├── class_a.py
  ├── class_b.py
  └── class_c.py
```

### 3. Tách theo chức năng
**Khi nào:** File có nhiều functions (>15) có thể nhóm

**Cách làm:**
```
utils.py (30 functions)
  ↓
utils/
  ├── __init__.py
  ├── converters.py
  ├── validators.py
  └── helpers.py
```

### 4. Tách theo Section
**Khi nào:** File rất dài với các section rõ ràng

**Cách làm:**
```
database.py (có comment sections: # ==========)
  ↓
database/
  ├── __init__.py
  ├── cardiovascular.py
  ├── antibiotics.py
  └── diabetes.py
```

## Files được tạo

1. **`module_analysis_report.md`**
   - Báo cáo chi tiết tất cả modules
   - Phân loại: Critical, Warning, OK
   - Đề xuất tách cho từng file

2. **`module_split_plan.md`** (tùy chọn)
   - Kế hoạch tách chi tiết
   - Checklist các bước thực hiện
   - Template cho từng file cần tách

## Ví dụ output

```
📊 TỔNG QUAN:
   - 🔴 CRITICAL (>800 dòng): 6 files
   - 🟡 WARNING (500-800 dòng): 4 files
   - ✅ OK (≤500 dòng): 218 files

📋 TOP 10 FILE DÀI NHẤT:
 1. 🔴  8735 dòng 📊 | drugs\drug_database.py
 2. 🔴  3206 dòng 📊 | antibiotics\antibiotics_data.py
 3. 🔴  1393 dòng 📊 | diagnosis\ddx_data.py
 ...
```

## Lưu ý

- Script tự động bỏ qua: `__pycache__`, `.pyc`, `venv`, `env`, `.git`
- Có thể tùy chỉnh ngưỡng trong `ModuleAnalyzer` class
- Báo cáo được tạo dạng Markdown, dễ đọc và chia sẻ

## Tùy chỉnh

Chỉnh sửa ngưỡng trong `utils/module_analyzer.py`:

```python
class ModuleAnalyzer:
    MAX_LINES_RECOMMENDED = 500  # Ngưỡng warning
    MAX_LINES_CRITICAL = 800     # Ngưỡng critical
    MAX_FUNCTIONS_RECOMMENDED = 20
    MAX_CLASSES_RECOMMENDED = 5
```

