from typing import List
import collections
import math
import sys
import heapq

def lastStoneWeightII(stones: List[int]) -> int:
    total = sum(stones)
    max_weight = total // 2
    dp = [0 for i in range(max_weight + 1)]

    for w in stones:
        for j in range(max_weight + 1)[::-1]:
            if w <= j:
                dp[j] = max(dp[j], dp[j - w] + w)
    print(dp)
    return total - 2 * dp[max_weight]

def lastStoneWeightII_2d(stones: List[int]) -> int:
    total = sum(stones)
    max_weight = total // 2
    dp = [[0 for i in range(max_weight + 1)] for i in range(len(stones) + 1)]
    #print(dp)
    for i in range(1,len(stones) + 1):
        for j in range(1, max_weight + 1):
            if stones[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - stones[i-1]] + stones[i-1])
    print(dp)
    return total - 2 * dp[len(stones)][max_weight]


print(lastStoneWeightII([2,7,4,1,8,1]))
#print(lastStoneWeightII([1,2]))
#print(lastStoneWeightII([31,26,33,21,40]))