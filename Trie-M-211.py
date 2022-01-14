from typing import List
import collections
import math
import sys
import os
import json

class WordDictionary:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def setChild(self, x):
        self.children.setdefault(x, WordDictionary())
    def getChild(self, x):
        return self.children.get(x, None)
    
    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            node.setChild(c)
            node = node.getChild(c)
        node.isEnd = True    
        
    def dfs(self, node, word):
        if node.isEnd and not word: return True

        if word[0] in node.children:
            return self.dfs(node.getChild(word[0]), word[1:])
        elif word[0] == '.':
            for k in node.children:
                if self.dfs(node.children[k], word[1:]):
                    return True
        return False

    def search(self, word: str) -> bool:
        return self.dfs(self, word)
        

wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("a")
print(wordDictionary.search("."))
print(wordDictionary.search("a"))
print(wordDictionary.search("aa"))
print(wordDictionary.search("a"))
print(wordDictionary.search(".a"))
print(wordDictionary.search("a."))