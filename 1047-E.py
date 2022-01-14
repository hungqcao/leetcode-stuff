from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = collections.deque()
        for c in s:
            if not stack: stack.append(c)
            else:
                if c != stack[-1]:
                    stack.append(c)
                else:
                    stack.pop()
        return "".join(stack)

                


        
sol = Solution()
print(sol.removeDuplicates("abbaca"))
print(sol.removeDuplicates("azxxzy"))