from typing import List
import collections
import math
import sys
from common import create2DArray

def smallestRange(nums: List[List[int]]) -> List[int]:
    lst = []
    for i in range(len(nums)):
        for num in nums[i]:
            lst.append((num, i))
    lst.sort(key=lambda x: x[0])
    size = len(lst)
    start, end = 0, 0
    indices = collections.defaultdict(int)
    head, tail = -1e9, 1e9
    #print(lst)
    while end < size:
        curNum, listIdx = lst[end]
        indices[listIdx] += 1

        while len(indices) == len(nums) and start <= end:
            #[head, tail]
            c, d = lst[start][0], lst[end][0]
            if tail - head > d - c or (c < head and tail - head == d - c):
                head, tail = c, d
                #print(f'Found {head} {tail}')
            tmp, removed = lst[start]
            indices[removed] -= 1
            if indices[removed] == 0:
                indices.pop(removed)
            start += 1
            
        end += 1
        
    return [head, tail]

print(smallestRange([[1]]))
print(smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(smallestRange([[1,2,3],[1,2,3],[1,2,3]]))
print(smallestRange([[10,10],[11,11]]))
print(smallestRange([[10],[11]]))
print(smallestRange([[1],[2],[3],[4],[5],[6],[7]]))