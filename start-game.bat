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

echo Starting Science Playground at http://localhost:8501 ...
".venv\Scripts\streamlit.exe" run "science_playground\app.py"
pause
