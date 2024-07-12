# Chicken Disease Classification

DATASET link: https://github.com/Diksha1312/Data_To_Experiment/raw/master/Chicken-fecal-images.zip

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Diksha1312/Deploy-Chicken-Disease-Classification-App-on-AWS-EC2-Using-CICD-setup-with-Docker-and-Github-Actions
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


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 277676390796.dkr.ecr.eu-north-1.amazonaws.com/chicken-disease-classification

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = eu-north-1

    AWS_ECR_LOGIN_URI = 

    ECR_REPOSITORY_NAME = 

2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 
