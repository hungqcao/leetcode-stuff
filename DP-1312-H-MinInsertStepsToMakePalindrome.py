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
    def minInsertions(self, s: str) -> int:
        if not s: return 0
        start, end = 0, len(s) - 1
        if s[start] != s[end]:
            return 1 + min(self.minInsertions(s[1:]), self.minInsertions(s[:len(s)-1]))
        else:
            return self.minInsertions(s[1:len(s)-1])

        
        

sol = Solution()
#print(sol.minInsertions("zzazz"))
#print(sol.minInsertions("mbadm"))
#print(sol.minInsertions("leetcode"))
print(sol.minInsertions("tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz"))
print([1,2,3][::5])