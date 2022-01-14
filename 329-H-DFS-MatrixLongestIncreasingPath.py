from typing import List
import collections
import math
import functools
class Solution:
    @functools.lru_cache(None)
    def dfs(self, row, col):
        ans = 1    
        for r,c in self.dirs:
            newR = row + r
            newC = col + c
            if 0 <= newR < self.M and 0<=newC<self.N and self.matrix[newR][newC] >self.matrix[row][col]:
                tmp = 1 + self.dfs(newR, newC)
                ans = max(tmp, ans)
        return ans
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.M, self.N = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        ret = 0
        for i in range(self.M):
            for j in range(self.N):
                ret = max(ret, self.dfs(i, j))
        return ret

sol = Solution()

print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
sol = Solution()
print(sol.longestIncreasingPath([[9,11,4],[6,10,8],[2,1,1]]))