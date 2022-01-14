from typing import List
import collections
import math
import functools

def removeBoxes(boxes: List[int]):
    size = len(boxes)
    @functools.lru_cache(None)
    def dfs(i, j, k):
        if i > j: return 0
        count = 0
        while i + count <= j and boxes[i] == boxes[i+count]:
            count += 1
        i2 = i + count
        res = dfs(i+count, j, 0) + (k+count)**2
        for m in range(i2, j + 1):
            if boxes[i] == boxes[m]:
                res = max(res, dfs(i2, m - 1, 0) + dfs(m, j, k + count))
        return res
    return dfs(0, size - 1, 0)


print(removeBoxes([1,3,2,2,2,3,4,3,1]))