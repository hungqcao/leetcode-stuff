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
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        queue = []
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        heapq.heappush(queue, (0, 1))
        visited = collections.defaultdict(list)
        res = float('inf')
        k = 0
        visited[1] = [0]
        while queue:
            cur_time, vertex = heapq.heappop(queue)
            if vertex == n and len(visited[n]) == 2:
                return max(visited[n])
            if (cur_time // change) % 2 == 1:
                cur_time = change * ((cur_time // change)+1)
            for nei in graph[vertex]:
                if not visited[nei] or (len(visited[nei]) == 1 and visited[nei][0] != (cur_time + time)):
                    #print(f'time: {cur_time + time}')
                    visited[nei] += [cur_time + time]
                    heapq.heappush(queue, (cur_time + time, nei))


        

sol = Solution()
print(sol.secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))
print(sol.secondMinimum(2, [[1,2]], 3, 2))