from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        st = collections.deque()
        for idx, c in enumerate(s):
            if c in ('(', ')'):
                if st and s[st[-1]] == '(' and c == ')':
                    st.pop()
                else:
                    st.append(idx)
        print(st)
        while st:
            s[st.pop()] = ''
        return ''.join(s)




sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
print(sol.minRemoveToMakeValid("a)b(c)d"))
print(sol.minRemoveToMakeValid("))(("))