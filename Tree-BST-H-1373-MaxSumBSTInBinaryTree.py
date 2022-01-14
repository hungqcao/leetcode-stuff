from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList, TreeNode, convertToTree

class Solution:
    def dfs(self, node):
        if not node: return (None, True, None, None)
        total_sum_left, isBST_left, min_left_val, max_left_val = self.dfs(node.left)
        total_sum_right, isBST_right, min_right_val, max_right_val = self.dfs(node.right)
        if not total_sum_left and not total_sum_right:
            self.res = max(self.res, node.val)
            return (node.val, True, node.val, node.val)
        elif total_sum_right and total_sum_left:
            new_sum = total_sum_left + total_sum_right + node.val
            if isBST_left and isBST_right:
                if max_left_val < node.val < min_right_val:
                    self.res = max(self.res, new_sum)
                    return (new_sum, True, min_left_val, max_right_val)
            return (new_sum, False, min(min_left_val, node.val), max(max_right_val, node.val))
        elif total_sum_right:
            new_sum = total_sum_right + node.val
            if isBST_right:
                if node.val < min_right_val:
                    self.res = max(self.res, new_sum)
                    return (new_sum, True, node.val, max_right_val)
            return (new_sum, False, min(min_right_val, node.val), max(max_right_val, node.val))
        else:
            new_sum = total_sum_left + node.val
            if isBST_left:
                if node.val > max_left_val:
                    self.res = max(self.res, new_sum)
                    return (new_sum, True, min_left_val, node.val)
            return (new_sum, False, min(min_left_val, node.val), max(max_left_val, node.val))


    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        print(self.res)
        return self.res

sol = Solution()
sol.maxSumBST(convertToTree([1,4,3,2,4,2,5,None,None,None,None,None,None,4,6]))
sol.maxSumBST(convertToTree([4,3,None,1,2]))
sol.maxSumBST(convertToTree([-4,-2,-5]))