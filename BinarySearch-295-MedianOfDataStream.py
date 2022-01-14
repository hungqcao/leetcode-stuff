from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:

    def __init__(self):
        self.maxH = []
        self.minH = []

    @functools.lru_cache(None)
    def addNum(self, num: int) -> None:        
        if self.isOdd():
            heapq.heappush(self.maxH, -heapq.heappushpop(self.minH, num))
        else:
            heapq.heappush(self.minH, -heapq.heappushpop(self.maxH, -num))

    def findMedian(self) -> float:
        print(f'min: {self.minH}')
        print(f'max: {self.maxH}')
        if self.isOdd():
            return self.minH[0]
        else:
            return (-self.maxH[0] + self.minH[0]) / 2
    
    def isOdd(self):
        return len(self.maxH) != len(self.minH)

sol = Solution()
# print(sol.addNum(1))
# print(sol.addNum(2))
# print(sol.findMedian())
# print(sol.addNum(3))
# print(sol.findMedian())
# print(sol.addNum(4))
# print(sol.findMedian())
# print(sol.addNum(5))
# print(sol.findMedian())
# print(sol.addNum(6))
# print(sol.findMedian())

print(sol.addNum(-1))
print(sol.addNum(-2))
print(sol.findMedian())
print(sol.addNum(-3))
print(sol.findMedian())
print(sol.addNum(-4))
print(sol.findMedian())
print(sol.addNum(-5))
print(sol.findMedian())