from typing import List
import collections
import math
import sys
import os
from common import convertToTree
from common import create2DArray, __location__
import heapq
import functools
from common import TreeNode

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indeg = [0]*n
        for u, v in relations: 
            graph[u-1].append(v-1)
            indeg[v-1] += 1
        
        pq = []
        for i, x in enumerate(indeg): 
            if x == 0: heapq.heappush(pq, (time[i], i))
        
        while pq: 
            t, u = heapq.heappop(pq)
            for v in graph[u]: 
                indeg[v] -= 1
                if indeg[v] == 0: 
                    heapq.heappush(pq, (t + time[v], v))
        return t
        
                    
sol = Solution()
#print(sol.minimumTime(3, [[1,3],[2,3]], [3,2,5]))
#print(sol.minimumTime(5,[[1,5],[2,5],[3,5],[3,4],[4,5]],[1,2,3,4,5]))
print(sol.minimumTime(9,[[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]],[9,5,9,5,8,7,7,8,4]))
