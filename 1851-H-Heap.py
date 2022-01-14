from typing import List
import collections
import math
import functools
import heapq

def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals = sorted(intervals)
    hq = []
    res = {}
    for q in sorted(queries):    
    
    
#print(areConnected(6, 2, [[1,4],[2,5],[3,6]]))
print(areConnected(6, 0, [[4,5],[3,4],[3,2],[2,6],[1,3]]))