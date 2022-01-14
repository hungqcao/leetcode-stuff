from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json
import functools

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sums[i] += (nums[i-1] + sums[i-1])
        print(sums)
        target = sums[-1] - x
        if target == 0: return len(nums)
        
        d = collections.defaultdict()
        res = -1
        for i in range(len(sums)):
            if sums[i] - target in d:
                left, right = min(d[sums[i] - target], i), max(d[sums[i] - target], i)

                print(f'{left} {right}')
                res = max(res, (right - left))
            d[sums[i]] = i
        return len(nums) - res if res > 0 else -1
        



sol = Solution()
print(sol.minOperations([1,1,4,2,3], 5))
print(sol.minOperations([5,6,7,8,9], 4))
print(sol.minOperations([3,2,20,1,1,3], 10))
print(sol.minOperations([5,2,3,1,1], 5))
print(sol.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309],134365))
#print(sol.minOperations([1241,8769,9151,3211,2314,8007,3713,5835,2176,8227,5251,9229,904,1899,5513,7878,8663,3804,2685,3501,1204,9742,2578,8849,1120,4687,5902,9929,6769,8171,5150,1343,9619,3973,3273,6427,47,8701,2741,7402,1412,2223,8152,805,6726,9128,2794,7137,6725,4279,7200,5582,9583,7443,6573,7221,1423,4859,2608,3772,7437,2581,975,3893,9172,3,3113,2978,9300,6029,4958,229,4630,653,1421,5512,5392,7287,8643,4495,2640,8047,7268,3878,6010,8070,7560,8931,76,6502,5952,4871,5986,4935,3015,8263,7497,8153,384,1136],894887480))