'''
Created on 2016. 9. 24.

@author: Administrator
'''

import datetime

# 책 p326

# date 설정
dt = datetime.date(1999,11,6)
print(dt, type(dt))
print(dt.year, dt.month, dt.day)

# time 설정
tm = datetime.time(11,10,6)
print(tm, type(tm))
print(tm.hour, tm.minute, tm.second)

# 시스템 날짜
dt = datetime.date.today()
print(dt, type(dt))
print(dt.year, dt.month, dt.day)

dttm = datetime.datetime(1980,1,20,9,10,13)
print(dttm, type(dttm))

dttm = datetime.datetime.today()
print(dttm, type(dttm))
