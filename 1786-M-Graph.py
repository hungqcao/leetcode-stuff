from typing import List
import collections
import math
import itertools
import functools
import heapq

def countRestrictedPaths(n: int, edges: List[List[int]]) -> int:
    q, distance, adj = [(0, n)], {}, collections.defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    while q:
        dis, node = heapq.heappop(q)
        if node not in distance:
            distance.setdefault(node, float('inf'))
        if distance[node] > dis:
            distance[node] = dis
            for v, w in adj[node]:
                heapq.heappush(q, (dis + w, v))

    @functools.lru_cache(None)
    def dfs(src):
        if src == n: return 1  # Found a path to reach to destination
        ans = 0
        for nei, w in adj[src]:
            if distance[src] > distance[nei]:
                ans = (ans + dfs(nei)) % 1000000007
        return ans
    return dfs(1)
    
    
print(countRestrictedPaths(5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))
print(countRestrictedPaths(7, [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]))