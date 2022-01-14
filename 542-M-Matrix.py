from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    queue = []

    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                mat[row][col] = float('inf')
            else:
                queue.append((row, col))
    
    while queue:
        size = len(queue)
        for i in range(size):
            row, col = queue.pop(0)
            for tr, tc in [(-1,0),(1,0),(0,1),(0,-1)]:
                if 0 <= tr + row < m and 0 <= tc + col < n:
                    if mat[row+tr][tc+col] == float('inf'):
                        if mat[row][col] == 0:
                            mat[row+tr][tc+col] = 1
                        else:
                            mat[row+tr][tc+col] = min(mat[row][col] + 1, mat[row+tr][tc+col])
                        queue.append((row+tr, col+tc))
                
    return mat
       
#print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
#print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print(updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]))