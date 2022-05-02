# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:43:15 2022

@author: Quantum Sage
"""

from datetime import datetime as dt
import datetime
import pytz
import time
print(dt.now()) #prints present time in the format yyyy/mm/dd hh:mm:s.ms
tz=pytz.timezone("Singapore") #object created for the timezone Singapore
print(dt.now(tz)) #prints the time along with the variance of time "time+8:00" for Singapore
print(pytz.all_timezones) #prints all available timezones
print(len(pytz.all_timezones)) #prints the number of available timezones
print(time.time()) #prints the time in seconds since epoch i.e January 1, 1970, 00:00:00 (UTC)