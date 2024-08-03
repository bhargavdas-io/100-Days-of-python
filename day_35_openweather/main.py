import requests
from twilio.rest import Client
account_sid = 'ACf2a37bc0095ff197a682326fae06b1205'
auth_token = '06bb7ef639e58fdf096ec3dab72be8535'
API_KEY = 'e93697bbbdb2e1e6c9336fb7f76faaf26'
URL = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'lat': 26.140289,
    'lon': 91.791862,
    'appid': 'e93697bbbdb2e1e6c9336fb7f76faaf26',
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
        from_='whatsapp:+[twilio number]',
        body='আজি বৰষুণ দিবলৈ গৈ আছে। ছাতিটো ল’বলৈ নাপাহৰিব। ☂️',
        to='whatsapp:+[registered_number]'
    )
    print(message.status)



