from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

def clumsy(n: int) -> int:
    cur, res = n, None
    while n > 0:
        tmp = n
        for op in ['*','/']:
            if n > 1:
                if op == '*':
                    tmp = tmp * (n-1)
                    n -=1
                elif op == '/' and n > 1:
                    tmp = tmp // (n-1)
                    n -=1
        #print(tmp)
        if not res:
            res = tmp
        else:
            res -= tmp
        if n > 0:
            res += (n-1)
            n-=1
        n-=1
    return res
            

print(clumsy(4))
print(clumsy(5))
print(clumsy(10))