from typing import DefaultDict, List
import collections
import math
import sys

def coinChange(coins: List[int], amount: int) -> int:
    dp = [sys.maxsize for i in range(amount + 1)]
    
    for c in coins:
        dp[c] = 1
    for n in range(amount + 1):            
        for c in coins:                
            if c <= n:
                dp[n] = min(dp[n], dp[n-c] + 1)
        print(dp)
    return dp[amount]

print(coinChange([1,2,5], 11))