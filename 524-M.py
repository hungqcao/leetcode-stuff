from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest = ""
        for word in dictionary:
            idx = 0
            for c in s:
                if idx < len(word) and c == word[idx]:
                    idx += 1
            if idx == len(word) and (len(word) > len(longest) or len(word) == len(longest) and word < longest):
                longest = word
        return longest

                


        
sol = Solution()
print(sol.findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
print(sol.findLongestWord("abpcplea", ["a","b","c"]))
print(sol.findLongestWord("abce", ["abc","abe"]))
