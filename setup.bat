@echo off
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║  Student Performance Analysis - Setup Script              ║
echo ║  Windows (Python 3.8+)                                    ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo ✓ Python found
python --version
echo.

REM Create virtual environment
echo [1/3] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ❌ ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment created
echo.

REM Activate virtual environment
echo [2/3] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment activated
echo.

REM Install requirements
echo [3/3] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ ERROR: Failed to install dependencies
    echo Try running: pip install -r requirements.txt
    pause
    exit /b 1
)
echo ✓ Dependencies installed successfully
echo.

echo ╔════════════════════════════════════════════════════════════╗
echo ║  ✓ Setup Complete!                                         ║
echo ╠════════════════════════════════════════════════════════════╣
echo ║  To run the analysis:                                     ║
echo ║                                                            ║
echo ║  Option 1 - Python Script:                                ║
echo ║    python student_analysis.py                             ║
echo ║                                                            ║
echo ║  Option 2 - Jupyter Notebook:                             ║
echo ║    jupyter notebook                                        ║
echo ║    Then open student_analysis.ipynb                       ║
echo ║                                                            ║
echo ║  Option 3 - VS Code:                                      ║
echo ║    code .                                                  ║
echo ║    Click "Run" button on the script                       ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

pause
