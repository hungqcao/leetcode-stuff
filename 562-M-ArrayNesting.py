from typing import List
import collections
import math
from common import TreeNode, convertToTree
import itertools

def arrayNesting(nums: List[int]) -> int:
    seen = [0] * len(nums)
    res = 0
    for i in nums:
        count = 0
        while not seen[i]:
            seen[i] = 1
            count += 1
            i = nums[i]
        res = max(res, count)
    return res

print(arrayNesting([7,5,4,0,3,1,6,2]))