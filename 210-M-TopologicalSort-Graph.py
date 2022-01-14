from typing import List
import collections
import math

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = {i: set() for i in range(numCourses)}
    indegrees = {i: 0 for i in range(numCourses)}
    for pre in prerequisites:
        graph[pre[1]].add(pre[0])
        indegrees[pre[0]] += 1
    
    ret = []
    nodes = collections.deque()
    for node in range(numCourses):
        if not indegrees[node]:
            nodes.append(node)
    
    while nodes:
        node = nodes.pop()
        ret.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                nodes.append(neighbor)
    if len(ret) != numCourses:
        return []
    return ret



#print(findOrder(1, []))
#print(findOrder(2, [[1,0]]))
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
#print(findOrder(3, [[1,0],[1,2],[0,1]]))

def findValid(list):
    if not list: return True
    pset = set()
    dset = set()
    for ch in list:
        if ch[0] == 'P':
            if ('D' + ch[1] in dset) or ch in pset:
                return False
            else:
                pset.add(ch)
        else:
            if 'P' + ch[1] not in pset or ch in dset:
                return False
            else:
                dset.add(ch)
    if len(pset) != len(dset):
        return False
    return True

# print(findValid(['P1', 'P2', 'D1', 'D2']))
# print(findValid(['P1', 'D1', 'P2', 'D2']))
# print(findValid(['P1', 'D2', 'D1', 'P2']))
# print(findValid(['P1', 'D2']))
# print(findValid(['P1', 'P2']))
# print(findValid(['P1', 'D1', 'D1']))
# print(findValid([]))
# print(findValid(['P1', 'P1', 'D1']))
# print(findValid(['P1', 'P1', 'D1', 'D1']))
# print(findValid(['P1', 'D1', 'P1']))
# print(findValid(['P1', 'D1', 'P1', 'D1']))