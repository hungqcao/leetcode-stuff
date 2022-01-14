from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        col0 = False
        for i in range(R):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(R)[::-1]:
            for j in range(1, C)[::-1]:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0:
                matrix[i][0] = 0
        print(matrix)
sol = Solution()
#sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
#sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
sol.setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])