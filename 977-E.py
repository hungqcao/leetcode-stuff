from typing import List
import collections
import math
import sys
from common import create2DArray

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0]*len(nums)
        idx = len(nums) - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                res[idx] = nums[left]**2
                left += 1
            else:
                res[idx] = nums[right]**2
                right -= 1
            idx -= 1
        return res
    
sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
print(sol.sortedSquares([-7,-3,2,3,11]))
        


