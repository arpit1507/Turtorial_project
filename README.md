# CI/CD Pipeline and Full end to end project tutorial (replicated)

#### All the Steps in the Project

##### Project Template Creation
creating a template.py file for generating the project structure 
- current project structure
```
project/
│
├── config/
│   └── config.yaml
│
├── src/
│   ├── __init__.py
│   │
│   ├── components/
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── common.py
│   │
│   ├── constants/
│   │   └── __init__.py
│   │
│   └── config/
│       ├── __init__.py
│       └── configuration.py
│
├── templates/
│   └── index.html
│
├── research/
│   └── trials.ipynb
│
├── .github/
│   └── workflows/
│       └── .gitkeep
│
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── setup.py
├── README.md
├── .gitignore
├── main.py
└── template.py
```


##### Project Step and Requirment Installation
after creating the structure and the required files. we created steup.py and added all the required packages from python for this projects 
###### steps for this

- first create a conda environment
```bash
conda create -n tutorial python=3.9 -y
```
- then activate the environment
```bash
conda activate tutorial
```
- then run the python command to install all the requirements
```bash
pip install -r requirements.txt
```

###### Logging, Utils and Exception module

###### Project Workflows

###### All component Modular Code Implimentation

###### Training Pipeline

###### MLFlow 

###### DVC

###### Prediction Pipeline and App Creation

###### Docker 

###### Final CI/CD Deployment on AWS
