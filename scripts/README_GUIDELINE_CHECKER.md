# Hướng dẫn sử dụng Guideline Checker

Script tự động kiểm tra và cập nhật guideline trong các bài viết y khoa.

## Cài đặt

Script sử dụng Python 3.7+ với các thư viện chuẩn (không cần cài đặt thêm).

## Sử dụng

### 1. Chạy kiểm tra và tạo báo cáo

```bash
python scripts/check_guideline_updates.py
```

Lệnh này sẽ:
- Quét tất cả các file `.md` trong `content/articles/`
- Trích xuất thông tin guideline từ mỗi file
- Tạo báo cáo tại `reports/guideline_check_YYYY-MM-DD.md`

### 2. Chỉ tạo báo cáo (không cập nhật gì)

```bash
python scripts/check_guideline_updates.py --report-only
```

### 3. Kiểm tra và cập nhật ngày review (dry-run)

```bash
python scripts/check_guideline_updates.py --update-dates
```

Lệnh này sẽ hiển thị những file sẽ được cập nhật nhưng **không thực sự cập nhật** (dry-run mode).

### 4. Thực sự cập nhật ngày review

```bash
python scripts/check_guideline_updates.py --update-dates --force
```

⚠️ **Cảnh báo:** Lệnh này sẽ thực sự sửa các file. Nên commit code trước khi chạy.

### 5. Chỉ định file output

```bash
python scripts/check_guideline_updates.py --output reports/my_report.md
```

## Cách hoạt động

### 1. Trích xuất thông tin guideline

Script sẽ tìm thông tin guideline từ:
- **Metadata (frontmatter):** `last_reviewed`, `guideline_version`
- **Header:** Dòng `> **Cập nhật:** Tháng X/YYYY`
- **Tài liệu tham khảo:** Section `**Tài liệu tham khảo chính:**`

### 2. Xác định guideline cần kiểm tra

Script sử dụng chu kỳ cập nhật ước tính:
- **ESC, ACC/AHA, KDIGO, ACR, EULAR:** ~3 năm
- **ADA, GOLD, GINA:** Hàng năm
- **ATS, IDSA:** ~5 năm

Nếu `năm hiện tại >= năm guideline + chu kỳ`, script sẽ đánh dấu là "cần kiểm tra".

### 3. Tự động cập nhật ngày

Khi dùng `--update-dates`, script sẽ:
- Cập nhật `last_reviewed: YYYY-MM` trong frontmatter
- Cập nhật `**Cập nhật:** Tháng X/YYYY` trong header

## Ví dụ output

### Báo cáo sẽ bao gồm:

```
# Báo cáo kiểm tra Guideline
**Ngày tạo:** 2025-02-18 10:30:00
**Năm hiện tại:** 2025

## Tổng quan
- Tổng số file: 82
- Cần kiểm tra: 15
- Không cần kiểm tra: 67
- Lỗi: 0

## Các file cần kiểm tra guideline

### suy-tim-hfref-4-tru-dieu-tri.md
**Đường dẫn:** content/articles/suy-tim-hfref-4-tru-dieu-tri.md
**Guideline hiện tại:**
- ESC 2021
- ACC/AHA 2022
**Lý do cần kiểm tra:**
- ESC 2021 có thể đã có bản mới (chu kỳ ~3 năm, hiện tại 2025)
- Last reviewed: 2023-01
```

## Lịch trình chạy định kỳ

### Khuyến nghị

1. **Mỗi tháng:** Chạy kiểm tra và xem báo cáo
   ```bash
   python scripts/check_guideline_updates.py --report-only
   ```

2. **Mỗi 6 tháng:** Chạy và cập nhật ngày review
   ```bash
   python scripts/check_guideline_updates.py --update-dates --force
   ```

3. **Trước mỗi release:** Kiểm tra lại toàn bộ
   ```bash
   python scripts/check_guideline_updates.py --report-only
   ```

### Tự động hóa (tùy chọn)

Có thể tạo cron job hoặc GitHub Actions để chạy tự động:

**GitHub Actions (ví dụ):**
```yaml
name: Check Guideline Updates

on:
  schedule:
    - cron: '0 0 1 * *'  # Chạy mỗi tháng
  workflow_dispatch:  # Cho phép chạy thủ công

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: python scripts/check_guideline_updates.py --report-only
      - uses: actions/upload-artifact@v2
        with:
          name: guideline-report
          path: reports/
```

## Lưu ý

1. **Script chỉ kiểm tra, không tự động cập nhật guideline:** Bạn vẫn cần tự kiểm tra và cập nhật guideline mới thủ công.

2. **Chu kỳ cập nhật là ước tính:** Các guideline có thể không tuân theo chu kỳ chính xác.

3. **Cần xác nhận thủ công:** Sau khi có báo cáo, nên kiểm tra lại các guideline quan trọng trên trang web chính thức.

4. **Backup trước khi cập nhật:** Luôn commit code trước khi chạy `--update-dates --force`.

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

## Troubleshooting

### Lỗi: "Thư mục không tồn tại"
- Kiểm tra đường dẫn `ARTICLES_DIR` trong script
- Đảm bảo đang chạy từ thư mục gốc của project

### Không tìm thấy guideline
- Kiểm tra format của guideline trong file markdown
- Có thể cần điều chỉnh regex pattern trong `_extract_guidelines_from_text()`

### Báo cáo quá dài
- File được đánh dấu "không cần kiểm tra" chỉ hiển thị 20 đầu tiên
- Có thể sửa số lượng trong code nếu cần

