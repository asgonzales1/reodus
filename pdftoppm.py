#!/usr/bin/env python3

# Author: Arvin Gonzales
# Author ID: reodus.x
# Date Created: 2025/09/18
# Purpose: INSTALL pdftoppm
### For converting pdf files to images like png or jpeg

sudo apt update
sudo apt install poppler-utils

# Run the command below to convert pdf to png
# If multiple pages, it will result output - #, like:
# output-1.png
# output-2.png
pdftoppm input.pdf output -png

# Run the command below to convert pdf to jpeg
pdftoppm input.pdf output -jpeg
