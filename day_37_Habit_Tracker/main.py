import requests
from datetime import datetime

USERNAME = 'bhargav98'
TOKEN = 'u6879702137yioqwe1'
GRAPH_ID = 'xtrack1'
pixela_endpoint = 'https://pixe.la/v1/users'
user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

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

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
date = datetime.now()

pixel_parameters = {
    'date': date.strftime('%Y%m%d'),
    'quantity': input("How many pages have I read today?: "),

}

response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)
#
# pixel_update = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240508'
#
# update_parameters = {
#     'quantity': '5',
# }

# update = requests.put(url=pixel_update, json=update_parameters, headers=headers)
# print(update.text)

# pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
#
# delete = requests.delete(url=pixel_delete,headers=headers)
#
# print(delete.text)
