import datetime as dt
import os
import random
import smtplib

MY_MAIL = "dekopicha7@gmail.com"
PASSWORD = os.environ.get("GMAIL_PWD")

BIRTHDAYS = {"Meow": {"birthday": "1975-5-2",
                      "email": "any_mail@gmail.com"},
             "Bark": {"birthday": "1942-08-17",
                      "email": "any_mail@gmail.com"},
             "Ata": {"birthday": "2024-04-23",
                      "email": "any_mail@gmail.com"}
            }

LETTERS_PATH = os.environ.get("LETTERS_PATH")
PATTERN = "[NAME]"
DATE_FORMAT = r"%Y-%m-%d"

current_time = dt.datetime.now()

for name in BIRTHDAYS:
    date_of_birth = dt.datetime.strptime(BIRTHDAYS[name]["birthday"], DATE_FORMAT)
    
    if date_of_birth.month == current_time.month and date_of_birth.day == current_time.day:
        with open(f"{LETTERS_PATH}letter_{random.randint(1, 3)}.txt", "r") as f:
            content = f.read()

        letter = content.replace(PATTERN, name)
        receiver_mail = BIRTHDAYS[name]["email"]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_MAIL, PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=receiver_mail, msg=f"Subject: Happy Birthday!\n\n{letter}")
