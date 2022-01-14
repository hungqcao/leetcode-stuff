from typing import List
import collections
import math
import sys
import os
import functools
import json

def minDifficulty(jobDifficulty: List[int], d: int) -> int:
    size = len(jobDifficulty)
    if d  > size: return -1

    @functools.lru_cache(None)
    def dfs(start, d):
        print(f'{start} {d}')
        if d == 1: return max(jobDifficulty[start:])

        res = float('inf')
        for i in range(start, size - d + 1):
            tmp = max(jobDifficulty[start:i + 1]) + dfs(i + 1, d - 1)
            res = min(res, tmp)
        return res
    return dfs(0, d)


#print(minDifficulty([6,5,4,3,2,1], 2))
#print(minDifficulty([1,1,1], 3))
#print(minDifficulty([7,1,7,1,7,1], 3))
#print(minDifficulty([11,111,22,222,33,333,44,444], 6))
minDifficulty([380,302,102,681,863,676,243,671,651,612,162,561,394,856,601,30,6,257,921,405,716,126,158,476,889,699,668,930,139,164,641,801,480,756,797,915,275,709,161,358,461,938,914,557,121,964,315],10)
minDifficulty([324,448,44,267,802,893,373,421,57,11,695,368,817,753,227,214,201,285,473,236,649,580,149,231,353,932,7,961,222,677,921,826,224,595,28,765,780,888,718,358,702,254,245,235,671,3,750,197,977,806,206,105,111,258,829,794,972,973,439,738,701,959,276,54,503,89,662,249,238,831,849,999,822,928,174,127,991,697,98,273,354,682,404,320],8)