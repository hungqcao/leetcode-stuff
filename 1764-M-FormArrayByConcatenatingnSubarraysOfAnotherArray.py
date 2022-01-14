from typing import List
import collections

def canChoose(groups: List[List[int]], nums: List[int]) -> bool:
    start = 0
    for group in groups:
        found = False
        while not found:
            while start < len(nums) and nums[start] != group[0]:
                start += 1
            
            if start >= len(nums):
                return False

            tmp, tail, size = 0, start, len(group)
            while tail < len(nums) and tmp < len(group) and nums[tail] == group[tmp]:
                tmp += 1
                tail += 1
            if tail - start == size:
                found = True
            if found:
                start = tail
            else:
                start += 1

    return True


print(canChoose([[1,-1,-1],[3,-2,0]], [1,-1,0,1,-1,-1,3,-2,0]))
print(canChoose([[10,-2],[1,2,3,4]], [1,2,3,4,10,-2]))
print(canChoose([[1,2,3],[3,4]], [7,7,1,2,3,4,7,7]))
print(canChoose([[21,22,21,22,21,30]], [21,22,21,22,21,22,21,30]))