from typing import List
import collections
import math
import itertools
import heapq

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    q, t, adj = [(0, k)], {}, collections.defaultdict(list)
    for u,  v, w in times:
        adj[u].append((v, w))
    while q:
        time, node = heapq.heappop(q)
        if node not in t:
            t[node] = time
            for v, w in adj[node]:
                heapq.heappush(q, (time + w, v))
    return max(t.values()) if len(t) == n else -1
    
    
#print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
#print(networkDelayTime([[1,2,1]], 2, 1))
#print(networkDelayTime([[1,2,1]], 2, 2))
#print(networkDelayTime([[1,2,1],[2,3,2],[1,3,4]],3,1))
print(networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]],3,1))