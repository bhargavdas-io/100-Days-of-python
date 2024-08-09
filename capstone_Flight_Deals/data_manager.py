import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


load_dotenv()
sheet_url = 'https://api.sheety.co/03e2cfdf998037f5e602b6006eadb329/flightDeals/prices'
header = {
            "Authorization": os.environ["SHEET_AUTH"]
        }

class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETLY_USERNAME"]
        self._password = os.environ["SHEETLY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_url, headers=header)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_iata(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheet_url}/{city['id']}",
                json=new_data, headers=header
            )
            print(response.text)
