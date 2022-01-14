from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import convertToTree
from common import ListNode, convertToTree, TreeNode
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        N = len(s)
        ranges = [(N, -1) for i in range(26)]
        for i,c in enumerate(s):
            minidx, maxidx = ranges[ord(c) - ord('a')]
            ranges[ord(c) - ord('a')] = (min(minidx, i), max(maxidx, i))
        pq = []
        for start, end in ranges:
            if (start, end) != (N, -1):
                heapq.heappush(pq, (start, end))
        
        ret = []
        while pq:
            start, end = heapq.heappop(pq)
            while pq and start <= pq[0][0] <= end:
                tmpS, tmpE = heapq.heappop(pq)
                end = max(end, tmpE)
            ret.append((start, end))
        
        #print(ret)
        return list(map(lambda x: x[1] - x[0] + 1, ret))
        




sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabels("eccbbbbdec"))