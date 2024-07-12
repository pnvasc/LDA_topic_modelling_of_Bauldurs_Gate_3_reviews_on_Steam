#!/bin/bash

# Create and activate virtual environment
python -m venv bg3_analysis
source bg3_analysis/bin/activate  

# Install required packages
pip install -r requirements.txt

# Save dependencies
pip freeze > requirements.txt

# Create kernel to run Jupyter notebook
python -m ipykernel install --user --name=bg3_analysis_kernel --display-name "Python (bg3_analysis_kernel)"

# Commit changes
git add .
git commit -m "Add project dependencies"