# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 18:14:14 2023

@author: hp
"""
#locust -f stress_test.py --headless -u 10 -r 10 --run-time 1m --host http://127.0.0.1:5000

from locust import HttpUser, task, between
import json
#locust -f stress_test.py --headless -u 10 -r 10 --run-time 1m --host http://127.0.0.1:5000

class PredictUser(HttpUser):
    wait_time = between(5, 10)

    @task
    def predict(self):
        headers = {'Content-type': 'application/json'}
        data = {
            "Anime_Title": "Attack on Titan",
            "Anime_Genre": ["Action, Drama, Fantasy"],
            "Anime_Description": "The story of Eren Yeager, his friends Mikasa Ackerman and Armin Arlert, ...",
            "Anime_Type": "TV",
            "Anime_Producer": ["Production I.G, Wit Studio"],
            "Anime_Studio": ["Mappa"],
        }
        response = self.client.post('/predict', data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("OK")

