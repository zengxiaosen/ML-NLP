from datetime import datetime
from datetime import timedelta
import time
now = datetime.now()
aDay = timedelta(days=1)
now = now + aDay
print now.strftime('%Y-%m-%d')

aDay = timedelta(days=-1)
now = now + aDay
print now.strftime('%Y-%m-%d')
last_month = time.localtime()[1]-1 or 12
print last_month

d1 = datetime.now()
time.sleep(10)
eclipseTimes = datetime.now() - d1
print eclipseTimes.total_seconds()