import requests
from datetime import datetime
import smtplib

# Your latitude
MY_LAT = 0

# Your longitude
MY_LONG = 100

EMAIL = "your.email@example.com"
PASSWORD = "password"

TIME_DIFFERENCE = 14

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - TIME_DIFFERENCE
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - TIME_DIFFERENCE

time_now = datetime.now()

# If the ISS is close to my current position
if iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5:
        # and it is currently dark
        if time_now.hour <= sunrise or sunset <= time_now.hour:
            # Then send me an email to tell me to look up.
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=EMAIL,
                                 password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="to_addr@example.com",
                    msg="Subject:ISS is close to you!\n\n"
                        "Look up! ISS is close to you!"
                )

# BONUS: run the code every 60 seconds.
