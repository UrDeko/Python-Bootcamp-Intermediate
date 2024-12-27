import datetime as dt
import os
import requests
import smtplib

MY_MAIL = os.environ.get("GMAIL")
PASSWORD = os.environ.get("APP_PWD")

LAT = 56.263920
LON = 9.501785

response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data = response.json()
iss_position = iss_data["iss_position"]

if LAT - 5 <= float(iss_position["latitude"]) <= LAT + 5 and \
   LON - 5 <= float(iss_position["longitute"]) <= LON + 5:
    mail_content = f"Subject: ISS Location\n\nCurrent ISS location: {iss_position}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_MAIL, PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=os.environ.get("MAIL"), msg=mail_content)