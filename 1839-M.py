from typing import List, Optional, Sized
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        start = 0
        ret = 0
        while start < len(word):
            counter = {}
            lastC = word[start]
            idx = start
            while idx < len(word) and lastC <= word[idx]:
                if word[idx] not in counter:
                    counter.setdefault(word[idx], 1)
                else:
                    counter[word[idx]] += 1
                lastC = word[idx]
                idx += 1
            
            if len(counter) == 5:
                ret = max(ret, idx - start)
            start = idx
        return ret

def maxEvents(arrival, duration):
    # Write your code here
    arr = []
    for idx,a in enumerate(arrival):
        arr.append([a, a + duration[idx]])
    print(arr)
    arr = sorted(arr, key=lambda x: x[1])
    start = count = 0
    for event in arr:
        if event[0] >= start:
            count += 1
            start = event[1]
    return count + 1

print(maxEvents([1,3,3,5,7], [2,2,1,2,1]))

# sol = Solution()
# print(sol.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
# print(sol.longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))
# print(sol.longestBeautifulSubstring("a"))