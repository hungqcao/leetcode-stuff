from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s = list(s)
        st = collections.deque()
        for idx, c in enumerate(s):
            if self.check(st, k, c):
                tmp = 1
                while tmp < k:
                    tmp += 1      
                    st.pop()
            else:
                st.append(c)
        print(st)
        return ''.join(st)
    def check(self, st, k, c):
        tmp = 1
        while len(st) >= k - 1 and tmp < k and st[0-(tmp)] == c:
            tmp += 1      
        if tmp == k:
            return True
        return False      




sol = Solution()
print(sol.removeDuplicates("abcd", 2))
print(sol.removeDuplicates("deeedbbcccbdaa", 3))
print(sol.removeDuplicates("pbbcggttciiippooaais", 2))