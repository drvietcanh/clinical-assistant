@echo off
REM Script tự động chạy kiểm tra guideline hàng tháng
REM Sử dụng: Double-click hoặc chạy từ Task Scheduler

echo ========================================
echo  GUIDELINE CHECKER - Auto Run
echo ========================================
echo.

cd /d "%~dp0"

echo [1/4] Đang tạo báo cáo chi tiết...
python scripts\check_guideline_updates.py --report-only
if errorlevel 1 (
    echo ❌ Lỗi khi tạo báo cáo chi tiết
    exit /b 1
)

echo.
echo [2/4] Đang export JSON mới nhất...
python scripts\export_guideline_report.py --format json --output reports\guideline_report_latest.json
if errorlevel 1 (
    echo ❌ Lỗi khi export JSON
    exit /b 1
)

echo.
echo [3/4] Đang tạo TODO checklist...
python scripts\generate_guideline_todo.py
if errorlevel 1 (
    echo ❌ Lỗi khi tạo TODO
    exit /b 1
)

echo.
echo [4/4] Đang tạo HTML dashboard...
python scripts\create_guideline_dashboard.py
if errorlevel 1 (
    echo ❌ Lỗi khi tạo dashboard
    exit /b 1
)

echo.
echo ========================================
echo  ✅ Hoàn thành!
echo ========================================
echo.
echo Các file đã được tạo:
echo   - reports\guideline_check_*.md
echo   - reports\guideline_report_latest.json
echo   - reports\GUIDELINE_TODO.md
echo   - reports\dashboard.html
echo.

pause

