#! /usr/bin/env python
# -*- coding:utf-8 -*-
import time
import datetime

# str 转datetime
str = '2012-11-19'
date_time = datetime.datetime.strptime(str, '%Y-%m-%d')
print(date_time)

# 获取当前时间
t_date = datetime.date.today()
print('------------------------')
print(datetime.date.ctime(t_date))
print(t_date)
# 获取第几周
week = t_date.strftime("%W")
print(week)
print(type(week))
ds = '单' if int(week) % 2 == 1 else '双'
print(ds)
# 获取星期几
week_day = t_date.strftime("%w")
print(week_day)
