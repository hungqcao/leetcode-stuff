from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
import bisect
from common import ListNode, convertToLinkedList

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = sorted(heaters)
        res = 0
        for house in houses:
            index = bisect.bisect_left(heaters, house)
            if index == len(heaters):
                res = max(res, house - heaters[-1])
            elif index == 0:
                res = max(res, heaters[0] - house)
            else:
                res = max(res, min(house - heaters[index - 1], heaters[index] - house))
        return res
            

sol = Solution()
print(sol.findRadius([1,2,3], [2]))