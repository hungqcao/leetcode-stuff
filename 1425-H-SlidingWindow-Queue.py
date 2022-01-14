from typing import List
import collections
import math
import itertools
import heapq

def constrainedSubsetSum(nums: List[int], k: int) -> int:
    idx, N, queue = 0, len(nums), collections.deque()
    for i in range(N):

        if queue and i - queue[0] > k:
            queue.popleft()
        nums[i] += nums[queue[0]] if queue else 0
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        if nums[i] >= 0:
            queue.append(i)

        #print(queue)
    #print(nums)
    return max(nums)

    

print(constrainedSubsetSum([10,2,-10,5,20], 2))
print(constrainedSubsetSum([-1,-2,-3], 1))
print(constrainedSubsetSum([10,-2,-10,-5,20], 2))
print(constrainedSubsetSum([-5266,4019,7336,-3681,-5767],2))
    