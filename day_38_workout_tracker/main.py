import requests
from datetime import datetime

APP_ID = '1ac38c53'
API_KEY = '4f813a37ab062145fff800691e8b00b9'
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

# print(exercise)
# print(duration)
# print(calories)

today_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

sheet_header = {
    "Authorization": 'Basic Ymhhcmdhdl9kYXM5ODpiblZzYkRwdWRXeHM='
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
