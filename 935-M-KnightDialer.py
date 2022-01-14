from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    def __init__(self) -> None:
        self.validMoves = { 
            1: [6, 8], 
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2],
            0: [4, 6]
            }
            
    @functools.lru_cache(None)
    def dfs(self, move, n):
        if n == 1: return 1

        ret = 0
        for m in self.validMoves[move]:
            ret += self.dfs(m, n-1)
        
        return ret

    def knightDialer2(self, n: int) -> int:
        ret = 0
        for i in range(10):
            ret += self.dfs(i, n)
        return ret % (10**9+7)
    def knightDialer(self, N):
        # Neighbors maps K: starting_key -> V: list of possible destination_keys
        neighbors = {
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
        }
        current_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for _ in range(N-1):
            next_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for src_key in range(10):
                for dst_key in neighbors[src_key]:
                    next_counts[dst_key] = (next_counts[dst_key] + current_counts[src_key]) % (10**9 + 7)
            current_counts = next_counts
        return sum(current_counts) % (10**9 + 7)



sol = Solution()
#print(sol.knightDialer(1))
print(sol.knightDialer(2))
print(sol.knightDialer(3131))