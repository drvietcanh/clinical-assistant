@echo off
echo ======================================================================
echo XOA CACHE STREAMLIT
echo ======================================================================
echo.

echo Dang xoa cache...
rmdir /s /q "%USERPROFILE%\.streamlit\cache" 2>nul
rmdir /s /q ".streamlit\cache" 2>nul
rmdir /s /q "__pycache__" 2>nul
rmdir /s /q "drugs\__pycache__" 2>nul
rmdir /s /q "pages\__pycache__" 2>nul
rmdir /s /q "components\__pycache__" 2>nul
rmdir /s /q "utils\__pycache__" 2>nul
rmdir /s /q "config\__pycache__" 2>nul

echo.
echo ======================================================================
echo HOAN TAT!
echo ======================================================================
echo Khoi dong lai Streamlit de ap dung.
echo Chay: streamlit run app.py
echo ======================================================================
pause
