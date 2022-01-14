from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep = 0
        for idx, step in enumerate(nums):
            if maxStep < idx:
                return False
            maxStep = max(maxStep, step + idx)
        return True


sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))