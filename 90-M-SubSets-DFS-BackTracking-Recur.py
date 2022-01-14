from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    ans = []
    def dfs(arr, cur_list):
        ans.append(cur_list)
        if not arr:
            return
        
        for i,n in enumerate(arr):
            if i > 0 and arr[i-1] == arr[i]:
                continue
            dfs(arr[i+1:], cur_list + [n])
    dfs(sorted(nums), [])
    return ans

    

    
print(subsetsWithDup([1,2,2]))
print(subsetsWithDup([0]))
print(subsetsWithDup([4,4,4,1,4]))