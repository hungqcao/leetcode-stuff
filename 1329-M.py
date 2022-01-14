from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import heapq

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        R, C = len(mat), len(mat[0])
        for i in range(R):
            for j in range(C):
                #if abs(i-j) not in d:
                #    d[abs(i-j)] = []
                heapq.heappush(d[i - j], mat[i][j])
        
        for i in range(R):
            for j in range(C):
                val = heapq.heappop(d[i-j])
                mat[i][j] = val
        
        return mat

sol = Solution()
print(sol.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))