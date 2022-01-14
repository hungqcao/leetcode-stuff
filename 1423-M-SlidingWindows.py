from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

def maxScore(cardPoints: List[int], k: int) -> int:
    total = sum(cardPoints)
    curSum = ans = 0
    subLen = len(cardPoints) - k
    curSum = sum(cardPoints[0:subLen])
    for i in range(len(cardPoints) - subLen + 1):
        print(i)
        ans = max(ans, total - curSum)
        if i + subLen < len(cardPoints):
            curSum -= cardPoints[i]
            curSum += cardPoints[i + subLen]
    return ans
    
    
#print(maxScore([11,49,100,20,86,29,72], 4))
#print(maxScore([1,2,3,4,5,6,1], 3))
print(maxScore([96,90,41,82,39,74,64,50,30], 8))