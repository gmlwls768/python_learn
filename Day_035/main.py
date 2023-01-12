import requests
half_day = 5
api_key = "enter api key"
parameters = {
    "lon": "129.3113596",
    "lat": "35.5383773",
    "cnt": "",
    "appid": api_key,

}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
read = response.json()["list"]
count = 0
weather_slice = read[:5]
for data in weather_slice:
    print(data["weather"][0]["id"])
if count >= 1:
    print("bring")
