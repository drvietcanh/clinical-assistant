# Hướng dẫn thiết lập Task Scheduler cho Guideline Checker

## Tổng quan

Thiết lập Windows Task Scheduler để tự động chạy kiểm tra guideline mỗi tháng, không cần chạy thủ công.

---

## Bước 1: Tạo script batch

File `run_guideline_check.bat` đã được tạo sẵn trong thư mục gốc project.

**Kiểm tra:**
- Đảm bảo file `run_guideline_check.bat` tồn tại
- Đường dẫn project: `D:\1app\medical`

---

## Bước 2: Test script thủ công

**Trước khi thiết lập Task Scheduler, hãy test script:**

1. Double-click vào `run_guideline_check.bat`
2. Hoặc mở Command Prompt và chạy:
   ```cmd
   cd D:\1app\medical
   run_guideline_check.bat
   ```

3. Kiểm tra kết quả:
   - Các file trong `reports/` đã được tạo
   - Không có lỗi

**Nếu có lỗi:** Kiểm tra Python đã được cài đặt và có trong PATH.

---

## Bước 3: Thiết lập Task Scheduler

### 3.1. Mở Task Scheduler

1. Nhấn `Win + R`
2. Gõ `taskschd.msc` và Enter
3. Hoặc tìm "Task Scheduler" trong Start Menu

### 3.2. Tạo Task mới

1. Click **"Create Basic Task..."** ở bên phải
2. **Name:** `Monthly Guideline Check`
3. **Description:** `Tự động kiểm tra và cập nhật guideline mỗi tháng`
4. Click **Next**

### 3.3. Thiết lập Trigger (Khi nào chạy)

1. Chọn **Monthly** (Hàng tháng)
2. Click **Next**
3. **Start date:** Chọn ngày hôm nay hoặc ngày 1 tháng sau
4. **Start time:** Chọn giờ (ví dụ: 08:00)
5. **Monthly:** Chọn ngày 1 mỗi tháng
6. Click **Next**

### 3.4. Thiết lập Action (Làm gì)

1. Chọn **Start a program**
2. Click **Next**
3. **Program/script:** 
   ```
   cmd.exe
   ```
4. **Add arguments (optional):**
   ```
   /c "D:\1app\medical\run_guideline_check.bat"
   ```
5. **Start in (optional):**
   ```
   D:\1app\medical
   ```
6. Click **Next**

### 3.5. Hoàn tất

1. Đánh dấu **"Open the Properties dialog for this task when I click Finish"**
2. Click **Finish**

### 3.6. Cấu hình nâng cao (Optional)

Trong Properties dialog:

1. **General tab:**
   - ✅ Đánh dấu **"Run whether user is logged on or not"** (nếu muốn chạy khi không đăng nhập)
   - ✅ Đánh dấu **"Run with highest privileges"** (nếu cần quyền admin)

2. **Conditions tab:**
   - Có thể bỏ chọn **"Start the task only if the computer is on AC power"** (nếu muốn chạy cả khi dùng pin)

3. **Settings tab:**
   - ✅ Đánh dấu **"Allow task to be run on demand"** (cho phép chạy thủ công)
   - ✅ Đánh dấu **"Run task as soon as possible after a scheduled start is missed"** (chạy bù nếu bỏ lỡ)

4. Click **OK**

---

## Bước 4: Test Task

### 4.1. Chạy thủ công

1. Trong Task Scheduler, tìm task **"Monthly Guideline Check"**
2. Click chuột phải → **Run**
3. Kiểm tra kết quả:
   - Xem **Last Run Result** (phải là `0x0` = thành công)
   - Kiểm tra file trong `reports/` đã được tạo

### 4.2. Xem log

1. Click chuột phải vào task → **Properties**
2. Tab **History** → Xem log chi tiết

---

## Bước 5: Kiểm tra định kỳ

### Sau 1 tháng:

1. Kiểm tra task đã chạy chưa:
   - Mở Task Scheduler
   - Xem **Last Run Time** của task

2. Kiểm tra file mới:
   - `reports/guideline_check_YYYY-MM-DD.md`
   - `reports/guideline_report_latest.json`
   - `reports/GUIDELINE_TODO.md`
   - `reports/dashboard.html`

---

## Troubleshooting

### Lỗi: "The system cannot find the file specified"

**Nguyên nhân:** Đường dẫn không đúng hoặc Python không có trong PATH.

**Giải pháp:**
1. Kiểm tra đường dẫn project: `D:\1app\medical`
2. Test Python: Mở Command Prompt, gõ `python --version`
3. Nếu không có Python trong PATH, sử dụng đường dẫn đầy đủ:
   ```
   C:\Python39\python.exe scripts\check_guideline_updates.py --report-only
   ```

### Lỗi: "Access is denied"

**Nguyên nhân:** Không đủ quyền.

**Giải pháp:**
1. Chạy Task Scheduler với quyền Administrator
2. Hoặc trong Properties → General → chọn **"Run whether user is logged on or not"** và nhập password

### Task không chạy tự động

**Kiểm tra:**
1. Task có được Enable không? (Click chuột phải → Enable)
2. Trigger có đúng không?
3. Computer có bật vào thời gian đã lên lịch không?

---

## Tùy chỉnh

### Chạy hàng tuần thay vì hàng tháng

1. Mở Properties của task
2. Tab **Triggers** → Edit
3. Đổi từ **Monthly** sang **Weekly**
4. Chọn ngày trong tuần (ví dụ: Thứ 2)

### Chạy nhiều lần trong ngày

1. Tab **Triggers** → Edit
2. Đánh dấu **"Repeat task every"**
3. Chọn khoảng thời gian (ví dụ: 1 hour)
4. Chọn **"for a duration of"** (ví dụ: 1 day)

### Gửi email khi hoàn thành (Advanced)

Cần thêm script gửi email. Có thể tạo script Python riêng hoặc dùng PowerShell.

---

## Lưu ý

1. **Đảm bảo Python đã cài đặt** và có trong PATH
2. **Test script trước** khi thiết lập Task Scheduler
3. **Kiểm tra định kỳ** xem task có chạy đúng không
4. **Backup** các file báo cáo quan trọng

---

## Kết quả mong đợi

Sau khi thiết lập, mỗi tháng hệ thống sẽ tự động:

✅ Quét tất cả 82 file markdown  
✅ Tạo báo cáo chi tiết  
✅ Export JSON mới nhất  
✅ Sinh TODO checklist  
✅ Tạo HTML dashboard  

**Tất cả file sẽ được lưu trong `reports/`**

---

## Hỗ trợ

Nếu gặp vấn đề, kiểm tra:
- Log trong Task Scheduler History
- File `run_guideline_check.bat` có chạy được thủ công không
- Python và các script có hoạt động bình thường không

