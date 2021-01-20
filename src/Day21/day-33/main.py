import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

MY_LAT = 0
MY_LNG = 100

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(" https://api.sunrise-sunset.org/json",
                        params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()

# remove time difference
sunrise_hour = int(sunrise.split("T")[1].split(":")[0]) - 14
print(sunrise_hour)
print(time_now.hour)
