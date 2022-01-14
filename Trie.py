from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def setChild(self, x):
        self.children.setdefault(x, Trie())
    def getChild(self, x):
        return self.children.get(x, None)

class Solution:
    def LPM(self, prefix, numbers):

        self.root = Trie()
        # build trie
        for pre in prefix:
            node = self.root
            for c in pre:
                node.setChild(c)
                node = node.getChild(c)
            node.isEnd = True
        
        # compare each number
        def match(number, node, path):
            while number:
                cur = number[0]
                if cur in node.children:
                    path += cur
                    node = node.getChild(cur)
                    number = number[1:]
                    if node.isEnd:
                        self.res = path
                else:
                    break
            self.ans.append(self.res)
                
        self.ans = []
        for number in numbers:
            self.res = ""
            node = self.root
            match(number, node, "")
        return self.ans
        
obj = Solution()
print(obj.LPM(["213", "21358", "1234", "12"], ["21349049", "1204539492", "123490485904"]))