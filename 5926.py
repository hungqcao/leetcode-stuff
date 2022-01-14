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
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = collections.deque()
        for i, t in enumerate(tickets):
            queue.append((t, i))
        count = 0
        while queue:
            t, i = queue.popleft()
            t-=1
            count += 1
            if t == 0 and i == (k):
                return count
            elif t > 0:
                queue.append((t, i))
        return 0

    def reverseList(self, head: ListNode) -> ListNode:      
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:
        tmp = head
        count = 1
        beg = head
        while tmp:
            i = count
            prev = tmp
            while i > 0:
                tmp = tmp.next
                i -= 1
            if count % 2 == 0:
                oldHead = beg.next
                newNode = self.reverseList(beg.next)
                beg.next = newNode
                oldHead.next = tmp
            beg = tmp

        
                    
sol = Solution()
print(sol.timeRequiredToBuy([2, 3, 2], 2))
print(sol.timeRequiredToBuy([5, 1, 1, 1], 0))