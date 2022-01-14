from typing import List
import collections
import math

def getMaximumGold(grid: List[List[int]]) -> int:
    res = 0
    M, N = len(grid), len(grid[0])
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]    

    def dfs(row, col, visited, dp: dict):
        if 0 > row or row >= M or 0 > col or col >= N: return 0
        if grid[row][col] == 0: return 0
        if (row, col) in visited: return 0     
        visited.add((row, col))
        gold = 0
        for r, c in moves:
            gold = max(gold, dfs(row + r, col + c, visited, dp))
        visited.remove((row, col))
        dp.setdefault((row, col), 0)
        dp[(row, col)] = max(dp[(row, col)], grid[row][col] + gold)
        return grid[row][col] + gold
    
    dp = collections.defaultdict()
    for r in range(M):
        for c in range(N):
            res = max(res, dfs(r, c, set(), dp))
    return res

#print(getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
#print(getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print(getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]))