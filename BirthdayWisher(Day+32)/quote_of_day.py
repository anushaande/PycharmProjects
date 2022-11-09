import smtplib
import datetime as dt
import random


today = dt.datetime.now()
day = today.weekday()

with open("quotes.txt") as file:
    quotes_list = file.readlines()
print(quotes_list)

if day == 1:
    username = "anusha.qa.work@gmail.com"
    password = "welcome123()"
    message = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username,
                            to_addrs="anushaande@yahoo.com",
                            msg=f"Subject:Quote Of The Day\n\n{message}")