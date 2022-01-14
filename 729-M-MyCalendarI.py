from typing import List
import collections
import math
import sys
import os
import json

class Node:
    def __init__(self, start, end, left, right) -> None:
        self.s = start
        self.e = end
        self.left = left
        self.right = right

class MyCalendar:

    def __init__(self):
        self.root = None

    def helper(self, node, start, end) -> bool:
        if node.s >= end:
            if not node.left:
                node.left = Node(start, end, None, None)
                return True
            else:
                return self.helper(node.left, start, end)
        elif node.e <= start:
            if not node.right:
                node.right = Node(start, end, None, None)
                return True
            else:
                return self.helper(node.right, start, end)
        
        return False

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end, None, None)
            return True
        else:
            return self.helper(self.root, start, end)

cal = MyCalendar()
print(cal.book(10, 20))
print(cal.book(15, 25))
print(cal.book(20, 30))