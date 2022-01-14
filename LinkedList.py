from typing import List
import math
import sys
import os
import collections
from common import create2DArray, __location__
import json
import functools
import heapq

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
    def __str__(self) -> str:
        return str(self.val) if self.val else "x"

class Solution:
    def insert(self, head, val):
        prev = head
        tmp = head.next
        if not tmp:
            head.next = Node(val)
            return
        while tmp:
            if tmp.val > val:
                prev.next = Node(val)
                prev.next.next = tmp
                return            
            prev = tmp
            tmp = tmp.next
        prev.next = Node(val)
    def minDeletions(self, s: str) -> int:
        head = Node(None)
        for i in [1,4,6,2,10,1]:
            self.insert(head, i)
        tmp = head
        while tmp:
            print(tmp)
            tmp = tmp.next




            


sol = Solution()
sol.minDeletions("bbcebab")