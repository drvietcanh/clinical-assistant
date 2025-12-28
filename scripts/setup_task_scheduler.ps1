# Script PowerShell để thiết lập Task Scheduler tự động
# Chạy với quyền Administrator: Right-click -> Run as Administrator

param(
    [string]$TaskName = "Monthly Guideline Check",
    [string]$ProjectPath = "D:\1app\medical",
    [int]$DayOfMonth = 1,
    [string]$Time = "08:00"
)

# Kiểm tra quyền Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "❌ Cần chạy với quyền Administrator!" -ForegroundColor Red
    Write-Host "   Right-click PowerShell -> Run as Administrator" -ForegroundColor Yellow
    exit 1
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  THIẾT LẬP TASK SCHEDULER" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Kiểm tra đường dẫn project
if (-not (Test-Path $ProjectPath)) {
    Write-Host "❌ Đường dẫn không tồn tại: $ProjectPath" -ForegroundColor Red
    exit 1
}

$batchFile = Join-Path $ProjectPath "run_guideline_check.bat"
if (-not (Test-Path $batchFile)) {
    Write-Host "❌ Không tìm thấy file: $batchFile" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Đường dẫn project: $ProjectPath" -ForegroundColor Green
Write-Host "✅ File batch: $batchFile" -ForegroundColor Green
Write-Host ""

# Xóa task cũ nếu tồn tại
$existingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existingTask) {
    Write-Host "⚠️  Task đã tồn tại. Đang xóa task cũ..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# Tạo action
$action = New-ScheduledTaskAction -Execute "cmd.exe" `
    -Argument "/c `"$batchFile`"" `
    -WorkingDirectory $ProjectPath

# Tạo trigger (hàng tháng, ngày 1, lúc 8h sáng)
$trigger = New-ScheduledTaskTrigger -Monthly -DaysOfMonth $DayOfMonth -At $Time

# Tạo settings
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -RunOnlyIfNetworkAvailable:$false `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2)

# Tạo principal (chạy với quyền user hiện tại)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive

# Đăng ký task
try {
    Register-ScheduledTask `
        -TaskName $TaskName `
        -Action $action `
        -Trigger $trigger `
        -Settings $settings `
        -Principal $principal `
        -Description "Tự động kiểm tra và cập nhật guideline mỗi tháng" `
        -Force | Out-Null
    
    Write-Host "✅ Đã tạo task thành công!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Thông tin task:" -ForegroundColor Cyan
    Write-Host "  - Tên: $TaskName" -ForegroundColor White
    Write-Host "  - Chạy: Ngày $DayOfMonth mỗi tháng, lúc $Time" -ForegroundColor White
    Write-Host "  - File: $batchFile" -ForegroundColor White
    Write-Host ""
    Write-Host "Để test task, chạy:" -ForegroundColor Yellow
    Write-Host "  Start-ScheduledTask -TaskName `"$TaskName`"" -ForegroundColor White
    Write-Host ""
    Write-Host "Để xem task:" -ForegroundColor Yellow
    Write-Host "  Get-ScheduledTask -TaskName `"$TaskName`"" -ForegroundColor White
    Write-Host ""
    Write-Host "Để xóa task:" -ForegroundColor Yellow
    Write-Host "  Unregister-ScheduledTask -TaskName `"$TaskName`" -Confirm:`$false" -ForegroundColor White
    
} catch {
    Write-Host "❌ Lỗi khi tạo task: $_" -ForegroundColor Red
    exit 1
}

