from typing import List
import collections
import math

def isTransformable(s: str, t: str) -> bool:    
    idx = [collections.deque() for _ in range(10)]
    
    for i, c in enumerate(s):
        idx[int(c)].append(i)
    
    for c in t:
        d = int(c)
        if not idx[d]:
            return False
        
        for i in range(d):
            if idx[i] and idx[i][0] < idx[d][0]:
                return False
        idx[d].popleft()

    return True

print(isTransformable('84532', '34852'))
print(isTransformable('34521', '23415'))
print(isTransformable('12345', '12345'))
print(isTransformable('1', '2'))