@echo off
REM Script để kiểm tra và sửa số thập phân dư không có ý nghĩa lâm sàng

echo ========================================
echo KIEM TRA SO THAP PHAN DU
echo ========================================
echo.

REM Kiểm tra xem có tham số không
if "%1"=="" (
    echo Usage:
    echo   fix_decimal_precision.bat check    - Chi kiem tra va bao cao
    echo   fix_decimal_precision.bat fix      - Tu dong sua
    echo   fix_decimal_precision.bat dry-run  - Xem se sua gi nhung khong sua that
    echo.
    echo Mac dinh: check
    set MODE=check
) else (
    set MODE=%1
)

if "%MODE%"=="check" (
    echo [MODE: CHECK] Chi kiem tra va tao bao cao...
    python utils/fix_decimal_precision.py --check --report DECIMAL_PRECISION_REPORT.md
) else if "%MODE%"=="fix" (
    echo [MODE: FIX] Tu dong sua cac loi...
    python utils/fix_decimal_precision.py --fix --report DECIMAL_PRECISION_REPORT.md
) else if "%MODE%"=="dry-run" (
    echo [MODE: DRY-RUN] Xem se sua gi nhung khong sua that...
    python utils/fix_decimal_precision.py --fix --dry-run --report DECIMAL_PRECISION_REPORT.md
) else (
    echo Loi: Mode khong hop le: %MODE%
    echo Su dung: check, fix, hoac dry-run
    exit /b 1
)

echo.
echo ========================================
echo HOAN THANH
echo ========================================
pause

