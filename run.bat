@echo off
REM ========================================
REM Clinical Assistant - Quick Start Script
REM ========================================

echo.
echo ========================================
echo   Clinical Assistant - Streamlit App
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python khong duoc cai dat!
    echo Vui long cai dat Python tu https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python da duoc cai dat
echo.

REM Check if in virtual environment
if defined VIRTUAL_ENV (
    echo [OK] Dang trong virtual environment: %VIRTUAL_ENV%
) else (
    echo [INFO] Khong trong virtual environment
    echo [INFO] Neu chua tao venv, chay: python -m venv venv
    echo [INFO] Sau do chay: venv\Scripts\activate
)
echo.

REM Check if streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Streamlit chua duoc cai dat!
    echo [INFO] Dang cai dat cac dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Cai dat that bai!
        pause
        exit /b 1
    )
    echo [OK] Cai dat thanh cong!
    echo.
)

echo [INFO] Kiem tra cac dependencies...
pip list | findstr streamlit >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Streamlit khong tim thay trong pip list
    echo [INFO] Dang cai dat lai...
    pip install streamlit pandas numpy openpyxl
)

echo.
echo ========================================
echo [OK] Moi thu san sang!
echo ========================================
echo.
echo [INFO] Dang khoi dong Streamlit app...
echo [INFO] App se mo trong trinh duyet o: http://localhost:8501
echo.
echo [TIP] Nhan Ctrl+C de dung server
echo.
echo ========================================
echo.

REM Start Streamlit app
python -m streamlit run app.py

REM If streamlit exits
echo.
echo ========================================
echo [INFO] Streamlit da dung
echo ========================================
pause

