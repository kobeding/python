#!/usr/bin/python3.5

from datetime import datetime,timedelta,timezone
#获取当前datetime：
now = datetime.now()
print('now=',now)
print('type(now)=',type(now))
#用指定日期时间创建datetime
dt = datetime(2008,8,8,8,8,8)
print('dt =',dt)
#把timestamp转换为datetime:
t = now.timestamp()
print('timestamp->datetime:',datetime.fromtimestamp(t))
print('timestamp->datetime as UTC+0:',datetime.utcfromtimestamp(t))
#从str读取datetime：
cday = datetime.strptime('2015-6-1 18:18:18','%Y-%m-%d %H:%M:%S')
print('strptime:',cday)
#把datatime格式化输出：
print('strftime:',cday.strftime('%a, %b %d %H:%M'))
#对日期进行加减：(timedelta类)
print('current datetime =',cday)
print('current + 10 hours =',cday + timedelta(hours=10))
print('current - 1 day =',cday - timedelta(days=1))
print('current + 2.5 day =',cday + timedelta(days=2,hours=12))
#把时间从UTC+0时区转为UTC+8：
#一个datetime有一个时区属性tzinfo,默认None,所以无法区分datetime的时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
#UTC+0:00 now = 2016-04-25 03:48:12.233319+00:00
#UTC+8:00 now = 2016-04-25 11:48:12.233319+08:00
#timezone(timedelta(hours=8))----创建UTC+8 时区
print('UTC+0:00 now =',utc_dt)
print('UTC+8:00 now =',utc8_dt)