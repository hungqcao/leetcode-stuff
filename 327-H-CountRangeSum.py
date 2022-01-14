from typing import List
import collections
import math

def countRangeSum(nums: List[int], lower: int, upper: int) -> int:
    ans, size, sums = 0, len(nums), [0]
    for i in nums:
        sums.append(sums[-1] + i)
    
    def mergeSort(start, end):
        if start == end: return 0
        mid = (start + end) // 2
        count = mergeSort(start, mid) + mergeSort(mid + 1, end)
        i = j = mid + 1
        for left in sums[start:mid + 1]:
            while i <= end and sums[i] - left < lower:
                i += 1
            while j <= end and sums[j] - left <= upper:
                j += 1
            count += (j - i)
        sums[start:end+1] = sorted(sums[start:end+1])
        return count
    ans = mergeSort(0, len(sums) - 1)
    return ans
            
print(countRangeSum([-2,5,-1], -2, 2))
print(countRangeSum([0], 0, 0))
print(countRangeSum([0, 0], 0, 0))
print(countRangeSum([2147483647,-2147483648,-1,0], -1, 0))