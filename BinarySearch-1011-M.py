from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:         
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            
            count = 1
            csum = 0
            for idx, n  in enumerate(weights):
                if csum + n <= mid:
                    csum += n
                else:
                    count += 1
                    csum = n

            if count <= days:
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(sol.shipWithinDays([3,2,2,4,1,4], 3))
print(sol.shipWithinDays([1,2,3,1,1], 4))