from typing import List
import collections
import math
import sys
import os
from common import convertToTree
from common import create2DArray, __location__
import heapq
import functools
from common import TreeNode, ListNode
        

class Solution:
    def __init__(self) -> None:
        self.uf = dict()
    def find(self, x):
        self.uf.setdefault(x, x)
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]
    def union(self, x, y):
        self.uf[self.find(x)] = self.find(y)

    def dfs(self, pair, start_dict, visited: set, n, memo):
        if pair in memo:
            return memo[pair]
        visited.add(pair)
        res = []
        for s, e in start_dict[pair[1]]:
            if (s, e) not in visited:
                ret = self.dfs((s, e), start_dict, visited, n, memo)
                for t in ret:
                    res += [[pair[0], pair[1]]] + [t]
        visited.remove(pair)
        #memo[pair] = res
        print(f"{pair} - {res}")
        if not res:
            return [[pair[0], pair[1]]]
        return res


    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        start = collections.defaultdict(list)
        end = collections.defaultdict(list)
        for s, e in pairs:
            start[s].append((s, e))
        print(start)

        ret = self.dfs((11, 9), start, set(), len(pairs), collections.defaultdict(list))
        print(ret)
        # for s, e in pairs:
        #     ret = self.dfs((s, e), start, set(), [[s, e]], len(pairs), collections.defaultdict())
        #     if len(ret) == len(pairs):
        #         return ret
        return []


sol = Solution()
print(sol.validArrangement([[5,1],[4,5],[11,9],[9,4],[9,5]]))