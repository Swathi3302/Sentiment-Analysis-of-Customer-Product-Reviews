@echo off
title Sentiment AI
cd /d "%~dp0"
echo ===================================================
echo   Starting Sentiment AI Web Application
echo   Opening in browser at http://localhost:8000
echo ===================================================
if exist "venv\Scripts\python.exe" (
    venv\Scripts\python.exe server.py
) else (
    python server.py
)
pause
