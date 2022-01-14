from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq

class Solution:
    def findLastMaximal(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) # [left, right)
        while right - left > 1:
            mid = (left + right) // 2
            if arr[mid] <= k:
                left = mid
            else:
                right = mid
        return left # maximal statifies condition arr[mid] >= k
    def findLastMimimal(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1 #[left, right]
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= k:
                right = mid
            else:
                left = mid + 1
        return left # minimal statifies condition arr[mid] >= k

sol = Solution()
# find exact number
print(sol.findLastMimimal([2,4,6,8,10], 11))
print(sol.findLastMaximal([2,4,6,8,10], 2))
print('--')
# find largest number <= target
print(sol.findLastMaximal([2,4,6,8,10], 5))

print('--')
# find smallest number >= target
print(sol.findLastMimimal([2,4,6,8,10], 5))

print('--')
