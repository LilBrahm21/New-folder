# brahm brar, how to get the time of day python
import time

#first instance of the time in program
first_time = time.gmtime()
#print(first_time)

#current time in seconds
current = time.time()
print(current) #seconds since Jan 1 1970

#current date and time like we see it notmally
now = time.ctime(current)
#print(now)

#get just a part of the time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour #military time (0-23)
print(hour)