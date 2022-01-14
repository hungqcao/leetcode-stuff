from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return math.ceil((abs(goal - sum(nums))) / limit)
        
        

    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        nums = sorted(nums, key=lambda x: (counter[x], x))
        return nums



sol = Solution()
print(sol.minElements([1,-10,9,1], 100, 0))
print(sol.minElements([1,-1,1], 3, -4))
print(sol.frequencySort([1,1,2,2,2,3]))