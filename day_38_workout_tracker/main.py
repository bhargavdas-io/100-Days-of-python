import requests
import os
from datetime import datetime

APP_ID = os.environ.get("NLP_APP_ID")
API_KEY = os.environ.get("NLP_API_KEY")
NLP_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETLY_ENDPOINT = 'https://api.sheety.co/03e2cfdf998037f5e602b6006eadb329/workoutTracking/workouts'
GENDER = 'Male'
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 25


header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

api_params = {
    'query': input("What exercises have you done today?: "),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

request = requests.post(url=NLP_ENDPOINT, json=api_params, headers=header)

data = request.json()

exercise = data['exercises'][0]['name']
duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']


today_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

sheet_header = {
    "Authorization": os.environ.get('SHEETLY_AUTHORIZATION')
}
sheet_inputs = {
    "workout": {
        "date": today_date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories

    }

}
sheet_data = requests.post(url=SHEETLY_ENDPOINT, json=sheet_inputs, headers=sheet_header)
print(sheet_data.text)
