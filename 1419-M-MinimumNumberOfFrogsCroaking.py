from typing import List
import collections
import math
import itertools

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    ans, singing = 0, 0
    d = {}
    for c in "croak":
        d.setdefault(c, 0)
    for c in croakOfFrogs:
        if d['c'] == 0 and (d['r'] > 0 or d['o'] > 0 or d['a'] > 0 or d['k'] > 0):
            return -1
        if c == 'c':
            singing += 1
            ans = max(singing, ans)
        elif c == 'k':
            if d['c'] > 0 and d['r'] > 0 and d['o'] > 0 and d['a'] > 0:
                singing -= 1
                d['c'] -= 1
                d['r'] -= 1
                d['o'] -= 1
                d['a'] -= 1
                d['k'] -= 1
        d[c] += 1
    return ans if all([v == 0 for v in d.values()]) else -1
    
print(minNumberOfFrogs('croakcroak'))
print(minNumberOfFrogs('crcoakroak'))
print(minNumberOfFrogs('croakcrook'))
print(minNumberOfFrogs('croakcroa'))
print(minNumberOfFrogs("aoocrrackk"))
