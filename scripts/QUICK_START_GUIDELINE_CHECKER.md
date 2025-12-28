# Hướng dẫn nhanh - Guideline Checker

## Chạy kiểm tra guideline

```bash
# Kiểm tra và tạo báo cáo
python scripts/check_guideline_updates.py

# Xem báo cáo tại: reports/guideline_check_YYYY-MM-DD.md
```

## Cập nhật ngày review (dry-run)

```bash
# Xem những file sẽ được cập nhật (không thực sự cập nhật)
python scripts/check_guideline_updates.py --update-dates

# Hoặc dùng script nhanh hơn:
python scripts/update_guideline_dates.py --dry-run
```

## Thực sự cập nhật ngày review

⚠️ **Cảnh báo:** Lệnh này sẽ sửa file. Commit code trước khi chạy!

```bash
python scripts/check_guideline_updates.py --update-dates --force

# Hoặc:
python scripts/update_guideline_dates.py
```

## Lịch trình khuyến nghị

**Mỗi tháng:**
```bash
python scripts/check_guideline_updates.py --report-only
```

**Mỗi 6 tháng:**
```bash
python scripts/check_guideline_updates.py --update-dates --force
```

## Xem báo cáo

Báo cáo được lưu tại: `reports/guideline_check_YYYY-MM-DD.md`

Báo cáo sẽ liệt kê:
- Các file cần kiểm tra guideline
- Guideline hiện tại của mỗi file
- Lý do tại sao cần kiểm tra (dựa trên chu kỳ cập nhật)

