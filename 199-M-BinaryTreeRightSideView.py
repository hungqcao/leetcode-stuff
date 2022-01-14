from typing import List
import collections
import math
from common import TreeNode, convertToTree

def rightSideView(root: TreeNode) -> List[int]:
    if root == None:
        return []
    queue, res = [], []
    queue.append(root)
    while queue:
        size = len(queue)
        for i in range(0, size):
            curNode = queue.pop(0)
            if i == size - 1:
                res.append(curNode.val)
            if curNode.left != None:
                queue.append(curNode.left)
            if curNode.right != None:
                queue.append(curNode.right)
    return res


root = convertToTree([1,2,3,None,5,None,4])
print(rightSideView(root))
root = convertToTree([1,None,3])
print(rightSideView(root))