#naive object -
from datetime import datetime
#print(datetime.now()) # no timezone, = not much use in commercial multiclient systems, current time
#aware object - is an object aware about timezones

from datetime import datetime, timezone, timedelta
#print(datetime.now(timezone.utc)) #2024-05-13 15:44:20.630835+00:00  +00:00 means aware object

#another date time library to take a look at - ARROW
today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1) #adds 1 day

print(today)
print(tomorrow)

print(today.strftime('%m-%d-%Y %H:%M:%S')) #string format time; in printout there's still no timezone, but there is an object

user_date = input('Enter the data in YYYY-mm-dd format: ')
print(type(user_date))
user_date = datetime.strptime(user_date,"%Y-%m-%d") #string parse time, convert user input to datetime onject
print(user_date)
print(type(user_date))


#see https://strftime.org/ for Python strftime cheatsheet
