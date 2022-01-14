from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

def findGCD(nums: List[int]) -> int:
    nums.sort()
    a, b = nums[0], nums[-1]
    for i in range(a, 0, -1):
        if b % i == 0 and a % i == 0: return i
    return 1

print(findGCD([2,5,6,9,10]))
print(findGCD([7,5,6,8,3]))
print(findGCD([3,3]))