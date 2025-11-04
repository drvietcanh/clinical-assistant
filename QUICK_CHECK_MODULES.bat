@echo off
REM Script nhanh để kiểm tra module - Double click để chạy
echo ================================================================================
echo KIEM TRA MODULE - PHAN TICH DO DAI VA DE XUAT TACH
echo ================================================================================
echo.

python check_modules.py --auto

echo.
echo ================================================================================
echo Hoan thanh! Xem ket qua trong:
echo - module_analysis_report.md (bao cao chi tiet)
echo - module_split_plan.md (ke hoach tach)
echo ================================================================================
pause

