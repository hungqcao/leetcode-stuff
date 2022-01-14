from typing import List
import collections
import math
import sys
from common import convertToTree, TreeNode

def balanceBST(root: TreeNode) -> TreeNode:
    arr = []
    def inOrder(node):
        if not node:
            return
        inOrder(node.left)
        if node.val:
            arr.append(node.val)
        inOrder(node.right)
    inOrder(root)
    def build(nums):
        if not nums:
            return None
        mid = (0 + len(nums))//2
        node = TreeNode(nums[mid], None, None)
        node.left = build(nums[:mid])
        node.right = build(nums[mid+1:])
        return node
    
    root = build(arr)
    return root


root = convertToTree([1,None,2,None,3,None,4,None,None])
print(balanceBST(root))