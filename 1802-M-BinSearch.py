from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def check(self, num, idx, maxSum):
        left = max((num - idx), 0)
        ret = (num + left) * (num - left + 1) / 2
        right =  max(0, num - (self.N - idx - 1))
        ret += (num + right) * ( num - right + 1) / 2
        return ret - num
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        self.N = n
        maxSum -= n
        left, right = 0, maxSum + 1
        while right - left > 1:
            mid = (right + left) // 2
            check = self.check(mid, index, maxSum)
            if (check > maxSum):
                right = mid
            else:
                left = mid
        return left + 1

sol = Solution()
print(sol.maxValue(4, 0, 4))
print(sol.maxValue(1, 0, 24))
print(sol.maxValue(4, 2, 6))
print(sol.maxValue(6, 1, 10))
print(sol.maxValue(3, 2, 18))