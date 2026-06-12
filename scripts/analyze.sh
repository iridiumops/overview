#!/bin/bash

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"

# Activate conda environment
conda activate iridium_overview

# Interactively ask for file path
read -p "Enter full path to exported yaml file: " yaml_file
echo

# Run python analyze script with file path as argument
python "${SCRIPT_DIR}/../src/analyze.py" "$yaml_file"

read -p "Press Enter to exit..."
