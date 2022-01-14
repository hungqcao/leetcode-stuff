from typing import List
import collections
import math
import sys
import os
import json

class Node:
    def __init__(self, start, end, left, right, merged) -> None:
        self.s = start
        self.e = end
        self.left = left
        self.right = right
        self.merged = merged

class MyCalendar:

    def __init__(self):
        self.root = None

    def is_valid(self, node, start, end):
        if not node: return True
        if node.s >= end:
            return self.is_valid(node.left, start, end)
        elif node.e <= start:
            return self.is_valid(node.right, start, end)
        else:
            if node.merged: return False
            a = min(node.s, start)
            b = max(node.s, start)
            c = min(node.e, end)
            d = max(node.e, end)
            return self.is_valid(node.left, a, b) and self.is_valid(node.right, c, d)

    def helper(self, node, start, end):
        if not node:
            return Node(start, end, None, None, False)
        elif node.s >= end:
            node.left = self.helper(node.left, start, end)
        elif node.e <= start:
            node.right = self.helper(node.right, start, end)
        else:
            node.merged = True
            a = min(node.s, start)
            b = max(node.s, start)
            c = min(node.e, end)
            d = max(node.e, end)
            node.left = self.helper(node.left, a, b)
            node.right = self.helper(node.right, c, d)
            node.s = b
            node.e = c
        return node

    def book(self, start: int, end: int) -> bool:
        if not self.is_valid(self.root, start, end):
            return False
        else:
            self.root = self.helper(self.root, start, end)
            return True

cal = MyCalendar()
print(cal.book(24, 40))
print(cal.book(43, 50))
print(cal.book(27, 43))
print(cal.book(5, 21))
print(cal.book(30, 40))
print(cal.book(14, 29))
print(cal.book(3, 19))
print(cal.book(3, 14))
print(cal.book(25, 39))
print(cal.book(6, 19))