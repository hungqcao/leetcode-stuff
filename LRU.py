from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Node:

    def __init__(self, key = None, value = None, next = None, prev = None) -> None:
        self.value = value
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = dict()
        self.capacity = capacity
        self.count = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.removeNode(node)
        self.putInFront(node) 
        return node.value

    
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].value = value
            self.removeNode(self.dict[key])
            self.putInFront(self.dict[key]) 
            return
        if self.count == self.capacity:   
            self.dict.pop(self.tail.prev.key)
            self.removeNode(self.tail.prev)  
            self.count -= 1
        newNode = Node(key, value, None, None)
        self.dict[key] = newNode
        self.putInFront(newNode)
        self.count += 1


    def putInFront(self, node: Node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head        
    
    def removeNode(self, node: Node):    
        node.prev.next = node.next
        node.next.prev = node.prev
        
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))