from typing import List
import collections
import math
import sys
import os
from common import convertToTree
from common import create2DArray, __location__
import heapq
import functools
from common import TreeNode

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # sort
    intervals.sort(key=lambda x:x[0])
    ans = []
    
    for arr in intervals:
        if not ans: ans.append(arr)
        else:
            peek = ans[-1]
            # separate
            if arr[0] > peek[1] + 1:
                ans.append(arr)
            elif arr[0] == peek[1] + 1:
                peek[1] = arr[1]
            elif arr[0] <= peek[1] and arr[1] >= peek[1]:
                peek[1] = arr[1]
            else:
                continue         
    return ans

def compactAndSort(rangestring):
    if not rangestring: return rangestring
    strTokens = [s.strip() for s in rangestring.split(',')]
    tokens = []
    for strToken in strTokens:
        firstNum, secondNum = [t.strip() for t in strToken.split(':')]
        tokens.append([int(firstNum), int(secondNum)])
    
    mergedTokens = merge(tokens)
    return ",".join([f'{first}:{second}' for first,second in mergedTokens])

#print(compactAndSort("6:10 , 1:5"))
                   
class Solution:
    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            for j in range(n//2):
                row[j], row[~j] = row[~j], row[j]

sol = Solution()
sol.rotate([[1,2,3],[4,5,6],[7,8,9]])