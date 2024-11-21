@echo off
chcp 65001 > nul

echo Exporting conda environment to file...

call activate.bat iridium_overview
call conda env export > environment.yml

pause
goto :eof