# Scripts tự động hóa

## Guideline Checker

Bộ script để kiểm tra và cập nhật guideline trong các bài viết y khoa.

### Scripts có sẵn

1. **`check_guideline_updates.py`** - Script chính để kiểm tra guideline
   - Quét tất cả các file markdown
   - Trích xuất thông tin guideline
   - Tạo báo cáo về file cần kiểm tra
   - Có thể tự động cập nhật ngày review

2. **`update_guideline_dates.py`** - Script nhanh để cập nhật ngày review
   - Đơn giản hơn, chỉ cập nhật ngày
   - Nhanh hơn khi chỉ cần cập nhật ngày

### Sử dụng nhanh

```bash
# Xem báo cáo tổng hợp ngắn gọn (nhanh nhất)
python scripts/check_guideline_summary.py

# Kiểm tra guideline và tạo báo cáo chi tiết
python scripts/check_guideline_updates.py

# Cập nhật ngày review (dry-run)
python scripts/update_guideline_dates.py --dry-run

# Thực sự cập nhật ngày review
python scripts/update_guideline_dates.py

# Xuất báo cáo ra JSON
python scripts/export_guideline_report.py --format json

# So sánh 2 báo cáo
python scripts/compare_guideline_reports.py report1.json report2.json

# Tạo HTML dashboard
python scripts/create_guideline_dashboard.py

# Kiểm tra format file
python scripts/validate_article_format.py

# Windows: Dùng batch script (nhanh hơn)
check_guidelines.bat summary
check_guidelines.bat report
check_guidelines.bat all
```

### Scripts bổ sung (nâng cao)

4. **`export_guideline_report.py`** - Xuất báo cáo ra JSON/CSV
   - Xuất báo cáo ra định dạng JSON hoặc CSV
   - Tích hợp với hệ thống khác
   - Phân tích bằng Excel/Google Sheets

5. **`compare_guideline_reports.py`** - So sánh 2 báo cáo
   - So sánh 2 báo cáo để xem thay đổi
   - Theo dõi thay đổi theo thời gian
   - Tìm file mới/xóa/thay đổi

6. **`check_guidelines.bat`** - Batch script cho Windows
   - Chạy nhanh các lệnh phổ biến
   - Không cần nhớ lệnh Python đầy đủ

7. **`create_guideline_dashboard.py`** - Tạo HTML dashboard
   - Tạo dashboard HTML đẹp mắt từ báo cáo
   - Hiển thị thống kê và danh sách file cần kiểm tra
   - Dễ xem và chia sẻ

8. **`validate_article_format.py`** - Kiểm tra format file
   - Kiểm tra format của các file markdown
   - Tìm lỗi và cảnh báo
   - Đảm bảo chất lượng bài viết

### Tài liệu chi tiết

- `README_GUIDELINE_CHECKER.md` - Hướng dẫn chi tiết đầy đủ
- `README_ADVANCED.md` - Tính năng nâng cao
- `QUICK_START_GUIDELINE_CHECKER.md` - Hướng dẫn nhanh
- `USAGE_EXAMPLES.md` - Ví dụ sử dụng và workflow

### Tự động hóa (Task Scheduler)

**Thiết lập chạy tự động hàng tháng:**

```powershell
# Chạy PowerShell với quyền Admin
cd D:\1app\medical
.\scripts\setup_task_scheduler.ps1
```

Xem hướng dẫn chi tiết: `HUONG_DAN_TASK_SCHEDULER.md` hoặc `scripts/README_TASK_SCHEDULER.md`

### Lịch trình khuyến nghị

- **Mỗi tháng:** Chạy kiểm tra và xem báo cáo (có thể tự động hóa)
- **Mỗi 6 tháng:** Cập nhật ngày review cho tất cả file

