@echo off

cd /d "%~dp0"

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not found. Please install Python 3.x from https://www.python.org/downloads/ and add it to your PATH.
    pause
    exit /b 1
)

python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r dependencies/requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install Python dependencies. Please check the error messages above.
    pause
    exit /b 1
)

python source_code/main.py

pause
