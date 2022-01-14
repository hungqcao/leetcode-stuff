from typing import List
import collections
import math
import sys
import os
from common import convertToTree
from common import create2DArray, __location__
import heapq
import functools
from common import TreeNode

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ret = 0
        vowels =  {'a','e','i','o','u'}
        for idx, c in enumerate(word):
            d = {}
            tmp = idx
            while tmp < len(word) and word[tmp] in vowels:  
                if word[tmp] in vowels:
                    d.setdefault(word[tmp], 0)
                    d[word[tmp]] += 1
                    if all([i in d and d[i] > 0 for i in vowels]):
                        print(word[idx:tmp+1])
                        ret += 1
                tmp += 1
        return ret       
                
    def countVowels(self, word: str) -> int:
        ret = 0
        vowels =  {'a','e','i','o','u'}
        for idx,c in enumerate(word):
            if c in vowels:
                ret += (1+len(word) - idx - 1)
                ret += (idx)
                ret += (len(word) - idx +  1)
        return ret

    def dfs(self, node, t, qualily, visited: set):
        if t > self.maxTime: return
        if node == 0:
            self.res = max(qualily, self.res)
        
        if node not in visited:
            qualily += self.values[node]
        
        if node in self.edgesDict:
            for nei, time in self.edgesDict[node]:
                self.dfs(nei, t + time, qualily, visited.union(set([node])))

            
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        self.edgesDict = {}
        self.maxTime = maxTime
        self.values = values
        for edge in edges:
            self.edgesDict.setdefault(edge[0], [])
            self.edgesDict.setdefault(edge[1], [])
            self.edgesDict[edge[0]].append([edge[1], edge[2]])
            self.edgesDict[edge[1]].append([edge[0], edge[2]])
        self.res = self.values[0]
        self.dfs(0, 0, 0, set())
        return self.res
                    
sol = Solution()
#print(sol.countVowelSubstrings("aeiouu"))
#print(sol.countVowelSubstrings("cuaieuouac"))
print(sol.countVowels("abaa"))
print(sol.countVowels("abc"))
print(sol.countVowels("noosabasboosa"))
#print(sol.maximalPathQuality([0,32,10,43], [[0,1,10],[1,2,15],[0,3,10]], 49))
#print(sol.maximalPathQuality([39,73,63,17],[[0,1,61],[1,2,13],[2,3,44],[0,3,11]],10))