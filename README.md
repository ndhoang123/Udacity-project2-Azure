# Udacity-project2-Azure
This is repo for project 2 of azure devops

[![Python application test with Github Actions](https://github.com/ndhoang123/Udacity-project2-Azure/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/ndhoang123/Udacity-project2-Azure/actions/workflows/pythonapp.yml)
# Overview

The comprehensive guidelines is to guide you to build CI/CD by combining the Azure Devops and Github, Github Action.

## Project Plan
In order to work efficienly and be on time, we have to make a plan as well as the board to trace the status of our steps on the project:

- A [project plan](https://docs.google.com/spreadsheets/d/1TFcDyEj9_2rUecir7h3jiAT2XoYQoI8STsnASP4vSQM/edit?usp=sharing)

- A [board of our project](https://trello.com/invite/b/KI1ZIwDl/ATTI59d916a4f9a454fa5095d56bc2431a576FE94015/udacity-project2-tracking) is used to see the status of tasks

## Instructions

### Architectural Diagram
The diagram shows the workflow of this project
<img width="784" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/fd4fe015-4e56-4e6f-8ac1-a04a4a6dc604">

## Deploy the app in Azure Cloud Shell

In Azure Cloud Shell, clone the repo:
```
git clone git@github.com:ndhoang123/Udacity-project2-Azure.git
```
<img width="1279" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/5400ac73-4b56-442c-a02c-d9591bf271ec">

Change into the new directory:
```
cd Udacity-project2-Azure
```

Create a virtual environment:
```
python3 -m venv ~/.udacityproject
```

Activate the virtual environment:
```
source ~/.udacityproject/bin/activate
```

Install dependencies in the virtual environment and run tests:
```
make all
```
<img width="1265" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/ab0040cb-0b22-4706-849d-4719bc65556e">

Make changes and test GitHub action

<img width="643" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/f5c86724-1d82-4133-b295-97ca4a87da51">

The screenshots of Github Action
<img width="1271" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/34cae035-fd5d-439a-b9ed-e390a86abe2b">

## Deploy the app to an Azure App Service

Create an App Service in Azure. 

Use this [file](https://github.com/HTTP2916/azure-devops-project2.1/blob/main/commands.sh) to create new App Services

```
az webapp up --name flask-app-predict-1119 --resource-group Udacity --sku B1 --logs --runtime "PYTHON:3.8"
```

Next, create the pipeline in Azure DevOps. The basic steps are:

- Go to [https://dev.azure.com](https://dev.azure.com) and sign in.
- Create a new private project.
- Create a new service connection to ARM, select the subscription and the app service.
- Create the Agent pool
- Create a new pipeline linked to your GitHub repo using GiThub YAML File.

Screenshot of the App Service:
<img width="1058" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/d720bb04-ed6f-4331-8917-1d21eead1121">

Screenshot of Azure DevOps Project:
<img width="1279" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/73bf36c2-e894-4cb6-a4bf-d2beca10056e">

The screenshots of success pipeline:
<img width="1275" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/a1bde850-96d1-4101-9735-fa58c8f6b691">

To test the app running in Azure App Service, edit line 28 of the make_predict_azure_app.sh script with the DNS name of your app. Then run the script:
```
./make_predict_azure_app.sh 
```

If it's working you should see the following output:

<img width="643" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/f5c86724-1d82-4133-b295-97ca4a87da51">

When it's completed, navigate to your page and as you can see, the web app is running.
<img width="1280" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/205a7996-364b-4458-a9ca-addba6b1cf15">


View the app logs:

To view the log-in Cloud Shell
```
az webapp log tail --name flask-app-predict-1119 --resource-group Udacity
```
<img width="1264" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/efa63db8-28c9-456f-8fba-7a47ddd04b33">

## Load test

I use Locust to perform load tests on my local computer. 

Install locust:
```
pip install locust
```
<img width="1277" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/c0e08fd4-1bf1-4d6f-837e-e82d458cc0d2">

Start load test:
```
locust -f locustfile.py --host https://flask-app-predict-1119.azurewebsites.net/ --users 100 --spawn-rate 5 
```
Open a browser and go to [http://localhost:8089](http://localhost:8089) then click Start Swarming. Running the following below:
<img width="1280" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/b2faddca-3d31-4520-a384-d9bc873abc3a">
<img width="1277" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/307f19ef-bca1-4421-910b-ca9b49987933">
<img width="1266" alt="image" src="https://github.com/ndhoang123/Udacity-project2-Azure/assets/27766520/44d26687-1904-477c-8bc2-8a190e2b8e0e">

## Enhancements
- Some features that we intend to improve in the upcoming days
    - Improve the UI
    - Add more features that the user want to add from both FE and BE
    - Optimize the model with more pre-trained models
    - Diverse the data input

## Demo 
[Video for guideline the CI/CD running](https://youtu.be/Ih5Y5xAJDnQ)
