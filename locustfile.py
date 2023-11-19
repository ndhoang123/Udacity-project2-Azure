import time
from locust import HttpUser, between, task

class PredictTestUser(HttpUser):
    host = "https://flask-app-predict-1119.azurewebsites.net:443"
    wait_time = between(0.5, 2)

    @task
    def index(self):
        self.client.get("/")

    @task
    def predict(self):
        self.client.post("/predict", json={
            "CHAS":{
                "0":0
                },
            "RM":{
                "0":6.575
                },
            "TAX":{
                "0":296.0
                },
            "PTRATIO":{
                "0":15.3
                },
            "B":{
                "0":396.9
                },
            "LSTAT":{
                "0":4.98
                }
        })