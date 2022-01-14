from typing import List
import collections
import math
import itertools
import heapq

def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0 for i in range(m + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 0
            else:
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
    
    #print(dp)
    return dp[n][m]

def numDistinct2(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 0
            else:
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
    
    #print(dp)
    return dp[n][m]

print(numDistinct('rabbbit','rabbit'))
print(numDistinct('babgbag','bag'))
    
    