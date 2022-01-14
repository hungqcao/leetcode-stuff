from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for i in range(n)] for j in range(m + 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


sol = Solution()
print(sol.uniquePaths(3, 7))
print(sol.uniquePaths(3, 2))
print(sol.uniquePaths(7, 3))
print(sol.uniquePaths(3, 3))