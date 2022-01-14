from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

def angleClock(hour: int, minutes: int) -> float:
    if hour == 12:
        hour = 0
    hour_angle = hour * 30 + (minutes/60) * 30
    minutes_angle = (minutes / 60) * 360
    res = abs(hour_angle - minutes_angle)
    return res if res <= 180 else 360 - res

print(angleClock(12, 30))
print(angleClock(3, 30))
print(angleClock(3, 15))
print(angleClock(4, 50))
print(angleClock(12, 0))