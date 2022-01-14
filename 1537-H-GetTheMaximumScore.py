from typing import List
import collections
import math
import sys
from common import create2DArray

def maxSum(nums1: List[int], nums2: List[int]) -> int:
    p1, p2, sum1, sum2 = len(nums1) - 1, len(nums2) - 1, 0, 0
    mod = 10**9 + 7
    while p1 >= 0 and p2 >= 0:
        val1 = nums1[p1]
        val2 = nums2[p2]

        if val1 > val2:
            sum1 += val1
            p1 -= 1
        elif val1 < val2:
            sum2 += val2
            p2 -= 1
        else:
            sum1 = sum2 = max(sum1, sum2) + val2
            p1 -= 1
            p2 -= 1
    #if p1 >= 0:
    sum1 += sum(nums1[:p1 + 1])

    #if p2 >= 0:
    sum2 += sum(nums2[:p2 + 1])
    return max(sum1, sum2) % mod

#print(maxSum([2,4,5,8,10],[4,6,8,9]))
#print(maxSum([1,3,5,7,9],[3,5,100]))
#print(maxSum([1,2,3,4,5],[6,7,8,9,10]))
#print(maxSum([1,4,5,8,9,11,19],[2,3,4,11,12]))
