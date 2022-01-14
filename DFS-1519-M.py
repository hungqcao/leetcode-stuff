from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Solution:
    def dfs(self, node, parent):
        counter = collections.Counter()
        counter[ord(self.labels[node]) - ord('a')] += 1
        for nei in self.graph[node]:
            if nei != parent:
                counter += self.dfs(nei, node)
        
        self.final[node] = counter[ord(self.labels[node]) - ord('a')]
        return counter



    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.final = [0] * n
        self.graph = collections.defaultdict(list)
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.labels = labels
        self.dfs(0, None)
        #print(self.final)
        return self.final
        
sol = Solution()
sol.countSubTrees(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],"abaedcd")
sol.countSubTrees(4,[[0,1],[1,2],[0,3]],"bbbb")
sol.countSubTrees(5,[[0,1],[0,2],[1,3],[0,4]],"aabab")
sol.countSubTrees(4,[[0,2],[0,3],[1,2]],"aeed")
