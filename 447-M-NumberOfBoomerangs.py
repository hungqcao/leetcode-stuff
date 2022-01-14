from typing import List
import collections
import math

def numberOfBoomerangs(points: List[List[int]]) -> int:
    n = len(points)
    res = 0
    for i in range(n):
        dist = dict()
        for j in range(n):
            if i == j:
                continue
            
            distance = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1]-points[j][1])**2)
            key = distance
            if key in dist:
                res += dist[key]
            dist[key] = dist.get(key, 0) + 1
    return res*2


print(numberOfBoomerangs([[0,0],[1,0],[2,0]]))
print(numberOfBoomerangs([[1,1],[2,2],[3,3]]))
print(numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))