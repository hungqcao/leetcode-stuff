from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json
import functools

class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        pool = set()
        while i**2 <= n:
            pool.add(i**2)
            i += 1
        
        queue = collections.deque()
        queue.append(n)
        level = 0
        while queue:
            level += 1
            for i in range(len(queue)):
                need = queue.popleft()
                for n in pool:
                    if need == n:
                        return level
                    elif need > n:
                        queue.append(need - n)
        return 0

            


sol = Solution()
print(sol.numSquares(12))
print(sol.numSquares(13))