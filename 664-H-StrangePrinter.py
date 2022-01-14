from typing import List
import collections
import math

def strangePrinter(s: str):
    if not s: return 0
    s = ''.join(a for a, b in zip(s, '#' + s) if a != b)
    size = len(s)
    dp = [[float('inf') for r in range(size)] for r in range(size)]
    #dp[i][i] = 1
    #dp[i][i+1] = 2 if s[i] != s[i+1]
    #dp[i][i+len] = min(dp[i][k],dp[k+1][i+len]) if s[k] != s[k+1] e
    for i in range(size):
        dp[i][i] = 1
        if i < size - 1: 
            dp[i][i+1] = 1 if s[i] == s[i + 1] else 2
    for _len in range(2, size):
        for i in range(size-_len):
            for k in range(_len):
                tmp = dp[i][i+k] + dp[i+k+1][i+_len]
                dp[i][i+_len] = min(dp[i][i+_len], tmp - 1 if s[i+k] == s[i+_len] else tmp)
    return dp[0][size - 1]





print(strangePrinter('aaabbbaaaa'))
print(strangePrinter('aababbabaaaa'))