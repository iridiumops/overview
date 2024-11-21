@echo off
chcp 65001 > nul

set "conda_env=iridium_overview"

echo Checking if conda environment exists...
call conda list --name %conda_env%
if %ERRORLEVEL% EQU 0 (
   echo Removing old conda environment...
   call conda env remove --name %conda_env%
) else (
   echo Environment %conda_env% not found.
)

echo Creating new conda environment from file...
call conda env create --name %conda_env% -f environment.yml

pause
goto :eof