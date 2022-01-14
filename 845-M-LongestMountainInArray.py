from typing import List
import collections
import math

def longestMountain(arr: List[int]) -> int:
    res = up = down = 0
    for i in range(1, len(arr)):   
        if down and arr[i - 1] < arr[i] or arr[i - 1] == arr[i]:
            up = down = 0     
        up += arr[i - 1] < arr[i]
        down += arr[i - 1] > arr[i]
        if up and down: res = max(res, down + up + 1)
    return res

def longestMountain2(arr: List[int]) -> int:
    res, N = 0, len(arr)
    if N < 3: return res
    start = 0
    while start < N - 1:
        end = start
        while end < N - 1 and arr[end] < arr[end + 1]:
            end += 1
        tmp = end
        while end > start and end < N - 1 and arr[end] > arr[end + 1]:
            end += 1
        if end > tmp:
            print(f'{start} -> {end}')
            res = max(res, end - start + 1)
            start = end
        else:
            start = end + 1
    return res
            
print(longestMountain([2,1,4,7,3,2,5]))
print(longestMountain([2,2,2]))
print(longestMountain([0,1,2,3,4,5,4,3,2,1,0]))
print(longestMountain([0,1,2,3,4,5,6,7,8,9]))
print(longestMountain([875,884,239,731,723,685]))