from typing import List
import collections
import math
import sys
import os
from common import convertToTree
from common import create2DArray, __location__
import heapq
import functools
from common import TreeNode, ListNode

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        cur_cap = capacity
        idx = 0
        while idx < len(plants):
            water = plants[idx]
            if cur_cap >= water:
                cur_cap -= water
                res += 1
                idx += 1
            # elif cur_cap == water:
            #     res += (idx + 1) * 2
            #     cur_cap = capacity
            #     res += 1
            #     idx += 1
            else:
                res += (idx) * 2
                cur_cap = capacity
        return res

sol = Solution()
#print(sol.wateringPlants([2,2,3,3], 5))
#print(sol.wateringPlants([1,1,1,4,2,3], 4))
#print(sol.wateringPlants([7,7,7,7,7,7,7], 8))
#print(sol.wateringPlants([5,6,2,7,8,4,4,1,6,4], 10))

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.data = collections.defaultdict()
        for idx, d in enumerate(arr):
            if d not in self.data:
                self.data[d] = [0] * len(arr)
            self.data[d][idx] = 1
            for k in self.data.keys():
                if idx > 0:
                    v = self.data[k]
                    v[idx] += v[idx-1]
        # for k, v in self.data.items():
        #     for idx, n in enumerate(v):
        #         if idx > 0:
        #             v[idx] += v[idx-1]
        
        #print(self.data)

    def query(self, left: int, right: int, value: int) -> int:
        print(self.data[value])
        return self.data[value][right] - self.data[value][left-1] if left > 0 else self.data[value][right]

#rangeFreqQuery = RangeFreqQuery([33, 12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
#print(rangeFreqQuery.query(1, 2, 4))
#print(rangeFreqQuery.query(0, 11, 33))
#rangeFreqQuery = RangeFreqQuery([2,2,1,2,2,1])
#print(rangeFreqQuery.query(1, 2, 4))
#print(rangeFreqQuery.query(0, 11, 33))
print(16 << 1)