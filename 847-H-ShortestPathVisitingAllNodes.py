from typing import List
import collections
import math
import sys
from common import create2DArray

def bfs(graph: List[List[int]]) -> int:
    numNode = len(graph)
    all_visited = (1 << numNode) - 1
    masks = [1 << i for i in range(numNode)]
    node_visited = [set() for  i in range(numNode)]

    queue = [(i, masks[i]) for i in range(numNode)]
    score = 0
    while queue:
        count = len(queue)
        while count:
            q, visited = queue.pop(0)
            if visited == all_visited:
                return score
            for neighboor in graph[q]:
                new_visited = visited | masks[neighboor]
                print(f'{q} {bin(new_visited)}')
                if all_visited == new_visited:
                    return score + 1
                if new_visited not in node_visited[neighboor]:
                    node_visited[neighboor].add(new_visited)
                    queue.append((neighboor, new_visited))
            count -= 1
        score += 1
        
    return -1        

print(bfs([[1],[0,2,4],[1,3],[2],[1,5],[4]]))
#print(bfs([[]]))
#print(bfs([[1,2,3],[0],[0],[0]]))
#print(bfs([[1],[0,2,4],[1,3,4],[2],[1,2]]))