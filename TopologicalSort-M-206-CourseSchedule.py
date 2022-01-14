from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]]+=1
        queue = list(filter(lambda x:indegree[x] == 0, indegree))
        count = 0
        while len(queue) > 0:
            pop = queue.pop()
            count += 1
            for nei in graph[pop]:
                if indegree[nei] > 0:
                    indegree[nei]-=1
                    if indegree[nei] == 0:
                        queue.append(nei)

        return count == numCourses 



sol = Solution()
print(sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
print(sol.canFinish(2, [[1,0]]))
print(sol.canFinish(3,[[1,0],[1,2],[0,1]]))