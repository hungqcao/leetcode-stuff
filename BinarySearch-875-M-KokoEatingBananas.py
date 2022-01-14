from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (right + left) // 2

            count = 0
            for p in piles:
                count += ((p + mid - 1) // mid)
            
            if count <= h:
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))
print(sol.minEatingSpeed([30,11,23,4,20], 5))