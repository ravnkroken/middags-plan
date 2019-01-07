import datetime
import time
from dateutil.rrule import DAILY, rrule,  MO, TU, WE, TH, SU
import calendar

#Read the list of dinners
dinners = ['Fisk','Kjøtt','Speilegg','Pasta','Egg']
dinners = dinners*54


#Make a list of dates, dayofweek and dinner for that day
first_dinner_day = datetime.datetime(2018,12,30)
last_dinner_day = first_dinner_day+datetime.timedelta(365-2)
daynames = calendar.day_name
dates_with_dinners = rrule(DAILY,dtstart = first_dinner_day,
                           until=last_dinner_day,byweekday= (MO,TU,WE,TH,SU))
dinner_dates = []
for i,date in enumerate(dates_with_dinners):
    dinner_dates.append([date,calendar.day_name[date.weekday()],dinners[i]])






