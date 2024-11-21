@echo off
chcp 65001 > nul

:: activate Anaconda ENV
call activate.bat iridium_overview

:: run python build script
echo Building Iridium Overview
python src/build.py

if %ERRORLEVEL% EQU 0 (
   echo Success
) else (
   echo An ERROR occured during build process.
)

pause > nul
goto :eof