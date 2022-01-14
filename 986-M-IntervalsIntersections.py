from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        pq = []
        curInterval = [0, 0]
        ret = []
        p1 = p2 = 0
        while p1 < len(firstList) and p2 < len(secondList):
            s1, e1 = firstList[p1]
            s2, e2 = secondList[p2]
            
            if s1 <= e2 and s2 <= e1:
                ret.append([max(s1, s2), min(e1, e2)])
            
            if e1 <= e2:
                p1 += 1
            else:
                p2 += 1
        return ret

                


        
sol = Solution()
print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
print(sol.intervalIntersection([[1,3],[5,9]], []))
print(sol.intervalIntersection([], [[1,3],[5,9]]))
print(sol.intervalIntersection([[1,7]], [[3,10]]))
print(sol.intervalIntersection([[5,10]], [[3,10]]))
print(sol.intervalIntersection([[3,5],[9,20]], [[4,5],[7,10],[11,12],[14,15],[16,20]]))