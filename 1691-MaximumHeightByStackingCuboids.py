from typing import List
import collections
import math
import sys
from common import create2DArray

def maxHeight(cuboids: List[List[int]]) -> int:
    cuboids = [[0, 0, 0]] + sorted(map(sorted, cuboids))
    #print(cuboids)
    dp = [0 for i in range(len(cuboids))]
    for i in range(1, len(cuboids)):
        for j in range(i):
            if all([cuboids[j][k] <= cuboids[i][k] for k in range(3)]):
                dp[i] = max(dp[i], dp[j] + cuboids[i][2])
    #print(dp)
    return max(dp)



#maxHeight([[50,45,20],[95,37,53],[45,23,12]])
maxHeight([[38,25,45],[76,35,3]])