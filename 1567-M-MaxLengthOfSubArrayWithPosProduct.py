from typing import List
import collections
import math


def getMaxLen(nums):
    ans, pos, neg = 0, 0, 0
    for num in nums:
        if num > 0:
            pos += 1
            neg = neg + 1 if neg > 0 else 0
        elif num < 0:
            pos, neg = neg + 1 if neg > 0 else 0, pos + 1
        else:
            pos, neg = 0, 0
        ans = max(ans, pos)
    return ans
def getMaxLen2(nums):
    size, res = len(nums), 0
    dp = [[1 for i in range(size)] for j in range(size)]

    for i in range(size-1, -1, -1):
        dp[i][i] = nums[i]
        res = max(res, 1 if nums[i] > 0 else 0)
        for j in range(i + 1, size):
            dp[i][j] = dp[i][i] * dp[i + 1][j]
            if (dp[i][j] > 0):
                res = max(res, j - i + 1)
    
    #print(dp)
    return res


print(getMaxLen([1, -2, -3, 4]))
print(getMaxLen([0,1,-2,-3,-4]))
print(getMaxLen([-1,-2,-3,0,1]))
print(getMaxLen([-1,2]))
print(getMaxLen([1,2,3,5,-6,4,0,10]))