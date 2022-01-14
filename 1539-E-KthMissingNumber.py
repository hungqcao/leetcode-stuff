from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = -1, len(arr)
        while right - left > 1:
            mid = (left + right) // 2
            if arr[mid] - 1 - mid >= k:
                right = mid
            else:
                left = mid
        return right + k
    def findKthPositive2(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1 
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - 1 - mid >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left + k

sol = Solution()
#print(sol.findKthPositive([2,3,4,7,12], 5))
#print(sol.findKthPositive([2], 1))
#print(sol.findKthPositive([1,2,3,4], 2))
#print(sol.findKthPositive2([1,2,3,4], 3))