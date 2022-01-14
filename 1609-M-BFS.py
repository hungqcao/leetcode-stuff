from typing import List
import collections
import math
import sys
import os
from common import convertToTree
from common import create2DArray, __location__
import heapq
import functools
from common import TreeNode

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = collections.deque()
        level = 0
        queue.append(root)
        while queue:
            pop = None
            for _ in range(len(queue)):
                if not pop:
                    pop = queue.popleft()
                    if pop.left:
                        queue.append(pop.left)
                    if pop.right:
                        queue.append(pop.right)
                else:
                    next = queue.popleft()
                    if level % 2 == 0:
                        if next.val % 2 != 0 or pop.val % 2 != 0: return False
                        if next.val <= pop.val: return False
                    else:
                        if next.val % 2 == 0 or pop.val % 2 == 0: return False
                        if next.val >= pop.val: return False
                    if next.left:
                        queue.append(next.left)
                    if next.right:
                        queue.append(next.right)
                    pop = next
            level += 1
        return True
                    
sol = Solution()
print(sol.isEvenOddTree(convertToTree([1,10,4,3,None,7,9,12,8,6,None,None,2])))
print(sol.isEvenOddTree(convertToTree([5,4,2,3,3,7])))
print(sol.isEvenOddTree(convertToTree([11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17, None])))