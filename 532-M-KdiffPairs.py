from typing import List
import collections
import math
import itertools
import heapq

def findPairs(nums: List[int], k: int) -> int:
    mySet = collections.Counter(nums)
    count = 0
    for num in mySet.keys():
        if k == 0 and mySet[num] >= 2:
            count += 1
        elif k > 0 and k + num in mySet:
            #print(num)
            count += 1
    return count
    
    
print(findPairs([3,1,4,1,5], 2))
print(findPairs([1,2,3,4,5], 1))
print(findPairs([1,3,1,5,4], 0))
print(findPairs([1,2,4,4,3,3,0,9,2,3], 3))
print(findPairs([-1,-2,-3], 1))
