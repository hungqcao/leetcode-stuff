from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json
import functools

class Solution:
    @functools.lru_cache(None)
    def dfs(self, cur_pos, steps, arrLen):
        if cur_pos == 0 and steps == 0:
            return 1
        if steps == 0: return 0
        res = self.dfs(cur_pos, steps - 1, arrLen)
        if cur_pos > 0:
            res += self.dfs(cur_pos - 1, steps - 1, arrLen)
        if cur_pos < arrLen - 1:
            res += self.dfs(cur_pos + 1, steps - 1, arrLen)
        return res
    def numWays(self, steps: int, arrLen: int) -> int:
        res = self.dfs(0, steps, arrLen)
        return res % (10**9+7)

sol = Solution()
print(sol.numWays(3, 2))