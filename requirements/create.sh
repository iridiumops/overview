#!/bin/bash

conda_env=iridium_overview

echo "Checking if conda environment exists..."
conda list --name $conda_env
if [ $? -eq 0 ]; then
   echo "Removing old conda environment..."
   conda env remove --name $conda_env
else
   echo "Environment $conda_env not found."
fi

echo "Creating new conda environment from file..."
conda env create --name $conda_env -f environment.yaml

read -p "Press Enter to exit..."
