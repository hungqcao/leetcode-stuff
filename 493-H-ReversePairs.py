from typing import List
import collections
import math

def reversePairs(nums: List[int]) -> int:
    count = [0]
    def helper(left, right):        
        if len(left) < 1:
            return right
        if len(right) < 1:
            return left
        left = helper(left[:len(left)//2], left[len(left)//2:])
        right = helper(right[:len(right)//2], right[len(right)//2:])
        l, r =  0, 0
        while l  < len(left) and r < len(right):
            if left[l] <= 2 * right[r]:
                l += 1
            else:
                count[0] += len(left) - l 
                r += 1
        return sorted(left + right)
    
    helper(nums[:len(nums)//2], nums[len(nums)//2:])
    return count[0]


print(reversePairs([1,3,2,3,1]))
print(reversePairs([2,4,3,5,1]))
print(reversePairs([2,4,3,5,1]))



