from typing import List
import collections
import math

def countSpecialSubsequences(nums: List[int]) -> int:
    dp = [0] * 3
    for n in nums:
        if n == 0:
            dp[0] += dp[0] + 1
        else:
            dp[n] += dp[n] + dp[n - 1]
    return dp[-1]

print(countSpecialSubsequences([0,1,2,2]))
print(countSpecialSubsequences([2,2,0,0]))
print(countSpecialSubsequences([0,1,2,0,1,2]))