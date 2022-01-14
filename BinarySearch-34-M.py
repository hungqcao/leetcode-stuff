from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:  
        left, right = 0, len(nums) - 1 # 0, 1
        while left < right:
            mid = (left + right) // 2 # 0 + 1 // 2 = 0
            if nums[mid] == target:
                start = end = mid # 0, 0
                while start > 0 and nums[start] == nums[mid]:
                    start -= 1
                while end < len(nums) - 1 and nums[end] == nums[mid]:
                    end += 1
                return [start if nums[start] == target else start + 1, end if nums[end] == target else end - 1]
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if left < len(nums) and nums[left] == target:
            return [left, left]
                
        return [-1, -1]

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([], 8))
print(sol.searchRange([1], 1))
print(sol.searchRange([2, 2], 2))