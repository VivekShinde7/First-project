import logging
import os
from pathlib import Path

list_of_files=[
    r".github\workflows\.gitkeep",
    r"src\__init__.py",
    r"src\components\__init__.py",
    r"src\components\data_ingestion.py",
    r"src\components\data_transformation.py",
    r"src\components\model_trainer.py",
    r"src\components\model_evaluation.py",
    r"src\pipeline\__init__.py",
    r"src\pipeline\training_pipeline.py",
    r"src\pipeline\prediction_pipeline.py",
    r"src\utils\__init__.py",
    r"src\utils\utils.py",
    r"src\logger\login.py",
    r"src\exception\exception"
    r"tests\unit\__init__.py",
    r"tests\integration\__init__.py",
    r"init_setup.sh",
    r"requirements.txt",
    r"requirements_dev.txt",
    r"setup.py",
    r"setup.cfg",
    r"pyproject.toml",
    r"tox.ini",
    r"experiment\experiments.ipynb"

]

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        #logging.info(f"Creating directory: {filedir} for file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass # create an enpty file 