from typing import List
import collections
import math

def minSwaps(grid: List[List[int]]) -> int:
    trailing = [0] * len(grid)
    M, N = len(grid), len(grid[0])
    for r in range(M):
        num0 = 0
        for c in range(N)[::-1]:            
            if grid[r][c] == 0:
                num0 += 1
            else:
                break
        trailing[r] = num0
    
    res = 0
    for i in range(M):
        target = M - i - 1
        swapIdx = i
        while swapIdx < M and trailing[swapIdx] < target:
            swapIdx += 1
        if swapIdx >= M: return -1

        swap = 0
        while swapIdx > i:
            tmp = trailing[swapIdx]
            trailing[swapIdx] = trailing[swapIdx - 1]
            trailing[swapIdx - 1] = tmp
            swapIdx -= 1
            swap += 1
        res += swap

    return res

print(minSwaps([[0,0,1],[1,1,0],[1,0,0]]))
print(minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
print(minSwaps([[1,0,0],[1,1,0],[1,1,1]]))