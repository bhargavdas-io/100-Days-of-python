import requests
import os
from datetime import datetime

USERNAME = 'bhargav98'
TOKEN = os.environ.get('TOKEN')
GRAPH_ID = os.environ.get('ID')
pixela_endpoint = 'https://pixe.la/v1/users'
user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_parameters = {
    "id": 'xtrack1',
    "name": 'Reading Graph',
    "unit": 'pages',
    "type": 'int',
    "color": 'ajisai',

}

headers = {
    "X-USER-TOKEN": TOKEN  #header
}

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
date = datetime.now()

pixel_parameters = {
    'date': date.strftime('%Y%m%d'),
    'quantity': input("How many pages have I read today?: "),

}

response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)
