import requests
from datetime import datetime
import smtplib
import time

my_email = "email@gmail.com"
password = "pw"  # google app pw

MY_LAT = 129.3113596
MY_LONG = 35.5383773
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # catch error

longitude = float(response.json()["iss_position"]["longitude"])
latitude = float(response.json()["iss_position"]["latitude"])
iss_position = (longitude, latitude)
print(iss_position)

del response
parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}
response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour

while True:
    time.sleep(60)
    if sunset <= time_now or sunrise >= time_now:
        if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg="subject:Look Up \n\nThe ISS is above yo in the sky.")
