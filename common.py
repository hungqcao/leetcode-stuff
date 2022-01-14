from typing import List
import collections
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convertToLinkedList(nums: List[int]):
    head = ListNode(nums[0])
    node = head
    for i in range(1, len(nums)):
        node.next = ListNode(nums[i])
        node = node.next    
    return head

def convertToTree(nums: List[int]):
    def helper(nodes: List[TreeNode], subList: List[int]):
        if not subList:
            return
        newNodes = []
        for node in nodes:
            if subList:
                if (subList[0] != None):
                    node.left = TreeNode(subList[0])
                    newNodes.append(node.left)
                subList.pop(0)
                if subList:
                    if (subList[0] != None):
                        node.right = TreeNode(subList[0])
                        newNodes.append(node.right)
                    subList.pop(0)
        helper(newNodes, subList)
    root = TreeNode(nums[0])
    nums.pop(0)
    helper([root], nums)
    return root
def create2DArray(initValue, row, col):
    return [[initValue for r in range(col)] for r in range(row)]


