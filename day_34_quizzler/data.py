import requests
URL = 'https://opentdb.com/api.php'
parameters = {
    "amount": 10,
    "type": "boolean"
}
connection = requests.get(url=URL, params=parameters)
connection.raise_for_status()
data = connection.json()
question_data = data["results"]



