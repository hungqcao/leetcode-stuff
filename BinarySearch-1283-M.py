from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            tmp = sum([(i + mid - 1) // mid for i in nums])
            if tmp <= threshold:
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
print(sol.smallestDivisor([1,2,5,9], 6))
print(sol.smallestDivisor([44,22,33,11,1], 5))