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

# class Solution:
#     def getAverages(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         cur_sum = 0
#         idx = 0
#         while idx < len(nums) and idx < k:
#             res.append(-1)
#             cur_sum += nums[idx]
#             idx += 1
#         cur_sum += nums[idx] if idx < len(nums) else 0
#         idx+=1
#         while idx < len(nums) and idx <= k*2:
#             cur_sum+=nums[idx]
#             idx += 1
        
#         start = 0
#         if len(res)*2 < len(nums):
#             res.append(cur_sum // (k*2 + 1))
#             while idx < len(nums):          
#                 cur_sum += nums[idx]
#                 cur_sum -= nums[start]
#                 res.append(cur_sum // (k*2 + 1))
#                 idx += 1
#                 start += 1
            
#         for i in range(len(res), len(nums)):
#             res.append(-1)
        
#         return res


# sol = Solution()
# print(sol.getAverages([7,4,3,9,1,8,5,2,6], 5))
# print(sol.getAverages([7,4,3,9,1,8,5,2,6], 4))
# print(sol.getAverages([100000], 0))
# print(sol.getAverages([71], 1))
# print(sol.getAverages([], 1))
# print(sol.getAverages([9], 1110))
# print(sol.getAverages([8], 100000))
# class Solution:
#     def minimumDeletions(self, nums: List[int]) -> int:
#         min_n = min(nums)
#         max_n = max(nums)
#         min_idx = max_idx = 0
#         for idx, n in enumerate(nums):
#             if n == min_n:
#                 min_idx = idx
#             if n == max_n:
#                 max_idx = idx
        
#         left, right = min(min_idx, max_idx), max(max_idx, min_idx)
        
#         res = 0
#         front = left + 1
#         back = len(nums) - right
#         if front > back:
#             res += back
#             res += min(front, right - left)
#         else:
#             res += front
#             res += min(back, right - left)
#         return res

# sol = Solution()
# print(sol.minimumDeletions([2,10,7,5,4,1,8,6]))
# print(sol.minimumDeletions([0,-4,19,1,8,-2,-3,5]))
# print(sol.minimumDeletions([2]))
        

class Solution:
    def __init__(self) -> None:
        self.uf = dict()
    def find(self, x):
        self.uf.setdefault(x, x)
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]
    def union(self, x, y):
        self.uf[self.find(x)] = self.find(y)

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        self.uf = dict()
        res = []
        pq = []
        graph = collections.defaultdict()
        for x,y,t in meetings:
            heapq.heappush(pq, (t, x, y))
        
        self.union(0, firstPerson)

        while pq:
            time, x, y = heapq.heappop(pq)
            if (self.find(0) == self.find(x)) or (self.find(0) == self.find(y)):
                self.union(x, y)
            while pq and pq[0][0] == time:
                time, x, y = heapq.heappop(pq)
                if (self.find(0) == self.find(x)) or (self.find(0) == self.find(y)):
                    self.union(x, y)
        for i in range(n):
            if self.find(0) == self.find(i):
                res.append(i)
        return res

sol = Solution()
#print(sol.findAllPeople(6,[[1,2,5],[2,3,8],[1,5,10]], 1))
#print(sol.findAllPeople(4,[[3,1,3],[1,2,2],[0,3,3]], 3))
#print(sol.findAllPeople(5,[[3,4,2],[1,2,1],[2,3,1]], 1))
#print(sol.findAllPeople(6,[[0,2,1],[1,3,1],[4,5,1]], 1))
#print(sol.findAllPeople(11,[[5,1,4],[0,4,18]], 1))