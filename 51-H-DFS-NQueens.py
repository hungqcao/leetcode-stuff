from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    def dfs(self, queens, sum, minus, n):
        row = len(queens)
        if row == n:
            self.ret.append(queens)
            return

        for col in range(n):
            if col not in queens and row - col not in minus and row + col not in sum:
                self.dfs(queens + [col], sum + [row+col], minus + [row-col], n)
                


    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ret = []
        self.dfs([],[], [], n)
        return self.ret
        
        




sol = Solution()
print(sol.solveNQueens(4))