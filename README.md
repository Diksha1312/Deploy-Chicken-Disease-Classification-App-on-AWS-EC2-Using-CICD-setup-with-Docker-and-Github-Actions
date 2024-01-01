Chicken Disease Classification

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update configuration manager in src config
5. Update the components
6. Update pipeline
7. Update main.py
8. Update dvc.yaml


DATASET link: https://github.com/Diksha1312/Data_To_Experiment/raw/master/Chicken-fecal-images.zip

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Diksha1312/Chicken-Disease-Classification
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```



### STEP 02- Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- 

1. To run main file
```bash
python main.py
```

2. To run from app using Flask
```bash
python app.py
```

3. To run through DVC, use below commands
```bash
1. dvc init
2. dvc repro
3. dvc dag
```
