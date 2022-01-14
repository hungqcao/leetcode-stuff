from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode
class Solution:
    def calculate(self, s: str) -> int:
        stack = collections.deque()
        idx = 0

        while idx < len(s):
            c = s[idx]
            if c.isspace():
                idx += 1
                continue
            elif c.isnumeric():
                n = ''
                while idx < len(s) and s[idx].isnumeric():
                    n += s[idx]
                    idx+= 1
                n = int(n)
                while stack and stack[0] in ('*', '/'):
                    op = stack.popleft()
                    left = stack.popleft()
                    if op  == '*':
                        n *= int(left)
                    else:
                        n = int(left) // n
                stack.appendleft(n)
            else:
                idx += 1
                stack.appendleft(c)


        print(stack)
        while len(stack) > 2:
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            if op == '+':
                res = int(left) + int(right)
            else:
                res = int(right) - int(left)
            stack.append(res)
        return stack[0]

sol = Solution()
#print(sol.calculate("3+2*2"))
#print(sol.calculate(" 3/2 "))
#print(sol.calculate(" 3 + 5 /2"))
#print(sol.calculate("42"))
print(sol.calculate("1-1+1"))
print(sol.calculate("0-2147483647"))