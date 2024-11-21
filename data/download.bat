@echo off

:: find curl or use copy from bin folder
set "curl=curl.exe"
where %curl% >nul 2>nul
if NOT ERRORLEVEL 0 (
   set "curl=./../bin/curl.exe"
)

del invGroups.csv
del invTypes.csv
%curl% https://www.fuzzwork.co.uk/dump/latest/invGroups.csv --retry 3 --output invGroups.csv
%curl% https://www.fuzzwork.co.uk/dump/latest/invTypes.csv --retry 3 --output invTypes.csv

pause
goto :eof
