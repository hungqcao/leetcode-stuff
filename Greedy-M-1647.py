from typing import List
import math
import sys
import os
import collections
from common import create2DArray, __location__
import json
import functools
import heapq

class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        arr = [-v for v in counter.values()]
        heapq.heapify(arr)
        res = 0
        while arr:
            n = -heapq.heappop(arr)
            if arr and n == -arr[0]:
                if n - 1 != 0:
                    heapq.heappush(arr, -(n - 1))
                res += 1
        print(res)
        return res

            


sol = Solution()
sol.minDeletions("bbcebab")
sol.minDeletions("aaabbbcc")
sol.minDeletions("ceabaacb")