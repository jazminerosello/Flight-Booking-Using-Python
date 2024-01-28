from datetime import date
from datetime import time
from datetime import datetime


hour = str(input("Hour: "))
minute = str(input("Minute: "))
am_pm = str(input("AM/PM: ")).upper()
time_of_arrival = hour + ":" + minute + am_pm

#arrive_time = time.strptime(time_of_arrival, '%I:%M %p')

time = datetime.strftime(time_of_arrival, '%I:%M%p').time()

print(time)
#print(arrive_time)


