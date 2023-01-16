import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
username = os.environ.get("username")
projectName = os.environ.get("projectName")
sheetName = os.environ.get("sheetName")
sheety_auth = os.environ.get("sheety_auth")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"


gender = os.environ.get("gender")
weight_kg = os.environ.get("weight_kg")
height_cm = os.environ.get("height_cm")
age = os.environ.get("age")

exercise_text = input("Tell me which exercises you did: ")


now = dt.datetime.now().strftime("%Y/%m/%d")
time = dt.datetime.today().strftime("%X")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameter = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age,

}
response = requests.post(exercise_endpoint, parameter, headers=headers)
result = response.json()["exercises"][0]

exercise_name = result["name"].title()
duration_min = result["duration_min"]
nf_calories = result["nf_calories"]
print(exercise_name)
print(duration_min)
print(nf_calories)

headers = {
    "Authorization": sheety_auth
}
parameter = {
    "workout": {
        "date": now,
        "time": time,
        "exercise": exercise_name,
        "duration": duration_min,
        "calories": nf_calories,
    }

}
response = requests.post(sheety_endpoint, json=parameter, headers=headers)
print(response.text)
