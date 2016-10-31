# coding:utf-8
from datetime import datetime

now = datetime.now()
print(now)

d = datetime(2016,12,9)
print(d)

'''
timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
'''
ts = d.timestamp()
print(datetime.fromtimestamp(ts))   # 本地时间+8
print(datetime.utcfromtimestamp(ts))# UTC时间

#string to time, 转换后的datetime是没有时区信息的
d = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(d)

# datetime to string
print(now.strftime('%Y-%m-%d'))

# datetime加减
from datetime import timedelta
td = timedelta(hours=8)
print(now + td)

'''
本地时间转成UTC时间
1.时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
'''

from datetime import timezone
utcnow = datetime.utcnow().replace(tzinfo=timezone.utc) #1.
print(utcnow)
print(utcnow.astimezone(timezone(timedelta(hours=8))))
