#!/bin/bash

# Activate conda environment
conda activate iridium_overview

# Run python build script
echo "Building Iridium Overview"
python src/build.py

if [ $? -eq 0 ]; then
   echo "Success"
else
   echo "An ERROR occurred during build process."
fi

read -p "Press Enter to exit..."
