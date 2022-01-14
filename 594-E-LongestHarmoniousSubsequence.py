from typing import List
import collections
import math
import itertools
import heapq

def findLHS(nums: List[int]) -> int:
    counter = collections.Counter(nums)
    ans = 0
    for k in counter.keys():
        ans = max(ans, counter[k] + counter[k+1] if k + 1 in counter else 0)
    return ans

    
    
print(findLHS([1,3,2,2,5,2,3,7]))
print(findLHS([1,2,3,4]))
print(findLHS([1,1,1,1]))