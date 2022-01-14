from typing import List
import collections
import math
import itertools
import heapq

def twoCitySchedCost(costs: List[List[int]]) -> int:
    ''.rf
    N = len(costs) // 2
    cost1 = sorted(costs, key=lambda x: x[1] - x[0], reverse=True)
    return sum([_[0] for _ in cost1[:N]] + [_[1] for _ in cost1[N:]])

    

print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
print(twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))