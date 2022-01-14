from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0 for i in range(n)] for i in range(n)]
        rowStart = 0
        rowEnd = n - 1
        colStart = 0
        colEnd = n - 1
        num = 1
        while num <= n*n:
            #go right row:0 col 0>n-1  
            for i in range(colStart, colEnd + 1):
                ret[rowStart][i] = num
                num += 1
                
            rowStart += 1
            # go down
            for i in range(rowStart, rowEnd + 1):
                ret[i][colEnd] = num
                num += 1
                
            colEnd -= 1
            # go left
            for i in range(colEnd, colStart - 1, -1):
                ret[rowEnd][i] = num
                num += 1
            
            rowEnd -= 1
            # go up
            for i in range(rowEnd, rowStart - 1, -1):
                ret[i][colStart] = num
                num += 1
            
            colStart += 1
        
        return ret
    
    def test(self, arr):
        #arr = list(reversed(arr))
        for r in range(len(arr)):
            arr[r] = list(reversed(arr[r]))
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                print(f"{arr[i][j]} {arr[j][i]}")
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        #print(list(reversed(arr)))
        print(arr)
sol = Solution()
#print(sol.generateMatrix(3))
#print(sol.generateMatrix(4))
sol.test([
    [1, 2,  3,  4],
    [6, 7,  8,  9],
    [11,12, 13, 14],
    [15,16, 17, 18]
])
"""
[[4, 9, 14, 18], 
[3, 8, 13, 17], 
[2, 7, 12, 16], 
[1, 6, 11, 15]]

[[15, 11, 6, 1], 
[16, 12, 7, 2], 
[17, 13, 8, 3], 
[18, 14, 9, 4]]
"""