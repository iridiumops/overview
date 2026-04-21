#!/bin/bash

echo "Exporting conda environment to file..."

conda activate iridium_overview
conda env export > environment.yaml

read -p "Press Enter to exit..."
