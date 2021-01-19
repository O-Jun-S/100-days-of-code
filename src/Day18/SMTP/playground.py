# import smtplib
#
# my_email = "mail@example.com"
# password = "password"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="mail.to@example.com",
#                         msg="Subject:Hello\n\n"
#                             "This is the body of my email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=2006, month=7, day=18, hour=18)

