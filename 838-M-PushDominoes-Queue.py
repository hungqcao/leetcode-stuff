from typing import List
import collections
import math

def pushDominoes(dominoes: str) -> str:
    d = 'L' + dominoes + 'R'
    res = ''
    i = 0
    for j in range(1, len(d)):
        if d[j] == '.':
            continue
        mid = j - i - 1
        if i:
            res += d[i]
        if d[i] == d[j]:
            res += d[i] * mid
        elif d[i] == 'L' and d[j] == 'R':
            res += '.' * mid
        else:
            res += (mid // 2) * 'R' + (mid%2)*'.' + (mid // 2)*'L'
        i = j
        
    return res

#print(pushDominoes("RR.L"))
print(pushDominoes(".L.R...LR..L.."))