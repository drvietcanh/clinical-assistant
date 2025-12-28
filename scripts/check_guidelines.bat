@echo off
REM Batch script để chạy nhanh các lệnh kiểm tra guideline
REM Sử dụng: check_guidelines.bat [summary|report|update|all]

if "%1"=="" (
    echo.
    echo ========================================
    echo  GUIDELINE CHECKER - Quick Commands
    echo ========================================
    echo.
    echo Sử dụng: check_guidelines.bat [command]
    echo.
    echo Commands:
    echo   summary  - Xem báo cáo tổng hợp ngắn gọn
    echo   report   - Tạo báo cáo chi tiết
    echo   update   - Cập nhật ngày review (dry-run)
    echo   force    - Thực sự cập nhật ngày review
    echo   all      - Chạy summary và report
    echo.
    exit /b 1
)

if "%1"=="summary" (
    echo Đang tạo báo cáo tổng hợp...
    python scripts/check_guideline_summary.py
    exit /b 0
)

if "%1"=="report" (
    echo Đang tạo báo cáo chi tiết...
    python scripts/check_guideline_updates.py --report-only
    echo.
    echo Báo cáo đã được lưu tại: reports\guideline_check_*.md
    exit /b 0
)

if "%1"=="update" (
    echo Đang kiểm tra file sẽ được cập nhật (dry-run)...
    python scripts/update_guideline_dates.py --dry-run
    echo.
    echo Chạy 'check_guidelines.bat force' để thực sự cập nhật
    exit /b 0
)

if "%1"=="force" (
    echo ⚠️  CẢNH BÁO: Lệnh này sẽ cập nhật file!
    echo.
    pause
    echo Đang cập nhật ngày review...
    python scripts/update_guideline_dates.py
    exit /b 0
)

if "%1"=="all" (
    echo ========================================
    echo  1. Đang tạo báo cáo tổng hợp...
    echo ========================================
    python scripts/check_guideline_summary.py
    echo.
    echo ========================================
    echo  2. Đang tạo báo cáo chi tiết...
    echo ========================================
    python scripts/check_guideline_updates.py --report-only
    echo.
    echo ========================================
    echo  Hoàn thành!
    echo ========================================
    echo Báo cáo đã được lưu tại: reports\guideline_check_*.md
    exit /b 0
)

echo Lệnh không hợp lệ: %1
exit /b 1

