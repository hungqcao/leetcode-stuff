from typing import List
import collections

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, val: int) -> None:
        if self.q:
            curMin = self.getMin()
            newMin = min(curMin, val)
        else:
            newMin = val
        self.q.append((val, newMin))
        

    def pop(self) -> None:
        val, min = self.q.pop()
        

    def top(self) -> int:
        val, min = self.q[-1]
        return val
        

    def getMin(self) -> int:
        val, min = self.q[-1]
        return min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.pop()