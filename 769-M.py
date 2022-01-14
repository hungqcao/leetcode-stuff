from typing import List
import collections
import math
import sys
from common import create2DArray

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        count = p = 0
        while p < len(arr):
            if sorted_arr[p] == arr[p]:
                count += 1
            else:
                start = p
                while p < len(arr) and collections.Counter(arr[start:p+1]) != collections.Counter(sorted_arr[start:p+1]):
                    p += 1
                count += 1
                
            p += 1
        return count
    
sol = Solution()
print(sol.maxChunksToSorted([1,1,1,0,1,0,0,0,1,0]))
print(sol.maxChunksToSorted([1,0,2,3,4]))
        


