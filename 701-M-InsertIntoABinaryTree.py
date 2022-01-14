from typing import List
import collections
import math
from common import TreeNode, convertToTree
import itertools

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if not root: return TreeNode(val)
    if root.val <= val:
        root.right = insertIntoBST(root.right, val)
    else:
        root.left = insertIntoBST(root.left, val)
    return root
            
node = insertIntoBST(convertToTree([5,2,7,1,3, None, None]), 4)

print(node)