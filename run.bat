@echo off
cd /d "%~dp0"

:: Try py first
py --version >nul 2>&1
if %errorlevel%==0 (
    echo Python found using "py"
    set PY_CMD=py
    goto :done
)

:: Try python next
python --version >nul 2>&1
if %errorlevel%==0 (
    echo Python found using "python"
    set PY_CMD=python
    goto :done
)

echo No Python installation found.
exit /b 1

:done
set projectName=%1
set language=%2
set path=%3

%PY_CMD% "src/main.py" "%projectName%" "%language%" "%path%"