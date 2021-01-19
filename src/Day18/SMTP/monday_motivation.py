import datetime as dt
import smtplib
import random

my_email = "your.email@example.com"
password = "password"

with open("quotes.txt") as file:
    quotes = file.readlines()

# If today is Tuesday, then send a mail.
if dt.datetime.now().weekday() == 1:
    with smtplib.SMTP("smtp.example.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        quote = random.choice(quotes)
        message = f"Subject:Monday Motivation\n\n{quote}"

        connection.sendmail(from_addr=my_email,
                            to_addrs="to_email@example.com",
                            msg=message
                            )
