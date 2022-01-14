from typing import List
import collections
import math
def minTaps(n: int, ranges: List[int]):
    jumps = [0 for i in range(n + 1)]
    for i in range(n+1):
        if ranges[i] == 0:
            continue
        l = max(0,i-ranges[i])
        jumps[l] = max(jumps[l], i + ranges[i])
    res = low = hi = 0
    while hi < n:
        low, hi = hi, max(jumps[low:hi+1])
        if low == hi: return -1
        res += 1

    return res


def minTaps2(n: int, ranges: List[int]):
    dp = [n + 1 for _ in range(n+1)]
    dp[0] = 0
    for i in range(len(ranges)):
        start = max(0, i-ranges[i])
        end = min(i + ranges[i], n)
        for j in range(start + 1, end + 1):
            dp[j] = min(dp[j], dp[start] + 1)
        print(dp)

        




#print(minTaps(5, [3,4,1,1,0,0]))
print(minTaps(7, [1,2,1,0,2,1,0,1]))
#print(minTaps(5, [4,0,0,0,0,0,0,0,4]))
#print(minTaps(5, [0,0,0,1,0,0]))
#print(minTaps(5, [3,4,1,1,0,0]))