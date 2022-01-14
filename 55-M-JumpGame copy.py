from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Solution:
    def dfs(self, arr, idx, target):
        if 0 > idx or idx >= len(arr) or arr[idx] == -1: return False
        if arr[idx] == 0: return True
        val = arr[idx]
        arr[idx] = -1
        for step in [idx + val, idx - val]:
            if self.dfs(arr, step, target):
                return True
        arr[idx] = val
        return False
    def canReach(self, arr: List[int], start: int) -> bool:
        
        return self.dfs(arr, start, 0)


sol = Solution()
print(sol.canReach([4,2,3,0,3,1,2], 5))
print(sol.canReach([4,2,3,0,3,1,2], 0))
print(sol.canReach([3,0,2,1,2], 2))