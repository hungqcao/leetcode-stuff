from typing import List
import collections
import math
from common import create2DArray

def bfs(grid: List[List[int]]) -> int:
    size = len(grid)
    if grid[0][0] == 1 or grid[size - 1][size - 1] == 1:
        return -1
    queue = [(0, 0, 1)]
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row, col, score in queue:
        if row == size - 1 and col == size - 1:
            return score

        for mrow, mcol in moves:
            nRow, nCol = row + mrow, col + mcol
            if 0 <= nRow < size and 0 <= nCol < size and grid[nRow][nCol] == 0:
                grid[nRow][nCol] = 1
                queue.append((nRow, nCol, score + 1))
        
    return -1                

def dfs(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    score = create2DArray(-1, rows, cols)
    visited = create2DArray(False, rows, cols)
    score[0][0] = 1
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def findPath(visited, row, col, prevScore):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if visited[row][col]:
            return
        if grid[row][col] == 1:
            return
        if score[row][col] == -1:
            score[row][col] = prevScore + 1
        elif score[row][col] < prevScore + 1:
            return
        else:
            score[row][col] = min(score[row][col], prevScore + 1)

        visited[row][col] = True
        print((row, col))
        #posMoves = set([(row + move[0], col + move[1]) for move in moves])
        # if (rows - 1, cols - 1) in posMoves:
        #     findPath(visited, rows - 1, cols - 1, score[row][col])
        #     return
        # else:
        for move in moves:
            newRow, newCol = row + move[0], col + move[1]
            findPath(visited, newRow, newCol, score[row][col])
        visited[row][col] = False
    findPath(visited, 0, 0, 0)
    return score[rows-1][cols-1]



print(bfs([[1,0,0],[1,1,0],[1,1,0]]))