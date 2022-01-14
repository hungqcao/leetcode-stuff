from typing import List
import collections
import math
import sys
import os
from common import create2DArray
import heapq

def minRefuelStopsDP(target: int, startFuel: int, stations: List[List[int]]) -> int:
    dp = [startFuel] + [0] * len(stations)
    for i in range(len(stations)):
        for t in range(i + 1)[::-1]:
            if dp[t] >= stations[i][0]:
                dp[t+1] = max(dp[t+1], dp[t] + stations[i][1])
    for t, d in enumerate(dp):
        if d >= target: return t
    return -1
def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    pq = []
    res = i = 0
    while startFuel < target:
        while i  < len(stations) and stations[i][0] <= target:
            heapq.heappush(pq, -stations[i][1])
            i += 1
        if not pq:
            return -1
        target += heapq.heappop(pq)
        res += 1
    return res

#print(minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]))
#print(minRefuelStops(1, 1, []))
#print(minRefuelStops(100, 1, [[10,100]]))
#print(minRefuelStops(999, 1000, [[5,100],[997,100],[998,100]]))
#print(minRefuelStops(100, 25, [[25,25],[50,25],[75,25]]))
#print(minRefuelStops(1000, 299, [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]))

def isAlienSorted( words: List[str], order: str) -> bool:
    orderDict = {c: i for i,c in enumerate(order)}
    characters = [[orderDict[w] for w in word] for word in words]
    print([1] <= [0, 1])
    print(all(w1 <= w2 for w1,w2 in zip(characters, characters[1:])))
    return

isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz")







