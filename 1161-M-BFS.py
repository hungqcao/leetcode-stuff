from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = collections.deque()
        max = float('-inf')
        res = 0
        queue.append(root)
        level = 1
        while queue:
            N = len(queue)
            curSum = 0
            for _ in range(N):
                popNode = queue.popleft()
                curSum += popNode.val
                if popNode.left: queue.append(popNode.left)
                if popNode.right: queue.append(popNode.right)
            if curSum > max:
                max = curSum
                res = level
            level+=1
        return res
    
sol = Solution()
#print(sol.maxLevelSum(convertToTree([1,7,0,7,-8,None,None])))
#print(sol.maxLevelSum(convertToTree([989,None,10250,98693,-89388,None,None,None,-32127])))
print(sol.maxLevelSum(convertToTree([-100,-200,-300,-20,-5,-10,None])))