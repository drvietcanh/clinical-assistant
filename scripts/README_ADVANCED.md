# Guideline Checker - Tính năng nâng cao

## Scripts bổ sung

### 1. `export_guideline_report.py` - Xuất báo cáo ra JSON/CSV

Xuất báo cáo guideline ra định dạng JSON hoặc CSV để tích hợp với hệ thống khác hoặc phân tích thêm.

**Sử dụng:**

```bash
# Xuất ra JSON (mặc định)
python scripts/export_guideline_report.py

# Xuất ra CSV
python scripts/export_guideline_report.py --format csv

# Chỉ định file output
python scripts/export_guideline_report.py --format json --output reports/my_report.json
```

**Output:**

- **JSON:** Đầy đủ thông tin, dễ xử lý bằng code
- **CSV:** Dễ mở trong Excel, Google Sheets để phân tích

**Ví dụ JSON:**
```json
{
  "generated_at": "2025-12-26T13:30:00",
  "total_files": 82,
  "needs_check": 44,
  "files": [
    {
      "file": "suy-tim-hfref-4-tru-dieu-tri.md",
      "guidelines": [
        {"name": "ESC", "year": 2021},
        {"name": "ACC/AHA", "year": 2022}
      ],
      "needs_check": true,
      "reasons": [...]
    }
  ]
}
```

---

### 2. `compare_guideline_reports.py` - So sánh 2 báo cáo

So sánh 2 báo cáo để xem có gì thay đổi (file mới, file xóa, thay đổi guideline, v.v.)

**Sử dụng:**

```bash
# Tạo 2 báo cáo
python scripts/export_guideline_report.py --output reports/report1.json
# ... sau một thời gian ...
python scripts/export_guideline_report.py --output reports/report2.json

# So sánh
python scripts/compare_guideline_reports.py reports/report1.json reports/report2.json
```

**Output:**
- File mới được thêm
- File bị xóa
- File thay đổi trạng thái (cần kiểm tra ↔ không cần)
- File có thay đổi guideline hoặc ngày review

**Use case:**
- So sánh báo cáo trước và sau khi cập nhật guideline
- Theo dõi thay đổi theo thời gian
- Kiểm tra xem đã cập nhật những gì

---

### 3. `check_guidelines.bat` - Batch script cho Windows

Script batch để chạy nhanh các lệnh phổ biến.

**Sử dụng:**

```cmd
# Xem báo cáo tổng hợp
check_guidelines.bat summary

# Tạo báo cáo chi tiết
check_guidelines.bat report

# Xem file sẽ được cập nhật (dry-run)
check_guidelines.bat update

# Thực sự cập nhật
check_guidelines.bat force

# Chạy cả summary và report
check_guidelines.bat all
```

**Lợi ích:**
- Không cần nhớ lệnh Python đầy đủ
- Nhanh và tiện lợi
- Có thể tạo shortcut trên desktop

---

## Workflow nâng cao

### Workflow 1: Theo dõi thay đổi theo thời gian

```bash
# Tháng 1
python scripts/export_guideline_report.py --output reports/2025-01.json

# Tháng 2
python scripts/export_guideline_report.py --output reports/2025-02.json

# So sánh
python scripts/compare_guideline_reports.py reports/2025-01.json reports/2025-02.json
```

### Workflow 2: Tích hợp với hệ thống khác

```bash
# Xuất ra JSON
python scripts/export_guideline_report.py --format json --output reports/latest.json

# Xử lý bằng Python script khác
python my_custom_analysis.py reports/latest.json
```

### Workflow 3: Báo cáo hàng tháng tự động

Tạo scheduled task hoặc cron job:

```bash
# Windows Task Scheduler
# Chạy mỗi tháng ngày 1, lúc 9h sáng
python scripts\export_guideline_report.py --format json --output reports\$(date +%%Y-%%m).json
python scripts\check_guideline_updates.py --report-only
```

### Workflow 4: CI/CD Integration

```yaml
# .github/workflows/guideline-check.yml
name: Guideline Check

on:
  schedule:
    - cron: '0 9 1 * *'  # Ngày 1 mỗi tháng
  workflow_dispatch:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Generate report
        run: |
          python scripts/check_guideline_updates.py --report-only
          python scripts/export_guideline_report.py --format json
      
      - name: Upload reports
        uses: actions/upload-artifact@v3
        with:
          name: guideline-reports
          path: reports/
      
      - name: Compare with previous
        if: hashFiles('reports/*.json') != ''
        run: |
          # So sánh với báo cáo tháng trước (nếu có)
          python scripts/compare_guideline_reports.py \
            reports/previous.json \
            reports/guideline_report_$(date +%Y-%m-%d).json || true
```

---

## Tùy chỉnh và mở rộng

### Thêm guideline mới vào chu kỳ

Sửa file `check_guideline_updates.py`:

```python
GUIDELINE_CYCLE = {
    # ... existing ...
    "NEW_GUIDELINE": 2,  # Chu kỳ 2 năm
}
```

### Thay đổi format báo cáo

Sửa các hàm `generate_report()` trong `check_guideline_updates.py` để thay đổi format markdown.

### Tích hợp với database

Sử dụng `export_guideline_report.py` để xuất JSON, sau đó import vào database:

```python
import json
from scripts.export_guideline_report import GuidelineChecker

checker = GuidelineChecker(ARTICLES_DIR)
results = checker.scan_all_articles()

# Lưu vào database
for result in results:
    # Save to database
    db.save_guideline_check(result)
```

---

## Tips và tricks

1. **Kết hợp với git:** Commit báo cáo JSON để theo dõi lịch sử
2. **Tạo dashboard:** Dùng JSON để tạo dashboard hiển thị tình trạng guideline
3. **Alert system:** Tạo script tự động gửi email khi có guideline cần kiểm tra
4. **Integration:** Tích hợp với project management tools (Jira, Trello, etc.)

---

## Troubleshooting

### Lỗi encoding khi xuất CSV

CSV sử dụng `utf-8-sig` để Excel có thể mở đúng. Nếu vẫn lỗi, thử dùng JSON.

### So sánh không chính xác

Đảm bảo 2 báo cáo được tạo từ cùng một version của script.

### Batch script không chạy

Đảm bảo file `.bat` được lưu với encoding Windows (ANSI hoặc UTF-8 với BOM).

