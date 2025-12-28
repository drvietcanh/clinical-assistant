@echo off
echo ========================================
echo Commit va Push cac thay doi giao dien thuoc
echo ========================================
echo.

REM Check if git is available
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Git khong tim thay trong PATH
    echo Vui long cai dat Git hoac them Git vao PATH
    echo.
    echo Ban co the commit thu cong bang cach:
    echo 1. Mo Git Bash hoac Command Prompt
    echo 2. cd "d:\1 medical"
    echo 3. Chay cac lenh sau:
    echo.
    echo git add pages/Drug_Detail.py
    echo git add drugs/drug_info_components/detail_view.py
    echo git add drugs/drug_info_components/card_components.py
    echo git add static/drug_detail_mobile.css
    echo git add docs/DRUG_UI_*.md
    echo.
    echo git commit -m "feat: Cai thien giao dien trang chi tiet thuoc"
    echo git push
    pause
    exit /b 1
)

echo Dang kiem tra git status...
git status
echo.

echo Dang add cac file da thay doi...
git add pages/Drug_Detail.py
git add drugs/drug_info_components/detail_view.py
git add drugs/drug_info_components/card_components.py
git add static/drug_detail_mobile.css
git add docs/DRUG_UI_RESEARCH_AND_IMPROVEMENT_PLAN.md
git add docs/DRUG_UI_IMPROVEMENTS_SUMMARY.md
git add docs/DRUG_UI_FINAL_SUMMARY.md
git add docs/DRUG_UI_ERROR_CHECK_REPORT.md
echo.

echo Dang commit...
git commit -m "feat: Cai thien giao dien trang chi tiet thuoc - hien dai, chuyen nghiep, de su dung

- Tao trang rieng cho tung thuoc (pages/Drug_Detail.py)
- Enhanced header voi badges, icons, color coding theo nhom thuoc
- At-a-glance summary box voi thong tin quan trong
- Enhanced quick facts box voi card layout
- Quick action buttons (So sanh, Tinh lieu, TDM, Tuong tac)
- Enhanced dosing section voi visual cards
- Categorized side effects (common/serious/rare)
- Enhanced contraindications voi color coding
- Enhanced pregnancy/lactation section
- Enhanced interactions voi severity levels
- Enhanced monitoring va TDM sections
- Related drugs suggestions tu cung nhom
- Mobile CSS optimization
- Tai lieu nghien cuu va ke hoach cai tien

Dua tren nghien cuu: Drugs.com, WebMD, Epocrates, UpToDate"
echo.

echo Dang push len remote...
git push
echo.

echo ========================================
echo Hoan thanh!
echo ========================================
pause

