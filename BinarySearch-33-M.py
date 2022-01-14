from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def search(self, nums: List[int], target: int) -> int:      
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 # 0 + 1 // 2 = 0

            # left
            if nums[left] <= nums[mid]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1


        return left if nums[left] == target else -1

sol = Solution()
#print(sol.search([4,5,6,7,0,1,2], 0))
print(sol.search([3, 1], 1))