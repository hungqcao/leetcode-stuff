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
    def dfs(self, l, s):
        n = len(s)
        if n == l: return 1
        if s[l] == '0': return 0
        res = self.dfs(l + 1, s)
        if l < n - 1 and ((int(s[l + 1]) <= 6 and int(s[l]) == 2) or (int(s[l]) == 1)):
            res += self.dfs(l + 2, s)
        return res

    def numDecodings(self, s: str) -> int:
        return self.dfs(0, s)


sol = Solution()
#print(sol.numDecodings("12"))
#print(sol.numDecodings("26"))
#print(sol.numDecodings("0"))
#print(sol.numDecodings("06"))
#print(sol.numDecodings("1101"))
#print(sol.numDecodings("226"))
print(sol.numDecodings("10"))