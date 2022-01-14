from typing import Counter, List
import collections
import math
import sys
from common import create2DArray

def knightProbability(n: int, k: int, row: int, column: int) -> float:
    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    
    def calPos(K: int, rw: int, col: int):
        if rw < 0 or rw >= n or col < 0 or col >= n:
            return 0
        if K == 0:
            return 1

        res = 0
        for move in moves:
            res += 0.125 * calPos(K-1, row + move[0], col + move[1])
        return res
    
    return calPos(k, row, column)

def dp(n: int, k: int, row: int, column: int) -> float:
    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    memo = {}
    def calPos(K: int, rw: int, col: int):
        if rw < 0 or rw >= n or col < 0 or col >= n:
            return 0
        if K == 0:
            return 1
        if (rw, col, K) in memo:
            return memo[(rw, col, K)]
        res = 0
        for move in moves:
            res += 0.125 * calPos(K-1, rw + move[0], col + move[1])
        memo[(rw,  col, K)] = res
        return res
    
    return calPos(k, row, column)
#print(dp(3, 2, 0, 0))
#print(dp(1, 0, 0, 0))
print(dp(8, 30, 6, 4))