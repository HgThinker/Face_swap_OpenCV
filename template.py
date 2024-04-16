import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "weather_website_crawler"

list_of_files = [
    'image/README.md',
    'src/README.md',
    'scripts/README.md',
    'output/README.md',
    'src/FACE_SWAP/README.md'
    'setup.py',
    'README.md'
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "": 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f: 
            pass 
            logging.info(f"Creating empty file: {filepath}")
    else: 
        logging.info(f"{filename} already exists")