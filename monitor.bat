@echo off
chcp 65001 > nul

:: activate Anaconda ENV
call activate.bat iridium_overview

:: run python script
python src/monitor.py

pause > nul
goto :eof