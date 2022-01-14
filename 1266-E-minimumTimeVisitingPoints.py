from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Solution:
    def calTime(self, x1, y1, x2, y2):
        distance = max(abs(x2-x1), (abs(y2-y1)))
        return distance
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for p in range(1, len(points)):
            res += self.calTime(points[p][0], points[p][1], points[p-1][0], points[p-1][1])
        return res
        
sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(sol.minTimeToVisitAllPoints([[3,2],[-2,2]]))
print(sol.minTimeToVisitAllPoints([[3,2],[2,-2]]))
print(sol.minTimeToVisitAllPoints([[3,2],[-2,1]]))
print(sol.minTimeToVisitAllPoints([[3,2],[-2,-2]]))