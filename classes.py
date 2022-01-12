#author Tanner Mesaric
from datetime import date, time, datetime
import datetime
monwed = {
    "ACCT 222 Section 2":time(9,40,00),
    "Phil 213 Section 2":time(12,00,00),
    "ITEC 242 Section 3":time(17,00,00)
}

tuesthurs = {
    "CSCE 204 Section 1":time(11,40,00),
    "ITEC 245 Section 2":time(13,15,00)
}

today = date.today()
if date.today().weekday() == 0 or date.today().weekday() == 2:
    print("Today's Schedule")
    for key in monwed:
        print(f"{key} - {monwed[key].strftime('%I:%M %p')}")
elif date.today().weekday() == 1 or date.today().weekday() == 3:
    print("Today's Schedule")
    for key in tuesthurs:
        print(f"{key} - {tuesthurs[key].strftime('%I:%M %p')}")
else:
    print("You have no classes today.")
