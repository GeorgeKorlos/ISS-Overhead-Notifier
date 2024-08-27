import requests 
from datetime import datetime   
import time
import smtplib
import os

MAIL = os.getenv('EMAIL')
PASS = os.getenv('PASSWORD')
LAT = os.getenv('LATITUDE')
LNG = os.getenv('LONGITUDE')

def is_iss_overhead(LAT, LNG):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    parameters = {
        'lat': LAT,
        'lng': LNG,
        'formatted': 0
    }

    if LAT - 5 <= iss_latitude <= LAT + 5 and LNG - 5 <= iss_longitude <= LNG + 5:
        response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
        sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

        time_now = datetime.now().hour

        if time_now < sunrise or time_now > sunset:
            return True

while True:
    time.sleep(60)
    if is_iss_overhead(LAT=LAT, LNG=LNG):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MAIL,PASS)
        connection.sendmail(
            from_addr=MAIL,
            to_addrs=MAIL,
            msg='Subject: Look up. ISS overhead.'
        )
    