from typing import List
import collections
from common import ListNode, convertToLinkedList

def rotateRight(head: ListNode, k: int) -> ListNode:
    def reverse(node):
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev

    originalHead =  head
    size = 0
    tmp = head
    while tmp:
        tmp = tmp.next
        size += 1

    k = k % size
    if k != 0:
        head = reverse(head)

        tailHead = head
        tmp = head
        while k > 1:
            tmp = tmp.next
            k -= 1
        
        separator = tmp.next
        tmp.next = None
        head = reverse(head)
        tmp = reverse(separator)

        tailHead.next = originalHead

    return head


print(rotateRight(convertToLinkedList([1, 2]), 2))