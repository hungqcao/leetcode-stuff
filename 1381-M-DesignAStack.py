from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class CustomStack:

    def __init__(self, maxSize: int):
        self.queue = collections.deque()
        self.max = maxSize
        self.len = 0
        self.ops = collections.deque()

    def push(self, x: int) -> None:
        if self.len < self.max:
            self.queue.appendleft(x)
            self.len += 1
        
    def pop(self) -> int:
        if self.len == 0: return -1
        self.len -= 1
        return self.queue.popleft()
        

    def increment(self, k: int, val: int) -> None:
        for i in range(self.len - 1, self.len - k - 1, -1):
            if i >= 0:
                self.queue[i] += val

    def print(self):
        print(self.queue) 
    
sol = CustomStack(3)
sol.push(1)
sol.push(2)
sol.pop()
sol.push(2)
sol.push(3)
sol.push(4)
sol.print()
sol.increment(5, 100)
sol.print()
sol.increment(2, 100)
sol.print()
sol.pop()
sol.print()
sol.pop()
sol.print()
sol.pop()
sol.pop()
sol.print()