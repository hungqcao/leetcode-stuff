from typing import List
import collections
import math
from common import TreeNode, convertToTree
import itertools

def maxWidthRamp2(nums: List[int]) -> int:
    #arr = [b-a for a,b in itertools.combinations(range(len(nums)), 2) if nums[b] >= nums[a]]
    stack = []
    ans = 0
    for i, num in enumerate(nums):
        if stack:
            peek, idx = stack[-1]
            if num < peek:
                stack.append((num, i))
            else:
                pop = []
                while stack and num >= stack[-1][0]:
                    peek, idx = stack[-1]
                    ans = max(ans, i - idx)
                    pop.append(stack.pop())
                
                while pop:
                    stack.append(pop.pop())
        else:
            stack.append((num, i))
    return ans

def maxWidthRamp(A):
    s = []
    res = 0
    for i, a in enumerate(A):
        if not s or A[s[-1]] > a:
            s.append(i)
    for j in range(len(A))[::-1]:
        while s and A[s[-1]] <= A[j]:
            res = max(res, j - s.pop())
    return res
print(maxWidthRamp([6,0,8,2,1,5]))
print(maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))