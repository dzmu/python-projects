# Author Tanner Mesaric
from datetime import date, time, datetime
import datetime

events = {
    "Classes Begin":date(2021,8,19), 
    "Add/Drop":date(2021, 8,25), 
    "Labor Day Holiday":date(2021, 9, 6),
    "Fall Break Day":date(2021,10,7), 
    "Last Day to Drop":date(2021,11,3), 
    "Thanksgiving":date(2021,11,25),
    "Last Day of Class":date(2021,12,3),
    "Reading Day":date(2021,12,4),
    "Commencement":date(2021,12,13)
    }

today = date.today()
thirtyDays = today + datetime.timedelta(days=30)



for key in events:
    if events[key] == date.today():
        print(f"- {key} - {events[key].strftime('%b %d, %A')} TODAY!")
    elif (events[key] - date.today()).days <=30 and (events[key] - date.today()).days >= 0:
        numDaysaway = (events[key] - date.today()).days
        print(f"- {key} - {events[key].strftime('%b %d, %A')} - in {numDaysaway} days")
    else:
        print(f"- {key} - {events[key].strftime('%b %d, %A')}")