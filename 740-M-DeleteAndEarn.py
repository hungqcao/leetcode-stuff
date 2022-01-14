from typing import List
import collections
import math
import itertools
import heapq

def deleteAndEarn(nums: List[int]) -> int:
    arr = [0] * 10001
    for i in nums:
        arr[nums] += i
    
    take = skip = 0
    for i in range(arr):
        takei = skip + arr[i]
        skipi = max(take, skip)
        skip = skipi
        take = takei
    return max(take, skip)
    
    
#print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
#print(networkDelayTime([[1,2,1]], 2, 1))
#print(networkDelayTime([[1,2,1]], 2, 2))
#print(networkDelayTime([[1,2,1],[2,3,2],[1,3,4]],3,1))
print(networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]],3,1))