import pandas
import datetime as dt
import random
import smtplib

# Extra hard starting project
data = pandas.read_csv("birthdays.csv")

my_email = "your.email@example.com"
password = "password"


def birthday_person():
    birthday_people = []
    now = dt.datetime.now()
    for (index, row) in data.iterrows():
        person_data = row
        year = person_data["year"]
        month = person_data["month"]
        day = person_data["day"]

        if now.year == year and now.month == month and now.day == day:
            birthday_people.append(person_data)
    return birthday_people


bir_people = birthday_person()
for person in bir_people:
    # generate random integer from 1 to 3.
    letter_index = random.randint(1, 4)
    temp_file_name = f"letter_templates/letter_{letter_index}.txt"
    with open(temp_file_name) as temp:
        letter_temp = temp.read()

    person_email = person["email"]
    person_name = person["name"]

    letter = letter_temp.replace("[NAME]", person_name)

    with smtplib.SMTP("smtp.example.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person_email,
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )

