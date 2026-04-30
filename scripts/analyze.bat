@echo off
chcp 65001 > nul

:: activate Anaconda ENV
call activate.bat iridium_overview

:: interactively ask for file path
set /p "yaml_file=Enter full path to exported yaml file:"
echo.
:: run python analyze script with file path as argument
python src/analyze.py "%yaml_file%"

pause > nul
goto :eof