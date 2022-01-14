from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    @functools.lru_cache(None)
    def dfs(self, remainingTasks, remainingTime):
        if remainingTasks == self.endState:
            return 1
        
        res = self.N
        for idx, task in enumerate(self.tasks):
            mask = (1 << idx)
            if remainingTasks & mask == 0:
                remaining = remainingTasks | mask
                if task > remainingTime:
                    res = min(res, self.dfs(remaining, self.sessionTime - task) + 1)
                else:
                    res = min(res, self.dfs(remaining, remainingTime - task))
        return res
        
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        self.sessionTime = sessionTime
        self.N = len(tasks)
        self.tasks = tasks
        self.endState = int("1"*self.N, 2)
        return self.dfs(0, self.sessionTime)
        
        

sol = Solution()
print(sol.minSessions([1,2,3], 3))
print(sol.minSessions([3,1,3,1,1], 8))
#print(sol.minSessions([1,2,3,4,5], 15))
#print(sol.minSessions([3,2,2,5], 6))