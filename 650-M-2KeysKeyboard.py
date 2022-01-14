from typing import List
import collections
import math
import itertools
import heapq

def minSteps(n: int) -> int:
    dp = [float('inf')] * (n + 1)
    dp[0] = dp[1] = 0
    if n <= 1: return dp[n]
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = i
        for j in range(2, math.ceil(i / 2) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
    return dp[n]
    
#print(minSteps(1))
#print(minSteps(2))
#print(minSteps(3))
#print(minSteps(4))
#print(minSteps(5))
#print(minSteps(11))
print(minSteps(50))
#print(minSteps(721))
print(minSteps(722))