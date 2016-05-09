#-*- coding:UTF-8 -*-
__author__ = 'maomao'
import time,random
import commands

def getTimeInt():
    """返回时间戳"""
    return str(time.time())


def Dimestamp_datetime(value):
    """时间戳转换时间"""
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

def Datetime_timestamp(dt):
     """时间转换时间戳"""
     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
     s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
     return int(s)

def RANDOM_STR(lenx=18):
    """随机生成一组字符串"""
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    randomx = random.Random()
    for i in range(lenx):
        str += chars[randomx.randint(0, length)]
    return str