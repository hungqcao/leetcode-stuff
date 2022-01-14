from typing import Counter, List
import collections
import math
import sys
from common import create2DArray

def minDifference(nums: List[int]) -> int:
    nums = sorted(nums)
    return min(b-a for a,b in zip(nums[:4], nums[-4:]))
#print(dp(3, 2, 0, 0))
#print(dp(1, 0, 0, 0))
print(minDifference([6,6,0,1,1,4,6]))