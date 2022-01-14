from typing import List
import collections
import math

def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
    queue = [(sx, sy)]
    seen = set([(sx, sy)])
    while queue:
        size = len(queue)
        for i in range(size):
            tmp_x, tmp_y = queue.pop(0)
            if tmp_x == tx and tmp_y == ty: return True
            if tmp_x*tmp_y >= tx*ty: continue
            if (tmp_x, tmp_x + tmp_y) not in seen:
                queue.append((tmp_x, tmp_x+tmp_y))
                seen.add((tmp_x, tmp_x + tmp_y))
            if (tmp_x+tmp_y, tmp_y) not in seen:
                queue.append((tmp_x+tmp_y, tmp_y))
                seen.add((tmp_x+tmp_y, tmp_y))
    return False
            
#print(reachingPoints(1,1,3,5))
#print(reachingPoints(1,1,2,2))
#print(reachingPoints(1,1,1,1))
n = 2
n %= 1
print(n)