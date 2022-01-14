from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        self.edgesMap = collections.defaultdict(list)
        self.succProbMap = collections.defaultdict(float)
        res = 0

        priQueue = [(-1, start)]
        _ = 0
        for f,t in edges:
            self.edgesMap[f].append(t)
            self.edgesMap[t].append(f)
            self.succProbMap[(f, t)] = self.succProbMap[(t, f)] = succProb[_]
            _+=1
        visited = set()
        while priQueue:
            prob, node = heapq.heappop(priQueue)
            visited.add(node)
            if node == end: res = max(res, -prob)
            else:
                for nei in self.edgesMap[node]:
                    if nei not in visited:
                        heapq.heappush(priQueue, (-(-prob * self.succProbMap[(node, nei)]), nei))
        return res

        
sol = Solution()
print(sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print(sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
print(sol.maxProbability(3, [[0,1]], [0.5], 0, 2))