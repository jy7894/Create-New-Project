@echo off

for %%C in (py python python3) do (
    %%C --version >nul 2>&1
    if not errorlevel 1 (
        set PY_CMD=%%C
        goto :done
    )
)

echo No Python installation found.
exit /b 1

:done
set projectName=%~1
set language=%~2
set givenPath=%~3

if "%projectName%"=="" (
    echo projectName:
    set /p projectName=
)

if "%language%"=="" (
    echo language:
    set /p language=
)

if "%givenPath%"=="" (
    echo path^<Optional^>:
    set /p givenPath=
    if "%givenPath%"=="" (
        set givenPath=%CD%
    )
)

"%PY_CMD%" "%~dp0src\main.py" "%projectName%" "%language%" "%givenPath%"

setlocal