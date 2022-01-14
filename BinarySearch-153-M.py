from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def findMin(self, nums: List[int]) -> int: 
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 # 0 + 1 // 2 = 0

            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]

            if nums[left] >= nums[mid] >= nums[right]:
                return nums[right]

            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            # left
            if nums[left] <= nums[mid]:
                left = mid
            else:
                right = mid
               
        return -1

sol = Solution()
print(sol.findMin([3,4,5,1,2]))
print(sol.findMin([4,5,6,7,0,1,2]))
print(sol.findMin([11,13,15,17]))