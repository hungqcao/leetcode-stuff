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
    def checkWord(self, word: str):
        countHyphen = 0
        for i, c in enumerate(word):
            if c.isdigit(): return False
            if c == '-':
                if countHyphen > 0: return False
                countHyphen += 1
                if i == 0 or i == len(word) - 1 or not word[i-1].isalpha() or not word[i+1].isalpha():
                    return False
            if c in ('!', '.',','):
                if i != len(word) - 1: return False
        return True


    def countValidWords(self, sentence: str) -> int:
        words = list(filter(lambda _: len(_) > 0, sentence.split(' ')))
        res = []
        for w in words:
            if self.checkWord(w): 
                res.append(w)
        print(res)
        return len(res)
        
                    
sol = Solution()
#print(sol.countValidWords("cat and  dog"))
#print(sol.countValidWords("a-b-c"))
print(sol.countValidWords("8 .m t ar 6bq 2o"))
#print(sol.countValidWords("!this  1-s b8d!"))
#print(sol.countValidWords("alice and  bob are playing stone-game10"))
#print(sol.countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."))


print(".".isalpha())