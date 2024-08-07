import requests
import os
from twilio.rest import Client
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
API_KEY = os.environ.get("WEATHER_API")
URL = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'lat': 26.140289,
    'lon': 91.791862,
    'appid': API_KEY,
    'units': 'metric',
    'cnt': 4,

}

connection = requests.get(url=URL, params=parameters)
connection.raise_for_status()
data = connection.json()
weather_id = data['list'][0]['weather'][0]['id']
will_rain = False
for hour_data in data['list']:
    condition_code = int(hour_data['weather'][0]["id"])
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:[TWILIO_NUMBER]',
        body='আজি বৰষুণ দিবলৈ গৈ আছে। ছাতিটো ল’বলৈ নাপাহৰিব। ☂️',
        to='whatsapp:[YOUR_REG_NUMBER]'
    )
    print(message.status)



