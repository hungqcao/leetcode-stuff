from typing import List
import collections
import math
import itertools
import heapq

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    N, queue = len(nums), collections.deque()
    ans = []
    
    for i in range(k):
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)
    
    for i in range(k, N):
        print(f'deque: {queue}')
        ans.append(nums[queue[0]])
        if i - queue[0] >= k:
            queue.popleft()
         
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)

    if queue:
        ans.append(nums[queue[0]])
        
    return ans

    
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1, -1], 1))
print(maxSlidingWindow([9, 11], 2))
print(maxSlidingWindow([4, -2], 2))
print(maxSlidingWindow([1,3,1,2,0,5],3))