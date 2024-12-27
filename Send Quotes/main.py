import datetime as dt
import os
import random
import smtplib

MY_MAIL = os.environ.get("GMAIL")
PASSWORD = os.environ.get("APP_PWD")
QUOTES_FILE = "Python Bootcamp/Intermediate/Send Quotes/quotes.txt"

if dt.datetime.now().weekday() == 0:
    with open(QUOTES_FILE, "r") as f:
        quotes = f.readlines()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=os.environ.get("MAIL"), msg=f"Subject: Quote\n\n {random.choice(quotes)}")
