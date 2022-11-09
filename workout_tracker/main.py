    import requests
import datetime as dt
import os

## ALl the authentication keys required
APP_ID = os.environ.get("app_id")
APP_KEY = os.environ.get("app_key")
USER = os.environ.get("user")
SHEETY_AUTH = os.environ.get("sheety_auth")
SHEETY_END_POINT = os.environ.get("sheety_end_point")


# Accessing nutritionix endpoint and getting the workout information
header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

exer_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
parameters = {"query": input("Workout for today is ?"),
              "gender": "female",
              "weight_kg": 72.5,
              "height_cm": 167.64,
              "age": 30}

response = requests.post(url=exer_end_point, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
result_list = result['exercises']

# Accessing sheety endpoint and posting the workout for the day.
sheety_end_point = SHEETY_END_POINT
today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%H:%M:%S")
for workout in result['exercises']:
    parameters = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": workout['user_input'],
            "duration": workout['duration_min'],
            "calories": workout['nf_calories']
        }
    }
    header = {"Authorization": SHEETY_AUTH}
    sheety_response = requests.post(url=sheety_end_point, json=parameters, headers=header)
    print(sheety_response.text)



