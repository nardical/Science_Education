@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\streamlit.exe" (
    echo Virtual environment not found. From this folder, run:
    echo   python -m venv .venv
    echo   .venv\Scripts\activate
    echo   pip install -r requirements.txt
    pause
    exit /b 1
)

echo Updating Science Playground from GitHub ...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0update-from-github.ps1"

echo Stopping any leftover Science Playground still using port 8501 ...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-NetTCPConnection -LocalPort 8501 -State Listen -ErrorAction SilentlyContinue | Where-Object { $_.OwningProcess -gt 0 } | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }"

echo Starting Science Playground at http://localhost:8501 ...
echo If a tab is already open there, press Ctrl+Shift+R or use a new tab.
".venv\Scripts\streamlit.exe" run "science_playground\app.py" --server.port 8501 --server.fileWatcherType poll
pause
