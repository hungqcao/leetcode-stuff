from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

def jump(nums: List[int]) -> int:
    left = right = steps = 0
    while right < len(nums) -1:
        left, right = right, max([i + nums[i] for i in range(left,right+1)])
        print(f"{left} {right}")
        if left == right: return -1
        steps += 1
    return steps

print(jump([2,3,1,1,4]))
print(jump([2,1,1,3,0,0,0,0,4]))