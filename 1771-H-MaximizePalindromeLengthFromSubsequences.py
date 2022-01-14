from typing import List
import collections
import math

def longestPalindrome(word1: str, word2: str) -> int:
    size1, size2 = len(word1), len(word2)
    s = word1 + word2
    size = len(s)
    res = 0
    dp = [[0 for i in range(size)] for j in range(size)]
    for i in range(size - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, size):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
                if j >= size1 and i < size1:
                    res = max(res, dp[i][j])
            else:
                dp[i][j] = max(dp[i][j-1], dp[i + 1][j])

        print(dp)
    return res


def topDown(s: str) -> int:

    def helper(left, right, memo):
        if left == right:
            return 1
        if left > right:
            return 0
        if (left, right) in memo:
            return memo[(left, right)]

        if s[left] == s[right]:
            memo[(left, right)] = helper(left + 1, right -1, memo) + 2
        else:
            memo[(left, right)] = max(helper(left + 1, right, memo), helper(left, right - 1, memo))
        
        return memo[(left, right)]
    
    return helper(0, len(s) - 1, {})

print(longestPalindrome("ba", "b"))
