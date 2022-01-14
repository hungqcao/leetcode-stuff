from typing import List
import collections
import math
import itertools
import heapq

def sumEvenAfterQueries(nums: List[int], queries: List[List[int]]) -> List[int]:
    curSum = sum(i for i in nums if i%2==0)
    ans = []
    for val, idx in queries:
        prev = nums[idx]
        newVal = prev + val
        if prev % 2 == 0:
            if newVal % 2 == 0:
                curSum -= prev
                curSum += newVal
            else:
                curSum -= prev
        else:
            if newVal % 2 == 0:
                curSum += newVal
        nums[idx] = newVal
        ans.append(curSum)
    return ans

print(sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))
print(sumEvenAfterQueries([1], [[4,0]]))

    
    