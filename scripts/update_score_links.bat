@echo off
REM Quick script to update score links
REM Run this after adding new articles/protocols

echo [INFO] Updating score links...
python scripts/auto_link_scores_to_content.py

if %ERRORLEVEL% EQU 0 (
    echo [OK] Score links updated successfully!
) else (
    echo [ERROR] Failed to update score links
    pause
)

