@echo off
REM ========================================
REM Clinical Assistant - Setup Script
REM One-time setup for first run
REM ========================================

echo.
echo ========================================
echo   Clinical Assistant - Setup
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python khong duoc cai dat!
    echo Vui long cai dat Python tu https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python version:
python --version
echo.

REM Create virtual environment
echo [INFO] Dang tao virtual environment...
if exist venv (
    echo [WARNING] Thu muc venv da ton tai!
    set /p choice="Ban co muon xoa va tao lai? (y/n): "
    if /i "%choice%"=="y" (
        echo [INFO] Dang xoa venv cu...
        rmdir /s /q venv
        python -m venv venv
        echo [OK] Da tao venv moi
    ) else (
        echo [INFO] Giu nguyen venv cu
    )
) else (
    python -m venv venv
    echo [OK] Da tao venv moi
)
echo.

REM Activate virtual environment
echo [INFO] Dang kich hoat virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Kich hoat venv that bai!
    pause
    exit /b 1
)
echo [OK] Virtual environment da duoc kich hoat
echo.

REM Upgrade pip
echo [INFO] Dang nang cap pip...
python -m pip install --upgrade pip
echo.

REM Install dependencies
echo [INFO] Dang cai dat dependencies tu requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Cai dat that bai!
    pause
    exit /b 1
)
echo.

echo ========================================
echo [SUCCESS] Setup hoan tat!
echo ========================================
echo.
echo Cac buoc tiep theo:
echo.
echo 1. Kich hoat virtual environment:
echo    venv\Scripts\activate
echo.
echo 2. Chay ung dung:
echo    run.bat
echo    HOAC
echo    python -m streamlit run app.py
echo.
echo 3. Mo trinh duyet va truy cap:
echo    http://localhost:8501
echo.
echo ========================================
pause

