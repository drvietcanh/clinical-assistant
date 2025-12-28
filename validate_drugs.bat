@echo off
chcp 65001 >nul
echo ================================================================================
echo KIỂM TRA DỮ LIỆU THUỐC
echo ================================================================================
echo.

echo [1/4] Đang chạy kiểm tra toàn diện...
python comprehensive_drug_validation.py
if %errorlevel% neq 0 (
    echo.
    echo ❌ Lỗi khi chạy validation!
    pause
    exit /b 1
)

echo.
echo [2/4] Đang export các vấn đề cần sửa...
python export_validation_issues.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể export (có thể do chưa có báo cáo)
)

echo.
echo [3/4] Đang tạo báo cáo HTML...
python generate_html_report.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể tạo báo cáo HTML
)

echo.
echo [4/6] Đang phân tích lỗi có thể tự động sửa...
python auto_fix_common_errors.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể phân tích lỗi
)

echo.
echo [5/6] Đang tạo danh sách công việc ưu tiên...
python create_priority_task_list.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể tạo danh sách công việc
)

echo.
echo [6/8] Đang tạo code để áp dụng sửa lỗi...
python apply_auto_fixes_to_file.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể tạo code sửa lỗi
)

echo.
echo [7/8] Đang tạo templates cho các field thiếu...
python generate_field_templates.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể tạo templates
)

echo.
echo [8/10] Đang cập nhật tiến trình...
python update_progress.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể cập nhật tiến trình
)

echo.
echo [9/10] Đang tạo checklist công việc...
python create_workflow_checklist.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể tạo checklist
)

echo.
echo [10/10] Đang lưu snapshot và so sánh...
python compare_validation_results.py
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Cảnh báo: Không thể so sánh kết quả
)

echo.
echo ================================================================================
echo HOÀN THÀNH!
echo ================================================================================
echo.
echo Các file đã tạo:
echo   - drug_validation_report.json (Báo cáo JSON)
echo   - drug_validation_report.txt (Báo cáo text)
echo   - drug_validation_report.html (Báo cáo HTML - mở trong trình duyệt)
echo   - validation_errors_by_priority.txt (Lỗi theo ưu tiên)
echo   - validation_missing_fields_summary.txt (Tóm tắt field thiếu)
echo   - validation_drugs_needing_fixes.txt (Chi tiết thuốc cần sửa)
echo   - validation_errors.csv (File CSV cho Excel)
echo   - auto_fix_suggestions.txt (Gợi ý sửa lỗi tự động)
echo   - priority_tasks.md (Danh sách công việc ưu tiên - Markdown)
echo   - priority_tasks.txt (Danh sách công việc ưu tiên - Text)
echo   - priority_tasks.json (Danh sách công việc ưu tiên - JSON)
echo   - auto_fix_code_to_add.py (Code để áp dụng sửa lỗi)
echo   - field_templates.md (Templates cho các field thiếu)
echo   - field_templates.py (Templates Python)
echo   - progress_summary.txt (Tóm tắt tiến độ)
echo   - validation_checklist.md (Checklist công việc)
echo   - validation_snapshots/ (Thư mục snapshots)
echo.
pause

