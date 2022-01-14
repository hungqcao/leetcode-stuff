from typing import List
import collections
import math
import itertools

def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    ans = 0
    queue = [(startRow, startColumn)]
    while queue and maxMove > 0:
        size = len(queue)
        maxMove -= 1
        for i in range(size):
            row, col = queue.pop(0)

            for moveR, moveC in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newR, newC = row + moveR, col + moveC
                if newR < 0 or newR >= m or newC < 0 or newC >= n:
                    ans += 1
                else:
                    queue.append((newR, newC))

    return ans % 1_000_000_007
    
print(findPaths(2, 2, 2, 0, 0))
print(findPaths(1, 3, 3, 0, 1))