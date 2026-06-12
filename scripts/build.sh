#!/bin/bash

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"

# Activate conda environment
conda activate iridium_overview

# Run python build script
echo "Building Iridium Overview"
python "${SCRIPT_DIR}/../src/build.py"

if [ $? -eq 0 ]; then
   echo "Success"
else
   echo "An ERROR occurred during build process."
fi

read -p "Press Enter to exit..."
