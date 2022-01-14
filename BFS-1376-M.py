from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json
import functools
import heapq

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        graph = collections.defaultdict(list)
        for i in range(n):
            if i != -1:
                graph[manager[i]].append(i)
        queue = []
        queue.append((headID, 0))
        while queue:
            e, time = queue.pop(0)
            for nei in graph[e]:                
                queue.append((nei, time + informTime[e]))
            res = max(res, time)
            
        print(res)
        return res




        

sol = Solution()
sol.numOfMinutes(1,0,[-1],[0])
sol.numOfMinutes(6,2,[2,2,-1,2,2,2],[0,0,1,0,0,0])
sol.numOfMinutes(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
sol.numOfMinutes(11,4,[5,9,6,10,-1,8,9,1,9,3,4],[0,213,0,253,686,170,975,0,261,309,337])