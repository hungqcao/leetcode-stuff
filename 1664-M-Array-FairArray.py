from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)
        oddSum = [0 for _ in range(N)]
        evenSum = [0 for _ in range(N)]
        for i,num in enumerate(nums):
            if i % 2 == 0:
                evenSum[i] = (evenSum[i-1] if i > 0 else 0) + num
                if i > 0:
                    oddSum[i] = oddSum[i-1]
            else:
                oddSum[i] = (oddSum[i-1] if i > 0 else 0) + num
                if i > 0:
                    evenSum[i] = evenSum[i-1]
        
        res = 0
        for i, num in enumerate(nums):
            
            missingEven = evenSum[N-1] - evenSum[i]
            missingOdd = oddSum[N-1] - oddSum[i]
            newEven = (evenSum[i-1] if i > 0 else 0) + missingOdd
            newOdd = (oddSum[i-1] if i > 0 else 0) + missingEven
            if newEven == newOdd: 
                #print(i)
                res += 1

        #print(oddSum)
        #print(evenSum)
        return res
    
sol = Solution()
print(sol.waysToMakeFair([2,1,6,4]))
print(sol.waysToMakeFair([1,1,1]))
print(sol.waysToMakeFair([1,2,3]))