from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

def longestDecomposition(text: str) -> int:
    head, tail = 0, len(text) - 1
    left = right = pow = 0
    ans = 0
    while head < tail:
        left = (left * (26)) + (ord(text[head]) - 96)
        right = ((ord(text[tail]) - 96) * 26**pow) + right
        if left == right:            
           ans += (1 if head == tail else 2)
           left = right = pow =0
        else: 
            pow += 1
        head+=1
        tail-=1
    
    return ans + (1 if left != right or head == tail else 0)

    

    
print(longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
print(longestDecomposition('merchant'))
print(longestDecomposition('aaa'))
print(longestDecomposition('antaprezatepzapreanta'))
print(longestDecomposition("elvtoelvto"))