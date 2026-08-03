#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Student Performance Analysis - Setup Script              ║"
echo "║  macOS/Linux (Python 3.8+)                                ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "✓ Python found"
python3 --version
echo ""

# Create virtual environment
echo "[1/3] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to create virtual environment"
    exit 1
fi
echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "[2/3] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to activate virtual environment"
    exit 1
fi
echo "✓ Virtual environment activated"
echo ""

# Install requirements
echo "[3/3] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to install dependencies"
    echo "Try running: pip install -r requirements.txt"
    exit 1
fi
echo "✓ Dependencies installed successfully"
echo ""

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  ✓ Setup Complete!                                         ║"
echo "╠════════════════════════════════════════════════════════════╣"
echo "║  To run the analysis:                                     ║"
echo "║                                                            ║"
echo "║  Option 1 - Python Script:                                ║"
echo "║    python student_analysis.py                             ║"
echo "║                                                            ║"
echo "║  Option 2 - Jupyter Notebook:                             ║"
echo "║    jupyter notebook                                        ║"
echo "║    Then open student_analysis.ipynb                       ║"
echo "║                                                            ║"
echo "║  Option 3 - VS Code:                                      ║"
echo "║    code .                                                  ║"
echo "║    Click "Run" button on the script                       ║"
echo "║                                                            ║"
echo "║  Remember to activate venv first:                         ║"
echo "║    source venv/bin/activate                               ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
