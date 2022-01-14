from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    size = len(gas)
    start, tank, total = 0, 0, 0
    for i in range(size):
        diff = gas[i] - cost[i]
        tank += diff
        total += diff
        if tank < 0:
            start = i + 1
            tank = 0
        
    return -1 if total < 0 else start

print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(canCompleteCircuit([2,3,4],[3,4,3]))
print(canCompleteCircuit([1,2,3,4,5,5,70],[2,3,4,3,9,6,2]))
print(canCompleteCircuit([2],[2]))
print(canCompleteCircuit([3,1,1],[1,2,2]))