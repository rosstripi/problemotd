"""
description: program to find the angle between hands on a 24-hour clock
author: rossbot
"""

def find_angle(time="0:00"):
    hour = (float(time[:time.index(":")])) % 12
    minute = float(time[time.index(":")+1:])

    hour_angle = (hour/12.0 * 360.0) + ((1.0/12.0 * 360.0) * minute/60.0)
    minute_angle = minute/60.0 * 360.0

    angle = abs(minute_angle - hour_angle)
    return angle
