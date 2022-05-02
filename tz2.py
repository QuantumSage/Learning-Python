# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:53:26 2022

@author: Quantum Sage
"""

import calendar
import pytz
from datetime import datetime as dt

"""
calendar.weekday? returns the usage of the function
signature: calendar.weekday(year,month,day)
Returns from 0-6~Mon-Sun
"""
print(calendar.weekday(2022,7,6))

#leapyear criteria: divisible by 4 and incase its a century year (100,400) it has to be divisible by 400

"""
From Jan-Jul: Odd:31 days Even:30 days
From Aug-Dec: Odd:30 days Even:31 days
"""
timezones=pytz.all_timezones

for i in range(len(timezones)):
    zones=timezones[i]
    tz=pytz.timezone(zones)
    print("Current time at timezone",zones," is:",dt.now(tz))
print(calendar.isleap(1982)) #checks if leap year
