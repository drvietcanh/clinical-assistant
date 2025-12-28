# Hướng dẫn sử dụng Script kiểm tra Guideline

## Tổng quan

Đã tạo bộ script Python để tự động kiểm tra và cập nhật guideline trong các bài viết y khoa. Script sẽ:
- Quét tất cả các file markdown
- Trích xuất thông tin guideline hiện tại
- Đánh giá xem guideline có cần kiểm tra không (dựa trên chu kỳ cập nhật)
- Tạo báo cáo chi tiết
- Tự động cập nhật ngày review (tùy chọn)

## Cài đặt

Không cần cài đặt gì thêm. Script sử dụng Python 3.7+ với thư viện chuẩn.

## Sử dụng

### 1. Kiểm tra guideline và tạo báo cáo

```bash
python scripts/check_guideline_updates.py
```

Kết quả:
- Tạo file báo cáo tại `reports/guideline_check_YYYY-MM-DD.md`
- Hiển thị tổng kết: số file cần kiểm tra, không cần kiểm tra, lỗi

### 2. Chỉ tạo báo cáo (không làm gì khác)

```bash
python scripts/check_guideline_updates.py --report-only
```

### 3. Xem file nào sẽ được cập nhật ngày (dry-run)

```bash
# Dùng script chính
python scripts/check_guideline_updates.py --update-dates

# Hoặc dùng script nhanh
python scripts/update_guideline_dates.py --dry-run
```

### 4. Thực sự cập nhật ngày review

⚠️ **Cảnh báo:** Lệnh này sẽ sửa file. Nên commit code trước khi chạy!

```bash
# Dùng script chính
python scripts/check_guideline_updates.py --update-dates --force

# Hoặc dùng script nhanh
python scripts/update_guideline_dates.py
```

### 5. Chỉ định file output

```bash
python scripts/check_guideline_updates.py --output reports/my_custom_report.md
```

## Ví dụ kết quả

### Báo cáo sẽ bao gồm:

```
# Báo cáo kiểm tra Guideline
**Ngày tạo:** 2025-02-18 10:30:00
**Năm hiện tại:** 2025

## Tổng quan
- Tổng số file: 82
- Cần kiểm tra: 44
- Không cần kiểm tra: 38
- Lỗi: 0

## Các file cần kiểm tra guideline

### suy-tim-hfref-4-tru-dieu-tri.md
**Đường dẫn:** content/articles/suy-tim-hfref-4-tru-dieu-tri.md
**Guideline hiện tại:**
- ESC 2021
- ACC/AHA 2022
**Lý do cần kiểm tra:**
- ESC 2021 có thể đã có bản mới (chu kỳ ~3 năm, hiện tại 2025)
- ACC/AHA 2022 có thể đã có bản mới (chu kỳ ~3 năm, hiện tại 2025)
**Last reviewed:** 2023-01
```

## Cách hoạt động

### 1. Trích xuất thông tin guideline

Script tìm thông tin từ:
- **Frontmatter (metadata):** `last_reviewed`, `guideline_version`
- **Header:** `> **Cập nhật:** Tháng X/YYYY`
- **Tài liệu tham khảo:** Section `**Tài liệu tham khảo chính:**`

### 2. Xác định guideline cần kiểm tra

Script sử dụng chu kỳ cập nhật ước tính:
- **ESC, ACC/AHA, KDIGO, ACR, EULAR:** ~3 năm
- **ADA, GOLD, GINA:** Hàng năm
- **ATS, IDSA:** ~5 năm

Nếu `năm hiện tại >= năm guideline + chu kỳ` → đánh dấu "cần kiểm tra"

### 3. Cập nhật ngày

Khi dùng `--update-dates --force`, script sẽ:
- Cập nhật `last_reviewed: YYYY-MM` trong frontmatter
- Cập nhật `**Cập nhật:** Tháng X/YYYY` trong header

## Lịch trình khuyến nghị

### Hàng tháng

```bash
python scripts/check_guideline_updates.py --report-only
```

Xem báo cáo và kiểm tra các guideline quan trọng.

### Mỗi 6 tháng

```bash
# 1. Kiểm tra và xem báo cáo
python scripts/check_guideline_updates.py --report-only

# 2. Cập nhật ngày review
python scripts/update_guideline_dates.py
```

### Trước mỗi release

```bash
python scripts/check_guideline_updates.py --report-only
```

Kiểm tra toàn bộ và cập nhật guideline nếu cần.

## Tự động hóa (tùy chọn)

### GitHub Actions

Có thể tạo workflow để chạy tự động mỗi tháng:

```yaml
name: Check Guideline Updates

on:
  schedule:
    - cron: '0 0 1 * *'  # Ngày 1 mỗi tháng
  workflow_dispatch:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - run: python scripts/check_guideline_updates.py --report-only
      - uses: actions/upload-artifact@v3
        with:
          name: guideline-report
          path: reports/
```

### Cron job (Linux/Mac)

```bash
# Chạy mỗi tháng vào ngày 1, lúc 9h sáng
0 9 1 * * cd /path/to/medical && python scripts/check_guideline_updates.py --report-only
```

### Task Scheduler (Windows)

1. Mở Task Scheduler
2. Tạo task mới
3. Trigger: Monthly, ngày 1
4. Action: Start a program
   - Program: `python`
   - Arguments: `scripts/check_guideline_updates.py --report-only`
   - Start in: `D:\1app\medical`

## Lưu ý quan trọng

1. **Script chỉ kiểm tra, không tự động cập nhật guideline mới:** Bạn vẫn cần tự kiểm tra và cập nhật guideline mới từ nguồn chính thức.

2. **Chu kỳ cập nhật là ước tính:** Các guideline có thể không tuân theo chu kỳ chính xác.

3. **Cần xác nhận thủ công:** Sau khi có báo cáo, nên kiểm tra lại các guideline quan trọng trên trang web chính thức của tổ chức.

4. **Backup trước khi cập nhật:** Luôn commit code trước khi chạy `--update-dates --force`.

5. **Script không thay đổi nội dung guideline:** Chỉ cập nhật ngày review, không tự động thay đổi thông tin guideline.

## Troubleshooting

### Lỗi: "Thư mục không tồn tại"
- Đảm bảo đang chạy từ thư mục gốc của project
- Kiểm tra đường dẫn `ARTICLES_DIR` trong script

### Không tìm thấy guideline
- Kiểm tra format của guideline trong file markdown
- Có thể cần điều chỉnh regex pattern

### Báo cáo quá dài
- File "không cần kiểm tra" chỉ hiển thị 20 đầu tiên
- Có thể sửa trong code nếu cần

## Tùy chỉnh

### Thay đổi chu kỳ guideline

Sửa dictionary `GUIDELINE_CYCLE` trong `check_guideline_updates.py`:

```python
GUIDELINE_CYCLE = {
    "ESC": 3,  # Thay đổi số năm
    "ADA": 1,
    # ...
}
```

### Thêm guideline mới

Thêm vào `GUIDELINE_CYCLE`:

```python
GUIDELINE_CYCLE = {
    # ...
    "NEW_GUIDELINE": 2,  # Chu kỳ 2 năm
}
```

