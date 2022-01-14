from typing import List
import collections
import math
import functools
import heapq

def areConnected(n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
    uf = dict()
    def find(x):
        uf.setdefault(x, x)
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]
    def union(x, y):
        uf[find(x)] = find(y)
    
    for i in range(threshold + 1, n + 1):
        x = i
        multi = 2
        y = multi * i
        while y <= n:
            union(x, y)
            multi += 1
            y = multi * i
    
    ret = []
    for x, y in queries:
        if x not in uf or y not in uf:
            ret.append(False)
        else:
            ret.append(find(uf[x]) == find(uf[y]))

    #print(uf)
    return ret
    
    
#print(areConnected(6, 2, [[1,4],[2,5],[3,6]]))
print(areConnected(6, 0, [[4,5],[3,4],[3,2],[2,6],[1,3]]))