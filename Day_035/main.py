import os
import requests
from twilio.rest import Client
half_day = 5

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
weather_api_key = os.environ.get("weather_api_key")
my_number = os.environ.get("my_number")
twilio_number = os.environ.get("twilio_number")
parameters = {
    "lon": "129.3113596",
    "lat": "35.5383773",
    "cnt": "",
    "appid": weather_api_key,

}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
read = response.json()["list"]
count = 0
weather_slice = read[:half_day]
for data in weather_slice:
    if data["weather"][0]["id"] >= 500:
        count += 1
if count >= 1:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_=twilio_number,
            to=my_number
        )
    print(message.status)
