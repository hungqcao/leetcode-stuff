from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

def minStoneSum(piles: List[int], k: int) -> int:
    max_heap = []
    for n in piles:
        heapq.heappush(max_heap, -n)
    while k > 0:
        num = -heapq.heappop(max_heap)
        num = math.ceil(num / 2)
        if num != 0:
            heapq.heappush(max_heap, -num)
        k -= 1
    
    return sum([-n for n in max_heap])
    
    
print(minStoneSum([5, 4, 9], 2))