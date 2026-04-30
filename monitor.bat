@echo off
chcp 65001 > nul

:: Monitoring script to get notified
:: Use task scheduler or cron to run daily after server downtime

:: Activate Anaconda ENV
call activate.bat iridium_overview

:: Run python script
python src/monitor.py

if %ERRORLEVEL% EQU 0 (
    echo Success: no changes detected, exiting...
    color 20
    timeout /T 5
    goto :eof
) else (
    if %ERRORLEVEL% EQU 2 (
        echo Info: changes were detected
        color 30
    ) else (
        echo Error: general error
        color 40
    )
    pause > nul
    goto :eof
)
