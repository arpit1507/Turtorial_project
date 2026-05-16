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
|   |
|   ├── pipeline/
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

##### Logging, Utils and Exception module
For creating a logging system i updated the init file in Tutorial_Project in src folder.
we need to create a message which will decribe the level time and module of each log and we can see every log in the running_logs.txt in logs folder

##### Project Workflows
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml
9. app.py


###### All component Modular Code Implimentation

###### Training Pipeline

###### MLFlow 

###### DVC

###### Prediction Pipeline and App Creation

###### Docker 

###### Final CI/CD Deployment on AWS
