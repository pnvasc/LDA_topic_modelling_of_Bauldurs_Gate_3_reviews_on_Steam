#!/bin/bash

# Create a new directory for project
mkdir LDA_topic_modelling_of_Bauldurs_Gate_3_reviews_on_Steam
cd LDA_topic_modelling_of_Bauldurs_Gate_3_reviews_on_Steam

# Initialize a git repository
git init

# Create a .gitignore file
echo "# Python
*.pyc
__pycache__/
venv/
*.db
.env
# IDE
.vscode/
.idea/
# Misc
.DS_Store
config.py
setup_project.sh" > .gitignore

# Create a README file
echo "# Topic modelling of Bauldurs Gate 3 reviews on Steam

This project performs both LDA and Transformers based topic modelling on Steam reviews of the game Baldur's Gate 3, then compares results of the two methods" > README.md

# Make initial commit
git add .
git commit -m "Initial commit: Project setup"

echo "Project setup complete!"

source ./setup_virtual_env.sh