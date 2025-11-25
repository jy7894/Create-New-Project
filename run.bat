@echo off

py --version >nul 2>&1
if %errorlevel%==0 (
    set PY_CMD=py
    goto :done
)

python --version >nul 2>&1
if %errorlevel%==0 (
    set PY_CMD=python
    goto :done
)

python3 --version >nul 2>&1
if %errorlevel%==0 (
    set PY_CMD=python3
    goto :done
)

echo No Python installation found.
exit /b 1

:done
set projectName=%~1
set language=%~2
set givenPath=%~3

if "%givenPath%"=="" (
    set givenPath=%CD%
)

"%PY_CMD%" "%~dp0src\main.py" "%projectName%" "%language%" "%givenPath%"