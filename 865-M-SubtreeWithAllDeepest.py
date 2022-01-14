from typing import List
import collections
import math
import sys
import os
from common import convertToTree, TreeNode
import json

def subtreeWithAllDeepest(root: TreeNode) -> TreeNode:
    deepestDepth, res = [float('-inf')], [None]
    def dfs(node: TreeNode, depth):
        deepestDepth[0] = max(depth, deepestDepth[0])
        if not node:
            return depth
        left = dfs(node.left, depth  + 1)
        right = dfs(node.right, depth  + 1)

        if left == deepestDepth[0] and right == deepestDepth[0]:
            res[0] = node

        return max(left, right)
    dfs(root, 0)
    return res[0]


root = convertToTree([3,5,1,6,2,0,8,None,None,None,4,None,None,None,None])
print(subtreeWithAllDeepest(root))

#root = convertToTree([0,1,3,None,2,None,None])
#print(subtreeWithAllDeepest(root))