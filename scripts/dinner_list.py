import datetime
import time
from dateutil.rrule import DAILY, rrule,  MO, TU, WE, TH, SU
import calendar
import re

#Read the list of dinners
dinners = []
with open('../middager.md','r') as fp:
    for line in fp:    
        if '##' in line:
            #Extract only the dinner names
            m =  re.search(':(.+)\.',line)
            if m:                
                dinners.append(m.group(1).strip())            
dinners = dinners*54


#Make a list of dates, dinners and day of week
first_dinner_day = datetime.datetime(2018,12,30)
last_dinner_day = first_dinner_day+datetime.timedelta(365-2)
daynames = calendar.day_name
dates_with_dinners = rrule(DAILY,dtstart = first_dinner_day,
                           until=last_dinner_day,byweekday= (MO,TU,WE,TH,SU))
dinner_dates = []
for i,date in enumerate(dates_with_dinners):
    dinner_dates.append([date,calendar.day_name[date.weekday()],dinners[i]])
    
#Connect to google calendar API and fill in dinner for each day






