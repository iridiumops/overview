#!/bin/bash

# Monitoring script to get notified
# Use task scheduler or cron to run daily after server downtime

# Set readable ANSI escape color codes
RED='\033[0;31m'
BLUE='\033[0;36m'
GREEN='\033[0;32m'
RESET='\033[0m'

# Activate conda environment
conda activate iridium_overview

# Run python script
python src/monitor.py

status=$?

if [ $status -eq 0 ]; then
    printf "${GREEN}Success: no changes detected, exiting...${RESET}\n"
    sleep 5
    exit 0
else
    if [ $status -eq 2 ]; then
        printf "${BLUE}Info: changes were detected${RESET}\n"
    else
        printf "${RED}Error: general error${RESET}\n"
    fi
    read -p "Press Enter to exit..."
fi
