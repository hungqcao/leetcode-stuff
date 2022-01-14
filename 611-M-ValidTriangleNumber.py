from typing import List
import collections

def triangleNumber(nums: List[int]) -> int:
    nums = sorted(nums)
    res, N = 0, len(nums)
    for i in range(2, N)[::-1]:
        left, right = 0, i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                res += (right-left)
                right-=1
            else:
                left += 1
    return res


print(triangleNumber([0,1,0]))
print(triangleNumber([2,2,3,4]))
print(triangleNumber([4,2,3,4]))