from typing import List
import collections
import math
import itertools

def longestSubstring(s: str, k: int) -> int:
    for c in set(s):
        if s.count(c) < k:
            return max([longestSubstring(subStr, k) for subStr in s.split(c)])
            
    return len(s)
            
print(longestSubstring('aaabb', 3))
print(longestSubstring('ababbc', 2))
