from typing import List
import collections
import math
import sys
import os
import json

class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def setChild(self, x):
        self.children.setdefault(x, Trie())
    def getChild(self, x):
        return self.children.get(x, None)
    
    def insert(self, word: str) -> None:
        node = self
        for c in word:
            node.setChild(c)
            node = node.getChild(c)
        node.isEnd = True    
        

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.getChild(c)
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.getChild(c)
        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))