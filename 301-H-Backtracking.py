from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    @functools.lru_cache(None)
    def isValidString(self, s):
        stack = collections.deque()
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
        return True if not stack else False
    @functools.lru_cache(None)
    def helper(self, s):
        if self.isValidString(s):
            if self.N - len(s) <= self.minLength:
                self.minLength = self.N - len(s)
                self.res[self.minLength].add(s)
                return 
            elif self.minLength < self.N and self.N - len(s) > self.minLength:
                return
        
        print(s)
        for idx, c in enumerate(s):
            self.helper(s[0:idx] + s[idx + 1:])

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = [set() for i in range(len(s) + 1)]
        self.N = len(s)
        self.minLength = len(s)
        self.helper(s)
        for s in self.res:
            if s:
                return s
        return []

        
sol = Solution()
#print(sol.removeInvalidParentheses("()())()"))
print(sol.removeInvalidParentheses("))(p(((())"))
#sol = Solution()
#print(sol.removeInvalidParentheses(")("))