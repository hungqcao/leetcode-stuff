from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.maxSize = k
        self.size = 0
        self.data = [-1] * k
        self.front = 0
        self.rear = k-1
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size >= self.maxSize: return False
        self.data[self.front] = value
        self.front = (self.front + 1) % self.maxSize
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size >= self.maxSize: return False
        self.data[self.rear] = value
        self.rear = (self.rear - 1) % self.maxSize
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.front = (self.front - 1) % self.maxSize
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.rear = (self.rear + 1) % self.maxSize
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty(): return -1
        return self.data[(self.front - 1) % self.maxSize]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty(): return -1
        return self.data[(self.rear + 1) % self.maxSize]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.maxSize
        


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
print(obj.insertLast(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertFront(4))
print(obj.getRear())
print(obj.isFull())
print(obj.deleteLast())
print(obj.insertFront(4))
print(obj.getFront())