from typing import List, Optional
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head

    slow = fast = head
    tail = None
    while fast and fast.next:
        tail = slow
        slow = slow.next
        fast = fast.next.next
    tail.next = None
    def merge(first, second):
        cur = None
        new_Head = ListNode(0)
        cur = new_Head
        while first and second:
            if first.val > second.val:
                cur.next = ListNode(second.val)
                cur = cur.next
                second = second.next
            else:
                cur.next = ListNode(first.val)
                cur = cur.next
                first = first.next
        while first:
            cur.next = ListNode(first.val)
            cur = cur.next
            first = first.next

        while second:
            cur.next = ListNode(second.val)
            cur = cur.next
            second = second.next
        
        return new_Head.next

    left = sortList(head)
    right = sortList(slow)
    
    res = merge(left, right)
    return res
    
    
print(sortList(convertToLinkedList([4,2,1,3])))