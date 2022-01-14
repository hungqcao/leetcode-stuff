from typing import List
import collections
import math

def peakIndexInMountainArray(arr: List[int]) -> int:
    low, hi = 0, len(arr)
    while low < hi:
        mid = (low + hi) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            hi = mid
    return low



print(peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))