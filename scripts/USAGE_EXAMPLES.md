# Ví dụ sử dụng Guideline Checker Scripts

## Kịch bản sử dụng phổ biến

### 1. Kiểm tra nhanh guideline (hàng tuần)

```bash
python scripts/check_guideline_summary.py
```

Kết quả: Hiển thị báo cáo tổng hợp ngắn gọn trên terminal, không tạo file.

**Khi nào dùng:** Khi muốn xem nhanh tình trạng guideline mà không cần báo cáo chi tiết.

---

### 2. Kiểm tra đầy đủ và lưu báo cáo (hàng tháng)

```bash
python scripts/check_guideline_updates.py --report-only
```

Kết quả: 
- Tạo file báo cáo chi tiết tại `reports/guideline_check_YYYY-MM-DD.md`
- Hiển thị tổng kết trên terminal

**Khi nào dùng:** Khi cần báo cáo chi tiết để xem xét và lưu trữ.

---

### 3. Xem file nào sẽ được cập nhật ngày (kiểm tra trước)

```bash
python scripts/update_guideline_dates.py --dry-run
```

Kết quả: Liệt kê các file sẽ được cập nhật nhưng không thực sự cập nhật.

**Khi nào dùng:** Trước khi cập nhật ngày, muốn xem trước những file sẽ bị thay đổi.

---

### 4. Cập nhật ngày review cho tất cả file (mỗi 6 tháng)

```bash
# Bước 1: Kiểm tra trước
python scripts/update_guideline_dates.py --dry-run

# Bước 2: Commit code hiện tại (quan trọng!)
git add .
git commit -m "Before updating guideline review dates"

# Bước 3: Cập nhật thực sự
python scripts/update_guideline_dates.py
```

Kết quả: Tất cả file có `last_reviewed` hoặc `**Cập nhật:**` sẽ được cập nhật thành ngày hiện tại.

**Khi nào dùng:** Định kỳ 6 tháng để đánh dấu rằng đã kiểm tra lại các file.

---

### 5. Kiểm tra và cập nhật trong một lần (không khuyến khích)

```bash
# Dry-run để xem sẽ cập nhật gì
python scripts/check_guideline_updates.py --update-dates

# Thực sự cập nhật
python scripts/check_guideline_updates.py --update-dates --force
```

**Lưu ý:** Chỉ dùng khi chắc chắn muốn cập nhật tất cả. Nên tách riêng bước kiểm tra và cập nhật.

---

### 6. Tạo báo cáo với tên file tùy chỉnh

```bash
python scripts/check_guideline_updates.py --output reports/my_custom_report_2025_02.md
```

**Khi nào dùng:** Khi muốn lưu báo cáo với tên cụ thể hoặc so sánh nhiều báo cáo.

---

### 7. Workflow đầy đủ (khuyến nghị hàng tháng)

```bash
# Bước 1: Xem tổng quan nhanh
python scripts/check_guideline_summary.py

# Bước 2: Tạo báo cáo chi tiết nếu cần
python scripts/check_guideline_updates.py --report-only

# Bước 3: Mở và xem báo cáo
# File: reports/guideline_check_YYYY-MM-DD.md

# Bước 4: Kiểm tra guideline quan trọng trên website chính thức
# - ESC: https://www.escardio.org/Guidelines
# - ACC/AHA: https://www.acc.org/guidelines
# - ADA: https://diabetesjournals.org/care/issue/48/Supplement_1
# - KDIGO: https://kdigo.org/guidelines/
# - GOLD: https://goldcopd.org/
# - GINA: https://ginasthma.org/

# Bước 5: Cập nhật guideline mới nếu có (thủ công)
```

---

### 8. Tự động hóa với cron/GitHub Actions

**Cron (Linux/Mac):**

```bash
# Thêm vào crontab (crontab -e)
# Chạy mỗi tháng vào ngày 1, lúc 9h sáng
0 9 1 * * cd /path/to/medical && python scripts/check_guideline_updates.py --report-only >> logs/guideline_check.log 2>&1
```

**GitHub Actions:**

```yaml
name: Monthly Guideline Check

on:
  schedule:
    - cron: '0 9 1 * *'  # Ngày 1 mỗi tháng, 9h sáng UTC
  workflow_dispatch:  # Cho phép chạy thủ công

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Check guidelines
        run: python scripts/check_guideline_updates.py --report-only
      
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: guideline-report
          path: reports/
      
      - name: Create summary
        run: python scripts/check_guideline_summary.py >> summary.txt
      
      - name: Upload summary
        uses: actions/upload-artifact@v3
        with:
          name: guideline-summary
          path: summary.txt
```

---

## So sánh các script

| Script | Mục đích | Tốc độ | Output |
|--------|----------|--------|--------|
| `check_guideline_summary.py` | Xem tổng quan nhanh | ⚡ Rất nhanh | Terminal |
| `check_guideline_updates.py --report-only` | Báo cáo chi tiết | 🐢 Chậm hơn | File markdown |
| `update_guideline_dates.py` | Cập nhật ngày | ⚡ Nhanh | Cập nhật file |

## Tips

1. **Luôn chạy dry-run trước:** Kiểm tra trước khi thực sự cập nhật file
2. **Commit trước khi cập nhật:** Đảm bảo có thể rollback nếu cần
3. **Xem báo cáo tổng hợp trước:** Dùng `check_guideline_summary.py` để xem nhanh
4. **Kiểm tra thủ công:** Script chỉ kiểm tra chu kỳ, cần kiểm tra thực tế trên website
5. **Lưu báo cáo:** Báo cáo chi tiết hữu ích để theo dõi lịch sử

