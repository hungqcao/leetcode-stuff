from typing import DefaultDict, List
import collections
import math

def minJumps(arr: List[int]):
    queue, size = [(0, 1)], len(arr)
    idxes = collections.defaultdict(list)
    for i,n in enumerate(arr):
        if 0 < i < size-1:
            if arr[i-1] == n and arr[i+1] == n:
                continue
        idxes[n] += [i]
    visited = [False for i in range(size)]
    visited[0] = True
    visited_group = set()
    while queue:
        idx, level = queue.pop(0)
        for visiting_idx in [idx + 1, idx - 1]:
            if 0 <= visiting_idx < size and not visited[visiting_idx]:
                if visiting_idx == size - 1:
                    return level
                queue.append((visiting_idx, level + 1))
                visited[visiting_idx] = True
        if arr[idx] not in visited_group:
            visited_group.add(arr[idx])
            for child in idxes[arr[idx]]:
                if not visited[child]:
                    if child == size - 1:
                        return level
                    queue.append((child, level + 1))
                    visited[child] = True
        #print(queue)
    return 0


#print(minJumps([100,-23,-23,404,100,23,23,23,3,404]))
#print(minJumps([7]))
#print(minJumps([7,6,9,6,9,6,9,7]))
#print(minJumps([6,1,9]))
print(minJumps([7,7,7,7,7,7,7,7,13]))