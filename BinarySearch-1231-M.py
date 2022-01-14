from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def maximizeSweetness(self, nums: List[int], k: int) -> int:            
        left, right = 1, sum(nums) / k
        while left < right:
            mid = (left + right) // 2
            
            count = csum = 0
            for idx, n  in enumerate(nums):
                csum += n
                if csum > mid:
                    count += 1
                    csum = 0

            if count <= k:
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
print(sol.maximizeSweetness([1,2,3,4,5,6,7,8,9], 5))