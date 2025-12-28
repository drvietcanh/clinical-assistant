@echo off
echo ========================================
echo KIEM TRA DONG BO GIT
echo ========================================
echo.

cd /d "%~dp0"

echo [1] Kiem tra trang thai git...
git status
echo.

echo [2] Kiem tra commit gan nhat...
git log --oneline -5
echo.

echo [3] Kiem tra ket noi remote...
git remote -v
echo.

echo [4] Kiem tra co thay doi chua commit...
git diff --stat
echo.

echo ========================================
echo KET QUA:
echo ========================================
git status --short
echo.

echo Neu co file thay doi, chay:
echo   git add .
echo   git commit -m "Luu thay doi"
echo   git push
echo.

pause

