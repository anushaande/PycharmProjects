from datetime import datetime as dt
import pandas
import random
import smtplib

today = dt.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
EMAIL = "anusha.qa.work@gmail.com"
PWD = "welcome123()"

birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open(f"/letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:HAPPY BIRTHDAY!\n\n{contents}")
