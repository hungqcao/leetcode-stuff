from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        visited = [0 for _ in range(n)]
        ans = 0
        count = 0
        heap = [(0, 0)]
        while heap:
            dist, curP = heapq.heappop(heap)
            if visited[curP] == 0:
                visited[curP] = 1
                ans += dist
                count += 1
                for neiD, nei in c[curP]:
                    if visited[nei] == 0:
                        heapq.heappush(heap, (neiD, nei))
                if count >= n: break


        return ans

        
        

sol = Solution()
print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
print(sol.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))
print(sol.minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]]))
print(sol.minCostConnectPoints([[0,0]]))