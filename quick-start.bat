@echo off
REM ========================================
REM Clinical Assistant - Quick Start
REM Fastest way to run the app
REM ========================================

cls
echo.
echo  ===================================================
echo     Clinical Assistant - Quick Start
echo  ===================================================
echo.
echo  Starting Streamlit app...
echo  Browser will open at: http://localhost:8501
echo.
echo  Press Ctrl+C to stop the server
echo  ===================================================
echo.

REM Run directly with python -m streamlit
python -m streamlit run app.py --server.port 8501 --server.headless false

pause

