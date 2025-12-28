# Hướng dẫn thiết lập Task Scheduler tự động

## Tổng quan

Có 2 cách thiết lập Task Scheduler:
1. **Thủ công** - Theo hướng dẫn trong `HUONG_DAN_TASK_SCHEDULER.md`
2. **Tự động** - Dùng script PowerShell (nhanh hơn)

---

## Cách 1: Tự động (Khuyến nghị)

### Bước 1: Mở PowerShell với quyền Administrator

1. Nhấn `Win + X`
2. Chọn **"Windows PowerShell (Admin)"** hoặc **"Terminal (Admin)"**
3. Xác nhận UAC nếu được hỏi

### Bước 2: Chạy script

```powershell
cd D:\1app\medical
.\scripts\setup_task_scheduler.ps1
```

### Bước 3: Tùy chỉnh (Optional)

```powershell
# Chạy vào ngày 15 mỗi tháng, lúc 9h sáng
.\scripts\setup_task_scheduler.ps1 -DayOfMonth 15 -Time "09:00"

# Đổi tên task
.\scripts\setup_task_scheduler.ps1 -TaskName "My Guideline Check"
```

### Bước 4: Test task

```powershell
# Chạy task ngay lập tức để test
Start-ScheduledTask -TaskName "Monthly Guideline Check"

# Xem kết quả
Get-ScheduledTask -TaskName "Monthly Guideline Check"
```

---

## Cách 2: Thủ công

Xem hướng dẫn chi tiết trong file: `HUONG_DAN_TASK_SCHEDULER.md`

---

## Kiểm tra task đã chạy

### Xem lịch sử

1. Mở **Task Scheduler**
2. Tìm task **"Monthly Guideline Check"**
3. Click chuột phải → **Properties** → Tab **History**

### Xem file kết quả

Sau khi task chạy, kiểm tra các file trong `reports/`:
- `guideline_check_YYYY-MM-DD.md` - Báo cáo chi tiết
- `guideline_report_latest.json` - Export JSON
- `GUIDELINE_TODO.md` - TODO checklist
- `dashboard.html` - HTML dashboard

---

## Troubleshooting

### Lỗi: "Script cannot be loaded because running scripts is disabled"

**Giải pháp:**
```powershell
# Chạy PowerShell với quyền Admin, sau đó:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Lỗi: "Access is denied"

**Giải pháp:**
- Đảm bảo chạy PowerShell với quyền Administrator
- Hoặc thiết lập thủ công theo `HUONG_DAN_TASK_SCHEDULER.md`

### Task không chạy

**Kiểm tra:**
1. Task có được Enable không?
2. Trigger có đúng không?
3. Computer có bật vào thời gian đã lên lịch không?
4. Xem log trong Task Scheduler History

---

## Quản lý task

### Xem thông tin task

```powershell
Get-ScheduledTask -TaskName "Monthly Guideline Check"
```

### Chạy task thủ công

```powershell
Start-ScheduledTask -TaskName "Monthly Guideline Check"
```

### Tạm dừng task

```powershell
Disable-ScheduledTask -TaskName "Monthly Guideline Check"
```

### Bật lại task

```powershell
Enable-ScheduledTask -TaskName "Monthly Guideline Check"
```

### Xóa task

```powershell
Unregister-ScheduledTask -TaskName "Monthly Guideline Check" -Confirm:$false
```

---

## Tùy chỉnh

### Chạy hàng tuần thay vì hàng tháng

Cần sửa script hoặc thiết lập thủ công trong Task Scheduler.

### Chạy nhiều lần trong ngày

Thiết lập thủ công trong Task Scheduler → Triggers → Edit → Repeat task.

---

## Kết quả mong đợi

Sau khi thiết lập, mỗi tháng hệ thống sẽ tự động:

✅ Quét 82 file markdown  
✅ Tạo báo cáo chi tiết  
✅ Export JSON mới nhất  
✅ Sinh TODO checklist  
✅ Tạo HTML dashboard  

**Tất cả file sẽ được lưu trong `reports/`**

