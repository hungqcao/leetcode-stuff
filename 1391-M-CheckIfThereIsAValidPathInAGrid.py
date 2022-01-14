from typing import List
import collections
import math
import itertools
import heapq

def hasValidPath(grid: List[List[int]]) -> bool:
    uf = {}
    rownum = len(grid)
    colnum = len(grid[0])
    def find(x):
        uf.setdefault(x, x)
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]
    def union(x, y):
        uf[find(x)] = uf[find(y)]

    def canConnectFromLeft(row, col):
        if 0 <= col <= colnum  - 1 and 0 <= row <= rownum - 1:
            val = grid[row][col]
            return val in set([1, 4, 6])
        return False

    def canConnectFromRight(row, col):
        if 0 <= col <= colnum  - 1 and 0 <= row <= rownum - 1:
            val = grid[row][col]
            return val in set([1, 3, 5])
        return False

    def canConnectFromTop(row, col):
        if 0 <= col <= colnum  - 1 and 0 <= row <= rownum - 1:
            val = grid[row][col]
            return val in set([2, 3, 4])
        return False

    def canConnectFromBottom(row, col):
        if 0 <= col <= colnum  - 1 and 0 <= row <= rownum - 1:
            val = grid[row][col]
            return val in set([2, 5, 6])
        return False
    
    for row in range(rownum):
        for col in range(colnum):
            val = grid[row][col]
            if val == 1:
                if canConnectFromLeft(row, col - 1):
                    union((row, col - 1), (row, col))
                # if col < colnum - 1 and grid[row][col + 1] == 3 or grid[row][col + 1] == 5:
                #     union((row, col + 1), (row, col))
            elif val == 2:
                # if row > 0 and grid[row - 1][col] == 4 or grid[row-1][col] == 3:
                #     union((row - 1, col), (row, col))
                if canConnectFromBottom(row + 1, col):
                    union((row + 1, col), (row, col))
            elif val == 3:
                if canConnectFromLeft(row, col - 1):
                    union((row, col - 1), (row, col))
                if canConnectFromBottom(row + 1, col):
                    union((row + 1, col), (row, col))
            elif val == 4:
                if canConnectFromBottom(row + 1, col):
                    union((row + 1, col), (row, col))
                # if col < colnum - 1 and (grid[row][col + 1] == 2 or grid[row][col + 1] == 5 or grid[row][col+1] == 6):
                #     union((row, col + 1), (row, col))
            elif val == 5:
                if canConnectFromLeft(row, col - 1):
                    union((row, col - 1), (row, col))
                #union((row - 1, col), (row, col))
            # elif val == 6:
            #     print()
                #union((row - 1, col), (row, col))
                #union((row, col + 1), (row, col))
    
    return uf[find((0, 0))] == uf[find((len(grid) - 1, len(grid[0]) - 1))]


    
    
print(hasValidPath([[2,4,3],[6,5,2]]))
print(hasValidPath([[1,2,1],[1,2,1]]))
print(hasValidPath([[1,1,2]]))
print(hasValidPath([[1,1,1,1,1,1,3]]))
print(hasValidPath([[2],[2],[2],[2],[2],[2],[6]]))