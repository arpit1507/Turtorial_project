import os 
from pathlib import Path

project_name = "Tutorial_Project"

list_of_files = [
    "main.py",
    "README.md",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/utils/common.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "requirements.txt",
    ".gitignore",
    "setup.py",
]

for file in list_of_files:
    Path(file).parent.mkdir(parents=True, exist_ok=True)
    if not os.path.exists(file):
        with open(file, "w") as f:
            pass
        print(f"Created file: {file}")
    else:
        print(f"File already exists: {file}")
