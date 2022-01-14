from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def check(self, bloomDay, curDay, k):
        flowers = bouques = 0
        for i in bloomDay:
            if i > curDay:
                flowers = 0
            else:
                bouques += (flowers + 1) // k
                flowers = (flowers + 1) % k
        return bouques

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left, right = 0, max(bloomDay)
        while right - left > 1:
            mid = (left + right) // 2
            if self.check(bloomDay, mid, k) >= m:
                right = mid
            else:
                left = mid
        return right

sol = Solution()
print(sol.minDays([1,10,3,10,2], 3, 1))