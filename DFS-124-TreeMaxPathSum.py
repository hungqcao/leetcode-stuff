from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json
import functools
from common import ListNode, convertToTree, TreeNode

class Solution:

    def dfs(self, node: TreeNode):
        if not node: return 0
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        val = node.val + left + right
        self.res = max(self.res, val)
        return node.val + max(left, right)

    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -2000
        self.dfs(root)
        return self.res


sol = Solution()
print(sol.maxPathSum(convertToTree([-10,9,20,None,None,15,7])))
print(sol.maxPathSum(convertToTree([1,-2,-3,1,3,-2,None,-1])))